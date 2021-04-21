import pygame
import os
from .customer import Customer

class White_cap(Customer):
    frames = []
    for x in range(20):
        str_plus = str(x)
        if x < 10:
            str_plus += '0'
    frames.append(pygame.image.load(os.path.join('.//assets/customers/white_cap', 'white_cap_1' + str_plus + '.jpg')))

    def __init__ (self):
        super().__init__()