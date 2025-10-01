
def longestSubStringWithoutRepeating(inputStr: str)  -> dict:

    output = {"longestSubStr": "", "longestLentgh": 0   }

    inputStr = inputStr.upper()
    


    if len(inputStr) == 0:
        return output
    
    tempStr = str()
    beginWindow, endWindow = 0,0

    for idx,val in enumerate(inputStr):


        beginWindow = idx 
        midWindow  = idx   
        endWindow = idx 
        print("------")

        print(beginWindow) 

        if len(inputStr) == 1:
             
             output = {"longestSubStr": inputStr, "longestLentgh": len(inputStr)   }

        # elif beginWindow + 1  >= len(inputStr):
            
        #         print("here 1")
        #         break
        #         print("after break")
        
         
        elif   beginWindow + 1 < len(inputStr) and inputStr[beginWindow] != inputStr[beginWindow + 1]   and inputStr[beginWindow ] not in tempStr :
            
            print("here 2")
            print("tempStr = ",tempStr)
            tempStr = tempStr + inputStr[beginWindow]
            output = {"longestSubStr": tempStr, "longestLentgh": len(tempStr)   }

        elif beginWindow + 1 < len(inputStr) and inputStr[beginWindow] == inputStr[beginWindow + 1]  and inputStr[beginWindow ] not in tempStr :
            
            print("here 3")
            tempStr = inputStr[beginWindow]
            output = {"longestSubStr": tempStr, "longestLentgh": len(tempStr)   } 

        elif beginWindow  == len(inputStr) and inputStr[beginWindow-1] != inputStr[beginWindow ] and inputStr[beginWindow ] not in tempStr :

            print("here 4")
            tempStr = tempStr + inputStr[beginWindow]
            output = {"longestSubStr": tempStr, "longestLentgh": len(tempStr)   } 

        else:       
            pass               

 
        
    return output   





# x= ""
# x= "a"
x= "abcde"
# x= "abba"
# x= "abcabcbb"
# x= "pwwkew"
# x= "aab"
# x= "dvdf"
# x= "tmmzuxt"
# x= "anviaj"
# x= "ohvhjdml"
# x= "abcdeafghij"
# x= "abcddcba"
# x= "bbbbb"
# x= "abbaac"
# x= "123451234"
# x= "AaBbCc"
# x= "AaaA"
# x= "a b c a"
# x= "123451234"
# x="!@#!!@#"
# x="\t\n\r"
# x="😀😃😄😁😆😅😂🤣"
# x="😀a😀"
# x="longestsubstringtest"
# x="abcdafghijklabcxyz"
# x="abcdeaBCDEF"
# x="qrstuqxyz"

answer = longestSubStringWithoutRepeating(x)
print(answer)




