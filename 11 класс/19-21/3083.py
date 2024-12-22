def game(s, step):
    if 36<=s<60:
        return step %2==0
    if step == 0:
        return 0
    if s >=60:
        return step % 2 !=0
    h = [game(s+1,step-1),game(s*2,step-1),game(s*3,step-1)]
    return any(h) if (step-1)%2==0 else all(h)

print('19)',[s for s in range(1,36) if game(s,2)])
print('20)',len([s for s in range(1,36) if not(game(s,1)) and game(s,3) and not(game(s,2)) and not(game(s,4))]))
print('21)',[s for s in range(1,36) if not(game(s,2)) and game(s,4) and not(game(s,1)) and not(game(s,3))])
