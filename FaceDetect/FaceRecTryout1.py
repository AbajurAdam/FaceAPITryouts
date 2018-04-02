import http.client
import urllib.request
import urllib.parse
import urllib.error
import base64
import requests
import json

subscription_key = '915abf3a916249adb70b0818d85025ee'


base_url = 'https://eastasia.api.cognitive.microsoft.com'

headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key,
}
params = {
    'returnFaceAttributes': 'emotion'
}
body = {'url': 'https://raw.githubusercontent.com/AbajurAdam/firstBlogDjango/master/a12.jpeg'}
try:
    # Execute the REST API call and get the response.
    response = requests.request('POST', base_url + '/face/v1.0/detect',
                                json=body, data=None, headers=headers, params=params)

    print('Response:')
    parsed = json.loads(response.text)
    info = (json.dumps(parsed, sort_keys=True, indent=2))
    print(info)
# Olley be tanıdı be :D
except Exception as e:
    print('Error:')
    print(e)
