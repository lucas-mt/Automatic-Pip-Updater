import shutil
import os

def apresentável(sdist: bool = False):
    with open('uppip.txt', 'r', encoding='utf-8') as uppip:
        leitor = uppip.readlines()

        if not sdist:
            for pkg in leitor:
                if 'sdist' not in pkg:
                    print(pkg)
        else:
            for pkg in leitor:
                print(pkg)


def trata(sdist: bool = False):
    with open('uppip.txt', 'r', encoding='utf-8') as uppip, open('tratuppip.txt', 'w', encoding='utf-8') as neo:
        leitor = uppip.readlines()

        if not sdist:
            for pkg in range(2, len(leitor)):
                if 'sdist' not in leitor[pkg]:
                    i = leitor[pkg].split(' ')[0]
                    neo.writelines(f'{i} \n')
        else:
            for pkg in range(2, len(leitor)):
                i = leitor[pkg].split(' ')[0]
                neo.writelines(f'{i} \n')

def apaga():
    os.remove('uppip.txt')
    os.remove('tratuppip.txt')
    shutil.rmtree('__pycache__/', ignore_errors = True)
