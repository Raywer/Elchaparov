def game(s, step):
    if s>=37:
        return step %2==0
    if step == 0:
        return 0
    h = [game(s+1,step-1),game(s+2,step-1),game(s+3,step-1),game(s*2,step-1)]
    return any(h) if (step-1)%2==0 else all(h)

print('19)',[s for s in range(1,37) if game(s,2)])
print('20)',min([s for s in range(1,37) if game(s,3) and not(game(s,1))]),max([s for s in range(1,37) if game(s,3) and not(game(s,1))]))
print('21)',[s for s in range(1,37) if not(game(s,2)) and game(s,4) and not(game(s,1)) and not(game(s,3))])