import requests

url = 'http://127.0.0.1:8000/upload/'
files = {'file': ('img.png', open('../img.png', 'rb'),'type=image/png')}
headers = {
    'accept': 'application/json; charset=utf-8',
    'Content-Type': 'multipart/form-data',
    'Cookie' : 'csrftoken=PTEZBoZ9SIgEeiyRFfwoVSJ3eS7VxcKh'

}

response = requests.post(url, headers=headers, files=files)
print(response.text)
