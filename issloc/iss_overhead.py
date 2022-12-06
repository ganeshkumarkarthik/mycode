import requests

# define base URL
url = "http://api.open-notify.org/iss-now.json"

def main():

    # Make HTTP GET request using requests, and decode
    # JSON attachment as pythonic data structure
    # Augment the base URL with a limit parameter to 1000 results
    resp = requests.get(url)
    resp = resp.json()

    print(resp)

    lon= resp["iss_position"]["latitude"]
    print(lon)

if __name__ == "__main__":
    main()   
