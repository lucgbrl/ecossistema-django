def readCity():
    if not city:
        city = input('What is yout city name?\n\n')
        confirm = input('Are you right you are from: {}?'.format(city))
    
        if confirm == 'Y':
            print('There are {} chars in the Noun {}'.format(len(city),city))

def main():
    readCity()

if __name__ == "__main__":
    readCity()