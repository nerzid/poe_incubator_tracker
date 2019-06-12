import requests

# base urls
from incubator import Incubator


base_url = "https://www.pathofexile.com/"
base_inventory_url = "character-window/get-items"

# params for requesting url
param_account_name = "accountName"
param_character = "character"
param_realm = "realm"

# character info to use in params
account_name = ""
realm = ""
character = ""

inventory = None

def set_param_values(account_name_val, realm_val, character_val):
    global account_name
    global realm
    global character
    account_name = account_name_val
    realm = realm_val
    character = character_val


def get_inventory_url():
    return base_url + base_inventory_url + "?" + param_account_name + "=" + account_name + "&" + param_realm + "=" + realm + "&" + param_character + "=" + character


def set_inventory():
    global inventory
    inventory = requests.get(get_inventory_url()).json()


def get_incubated_items():
    set_inventory()
    incubators = []
    if inventory:
        for item in inventory["items"]:
            if "incubatedItem" in item:
                item_name = item["name"]
                item_type = list(item["category"].items())[0][1][0]
                incubator_properties = item["incubatedItem"]
                incubators.append(Incubator(name=incubator_properties["name"],
                                            level=incubator_properties["level"],
                                            progress=incubator_properties["progress"],
                                            total=incubator_properties["total"],
                                            incubated_on=item_name,
                                            incubated_on_type=item_type))
    return incubators


def print_incubators():
    incubated_items = get_incubated_items()
    for incubated_item in incubated_items:
        print("Incubated On: " + incubated_item.incubated_on + "(" + incubated_item.incubated_on_type + ")")
        print("Name: " + incubated_item.name)
        print("Level: " + str(incubated_item.level))
        print("Status: " + str(incubated_item.progress) + "/" + str(incubated_item.total))

def get_pretty_incubators():
    incubated_items = get_incubated_items()
    result = ""
    for incubated_item in incubated_items:
        result += incubated_item.incubated_on + "(" + incubated_item.incubated_on_type + ") => "
        result += incubated_item.name
        result += " " + str(incubated_item.progress) + "/" + str(incubated_item.total)
        result += "\n"
    return result

if __name__ == '__main__':
    print(get_pretty_incubators())