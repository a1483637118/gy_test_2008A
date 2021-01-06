import requests
def login():
    url = "http://mall.yansl.com:8080/admin/login"

    payload = "{\"username\":\"admin\",\"password\":\"123456\"}"
    headers = {
        'Content-Type': "application/json"
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    jsondata=response.json()
    print(jsondata)
    bear=jsondata['data']['tokenHead']
    token=jsondata['data']['token']
    print(bear)
    print(jsondata['data']['token'])
    return token

def info(token):
    url = "http://mall.yansl.com:8080/admin/info"

    payload = "{\"username\":\"admin\",\"password\":\"123456\"}"
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer "+token
        }

    response = requests.request("GET", url, data=payload, headers=headers)

    jsondata=response.json()
    print(jsondata['message'])
    return jsondata['message']
if __name__ == '__main__':
    token=login()
    message=info(token)