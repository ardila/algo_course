__author__ = 'ardila'


a = [int(i) for i in open('int_array.txt', mode='r').read().split('\r\n')[:-1]]

def split(a):
    return a[:len(a)/2], a[len(a)/2:]

def merge_and_count_inversions(a):
    if len(a) == 1:
        return a, 0
    else:
        a1, a2 = split(a)
        b, count1 = merge_and_count_inversions(a1)
        c, count2 = merge_and_count_inversions(a2)
        i = 0
        j = 0
        sorted = []
        split_count = 0
        while (i<len(b)) or (j<len(c)):
            if i>=len(b):
                sorted.append(c[j])
                j+=1
            elif j>=len(c):
                sorted.append(b[i])
                i+=1
            else:
                if c[j]<b[i]:
                    split_count += len(b)-i
                    sorted.append(c[j])
                    j += 1
                else:
                    sorted.append(b[i])
                    i += 1
        return sorted, count1+count2+split_count
