def buildArray(target,n):
    i=0 
    number=1
    ans=[] 
    while n>0 and i<len(target):
        if number==target[i]:
            i+=1
            ans.append('Push')
        else:
            ans.append('Push')
            ans.append('Pop')
            number+=1 
            n-=1 
    return ans
