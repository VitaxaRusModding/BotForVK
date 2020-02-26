import vk_api
from threading import Thread 
from time import sleep, time
from vk_api.utils import get_random_id
import secrets;
 
print("VKNOTE") 
vk_session = vk_api.VkApi(token='08d39211a00eaf3d060372fd1076e4c3a83737dd8688a31be8f4f6663d31c232901f4adca76424dceeaf5')
vk = vk_session.get_api() 
 
confirmation_code = secrets.token_hex(16);
print(confirmation_code); 
 