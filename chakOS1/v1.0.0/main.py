import recovery
import boot

with open('startup_data.txt', mode='r') as startup_data_file:
    startup_data = startup_data_file.read()

    if startup_data.lower() == '':
        startup_one_off = recovery.Recovery()

    elif startup_data.lower() == 'true':
        boot.Boot()

    else:
        corrupt_data = recovery.Recovery()
