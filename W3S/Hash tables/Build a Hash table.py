my_hash_set = [None, 'Jones', None, 'Lisa', None, 'Bob', None, 'Siri', 'Pete', None]


def hash_function(value):
    sum_of_chars = 0
    for char in value:
        sum_of_chars += ord(char)
        print(char, ": ",ord(char))
    print("Total is : ", sum_of_chars)

    return sum_of_chars % 10


def contains(name):
    index = hash_function(name)
    return my_hash_set[index] == name


print("'Pete' is in the Hash Set:", contains('Pete'))


def buildHashTable():
    hash_table = [[] for i in range(10)]
    return hash_table

print("\nBelow is my hash table :")
myHashTable = buildHashTable()
print(myHashTable)