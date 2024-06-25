<div align="center">
   <h1>Kategoryzowanie zdjęć</h1>
   <p>
      Skrypt mający na celu kategoryzowanie zdjęć na podstawie ich zawartości, umożliwiający przetwarzanie pojedynczych plików oraz całych katalogów.
   </p>
</div>

## Wymagania
- Python 3.x
- Biblioteki Python: `argparse`

## Instalacja
```sh
# sklonuj repozytorium
git clone https://github.com/dsw52711/python-project
# przejdź do katalogu projektu
cd python-project
```

## Sposób użycia
Skrypt można uruchomić z wiersza poleceń używając następującej struktury:
```sh
python ./src/main.py [opcje] [pliki lub katalogi...]
```

### Opcje
- `--gray`: Kategoryzowanie zdjęć na odcienie szarości
- `--rgb`: Kategoryzowanie zdjęć na dominujący kolor z przestrzeni RGB (domyślne)

### Przykłady
1. Kategoryzacja pojedynczego pliku na odcienie szarości:
   ```sh
   python ./src/main.py --gray /ścieżka/do/pliku.jpg
   ```
1. Kategoryzacja wszystkich plików w katalogu na dominujący kolor z przestrzeni RGB:
   ```sh
   python ./src/main.py --rgb /ścieżka/do/katalogu
   ```
1. Kategoryzacja mieszanych plików i katalogów:
   ```sh
   python ./src/main.py /ścieżka/do/katalogu /ścieżka/do/pliku.jpg /ścieżka/do/pliku.png
   ```

# Autorzy
- Jan Konopnicki 52711