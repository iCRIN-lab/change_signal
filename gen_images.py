# petit code qui génère un nombre aléatoire d'allumettes
import random

from PIL import Image, ImageDraw, ImageFont
from screeninfo import get_monitors
from random import randint


def gen_allum(nb_img):
    choices = []
    for i in range(nb_img):
        gauche_droite = randint(0, 1)
        choices.append(gauche_droite)
        img = Image.new(
            mode="RGB",
            size=(get_monitors()[0].width, get_monitors()[0].height),
            color=(255, 255, 255),
        )
        foreground = Image.open("carre.jpeg")
        if gauche_droite == 0:
            img.paste(foreground, (150, 400))
        else:
            img.paste(foreground, (850, 400))
        img.save(f"img/img_{i+3}.png")
        print(f"Image n°{i}")
    return choices


L_choices = gen_allum(5)
print(L_choices)
