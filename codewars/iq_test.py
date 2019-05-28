def iq_test('test_str'):
    test_list = test_str.split(' ')
    even = [ev for ev in test_list if ev % 2 == 0]
    odd = [od for od in test_list if od % 2 == 1]
    return test_list.index(