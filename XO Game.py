import pygame  # Calling Library
pygame.init()  # Intialize Pygame Library


# Start Set Pygame Screen Size, Title, Icon Image and Background Color
screen = pygame.display.set_mode((550, 550))  # Screen Size of Pygame ---> (Length, Width)
pygame.display.set_caption("XO Game")  # The title of Pygame Screen
iconImage = pygame.image.load('Icon.jpg')  # The Variable for setting the Image Icon Path
pygame.display.set_icon(iconImage)  # Setting the Icon Image of Pygame Sreen
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# End Set Pygame Screen Size, Title, Icon Image and Background Color


# Start pygame.draw.rect(surface, (color), (startx,starty,length width)) ---> 9 Squares
first = pygame.draw.rect(screen, (255, 255, 255), (25, 25, 150, 150))  # 1st place
second = pygame.draw.rect(screen, (255, 255, 255), (200, 25, 150, 150))  # 2nd place
third = pygame.draw.rect(screen, (255, 255, 255), (375, 25, 150, 150))  # 3rd place
fourth = pygame.draw.rect(screen, (255, 255, 255), (25, 200, 150, 150))  # 4th place
fifth = pygame.draw.rect(screen, (255, 255, 255), (200, 200, 150, 150))  # 5th place
sixth = pygame.draw.rect(screen, (255, 255, 255), (375, 200, 150, 150))  # 6th place
seventh = pygame.draw.rect(screen, (255, 255, 255), (25, 375, 150, 150))  # 7th place
eigth = pygame.draw.rect(screen, (255, 255, 255), (200, 375, 150, 150))  # 8th place
ninth = pygame.draw.rect(screen, (255, 255, 255), (375, 375, 150, 150))  # 9th place
# End pygame.draw.rect(surface, (color), (startx,starty,length width)) ---> 9 Squares


# Start Variables To avoid drawing X and O in the Same box
first_open = True
second_open = True
third_open = True
fourth_open = True
fifth_open = True
sixth_open = True
seventh_open = True
eigth_open = True
ninth_open = True
# End Variables To avoid drawing X and O in the Same box


# Start Colors we will use
white = (255, 255, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
# End Colors we will use


# Start Possible Events for Winning or Draw Match
# Player X is the Winner
def winner_X():
    display_surface = pygame.display.set_mode((550, 550))
    font_X = pygame.font.Font('freesansbold.ttf', 40)
    text_X = font_X.render('Player X Won', True, yellow, black)
    text_rect_X = text_X.get_rect()
    text_rect_X.center = (550 // 2, 550 // 2)
    display_surface.fill(white)
    display_surface.blit(text_X, text_rect_X)
# Player O is the Winner
def winner_O():
    surface_display = pygame.display.set_mode((550, 550))
    font_O = pygame.font.Font('freesansbold.ttf', 40)
    text_O = font_O.render('Player O Won', True, red, black)
    rect_text_O = text_O.get_rect()
    rect_text_O.center = (550 // 2, 550 // 2)
    surface_display.fill(white)
    surface_display.blit(text_O, rect_text_O)
# Draw Match
def draw():
    surface_display = pygame.display.set_mode((550, 550))
    font_draw = pygame.font.Font('freesansbold.ttf', 40)
    text_draw = font_draw.render('Draw Match', True, green, black)
    rect_text_draw = text_draw.get_rect()
    rect_text_draw.center = (550 // 2, 550 // 2)
    surface_display.fill(white)
    surface_display.blit(text_draw, rect_text_draw)
# Start Possible Events for Winning or Draw Match


# Start Variables
choices = 0
running = True  # The Variable that controls the While Loop
draw_sign = 'X'  # Choosing X Player the O Player
# End Variables


# Start Winner Function
def is_wining():
    for row in range(3):
        winner_row = 0
        for col in range(3):
            winner_row += board[row - 1][col - 1]
            if winner_row == 3:
                winner_O()
            elif winner_row == -3:
                winner_X()
    for col in range(3):
        winner_col = 0
        for row in range(3):
            winner_col += board[row - 1][col - 1]
            if winner_col == 3:
                winner_O()
            elif winner_col == -3:
                winner_X()
    winner_Z = 0
    for Z in range(3):
        winner_Z += board[Z - 1][Z - 1]
        if winner_Z == 3:
            winner_O()
        elif winner_Z == -3:
            winner_X()
    winner_Z = 0
    col = 2
    row = 0
    for i in range(3):
        winner_Z += board[row][col]
        row += 1
        col -= 1
        if winner_Z == 3:
            winner_O()
        elif winner_Z == -3:
            winner_X()
    if choices == 9:
        draw()
# End Winner Function


# Start Insert Function
def insert():
    global running, choices, draw_sign, \
        first_open, second_open, third_open, \
        fourth_open, fifth_open, sixth_open, \
        seventh_open, eigth_open, ninth_open
    while running:
        pygame.time.delay(100)  # Refresh Time
        for event in pygame.event.get():

            # When the user clicks on the Close Button the screen will be closed
            if event.type == pygame.QUIT:
                running = False

            # Press Delete to reset the Game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DELETE:
                    running = True
                    first_open = True
                    second_open = True
                    third_open = True
                    fourth_open = True
                    fifth_open = True
                    sixth_open = True
                    seventh_open = True
                    eigth_open = True
                    ninth_open = True
                    first = pygame.draw.rect(screen, (255, 255, 255), (25, 25, 150, 150))  # 1st place
                    second = pygame.draw.rect(screen, (255, 255, 255), (200, 25, 150, 150))  # 2nd place
                    third = pygame.draw.rect(screen, (255, 255, 255), (375, 25, 150, 150))  # 3rd place
                    fourth = pygame.draw.rect(screen, (255, 255, 255), (25, 200, 150, 150))  # 4th place
                    fifth = pygame.draw.rect(screen, (255, 255, 255), (200, 200, 150, 150))  # 5th place
                    sixth = pygame.draw.rect(screen, (255, 255, 255), (375, 200, 150, 150))  # 6th place
                    seventh = pygame.draw.rect(screen, (255, 255, 255), (25, 375, 150, 150))  # 7th place
                    eigth = pygame.draw.rect(screen, (255, 255, 255), (200, 375, 150, 150))  # 8th place
                    ninth = pygame.draw.rect(screen, (255, 255, 255), (375, 375, 150, 150))  # 9th place

            # Draw the XO Signs
            if event.type == pygame.MOUSEBUTTONUP:
                position = pygame.mouse.get_pos()

                if first.collidepoint(position) and first_open:
                    choices += 1
                    # Draws a shapes based on whose turn it is
                    if draw_sign == 'O':
                        # pygame.draw.circle(surface, (color), (centerx, centery),radius)
                        pygame.draw.circle(screen, (255, 0, 0), (100, 100), 60)
                        pygame.draw.circle(screen, (255, 255, 255), (100, 100), 55)
                        draw_sign = 'X'
                        board[0][0] = 1
                    else:
                        pygame.draw.line(screen, (255, 255, 0), (50, 50), (150, 150), 10)
                        pygame.draw.line(screen, (255, 255, 0), (50, 150), (150, 50), 10)
                        draw_sign = 'O'
                        board[0][0] = -1
                    first_open = False  # Marks this space as taken

                if second.collidepoint(position) and second_open:
                    choices += 1
                    if draw_sign == 'O':
                        pygame.draw.circle(screen, (255, 0, 0), (275, 100), 60)
                        pygame.draw.circle(screen, (255, 255, 255), (275, 100), 55)
                        draw_sign = 'X'
                        board[0][1] = 1
                    else:
                        pygame.draw.line(screen, (255, 255, 0), (225, 50), (325, 150), 10)
                        pygame.draw.line(screen, (255, 255, 0), (225, 150), (325, 50), 10)
                        draw_sign = 'O'
                        board[0][1] = -1
                    second_open = False

                if third.collidepoint(position) and third_open:
                    choices += 1
                    if draw_sign == 'O':
                        pygame.draw.circle(screen, (255, 0, 0), (450, 100), 60)
                        pygame.draw.circle(screen, (255, 255, 255), (450, 100), 55)
                        draw_sign = 'X'
                        board[0][2] = 1
                    else:
                        pygame.draw.line(screen, (255, 255, 0), (400, 50), (500, 150), 10)
                        pygame.draw.line(screen, (255, 255, 0), (400, 150), (500, 50), 10)
                        draw_sign = 'O'
                        board[0][2] = -1
                    third_open = False

                if fourth.collidepoint(position) and fourth_open:
                    choices += 1
                    if draw_sign == 'O':
                        pygame.draw.circle(screen, (255, 0, 0), (100, 275), 60)
                        pygame.draw.circle(screen, (255, 255, 255), (100, 275), 55)
                        draw_sign = 'X'
                        board[1][0] = 1
                    else:
                        pygame.draw.line(screen, (255, 255, 0), (50, 225), (150, 325), 10)
                        pygame.draw.line(screen, (255, 255, 0), (50, 325), (150, 225), 10)
                        draw_sign = 'O'
                        board[1][0] = -1
                    fourth_open = False

                if fifth.collidepoint(position) and fifth_open:
                    choices += 1
                    if draw_sign == 'O':
                        pygame.draw.circle(screen, (255, 0, 0), (275, 275), 60)
                        pygame.draw.circle(screen, (255, 255, 255), (275, 275), 55)
                        draw_sign = 'X'
                        board[1][1] = 1
                    else:
                        pygame.draw.line(screen, (255, 255, 0), (225, 225), (325, 325), 10)
                        pygame.draw.line(screen, (255, 255, 0), (225, 325), (325, 225), 10)
                        draw_sign = 'O'
                        board[1][1] = -1
                    fifth_open = False

                if sixth.collidepoint(position) and sixth_open:
                    choices += 1
                    if draw_sign == 'O':
                        pygame.draw.circle(screen, (255, 0, 0), (450, 275), 60)
                        pygame.draw.circle(screen, (255, 255, 255), (450, 275), 55)
                        draw_sign = 'X'
                        board[1][2] = 1
                    else:
                        pygame.draw.line(screen, (255, 255, 0), (400, 225), (500, 325), 10)
                        pygame.draw.line(screen, (255, 255, 0), (400, 325), (500, 225), 10)
                        draw_sign = 'O'
                        board[1][2] = -1
                    sixth_open = False

                if seventh.collidepoint(position) and seventh_open:
                    choices += 1
                    if draw_sign == 'O':
                        pygame.draw.circle(screen, (255, 0, 0), (100, 450), 60)
                        pygame.draw.circle(screen, (255, 255, 255), (100, 450), 55)
                        draw_sign = 'X'
                        board[2][0] = 1
                    else:
                        pygame.draw.line(screen, (255, 255, 0), (50, 400), (150, 500), 10)
                        pygame.draw.line(screen, (255, 255, 0), (50, 500), (150, 400), 10)
                        draw_sign = 'O'
                        board[2][0] = -1
                    seventh_open = False

                if eigth.collidepoint(position) and eigth_open:
                    choices += 1
                    if draw_sign == 'O':
                        pygame.draw.circle(screen, (255, 0, 0), (275, 450), 60)
                        pygame.draw.circle(screen, (255, 255, 255), (275, 450), 55)
                        draw_sign = 'X'
                        board[2][1] = 1
                    else:
                        pygame.draw.line(screen, (255, 255, 0), (225, 400), (325, 500), 10)
                        pygame.draw.line(screen, (255, 255, 0), (225, 500), (325, 400), 10)
                        draw_sign = 'O'
                        board[2][1] = -1
                    eigth_open = False

                if ninth.collidepoint(position) and ninth_open:
                    choices += 1
                    if draw_sign == 'O':
                        pygame.draw.circle(screen, (255, 0, 0), (450, 450), 60)
                        pygame.draw.circle(screen, (255, 255, 255), (450, 450), 55)
                        draw_sign = 'X'
                        board[2][2] = 1
                    else:
                        pygame.draw.line(screen, (255, 255, 0), (400, 400), (500, 500), 10)
                        pygame.draw.line(screen, (255, 255, 0), (400, 500), (500, 400), 10)
                        draw_sign = 'O'
                        board[2][2] = -1
                    ninth_open = False

                is_wining()

        pygame.display.update()
# End Insert Function


# Start Main Function
def main():
    global running
    while running:
        insert()
# End Main Function



#Main Code
main()