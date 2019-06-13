import re


class PostmanOrganizer:

    def __init__(self, path_json_collection):
        with open(path_json_collection, "r") as fin:
            self.content = fin.read()
            self.pattern = re.compile(r'pm\.environment\.set\("(.+)"')
            self.find_floaters()

    def find_floaters(self):
        list_vars = []
        list_varss = []
        list_vars.extend(re.findall(r'pm\.environment\.set\(\\"(.+)\\"', self.content))
        list_vars_sub = re.findall(r'pm\.environment\.unset\(\\"(.+)\\"', self.content)

        for item in list_vars:
            if "Telem" not in item:
                list_varss.append(item)
        list_vars = list_varss
        list_varss = []
        for item in list_vars_sub:
            if "Telem" not in item:
                list_varss.append(item)
        list_vars_sub = list_varss

        floaters = [item for item in list_vars if item not in list_vars_sub]
        # print list_vars
        # print list_vars_sub

    def process_header_remove_xperfectserveidentity(self):
            self.recurse_and_update_remove_xperfectserveidentity(self.content)
            self.export_to_json(self.content)

    def process_contracts_update(self):
            self.extract_current_contracts()

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
