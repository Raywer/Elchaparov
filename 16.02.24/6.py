def rook(s_p,e_p):
    if s_p[0]==e_p[0] or s_p[1]==e_p[1]:
        return True
    return False
def bishop(s_p,e_p):
    if abs(s_p[0]-e_p[0])==abs(s_p[1]-e_p[1]):
        return True
    return False



def main():
    word=input().lower()
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    if word=='ладья':
        answer=rook((a,b),(c,d))