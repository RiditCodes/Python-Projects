import pygame
from pygame.locals import *
import sys
import time
import random
import pyjokes

class Game:
    def __init__(self):
        self.w = 750
        self.h = 500
        self.rest = True
        self.active = False
        self.input_text = ""
        self.word = ""
        self.time_start = 0
        self.total_time = 0
        self.accuracy = "0%"
        self.results = "Time:0 Accuracy:0 Words_per_minute:0"
        self.wpm = 0
        self.end = False
        self.HEAD_C = (255,213,102)
        self.TEXT_C = (240,240,240)
        self.RESULT_C = (255,70,70)

        pygame.init()
        self.open_img = pygame.image.load("keyboard.jpg")
        self.open_img = pygame.transform.scale(self.open_img, (750, 500))

        self.screen = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("Typing Speed")

    def draw_text(self, screen, msg, y, fsize, color):
            font = pygame.font.Font(None, fsize)
            text = font.render(msg, 1, color)
            text_rect = text.get_rect(self.w/2, y)
            screen.blit(text, text_rect)
            pygame.display.update()

    def get_sentence(self):
            sentence = pyjokes.get_joke()
            if len(sentence) <= 75:
                return sentence

    def show_results(self, screen):
        if (not self.end):
            self.total_time = time.time() - self.time_start

            count = 0
            for i,c in enumerate(self.word):
                try:
                    if self.input_text[1] == c:
                        count += 1
                except:
                    pass
            self.accuracy = count/len(self.word*100)
            self.wpm = len(self.input_text)*60/(5*self.total_time)
            self.end = True
            print(self.total_time)

            self.results = "Time" + str(round(self.total_time)) + "secs Accuracy" + str(round(self.accuracy)) + "%" + " WPM: " + str(round(self.wpm))
            self.time_img = pygame.image.load()
            self.time_img = pygame.transform.scale(self.time_img, (150, 150))

            screen.blit(self.time_img, self.w/2-75, self.h-140)

            self.draw_text(screen, "Reset", self.h-70, 26, (100,100,100))

        print(self.results)
        pygame.display.update()

    def run(self):
        self.reset_game()

        self.running = True
        while(self.running):
            clock = pygame.time.Clock()
            self.screen.fill((0, 0, 0), (50, 250, 650, 50))
            pygame.draw.rect(self.screen, self.HEAD_C, (50,250,650,50), 2)
            self.draw_text(self.screen, self.input_text,274,26,(250,250,250))
            pygame.display.update()

game = Game()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.update()

pygame.quit()