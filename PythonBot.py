# https://tproger.ru/quiz/kakoe-u-vas-totemnoe-zhivotnoe/?utm_source=site&utm_medium=banner&utm_campaign=totem_test&utm_content=fixed
def questions():
    question_list=[
    '1 Начало рабочего дня. К вам подходит совсем ещё зелёный стажёр и просит помочь с одной задачей. Согласитесь?',
    "2 Какое рабочее место лучше всего для вас подходит?",
    "3 Вы только что закончили проект, но в коде осталось много мусора, а кодстайл похож на джазовую импровизацию. Будете заниматься рефакторингом и уборкой в коде?\n",
    '4 Что вас больше всего раздражает, пока вы работаете?',
    '5 Если на работе появляется свободное время, то чем займётесь?\n',
    "6 Где вам комфортнее работать?\n",
    "7 Как часто вы меняете проекты?\n",
    '8 Ваш рабочий день закончился. Чем займётесь?'
    ]
    for i in question_list:
        print("#"*100)
        print(i)


    # for i in question_list:
    #     print("#"*100)
    #     print(i)
    #     answer()

def answer():
    answer_list = [
    "0: Да, почему бы нет. Свою работу разноображу и заодно юнцу помогу. \n"
    "1: Помогу, но только ближе к вечеру. С утра у самого ещё котелок не варит.\n"
    "2: Откажу ему. Пускай это грубо, но стажёр должен учиться справляться сам, а не постоянно бегать за помощью",

    "0:Стремлюсь к минимализму. На столе не должно быть ничего, что отвлекало бы меня. \n"
    "1: Рабочее место — это мой компьютер. Всё остальное не имеет значения. Могу хоть на коленках кодить.\n"
    "2: Всё, как у тру-программистов: мониторов побольше, две клавиатуры, несколько фиджет-игрушек.\n",

    "0: Разумеется. Код должен быть чистым и понятным, иначе в нём даже сам программист может запутаться. \n"
    "1: Главное правило инженера гласит: «Работает — не трогай!». Лучше отведу рабочее время на что-то более полезное.\n"
    "2: У меня ещё много работы, поэтому попрошу помощи у коллеги. Я ему неоднократно помогал, поэтому, думаю, он мне не откажет.\n",

    "0: Мне вообще ничего не мешает. Если я сел работать — я буду работать. \n"
    "1: Не могу нормально работать в шумной обстановке. Приходится уединяться в тихой комнате, где меня никто и ничто не отвлекает.\n"
    "2: Надоедливые коллеги. То помощи попросят, то на перекур зовут. Не дают нормально сосредоточиться.\n",

    "0: Свободного времени на работе у меня нет. Если не занимаюсь одним проектом, то сразу переключаюсь на другой. В крайнем случае почитаю что-нибудь полезное или займусь фитнесом. \n"
    "1: Схожу на перекус с другими коллегами. Мне нравится проводить с ними время, болтать о всяком.\n"
    "2: Полистаю ленту в поисках смешных мемов или поиграю во что-нибудь. Ведь если не отдыхать на работе, то можно быстро выгореть.\n",

    "0: В офисе. Там уютная рабочая обстановка, а рядом с коллегами всегда работается легче.  \n"
    "1: Дома. Там уютно, никто не отвлекает. А главное — можно работать с гибким графиком.\n"
    "2: Не имеет значения. Если в помещении есть Wi-Fi, то оно годится для работы. А на крайний случай и блокнот сойдёт. Бумажный.\n",

    "0: Не могу долго задерживаться на одном проекте. Либо надоедает, либо выгораю. Поэтому приходится постоянно двигаться.\n"
    "1: Вообще не люблю менять проекты. Быстро привыкаю к коллективу и не люблю лишних потрясений. \n"
    "2: Зачем уходить с одного проекта в другой, если можно быть на двух одновременно?\n",

    "0: Рабочий день закончился, но жизнь только начинается — у меня грандиозные планы до самого утра. \n"
    "1: Я могу кодить не только для работы, но и для души. У меня несколько пет-проектов, которые ждут моего внимания. Займусь ими.\n"
    "2: Всегда по-разному. Могу сходить на пробежку, в спортзал или выбраться на природу и что-нибудь приготовить.\n"]

    for id_answ in answer_list:
        print(id_answ[2])



def main():
    print("Какое у вас тотемное животное в программировании?")
    questions()
    answer()

if __name__ == '__main__':
    main()


#############################################
