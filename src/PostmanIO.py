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
            print("Working Directory changed to: " + path)
        except FileNotFoundError:
            print("Path not Found")

    def create_log_file(self):
        my_directory = os.path.join(os.getcwd(), datetime.datetime.now().strftime('%d-%m-%Y_%H-%M'))
        os.makedirs(my_directory)
        print("Directory Created: " + my_directory)
        self.change_working_directory(my_directory)
        return my_directory

    def extract_current_contracts(self):
        contract_current = []

        for request in self.content['item'][0]['item'][0]['item']:
            contract_current.append({"name": request['name'], "body": request['event'][0]['script']['exec']})
        for request in self.content['item'][0]['item'][1]['item']:
            contract_current.append({"name": request['name'], "body": request['event'][0]['script']['exec']})
        for request in contract_current:
            print(request)
        self.export_to_json(self.content, "contractsCurrent.json")

    def recurse_and_update_remove_xperfectserveidentity(self, general_object):
        if 'item' in general_object.keys():
            for row in general_object['item']:
                self.recurse_and_update_remove_xperfectserveidentity(row)
        else:
            if not any(
                    word in general_object['request']['url']['raw'] for word in ["entityMap", "swagger",
                                                                                 "identityLoginUrl"]):
                for header in general_object['request']['header']:
                    if 'x-perfectserve-identity' in header['key']:
                        general_object['request']['header'][:] = [d for d in general_object['request']['header']
                                                                  if d.get('key') != 'x-perfectserve-identity']