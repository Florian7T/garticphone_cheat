from PIL import Image
import numpy as np
import win32api, win32con,time,os

window = (820,330)
bar_y = 968
bar_x = 1245
bar_width = 215

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def draw(i:int,x:int,y:int):

    global last_color
    if i < 240:
        if last_color != i:
            last_color = i
            click(1460-int(i*(215/255)), 968)
        click(x, y)
    #elif i < 200:                      # < white niet nodig
    #    pyautogui.click(660, 470)
    #    pyautogui.click(x, y)
        #return colors['white']

if __name__ == "__main__":
    global last_color
    last_color = 999
    file_name = 'aaa'
    for file in os.listdir(os.path.dirname(os.path.realpath(__file__))):
        if '.jpg' in file or '.png' in file:
            file_name = file
            break
    if file_name == 'aaa':
        #print('No file to draw: .jpg .png')
        exit(0)
    #print(f'Drawing {file_name}...')
    img = Image.open(file_name).convert('LA')
    im_resized = img.resize((int(960/4),int(530/4)), Image.ANTIALIAS)
    im_resized.save('greyscale.png')
    img = Image.open('greyscale.png')
    array = np.array(img)


    _x=window[0]
    _y=window[1]

    for y in np.int_(array):
        for x in y:
            time.sleep(0.002)
            draw(x[0],_x,_y)
            _x+=4
        _x = window [0]
        _y+=4

    os.remove('greyscale.png')
    os.remove(file_name)               # <- useful
