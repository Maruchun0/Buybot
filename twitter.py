import tweepy as tw

def create_headers(bearer_token):   #Creates headers for requests
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def create_url(query_field):    #Creates a API URL for requests
    url = f'https://api.twitter.com/2/tweets/search/recent?query={query_field}'
    return url

def connect_to_endpoint(url, headers):  #Connects to API URL endpoint
    response = requests.request("GET", url, headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    headers = create_headers(settings.bearer_token)
    url = create_url('from:mangadeals')
    data = connect_to_endpoint(url, headers)
    print(json.dumps(data, indent = 4, sort_keys = True))

if __name__ == '__main__':
    import json
    import settings
    import requests
    main()
