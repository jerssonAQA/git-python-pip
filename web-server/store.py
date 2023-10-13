import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code) #estado de esa solicitud
    print(r.text)        #imprime la info en formato text
    print(type(r.text))  #imprime el tipo de datos
    categories = r.json()
    for category in categories:
        print(category['name'])

