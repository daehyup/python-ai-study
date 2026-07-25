import requests

def get_example():
    response = requests.get("https://google.com")

    print(response.status_code)
    print(response.text)

if __name__ == "__main__":
    get_example()