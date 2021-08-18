import copy
# 最长递增子串
str=[5, 3, 4, 8, 6, 7,9]
 
 
def find(str):
    long=1
    status = []
    sub=[]
    for index in range(len(str)): # 从第0个元素开始建立
        status.append(1)
        pre=0
        for preIndex in range(index):  # 从前面（第0个）元素中开始更新
            if(str[preIndex]<=str[index] and status[preIndex]+1>status[index]):
                # 如果当前元素小于元素，且更新后长度更长
                status[index]=status[preIndex]+1
                pre=preIndex
        # 记录每一种状态下的子串
        # print("pre",pre)# 记录的是上一个合适的子串的位置
        if(status[index]>long):
            long=status[index]
 
        if(long==1):
            sub.append([str[index]])
        else:
            new=copy.copy(sub[pre])
            new.append(str[index])
            sub.append(new)
            # print(new)
 
    print(str)
    print(long)
    print(status)
    print(sub)
 
 
if __name__=="__main__":
    find(str)