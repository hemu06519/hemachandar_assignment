def get_value(dictobj, key_value, key_exists = False):
    for k,v in dictobj.items():
        if k==key_value and key_exists == False:
            key_exists=True
        if key_exists==True:
            if isinstance(v, dict):
                get_value(v, key_value, key_exists)
            else:
                print("{} exists in the object, its value is :{}".format(key_value,v))
        else:
            get_value(v, key_value, key_exists)

if __name__ == "__main__":
  # Test Case : 1
  dictobj= {'a':{'b':{'c':'d'}}}
  # Test 1
  key_value = 'a'
  get_value(dictobj, key_value)
  # Test 2
  key_value = 'b'
  get_value(dictobj, key_value)
  # Test 3
  key_value = 'c'
  get_value(dictobj, key_value)
  # Test Case : 2
  dictobj = {'x':{'y':{'z':'a'}}} 
  # Test 4
  key_value = 'x'
  get_value(dictobj, key_value)
  # Test 5
  key_value = 'y'
  get_value(dictobj, key_value)
  # Test 6
  key_value = 'z'
  get_value(dictobj, key_value)
