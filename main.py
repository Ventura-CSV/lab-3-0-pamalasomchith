def main():
    ##################################################
    # Comlete your code here
    ##################################################
    result = int(input('Enter one integer value: '))

    if result < 0:
        print(f'The value {result} is an odd number')
    
    else:
        print(f'The value {result} is an even number')


    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
