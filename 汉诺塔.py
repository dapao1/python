def hanoi(n,x,y,z):#数量,原位置,缓冲区,目标位置
    if n==1:
        print(x,'--->',z)#将1从x移动到终点z
    else:
        hanoi(n-1, x, z, y)#将前n-1个盘子从x移动到y上
        print(x,'-->',z)#将最底下的最后一个盘子从x移动到z上
        hanoi(n-1,y,x,z)#将y上的n-1歌盘子移动到z上

n=int(input('请输入汉诺塔的层数:'))
hanoi(n,'X','Y','Z')
