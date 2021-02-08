"""Function to print 4 digit numbers"""
one = ["","One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
tens_1 = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
tens_2 = ["","Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

while True:
    try:
        while True:
            a = input()
            b = int(a)
            c = str(a)
            d = c[0]
            e = int(d)

            if type(int(a)) == int:
                if int(a) == 0:
                    print("Zero")

                elif len(c) == 1:
                    print(one[b])

                elif len(c) == 2:
                    f = c[1]
                    g = c[1]

                    if int(c[1]) == 0:
                        print(tens_2[int(c[0])])
                    elif int(c[0]) == 1:
                        print(tens_1[int(f)])
                    else:
                        print(tens_2[e] +" "+ one[int(g)])

                elif len(c) == 3:
                    if int(c[1]) == 0:
                        if int(c[2]) == 0:
                            print(one[int(c[0])] + " Hundred")
                        else:
                            print(one[int(c[0])] + " Hundred And " + one[int(c[2])])
                    elif int(c[1]) == 1:
                        print(one[int(c[0])] + " Hundred And " + tens_1[int(c[2])])
                    else:
                        if int(c[2]) == 0:
                            print(one[int(c[0])] + " Hundred And " + tens_2[int(c[1])])
                        else:
                            print(one[int(c[0])] + " Hundred And " + tens_2[int(c[1])] +" "+one[int(c[2])])

                elif len(c) == 4:
                    f = c[1]
                    g = c[1]
                    if int(c[1]) == 0:
                        if int(c[2]) == 0:
                            if int(c[3]) == 0:
                                print(one[int(c[0])] + " Thousand")
                            else:
                                print(one[int(c[0])] + " Thousand And " + one[int(c[3])])
                        elif int(c[2]) == 1:
                            print(one[int(c[0])] + " Thousand And " + tens_1[int(c[3])])
                        else:
                            if int(c[3]) == 0:
                                print(one[int(c[0])] + " Thousand And " + tens_2[int(c[2])])
                            else:
                                print(one[int(c[0])] + " Thousand And " + tens_2[int(c[2])] +" "+one[int(c[3])])
                    else:
                        if int(c[2]) == 0:
                            if int(c[3]) == 0:
                                print(one[int(c[0])]+ " Thousand "+ one[int(c[1])] + " Hundred")
                            else:
                                print(one[int(c[0])] + " Thousand " + one[int(c[1])] + " Hundred And " + one[int(c[3])])
                        elif int(c[2]) == 1:
                            print(one[int(c[0])] + " Thousand "+ one[int(c[1])]+ " Hundred And "+ tens_1[int(c[3])])

                        else:
                            if int(c[3]) == 0:
                                print(one[int(c[0])]+ " Thousand " + one[int(c[1])] + " Hundred And " + tens_2[int(c[2])])
                            else:
                                print(one[int(c[0])]+ " Thousand " + one[int(c[1])]+ " Hundred And "+ tens_2[int(c[2])]+" "+one[int(c[3])])
                elif len(c) > 4:
                  print("Number not in Range. Please enter a number between the Range 0000 - 9999")





    except ValueError:
      if a.lower() == "exit":
        print("Thank you")
        break
      elif a.lower() == "back":
        print("Thank you")
        break
      else:
        print("Invalid Input")

