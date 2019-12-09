import boto3, yaml, time

class Singleton(type):
    """
    Define an Instance operation that lets clients access its unique
    instance.
    """

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class ResumeData(metaclass=Singleton):
    def __init__(self):
        self.s3 = boto3.client('s3')
        self.resume_data = None
        self.resume_hash = None
        self.next_pull = time.time()
        self.poll_rate = 60 * 15


    def get_resume_data(self):
        if time.time() < self.next_pull and self.resume_data != None:
            return self.resume_data
        if self.resume_data == None and time.time() > self.next_pull:
            resp = self.s3.get_object(Bucket='rails-resume', Key='resume_data_staging_public.yml')
            data = yaml.load(resp['Body'])
            self.resume_data = data
            self.next_pull = time.time() + self.poll_rate
        return self.resume_data
