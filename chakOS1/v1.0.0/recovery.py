import os
import sys
import time
import preboot
import boot
import random
import setup_assistant
import main_disk_info
import disk_manager


class Recovery:
    def __init__(self):
        checker = preboot.Preboot()
        print('Welcome')
        time.sleep(3)

        print('chakOS v 1.0.0')
        time.sleep(1)

        logo = '''        __          __   ____  _____
          _____/ /_  ____ _/ /__/ __ \/ ___/
         / ___/ __ \/ __ `/ //_/ / / /\__ \ 
        / /__/ / / / /_/ / ,< / /_/ /___/ / 
        \___/_/ /_/\__,_/_/|_|\____//____/  
                                            '''
        print(logo)

        checker.check()
        time.sleep(2)

        if checker.corrupted:
            print('We\'re sorry, something went wrong during the boot process and '
                  'your device needed to enter the in-built recovery system. Don\'t '
                  'force shutdown \nyour Chakintosh.')
        else:
            normal = boot.Boot()

        while checker.corrupted:
            time.sleep(2)

            print('''These are your options:
            1. Select boot disk
            2. Install the latest compatible version of chakOS
            3. Format a disk
            4. Restart device
            5. Shut down device
         ''')

            option = input('Choose an option: ')

            if str(option) == '1':
                print('\n\n\n\n\n\n\n\n')
                print('Loading disks...')
                time.sleep(2)

                print('''These are your options:
                1. disk0 (Main hard drive)
                    512 GB SSD Storage
                    Chakintosh Hard Disk
                    Format: CHKFS
                2. Return
                ''')

                boot_disk = input('Choose an option: ')

                while str(boot_disk) == '1':
                    print('Sorry, this disk does not have a version of chakOS, macOS, '
                          'Windows, or Linux installed on it.')
                    time.sleep(2)

                    print('''These are your options:
                    1. disk0 (Main hard drive)
                        512 GB SSD Storage
                        Chakintosh Hard Disk
                        Format: CHKFS
                    2. Return
                        ''')
                    boot_disk = input('Choose an option: ')

                if str(boot_disk) == '2':
                    pass
                else:
                    print('Sorry, that wasn\'t a valid input.')

            elif str(option) == '2':
                print('\n\n\n\n\n\n\n\n')
                print('Checking hardware eligibility...')
                time.sleep(1)
                print('Loading available OSes...')
                time.sleep(1)

                print('''These are your options:
                1. chakOS v1.0.0
                2. Return
                ''')

                os_to_install = input('Choose an option: ')
                if str(os_to_install) == '1':
                    print('Preparing chakOS v1.0.0...')
                    time.sleep(5)
                    print('Downloading chakOS v1.0.0...')
                    time.sleep(2)
                    print(f'{random.randint(1, 30)}%')
                    time.sleep(2)
                    print(f'{random.randint(30, 60)}%')
                    time.sleep(2)
                    print(f'{random.randint(60, 90)}%')
                    time.sleep(2)
                    print('100%')
                    time.sleep(2)
                    print('\n\n\n\n\n\n\n\n\n')

                    with open('startup_data.txt', mode='w') as boot_log:
                        boot_log.write('True')

                    boot.Boot()

                    checker.chakOS_version = 'v1.0.0'
                    checker.check()
                    print('\n\n\n\n\n\n\n\n\n')

                    setup = setup_assistant.SetupAssistant()

                elif str(os_to_install) == '2':
                    pass

                else:
                    print('Sorry, that wan\'t a valid input. Shutting down device...')
                    time.sleep(2)
                    exit()

            elif str(option) == '3':
                time.sleep(1)
                print('''Format options:
            1. CHKFS (Chak File System)
                        ''')
                print('\n\n')

                disk_info = main_disk_info.MainDisk()
                disk_formatter = disk_manager.DiskManager()
                time.sleep(1)
                disk_formatter.format_disk()

            elif str(option) == '4':
                time.sleep(1)
                print('Restarting your Chakintosh...')
                time.sleep(2)
                print('\n\n\n\n\n\n')
                time.sleep(2)
                os.execv(sys.executable, ['python'] + sys.argv)

            elif str(option) == '5':
                time.sleep(2)
                print('Shutting down your Chakintosh...')
                time.sleep(2)
                exit()

            else:
                time.sleep(1)
                print('Sorry, but that is an invalid input.')
