import pygame

import sys

import random


pygame.init()

pygame.display.set_caption("Камень-ножницы-бумага")

screen = pygame.display.set_mode((420, 350))


choices = ['камень', 'ножницы', 'бумага']

computer_choice = random.choice(choices)


button_rock = pygame.Rect(20, 50, 120, 50)

button_scissors = pygame.Rect(150, 50, 120, 50)

button_paper = pygame.Rect(280, 50, 120, 50)

end_game = False


def draw_text(text, font, color, surface, x, y):

  textobj = font.render(text, 1, color)

  textrect = textobj.get_rect()

  textrect.topleft = (x, y)

  surface.blit(textobj, textrect)


def game():

  global end_game

  user_choice = ""

  result = ""

  while True:

    for event in pygame.event.get():

      if event.type == pygame.QUIT:

        pygame.quit()

        sys.exit()


      if event.type == pygame.MOUSEBUTTONDOWN:

        # Определите, на какую кнопку нажал пользователь

        mouse_pos = event.pos

        if button_rock.collidepoint(mouse_pos):

          user_choice = 'камень'

        elif button_scissors.collidepoint(mouse_pos):

          user_choice = 'ножницы'

        elif button_paper.collidepoint(mouse_pos):

          user_choice = 'бумага'


        if user_choice != "":

          computer_choice = random.choice(choices)

          # Определить победителя

          result = get_result(user_choice, computer_choice)

          draw_text('Выбор пользователя: ' + user_choice, font, (0, 0, 0), screen, 20, 120)

          draw_text('Выбор компьютера: ' + computer_choice, font, (0, 0, 0), screen, 20, 150)

          draw_text(result, font, (0, 0, 0), screen, 20, 180)


    screen.fill((255, 255, 255))

    draw_text('Выберите:', font, (0, 0, 0), screen, 20, 20)


    # Создайте кнопки для выбора камня, ножниц или бумаги

    pygame.draw.rect(screen, (255, 0, 0), button_rock)

    draw_text('Камень', font, (255, 255, 255), screen, 35, 60)


    pygame.draw.rect(screen, (0, 255, 0), button_scissors)

    draw_text('Ножницы', font, (255, 255, 255), screen, 165, 60)


    pygame.draw.rect(screen, (0, 0, 255), button_paper)

    draw_text('Бумага', font, (255, 255, 255), screen, 300, 60)


    if result != "":

      draw_text('Выбор пользователя: ' + user_choice, font, (0, 0, 0), screen, 20, 120)

      draw_text('Выбор компьютера: ' + computer_choice, font, (0, 0, 0), screen, 20, 150)

      draw_text(result, font, (0, 0, 0), screen, 20, 180)


    pygame.display.update()


def get_result(user_choice, computer_choice):

  if user_choice == computer_choice:

    return 'Ничья!'

  elif user_choice == 'камень' and computer_choice == 'ножницы':

    return 'Вы победили!'

  elif user_choice == 'ножницы' and computer_choice == 'бумага':

    return 'Вы победили!'

  elif user_choice == 'бумага' and computer_choice == 'камень':

    return 'Вы победили!'

  else:

    return 'Компьютер победил.'



if __name__ == '__main__':

  pygame.init()

  font = pygame.font.SysFont(None, 30)


  game()

  pygame.quit()

  sys.exit()