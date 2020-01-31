# gw2-item-quantity-checker
Check the quantity of any given item in your materials storage from your command line.

## Pre-requisites

1. Must have [Python3]() installed ([Windows 10](https://www.youtube.com/watch?v=V_ACbv4329E) | [MacOS](https://programwithus.com/learn-to-code/install-python3-mac/) | [Ubuntu/Linux](http://ubuntuhandbook.org/index.php/2017/07/install-python-3-6-1-in-ubuntu-16-04-lts/))
2. Must have [PIP3]() installed
3. Ensure `python3` and `pip3` are set in your PATH environment variable
4. Install [requests]() via `PIP3`

open command line and paste the command below
   ```bash
    pip3 install requests
   ```

## How to install and Run

1. Click `Clone or download` (large green button on the right of the near top of the page)
2. Clicks `Download ZIP` (or clone it with GIT)
3. Extract the ZIP folder to anywhere on your computer (Documents is recommended for Windows or your HOME directory for MacOS or Linux)
4. Open your terminal or command line
5. Change your active directory to this folder
6. Create your `config.json` file (see below)
7. Execute the program with this command

```bash
python3 gw2_item_checker.py
```

You can run this program by just retyping the command above or hitting the `up` arrow on your keyboard. 


## Set up your config.json file

Config template
```
{
    "api_key":"<API_KEY>",
    "api_base_url":"https://api.guildwars2.com/",
    "endpoints":{
        "items":"v2/items",
        "account-materials":"v2/account/materials"
    },
    "tracked_materials":[
        // REPLACE THESE VALUES WITH THE ITEM IDs YOU WANT TO TRACK || COMMA SEPARATED
        86977,86069,87645,88955,89537,90783 
    ]
}
```
Simply replace the `<API_KEY>` placeholder with your [GuildWars2 API Key](https://account.arena.net/applications) ([?](https://wiki.guildwars2.com/wiki/API:API_key))


## Add, Remove, or Edit the Items to Be Tracked

In your `config.json` file there is an object that defines the item IDs of the items you want to track from your material storage. You will need to edit this list of IDs in order to add, remove, or edit the items displayed on the command line.

**From `config.json` file**
```
"tracked_materials":[
        86977,86069,87645,88955,89537,90783 
    ]
```

The default items are all the Living World Season 4 currencies (trying to get that Skyscale!).

You can get the item ID of any material by clicking the **API** link in the right-hand panel on any item page in the [Guild Wars 2 WIKI](https://wiki.guildwars2.com/).

**For example**, if we look at the [Jute Scrap](https://wiki.guildwars2.com/wiki/Jute_Scrap) item and click the API link, we will see that the Item ID for this item is `19718`.

Find the items you want to track and add the ID to this list!

