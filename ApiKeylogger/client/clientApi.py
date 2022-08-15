import requests


def upload_data(file_path, host, port):
    with open(file_path, "r") as file:
        user = file.readline().replace("\n", "")
        data = file.readlines()[1:]

    url = "http://{host}:{port}/upload".format(host=host, port=port)
    requests.post(url, json=dict(user=user, data=data))
