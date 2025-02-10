from xmlrpc.client import Boolean

import requests


#GET
user_input = input("ID gir ")
get_url=f"https://jsonplaceholder.typicode.com/todos{user_input}"   #url sonuna /1 yazarsak ilk veriyi getirir. Örn: /5 yazarsak 5.veriyi getirir. İstersek kullanıcının istediğini de getiririz

get_response = requests.get(get_url)
print(get_response.json())


#POST
to_do_item = {'userId': 2, 'title': 'my to do', 'completed': False}
post_url="https://jsonplaceholder.typicode.com/todos"
#optional header
headers={"Content-Type" : "application/json"} #veri ile birlikte ek bilgiler gönderili headers ile
post_response = requests.post(post_url, json=to_do_item, headers=headers) #post_url ile hangi veri üzerinde işlem yapılacağını belirttik. to do item değişkeni ile de eklenecek bilgiler json olarak verilir. Buradan gelen cevap eklenip eklenmediğine dair post_response ye kaydedilir
print(post_response.json()) #json şeklinde istemezsek sadece eklendiğine dair mesaj verir. Nasıl v ene eklendiğini göstermez


