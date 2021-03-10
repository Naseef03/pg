import pyperclip


letters = 'abcdefghijklmnopqrstuvwxyz0123456789'
user_id = input('input for password: \n')
password = ''
for l in user_id:
    d = len(user_id)
    in_place = letters.index(l)
    if in_place % 2 == 0:
        d //= 2
    out_place = d + in_place
    if out_place > (len(letters) - 1):
        out_place -= len(letters)
    password += letters[out_place]
pyperclip.copy(password)
