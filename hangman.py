import random

# list tebakan
country = ['indonesia', 'malaysia', 'singapura', 'amerika', 'kanada', 'inggris', 'belanda', 'jepang', 'laos', 'mesir', 'arab', 'jerman']


# fungsi memilih secara acak 1 item yang beeada di
def choose(ls):
    choices = random.choices(ls)
    choosed = choices[0]
    return choosed


# fungsi unntuk membagi kata menjadi kumpulan huruf
def split(text):
    words = []
    words.extend(text)
    return words


# fungsi untuk membuat list tebakan
def guess(ls):
    guess = []

    for i in range(len(ls)):
        guess.append('')
    return guess



# main code
print('tebak nama negara\n'.title())
guess_word = choose(country)
split(guess_word)
guess = guess(guess_word)

while True:

    input_guess = input('masukan satu huruf: ')

    ls_index = [i for i, x in enumerate(guess_word) if x == input_guess]

    for j in range(len(ls_index)):
        guess[ls_index[j]] = guess_word[ls_index[j]]

    print(guess)
    if '' in guess:
        pass
    else:
        break

print('selamat anda berhasil'.upper())
