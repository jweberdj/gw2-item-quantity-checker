import requests, json, os

CONFIG = json.loads(open(os.fsencode('config.json')).read())

endpoints = CONFIG['endpoints']
tracked_items = CONFIG['tracked_materials']
api_key = CONFIG['api_key']

def fetch_endpoint(endpoint, data=None, params=None, headers=None):
    url = "{}{}".format(CONFIG['api_base_url'], endpoint)
    print("INFO: Querying {}".format(url))
    try:
        response = requests.get(url, data=data, params=params, headers=headers)

        if response.status_code != 200:
            response.raise_for_status()    
    except Exception as e:
        print("CRITICAL ERROR: {}".format(e))
    else:
        return json.loads(response.text)

def pretty_print(stuff):
    for thing in stuff:
        print("\n{sep}".format(sep="*"*50))
        print("Item Name: {}".format(thing['item_name']))
        print("Account QTY: {}\n".format(thing['account_qty']))

def main():
    request_data = {
        "access_token": api_key
    }
    params_string = ''
    count = 0
    for item in tracked_items:
        if count == len(tracked_items)-1:
            params_string += str(item)
        else:
            params_string += "{},".format(item)
        count += 1

    params = {
        "ids": params_string
    }
    account_materials = [item for item in fetch_endpoint(endpoints['account-materials'], data=request_data) if item['id'] in tracked_items]
    item_details = [item for item in fetch_endpoint(endpoints['items'], data=request_data, params=params)]
    
    materials = []

    for item in item_details:
        for mat in account_materials:
            if mat['id'] == item['id']:
                materials.append({
                    "item_name": item['name'],
                    "account_qty": mat['count']
                })

    pretty_print(materials)



if __name__ == "__main__":
    main()



