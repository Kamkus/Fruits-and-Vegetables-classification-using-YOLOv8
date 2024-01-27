import PySimpleGUI as sg
from ultralytics import YOLO



polish_translation = {
    'beetroot': 'Burak',
    'cabbage' : "Kapusta",
    'capsicium' : 'Papryka',
    'carrot' : 'Marchew',
    'cauliflower' : 'Kalafior',
    'chilli pepper': 'Papryczka chilli',
    'corn' : "Kukurydza",
    'cucumber': "Ogórek",
    'eggplant': 'Bakłażan',
    'fresh_banana':'Banan',
    'fresh_bell_pepper': 'Papryka',
    'fresh_guava' : 'Gujawa',
    'fresh_lemon': 'Cytryna',
    'fresh_mango': 'Mango',
    'fresh_orange-' : "Pomarańcza",
    'fresh_pomegranate' : "Granat",
    'fresh_strawberry': 'Truskawka',
    'fresh_tomato' : "Pomidor",
    'fresh-apple':'Jablko',
    'garlic' : 'Czosnek',
    'ginger': 'Imbir',
    'grapes' : 'Winogrono',
    'jalepeno' : 'Papryczka dżalapinio',
    'kiwi' : 'Kiwi',
    'lettuce' : 'Sałata',
    'onion' : 'Polak',
    'pear' : 'Gruszka',
    'peas' : 'Groszek',
    'pineapple' : 'Ananas',
    'potato' : 'Ziemnior',
    'raddish' : 'Rzodkiewka',
    'soy beans' : 'Ciecierzyca',
    'spinach' : 'Szpinacz',
    'sweetcorn' : 'Kukurydza',
    'sweetpotato' : 'Batat',
    'turnip' : 'Rzepa',
    'watermelon' : 'Arbuz',


}




model = YOLO('./runs/classify/train/weights/best.pt')

ImgBrowser = [
    [sg.I(), sg.FileBrowse(file_types=[('Pliki png', '*.png')])],
    [sg.Push(),sg.Ok(button_text="Sprawdź zdjęcie")],
]

ModelResponse = [
    [sg.Text("Odpowiedź modelu: Oczekuje", justification="center", key='response')]
]



layout = [
    [sg.Frame("Link do obrazu", ImgBrowser, size=(400, 80)), sg.Frame("Odpowiedź modelu", ModelResponse, size=(400, 80))],
    [sg.HorizontalSeparator()],
    [sg.Image(key="-IMG-", size=(10, 10))]
]


window = sg.Window("Rozpoznawanie owoców i warzyw", layout)
while 1:
    event, values = window.read()
    print(event,values)
    if event == "Sprawdź zdjęcie":
        if values['Browse'] != "":
            window['response'].update("Odpowiedź modelu: Przetwarzanie!")
            window['-IMG-'].update(values["Browse"])
            results = model(values["Browse"])
            top5Indexes = results[0].probs.top5
            top5probes = results[0].probs.top5conf.tolist()
            predictedName = results[0].names[top5Indexes[top5probes.index(max(top5probes))]]
            accuracy = max(top5probes) * 100
            # print(results[0].names[top5Indexes[top5probes.index(max(top5probes))]], "Pewność: ", max(top5probes) * 100 , '%')
            window['response'].update("Odpowiedź modelu: "+ polish_translation[predictedName] + " Pewność: " + str(round(accuracy,2))  +"%")

    elif event == sg.WIN_CLOSED:
        break
