
import time
import random
# ця функція додасть інтерактиву в ваш чат і зробить його більш схожим на реальний.


def delay_print(s):
    for c in s:
        print(c, end='')
        time.sleep(random.random() * 0.01)
    print()

character_name = input("Вітаю! Введіть ім'я вашого персонажа.")
delay_print("Вітаю, " + character_name +
            "! Тобі належить вибрати свій шлях у невеликій грі, в результаті якої ти дізнаєшся який сік компанії Січко™ тобі підходить найбільше!")

# стати персонажа та ворогів
answers_array = []

# загальні дані про гілку діалогу
quest_index = 0

delay_print("Вітаю на першому рівні! До тебе підходить невідоме створіння, схоже на гнома, і каже:\n'Привіт, незнайомцю. Якщо ти хочеш пройти, то тобі потрібно відгадати загадку. Якщо ти не хочеш, то я тебе вб'ю.'")

print("Варіанти відповідей:\n1) 'Так, я хочу відгадати загадку.'\n2) 'Ні, я не хочу відгадувати загадку. (почати драку)'")


# загальні дані про гілку діалогу
answer = input("Введіть відповідь: ")
answers_array.append(answer)

match answer:
    case "1": 
        delay_print("Гном: 'У мами Івана було три сини. Першого звали Петро, другого – Василь. Як звали третього сина?'")
        print("Варіанти відповідей:\n1) 'Іван'\n2) 'Петро'\n3) 'Василь'")
        answer = input("Введіть відповідь: ")
    case '2':
        print("*Гном розмахується кулаком і ударяє вас по коліну.*")
        delay_print("Гном: 'Н-Н-Н-А-А-А!!!'")
        print("*Ви відчуваєте сильний біль в коліні але він не надто сильний*\n1. *пнути гнома з усієї сили ногою*\n2. Будь ласка!!! Не бий! Я відповім на твою загадку!!!")
        answer = input("Введіть відповідь: ")
    case _: delay_print("Гном: 'Шо ти там бормочеш??!!'")

# загальні дані про гілку діалогу
quest_index = 1
previous_answer = answers_array[quest_index - 1]



answers_transformed = [int(i) for i in answers_array]



if sum(answers_transformed) == 1:
    answers_array.append(answer)
    

    match answer:
        case "1": 
            delay_print("Гном: 'Ура ти відгадав молодець'")
            exit(0)
        case '2':
            print("Гном: 'Відповідь не правильна")
            exit(0)
        case '3':
            print("Гном: 'Відповідь не правильна")
            exit(0)
        
        case _: 
            delay_print("Гном: 'Шо шо??!!'")
            exit(0)
else:
     answers_array.append(answer)
     
    
     match answer:
        case "1": 
            delay_print("Гном: 'Ти мене виграв('")
            exit(0)
        case '2':
            print("Гном: 'Ну тоді погнали")
            delay_print("Гном: 'У мами Івана було три сини. Першого звали Петро, другого – Василь. Як звали третього сина?'")
            print("Варіанти відповідей:\n1) 'Іван'\n2) 'Петро'\n3) 'Василь'")
            answer = input("Введіть відповідь: ")
            answers_array.append(answer)
        
        case _: 
            delay_print("Гном: 'Шо шо??!!'")
            exit(0)
         
         




quest_index = 2
previous_answer = answers_array[quest_index - 1]



answers_transformed = [int(i) for i in answers_array]



match answer:
    case "1": 
        delay_print("Гном: 'Ура ти відгадав молодець'")
    case '2':
        print("Гном: 'Відповідь не правильна")
    case '3':
        print("Гном: 'Відповідь не правильна")
        
    case _: delay_print("Гном: 'Шо шо??!!'")



         
