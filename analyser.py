def main():
    
    total=0
    even_count=0
    for i in range(10):
        x=int(input("tell me 10 numbers"))
        if i == 0:
            highest = x
            lowest = x
        if x > highest:
            highest = x
        if x < lowest:
            lowest = x

        total=total + x
        if x % 2==0:
            print("even")
            even_count = even_count + 1
        else:
            print("odd")  
    print(f"even numbers = {even_count}")  
    print(f"Average={total/10}")  
    print(f"highest number={highest}")
    print(f"lowest number={lowest}")
            
main()


