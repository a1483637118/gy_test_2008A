a = [1,2,3,5,6,7,8,9,123,567,2345,23456]

# 使用二分法查找判断某个数是否存在于list中，若存在则返回该数字的下标，不存在返回-1
s = 5
t = -1
lenth = len(a)
start = 0
end = lenth-1
while end > start:
    half = (end+start)//2
    if a[half]>s:
        end = half
    elif a[half]<s:
        start=half+1
    else:
        t = half
        break
print(t)

plist = [1,0,3,7,5,7]

b = list(set(plist))
b.sort(key=plist.index)
print('sds:',b