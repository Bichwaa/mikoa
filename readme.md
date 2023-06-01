Mikoa py is a python script that scrapes Tanzania's location data from the government's official source, Napa.

we want a list of regions +
a list of districts referencing regions they belong to +
a list of wards referencing their districts +
a list of streets if available +
postcode



Instructions:
I'd package it but I am too behind on the schedule that pays me... so;
1. All packages used here are from the standard library(python 3.10) so there is no need for a virtual env 
2. To get a json of regions:

if you're on windows go


> "python regions.py" 


And If you are cool go

> "python3 regions.py"


same for districts and wards


## GitHub-repo-as-a-backend

Since it might take some time until all this data is seeded into the database, 
we could use the repo as a backend for fetching this data since all the data is now just over 1MB.

```
-rw-r--r-- 1 user group 982K 2023-06-01 17:47 wards.json
-rw-r--r-- 1 user group  73K 2023-06-01 17:53 districts.json
-rw-r--r-- 1 user group 3.3K 2023-06-01 17:55 regions.json
```
### How
* Make this repo public so that the contents can be accessed by anyone on the internet
* Inspect the raw GitHub url for each file and make a GET request from the frontend app
    ```bash
    # For instance, to fetch wards.json (requires token for private repos)

    curl https://raw.githubusercontent.com/Bichwaa/mikoa/main/wards.json
    ```
* Use helper functions in `./js/helpers.js` to process the data on the frontend