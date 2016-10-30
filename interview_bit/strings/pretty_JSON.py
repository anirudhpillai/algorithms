def pretty_JSON(A):
    indent = 0
    result = []
    curr = ""
    for i in A:
        if i == '{' or i == '[':
            if curr:
                result.append('\t' * indent + curr)
                curr = ""
            result.append('\t' * indent + i)
            indent += 1
        elif i == '}' or i == ']':
            if curr:
                result.append('\t' * indent + curr)
            curr = i
            indent -= 1
        elif i == ',':
            result.append('\t' * indent + curr + i)
            curr = ""
        else:
            curr += i

    if curr:
        result.append('\t' * indent + curr)
        
    return result


for i in pretty_JSON('"{"attributes":[{"nm":"ACCOUNT","lv":[{"v":{"Id":null,"State":null},"vt":"java.util.Map","cn":1}],"vt":"java.util.Map","status":"SUCCESS","lmd":13585},{"nm":"PROFILE","lv":[{"v":{"Party":null,"Ads":null},"vt":"java.util.Map","cn":2}],"vt":"java.util.Map","status":"SUCCESS","lmd":41962}]}"'):
    print(i)

for i in pretty_JSON('{"id":100,"firstName":"Jack","lastName":"Jones","age":12}"'):
    print(i)
