#A segment of a string is called a slice.
# Selecting a slice is similar to selecting a character
S="Vinoth Mayilvaganan"
print("length of S= ",len(S))
print("Index of S= ",len(S)-1)
print(S[0:6])
print(S[7:19])
#The operator [n:m] returns the part of the string from
#the “n-th” character to the “m-th” character,
#including the first but excluding the last.
print(S[0:5])
#If you omit the first index (before the colon),
#the slice starts at the beginning of the string.
#If you omit the second index, the slice goes to the end of the string:
print(S[:])
print(S[:6])
print(S[7:])
