pip install google-maps-reviews

from google_maps_reviews import ReviewsClient

client = ReviewsClient(api_key='SECRET_API_KEY')



# Get reviews from many places found by search query
results = client.get_reviews('Memphis Seoul brooklyn usa', reviewsLimit=10, limit=10, language='en')

# Get reviews from the place by google id
results = client.get_reviews('0x89c258faf553cfad:0x8e9cfc7444d8f876', reviewsLimit=20, language='en')

# Get reviews from the place by URL
results = client.get_reviews('https://www.google.com/maps/place/Trump+Tower/@40.7608106,-73.983412,15z/data=!3m1!5s0x89c259a1e735d943:0xb63f84c661f84258!4m9!1m2!2m1!1sTrump+Tower!3m5!1s0x89c258faf553cfad:0x8e9cfc7444d8f876!8m2!3d40.7624284!4d-73.973794!15sCgtUcnVtcCBUb3dlcloNIgt0cnVtcCB0b3dlcpIBCGxhbmRtYXJr', reviewsLimit=20, language='en')

# Get only new reviews during last 24 hours
from datetime import datetime, timedelta
yesterday_timestamp = int((datetime.now() - timedelta(1)).timestamp())

results = client.get_reviews(
    '0x89c258faf553cfad:0x8e9cfc7444d8f876', sort='newest', cutoff=yesterday_timestamp, reviewsLimit=100, language='en')

import random

#local attach value is always set to false when just attaching the depatchemnt of these feature
#npm/cache

client_side = True
curl -X GET "https://api.app.outscraper.com/maps/search-v2?query=restaurants%2C%20Manhattan%2C%20NY%2C%20USA&limit=3&async=false" -H  "X-API-KEY: YOUR-API-KEY"
local value = set.api.value
loadstring(value.Set(HttpGet"https://api.app.outscraper.com/maps/search-v2?query=resturantsds"))()
pip.scrape.value = False
val = pip.scrape.value
if val.domains_service == "truevalue":
    
