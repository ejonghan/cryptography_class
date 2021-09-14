def vigenere(plain_message, keyword):
    e = ""
    count = 0 # keystream 을 반복시키기위한 변수
    key_stream = []
    
    # keystream 생성
    for c in keyword:
        n = s.find(c)
        key_stream.append(n)
 
    for c in plain_message:
        p_value = s.find(c)
        n = count % len(keyword)
        n = key_stream[n]
        c_value = (p_value + n) % 26
        e = e + s[c_value]
        
        count = count+1
    print(e)
