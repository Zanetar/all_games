from random import *
import random

class Game:
    def __int__(self,name,level):
        self.name=name
        self.level=level


class Rock_paper_scissors(Game):
    def __int__(self, name,level):
        super().__init__(name,level)

    def __repr__(self):
        return('Gra znajdź liczbę. Dowiedz się jaką cyfrę wylosował komputer')


    def rules(self):
        print('Witaj w grze KAMIEŃ,NOŻYCZKI,PAPIER')
        print('W każdej turze gracz wybiera jeden z symboli:' 
              'kamień '
              'nozyczki '
              'papier. ')
        print('Nastepnie komputer dokonuje własnego wyboru. '
              'Nastepuje konfrontacja symboli. ')
        print('Gracz, który pokazał silniejszy symbol otrzymuje punkt. '
              'W przypadku dwóch tych samych symboli mastępuje remis. ')
        print('Wygrywa gracz, który jako pierwszy zdobędzie 3 punktyt.'
              'Powodzenia!')


    def exit(self):
        exit=int(input('Czy chcesz zagrać w grę? 1-T,0-N'))
        return exit

    def game(self):
        user_points=[]
        comp_points=[]
        while True:
            sum_user=sum(user_points)
            sum_comp=sum(comp_points)
            if sum_user==3 and sum_comp<3:
                print('Wygrałeś grę GRATULACJE')
                break
            elif sum_comp==3 and sum_user<3:
                print('Przegrałeś grę. Zagraj jeszcze raz!')
                break
            elif sum_comp==3 and sum_user==3:
                print('REMIS!')
                break
            print('Wybierz właściwy symobl:')
            try:
                choose=int(input('dla nożyczek wybierz 1, dla kamienia wybierz 2, dla papieru wybierz 3'))
                if choose == 1:
                    print('Wybrałeś nożyczki')
                elif choose == 2:
                    print('Wybrałeś kamień')
                elif choose == 3:
                    print('Wybrałeś papier')
                else:
                    print ('Wybrałeś zły znak!')
                    break
                print('Następuje losowanie przez komputer...')
                choose_comp = randint(1, 3)
                if choose_comp == 1:
                    print('Komputer wylosował nożyczki')
                    if choose==choose_comp:
                        print('REMIS')
                        user_points.append(1)
                        comp_points.append(1)
                    elif choose==3:
                        print('PRZEGRAŁEŚ')
                        comp_points.append(1)
                    elif choose==2:
                        print('WYGRAŁEŚ')
                        user_points.append(1)
                elif choose_comp==2:
                    print('Komputer wylosował kamień')
                    if choose==choose_comp:
                        print('REMIS')
                        user_points.append(1)
                        comp_points.append(1)
                    elif choose==3:
                        print('WYGRAŁEŚ')
                        user_points.append(1)
                    elif choose==1:
                        print('PRZEGRAŁEŚ')
                        comp_points.append(1)
                elif choose_comp==3:
                    print('Komputer wylosował papier')
                    if choose==choose_comp:
                        print('REMIS')
                        user_points.append(1)
                        comp_points.append(1)
                    elif choose==1:
                        print('WYGRAŁEŚ')
                        user_points.append(1)
                    elif choose==2:
                        print('PRZEGRAŁEŚ')
                        comp_points.append(1)
                else:
                    print('WYBRAŁEŚ ZŁY ZNAK')
            except: print('WYBRAŁEŚ ZŁY ZNAK')

def menu_rock(object):
    try:
        while True:
            object.rules()
            object.game()
            a=object.exit()
            if a==0:
                print('Dziękujemy za grę')
                break
            elif a==1:
                pass
            elif a !=1 and a !=0:
                print('Wybrałeś zły znak.Jeżeli chcesz zagrać, to ponownie uruchom grę!!')
                break
    except: print('Wybrałeś zły znak. Jeżeli chcesz zagrać, to ponownie uruchom grę!!')


class Find_number(Game):
    def __int__(self, name,level,age):
        super().__init__(name,level,age)

    def __repr__(self):
        return('Gra znajdź liczbę. Dowiedz się jaką cyfrę wylosował komputer')
    def rules(self):
        print('Witaj w grze')
        print ('Za chwile komputer wylosuje liczbę całkowitą z zakresu 1-100.')
        print('Twoim zadaniem jest odgadnięcie tej właśnie liczby')
        print('Sam decydujesz ile prób potrzeba Ci na jej odgadnięcie')


    def choose(self):
        while True:
            try:
                choose=int(input('Wpisz liczbę prób z zakresu od 1-10, lub 0 aby przerwać'))
                if choose >=1 and choose<=10:
                    print(f'Twoja liczba prób to {choose} razy')
                    break
                    return choose
                elif choose== 0:
                    break
            except: print('Wprowadzono zły znak!')
        return choose

    def game(self,object):
        number= randint(1, 100)
        start=object.choose()
        while True:
            if start==0:
                print('Gra przerwana!')
                break
            try:
                players_number = int(input('Wprowadź swoją propzycję'))
                print(f'pozostało Ci {start} żyć')
                start = start - 1
                if number ==players_number:
                    print('wygrałeś!')
                    break
                elif number >players_number:
                    print('wylosowana liczba jest większa')
                    if start <= 0:
                        print('przegrałeś')
                        break
                elif number < players_number:
                    print('wylosowana liczba jest mniejsza')
                    if start == 0:
                        print('przegrałeś')
                        break
            except: print ('Wybrano zły znak!')


    def end(self):
        try:
            print('Czy chcesz grać dalej? Tak-1, Nie-0')
            anwser=int(input())
            if anwser==1 or anwser==0:
                return anwser
            else:
                print('Wybrałeś zły znak')
        except:
            print('Wybrałeś zły znak')

def menu_find(object):
    while True:
        object.rules()
        if object.game(object)==0:
            print('Do widzenia!')
            break
        else:
            if object.end()==0:
                print('Do widzenia!')
                break




class Hangman(Game):
    def __int__(self, name,level):
        super().__init__(name,level)

    def __repr__(self):
        return('Gra polega na odgadnięciu ukrytego wyrazu.')

    def print_1(self):
        print('------')
        print('|   |')
        print('|   O')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('----------')

    def print_2(self):
        print('------')
        print('|   |')
        print('|   0')
        print('|---+---')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('----------')

    def print_3(self):
        print('------')
        print('|   |')
        print('|   O')
        print('|---+---')
        print('|   |')
        print('|')
        print('|')
        print('|')
        print('|')
        print('----------')

    def print_4(self):
        print('------')
        print('|   |')
        print('|   O')
        print('|---+---')
        print('|   |')
        print('|   |')
        print('|')
        print('|')
        print('|')
        print('----------')

    def print_5(self):
        print('------')
        print('|   |')
        print('|   O')
        print('|---+---')
        print('|   |')
        print('|   |')
        print('|  |')
        print('|  |')
        print('|')
        print('----------')

    def print_6(self):
        print('------')
        print('|   |')
        print('|   O')
        print('|---+---')
        print('|   |')
        print('|   |')
        print('|  | |')
        print('|  | |')
        print('|')
        print('----------')

    def rules(self):
        print('Witaj w grze Wisielec')
        self.print_6()
        print('Twoim zadaniem jest odgadnięcie hasła, ukrytego przez komputer.')
        print('Wpisuj propozycję liter, które twoim zdaniem występują w ukrytym wyrazie')
        print('W przypadku, kiedy podasz błędną literę, komputer dorysuje kolejne części szubienicy')
        print('Gdy komputer skończy swój rysunek- przegrywasz')
        print('Masz tylko 6 żyć!')

    def difficulty_level(self):
        print('Wybierz poziom trudności')
        print('1-łatwy')
        print('2-średni')
        print('3-zaawansowany')
        level = int(input())
        return level

    def words(self,document):
        with open(document) as file:
            file = file.readlines()
            file = [i.rstrip('\n') for i in file]
            word = random.choice(file)
            return word

    def exit(self):
        self.print_6()
        exit = int(input('Czy chcesz zagrać w grę? 1-T,0-N'))
        return exit

    def game(self,word):
        wrong_anwsers = 6
        word = list(word)
        letters = list(word)
        print('TWOJE HASŁO')
        print(len(letters) * ' _ ')
        for i in range(len(letters)):
            letters[i] = '_'
        used_letters = []
        while True:
            proposed_letter = str(input('Wpisz swoją propozycję litery'))

            if proposed_letter in word:
                for i in range(len(word)):
                    if word[i] == proposed_letter:
                        letters[i] = proposed_letter
                        print(f'dobrze!{letters}')
                if letters == word:
                    a = (' '.join(word))
                    print(f'Wygrałeś grę.Szukane słowo to:   {a} .   GRATULACJE!')
                    break

            else:
                used_letters.append(1)
                print('Źle!')
                print(f'Wykorzystałeś już {sum(used_letters)}. Pozostało Ci{wrong_anwsers - sum(used_letters)}')
                print(letters)
                if sum(used_letters) == 1:
                   self.print_1()
                elif sum(used_letters) == 2:
                    self.print_2()
                elif sum(used_letters) == 3:
                    self.print_3()
                elif sum(used_letters) == 4:
                    self.print_4()
                elif sum(used_letters) == 5:
                    self.print_5()
                elif sum(used_letters) == 6:
                    self.print_6()
                    print(f'Przegrałeś grę! Szukane słowo to:     {word}')
                    break

    def exit(self):
        print('Dziękujemy za grę.')
        exit = int(input('Czy chcesz zagrać jeszcze raz? 1=T/0=N'))
        return exit

def menu_hang(object):
    try:
        while True:
            object.rules()
            difficult = object.difficulty_level()
            if difficult == 1:
                word = object.words('words.txt')
                object.game(word)
            elif difficult == 2:
                word = object.words('words2.txt')
                object.game(word)
            elif difficult == 3:
                word = object.words('words3.txt')
                object.game(word)
            x = object.exit()
            if x == 0:
                break
            elif x == 1:
                pass
            else:
                print('Podałeś zły znak. Uruchom grę ponownie')
                break
    except: print('Wybrano zły znak!')



first_game=Rock_paper_scissors()
second_game=Find_number()
third_game=Hangman()

def games():
    try:
        while True:
            print('Witaj w sekcji gra')
            print('Wybierz grę, w którą chcesz zagrać bądź 0, by wyjść')
            print('Papier, nożyczki, kamień-------1')
            print('Zgadnij liczbę-------2')
            print('Wisielec--------3')
            choice=int(input())
            if choice==0:
                break
            elif choice==1:
                menu_rock(first_game)
            elif choice==2:
                menu_find(second_game)
            elif choice==3:
                menu_hang(third_game)
            elif choice==0:
                break
            else:
                print('Wybrałeś zły znak')
                break
    except: print('Wybrałeś zły znak!')

games() #wywołanie programu
