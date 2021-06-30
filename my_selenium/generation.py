def gen_str_cookies(cookies):
    data_cookies = []
    for item in [i for i in cookies if i['domain'] == '.amazon.com']:
        
        # if item['name'] in ["sid","x-main","sess-at-main","session-token","sp-cdn","session-token"]:
        # 	temp = str(item['name'])+'="'+str(item['value'])+'"'
        # else:
        temp = str(item['name'])+'='+str(item['value'])

        data_cookies.append(temp)

    return ';'.join(data_cookies)