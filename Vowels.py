#########################################################
#                   vowel counter                       #
#                   Ceylan BAĞCI                        #
#                       python 3.7                      #
#########################################################
def count_vowels(text):
    vowels = "aeiou"
    count = 0
    count_a = 0
    count_e = 0
    count_o = 0
    count_u = 0
    count_i = 0

    for i in text:
        if i in vowels:
            if i == 'a':
                count_a +=1
            elif i == 'e':
                count_e +=1
            elif i == 'i':
                count_i +=1
            elif i == 'o':
                count_o +=1
            elif i == 'u':
                count_u +=1
            count += 1
    return " 'a' :{},  'e' :{}, 'i' :{}, 'o' :{}, 'u' :{},total vowels: {}".format(count_a,count_e,count_i,count_o,count_u,count)




if __name__ == '__main__':
    text = input("Copy paste a text!").lower()
    count = int
    print(count_vowels(text))


