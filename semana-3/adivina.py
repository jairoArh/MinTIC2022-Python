import random

images = ['''
    +---+
    |   |
        |
        |
        |
        |
        ======''','''
    +---+
    |   |
    O   |
        |
        |
        |
        ======''','''
    +---+
    |   |
    O   |
    |   |
        |
        |
        ======''','''
    +---+
    |   |
    O   |
    |   |
   /|   |
        |
        ======''','''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
        ======''','''
    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        ======''','''
    +---+
    |   |
    O   |
   /|\  |
   /|   |
        |
        ======''','''
    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        ======
        '''
]

words = ('COLOMBIA',
         'REPUBLICA',
         'VERANO',
         'MISIONTIC',
         'PUBLICIDAD',
         'PROGRAMADOR',
         'PYTHON',
         'SOGAMOSO',
         'COMPUTADOR',
         'DESARROLLANDO',
         'SOFTWARE',
         'PROCESOS')

print('B I E N V E N I D A(0)   A L  J U E G O  D E   A D I V I N A R   P A L A B R A S')

word = words[random.randrange(len(words))]

tries = 0

hiddenword = ['_'] * len(word)

found = False

exit = False

while not exit:
  print(images[tries])
  print('')
  print(hiddenword)
  print('----*' * 10 )
  current_letter = input('Digite una Letra para una palabra de %d caracteres ' % len(word)).upper()
  letter_index = []
  for i in range(len(word)):
    if word[i] == current_letter:
      letter_index.append(i)

  if len(letter_index) > 0:
    for i in letter_index:
      hiddenword[i] = current_letter
  else:
      tries += 1
      if tries == len(images):
        exit = True
  
  if '_' not in hiddenword:
    found = True
    exit = True

if found:
  print('¡¡¡¡EUREKA!!!! - Palabra Encontrada')
else:
  print(f'La Palabra era %s' % word )