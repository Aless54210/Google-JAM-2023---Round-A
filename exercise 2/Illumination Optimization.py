def min_light(streetLen, lightRadius, posLights):
    nbLights = 0
    actualPos = 0
    
    while actualPos < streetLen:
        if nbLights >= len(posLights) or posLights[nbLights] - lightRadius > actualPos:
            return "IMPOSSIBLE"
            
        actualPos = posLights[nbLights] + lightRadius
        nbLights += 1
    
    nbLightsOpti = nbLights
    for i in range(len(posLights)):
        newPosLights = posLights[:i] + posLights[i+1:]
        nbLights = min_light(streetLen, lightRadius, newPosLights)
        if nbLights != "IMPOSSIBLE" and nbLights < nbLightsOpti:
            nbLightsOpti = nbLights
    
    return nbLightsOpti

n = int(input())
for i in range(n):
    streetLen, lightRadius, nbLights = map(int, input().split())
    posLights = []
    line = input().split()
    for b in line:
        posLights.append(int(b))
    
    minLights = min_light(streetLen, lightRadius, posLights)

    print("Case #{}: {}".format(i+1, minLights))