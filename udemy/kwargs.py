def fav_color(**colors):
    for person, color in colors.items():
        print ('{}\'s favorite color is {}'.format(person, color))
#    return ['{}\'s favourite color is {}'.format(person, color) for person, color in colors.items()]




fav_color(Mike='green', John='red', Alex='grey')
#print (fav_color(Mike='green', John='red', Alex='grey'))
