
def twoSumProblem(inputLst: list, trgt: int =0)  -> list:
    
    intrmdtList = list()
    seen = {}

    for idx,num in enumerate(inputLst):
        
        
        diff = trgt - num                
        if diff in seen:          
            return [seen[diff], idx]  
        seen[num] = idx

    return []




x = [2, 7, 11, 15, 20, 30]
answer = twoSumProblem(x,26)
print(answer)




