def game(s, step):
    if s>=165:
        return step %2==0
    if step == 0:
        return 0
    h = [game(s+1,step-1),game(s*2,step-1)]
    return any(h) if (step-1)%2==0 else all(h)

print('19)',[s for s in range(1,165) if not(game(s,1)) and (game(s,2))])
print('20)',[s for s in range(1,165) if not(game(s,1)) and (game(s,3))])
print('21)',[s for s in range(1,165) if not(game(s,2)) and game(s,4)])