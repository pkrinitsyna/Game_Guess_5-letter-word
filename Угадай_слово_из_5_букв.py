import turtle
import random

height = 80                                         # начальная высота вывода на экран введенных пользователем слов
list_of_used_words = []                             # создание глобального списка загаданных слов на случай повторной игры
keyboard = 'йцукенгшщзхъфывапролджэячсмитьбю'       # порядок букв на клавиатуре
wrong_letters = []                                  # создание глобального списка букв, отсутствующих в слове
list_of_words =[]


def generate_word():                                # функция генерации слова
    global list_of_words
    with open(r'C:\Users\polle\Documents\Python\Угадай слово из 5 букв\слова.txt','r',encoding='utf-8') as f:
        list_of_words = f.read().splitlines()
    word = random.choice(list_of_words)
    while word in list_of_used_words:
        word = random.choice(list_of_words)
    list_of_used_words.append(word)
    return word

def print_keyboard(height,start,end,pen_keyboard):  # функция вывода клавиатуры на экран с удалением лишних букв
    width = -30
    for letter in keyboard[start:end]:
        if letter in wrong_letters:
            letter = ' '
        pen_keyboard.setpos(width,height)
        pen_keyboard.write(letter,font = ('Arial',18,'normal'))
        width += 30

def print_letter(col,letter,position):              # функция вывода буквы на экран с соответствующим цветом
    turtle.setpos(position)
    turtle.pencolor(col)
    turtle.write(letter,font = ('Arial',18,'normal'))
    
def check_for_duplication(user_word,word,ind):      # функция, определяющая цвет буквы в случаях ее дублирования в введенном или загаданном слове 
    if user_word.count(user_word[ind]) > 1 and word.count(user_word[ind]) == 1:
        if user_word[word.index(user_word[ind])] == user_word[ind]:
            return False
        if ind != user_word.index(user_word[ind]):
            return False
    return True
    
def check_attemp(user_word,word):                   # функция проверки правильности расположения буквы в слове
    global height
    height -= 25
    width = -180
    for i in range(len(word)):
        if user_word[i] == word[i]:
            print_letter('green',user_word[i],tuple([width,height]))
        elif user_word[i] in word and check_for_duplication(user_word,word,i):
            print_letter('orange',user_word[i],tuple([width,height]))
        else:
            print_letter('grey',user_word[i],tuple([width,height]))
        width += 20
        if user_word[i] not in word:
            wrong_letters.append(user_word[i])

def start_game():                                  # функция старта игры
    global height
    height = 80
    global wrong_letters
    wrong_letters = []
    turtle.Screen().clear()
    turtle.Screen().bgcolor('cornsilk')
    pen_keyboard = turtle.Turtle()
    pen_keyboard.hideturtle()
    pen_keyboard.penup()
    pen_keyboard.speed(0)
    turtle.hideturtle()
    turtle.penup()
    turtle.setpos(-200,200)
    turtle.pencolor('green')
    turtle.write('Зеленая буква - на нужной позиции',font=('Arial',18,'normal'))
    turtle.setpos(-200,170)
    turtle.pencolor('orange')
    turtle.write('Оранжевая буква - есть в слове',font=('Arial',18,'normal'))
    turtle.setpos(-200,140)
    turtle.pencolor('grey')
    turtle.write('Серая буква - отсутствует в слове',font=('Arial',18,'normal'))
    word = generate_word()
    user_word = ''
    attemp = 1
    while attemp <= 6 and user_word != word:
        user_word = ''
        pen_keyboard.clear()
        print_keyboard(55,0,12,pen_keyboard)
        print_keyboard(25,12,23,pen_keyboard)
        print_keyboard(-5,23,32,pen_keyboard)
        while user_word not in list_of_words:
            print()
            user_word = input('Введите слово из 5 букв: ').lower()
        check_attemp(user_word,word)
        attemp += 1
    turtle.setpos(-93,-120)
    if user_word == word:
        turtle.pencolor('ForestGreen')
        turtle.write('Вы угадали слово!', font=('Arial',18,'normal'))
    else:
        turtle.pencolor('red4')
        turtle.write('Вы не угадали слово: ' + word, font=('Arial',18,'normal'))

                                                   # основная часть программы
print('Привет! Давай играть в угадайку слов!')
print()
while input('Хотите сыграть? ').lower() == 'да':
    start_game()
