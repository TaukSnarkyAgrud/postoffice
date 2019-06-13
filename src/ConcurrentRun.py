import threading
import os


class ConcurrentRun:
    currentWorkspaceObject = ()
    results = []

    def __init__(self, api_key, collections_list, environments_list):
        self.api_key = api_key
        self.currentWorkspaceObject = (collections_list, environments_list)
        self.execute_each_collection_sequentially_but_concurrent_across_environments(self.currentWorkspaceObject)

    @staticmethod
    def run_command(cmd):
        os.system(cmd)

    @staticmethod
    def build_execution_phrase(output_filename, collection_uid, environment_uid, api_key):
        execute_phrase_preamble = "start /b newman run --reporters cli,json --reporter-json-export"
        execute_phrase_collection = "https://api.getpostman.com/collections/"
        execute_phrase_environment = "-e https://api.getpostman.com/environments/"
        execute_phrase_api_key = "?apikey="
        full_phrase = execute_phrase_preamble + " " + output_filename + ".json " + execute_phrase_collection + \
            collection_uid + execute_phrase_api_key + api_key + " " + execute_phrase_environment + \
            environment_uid + execute_phrase_api_key + api_key + " > " + output_filename + ".txt"
        return full_phrase

    def execute_each_collection_sequentially_but_concurrent_across_environments(self, workspace):
        collections = workspace[0]
        environments = workspace[1]

        for collection in collections:
            print("Starting a batch")
            counter = 0

            th0 = None
            th1 = None
            th2 = None

            for environment in environments:
                output_file_name = collection['name'] + "_" + environment['name']
                self.results.append(output_file_name + ".json")
                execution_phrase = self.build_execution_phrase(output_file_name, collection['uid'], environment['uid'],
                                                               self.api_key)

                if counter == 0:
                    th0 = threading.Thread(name=output_file_name, target=self.run_command(execution_phrase))
                    th0.start()
                if counter == 1:
                    th1 = threading.Thread(name=output_file_name, target=self.run_command(execution_phrase))
                    th1.start()
                if counter == 2:
                    th2 = threading.Thread(name=output_file_name, target=self.run_command(execution_phrase))
                    th2.start()
                counter += 1

            th0.join()
            th1.join()
            th2.join()
            print("Done with that batch")