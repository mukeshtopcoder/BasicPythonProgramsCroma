"""

6. Logical Operator
and , or , not
and:- If all the inputs are True then the Answer is True
        - Otherwise False

a = 7
b = 5
print( a>b and b>a )       # False
print( a>b and b>3 )       # True
print( a>b and b>3 and a>40 )  # False

or:- If all the inputs are False then the Answer is False
        - Otherwise True
        
a = 7
b = 5
print(a>b or b>a)     # True
print(a>b or b>3)     # True
print(a>10 or b>10)   # False
print(a>10 or b>10 or a>5)  # True

not:- not gate is also called inverter gate.
it works on only 1 input.
if input is True -> Answer is False. and vice-versa

print( not 10<5 )


print( int(True) )
print( int(False) )

print( bool(1) )
print( bool(0) )
print( bool(-345) )
print( bool(3753) )

Every number is True besides 0.

a = 7
b = 5
print( a and b )
print( b and a )
# it will return last value if there is no ZERO.
a = 7
b = 0
print( a and b )
print( b and a )


a = 7
b = 5
print( a or b )
print( b or a )
a = 7
b = 0
print( a or b )
print( b or a )
a = 0
b = 0
print( a or b )

print( not 0 )



7. Bitwise Operator
or            |
and           &
leftshift     <<
rightshift    >>

a = 19
b = 22
print( a & b )

a = 11
b = 22
print( a | b )

a = 9
b = 12
print( a | b )

Right Shift
a = 25
print(a>>5)

a = 3
print(a<<3)


# Data Type
Number
        int - 23,546,78,-324,345
        float - 312.456 , 43.876, -546.76
        binary - 0b11001 , 0b1001   ( 0,1 )
        octal - 0o234               (0,1,2,3,4,5,6,7)
        decimal/int - 637 , 47
        hexadecimal - 0x23B , 0xF92 ,
        0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F
        complex - a+jb ->a real , b imaginary
                3+7j
Boolean
        True
        False
String
        Character  (A , a )
        String  (Aman , Raman)
Sequential (List , Tuple)
        a = [32,54,76,98,43]   - LIST   []
        a = (32,54,76,87,98)   - Tuple  ()
SET
    A = { 2,4,65,7,98 }
Dictionary
    A = {32:324,5:768,7:98,1:543}

a = 0xF9
print(a)
"""
print("My First Program")
