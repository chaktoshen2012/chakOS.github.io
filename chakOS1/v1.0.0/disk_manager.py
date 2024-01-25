import time
import random
import main_disk_info


class DiskManager:
    def __init__(self):
        self.main_disk = 'ssdchkntsh512gbd0'
        self.disk_name = 'disk0 partition 1'

    def format_disk(self):
        time.sleep(1)
        format_option = input('Choose an option: ')

        if str(format_option) == '1':
            time.sleep(1)
            print(f'Preparing to format disk \'{self.main_disk}\' as format \'CHKFS\'')
            time.sleep(1)
            print('Unmounting disk')
            time.sleep(1)
            print('Formatting...')
            time.sleep(1)

            print(f'{random.randint(1, 30)}%')
            time.sleep(1)
            print(f'{random.randint(30, 60)}%')
            time.sleep(1)
            print(f'{random.randint(60, 90)}%')
            time.sleep(1)
            print('100%')

            time.sleep(1)
            print(f'Formatted disk \'{self.main_disk}\' as \'CHKFS\'\n\n')

            main_disk_specs = main_disk_info.MainDisk()
            main_disk_specs.format = 'CHKFS'

        else:
            print('Sorry, that wan\'t a valid input. Shutting down device...')
            time.sleep(2)
            exit()
