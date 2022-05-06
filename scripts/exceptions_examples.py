class Error(Exception):
    pass

class GatewayError(Error):
    pass

class BankServerError(Error):
    pass

def payments(payment, error = None):
    try:
        payment = payment
        if error == 'gateway':
            raise GatewayError
        
        elif error == 'bank':
            raise BankServerError
        else:
            print('Payment' + str(payment) + 'is successful')
        
    except GatewayError:
        print('gateway error')
        
    except BankServerError:
        print('bank server error')
        
    finally:
        print('Visit Again!')
        
