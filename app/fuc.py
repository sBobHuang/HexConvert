

def hexStr2BinStr(hex_str):
    try:
        hex_str = hex_str.split(' ')[0]
        n = int(hex_str, 16)
        return format(n, '032b')
    except:
        return '您输入的有误'


def dec2BinStr(n, digits):
    try:
        return format(n, f'0{digits}b')
    except:
        return '您输入的有误'


def binStr2Dec(bin_str):
    try:
        return int(bin_str.replace(' ', ''), 2)
    except:
        return '您输入的有误'


def hexStr2Dec(bin_str):
    try:
        return int(bin_str.replace(' ', ''), 16)
    except:
        return '您输入的有误'


def complementBinStr2Dec(bin_str):
    try:
        ans = 0
        for i in range(1, len(bin_str)):
            ans = ans * 2 + int(bin_str[i])
        # 如果是负数
        if bin_str[0] == '1':
            return -(2 ** (len(bin_str) - 1) - ans)
        return ans
    except:
        return '您输入的有误'


def Dec2ComplementBinStr(dec, digits):
    try:
        return bin(2 ** digits + dec)[-digits:]
    except:
        return '您输入的有误'


def BinStr2HexStr(bin_str):
    bin_str = bin_str.replace(' ', '')
    # bin_str = bin_str.split(' ')[0]
    n = int(bin_str, 2)
    return format(n, f'0{(len(bin_str)+3)//4}x')


def Dec2HexStr(n):
    # bin_str = bin_str.split(' ')[0]
    return format(n, 'x')
