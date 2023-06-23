def main():
    
    celcius = input('Enter Celcius: ')
    fahrenheit = (9 / 5) * float(celcius) + 32
    print (f'Fahrenheit: \t {fahrenheit:.2f}')
    
    return float(celcius), fahrenheit



if __name__ == '__main__':
    main()
