import io
import os
import sys
import unittest
from math import sin, cos, pi
from PIL import Image

# I most vehemently abhor this wretched programming language.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from main import process_file  

class TestImageProcessing(unittest.TestCase):
   def setUp(self):
      self.test_images = []

      width = 128
      height = 72

      dark_img = Image.new('RGB', (width, height))
      gray_img = Image.new('RGB', (width, height))
      white_img = Image.new('RGB', (width, height))
      red_img = Image.new('RGB', (width, height))
      grn_img = Image.new('RGB', (width, height))
      blu_img = Image.new('RGB', (width, height))

      for x in range(width):
         px = x*pi*2/width
         for y in range(height):
            py = y*pi*2/height
            r = int(127*(1-sin(px)*cos(py)))
            g = int(127*(1-sin(px)*sin(py)))
            b = int(127*(1-cos(px)))

            dark_img.putpixel((x, y), (r//10, g//10, b//10))
            gray_img.putpixel((x, y), (r, g, b))
            white_img.putpixel((x, y), (r*2, g*2, b*2))
            red_img.putpixel((x, y), (r, g//10, b//10))
            grn_img.putpixel((x, y), (r//10, g, b//10))
            blu_img.putpixel((x, y), (r//10, g//10, b))
      
      dark_img.save('dark_img.png')
      gray_img.save('gray_img.png')
      white_img.save('white_img.png')
      red_img.save('red_img.png')
      grn_img.save('grn_img.png')
      blu_img.save('blu_img.png')

      self.test_images.append('dark_img.png')
      self.test_images.append('gray_img.png')
      self.test_images.append('white_img.png')
      self.test_images.append('red_img.png')
      self.test_images.append('grn_img.png')
      self.test_images.append('blu_img.png')


   def tearDown(self):
      for img_path in self.test_images:
         try:
            os.remove(img_path)
         except OSError:
            pass
   

   def test_gray_mode(self):
      test_cases = [
         ('dark_img.png', 'ciemny '),
         ('gray_img.png', 'szary '),
         ('white_img.png', 'jasny '),
      ]

      for img_path, expected_output in test_cases:
         with self.subTest(img=img_path):
            captured_output = io.StringIO()
            sys.stdout = captured_output

            process_file(img_path, 'gray')

            sys.stdout = sys.__stdout__
            output = captured_output.getvalue().strip()
            self.assertTrue(output.startswith(expected_output))


   def test_rgb_mode(self):
      test_cases = [
         ('red_img.png', 'czerwony '),
         ('grn_img.png', 'zielony '),
         ('blu_img.png', 'niebieski '),
      ]

      for img_path, expected_output in test_cases:
         with self.subTest(img=img_path):
            captured_output = io.StringIO()
            sys.stdout = captured_output

            process_file(img_path, 'rgb')

            sys.stdout = sys.__stdout__
            output = captured_output.getvalue().strip()
            self.assertTrue(output.startswith(expected_output))


if __name__ == '__main__':
   unittest.main()
