# Способы вызова функции
def search_mail(a): # проверка -а- на содержание @, .com, .ru, .net
    t = False
    for i in range (0, len(a)):
        if a[i] == '@':
            t = True
    if (a[len(a)-4:len(a)] != '.net'
            and a[len(a)-4:len(a)] != '.com'
            and a[len(a)-3:len(a)] != '.ru'):
            t = False
    return t
def send_email(message, recipient, sender = 'university.help@gmail.com'):
    if (search_mail(recipient) == False) or (search_mail(sender) == False):
        print(f'Невозможно отправить письмо с адреса {sender} '
              f'на адрес {recipient}')
    elif sender == recipient:
        print(f'Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса '
              f'{sender} на адрес {recipient}')
    elif sender != 'university.help@gmail.com':
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса '
              f'{sender} на адрес {recipient}')
send_email('Это сообщение для проверки связи',
           'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!',
           'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание',
           'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре',
           'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')