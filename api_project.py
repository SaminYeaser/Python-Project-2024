import requests

def fetchRandomUser():
    url = 'https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=10'
    response = requests.get(url)
    data = response.json()
    
    if data['success'] and "data" in data:
        for i in data['data']['data']:

            userData = i['name']['first']
            print(userData)
    else:
        raise Exception('Data Can not be fetched!')

def main():
    try:
        fetchRandomUser()
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()

