def NULL_not_found(object: any) -> int:
    try:
        #print(type(object).__name__)
       #print(object == None)
        if(type(object).__name__ == "NoneType" and object == None):
            print("Nothing: None"+ " " + str(type(object)))
        elif(type(object).__name__ == "float" and object != object):
            print("Cheese: nan"+ " " + str(type(object)))
        elif(type(object).__name__ == "int"and object == 0) :
            print("Zero: 0"+ " " + str(type(object)))
        elif(type(object).__name__ == "str" and object == ""):
            print("Empty: ''"+ " " + str(type(object)))
        elif(type(object).__name__ == "bool"and object == False):
            print("Fake: False"+ " " + str(type(object)))
        else :
            raise Exception("Type not found")
        return 0
    
    except Exception as e:
        print(e)
        return 1
    
    return 42