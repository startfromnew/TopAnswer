import unittest

from PIL import Image

from lib.ocr import Ocr


class TestOcr(unittest.TestCase):
    def test_image_to_string(self):
        o=Ocr()
        img="../screen/2.png"
        print(o.image_to_string(img))
    def test_ocr_img_count(self):
        o=Ocr("test",1)
        q,c=o.ocr_img_count()
        print(q)
        print(c)
        print("ok")

    def test_crop(self):
        o=Ocr("zhishi",1)
        for i in range(12):
            q,c=o.ocr_img_count()
            print(q)
            print(c)
