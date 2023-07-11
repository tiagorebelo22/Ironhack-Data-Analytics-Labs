import requests
from slugify import slugify
path = "wikipedia"

def index_page(url):
    try:
        response = requests.get(url)
        f = open(path+'/'+slugify(url)+'.html','w')
        f.write(response.text)
        f.close()
    except:
        print("Error: ",url)
        pass