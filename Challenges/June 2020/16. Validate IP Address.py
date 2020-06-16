class Solution:
    def validIPAddress(self, IP: str) -> str:
        try:
            if ("-" in IP):
                pass
            elif ("." in IP):
                IP = IP.split(".")
                if (len(list(filter(lambda x : int(x)<0 or int(x)>=256 or (x[0]=='0' and x!='0'), IP))) == 0 and len(IP)==4):
                    return "IPv4"
            elif (":" in IP):
                IP = IP.split(":")
                if (len(list(filter(lambda x : int(x, 16)<0 or int(x, 16)>=int("ffff", 16) or len(x)>4, IP))) == 0 and len(IP)==8):
                    return "IPv6"
        except:
            pass
        return "Neither"