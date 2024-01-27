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
    'onion' : 'Cebula',
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

results = model('https://dietetycy.org.pl/wp-content/uploads/2022/06/44060527_m-1600x1067.jpg')


top5Indexes = results[0].probs.top5
top5probes = results[0].probs.top5conf.tolist()
print(polish_translation[results[0].names[top5Indexes[top5probes.index(max(top5probes))]]], "Pewność: ", max(top5probes) * 100 , '%')