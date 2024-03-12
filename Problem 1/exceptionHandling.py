"""
Name: Owen Anderson
Lab Time: THUR 2:00 - 3:15
"""
def exceptionHandling():
    # Split input into 2 parts: name and age
    parts = input().split()
    name = parts[0]
    while name != '-1':
        # FIXME: The following line will throw ValueError exception.
        #        Insert try/except blocks to catch the exception.
        try:
            age = int(parts[1]) + 1
            print(f'{name} {age}')
        except:
            print(f'{name} {0}')
        
        # Get next line
        parts = input().split()
        name = parts[0]

if __name__ == '__main__':
    exceptionHandling()