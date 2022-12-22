spisot_imen = ['Лиза-Лиза', 'Польнарефф', 'ing Crimson', 'АдМэн', 'DIOOOO']

if spisot_imen:
    for imya in spisot_imen:
        if imya == 'АдМэн':
            print('Ку, админ, чекнем список пользователей, или выпьем чаю?')
        else:
            print(
                f'Здравстуйте, {imya}, благодарим '
                f'за регистрацию на данном ресурсе')
else:
    print('Нам нужно больше пользователей!')
