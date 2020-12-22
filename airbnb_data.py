import airbnb
from config import airbnb_username, airbnb_password

api = airbnb.Api(airbnb_username, airbnb_password)
api = airbnb.Api(access_token="ACCESS_TOKEN_OBTAINED_ON_LOGIN")
api.get_profile()