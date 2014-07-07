# -*- coding: utf8 -*-

def get_inserted_money (my_money_dict) :

    #1: 돈을 투입합니다.
    inserted_money_sum = 0  #최종 투입된 금액

    while(True):
        print '\n내 주머니 상황'
        print '--------------------'
        for key,value in sorted(my_money_dict.items()):
            print "%d원이 %d개 있어요" % (key,value)

        inserted_money = raw_input('\n돈을 넣으세요(입금을 마치려면 엔터) : ')

        #엔터치면 돈 투입 끝으로 간주하고 while loop를 종료한다
        if not inserted_money:
            break

        else :
            #입력 데이터를 숫자형으로 형변환 (왜냐면 $raw_input()은 숫자입력도 문자열로 입력을 받기때문)
            inserted_money = int(inserted_money)

            ### 입력된 화폐를 가지고 있는지 확인
            if my_money_dict.has_key(inserted_money):

                # 입력된 화폐의 수량이 여부 확인
                if my_money_dict[inserted_money] != 0:

                    #투입한 만큼 지갑에서 돈을 뺀다. (해당 돈의 갯수에서 하나 빼기)
                    my_money_dict[inserted_money] -= 1

                    #누적해서 투입된 돈의 합을 표시한다.
                    inserted_money_sum += inserted_money
                    print '지금까지 %d가 투입되었네요' %inserted_money_sum


                    #음료 선택 여부 확인
                    select = input ('음료를 선택하시겠습니까?  예(1), 아니오(0) : ')
                    if select :
                        break

                else :
                    print '단일 화폐 %d원은 없습니다. 다시 입력하세요' %inserted_money

            else :
                print '유효하지 않은 돈'


    #투입된 돈의 총 합이 0이상이 아니면..입금이 안된 것임
    if inserted_money_sum <= 0: 
        print '돈이 입금되지 않았네요. 프로그램 종료 합니다'
        return 0

    print '지금까지 %d가 투입되었네요' % inserted_money_sum
    return inserted_money_sum

def calculate_money (my_money_dict, return_money) :
    thousand_5 = return_money / 5000
    thousand_5_remain = return_money % 5000

    thousand_1 = thousand_5_remain / 1000
    thousand_1_remain = thousand_5_remain % 1000

    hundred_5 = thousand_1_remain / 500
    hundred_5_remain = thousand_1_remain % 500

    hundred_1 = hundred_5_remain / 100
    hundred_1_remain = hundred_5_remain % 100

    if thousand_5 :
        my_money_dict[5000] += thousand_5
    if thousand_1 :
        my_money_dict[1000] += thousand_1
    if hundred_5 :
        my_money_dict[500] += hundred_5
    if hundred_1 :
        my_money_dict[100] += hundred_1

    return my_money_dict


def select_refreshment (products_dict, my_money_dict, inserted_money) :

    buyable = 0
    buyable_products = dict()
    thousand_5 =0
    thousand_1 =0
    hundred_5 =0
    hundred_1 =0

    #구매 가능품목 출력
    for product, spec in products_dict.items() :
        if spec['number'] != 0 :
            buyable = buyable + 1
            print '%2d번 : %7s - 가격: %4d, 수량: %3d' %(buyable, product, spec['price'], spec['number'])
            buyable_products[buyable] = product


    if buyable == 0 :
        print '구매 가능한 품목이 없습니다.'
        print '반환 할지 돈을 더 넣을지 :'
        return -1


    #음료 선택
    while (True) :
        select_num = input ('품목을 입력하세요. 취소하시려면 0번을 눌러주세요')

        if (select_num >= 1 and select_num <= buyable) :
            #print '%d번을 선택했네요' %select_num

            selected_product = buyable_products[select_num]
            products_dict[selected_product]['number'] -= 1

            return_money = inserted_money - products_dict[selected_product]['price']

            my_money_dict = calculate_money (my_money_dict, return_money)
            return selected_product, my_money_dict

        elif select_num == 0:
            #print '나가기를 선택했습니다'
            select_prodect = select_num
            my_money_dict = calculate_money (my_money_dict, return_money)
            return selected_product, my_money_dict

        else :
            print '잘못 입력했습니다. 다시 입력하세요.'


        

# 메인 로직
if __name__ == '__main__':

    products_dict = {
                    'vita500'   : {'price' : 500, 'number' : 2},
                    'milk'      : {'price' : 700, 'number' : 13},
                    'coffee'    : {'price' : 900, 'number' : 8}
                    }

    #               { 돈의종류 : 돈의갯수 }
    my_money_dict = {5000 : 2 , 1000 : 1, 500 : 2 , 100 : 8}

    #돈 투입하기
    inserted_money = get_inserted_money(my_money_dict)

    #음료 선택하기
    result = select_refreshment (products_dict, my_money_dict, inserted_money)
    my_money_dict = result[1]

    if result[0] == 0 :
        print '선택안함'
    else :
        print '%s 선택' %result[0]

    print '지갑상황'
    print result[1]






