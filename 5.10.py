correct_users = ['man0', 'man1', 'man2', 'man3', 'man4']
new_users = ['Ваня', 'MaN0', 'Speeedvagoooon', 'man2', 'Таня']
for user0 in new_users:
    for user1 in correct_users:
        if user0.lower() == user1.lower():
            print('Поменяй имя, хлебушек')
            break
    else:
        print('Ку, добро пожаловать')
