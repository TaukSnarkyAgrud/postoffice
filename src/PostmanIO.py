import json
import os
import datetime


class PostmanIO:
    def __init__(self):
        self.content = None

    def import_from_json(self, path):
        with open(path, "r") as fin:
            self.content = json.load(fin)

    @staticmethod
    def export_to_json(content):
        # generate pathname
        pathname = content['info']['name'] + ".postman_collection.json"

        # export to file
        with open(pathname, "w+") as fout:
            json.dump(content, fout, sort_keys=False, indent=4)

    @staticmethod
    def export_to_json(content, path):
        # generate pathname
        pathname = path

        # export to file
        with open(pathname, "w+") as fout:
            json.dump(content, fout, sort_keys=False, indent=4)

    @staticmethod
    def change_working_directory(path):
        try:
            os.chdir(path)
            print("Working directory has been changed to: " + path)
        except OSError:
            print("Can't change the Current Working Directory")

    def create_log_file(self):
        self.change_working_directory(os.path.join(os.getcwd(), "../LogFiles"))
        my_directory = os.path.join(os.getcwd(), datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
        os.makedirs(my_directory)
        self.change_working_directory(my_directory)
        return my_directory


