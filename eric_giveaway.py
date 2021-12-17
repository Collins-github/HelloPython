import random
from time import sleep

number_of_digits = 4
trial_limit = 10

#opening remarks
instructions = f'''
    Hi! My name is Eric and I would be giving away $50,000 cash to you if you can win my game.
    
    Whoa!!! Yay!!!
    
    Like every other legitimate giveaway, you'll have to work for this one.
    
    I have begun processing a transaction to transfer $50,000 to your account/wallet.
    
    What is left to do is type in my pin and the recipient account details and that is my game!

    My pin is a {number_of_digits}-digit number with no repeated digits.
    
    You have {trial_limit} trials to get it.
    
    Otherwise, the system will terminate the transaction and you lose the money.
    
    I would be giving you some clues tho.
    
    These are my clues.
    
    When I say, 
    
    'Uhmm...', it means a digit is correct but in the wrong position.
    
    'Ahah!' means a digit is correct and in the right position.
    
    'Nada' means none of the digits you guessed is correct.

    So if my pin is 1267 and you guessed 2037, the hint would be 'Ahah! Uhmm...'.
    
    Ready? Let's go.

    Good luck!
    
    '''
processes = '''
    Initializing a new transaction...
    >>>
    Transaction amount: $50,000.00
    >>>
    Processing...
    >>>
    Verifying if amount is transferable...
    >>>
    Cross-checking amount against account balance...
    >>>
    Amount is transferable!
    >>>
    Proceeding with transaction...
    >>>
    Input pin:

    '''

#closing remarks
validation_message = '''
    Verifying pin...
    >>>
    Pin is valid.
    >>>
    Proceeding with transaction...
    >>>
    '''
trial_limit_message = '''
    >>>
    >>>
    >>>

    Too many failed attempts...
    
    System detected suspicious activity...
    
    Probable cyberattack...
    
    Transaction terminated!

    Temporary system shutdown.
    
    3

    2

    1

    
'''

#error messages
error_intro = '''
    A problem occurred.
    '''
timeout_error = '''    
    Error: System timeout
           Try again later
           Transaction terminated!
    '''
crash_error = '''    
    Error: System crashed
           Transaction terminated!
    '''
processing_error = '''   
    Error: System process failed
           Transaction terminated!
    '''
unavailable_error = '''   
    Error: System unavailable at the moment
           Try again later
           Transaction terminated!
    '''
not_responding_error = '''
    Error: System not responding
           Try again later
           Transaction terminated!
    '''
error_outro = '''
    Contact support team: @collinsezedike on Twitter or Github
    '''
loading = '''
    Processing...
    
    Please wait...
'''

#a list of the error messages
error_messages = [timeout_error, crash_error, processing_error, unavailable_error, not_responding_error]

#this decides what message would be printed
error_message = error_intro + random.choice(error_messages) + error_outro


def main():
    slowmo(instructions, 0.03)
    input('Press ENTER to continue ')
    number_of_trials = 1
    pin = get_pin_function()
    print(loading)
    slowmo(processes, 0.1)
    while number_of_trials <= trial_limit:
        guess = ''

        while len(guess) != number_of_digits or not guess.isdecimal():
            print(f'Number of trials: {number_of_trials}')
            guess = input('> ')

        hint = get_hint_function(guess, pin, number_of_trials, trial_limit)
        print(hint)
        number_of_trials += 1
        if guess == pin:
            successful()
            break
    else:
        return unsuccessful()


def get_pin_function():
    number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    random.shuffle(number_list)
    pin = ''

    for i in range(number_of_digits):
        pin += number_list[i]
    return pin


def get_hint_function(guess, pin, number_of_trials, trial_limit):
    if guess == pin: 
         # returning an empty string so that Python would not display 'None'
         # returning 'pass' also displays 'None'
         return ''
    elif number_of_trials == trial_limit:
    	return "You have reached the trial limit!"
    else:
        hint = []
        for i in range(len(guess)):
            if guess[i] == pin[i]:
                hint.append('Ahah!')
            elif guess[i] in pin:
                hint.append('Uhmm...')
        if len(hint) == 0:
            return 'Nada'
        else:
            hint.sort()
            return ' '.join(hint)


def successful():
    print(loading)
    slowmo(validation_message, 0.1)
    input('Press ENTER to continue ')
    for i in range(0,50001):
        print(f'${i:,}.00')
    print(f'\n${i:,}.00')
    input('\nSpecify what way you would like to receive the money (e.g Crypto, Bank transfer, Paypal, etc.) ')
    print(loading)
    return slowmo(error_message, 0.01)


def unsuccessful():
    print(loading)
    sleep(5)
    slowmo(trial_limit_message, 0.01)


def slowmo(text, seconds):
    for i in text:
        print(i, end="")
        sleep(seconds)


if __name__ == '__main__':
   main()