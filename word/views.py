from django.shortcuts import render

def home(request):
    if request.method == 'POST':
        # getting the number from user
        # here the number is string
        num1 = request.POST['number']
        # if the number is null then rediect to home page
        if(num1 == ""):
            return render(request,'home.html')
        # converting the string to number
        n = int (num1)
        # declearing the arrays and num to store the word
        num=""
        number = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
        nty = ["","","Twenty","Thirty","Fourty","Fifty","Sixty","Seventy","Eighty","Ninty"]
        ten = ["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        
        # if the number less than or equal to zero then rediect to home page 
        if( n >= 0 ):
            return render(request,'home.html')
        # if the number is greater than 10 lakh than rediect to home page
        elif(n > 1000000 ):
            return render(request,'home.html')
        # the above condition false then go to the number conversion 
        else:
            # decleare a default array to store the numbers position
            d=[0,0,0,0,0,0]
            i=0
            # setting number positions 
            while n>0:
                d[ i ]= n % 10
                i=i+1
                n=n // 10
            print( d )
            #   
            f=""
            # checking the 5th position is zero or not,if not zero then store the number to num and also and lakh
            if( d[ 5 ] != 0):
                num = num + number[d[ 5 ]] + " Lakhs "
            # checking the 4th position is zero or not
            if( d[4]!=0 ):
                # if not zero then store the number to num and also add thousand
                if(d[4]==1):
                    # here the 4th position is not null,then store word in the ten array to num 
                    num = num + ten[d[ 3 ]] + " " + "Thousand " + " "
                # else store the word in the in the nty array to num
                else:
                    num = num + nty[d[ 4 ]] + " " + number[d[ 3 ]] + " Thousand "
                #  also set f=1
                f = 1
            # here f != 1 and 3rd position is not zero then add thousad to the num
            if( f != 1 ):
                if( d[3] != 0 ):
                    num = num + number[d[ 3 ]]+" " + "Thousand " + " "
            # here the 2th position is not null,then store word in the number array to num
            if( d[2] != 0 ):
                num = num + number[d[ 2 ]]+ " " + "Hundred " 
            # checking the 1th position is not zero
            if( d[1] !=0 ):
                # if it is starting with one, then store word in ten array to num
                if( d[1] == 1 ):
                    num = num + ten[d[ 0 ]] + " "
                # else store the word in the nty array to num 
                else:
                    num = num + " " + nty[d[ 1 ]] + " "
            # if 0th position is not zero 
            if( d[0] != 0 ):
                # also the 1th position is not null then number array to num
                if( d[1] != 1 ):
                    num = num + " " + number[d[0]]

            print(num)
    else:
        return render(request,'home.html')
    
    return render(request ,'home.html',{'results' : num})
