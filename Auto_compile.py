import os
import argparse
import numpy as np
import shutil

# Parse command line arguments
parser = argparse.ArgumentParser(
    description='auto compile')
parser.add_argument('--python_path', required=False,
                    metavar="dont need to comment when run code",
                    help='Directory of the main.py')
parser.add_argument('--file', required=False,
                    metavar="/home/simon/main.py",
                    help='/home/simon/main.py')
args = parser.parse_args()
if args.file != None:
    file_name = os.path.basename(os.path.realpath(args.file))
    args.python_path=args.file.split(file_name)[0]
    # for file in os.listdir(args.python_path):
    #     if ".py" in file:
    #         break
    # os.system('cd ' + args.python_path)
    # os.system()

    os.chdir(args.python_path)
    os.system("pyarmor obfuscate --recursive " +args.file)
    os.system("python -m compileall " + args.python_path)
    # if not os.path.exists(os.path.join(args.python_path, 'dist')):
    #     shutil.move(os.path.join(os.getcwd(), 'dist'), os.path.join(args.python_path,'dist'))
    dist = os.path.join(args.python_path, 'dist')
    pycache_1 = os.path.join(dist, '__pycache__')
    for file in os.listdir(args.python_path):
        if file != 'dist':
            try:
                os.remove(os.path.join(args.python_path, file))
            except:
                shutil.rmtree(os.path.join(args.python_path, file))
    for file in os.listdir(dist):
        if os.path.splitext(file)[1] == '.py':
            try:
                os.remove(os.path.join(dist, file))
            except:
                shutil.rmtree(os.path.join(args.python_path, file))
    for file in os.listdir(pycache_1):
        shutil.copy(os.path.join(pycache_1, file), os.path.join(dist, file.split('.')[0] + '.' + file.split('.')[-1]))
    shutil.rmtree(pycache_1)
    for file in os.listdir(dist):
        if os.path.splitext(file)[1] == '':
            folder = os.path.join(dist, file)
            for item in os.listdir(folder):
                if os.path.splitext(item)[1] == '.py':
                    try:
                        os.remove(os.path.join(folder, item))
                    except:
                        shutil.rmtree(os.path.join(folder, item))
                else:
                    pycache_2 = os.path.join(folder, item)
                    for items in os.listdir(pycache_2):
                        shutil.copy(os.path.join(pycache_2, items),
                                    os.path.join(folder, items.split('.')[0] + '.' + items.split('.')[-1]))
            shutil.rmtree(pycache_2)
    for file in os.listdir(dist):
        shutil.move(os.path.join(dist, file), os.path.join(args.python_path, file))
    shutil.rmtree(dist)