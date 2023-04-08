import requests

BASE = "http://127.0.0.1:5000/"

# data = [{"name": "Hag", "views": 20000, "likes": 3000}, {"name": "Wraith", "views": 8000, "likes": 9000}, {"name": "Trapper", "views": 90000, "likes": 100000}, {"name": "Legion", "views": 60000, "likes": 78964}]


# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i), data[i])
#     print(response.json())

# response = requests.get(BASE + "video/8")
# print(response.json())

patch_response = requests.patch(BASE + "video/1", {"views": 2347, "likes": "3457"})
print(patch_response.json())