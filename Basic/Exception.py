#结构1：try/exept
while True:
    try:
        x = int(input('请输入一个数字：'))
        break
    except ValueError:
        print('你输入的不是数字，请你再次尝试！')

print('\n','-'*60,'\n')


#结构2：try/exept...else
import sys

for arg in sys.argv[1:]:
    try:
        f = open(arg,'r')
        print(f)
    except IOError:
        print('Cannot open',arg)
    else:
        print(arg,'has',len(f.readline()),'lines')
        f.close()