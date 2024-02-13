def main():
    # Problem: Scan string for Ascii.
    # A dictionary to keep track of visited characters and occurrences
    charVisited = {}
    inputLine = input("Give me your string: ")

    # Loop through the string and add each char to the dict or increment
    for char in inputLine:
        if char in charVisited:
            charVisited[char] += 1
        else:
            charVisited[char] = 1
        # end if/else
    # end for
    # grab the top 3 max values and print them
    for i in range(3):
        maxVal = inputLine[0]
        for key in charVisited:
            if charVisited[key] > charVisited[maxVal]:
                maxVal = key
            # end if
        # end loop
        # To allow printing of space in a nice way
        maxKey = maxVal
        if maxVal == " ":
            maxKey = "Space"
        # end if
            
        print("Character: ", maxKey, " - ", charVisited[maxVal])
        charVisited.pop(maxVal)
    # end loop

    j = 0
    for key in charVisited:
        j += 1

    # How many of the ascii characters were used?
    print("Total Character Unused: ", 256 - j)    
    
# end main

if __name__ == "__main__":
    main()