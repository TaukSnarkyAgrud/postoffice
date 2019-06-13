from src.ConcurrentRun import ConcurrentRun
from src.PostmanIO import PostmanIO



def main():
    api_key = "dcc58ac7a9bf4e339b58deb82f39d443"
    collections = [
        {
            "id": "5a155e3c-b110-4654-9712-ad8df16bead4",
            "name": "Identity",
            "uid": "6382182-5a155e3c-b110-4654-9712-ad8df16bead4"
        },
        {
            "id": "598d221b-0c04-439e-a3e1-1726b857d81a",
            "name": "ScheduleSync",
            "uid": "6382182-598d221b-0c04-439e-a3e1-1726b857d81a"
        },
        {
            "id": "4569935e-6f5b-4807-87af-a7e854d3902f",
            "name": "Messaging",
            "uid": "6382185-4569935e-6f5b-4807-87af-a7e854d3902f"
        },
        {
            "id": "378d7197-a567-4e94-bf24-a1fad2ec2a12",
            "name": "CSP",
            "uid": "229020-378d7197-a567-4e94-bf24-a1fad2ec2a12"
        },
        {
            "id": "4bab333c-9d4b-42a4-b12c-aa52f2e1cfa8",
            "name": "Practitioner API",
            "uid": "6382182-4bab333c-9d4b-42a4-b12c-aa52f2e1cfa8"
        },
        {
            "id": "5acb5dcc-4465-4ea1-954a-82fb73055562",
            "name": "MQTT",
            "uid": "4690258-5acb5dcc-4465-4ea1-954a-82fb73055562"
        },
        {
            "id": "9cfbc26a-8931-4838-bba0-5f22ef8c15a3",
            "name": "Care Team API",
            "uid": "4690258-9cfbc26a-8931-4838-bba0-5f22ef8c15a3"
        },
        {
            "id": "81472f00-c197-48b9-9020-9d8495055ae1",
            "name": "EMR Link",
            "uid": "4690258-81472f00-c197-48b9-9020-9d8495055ae1"
        },
        {
            "id": "c1bf89a5-ca6b-4755-ada3-1e940ea8c734",
            "name": "System API",
            "uid": "4213740-c1bf89a5-ca6b-4755-ada3-1e940ea8c734"
        },
        {
            "id": "2e49498f-a2d9-462e-866c-0309b84f33a0",
            "name": "Alerts",
            "uid": "6382185-2e49498f-a2d9-462e-866c-0309b84f33a0"
        },
        {
            "id": "fde3a6f3-74d7-44fe-a586-8a9bb0410a4f",
            "name": "Licensing",
            "uid": "6382185-fde3a6f3-74d7-44fe-a586-8a9bb0410a4f"
        },
        {
            "id": "ae91bca3-df8a-4abb-8d3e-96ddbc952787",
            "name": "Assignments",
            "uid": "6382185-ae91bca3-df8a-4abb-8d3e-96ddbc952787"
        }
    ]
    environments = [
        {
            "id": "1f23b0cf-a42f-42d3-912f-0ae07524ef0a",
            "name": "Dev",
            "uid": "6382182-1f23b0cf-a42f-42d3-912f-0ae07524ef0a"
        },
        {
            "id": "1cf7dff2-8f90-44cc-8d41-fc4d043a0da5",
            "name": "QA",
            "uid": "6382182-1cf7dff2-8f90-44cc-8d41-fc4d043a0da5"
        },
        {
            "id": "0967e692-1919-43c7-910e-46137598aca6",
            "name": "Staging",
            "uid": "6382182-0967e692-1919-43c7-910e-46137598aca6"
        }
    ]

    path = PostmanIO()
    print(path.log_path)


if __name__ == "__main__":
    main()
