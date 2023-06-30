import os
import sys
import tratuppip as tpip

sdist = False if len(sys.argv) == 1 else sys.argv[1]

print('Isto pode demorar...')

if not os.path.exists('uppip.txt'):
    cmd = 'pip list --outdated > uppip.txt'
    os.system(cmd)

tpip.apresentável(sdist)


ask = input('deseja continuar com a atualização? [S/N] ').strip().lower()


if ask == 's':
    tpip.trata(sdist)

    cmd = 'pip install -r tratuppip.txt --upgrade'
    os.system(cmd)

    tpip.apaga()

    print('Atualização Finalizada!')

elif ask == 'n':
    print('MISSÃO ABORTADA!')

else:
    print('OPÇÃO NÃO ENCONTRADA!')
