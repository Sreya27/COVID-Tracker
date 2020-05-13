def moveTower(disc,fromPole, toPole, withPole):
    if disc >= 1:
        moveTower(disc-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(disc-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)

moveTower(4,"A","B","C")
