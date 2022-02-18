# print(f"\nfirst module '__name__' is : {__name__}")

def main():
    print(f"\nfirst module '__name__' is : {__name__}")

if __name__ == '__main__':
    main()
    print("\nRun directly from file first_module.py!\n")
else:
    print("\nRun from import in file second_module.py!\n")
