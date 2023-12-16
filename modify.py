import requests

data = {
    "name": "user1",
    "name1": "user1",
    "ok": "1",
    "name3": "",
    "password": "1234",
    "password1": "1234"
}

res = requests.post("https://www.instiz.net/popup_thome_info_ing.htm", data=data, cookies={"INSTIZID": "SESSION"})
print(res.text)