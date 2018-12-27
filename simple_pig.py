#Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
#
#Examples
#pig_it('Pig latin is cool') # igPay atinlay siay oolcay
#pig_it('Hello world !')     # elloHay orldway !

def pig_it(text):
    splitted = text.split()
    res =  ' '.join([word[1:]+word[:1]+'ay' for word in splitted if ('?' not  in word) and ('!' not in word)])
    if '?' in text:
        return res + ' ?'
    elif '!' in text:
        return res + ' !'
    else: return res