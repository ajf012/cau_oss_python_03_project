"""
parking_spot 클래스를 생성한다. 생성자를 통해 __item 필드를 생성한다.
parking_spot 클래스의 get 메소드를 통해 item[keyword]를 반환한다.
str_list_to_class_list 함수를 통해 [str_list]를 매개변수로 받은 후 parking_spot 클래스 객체로 변환한 후 반환한다.
print_spots 함수를 통해 [spots]를 매개변수로 받은 후 리스트에 저장된 모든 객체의 값을 출력한다.
"""
class parking_spot: #클래스를 생성
    __item = {}
    def __init__(self, name, city, district, ptype, longitude, latitude):  #생성자를 통해 __item 필드 생성
        self.__item = {'name':str(name), 'city':str(city), 'district':str(district), 
        'ptype':str(ptype), 'longitude':float(longitude), 'latitude':float(latitude)}

    def __str__(self): 
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})]"
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s
    def get(self,keyword='name'): #get 메소드를 통해 __item[keyword]를 반환한다.
        return self.__item[keyword]

def str_list_to_class_list(str_list):
    all_data_list=[]
    for l in str_list:
        data = l.split(',')
        all_data = parking_spot(data[1], data[2], data[3], data[4], data[5], data[6]) 
        #parking_spot 클래스 객체의 리스트로 변환
        all_data_list.append(all_data)
    return all_data_list 

def print_spots(spots):
    print(f"---print elements({len(spots)})---")
    for l in spots:
        print(l)
    #리스트에 저장된 모든 객체의 값 출력



# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    import file_manager
    str_list = file_manager.read_file("./input/free_parking_spot_seoul.csv")
    spots = str_list_to_class_list(str_list)
    print_spots(spots)

    # version#3
    # spots = filter_by_district(spots, '동작')
    # print_spots(spots)
    
    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)