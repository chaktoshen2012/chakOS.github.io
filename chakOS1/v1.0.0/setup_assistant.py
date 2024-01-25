import time
import boot


class SetupAssistant:
    def __init__(self):
        with open('user_data.txt', mode='r') as user_info:
            user_info = user_info.read()
            if user_info.lower() == '':
                print('Welcome to chakOS!')
                print('We are going to take up a few minutes of your time to set up your '
                      'Chakintosh.\n\n')

                print('| chakOS v1.0.0 | Setup your Chakintosh | Create a user account |')
                print('----------------------------------------------------------------')

                time.sleep(1)
                print('\n\nLet\'s create you a user account, so that you have your very own '
                      'unique '
                      'and customisable chakOS profile!')

                time.sleep(2)

                self.first_name = input('First, enter your first name: ')
                print(f'Welcome to chakOS, {self.first_name}!')
                time.sleep(1)
                self.last_name = input('Now, please enter your last name: ')
                print(f'A noble family must descend from the {self.last_name} ancestors!')
                time.sleep(1)
                self.age = input('How old are you? ')

                while int(self.age) < 0 or int(self.age) > 150:
                    print('I\'m not sure that\'s a valid age.')
                    time.sleep(1)
                    print('\n\n\n')
                    self.age = input('How old are you? ')
                    print('\n\n\n')

                time.sleep(1)
                print('Thank you.')
                time.sleep(1)
                self.adjective = input('(For a bit of fun) How would you describe yourself, '
                                       'in one adjective? ').lower()

                print('Thank you for the information. Your user account has been created.')
                time.sleep(2)
                print('\n\n\n')
                print(f'Your current profile is: {self.first_name} {self.last_name}, age '
                      f'{self.age}, '
                      f'a very {self.adjective} person')

                print(f'Your all set, {self.first_name}! Have fun!')

                with open('user_data.txt', mode='w') as user_information:
                    user_information.write(f'{self.first_name}\n'
                                           f'{self.last_name}\n'
                                           f'{self.age}\n'
                                           f'{self.adjective}\n')

                boot.Boot()

            else:
                pass
