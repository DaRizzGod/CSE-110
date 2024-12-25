friends = []

friend = ''

while friend != 'end':
    friend = input('Who is your friend? ')
    if friend != 'end':
        friends.append(friend)

friends.sort()
print('Here are your friends.')
for friend in friends:
    print(friend)

