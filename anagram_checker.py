def anagram_checker(string1, string2):

    # Remove spaces and convert to lower case
    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()
    
    # Compare the length of both strings
    if len(string1) == len(string2):
        # Sort each string and compare
        if sorted(string1) == sorted(string2):
            return True

    return False

    
print ("Pass" if not (anagram_checker('water','waiter')) else "Fail")
print ("Pass" if anagram_checker('Dormitory','Dirty room') else "Fail")
print ("Pass" if anagram_checker('Slot machines', 'Cash lost in me') else "Fail")
print ("Pass" if not (anagram_checker('A gentleman','Elegant men')) else "Fail")
print ("Pass" if anagram_checker('Time and tide wait for no man','Notified madman into water') else "Fail")