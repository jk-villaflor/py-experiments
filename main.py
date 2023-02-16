from pyfacebook import GraphAPI
api = GraphAPI(app_id="546568416031478", app_secret="1c65f33cce08f5a16ddc603325af44d6", oauth_flow=True)
# authUrl = api.get_authorization_url()
# api.exchange_user_access_token(response="url redirected")

# objectId = api.get_object(object_id = "20531316728")

# print('obectId =>', objectId)

profile = api.get_object("me")
print('profile =>', profile)