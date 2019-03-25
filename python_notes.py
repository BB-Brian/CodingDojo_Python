# some common string methods:
string.upper(): returns a copy of the string with all the characters in uppercase.

string.lower(): returns a copy of the string with all the characters in lowercase.

string.count(substring): returns number of occurrences of substring in string.

string.split(char): returns a list of values where string is split at the given character. Without a parameter the default split is at every space.

string.find(substring): returns the index of the start of the first occurrence of substring within string.

string.isalnum(): returns boolean depending on whether the string's length is > 0 and all characters are alphanumeric (letters and numbers only). Strings that include spaces and punctuation will return False for this method. Similar methods include .isalpha(), .isdigit(), .islower(), .isupper(), and so on. All return booleans.

string.join(list): returns a string that is all strings within our set (in this case a list) concatenated.

string.endswith(substring): returns a boolean based upon whether the last characters of string match substring.

#*******************************************
#some common sequence methods (lists/tuples)
max(sequence) returns the largest value in the sequence

sum(sequence) return the sum of all values in sequence

map(function, sequence) applies the function to every item in the sequence you pass in. Returns a list of the results.

min(sequence) returns the lowest value in a sequence.

sorted(sequence) returns a sorted sequence

#*******************************************
#some common sequence methods (lists/tuples)
capitals = {"svk":"Bratislava","deu":"Berlin", "dnk":"Copenhagen"}
# creating a new key/value pair
capitals["abc"] = "New Country"
# updating
capitals["abc"] = "ABC Country"
#to print all keys
for data in capitals:
     print(data)
#another way to print all keys
for key in capitals.keys():
     print(key)
#to print the values
for val in capitals.values():
     print(val)
#to print all keys and values
for key, val in capitals.items():
     print(key, " = ", val)
