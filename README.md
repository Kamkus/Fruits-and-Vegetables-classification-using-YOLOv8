# Rozpoznawanie warzyw i owoców na podstawie obrazka

## Wyjaśnienie plików

### panel.py
Główny plik projektu, znajduje się w nim panel storzony w **PySimpleGUI**. Pozwala on na wybranie danego obrazu z dysku i otrzymaniu odpowiedzi algorytmu jaki obiekt jest widoczny na obrazie.(**UWAGA: Pliki wybierane przez panel obsługują tylko format .png. Aby sprawdzić inne rozszerzenia prosze przeczytać o pliku prediction.py**)

#### main.py 
Plik w którym znajduje się kod do trenowania naszego algorytmu. Model ***yolov8n-cls.pt*** jest rekomendowany do trenowania przez twórcę algorytmu. Aby trenowanie było możliwę należy zachować odpowiednią strukturę danych treningowych oraz danych walidacyjnych.
```
train_data
└───train(Stała nazwa)
│   └───cucumber(Nazwa klucza danej)
│   │   └───cucumber.png
│   │
│   └───watermelon(Nazwa klucza danej)
│       └───watermelon.png
│   
└───val(Stała nazwa)(Walidacja treningu)
│   └───cucumber(Nazwa klucza danej)
│   │   └───cucumber.png
│   │
│   └───watermelon(Nazwa klucza danej)
│       └───watermelon.png
```

#### structurization.py
Plik który został użyty do posegregowania zdjęc które miały nazwy np. productName1___xxx.png według nazwy do poszczególnych folderów aby utworzyć odpowiednią strukturę do szkolenia modelu yolov8.

#### prediction.py
Plik w którym znajduje się możliwość manualnego sprawdzenia odpowiedzi wytrenowanego modelu na zadane zdjęcie w każdym formacie (***testowałem jpg oraz png***). Aby to zrobić wystarczy podać relatywną lub absolutną ścieżkę do obrazu, lub podać link i uruchomić program. W konsoli pokaże nam się wynik oraz przekonanie co do wyniku. (**UWAGA W momencie podania linku, obraz zostanie pobrany na komputer i wrzucony do katalogu w którym znajduje się skrypt**)

## Instalacja
### Stworzenie środowiska 
Środowisko stworzone przeze mnie to virtual environment w wersji **Python 3.10.0**

### Dodawanie bibliotek
```python
    # Pycharm
        Należy z menu wyboru modułów dodać następujące moduły
        - ultralytics 8.0.58
        - PySimpleGUI
    # VSC
        py -m pip install ultralytics #Instalowanie ultralytics
        py -m pip install PySimpleGUI #Instalowanie PySimpleGUI
```
### Uruchomienie Projektu 😊

# Dane treningowe
Całą zawartość danych treningowych to prawie 2 GB więc pozwole sobie nie wrzucać jej tutaj, jednak wszystkie zdjęcia których użyliśmy można znaleźć tutaj -> [Roboflow](https://universe.roboflow.com/cse299/fruit-and-vegetable/dataset/1)  oraz tutaj -> [Kaggle](https://www.kaggle.com/datasets/kritikseth/fruit-and-vegetable-image-recognition)