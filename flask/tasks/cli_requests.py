# If you need to do some debugging of your API or tests are failing
#   and you are have issues debugging there, you can write little functions
#   using the third-party requests library for Python. You can install this to
#   your virtual environment with:
#       pip install requests
import requests

# You can also use the command line tool CURL to make requests to your API.
#   Curl is available on MacOS by default and Windows Powershell should have it built in as well.
#   This curl command below is the equivalent of the post_api_request() function.
# curl --header "Content-Type: application/json" --request POST --data '{"description":"Json POST"}' http://localhost:8000/api/tasks/

def post_api_request():
    print("POST")
    r = requests.post('http://127.0.0.1:8000/api/v1/tasks/', json={"description": "Too much info Prof!!"})
    print(f"Response Code: {r.status_code}")
    print(f"Response Content: {r.json()}")

def get_api_request():
    print("GET")
    r = requests.get('http://127.0.0.1:8000/api/v1/tasks/')
    print(f"Response Code: {r.status_code}")
    print(f"Response Content: {r.json()}")

def put_api_request():
    print("PUT")
    r = requests.put('http://127.0.0.1:8000/api/v1/tasks/1/', json={"description": "Updated Task!"})
    print(f"Response Code: {r.status_code}")
    print(f"Response Content: {r.json()}")

def delete_api_request():
    print("DElETE")
    r = requests.put('http://127.0.0.1:8000/api/v1/tasks/1/', json={"description": "Updated Task!"})
    print(f"Response Code: {r.status_code}")
    print(f"Response Content: {r.json()}")

def main():
    post_api_request()
    get_api_request()
    put_api_request()
    delete_api_request()

if __name__ == "__main__":
    main()
