from ultralytics import YOLO



# globalNames = {
#     'fresh_banana' : 'Banan',
#     'fresh_bell_pepper': 'Papryka',
#     'fresh_guava' : 'Guava',
#     'fresh_lemon' : 'Cytryna',
#     'fresh_mango' : 'Mango',
#     'fresh_orange-' : 'Pomarańcza',
#     'fresh_pomegranate' : 'Granat',
#     'fresh-apple' : "Jablko",
#     'fresh_strawberry' : "Truskawka",
#     'fresh_tomato' : "Pomidor",
#     'fresh-apple' : "Jabłko",
#     'stale_lemon' : "Zgniła cytryna",
# }




model = YOLO('./runs/classify/train/weights/best.pt')

results = model('https://dietetycy.org.pl/wp-content/uploads/2022/06/44060527_m-1600x1067.jpg')


top5Indexes = results[0].probs.top5
top5probes = results[0].probs.top5conf.tolist()
print(results[0].names[top5Indexes[top5probes.index(max(top5probes))]], "Pewność: ", max(top5probes) * 100 , '%')