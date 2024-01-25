import time
from tkinter import *
import os
import sys
import recovery
import main_disk_info
import disk_manager
import boot
import diagnostics


class Ui:
    def __init__(self):
        print('\n\n\n\n\n\n\n')

        with open('user_data.txt', mode='r') as user_file:
            user_data = user_file.readlines()
            first_name = user_data[0]

        print(f'Welcome, {first_name}'
              f'chakOS is filled with wonderful opportunities.')
        time.sleep(1)
        print('Learn more about Chakky at sites.google.com/view/chakkyinfo')

        time.sleep(1)

        is_on = True

        while is_on:
            print('What would you like to do first out of these options?\n'
                  '1. Open an app\n'
                  '2. Restart Chakintosh\n'
                  '3. Shut down Chakintosh\n'
                  '4. Set startup options')

            time.sleep(1)

            user_action = input('Choose an option: ')

            time.sleep(1)
            if user_action == '1':
                print('\n\n\n\n\n')
                print('Choose an app to open:\n'
                      '1. Notebook\n'
                      '2. Clock\n'
                      '3. Settings\n'
                      '4. chakOS Instruction Manual')

                time.sleep(1)

                app_to_open = input('Which app to open? ')

                time.sleep(1)

                if app_to_open == '1':
                    print('\n\n\n\n\n')
                    from tkinter import simpledialog
                    from datetime import datetime
                    from tkinter import messagebox

                    notebook_app = Tk()
                    notebook_app.title('chakOS Notebook v1.0.0')
                    notebook_app.config(padx=30, pady=30)

                    welcome_to_notes_label = Label(text='Welcome to Notes!',
                                                   font=('Times New Roman', 24, 'bold'))
                    welcome_to_notes_label.config(padx=20, pady=20)
                    welcome_to_notes_label.pack()

                    note_emoji = Label(text='📝', font=('Arial', 200, 'normal'))
                    note_emoji.config(padx=100)
                    note_emoji.pack()

                    def create_note():
                        current_time = datetime.now()
                        current_time = str(current_time)

                        datetime_list = []

                        for character in current_time:
                            datetime_list.append(character)

                        year_digit_one = datetime_list[0]
                        year_digit_two = datetime_list[1]
                        year_digit_three = datetime_list[2]
                        year_digit_four = datetime_list[3]

                        current_year = year_digit_one + year_digit_two + year_digit_three + year_digit_four

                        month_digit_one = datetime_list[5]
                        month_digit_two = datetime_list[6]

                        current_month = month_digit_one + month_digit_two

                        date_digit_one = datetime_list[8]
                        date_digit_two = datetime_list[9]

                        current_date = date_digit_one + date_digit_two

                        global user_datetime
                        user_datetime = f'{current_date}/{current_month}/{current_year}'

                        def save_note():
                            with open('notes.txt', mode='a') as notes:
                                notes.write(
                                    f'["{note_title} (Created on {user_datetime})", "{note_text.get("1.0", "end-1c")}"]\n')
                                note_text.config(relief='ridge')

                            note_text.pack_forget()
                            save_button.pack_forget()

                            messagebox.showinfo(title='Save successful', message='Your note was saved successfully!')

                        global save_button
                        save_button = Button(notebook_app, text='Save and close', command=save_note)
                        save_button.pack()

                        global note_title
                        note_title = simpledialog.askstring(title='Set a title',
                                                            prompt='What should the title be?')

                        global note_text
                        note_text = Text(notebook_app, height=10, width=50, foreground='black')
                        note_text.pack()

                    add_button = Button(notebook_app, text='Create a note...', command=create_note)
                    add_button.pack()

                    def open_note():
                        with open('notes.txt', mode='r') as notes:
                            all_notes = notes.readlines()
                            number_of_notes = len(all_notes)
                            number_of_notes = int(number_of_notes)

                            if number_of_notes == 0:
                                messagebox.showwarning(title='Oh dear', message='It looks like there aren\'t '
                                                                                'any available notes to choose '
                                                                                'from.')
                            else:
                                available_label = Label(text=f'''The available notes are:''')
                                available_label.pack()

                                note_count = 0

                                def note_opened():
                                    first_note.pack_forget()
                                    available_label.pack_forget()
                                    global new_note_text
                                    new_note_text = Text(notebook_app, height=10, width=50, foreground='black')
                                    first_note_list = [f'{all_notes[note_count - 1].replace("[]", "")}']
                                    new_note_text.insert(1.0, first_note_list[0].replace("\"\"", ""))
                                    new_note_text.pack()

                                def close_note():
                                    new_note_text.pack_forget()
                                    messagebox.showinfo(title='Operation Successful', message='The note '
                                                                                              'was closed '
                                                                                              'successfully.')
                                    close_button.pack_forget()

                                close_button = Button(notebook_app, text='Close the note...', command=close_note)
                                close_button.pack()

                                while note_count < number_of_notes:
                                    first_note = Button(text=f'{all_notes[note_count].replace("[]", "")}',
                                                        command=note_opened)
                                    first_note.pack()
                                    note_count += 1

                    open_note_button = Button(notebook_app, text='Open a previous note...', command=open_note)
                    open_note_button.pack()

                    notebook_app.mainloop()

                elif app_to_open == '2':
                    from datetime import datetime

                    time.sleep(1)
                    print('\n\n\n\n\n')

                    clock_app = Tk()
                    clock_app.title('chakOS Clock v1.0.0')
                    clock_app.config(padx=30, pady=30)

                    welcome_to_clock_label = Label(text='Welcome to Clock!',
                                                   font=('Times New Roman', 24, 'bold'))
                    welcome_to_clock_label.config(padx=20, pady=20)
                    welcome_to_clock_label.pack()

                    clock_emoji = Label(text='⏰', font=('Arial', 200, 'normal'))
                    clock_emoji.config(padx=100)
                    clock_emoji.pack()

                    current_time = str(datetime.now())
                    current_time = current_time[11:]
                    current_time = current_time[:8]

                    current_date = str(datetime.now())
                    current_date = current_date[:10]

                    time_label = Label(text=f'The current time is: {current_time}', font=('Times New Roman',
                                                                                          24, 'bold'))
                    time_label.pack()

                    if current_date[5] + current_date[6] == '01':
                        current_month = 'January'
                    elif current_date[5] + current_date[6] == '02':
                        current_month = 'February'
                    elif current_date[5] + current_date[6] == '03':
                        current_month = 'March'
                    elif current_date[5] + current_date[6] == '04':
                        current_month = 'April'
                    elif current_date[5] + current_date[6] == '05':
                        current_month = 'May'
                    elif current_date[5] + current_date[6] == '06':
                        current_month = 'June'
                    elif current_date[5] + current_date[6] == '07':
                        current_month = 'July'
                    elif current_date[5] + current_date[6] == '08':
                        current_month = 'August'
                    elif current_date[5] + current_date[6] == '09':
                        current_month = 'September'
                    elif current_date[5] + current_date[6] == '10':
                        current_month = 'October'
                    elif current_date[5] + current_date[6] == '11':
                        current_month = 'November'
                    elif current_date[5] + current_date[6] == '12':
                        current_month = 'December'
                    else:
                        current_month = ''

                    current_year = current_date[:4]

                    date_label = Label(text=f'The current date is: {current_date[8] + current_date[9]} '
                                            f'{current_month} {current_year}', font=('Times New Roman', 24,
                                                                                     'bold'))

                    date_label.pack()

                    def refresh():
                        global time_label
                        time_label.pack_forget()
                        global date_label
                        date_label.pack_forget()
                        current_time = str(datetime.now())
                        current_time = current_time[11:]
                        current_time = current_time[:8]

                        current_date = str(datetime.now())
                        current_date = current_date[:10]

                        time_label = Label(text=f'The current time is: {current_time}', font=('Times New Roman',
                                                                                              24, 'bold'))
                        time_label.pack()

                        if current_date[5] + current_date[6] == '01':
                            current_month = 'January'
                        elif current_date[5] + current_date[6] == '02':
                            current_month = 'February'
                        elif current_date[5] + current_date[6] == '03':
                            current_month = 'March'
                        elif current_date[5] + current_date[6] == '04':
                            current_month = 'April'
                        elif current_date[5] + current_date[6] == '05':
                            current_month = 'May'
                        elif current_date[5] + current_date[6] == '06':
                            current_month = 'June'
                        elif current_date[5] + current_date[6] == '07':
                            current_month = 'July'
                        elif current_date[5] + current_date[6] == '08':
                            current_month = 'August'
                        elif current_date[5] + current_date[6] == '09':
                            current_month = 'September'
                        elif current_date[5] + current_date[6] == '10':
                            current_month = 'October'
                        elif current_date[5] + current_date[6] == '11':
                            current_month = 'November'
                        elif current_date[5] + current_date[6] == '12':
                            current_month = 'December'
                        else:
                            current_month = ''

                        current_year = current_date[:4]

                        date_label = Label(text=f'The current date is: {current_date[8] + current_date[9]} '
                                                f'{current_month} {current_year}', font=('Times New Roman', 24,
                                                                                         'bold'))
                        date_label.pack()

                    refresh_button = Button(text='Refresh', command=refresh)
                    refresh_button.pack()

                    clock_app.mainloop()

                elif app_to_open == '3':
                    from tkinter import simpledialog

                    settings_app = Tk()
                    settings_app.title('System Settings')
                    settings_app.config(padx=10, pady=10)

                    settings_label = Label(text='System Settings', font=('Times New Roman', 24, 'bold'))
                    settings_label.config(padx=50, pady=50)
                    settings_label.pack()

                    settings_emoji = Label(text='⚙️', font=('Arial', 200, 'normal'))
                    settings_emoji.config(padx=20, pady=20)
                    settings_emoji.pack()

                    def open_profile_settings():
                        with open('user_data.txt', mode='r') as user_data:
                            user_data = user_data.readlines()
                            user_first_name = user_data[0]
                            user_last_name = user_data[1]
                            user_age = user_data[2]
                            user_adjective = user_data[3]

                            user_name = user_first_name + user_last_name

                            user_data_label = Label(text=f'''
                            Your full name is: {user_name}
                            Your age is: {user_age}
                            You describe yourself as: {user_adjective.lower()}
                            ''', font=('Arial', 15, 'normal'))
                            user_data_label.pack()

                            def change_details():
                                f_name = simpledialog.askstring(title='New name', prompt='What '
                                                                                         'should your '
                                                                                         'new first '
                                                                                         'name be?')

                                l_name = simpledialog.askstring(title='New name', prompt='What should '
                                                                                         'your new last '
                                                                                         'name be?')

                                age = simpledialog.askstring(title='New age', prompt='What is your new '
                                                                                     'age?')

                                dscrp = simpledialog.askstring(title='New description', prompt='What '
                                                                                               'would you'
                                                                                               ' describe'
                                                                                               ' yourself'
                                                                                               ' as now?')

                                user_data_label = Label(text=f'''
                                Your full name is: {f_name} {l_name}
                                Your age is: {age}
                                Your adjective/description is: {dscrp.lower()}
                                ''')
                                user_data_label.pack()

                            change_button = Button(text='Change my details...', command=change_details)
                            change_button.pack()

                    user_settings_button = Button(text='My Profile', command=open_profile_settings)
                    user_settings_button.pack()

                    settings_app.mainloop()

                elif app_to_open == '4':
                    time.sleep(1)
                    print('\n\n\n\n\n')
                    time.sleep(1)
                    print('''chakOS is a complex operating system, the world\'s most 
                             advanced piece of code ever written. With over 16
                             different files, each with more than 700 lines of code, 
                             chakOS is raising the computer industry standard.''')
                    time.sleep(2)

                    print('chakOS has an instruction manual, built just for you, so '
                          'that you can navigate through this machinery with ease.')

                    time.sleep(1)

                    right = False

                    while not right:
                        user_level = input('From a rating of 1 to 3, how would you rate '
                                           'your experience and knowledge of chakOS? '
                                           '1 is the least experienced and the least'
                                           'knowledge, while is 3 is the most experienced '
                                           'and the most knowledge.')

                        try:
                            user_level = int(user_level)

                        except:
                            print('Sorry, we only accept integers.')

                        else:
                            if user_level < 1 or user_level > 3:
                                print('Sorry, the integer must be from 1 to 3 '
                                      'inclusive.')
                            else:
                                right = True

                        finally:
                            print('Thank you. Your rating will help us to know '
                                  'what you require.')

                            right = True

                        if user_level < 5 and user_level > 0:
                            user_xp = 'Low'

                        elif user_level >= 5 and user_level < 8:
                            user_xp = 'Average'

                        elif user_level <= 10 and user_level >= 8:
                            user_xp = 'High'

                    time.sleep(1)

                    print('Here are the basics that you need to know:')

                    time.sleep(1)

                    print('\n\n\n')

                    time.sleep(1)

                    print('''
                    chakOS v1.0.0 has 3 GUI-based apps: Clock, Notebook, and Settings,
                    all of which that use the Tkinter library. chakOS also has the 
                    chakOS instruction manual, which is what you're using right now. 
                    
                    In the unlikely event of a hardware or software fault, your 
                    startup disk may become corrupt and the computer will automatically 
                    startup to the in-built recovery mode.
                    
                    The base system recovery partition cannot be erased, deleted, or 
                    removed from chakOS, and comes with every software package of each 
                    released version of chakOS.
                    
                    Startup options can be adjusted in the startup manager.
                    
                    Restarting in target disk mode will allow you to review all your 
                    startup disks and to startup from a different disk.
                    
                    Restarting in recovery mode will boot you up into the internal 
                    Recovery HD Partition, but this should only be used in the 
                    case of disk corruption.
                    
                    Restarting in the diagnostics utility will allow you to diagnose 
                    any abnormal hardware parts, software problems, or bugs and errors 
                    that may lead to disk malfunction, and eventually, corruption.
                    
                    Restarting into the NVRAM reset utility will allow you to reset 
                    the NVRAM/PRAM. A warning that this option should only be used 
                    by experts who have rated themselves higher than a 7.
                    
                    Restarting into the SMC reset utility will allow you to safely 
                    reset the SMC (System Management Controller). A warning that this 
                    option should only be used by experts who have rated themselves 
                    higher than a 5.
                    ''')

                    time.sleep(2)

                    print('\n\n\n\n')

                    time.sleep(5)

                else:
                    print('Sorry, that option isn\'t available yet.')
                    print('\n\n\n\n')
                    time.sleep(1)

            elif user_action == '2':
                time.sleep(1)
                print('\n\n\n')

                print('Restarting Chakintosh...')

                time.sleep(1)

                os.execv(sys.executable, ['python'] + sys.argv)

            elif user_action == '3':
                time.sleep(1)
                print('\n\n\n')

                print('Shutting down Chakintosh...')

                time.sleep(1)

                exit()

            elif user_action == '4':
                time.sleep(1)
                print('There are many startup options to choose from.')

                time.sleep(1)
                print('''
                Type 'o' for target disk mode
                Type 'r' for recovery mode
                Type 'd' for the diagnostics utility
                Type 'n' for the NVRAM reset utility
                Type 's' for the SMC reset utility
                Type 'c' to cancel.
                ''')

                time.sleep(1)
                print('\n\n\n\n')

                time.sleep(1)
                startup_mode = input('Choose an option: ').lower()

                if startup_mode == 'o':
                    time.sleep(1)
                    print('\n\n\n\n\n')

                    normal_disk = disk_manager.DiskManager()

                    disk_name = normal_disk.main_disk
                    disk_part = normal_disk.disk_name

                    normal_disk_again = main_disk_info.MainDisk()

                    disk_format = normal_disk_again.disk_format
                    disk_capacity = normal_disk_again.capacity

                    print(f'''
                    These are the available disks you can boot from:
                    1. {disk_name} ({disk_part}), with a capacity of {disk_capacity}, 
                    currently formatted as {disk_format}
                    ''')

                    time.sleep(1)

                    print('\n\n\n')

                    disk_to_boot_from = str(input('Choose a disk to boot from: '))

                    if disk_to_boot_from == '1':
                        boot.Boot()

                    else:
                        print('Sorry, that option isn\'t available yet.')

                elif startup_mode == 'r':
                    time.sleep(1)
                    print('\n\n\n\n\n')

                    recovery.Recovery()

                elif startup_mode == 'd':
                    time.sleep(1)
                    print('\n\n\n\n\n')

                    run_diagnostics = diagnostics.RunDiagnostics()

                elif startup_mode == 'n':
                    time.sleep(1)
                    print('\n\n\n\n\n')

                    print('Welcome to the NVRAM reset utility. We understand that you '
                          'are experiencing problems with your Chakintosh, or simply '
                          'want to reset the NVRAM just because. Either way, Chakky '
                          'will assist you to the best we can.')

                    time.sleep(1)
                    print('\n\n\n')

                    print('We are now performing a reset. Please don\'t turn off your '
                          'Chakintosh.')

                    time.sleep(2)
                    print('The NVRAM was reset successfully. Just sit back, relax, '
                          'and watch your computer work hard again.')
                    print('\n\n\n')

                elif startup_mode == 's':
                    time.sleep(1)
                    print('\n\n\n\n\n')

                    print('Welcome to the SMC reset utility. We understand that you '
                          'are experiencing problems with your Chakintosh, or simply '
                          'want to reset the SMC just because. either way, Chakky '
                          'will assist you to the best way we can.')

                    time.sleep(1)
                    print('\n\n\n')

                    print('We are now performing a reset. Please don\'t turn off your '
                          'Chakintosh.')

                    time.sleep(2)
                    print('The NVRAM was reset successfully. Just sit back, relax, '
                          'and watch your computer work hard again.')
                    print('\n\n\n')

                elif startup_mode == 'c':
                    time.sleep(1)

                else:
                    print('Sorry, that option isn\'t available yet.')

            else:
                print('Sorry, that option isn\'t available yet.')
