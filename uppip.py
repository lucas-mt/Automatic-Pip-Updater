import os
import sys
import tratuppip as tpip

sdist = False if len(sys.argv) == 1 else sys.argv[1]

print('this may take a while...')

if not os.path.exists('uppip.txt'):
    cmd = 'pip list --outdated > uppip.txt'
    os.system(cmd)

tpip.apresentável(sdist)


ask = input('do you confirm the upgrade? [Y/N] ').strip().lower()


if ask == 'y':
    tpip.trata(sdist)

    cmd = 'pip install -r tratuppip.txt --upgrade'
    os.system(cmd)

    tpip.apaga()

    print('Everything Good To Go!')

elif ask == 'n':
    print('ABORTED ACTION!')

else:
    print('OPTION NOT FOUND!')
