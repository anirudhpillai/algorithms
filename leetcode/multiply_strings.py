# def multiply(num1, num2):
#     def mult(s, n):
#         print(s, n)
#         ans = ""
#         carry = 0
#         for i in s:
#             r = n * int(i) + carry
#             print(r)
#             if r > 9:
#                 carry = int(str(r)[:-1])
#                 ans += str(r)[-1]
#             else:
#                 carry = 0
#                 ans += str(r)
#
#         return str(ans) + str(carry)[::-1] if carry else str(ans)
#
#     adds = [("0"*i) + mult(num2[::-1], int(k)) for i, k in enumerate(reversed(num1))]
#     print(adds)
#
#     result = ""
#     carry = 0
#     for i in range(len(max(adds, key=len))):
#         s = 0
#         for j in adds:
#             if i < len(j):
#                 s += int(j[i])
#         s += carry
#         s = str(s)
#         if int(s) > 9:
#             carry = int(s[:-1])
#             result += s[-1]
#         else:
#             carry = 0
#             result += s
#
#     if carry:
#         result += str(carry)
#
#     return result[::-1]

def multiply(num1, num2):
    if num1 == '0' or num2 == '0':
        return "0"
        
    int[] d = new int[str1.length + str2.length];//digits
    for (int j = str2.length - 1; j >= 0; j--){//str2
        for (int i = str1.length - 1; i >= 0; i--){//str1
            int n = (str1[i] - '0') * (str2[j] - '0');
            // for each i,j, its multiplication contributes to d[i + j + 1] and d[i + j]
            d[i + j] += n / 10;//carry
            d[i + j + 1] += n % 10;//current digit
        }
    }
    for (int i = d.length - 1; i >= 1; i--){
        //rearrange the output
        d[i - 1] += d[i] / 10;//carry
        d[i] = d[i] % 10 + '0';//current digit
    }
    d[0] += '0';//don't forget the first digit
    int start = d[0] == '0'? 1 : 0;
    return new String(d, start, d.length - start);

print(multiply("50", "200"))
