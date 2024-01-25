import time
import preboot


class RunDiagnostics:
    def __init__(self):
        disk = 'corrupt'
        software = 'corrupt'
        time.sleep(1)
        print('Directing you to the chakOS diagnostics utility...')
        time.sleep(1)

        preboot_check = preboot.Preboot()

        diagnostic = ''

        if not preboot_check.corrupted:
            diagnostic = 'pass'

        else:
            diagnostic = 'fail'

        if diagnostic == 'pass':
            time.sleep(1)
            print('\n\n\n')
            print('It seems that your Chakintosh is completely fine. The chakOS '
                  'diagnostics utility could not detect any problems or errors. '
                  'If you suspect something, please contact Chakky support.')

        else:
            time.sleep(2)
            print('\n\n\n')
            print('It seems that Chakintosh is corrupt. Take it to an authorised '
                  'Chakky service provider or contact Chakky support as soon as '
                  'possible, before complications occur. We\'ll sort it out for you.')
