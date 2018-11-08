from flask import Flask
from flask import redirect, url_for
from flask import request, make_response
from flask import render_template
from itertools import permutations as p
#scrabble word dictionary

app = Flask(__name__)

file = open('/usr/share/dict/american-english', 'r')
file = open('/usr/share/dict/british-english','r')

american = set(line.strip() for line in open('/usr/share/dict/american-english', 'r'))
british = set(line.strip() for line in open('/usr/share/dict/british-english', 'r'))



@app.route('/', methods=['GET','POST'])
def scrabble():
    #input should be 7 individual id characters from user
    return render_template('scrabble.html')

@app.route('/permutation', methods=['GET','POST'])
def permutation():
    wildcard = '*'
    permutation = []

    for letter in ["letter1", "letter2", "letter3", "letter4", "letter5", "letter6", "letter7"]:
        if request.form.get(letter) != '':
            permutation.append(request.form.get(letter))

    list_words = []
    for i in range(7):
        list_words+= list(p(permutation,i+1))
    
    joinList = []
    for word in list_words:
        joinList.append(''.join(word))

    #set joinList
    joinSet = set(joinList)
   
    newList = []

    total = 0
    mydictionary = request.form.get('dictionary')
    if mydictionary == 'british':
        for word in joinSet:
            if len(word) > 1:
                if word in british:
                    newList.append(word)
    else:
        if mydictionary == 'american':
            if len(word) > 1:
                for word in joinSet:
                    if word in american:
                        newList.append(word)

    scoreDict = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

    return_total = []
    for word in newList:
        total = 0
        for i in word:
            total = total+scoreDict[i]
        return_total.append(str(total))
    

    return render_template('scrabble.html', count = return_total, result = newList, myset = joinSet , words = newlist)
        



if __name__ == '__main__':
    app.run() 




