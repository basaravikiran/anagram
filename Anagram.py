def are_anagrams(string1,string2):
    """
    This python 3 based method accepts two strings and returns True if they are anagrams.
    The algorithm compares the lists derived from the strings by removing white spaces ,
    converting them to lower case and then sorting the characters
    """
    list1= sorted(string1.replace(' ','').lower())
    list2 = sorted(string2.replace(' ', '').lower())
    return list1 == list2

if __name__ == '__main__' :
    print(are_anagrams('RAdium came',"Madam Curie" ))