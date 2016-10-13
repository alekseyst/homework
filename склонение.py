word = input ('Enter a word: ')
if word.endswith ('а') or word.endswith ('я'):
    print ('Nom.Sg')
elif word.endswith ('ы') or word.endswith ('и'):
    print ('Gen.Sg')
elif word.endswith ('е'):
    print ('Dat.Sg/Prep.Sg')
elif word.endswith ('у') or word.endswith ('ю'):
    print ('Acc.Sg')
elif word.endswith ('а') or word.endswith ('я'):
    print ('Inst.Sg')
elif word.endswith ('ы') or word.endswith ('и'):
    print ('Nom.Pl')
elif word.endswith ('ь'):
    print ('Gen.Pl/Acc.Pl')
elif word.endswith ('ам') or word.endswith ('ям'):
    print ('Acc.Pl')
elif word.endswith ('а') or word.endswith ('я'):
    print ('Nom.Sg')
