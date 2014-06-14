from timeit import time

def calc_time(func):
    def wrappedFunc(*args, **kwargs):
        start_time = time.time()
        val = func(*args, **kwargs)
        end_time = time.time()
        print '\n-------------'
        print 'Function-name:', func.func_name
        print 'Time: %fs' % (end_time - start_time)
        print '-------------'
        return val
    return wrappedFunc