'''Testing the speed of different printing methods'''

from decorators import timer

tests = dict()

def register_test(func):
    '''Register a function as a test'''
    tests[func.__name__] = func
    return func

@register_test
@timer
def str_format_simple(var, n):
    print("Testing str + ' ' + str")
    for _ in range(n):
        var + ' ' + var

@register_test
@timer
def str_old_format_test(var, n):
    print("Testing '%s %s' % (str, str)")
    for _ in range(n):
        '%s %s' % (var, var)

@register_test
@timer
def str_interpolation_test(var, n):
    print("Testing f'{str} {str}'")
    for _ in range(n):
        f'{var} {var}'

@register_test
@timer
def str_format_test(var, n):
    print("Testing '{} {}'.format(str, str)")
    for _ in range(n):
        '{} {}'.format(var, var)
        
@register_test
@timer
def str_format_index_test(var, n):
    print("Testing '{0} {0}'.format(str)")
    for _ in range(n):
        '{0} {0}'.format(var)
        
@register_test
@timer
def str_format_dict_test(var, n):
    var = {'var_str': var}
    print("Testing '{var_str} {var_str}'.format(**dict)")
    for _ in range(n):
        '{var_str} {var_str}'.format(**var)


if __name__ == '__main__':
    var = 'test_string'
    n = 100000
    #times = dict()
    for name in tests:
        tests[name](var, n)
        print('')
