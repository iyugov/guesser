
import json

def ans_input(prompt):
    correct = False
    while not correct:
        ans = input(prompt + " [да/нет] ")
        correct = ans.lower() in ['д', 'да', 'н', 'нет']
        if not correct:
            print("Извини, я не очень понял ответ.")
    return ans.lower() in ['д', 'да']

print("Привет! Я Угадайка!")

try:
    with open("data.json", "r") as f:
        tree = json.load(f)
except:
    print("Не могу вспомнить, как играли в прошлый раз... Начну с простого.")
    tree = ["книга", None]

learned_new = False
play_round = True
while play_round:
    print("Загадай что-нибудь, а я буду отгадывать.")
    node = tree
    round_played = False
    while not round_played:
        if node[1] is None:
            if ans_input("Это %s?" % node[0]):
                print("Это %s! Ура, я угадал!" % node[0])
                guessed = True
            else:
                new_answer = input("Сдаюсь! Что же это? ")
                new_question = input("Подскажи вопрос, по ответу на который можно понять, чем различаются %s и %s: " % (new_answer, node[0]))
                new_question = new_question.rstrip("?")
                old_answer = node[0]
                node[0] = new_question
                if ans_input("Как нужно ответить на этот вопрос, если загадывается %s?" % new_answer):
                    node[1] = [[old_answer, None], [new_answer, None]]
                else:
                    node[1] = [[new_answer, None], [old_answer, None]]
                print("Спасибо! Буду знать!")
                learned_new = True
            round_played = True
            play_round = ans_input("Сыграем ещё раз?")
        else:
            node = node[1][1 if ans_input("%s?" % node[0]) else 0]

print("Спасибо за игру!")
if learned_new:
    try:
        with open("data.json", "w") as f:
            json.dump(tree, f)
    except:
        print("Как бы не забыть новое...")
    else:
        print("Я научился новому!")
