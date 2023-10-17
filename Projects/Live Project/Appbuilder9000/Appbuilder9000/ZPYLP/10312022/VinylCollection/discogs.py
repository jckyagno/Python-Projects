# -------- DISCOGS API LOGIC BELOW ----------v
import requests

# my user token to access discogs API
DISCOGS_TOKEN = "DBiUmQgyHHBGmXsybviPrgmVVSJmMDdhpxBAGwle"

# uses catalog number to pull release info via discogs api
# and returns it as json
def get_discogs_data(cat_number):
    discogs_data = discogs_request(cat_number)
    discogs_data_as_json = discogs_data.json()
    release_json = discogs_data_as_json['results'][0]
    return release_json

# returns the api request from discogs
def discogs_request(cat_number):
    url = discogs_url(cat_number, DISCOGS_TOKEN)
    return requests.get(url)

# assembles and returns url for discogs request using the
# catalog number and user token
def discogs_url(cat_number, token):
    url = "https://api.discogs.com/database/search?q=" \
          + cat_number + "&token=" + token
    return url