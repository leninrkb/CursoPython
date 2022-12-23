try:
    a = int(input('tu edad'))
    print(f'tu naciste en {2022-a}')
except:
    print('error ingreso datos')
    
    
    
    

try:
    a = int(input('tu edad'))
    print(f'tu naciste en {2022-a}')
except ValueError:
    print('error ingreso datos')
except ZeroDivisionError:
    print('error ingreso datos')
except TypeError:
    print('error type')
except AttributeError:
    print('error type')
except SyntaxError:
    print('error type')
except:
    print('algo salio mal')