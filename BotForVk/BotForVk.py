
import vk_api
import bot
import traceback
from threading import Thread
from time import sleep, time
from vk_api.utils import get_random_id
 

def Update_vk(): 
    try: 
        vk_session = vk_api.VkApi('89960214009', 'Vx20192020')
        vk_session.app_id = 	6686766;
        vk_session.auth() 
        vk = vk_session.get_api() 
        while True:
            print(0) 
            posts = vk.wall.get( owner_id=-182167266,filter="suggests") #признавашки
            for x in posts.get('items'):
                id_post = x.get('id')
                print(id_post)
                message = x.get('text')
                if(isAnonim(message)): from_group = 0
                else: from_group = 1
                if not isValide(message,'alloff.txt'):
                    print("no valide!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                else:
                    attachments=x.get('attachments')
                    print(attachments)
                    vk.wall.post(post_id=id_post,owner_id=x.get('owner_id'),from_group=from_group,message=x.get('text'),signed=from_group)
            posts = vk.wall.get( owner_id=-182172014,filter="suggests")
            for x in posts.get('items'):
                id_post = x.get('id')
                print(id_post)
                message = x.get('text')
                if(isAnonim(message)): from_group = 0
                else: from_group = 1
                if not isValide(message,'matoff.txt'):
                    print("no valide!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                else:
                    attachments=x.get('attachments')
                    print(attachments)
                    vk.wall.post(post_id=id_post,owner_id=x.get('owner_id'),from_group=from_group,message=x.get('text'),signed=from_group)
               
            sleep(1800)

    except Exception as e:
        print('Ошибка:\n', traceback.format_exc())
         
        Update_vk()


variable = Thread(target=Update_vk) 
variable.start() 


def isAnonim(message):
    if message.lower().find('анон') != -1:
        print("Анонимно")
        return True;
    else:
        print("Не анонимно")
        return False;
def isValide(message,file):
    file = open(file,'r')
    text = file.read()  
    lst = text.replace(',', '').split()
    message = message.lower()
    for x in lst: 
        if  message.find(x) != -1:
            print("Есть " + x) 
            return False
          
    return True
