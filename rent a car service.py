toyota_cars={'car1':'toyota corolla 2015 XLI','car2':'toyota corolla 2015 GLI','car3':'toyota corolla 2016 XLI','car4':'toyota corolla 2016 GLI',
             'car4':'toyota corolla 2017 XLI','car5':'toyota corolla 2017 GLI','car6':'toyota corolla 2017 GRANDE','car7':'toyota corolla 2018 XLI',
             'car8':'toyota corolla 2018 GLI','car9':'toyota corolla 2018 GRANDE','car10':'toyota land cruiser V8','car11':'toyota VIGO','car12':'toyota revo',
             'car13':'toyota HIACE'}

toyota_1=['toyota corolla 2015 XLI','toyota corolla 2015 GLI','toyota corolla 2016 XLI','toyota corolla 2016 GLI',
             'toyota corolla 2017 XLI','toyota corolla 2017 GLI','toyota corolla 2017 GRANDE','toyota corolla 2018 XLI',
             'toyota corolla 2018 GLI','toyota corolla 2018 GRANDE','toyota land cruiser V8','toyota VIGO','toyota revo',
             'toyota HIACE']

honda_cars={'car14':'honda city 2015','car15':'honda CIVIC 2015','car16':'honda city 2016','car17':'honda CIVIC 2016','car18':'honda CIVIC 2018',
            'car19':'honda city 2018','car20':'honda accord 2017','car21':'honda accord 2018','car22':'visel','car23':'honda BR-V'}

honda_1=['honda city 2015','honda CIVIC 2015','honda city 2016','honda CIVIC 2016','honda CIVIC 2018',
            'honda city 2018','honda accord 2017','honda accord 2018','visel','honda BR-V']

suzuki_cars={'car24':'suzuki mehran 2017','car25':'suzuki mehran 2018','car26':'suzuki ciaz 2017','car27':'suzuki japanese ALTO 2018',
             'car28':'suzuki VITARA'}

suzuki_1=['suzuki mehran 2017','suzuki mehran 2018','suzuki ciaz 2017','suzuki japanese ALTO 2018',
        'suzuki VITARA']

highlevel_cars={'car29':'mercedes BENZ C class 2018','car30':'merecedes BENZ E class 2018','car31':'AUDI A7','car32':'AUDI A4','car33':'AUDI A2'}

highlevel_1=['mercedes BENZ C class 2018','merecedes BENZ E class 2018','AUDI A7','AUDI A4','AUDI A2']

CC_toyota_cars={'toyota corolla 2015 XLI':'1300cc','toyota corolla 2015 GLI':'1300cc','toyota corolla 2016 XLI':'1300cc','toyota corolla 2016 GLI':'1300cc',
             'toyota corolla 2017 XLI':'1300cc','toyota corolla 2017 GLI':'1300cc','toyota corolla 2017 GRANDE':'1800cc','toyota corolla 2018 XLI':'1300cc',
             'toyota corolla 2018 GLI':'1300cc','toyota corolla 2018 GRANDE':'1800cc','toyota land cruiser V8':'4461cc','toyota VIGO':'2494cc','toyota revo':'2494cc',
            'toyota HIACE':'4000cc'}

cc_honda_cars={'honda city 2015':'1500cc','honda CIVIC 2015':'1800cc','honda city 2016':'1497cc','honda CIVIC 2016':'1500cc','honda CIVIC 2018':'1800cc',
            'honda city 2018':'1500cc','honda accord 2017':'2.4L','honda accord 2018':'2.8L','visel':'2200cc','honda BR-V':'1500cc'}

suzuki_cars={'suzuki mehran 2017':'850cc','suzuki mehran 2018':'850cc','suzuki ciaz 2017':'1800cc','suzuki japanese ALTO 2018':'650cc',
             'suzuki VITARA':'1800cc'}


print("\t\t welcome to the 'RENT A RIDE'\t\t")
user1=input('enter your name please: ')
print('We Welcome You Our Valued Customer', user1, '!!')
print('--------')
print('following are the terms and conditions:\n1-you will be responsible for the all type of damages to the car if driver wasnt with you.\n2-you have to manage the fuel tank of the car.\n3-you photocopy of the NIC will be kept will you hier the car.\n4-we only rent car on daily basis.')
user2=input('Are you agree with the terms and conditions? (yes or no): ')
if user2=='yes':
    print('we deal with the below mentioned companies: \n1-toyota\n2-honda\n3-suzuki\n4-audi\n5-mercedes')
    user_a=int(input('number the company you trust in: '))
    '''enter 1,2,3,4 and 5'''
    if user_a==1:
        print('Here are the following cars avalible in toyota')
        print('1-toyota corolla 2015 XLI \t2-toyota corolla 2015 GLI \n3-toyota corolla 2016 XLI\t4-toyota corolla 2016 GLI\n5-toyota corolla 2017 XLI\t6-toyota corolla 2017 GLI\n7-toyota corolla 2017 GRANDE\t8-toyota corolla 2018 XLI\n9-toyota corolla 2018 GLI\t10-toyota corolla 2018 GRANDE\n11-toyota land cruiser V8\t12-toyota VIGO\n13-toyota revo\t14-toyota HIACE')
        user3=int(input('which car do you want to ride: '))
        if user3==1 or 2 or 3 or 4 or 5 or 6 or 8 or 9:
            print('this is ',CC_toyota_cars.get('toyota corolla 2017 GLI'),'cars')
            print('this car will give you 14km in one liter on petrol')
            price=12000
            print('they will be charged' + str(price) + 'per day')
            user4=int(input('for how many days do you want car on rent: '))
            print('your total cost will be:', user4*price, 'rupees for', user4, 'days')
            print('this is only petrol car and driver is your choice')
            agree1=input('are you sure you want to get this car for rent: ')
            if agree1=='yes':
                print('thankyou!, you must vist our showroom when ever you want after 10:00AM every morning')
            else:
                print('no tensions...! see you again!')
        elif user3==7 or 10:
            print('this is 1800cc car')
            print('terms and conditions will be applied')
            price2=15000
            print('this will be cost 15000 per day and driver is upto you')
            print('this car will give you 14km in one liter of petrol')
            user5=int(input('enter for how many days do you want car on rent: '))
            print('your total cost will be: ', user5*price, 'rupees for', user5, 'days')
            agree2=input('are you sure you want to get this car for rent: ')
            if agree2=='yes':
                print('thankyou!, you must vist our showroom when ever you want after 10:00AM every morning')
            else:
                print('no tensions...! see you again!')
        elif user3==11 or 12 or 13 or 14:
            print('this is 2000+cc car')
            print('this car will give you 8km in one liter')
            price3=22000
            print('they will be cost 22000 per day and driver will be provided to you')
            user6=int(print('for how many days do you want this car: '))
            print('your total price will be: ',user6*price3, 'rupees for', user6, 'days')
            agree3=input('are you sure you want to get this car for rent: ')
            if agree3=='yes':
                print('thankyou!, you must vist our showroom when ever you want after 10:00AM every morning')
            else:
                print('no tensions...! see you again!')
        else:
            print('sorry enter the valid number of the car list is given above... !\n thankyou')
    elif user_a==2:
        print('here are the following cars avalible in HONDA')
        print('1-honda city 2015\t2-honda CIVIC 2015\n3-honda city 2016\t4-honda CIVIC 2016\n5-honda CIVIC 2018\t6-honda city 2018\n7-honda accord 2017\t8-honda accord 2018\n9-visel\t10-honda BR-V')
        user7=int(input('which car do you want to hire: '))
        if user7==1 or 3 or 4 or 6 or 10:
            print('this is 1500cc car')
            print('this car will give 18km in one liter')
            print('they will be cost 18000 rupees per day')
            price4=18000
            user8=int(input('for how many day do you want car: '))
            print('the total price will be', price4*user8, 'rupees for', user8, 'days')
            agree4=input('are you sure you want to get this car for rent: ')
            if agree4=='yes':
                print('thankyou!, you must vist our showroom when ever you want after 10:00AM every morning')
            else:
                print('no tensions...! see you again!')
        elif user7==2 or 5 or 9:
            print('this is 1800cc car')
            print('this car will give 6km in one liter')
            print('this will be cost 20000 rupees per day')
            price5=20000
            user9=int(input('for how many day do you want car: '))
            print('the total price will be', price5*user9, 'rupees for', user9 , 'days')
            agree5=input('are you sure you want to get this car for rent: ')
            if agree5=='yes':
                print('thankyou!, you must vist our showroom when ever you want after 10:00AM every morning')
            else:
                print('no tensions...! see you again!')
        elif user7==7 or 8:
            print('this is 2.4L car')
            print('this car will give 8km in one liter')
            print('this will be cost 26000 rupees per day')
            price6=26000
            user10=int(input('for how many day do you want car: '))
            print('the total price will be', price6*user10, 'rupees for', user10 , 'days')
            agree6=input('are you sure you want to get this car for rent: ')
            if agree6=='yes':
                print('thankyou!, you must vist our showroom when ever you want after 10:00AM every morning')
            else:
                print('no tensions...! see you again!')
        else:
            print('enter the valid number of car please...!! THANKYOU ')
    elif user_a==3:
        print('here are the following cars avalible in suzuki')
        print('1-suzuki mehran 2017\t2-suzuki mehran 2018\n3-suzuki ciaz 2017\t4-suzuki japanese ALTO 2018\n5-suzuki VITARA')
        user11=int(input('enter which car do you want to hire: '))
        if user11==1 or 2:
            print('this is 850cc car')
            print('this car will give 24km in one liter')
            print('this will be cost 8000 rupees per day')
            price7=8000
            user12=int(input('for how many day do you want car: '))
            print('the total price will be', price7*user12, 'rupees for', user12, 'days')
            agree7=input('are you sure you want to get this car for rent: ')
            if agree7=='yes':
                print('thankyou!, you must vist our showroom when ever you want after 10:00AM every morning')
            else:
                print('no tensions...! see you again!')
        elif user11==3 or 5:
            print('this is 1800cc car')
            print('this car will give 5km in one liter')
            print('this will be cost 18000 rupees per day')
            price8=18000
            user13=int(input('for how many day do you want car: '))
            print('the total price will be', price8*user13, 'rupees for', user13 ,'days')
            agree8=input('are you sure you want to get this car for rent: ')
            if agree8=='yes':
                print('thankyou!, you must vist our showroom when ever you want after 10:00AM every morning')
            else:
                print('no tensions...! see you again!')
        elif user11==4:
            print('this is 650cc car')
            print('this car will give 23km in one liter')
            print('this will be cost 6000 rupees per day')
            price9=6000
            user14=int(input('for how many day do you want car: '))
            print('the total price will be', price9*user14, 'rupees for', user14, 'days')
            agree9=input('are you sure you want to get this car for rent: ')
            if agree9=='yes':
                print('thankyou!, you must vist our showroom when ever you want after 10:00AM every morning')
            else:
                print('no tensions...! see you again!')
        else:
            print('enter the valid number of car...! thankyou')
    elif user_a==4:
        print('here are the following cars avalible in AUDI')
        print('1-AUDI A7\t2-AUDI A4\n3-AUDI A2')
        user15=int(input('which car do you want to hire: '))
        if user15==1 or 2 or 3:
            print('this is a luxirious car')
            print('this car will give 12km in one liter')
            print('this will be cost 30000 rupees per day')
            price10=30000
            user16=int(input('for how many day do you want car: '))
            print('the total price will be', price10*user16, 'rupees for', user16 , 'days')
            agree10=input('are you sure you want to get this car for rent: ')
            if agree10=='yes':
                print('thankyou!, you must vist our showroom when ever you want after 10:00AM every morning')
            else:
                print('no tensions...! see you again!')
        else:
            print('please enter the valid number of car....!! THANKYOU')
    elif user_a==5:
        print('here are the following cars avalible in mercedes')
        print('1-mercedes BENZ C class 2018\t2-merecedes BENZ E class 2018')
        user17=int(input('which car do want to hire: '))
        if user17==1 or 2:
            print('this is a luxirious car')
            print('this car will give 8km in one liter')
            print('this will be cost 30000 rupees per day')
            price11=30000
            user18=int(input('for how many day do you want car: '))
            print('the total price will be', price11*user18, 'rupees for' ,user18, 'days')
            agree11=input('are you sure you want to get this car for rent: ')
            if agree11=='yes':
                print('thankyou!, you must vist our showroom when ever you want after 10:00AM every morning')
            else:
                print('no tensions...! see you again!')
        else:
            print('please enter a valid number of car...! thankyou!')
    else:
        print('please enter the valid number of car list')
else:
    print('sorry', user1,'you have to agree with the terms and conditions')
    
        
            
            
            
        
        
        
            
            
