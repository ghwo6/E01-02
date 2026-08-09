def s_input(inquiry:str)->str:
    while True:
        try:
            select = input(inquiry).strip()
        except KeyboardInterrupt:
            print("\n","(Ctrl + C) 를 입력 받았습니다.","\n")
            exit(-1)
        except EOFError:
            print("\n","(Ctrl + D)를 입력 받았습니다.","\n")
            exit(-1)
        if select == "" or select == None:
            print("아무 입력도 받지 못했습니다.")
        else:
            return select
        print()
        
def int_input(inquiry:str,lower:int,upper:int,hint=None)->int:
    while True:
        try:
            select = input(inquiry).strip()
        except KeyboardInterrupt:
            print("\n","(Ctrl + C) 를 입력 받았습니다.","\n")
            print()
            exit(-1)
        except EOFError:
            print("\n","(Ctrl + D)를 입력 받았습니다.","\n")
            print()
            exit(-1)
        if select == "" or select == None:
            print("아무 입력도 받지 못했습니다.")
        else:
            if select.isdigit():
                select = int(select)
                if lower <= select <= upper:
                    return select
                else:
                    print(f"{lower}  ~ {upper} 사이로 입력해주세요.")
            else:
                print("숫자를 입력해주세요.")
        if hint != None:
            hint()
        
        print()
