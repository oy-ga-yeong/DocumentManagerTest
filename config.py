import yaml

class Config:
    def __init__(self, path='auth.yaml'):
        with open(path, 'r') as f:
            data = yaml.safe_load(f)
        self.url = data['url']
        self.token = data['token']
        self.space = data['space'] 