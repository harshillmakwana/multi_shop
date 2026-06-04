import razorpay

KEY_ID = 'rzp_test_SuHJDPoOSzG2d8'

variants = [
    'I9vELDUhWgPRScJ0TijJxHn9', # Capital I
    'l9vELDUhWgPRScJ0TijJxHn9', # Lowercase l
    '19vELDUhWgPRScJ0TijJxHn9', # Digit 1
]

def test_variants():
    for var in variants:
        try:
            print(f"Testing key secret: '{var}'...")
            client = razorpay.Client(auth=(KEY_ID, var))
            order_data = {
                'amount': 10000, 
                'currency': 'INR',
                'payment_capture': 1
            }
            order = client.order.create(data=order_data)
            print(f"-> SUCCESS for secret '{var}'!")
            print("Order ID:", order['id'])
            return var
        except Exception as e:
            print(f"-> FAILED for secret '{var}': {str(e)}")
            
    print("All variants failed.")
    return None

if __name__ == '__main__':
    test_variants()
