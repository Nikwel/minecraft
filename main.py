import PySimpleGUI as sg
from PIL import Image   
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

sg.theme('BluePurple')

img_Iron_Sword = get_img_data('Iron_Sword.png')
img_Iron_Axe = get_img_data('Iron_Axe.png')

inventory= []

 
column1 = [[sg.Text('Column 1', background_color='#d3dfda', justification='center', size=(10, 1))],
           [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1')],
           [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],
           [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]


layout = [
        [sg.Listbox(values=('Iron_Pickaxe', 'Iron_Sword', 'Iron_Axe', 'Iron_Shovel', 'Stone_Bricks', 'Bread'),key='Item_to_craft', size=(30, 3)), sg.Slider(range=(1, 64), orientation='v', size=(5, 20), default_value=1,key='Amount'), sg.Button('Craft')],
        [sg.Text('', key='-OUTPUT-') ],
        [sg.Image(img_Iron_Sword, key='image_key', size=(60,60))],
        [sg.Image(img_Iron_Axe, key='image_key', size=(60,60))]
       
        
     
]
 
window = sg.Window('Tittel på programmer', layout)
#window2 = sg.Window('Visning av bilde', layout)

 
while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    if event == 'Craft':

        item = [values['Item_to_craft'], values['Amount']]
        inventory.append(item)
       
        # Update the "output" text element to be the value of "input" element
        window['-OUTPUT-'].update(inventory)
 
window.close()