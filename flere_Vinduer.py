import PySimpleGUI as sg
from PIL import Image   
from random import randint
import io
def get_img_data(f, maxsize=(1200, 850)):
    """
    Generate image data using PIL
    """
    img = Image.open(f)
    img.thumbnail(maxsize)
    bio = io.BytesIO()
    img.save(bio, format="PNG")
    del img
    return bio.getvalue()
 
# Design pattern 2 - First window remains active

img_Iron_Sword = get_img_data('Iron_Sword.png')
img_Iron_Axe = get_img_data('Iron_Axe.png')
img_Iron_Pickaxe = get_img_data('Iron_Pickaxe.png')
img_Bread = get_img_data('Bread.png')
img_Box = get_img_data('Box.png')
img_Oak_Planks = get_img_data('Oak_Planks.png')
img_Iron_Shovel = get_img_data('Iron_Shovel.png')
img_Stone_Bricks = get_img_data('Stone_Bricks.png')
img_Diamond_Sword = get_img_data('Diamond_Sword.png')
img_Spruce_Planks = get_img_data('Spruce_Planks.png')
img_Steve = get_img_data('Steve.png')

inventory= []

items = {
    'Iron_Pickaxe' : img_Iron_Pickaxe,
    'Iron_Sword' : img_Iron_Sword,
    'Iron_Axe' : img_Iron_Axe,
    'Iron_Shovel' : img_Iron_Shovel,
    'Bread' : img_Bread,
    'Oak_Planks' : img_Oak_Planks,
    'Stone_Bricks' : img_Stone_Bricks,
    'Diamond_Sword' : img_Diamond_Sword,
    'Spruce_Planks' : img_Spruce_Planks
}


box = {
    'inv_1': False,
    'inv_2': False,
    'inv_3': False,
    'inv_4': False,
    'inv_5': False,
    'inv_6': False,
    'inv_7': False,
    'inv_8': False,
    'inv_9': False,
    'inv_10': False,
    'inv_11': False,
    'inv_12': False,
    'inv_13': False,
    'inv_14': False,
    'inv_15': False,
    'inv_16': False,
    'inv_17': False,
    'inv_18': False,
    'inv_19': False,
    'inv_20': False,
    'inv_21': False,
    'inv_22': False,
    'inv_23': False,
    'inv_24': False,
    'inv_25': False,
    'inv_26': False,
    'inv_27': False,
    'inv_28': False,
    'inv_29': False,
    'inv_30': False,
    'inv_31': False,
    'inv_32': False,
    'inv_33': False,
    'inv_34': False,
    'inv_35': False,
    'inv_36': False,
    'inv_37': False,
    'inv_38': False,
    'inv_39': False,
    'inv_40': False,
    'inv_41': False,
    'inv_42': False,
    'inv_43': False,
    'inv_44': False,
    'inv_45': False
}




img_chosen = img_Box

#items['Iron_pickaxe']
#items[vals1['Item_to_craft']]


#win1['inv_11'].update(items[vals1['Item_to_craft']])


def win1_layout():
    layout = [

        [sg.Image(img_Steve, key='Steve', size=(80,130)),sg.Listbox(values=('Iron_Pickaxe', 'Iron_Sword', 'Iron_Axe', 'Iron_Shovel', 'Stone_Bricks', 'Bread', 'Oak_Planks', 'Diamond_Sword', 'Spruce_Planks' ),key='Item_to_craft', size=(30, 3)), sg.Button('Craft'), sg.Slider(range=(1, 45), orientation='h', size=(10, 20),expand_x=True, default_value=1,key='slot')], 
        [[sg.Image(img_Box, key='crefting', size=(60,60)), sg.Image(img_Box, key='crefting2', size=(60,60)),],[sg.Image(img_Box, key='crefting3', size=(60,60)), sg.Image(img_Box, key='crefting4', size=(60,60))]],
        [sg.Image(img_Box, key='inv_37', size=(60,60)), sg.Image(img_Box, key='inv_38', size=(60,60)), sg.Image(img_Box, key='inv_39', size=(60,60)), sg.Image(img_Box, key='inv_40', size=(60,60)), sg.Image(img_Box, key='inv_41', size=(60,60)), sg.Image(img_Box, key='inv_42', size=(60,60)), sg.Image(img_Box, key='inv_43', size=(60,60)), sg.Image(img_Box, key='inv_44', size=(60,60)), sg.Image(img_Box, key='inv_45', size=(60,60)),],
        [sg.Image(img_Box, key='inv_28', size=(60,60)), sg.Image(img_Box, key='inv_29', size=(60,60)), sg.Image(img_Box, key='inv_30', size=(60,60)), sg.Image(img_Box, key='inv_31', size=(60,60)), sg.Image(img_Box, key='inv_32', size=(60,60)), sg.Image(img_Box, key='inv_33', size=(60,60)), sg.Image(img_Box, key='inv_34', size=(60,60)), sg.Image(img_Box, key='inv_35', size=(60,60)), sg.Image(img_Box, key='inv_36', size=(60,60)),],
        [sg.Image(img_Box, key='inv_19', size=(60,60)), sg.Image(img_Box, key='inv_20', size=(60,60)), sg.Image(img_Box, key='inv_21', size=(60,60)), sg.Image(img_Box, key='inv_22', size=(60,60)), sg.Image(img_Box, key='inv_23', size=(60,60)), sg.Image(img_Box, key='inv_24', size=(60,60)), sg.Image(img_Box, key='inv_25', size=(60,60)), sg.Image(img_Box, key='inv_26', size=(60,60)), sg.Image(img_Box, key='inv_27', size=(60,60)),],
        [sg.Image(img_Box, key='inv_10', size=(60,60)), sg.Image(img_Box, key='inv_11', size=(60,60)), sg.Image(img_Box, key='inv_12', size=(60,60)), sg.Image(img_Box, key='inv_13', size=(60,60)), sg.Image(img_Box, key='inv_14', size=(60,60)), sg.Image(img_Box, key='inv_15', size=(60,60)), sg.Image(img_Box, key='inv_16', size=(60,60)), sg.Image(img_Box, key='inv_17', size=(60,60)), sg.Image(img_Box, key='inv_18', size=(60,60)),],
        [sg.Image(img_Box, key='inv_1', size=(60,60)), sg.Image(img_Box, key='inv_2', size=(60,60)), sg.Image(img_Box, key='inv_3', size=(60,60)), sg.Image(img_Box, key='inv_4', size=(60,60)), sg.Image(img_Box, key='inv_5', size=(60,60)), sg.Image(img_Box, key='inv_6', size=(60,60)), sg.Image(img_Box, key='inv_7', size=(60,60)), sg.Image(img_Box, key='inv_8', size=(60,60)), sg.Image(img_Box, key='inv_9', size=(60,60)), ]
        
        
       
        
]


    return layout
   
def win2_layout():
    layout = [[sg.Text('Window 2')],
              [sg.Input(do_not_clear=True)],
              [sg.Button('Exit')]]
 
    return layout


def choose_img(item):
    if item == 'Bread':
        img = img_Bread

    else:
        img = img_Iron_Sword

    return img


def win3_layout():
    layout=[ ]
    
    for item in inventory:
        img = choose_img(item[0])

    

        layout.append([sg.Image(img, key='image_key', size=(60,60))])

    return layout
 
win1 = sg.Window('Minecraft', win1_layout())
 
win2_active = False


while True:
    ev1, vals1 = win1.read(timeout=100)
    
    if ev1 == sg.WIN_CLOSED or ev1 == 'Exit':
        break

    if ev1 == 'Craft':

        add_item = str(vals1['Item_to_craft'])
        add_item = add_item[2:]
        add_item = add_item[:-2]

        print(add_item)

        number = vals1['slot']
        number = int(number)
        chosen_box = 'inv_' + str(number)

        if box[chosen_box] == False:
            box[chosen_box] = True
            win1[chosen_box].update(items[add_item])

            
       
        # Update the "output" text element to be the value of "input" element
      
       

 
 
    if not win2_active and ev1 == 'Launch 2':
        win2_active = True
        #win1.Hide()  # fjern hashtag for å skjule window 1 når window 2 skal vises
        win2 = sg.Window('Window 2', win2_layout())
 
    if win2_active:
        ev2, vals2 = win2.read(timeout=100)
        if ev2 == sg.WIN_CLOSED or ev2 == 'Exit':
            win2_active  = False
            #win1.UnHide()   # fjern hashtag for å vise window 1 igjen
            win2.close()

    
