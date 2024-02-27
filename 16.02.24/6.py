def rook(s_p,e_p):
    if s_p[0]==e_p[0] or s_p[1]==e_p[1]:
        return True
    return False
def bishop(s_p,e_p):
    if abs(s_p[0]-e_p[0])==abs(s_p[1]-e_p[1]):
        return True
    return False

def queen(s_p,e_p):
    if rook(s_p, e_p) or bishop(s_p, e_p):
        return True
    return False

def main():
    word=input().lower()
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    if word=='ладья':
        answer=rook((a,b),(c,d))
    if word=='слон':
        answer = bishop((a, b), (c, d))
    if word=='ферзь':
        answer = queen((a, b), (c, d))
