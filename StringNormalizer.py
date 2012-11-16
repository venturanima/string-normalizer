#Assumption: if we ever try to ".." above root, return null
#Assumption: //.. should output "", ///.. should output "/"
class StringNormalizer():
    def normalize(self, filePath):
        """
        Normalizes file path by keeping list of tokens. Each token can be one of three cases.
        Case 1: Token is ..
           Pop from end of list
        Case 2: Token is .
           Do nothing to list
        Case 3: Token is a normal token
           Add to end of list
        """
        splitString = filePath.split("/")
        tokenList = []
        for token in splitString:
            print "tokenList: " + str(tokenList)
            if token == "..":
                if len(tokenList) == 0:
                    return None
                tokenList.pop()
                print "tokenList is now: " + str(tokenList)
            elif token == ".":
                pass
            else:
                tokenList.append(token)
        
        return '/'.join(tokenList)
        
#Interactive manual tester        
def main():
    while True:
        normalizer = StringNormalizer()
        inputStr = raw_input("\nPlease input a string(q to quit): ")
        if inputStr == 'q':
            print "Now quitting. Thanks for using this program!"
            break;
        else:
            normalized = normalizer.normalize(inputStr)
            if normalized != None:
                print "Your output looks like: " 
                print "\t" + normalized
            else:
                print "Invalid input. Please try again."
            
if __name__ == "__main__":
    main()