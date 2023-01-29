def do_stuff(num):
    try:
        return 15 / int(num)
    except ValueError:
        return 'Please enter a number.'
    except ZeroDivisionError as err:
        return err


print(do_stuff(''))
