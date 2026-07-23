import requests
# 1## - error   
# 2## - success
# 3## - failure
# 4## - error
# 5## - exception

api = "https://fakestoreapi.com/products"
data = requests.get(api)
print(data.json())