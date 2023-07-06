import requests

url = "https://api.bunny.net/videolibrary?page=0&perPage=1000&includeAccessKey=true"

headers = {
    "accept": "application/json",
    "AccessKey": "ca603a7e-edd1-4746-b9825356fb4a-e946-431c"
}

response = requests.get(url, headers=headers)

print(response.text)