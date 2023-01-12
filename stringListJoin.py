def mutate_string(string, position, character):
    #string = "abracadabra"
    #print(string)
    x = list(string)
    #print(x)
    #x[5] = "k"
    x[int(i)] = c
    #print(x)
    s_new = "".join(x)
    return s_new

# string = s , i = index , c = character



if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)