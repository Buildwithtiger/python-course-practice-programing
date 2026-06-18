def main():
    try:
      a=int(input("enter the no"))
    except Exception as e:
      print("enter the numeric value")
    finally:
      print("the value of a is",a)
main()