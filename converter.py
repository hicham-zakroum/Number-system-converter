#########################################################
#### coder  = " hicham zakroum \n"                  #####
#### script = " number converter \n"                #####
#### date   = " 07/01/2021 \n"                      #####
#########################################################
import pyfiglet

# the decorationn of the interface 
system = pyfiglet.figlet_format("converter number")


############# convert hexadicimal to base b

## convert hexadecimal to binary
def hexToBin(hexa):
    result99 = ""
    for i in hexa:
        if (i == "a") | (i == "A"):
            i = 10
            result = ""
            while i != 0:
                result += (str(i % 2))
                i = int(i/2)
            if len(result)%4 != 0:
                result += (str(0))
                if len(result) % 4 != 0:
                    result += (str(0))
                    if len(result)%4 != 0:
                        result += (str(0))
            else:
                result=result
            result_1 = result[::-1]
            result99 += result_1
        elif (i == "b") | (i == "B"):
            result = ""
            i = 11
            while i != 0 :
                result += (str(i%2))
                i = int(i/2)
            if len(result)%4 != 0 :
                result += (str(0))
                if len(result)%4 != 0:
                    result += (str(0))
                    if len(result)%4 != 0:
                        result += str(0)
            else:
                result=result
            result_1 = result[::-1]
            result99 += result_1
        elif (i == "c") | (i == "C"):
            result = ""
            i = 12
            while i != 0 :
                result += (str(i%2))
                i = int(i/2)
            if len(result)%4 != 0 :
                result += (str(0))
                if len(result)%4 != 0:
                    result += (str(0))
                    if len(result)%4 != 0:
                        result += str(0)
            else:
                result=result
            result_1 = result[::-1]
            result99 += result_1
        elif (i == "d") | (i == "D"):
            result = ""
            i = 13
            while i != 0 :
                result += (str(i%2))
                i = int(i/2)
            if len(result)%4 != 0 :
                result += (str(0))
                if len(result)%4 != 0:
                    result += (str(0))
                    if len(result)%4 != 0:
                        result += str(0)
            else:
                result=result
            result_1 = result[::-1]
            result99 += result_1
        elif (i == "e") | (i == "E"):
            result = ""
            i = 14
            while i != 0 :
                result += (str(i%2))
                i = int(i/2)
            if len(result)%4 != 0 :
                result += (str(0))
                if len(result)%4 != 0:
                    result += (str(0))
                    if len(result)%4 != 0:
                        result += str(0)
            else:
                result=result
            result_1 = result[::-1]
            result99 += result_1
        elif (i == "f") | (i == "F"):
            result = ""
            i = 15
            while i != 0 :
                result += (str(i%2))
                i = int(i/2)
            if len(result)%4 != 0 :
                result += (str(0))
                if len(result)%4 != 0:
                    result += (str(0))
                    if len(result)%4 != 0:
                        result += str(0)
            else:
                result=result
            result_1 = result[::-1]
            result99 += result_1

        elif hexa.isalpha():
            print("\nplease enter valid hexadecimal number!! ")
            break


        elif int(i) in range(0,9):
            result = ""
            i = int(i)
            while i != 0 :
                result += (str(i%2))
                i = int(i/2)
            if len(result)%4 != 0 :
                result += (str(0))
                if len(result)%4 != 0:
                    result += (str(0))
                    if len(result)%4 != 0:
                        result += str(0)
            else:
                result=result
            result_1 = result[::-1]
            result99 += result_1
    if result99 == "":
        print("")
    else:
        print("your binary number is : ",result99)

## covert hexadecimal to octal
def hexToOct(hexa):


    result = 0
    i = 0
    hexa1 = hexa[::-1]
    for j in hexa1:
        if (j == "a") | (j == "A"):
            j = 10
            result += j*(16**i)
            i += 1
        elif (j == "b") | (j == "B"):
            j = 11
            result += j*(16**i)
            i += 1
        elif (j == "c") | (j == "C"):
            j = 12
            result += j*(16**i)
            i += 1
        elif (j == "d") | (j == "D"):
            j = 13
            result += j*(16**i)
            i += 1
        elif (j == "e") | (j == "E"):
            j = 14
            result += j*(16**i)
            i += 1
        elif (j == "f") | (j == "F"):
            j = 15
            result += j*(16**i)
            i += 1
        elif hexa1.isalpha():
            print("\nplease enter valid hexadecimal number!! ")
            break
        elif hexa1.isspace():
            break
        elif int(j) in range(0,9):
            j = int(j)
            result += j*(16**i)
            i += 1


    result_total = ""
    while result != 0 :
        result_total += str(result%8)
        result = int(result/8)
    result_1 = result_total[::-1]

    if result_1 == "":
        print("")
    else:
        print("your octal  number is : ",result_1)

##########)) convert octal to base b

## convert octal to binary
def octToBin(octal):
    result99 = ""
    for i in octal:
        if octal.isalpha():
            print("\nplease enter valid octal number!! ")
            break

        elif int(i) > 7:
            print("\nplease enter valid octal number!! ")
            octToBin(input("enter your octal number : "))
            octal = ""
            break
        elif int(i) <= 7:
            result = ""
            i = int(i)
            while i != 0 :
                result += (str(i%2))
                i = int(i/2)
            if len(result)%3 != 0 :
                result += (str(0))
                if len(result)%3 != 0:
                    result += (str(0))
            else:
                result=result
            result_1 = result[::-1]
            result99 += result_1
        else:
            print('\nplease enter a valid octal number!! ')
            octToBin(input("enter your octal number : "))

    if result99 == "" :
        print("")
    else:
        print("your binary number is : ",result99)


## convert octal to hexadecimal
def octToHex(octal):

    result = 0
    i = 0
    octal_1 = octal[::-1]
    for a in octal_1:
        if octal_1.isalpha():
            print("\nplease enter valid octal number !!")
            break
        elif int(a) > 7:
            print("\nplease enter valid octal number!! ")
            octToHex(input("enter your octal number : "))
            break
        elif int(a) <= 7:
            a = int(a)
            result += a*(8**i)
            i += 1

        else:
            print("\nplease enter a valid octal number!! ")
            octToHex(input("enter your octal number : "))
    result99 = ""
    while result != 0 :
        remainder = str(result%16)
        if remainder == str(10):
            result99 += "A"
            result = int(result/16)
        elif remainder == "11":
            result99 += "B"
            result = int(result/16)
        elif remainder == "12":
            result99 += "C"
            result = int(result/16)
        elif remainder == "13":
            result99 += "D"
            result = int(result/16)
        elif remainder == "14":
            result99 += "E"
            result = int(result/16)
        elif remainder == "15":
            result99 += "F"
            result = int(result/16)
        else:
            remainder = remainder
            result99 += remainder
            result = int(result/16)

    result_1 = result99[::-1]

    if result_1 == "":
        print("")
    else:
        print("your hexadecimal number is : ",result_1)

############################### convert binary to base b 

## convert binary to octal
def binToOct(binary):
    bin1 = []
    binary99 = binary
    if len(binary99)%3 != 0:
        bin1.append(str(0))
        binary99 += "0"
        if len(binary99)%3 != 0:
            bin1.append(str(0))
    else:
        binary99=binary99

    for i in binary:
        if binary.isalpha():
            print("\nplease enter valid binary number !!")
            break
        elif int(i) in range(0,2):
            bin1.append(str(i))
        else:
            print("\nplease enter valid binary number!!")
            binToOct(input("enter your binary number : "))

    i =0 # 0 3 6
    j =3  # 3 6 9
    result99 =""
    while (i <= len(bin1)) & (j <= len(bin1)+1 ):
        bin2 = bin1[i:j]
        bin3 = bin2[::-1]
  
        # fonction (convert binary to decimal)
        result = 0
        k = 0
        for a in bin3:
            a = int(a)
            result += a*(2**k)
            k += 1
        result99 += str(result)
        i += 3
        j += 3

    if result99 == "0":
        print("")
    else:
        print("your octal number is : ",result99)

## convert binary to hexadecimal
def binToHex(binary):

    bin1 =[]
    binary99 = binary
    if len(binary99)%4 != 0 :
        bin1.append(str(0))
        binary99 += str(0)
        if len(binary99)%4 != 0:
            bin1.append(str(0))
            binary99 += str(0)
            if len(binary99)%4 != 0:
                bin1.append(str(0))
    else:
        binary99=binary99

    for i in binary:
        if binary.isalpha():
            print("\nplease enter a valid binary number!! ")
            break
        if int(i) in range(0,2):
            bin1.append(str(i))
        else:
            print("\nplease enter a valid binary number!!")
            binToHex(input("enter your binary number : "))

    i =0 # 0 4 8
    j =4  # 4 8 12
    result99 =""
    while (i <= (len(bin1))-3) & (j <= (len(bin1)+1) ):
        bin2 = bin1[i:j]
        bin3 = bin2[::-1]

        # fonction (convert binary to decimal)
        result = 0
        k = 0
        for a in bin3:
            a = int(a)
            result += a*(2**k)
            k += 1

        if result == 10:
            result99 += "A"
        elif result == 11:
            result99 += "B"
        elif result == 12:
            result99 += "C"
        elif result == 13:
            result99 += "D"
        elif result == 14:
            result99 += "E"
        elif result == 15:
            result99 += "F"
        else:
            result99 += str(result)

        i += 4
        j += 4

    if result99 == "0":
        print("")
    else:
        print("your hexadecimal is : ",result99)


########## to convert decimal to (base b) we divise by b :

## convert decimal to binary 
def decToBin(dec):

    if dec.isalpha():
        print("\nplease enter a valid decimal number!! ")

    else:
        result = ""
        while int(dec) != 0 :
            dec = int(dec)
            result += str(dec%2)
            dec = int(dec/2)
        result_1 = result[::-1]

        print("your binary number is : ",result_1)

## convert decimal to octal
def decToOct(dec):

    if dec.isalpha():
        print("\nplease enter valid decimal number!! ")

    else:
        result = ""
        while int(dec) != 0 :
            dec = int(dec)
            result += str(dec%8)
            dec = int(dec/8)
        result_1 = result[::-1]

        print("your octal  number is : ",result_1)

## convert decimal to hexadecimal 
def decToHex(dec):

    if dec.isalpha():
        print("\nplease enter valid decimal number")

    else:
        result99 = ""
        while dec != 0 :
            dec = int(dec)
            result = str(dec%16)
            if result == str(10):
                result99 += "A"
                dec = int(dec/16)
            elif result == "11":
                result99 += "B"
                dec = int(dec/16)
            elif result == "12":
                result99 += "C"
                dec = int(dec/16)
            elif result == "13":
                result99 += "D"
                dec = int(dec/16)
            elif result == "14":
                result99 += "E"
                dec = int(dec/16)
            elif result == "15":
                result99 += "F"
                dec = int(dec/16)
            else:
                result=result
                result99 += result
                dec = int(dec/16)

        result_1 = result99[::-1]

        print("your hexadecimal number is : ",result_1)


########## to convert (base b) to decimal we use this equation : sum(a*(b**i))

## convert binary to decimal 
def binToDec(binary):

    result = 0
    i = 0
    binary_1 = binary[::-1]
    for a in binary_1:
        if binary.isalpha():
            print("\nplease enter valid binary number!! \n")
            break
        elif (int(a) == 0) | (int(a) == 1):
            a = int(a)
            result += a*(2**i)
            i += 1
        else:
            print("\nplease enter valid binary number ")
            binToDec(input("enter your binary number : "))

    if result == 0:
        print("")
    else:
        print("your decimal number is :" ,result)

## convert octal to decimal 
def octToDec(octal):

    result = 0
    i = 0
    octal_1 = octal[::-1]
    for a in octal_1:
        if octal.isalpha():
            print("\nplease enter valid octal number !!")
            break
        if int(a) > 7:
            print("\nplease enter valid octal number!! ")
            octToDec(input("enter your octal number : "))
            octal_1 = "9"
            break
        elif int(a) <= 7:
            a = int(a)
            result += a*(8**i)
            i += 1

        else:
            print("\nplease enter a valid octal number!! \n")
            octToDec(input("enter your octal number : "))

    if result == 0:
        print("")
    else:
        print("your decimal number is : " , result)

## convert hexadecimal to decimal 
def hexToDec(hexa):

    result = 0
    i = 0
    hexa1 = hexa[::-1]
    for j in hexa1:
        if (j == "a") | (j == "A"):
            j = 10
            result += j*(16**i)
            i += 1
        elif (j == "b") | (j == "B"):
            j = 11
            result += j*(16**i)
            i += 1
        elif (j == "c") | (j == "C"):
            j = 12
            result += j*(16**i)
            i += 1
        elif (j == "d") | (j == "D"):
            j = 13
            result += j*(16**i)
            i += 1
        elif (j == "e") | (j == "E"):
            j = 14
            result += j*(16**i)
            i += 1
        elif (j == "f") | (j == "F"):
            j = 15
            result += j*(16**i)
            i += 1
        elif hexa1.isalpha():
            print("\nenter valid hexadecimal number!! ")

        elif int(j) in range(0,9):
            j = int(j)
            result += j*(16**i)
            i += 1

    if result == 0:
        print("")
    else:
        print("your decimal nomber is : " , result)

# the main function  
def main():
    # the decoration of the head_sript
    print("\n"+"*" *120 +"\n")
    print(system)
    print("by : [hicham zakroum]")
    print(""+"*"*120 + "\n")
    # the first options
    print("\n=========>>>>choice your fisrt option {1 or 2 or 3 or 4} or y to exit() \n")
    print("[1] :convert decimal to [binary] or [octal] or [hexadecimal]")
    print("[2] :convert binary to [decimal] or [octal] or [hexadecimal]")
    print("[3] :convert octal to [binary] or [decimal] or [hexadecimal]")
    print("[4] :convert hexadecimal to [binary] or [octal] or [decimal]")
    print("[y] :to exit() ")
    first_option = input(" your first option : ")
    # the second options
    if first_option == "1":
        # the second option
        def decToX():
            print("\n=========>>>>choice your second option {1 or 2 or 3} or [B] to back() \n")
            print("[1] :convert decimal to [binary]")
            print("[2] :convert decimal to [octal]")
            print("[3] :convert decimal to [hexadecimal]")
            print("[B] :to go back()\n" )
            second_option = input(" your second option : ")
            if second_option == "1":
                bol = "x"
                while bol == "x" :
                    decToBin(input("\nenter your decimal number : "))
                    bol = input("\nenter [x] to replay, [B] to back() or any other key to exit() :")
                    if bol == "b" or  bol == "B" :
                        decToX()

            elif second_option == "2":
                bol = "x"
                while bol == "x" :
                    decToOct(input("\nenter your decimal number : "))
                    bol = input("\nenter [x] to replay, [B] to back() or any other key to exit() :")
                    if bol == "b" or  bol == "B" :
                        decToX()

            elif second_option == "3":
                bol = "x"
                while bol == "x" :
                    decToHex(input("\nenter your decimal number : "))
                    bol = input("\nenter [x] to replay, [B] to back() or any other key to exit() :")
                    if bol == "b" or  bol == "B" :
                        decToX()

            elif second_option == 'b' or second_option == "B":
                main()

            else :
                print("\n\n your option is invalid, please enter a valid option ")
                decToX()
        decToX()

    elif first_option == "2":
        # the second option
        def binToX():
            print("\n=========>>>>choice your second option {1 or 2 or 3} or [B] to back() \n")
            print("[1] :convert binary to [decimal]")
            print("[2] :convert binary to [octal]")
            print("[3] :convert binary to [hexadecimal]")
            print("[B] :to go back()\n" )
            second_option = input(" your second option : ")
            if second_option == "1":
                bol = "x"
                while bol == "x" :
                    binToDec(input("\nenter your binary number : "))
                    bol = input("\nenter [x] to replay, [B] to back() or any other key to exit() :")
                    if bol == "b" or  bol == "B" :
                        decToX()

            elif second_option == "2":
                bol = "x"
                while bol == "x" :
                    binToOct(input("\nenter your binary number : "))
                    bol = input("\nenter [x] to replay, [B] to back() or any other key to exit() :")
                    if bol == "b" or  bol == "B" :
                        decToX()

            elif second_option == "3":
                bol = "x"
                while bol == "x" :
                    binToHex(input("\nenter your binary number : "))
                    bol = input("\nenter [x] to replay, [B] to back() or any other key to exit() :")
                    if bol == "b" or  bol == "B" :
                        decToX()

            elif second_option == 'b' or second_option == "B":
                main()

            else :
                print("\n\nyour option is invalid, please enter a valid option ")
                binToX()
        binToX()


    elif first_option == "3":
        # the second option
        def octToX():
            print("\n=========>>>>choice your second option {1 or 2 or 3} or [B] to back() \n")
            print("[1] :convert octal to [binary]")
            print("[2] :convert octal to [decimal]")
            print("[3] :convert octal to [hexadecimal]")
            print("[B] :to go back()\n" )
            second_option = input(" your second option : ")
            if second_option == "1":
                bol = "x"
                while bol == "x" :
                    octToBin(input("\nenter your octal number : "))
                    bol = input("\nenter [x] to replay, [B] to back() or any other key to exit() :")
                    if bol == "b" or  bol == "B" :
                        decToX()

            elif second_option == "2":
                bol = "x"
                while bol == "x" :
                    octToDec(input("\nenter your octal number : "))
                    bol = input("\nenter [x] to replay, [B] to back() or any other key to exit() :")
                    if bol == "b" or  bol == "B" :
                        decToX()

            elif second_option == "3":
                bol = "x"
                while bol == "x" :
                    octToHex(input("\nenter your octal number : "))
                    bol = input("\nenter [x] to replay, [B] to back() or any other key to exit() :")
                    if bol == "b" or  bol == "B" :
                        decToX()

            elif second_option == 'b' or second_option == "B":
                main()

            else :
                print("\n\nyour option is invalid, please enter a valid option ")
                octToX()
        octToX()

    elif first_option == "4":
        # the second option
        def hexToX():
            print("\n=========>>>>choice your second option {1 or 2 or 3} or [B] to back() \n")
            print("[1] :convert hexadecimal to [binary]")
            print("[2] :convert hexadecimal to [octal]")
            print("[3] :convert hexadecimal to [decimal]")
            print("[B] :to go back()\n" )
            second_option = input(" your second option : ")
            if second_option == "1":
                bol = "x"
                while bol == "x" :
                    hexToBin(input("\nenter your hexadecimal number : "))
                    bol = input("\nenter [x] to replay, [B] to back() or any other key to exit() :")
                    if bol == "b" or  bol == "B" :
                        decToX()

            elif second_option == "2":
                bol = "x"
                while bol == "x" :
                    hexToOct(input("\nenter your hexadecimal number : "))
                    bol = input("\nenter [x] to replay, [B] to back() or any other key to exit() :")
                    if bol == "b" or  bol == "B" :
                        decToX()

            elif second_option == "3":
                bol = "x"
                while bol == "x" :
                    hexToDec(input("\nenter your hexadecimal number : "))
                    bol = input("\nenter [x] to replay, [B] to back() or any other key to exit() :")
                    if bol == "b" or  bol == "B" :
                        decToX()

            elif second_option == 'b' or second_option == "B":
                main()

            else :
                print("\n\nyour option is invalid, please enter a valid option ")
                hexToX()
        hexToX()
    elif first_option == "y" :
        print("\ngoodbye\n")
    else :
        main()

main()