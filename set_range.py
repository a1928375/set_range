def biggest(a,b,c):
    if a>b>c or a>c>b:
        return a
    if b>c>a or b>a>c:
        return b
    else:
        return c
        
def smallest(a,b,c):
    if c<a<b or c<b<a:
        return c
    if b<a<c or b<c<a:
        return b
    else:
        return a

def set_range(a,b,c):
    return (biggest(a,b,c)-smallest(a,b,c))
    
print set_range(10, 4, 7)

print set_range(1.1, 7.4, 18.7)
