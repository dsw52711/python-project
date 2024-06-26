import argparse
import os
from PIL import Image
import numpy as np


def process_gray(file_path, image):
   gray_img = image.convert('L')
   gray_array = np.array(gray_img)
   avg_luminosity = np.mean(gray_array)
   
   if avg_luminosity < 85:
      print(f"ciemny     {file_path}")
   elif avg_luminosity < 170:
      print(f"szary      {file_path}")
   else:
      print(f"jasny      {file_path}")


def process_rgb(file_path, image):
   rgb_array = np.array(image)
   r_sum = np.sum(rgb_array[:, :, 0])
   g_sum = np.sum(rgb_array[:, :, 1])
   b_sum = np.sum(rgb_array[:, :, 2])
   
   max_channel = max(r_sum, g_sum, b_sum)
   
   if max_channel == r_sum:
      print(f"czerwony   {file_path}")
   elif max_channel == g_sum:
      print(f"zielony    {file_path}")
   else:
      print(f"niebieski  {file_path}")


def process_file(file_path, mode):
   try:
      with Image.open(file_path) as image:
         if mode == 'gray':
            process_gray(file_path, image)
         elif mode == 'rgb':
            process_rgb(file_path, image)
   except Exception as _:
      print(f"Przetwarzanie pliku '{file_path}' nie powiodło się")


def process_directory(directory_path, mode):
   files = [f for f in os.listdir(directory_path)]
   files = [os.path.join(directory_path, f) for f in files]
   files = [f for f in files if os.path.isfile(f)]
   for file_path in files:
      process_file(file_path, mode)


def main():
   parser = argparse.ArgumentParser(description='Kategoryzacja obrazów')
   parser.add_argument('--gray', action='store_true',
                       help='Kategoryzacja na odcienie szarości')
   parser.add_argument('--rgb', action='store_true',
                       help='Kategoryzacja na dominujący kolor z '+
                       'przestrzeni RGB')
   parser.add_argument('paths', nargs='+', help='Lista plików lub '+
                       'katalogów plików')
   args = parser.parse_args()

   mode = 'gray' if args.gray else 'rgb'
   for path in args.paths:
      if os.path.isdir(path):
         process_directory(path, mode)
      elif os.path.isfile(path):
         process_file(path, mode)
      else:
         print(f"Błąd: {path} nie jest plikiem ani katalogiem")


if __name__ == "__main__":
   main()