"""
start_process함수를 통해 [path]를 매개변수로 받은 후 file_manager 모듈의 str_list_to_class_list 함수를 
호출하여 문자열 리스트를 반환받는다.
반환받은 리스트를 이용하여, parking_spot_manger 모듈의 str_list_to_class_list함수로 parking_spot의 리스트를 반환받는다.
1번 옵션 선택시 : parking_spot_manager 모듈의 print_spots 함수 호출한다.
4번 옵션 선택시 : "Exit" 출력 후 while문을 종료시킨다.
"""
import parking_spot_manager
import file_manager

def start_process(path): 
    data_list = file_manager.read_file(path)
    final_list = parking_spot_manager.str_list_to_class_list(data_list)
    while True:
        print("---menu---") 
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        if select == 1:
            parking_spot_manager.print_spots(final_list)
        #final_list 전부 출력
            
        elif select == 2:
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            if select == 1:
                keyword = input('type name:')
                print("not implemented yet")
                # fill this block
            elif select == 2:
                keyword = input('type city:')
                print("not implemented yet")
                # fill this block
            elif select == 3:
                keyword = input('type district:')
                print("not implemented yet")
                # fill this block
            elif select == 4:
                keyword = input('type ptype:')
                print("not implemented yet")
                # fill this block
            elif select == 5:
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))
                print("not implemented yet")
                # fill this block
            else:
                print("invalid input")
        elif select == 3:
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                print("not implemented yet")
                # fill this block
            else: print("invalid input")
        elif select == 4:
            print("Exit")
            break
        #Exit출력 후 반복 종료
        else:
            print("invalid input")