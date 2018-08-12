name="www\"world wide web\""	# \ to escape quote

print('c:\some\name')	#\n means newline
print(r'c:\some\name')	#raw string

print("""
danish wani
buchpora
25""")	#multi line string literals

firstname="danish"
lastname="wani"
print(firstname + lastname)	#concatenation operator

3 * 'danish'	#strings can be repeated using * operator

firstname[0]	#char in position 0
firstname[-1]	#char in last position
firstname[0:2]	#slicing to obtain substring from index 0 to 2 but excluding 2
firstname[0]='t'#strings are immutable

len(firstname)	#length of string
