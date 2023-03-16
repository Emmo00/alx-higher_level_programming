def uniq_add(my_list=[]):
    seen = []
    sum = 0
    for i in my_list:
        if i not in seen:
           sum = sum + i
           seen.append(i)
    return sum 
