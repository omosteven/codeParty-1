def reverseall(statement):
    statement = statement[::-1]
    return statement
#print(reverseall('hello guy'))

def maxmin(K):

    KthMax =max(K)
    print(KthMax)
    KthMin = min(K)
    print(KthMin)
#maxmin([1,3,23])


def extractbinary():
    Number = input('Enter Number')
    extracted = []
    for num in Number.split():
      for no in num:
        no = int(no)
        if no == 0:
            extracted.append(str(no))
        elif no == 1:
            extracted.append(str(no))
    print(''.join(extracted))
#extractbinary()


def roboticcheck(ticket):
    ticket = str(ticket)
    tic = []
    for letter in ticket:
        no = ord(letter)
        tic.append(no)
    tic = sum(tic)
    if tic%2 == 0:
        print('Enter')
    else:
        print('Sorry')



def mostfrequent(word):
    freq = {}
    for letter in word:
        freq.update({letter:word.count(letter)})
    if max(freq.values())==1:
        print('None')
    elif max(freq.values())>1:
        res = dict((v,k) for k,v in freq.items())
        print(res[max(freq.values())])
#mostfrequent('addee')

def Trafic(A,B):
    A,B = str(A),str(B)
    for a in A.split():
        print(a)
#Trafic('A L S 3 2','B S S 4 3')