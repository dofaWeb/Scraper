"""Extract data from website: https://thewriteconversation.blogspot.com """ 
import requests

URL = "https://thewriteconversation.blogspot.com/"
response = requests.get(URL)