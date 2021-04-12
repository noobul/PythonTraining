import json

class JasonHandler:
    def __init__(self, file_name):
        self.file_name = file_name

    def add_to_json(self, prompt,  message):
        """ads info to specifie json file and prints message"""
        info = input(prompt)
        with open(self.file_name, 'w') as f:
            json.dump(info, f)
        print(f"{message} {info}")
        return info

    def read_from_json(self, message):
        """Reads info from specifi json file and prints message"""
        with open(self.file_name) as f:
            info = json.load(f)
        print(f"{message} {info}")