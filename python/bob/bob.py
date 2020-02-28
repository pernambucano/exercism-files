def hey(phrase):
    phrase = [x for x in phrase if (x.isalpha() and x != ' ') or x == '?' or x == ',']
    if (len(phrase) == 0):
        return 'Fine. Be that way!'
    elif ('?' == phrase[-1]) and len(phrase[:-1]) > 0 and  (len([x for x in phrase[:-1] if x.isupper()]) == len([x for x in phrase[:-1]])):
        return  'Calm down, I know what I\'m doing!'
    elif ('?' == phrase[-1]):  
        return 'Sure.'
    elif (len([x for x in phrase if x.isdigit()]) != len([x for x in phrase if x.isalnum()])) and (len([x for x in phrase if x.isupper() and x.isalpha()]) == len([x for x in phrase if x.isalpha()])):
        return 'Whoa, chill out!'
    else:
        return 'Whatever.'