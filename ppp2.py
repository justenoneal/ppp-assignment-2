def max_num(num_list):       #L is a list of 3 numbers
    return(max(num_list))

def mult_list(num_list):     #L is a list of numbers
    product = 1
    for n in num_list:
        product *= n
    return(product)

def rev_string(str):
        return(str[::-1])

def num_within(a, b, c):
     if a in range(b, c+1):
          return True
     else:
          return False

def pascal(n):
    i = 1
    for i in range(n+1):
        j = 1
        k = i + 0
        row = [1]
        for x in range(j, i+1):
            row.append(int((k*row[j-1]/j)))
            j += 1
            k -= 1
        print(row)



print(max_num([3, 2345, 123]))
print(mult_list([3, 2, 5, 8]))
print(rev_string("pizza cake"))
print(num_within(8, 2, 25))
pascal(11)