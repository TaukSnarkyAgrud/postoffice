from src.ConcurrentRun import ConcurrentRun
from src.PAPI import PAPI
from src.PostmanIO import PostmanIO


def main():
    import_pm_api_key = PostmanIO()
    import_pm_api_key.import_from_json("../auth/keys.json")
    api_key = import_pm_api_key.content["postmanAPI"]
    print("API Key Found: " + api_key)
    import_pm_api_key = None
    papi = PAPI(api_key)

    conner = ConcurrentRun(api_key, )

if __name__ == "__main__":
    main()
