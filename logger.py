def log_this(org_func):
    import logging 
    from time import perf_counter,sleep
    from datetime import datetime

    logging.basicConfig(filename='Loged_{}.log'.format(org_func.__name__),level=logging.INFO)

    def wrapper(*args,**kwargs):
        start=perf_counter()
        # time.sleep(2)
        org_func(*args,**kwargs)
        end=perf_counter()
        logging.info('Function ({}) ran with args:{}, and kwargs:{} at :{} took {:2f}s to execite'.format(org_func.__name__,args,kwargs,datetime.now(),(end-start)))
        
        return org_func(*args,**kwargs)
    
    return wrapper