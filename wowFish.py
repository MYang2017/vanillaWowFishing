# -*- coding: utf-8 -*-
# above line is used to accept chinese character

# fishing wow nostalrius

## todo list
# add jump to avoid AFK
# mouse move back rework

#####################
#import Image # old command
#import ImageGrab # old command
from PIL import Image
from PIL import ImageGrab
import time
import win32api, win32con  # for click
import win32gui  # for finding centre of wow window
import random
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
import math
import os
import operator
import ctypes # set DPI resolution correctly
from scipy import signal  # correlation
# from PIL import Image
# import cv2
import pyaudio  # sound detction
import struct  # sound processing
from scipy import ndimage  # calc CoM
import scipy.fftpack  # fft
# import pyclick
#####################

#####################
fish_area_w = 350
fish_area_h = 350
bob_area_w = 20
bob_area_h = 30
colours = []
Area_colours = []
time_start = 0
time_end = 0
iffish = False
base_Crangetry = []
#####################
Xroad = [1.08, 1.09]
Feras = [0.7, 1.09]
area_sensi = Feras
#####################
# set DPI resolution correctly
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
#####################
# wowAppName = u"魔兽世界"


##################### keys
VK_CODE = {'backspace':0x08,
           'tab':0x09,
           'clear':0x0C,
           'enter':0x0D,
           'shift':0x10,
           'ctrl':0x11,
           'alt':0x12,
           'pause':0x13,
           'caps_lock':0x14,
           'esc':0x1B,
           'spacebar':0x20,
           'page_up':0x21,
           'page_down':0x22,
           'end':0x23,
           'home':0x24,
           'left_arrow':0x25,
           'up_arrow':0x26,
           'right_arrow':0x27,
           'down_arrow':0x28,
           'select':0x29,
           'print':0x2A,
           'execute':0x2B,
           'print_screen':0x2C,
           'ins':0x2D,
           'del':0x2E,
           'help':0x2F,
           '0':0x30,
           '1':0x31,
           '2':0x32,
           '3':0x33,
           '4':0x34,
           '5':0x35,
           '6':0x36,
           '7':0x37,
           '8':0x38,
           '9':0x39,
           'a':0x41,
           'b':0x42,
           'c':0x43,
           'd':0x44,
           'e':0x45,
           'f':0x46,
           'g':0x47,
           'h':0x48,
           'i':0x49,
           'j':0x4A,
           'k':0x4B,
           'l':0x4C,
           'm':0x4D,
           'n':0x4E,
           'o':0x4F,
           'p':0x50,
           'q':0x51,
           'r':0x52,
           's':0x53,
           't':0x54,
           'u':0x55,
           'v':0x56,
           'w':0x57,
           'x':0x58,
           'y':0x59,
           'z':0x5A,
           'numpad_0':0x60,
           'numpad_1':0x61,
           'numpad_2':0x62,
           'numpad_3':0x63,
           'numpad_4':0x64,
           'numpad_5':0x65,
           'numpad_6':0x66,
           'numpad_7':0x67,
           'numpad_8':0x68,
           'numpad_9':0x69,
           'multiply_key':0x6A,
           'add_key':0x6B,
           'separator_key':0x6C,
           'subtract_key':0x6D,
           'decimal_key':0x6E,
           'divide_key':0x6F,
           'F1':0x70,
           'F2':0x71,
           'F3':0x72,
           'F4':0x73,
           'F5':0x74,
           'F6':0x75,
           'F7':0x76,
           'F8':0x77,
           'F9':0x78,
           'F10':0x79,
           'F11':0x7A,
           'F12':0x7B,
           'F13':0x7C,
           'F14':0x7D,
           'F15':0x7E,
           'F16':0x7F,
           'F17':0x80,
           'F18':0x81,
           'F19':0x82,
           'F20':0x83,
           'F21':0x84,
           'F22':0x85,
           'F23':0x86,
           'F24':0x87,
           'num_lock':0x90,
           'scroll_lock':0x91,
           'left_shift':0xA0,
           'right_shift ':0xA1,
           'left_control':0xA2,
           'right_control':0xA3,
           'left_menu':0xA4,
           'right_menu':0xA5,
           'browser_back':0xA6,
           'browser_forward':0xA7,
           'browser_refresh':0xA8,
           'browser_stop':0xA9,
           'browser_search':0xAA,
           'browser_favorites':0xAB,
           'browser_start_and_home':0xAC,
           'volume_mute':0xAD,
           'volume_Down':0xAE,
           'volume_up':0xAF,
           'next_track':0xB0,
           'previous_track':0xB1,
           'stop_media':0xB2,
           'play/pause_media':0xB3,
           'start_mail':0xB4,
           'select_media':0xB5,
           'start_application_1':0xB6,
           'start_application_2':0xB7,
           'attn_key':0xF6,
           'crsel_key':0xF7,
           'exsel_key':0xF8,
           'play_key':0xFA,
           'zoom_key':0xFB,
           'clear_key':0xFE,
           '+':0xBB,
           ',':0xBC,
           '-':0xBD,
           '.':0xBE,
           '/':0xBF,
           '`':0xC0,
           ';':0xBA,
           '[':0xDB,
           '\\':0xDC,
           ']':0xDD,
           "'":0xDE,
           '`':0xC0}
def funcPressKey(keyName):
    keyString = VK_CODE[keyName]
    win32api.keybd_event(keyString, 0, 0, 0)
    anti_bot()
    win32api.keybd_event(keyString, 0, win32con.KEYEVENTF_KEYUP, 0)
    return

##################### keys finish

################################################### sound
hockSoundMin = 0.011
hockSoundMax = 0.025

FORMAT = pyaudio.paInt16
SHORT_NORMALIZE = (1.0/32768.0)
CHANNELS = 2
RATE = 44100
INPUT_BLOCK_TIME = 0.3
INPUT_FRAMES_PER_BLOCK = int(RATE*INPUT_BLOCK_TIME)


def get_rms(block):

    # RMS amplitude is defined as the square root of the
    # mean over time of the square of the amplitude.
    # so we need to convert this string of bytes into
    # a string of 16-bit samples...

    # we will get one short out for each
    # two chars in the string.
    count = len(block)/2
    format = "%dh"%(count)
    shorts = struct.unpack( format, block )

    # iterate over the block.
    sum_squares = 0.0
    for sample in shorts:
    # sample is a signed short in +/- 32768.
    # normalize it to 1.0
        n = sample * SHORT_NORMALIZE
        sum_squares += n*n

    return math.sqrt( sum_squares / count )


pa = pyaudio.PyAudio()                                 #]
                                                       #|
stream = pa.open(format = FORMAT,                      #|
         channels = CHANNELS,                          #|---- You always use this in pyaudio...
         rate = RATE,                                  #|
         input = True,                                 #|
         frames_per_buffer = INPUT_FRAMES_PER_BLOCK)   #]

###################################################
def mouse_rand():
    return 0
    #return random.randrange(-1,1)

def anti_bot():
    time.sleep( random.uniform(0.02,0.055) ) # prevent action too fast, anti anti-boot
    return

def get_mouse_posi():
    m_posi = win32api.GetCursorPos()
    #print('Got Mouse Position')
    return m_posi

def get_fish_area(m_posi,w,h):
    fish_area = (m_posi[0]-w/2, m_posi[1]-h, m_posi[0]+w/2, m_posi[1]+h/2)
    #print('Got Fish Area Coords')
    return fish_area

def image_grab(p1p2):
    im=ImageGrab.grab(bbox=p1p2) # X1,Y1,X2,Y2
    #print('Fish Area Pic Taken')
    return im

def get_colours(pic, colour = 2):
    pic_size = pic.size
    picw = pic_size[0]
    pich = pic_size[1]
    colours = [[0 for x in range(picw)] for y in range(pich)]
    for x in range(0,picw):
        for y in range(0,pich):
            colours[y][x] = pic.getpixel((x, y))[colour] # take red component
    return colours

def get_colour_range(colours):
    down = min(colours)
    up = max(colours)
    return down, up

def get_area_colour_range(m_posi):
    Crange = []
    Area_colours = []
    for tt in range(1,15):
        pic_sample = image_grab( get_fish_area(m_posi, fish_area_w, fish_area_h) )
        Crange = get_colour_range(get_colours(pic_sample))
        time.sleep(0.04)
        Area_colours.append(Crange[0])
        Area_colours.append(Crange[1])
    down = min(Area_colours)
    up = max(Area_colours)
    return down, up

def if_fishing(base, current, sensitivity):
    if current[1] >= base[1]*sensitivity:
        return True
    else:
        return False

def simpleRclick():
    mouse_posi = get_mouse_posi()
    x = mouse_posi[0]
    y = mouse_posi[1]
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)
    return

def Rclick(x,y,quickmode):
    x = x + mouse_rand()
    y = y + mouse_rand()
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
    if not quickmode:
        anti_bot()
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)
    return

def Lclick(x,y,quickmode):
    x = x + mouse_rand()
    y = y + mouse_rand()
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    if not quickmode:
        anti_bot()
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    return

def press_fish(): # press 1
    win32api.keybd_event(0x31, 0,0,0)
    anti_bot()
    win32api.keybd_event(0x31,0 ,win32con.KEYEVENTF_KEYUP ,0)
    print('throw bob')
    return

def jump(): # jump
    win32api.keybd_event(0x20, 0,0,0)
    anti_bot()
    win32api.keybd_event(0x20,0 ,win32con.KEYEVENTF_KEYUP ,0)
    return

def pressSevenEight(): # press seven
    #### this part is in wow
    # /use 新鲜的刺须鲶鱼,新鲜的石鳞鳕鱼,新鲜的银头鲑鱼,新鲜的斑点黄尾鱼,新鲜的光滑大鱼,新鲜的滑皮鲭鱼,新鲜的彩鳍鱼,新鲜的红腮鱼
    # /use 巨型蚌壳
    #### finish
    print('delete useless fish')
    win32api.keybd_event(0x35, 0, 0, 0)
    anti_bot()
    win32api.keybd_event(0x35, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(0x36, 0, 0, 0)
    anti_bot()
    win32api.keybd_event(0x36, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(0x37, 0,0,0)
    anti_bot()
    win32api.keybd_event(0x37,0 ,win32con.KEYEVENTF_KEYUP ,0)
    print('open clam')
    win32api.keybd_event(0x38, 0, 0, 0)
    anti_bot()
    win32api.keybd_event(0x38, 0, win32con.KEYEVENTF_KEYUP, 0)
    return

def useFish():
    pressSevenEight()  # use fish with macro
    time.sleep(1.5)  # wait for cool down
    jump()
    return

def hook_bob(m_posi): # hold shift + right click
    print('hook bob!')
    # win32api.keybd_event(0x10, 0,0,0) # press shift
    anti_bot()
    Rclick(m_posi[0],m_posi[1],False)
    anti_bot()
    # win32api.keybd_event(0x10,0 ,win32con.KEYEVENTF_KEYUP ,0)
    # move mouse to side to avoid highlighting bob
    anti_bot()
    x = m_posi[0] + 10*random.randint(0,9) + random.randint(0,9)
    y = m_posi[1] + random.randint(0,90)
    win32api.SetCursorPos((x,y))
    return

def hook_bob_withShift(m_posi): # hold shift + right click
    print('hook bob!')
    win32api.keybd_event(0x10, 0,0,0) # press shift
    anti_bot()
    Rclick(m_posi[0],m_posi[1],False)
    anti_bot()
    win32api.keybd_event(0x10,0 ,win32con.KEYEVENTF_KEYUP ,0)
    # move mouse to side to avoid highlighting bob
    anti_bot()
    x = m_posi[0] + 10*random.randint(0,9) + random.randint(0,9)
    y = m_posi[1] + random.randint(0,90)
    win32api.SetCursorPos((x,y))
    return

def lets_fish():
    # add jump if AFK

    # for Nostarius fishing
    mouse_posi = get_mouse_posi() # mouse should be in wow window before start
    Lclick(mouse_posi[0],mouse_posi[1],True) # get to wow window
    #Lclick(-mouse_posi[0],mouse_posi[1],True) # get to other window
    fishout = 0
    while fishout <= 3:
        if fishout != 3:
            if fishout == 0:
                base_Crange = get_area_colour_range(mouse_posi)
            #current_mouse = get_mouse_posi()
            #Lclick(mouse_posi[0],mouse_posi[1],True) # get to wow window
            press_fish()
            #Lclick(current_mouse[0],current_mouse[1],True) # get to other window
            time.sleep(2)
            fish_pic = image_grab( get_fish_area(mouse_posi, fish_area_w, fish_area_h) )
            #fish_pic.save('fish.bmp', 'bmp')
            Crange = get_colour_range(get_colours(fish_pic))
            print('envi',base_Crange[1]*area_sensi[0],'<',Crange[1])
            iffish = if_fishing(base_Crange, Crange, area_sensi[0])
            if iffish:
                print('bob stabled')
                base_fishing_Crange = get_area_colour_range(mouse_posi)
                time.sleep(2.5)
                anti_bot()
                break
            time.sleep(1)
            anti_bot()
            fishout = fishout + 1
        elif fishout == 3:
            print('failed bob')
            mouse_posi = get_mouse_posi()
            jump()
            time.sleep(6)
            fishout = -1


    time.sleep(3) # wait bob stable
    time_start = time.time()
    while True:
        fish_pic = image_grab( get_fish_area(mouse_posi, fish_area_w, fish_area_h) )
        Crange = get_colour_range(get_colours(fish_pic))
        iffished = if_fishing(base_fishing_Crange, Crange, area_sensi[1])
        print('bob',base_fishing_Crange[1]*area_sensi[1],'<',Crange[1])
        if iffished:
            #print(base_fishing_Crange,Crange)
            #current_mouse = get_mouse_posi()
            #Lclick(mouse_posi[0],mouse_posi[1],True) # get to wow window
            hook_bob(mouse_posi)
            #Lclick(current_mouse[0],current_mouse[1],True) # get to other window
            print('hooked')
            break
        time_end = time.time()
        if (time_end - time_start) > 26:
            print('no fish hooked')
            break
    return


def get_avg_background_red():
    # take a screen shoot of whole wow screen with bag open for log
    takeScreenShootOfWholeWOW()

    centrex, centrey = find_centre_coors_of_window()
    mouse_posi = [centrex, centrey]
    # mouse_posi = get_mouse_posi() # mouse should be in wow window before start
    Lclick(mouse_posi[0],mouse_posi[1],True) # get to wow window
    pic_sample = image_grab( get_fish_area(mouse_posi, fish_area_w, fish_area_h) )
    # plt.figure()
    # plt.imshow(pic_sample)
    # plt.show()
    red_pic = get_colours(pic_sample)
    avg_matrix = np.array(red_pic)
    for r in range(0,9):
        time.sleep(.2)
        pic_sample = image_grab( get_fish_area(mouse_posi, fish_area_w, fish_area_h) )
        red_pic = get_colours(pic_sample)
        matrix = np.array(red_pic)
        avg_matrix = avg_matrix + matrix
    return avg_matrix/10,mouse_posi


def get_background_red(mouse_posi):
    Lclick(mouse_posi[0],mouse_posi[1],True) # get to wow window
    pic_sample = image_grab( get_fish_area(mouse_posi, fish_area_w, fish_area_h) )
    red_pic = get_colours(pic_sample)
    return np.array(red_pic)

def find_ind_of_max_in_list(l):
    max_value = max(l)
    return l.index(max_value)

def compare_images_and_find_bob(ini_mouse_posi,background_matrix):
    time.sleep(3)
    pic_sample = image_grab( get_fish_area(ini_mouse_posi, fish_area_w, fish_area_h) )
    red_pic = get_colours(pic_sample)
    bob_pic = np.array(red_pic)
    noOfImages = 3
    print('take ' + str(noOfImages) + ' background imgs')
    for r in range(noOfImages-1):
        time.sleep(.001)
        pic_sample = image_grab( get_fish_area(ini_mouse_posi, fish_area_w, fish_area_h) )
        red_pic = get_colours(pic_sample)
        matrix = np.array(red_pic)
        bob_pic = bob_pic + matrix
    bob_pic = bob_pic/noOfImages
    diffMatrix = background_matrix-bob_pic

    # plt.figure()
    # plt.imshow(background_matrix)
    # plt.figure()
    # plt.imshow(bob_pic)
    # plt.figure()
    # plt.imshow(diffMatrix)
    # plt.colorbar()
    # plt.show()

    # sorting finding
    # toSort = np.array(abs(diffMatrix))
    # toSort = toSort.flatten()
    # sorted = np.sort(toSort)
    # bobPixInd = np.where(abs(diffMatrix) > sorted[-100])
    # print(sorted[-100])

    # plt.figure()
    # plt.plot(sorted)
    print('find bob according to high red value pix')
    bobPixInd = np.where(abs(diffMatrix) > 35)
    # print(sorted[-200],len(sorted),len(bobPixInd))
    if len(bobPixInd[0])==0: # maybe check the centre of mass of this?
        print('did not find bob, throw again')
        return False,True
    else:
        print('bob found')
        # plt.figure()
        # plt.imshow(abs(diffMatrix))
        (ys, xs) = bobPixInd
        # for x, y in zip(xs, ys):
        #     plt.scatter(x, y, s=20, alpha=.5)
        #print(find_centre_of_mass(abs(diffMatrix)))
        avx, avy = np.average(xs), np.average(ys)
        # print(avx, avy)
        # plt.scatter(avx, avy, s=50, alpha=.75, marker='x')
        # plt.show()

        return [int(avx), int(avy)], False


def convert_bob_posi_to_mouse_posi(ini_mouse_posi,bob_posi):
    return ini_mouse_posi[0] + bob_posi[0]-fish_area_w/2, ini_mouse_posi[1] + bob_posi[1]-fish_area_h

def compare_images_and_check_if_bobbed(bob_posi):
    pic_sample = image_grab( get_fish_area(bob_posi, bob_area_w, bob_area_h) )

    red_pic = get_colours(pic_sample)
    bob_pic = np.array(red_pic)

    y_CoM = ndimage.measurements.center_of_mass(bob_pic)

    return y_CoM

def grab_small_bob_window(bob_posi):
    currentTime = str(int(time.time()))

    pic_sample = image_grab(get_fish_area(bob_posi, bob_area_w, bob_area_h))
    # pic_sample.save('fishRaw_' + currentTime + '.bmp', 'bmp')
    pic_sample_RGB = np.array(pic_sample.convert('RGB'))
    red_pic = pic_sample_RGB[:, :, 0]
    # redim = Image.fromarray(red_pic)
    # redim.save('red_' + currentTime + '.bmp', 'bmp')
    green_pic = pic_sample_RGB[:, :, 1]
    # greenim = Image.fromarray(green_pic)
    # greenim.save('green_' + currentTime + '.bmp', 'bmp')
    blue_pic =pic_sample_RGB[:, :, 2]
    # blueim = Image.fromarray(blue_pic)
    # blueim.save('blue_' + currentTime + '.bmp', 'bmp')

    bob_pic = np.array(blue_pic)
    return bob_pic

def find_avg(centres):
    return len(centres)

def focusOnWOWWindow():
    hwndMain = win32gui.FindWindow(None, u"魔兽世界")
    rect = win32gui.GetWindowRect(hwndMain)
    return rect

def find_centre_coors_of_window():
    hwndMain = win32gui.FindWindow(None, u"魔兽世界")
    rect = win32gui.GetWindowRect(hwndMain)
    wow_left = rect[0]
    wow_top = rect[1]
    wow_right = rect[2]
    wow_bottom = rect[3]
    return (wow_left+wow_right)/2,(wow_top+wow_bottom)/2

def takeScreenShootOfWholeWOW():
    rect = focusOnWOWWindow()
    wow_left = rect[0]
    wow_top = rect[1]
    wow_right = rect[2]
    wow_bottom = rect[3]
    wholeWOWPic = image_grab((wow_left, wow_top, wow_right, wow_bottom))
    fileNames = getCurrentTimeAsString()
    currentDirectory = 'C:/Users/t-meya/Documents/My Games/WOW-related/fishing/log/' + fileNames[1]
    if not os.path.exists(currentDirectory):
        os.mkdir(currentDirectory)
    wholeWOWPic.save(currentDirectory + '/' + fileNames[0] + '.png', 'png')
    time.sleep(3)

def dnd():
    # entre dnd
    # press entre
    funcPressKey('enter')
    # press /
    funcPressKey('/')
    # press d
    funcPressKey('d')
    # press n
    funcPressKey('n')
    # press d
    funcPressKey('d')
    time.sleep(0.5)
    # press entre
    funcPressKey('enter')
    time.sleep(0.5)
    return

def applyLure():
    # press 3 lure
    win32api.keybd_event(0x33, 0, 0, 0)
    anti_bot()
    win32api.keybd_event(0x33, 0, win32con.KEYEVENTF_KEYUP, 0)
    # press 2 pole
    win32api.keybd_event(0x32, 0, 0, 0)
    anti_bot()
    win32api.keybd_event(0x32, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(5)
    return

def dispRatio(ratioFloat):
    if math.isnan(ratioFloat):
        ratioFloat=0
    ratio = int(ratioFloat)
    totalLength = 15
    if ratio>=totalLength:
        ratio=totalLength
    msgToDisp = '='*ratio + '|' + '='*(totalLength-ratio) + ' ' + str(ratioFloat)
    print(msgToDisp)
    return

def getCurrentTimeAsString():
    timeNow = time.localtime()
    nian = timeNow.tm_year
    yue = timeNow.tm_mon
    ri = timeNow.tm_mday
    shi = timeNow.tm_hour
    fen = timeNow.tm_min
    miao = timeNow.tm_sec
    return [str(shi) + '-' + str(fen) + '-' + str(miao), str(nian) + '-' + str(yue) + '-' + str(ri)]

def saveScreen():

    return

# for Light's Hope fishing
def smarter_lets_fish():
    BGresetNum = 0
    # get background pic
    print('get background matrix')
    background_matrix, ini_mouse_posi = get_avg_background_red()
    print('got background ')
    print('entering dnd mode')
    dnd()
    while True:  # loop for fishing
        # retake bg every X loops to accomendate environmental changes
        if BGresetNum>40:
            BGresetNum = 03
            pressSevenEight()  # clean up inventory, delete useless fish and open up clams
            time.sleep(5)
            background_matrix, ini_mouse_posi = get_avg_background_red()
        get_bob_posi = True
        print('getting bob position')
        while get_bob_posi:
            # throw bob
            press_fish()
            print('analyse and get bob coords')
            bob_posi, get_bob_posi = compare_images_and_find_bob(ini_mouse_posi,background_matrix)
        print('got bob position')

        # convert coarse coors to abs coors for bob
        bob_posi = convert_bob_posi_to_mouse_posi(ini_mouse_posi, bob_posi)
        # hover to bob
        win32api.SetCursorPos(bob_posi)

        # loop analysing to check for hook
        timeLim = 23
        y_CoM_diff = 2
        startFishTime = time.time()
        amplitude = 0
        bob_window = np.zeros((int(bob_area_h*1.5), bob_area_w))
        iterTrack = 0
        bob_window_avg = np.zeros((int(bob_area_h*1.5), bob_area_w))
        diff_avg = 0

        diffRatioThresh = 4

        y_CoMTrack = []

        # redundent = 5

        # while redundent>0:
        #     stream.read(INPUT_FRAMES_PER_BLOCK)
        #     redundent -= 1
        #
        # print('listening to hook sound')
        while time.time()-startFishTime < timeLim:
            # check if hooked
            ## sound detection
            # block = stream.read(INPUT_FRAMES_PER_BLOCK)
            # amplitude = get_rms(block)
            # print(np.round(amplitude, 5))
            ## image recognition
            bob_window_now = grab_small_bob_window(bob_posi)
            iterTrack += 1
            bob_window_avg = (bob_window_avg*(iterTrack-1) + bob_window_now)/iterTrack
            bob_window_diff = np.sum(np.sum(np.square(bob_window_now-bob_window_avg)))#/(int(bob_area_h*1.5) * bob_area_w)
            diff_avg = (diff_avg*(iterTrack-1) + bob_window_diff)/iterTrack
            # beautifully display ratio
            dispRatio(bob_window_diff/diff_avg)
            # if hockSoundMin<amplitude and hockSoundMax>amplitude:  # sound
            if (bob_window_diff/diff_avg>diffRatioThresh) and (iterTrack > 5):
                print('hooked!')
                simpleRclick()
                break
            time.sleep(0.05)

        # stay focused in WOW window
        focusOnWOWWindow()

        # win32api.keybd_event(0x1B, 0, 0, 0)  # press escape
        time.sleep(5.5)  # wait for bob to disappear
        anti_bot()

        BGresetNum += 1  # update environment count

        print('next fish')
    return

def buysomething():
    time.sleep(3)

    while True:
        # spam left click on an item
        simpleRclick()
        time.sleep(0.3)
        anti_bot()

        # spam left click on another item
        # move to another position

    return


##while True:
##    # hover mouse on wow window before start
##    lets_fish() # Nostarius
##    time.sleep(5)
##    anti_bot()
##    print('next round')

# call fishing
for i in range(9):
    print('open bag for log!')
smarter_lets_fish()

# buy something
#buysomething()
quit()
