def main():
	print("first module's name is: "+__name__)

if __name__ == '__main__':
	main()
else:
	print("Called from import")