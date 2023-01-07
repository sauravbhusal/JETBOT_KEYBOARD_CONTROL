#we are supposed to run this code on jupyter notebook

from jetbot import Robot
import time
import requests
robot = Robot()

while True:
    res = requests.get('ip_address_where_server_streamed_the_value')
    print ('val = ',res.text)
    
    if res.text == '8':
        robot.backward(0.2)
        
    elif res.text == '4':
        robot.left(0.2)
        
    elif res.text == '6':
        robot.right(0.2)
        
    elif res.text == '2':
        robot.forward(0.2)

    elif res.text == '1':
        robot.backward(1)
        
    elif res.text == '0':
        robot.stop()
