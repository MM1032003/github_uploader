import os, sys, time as t

print(sys.argv)

if len(sys.argv) == 3:
    dir_path        = sys.argv[1]
    repository_link = sys.argv[2]
else:
    print("Please Enter The Directory Path And Repository Link")
    exit()

if not os.path.isabs(dir_path):
    dir_path    = os.path.abspath(dir_path)

try:
    os.chdir(dir_path)
except Exception as ex:
    print('Error ' + str(ex))
    exit()
    

os.system('git init')
t.sleep(.5)
os.system('git add .')
t.sleep(.5)
os.system('git commit -m "adding files"')
t.sleep(.5)
os.system(f'git remote add origin {repository_link}')
t.sleep(.5)
os.system('git pull origin master')
t.sleep(.5)
os.system('git push -f origin master')