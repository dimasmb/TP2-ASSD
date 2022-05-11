import numpy as np
import math

#OLA Algorithm. Just for Additive

def olaAlgorithm(input,window,timeFunction,overlap=0.5):

    grainSize = len(window)
    windowSpace = (1.0 - overlap) * len(window)

    maxTime = math.ceil(timeFunction[-1])
    outSize = maxTime
    output = np.zeros(outSize)

    slotNumber = math.ceil(maxTime/windowSpace)
    outSlot = np.zeros(slotNumber)
    outSlot[0] = 0

    for i in range(1,slotNumber):

        outSlot[i] = i*windowSpace



    inSlots= np.zeros(slotNumber)

    j=0
    tau=0
    for i in range(1,slotNumber):
        while tau < outSlot[i]:
            tau = timeFunction[j]
            j = j+1
        inSlots[i] = j-1


    windowCenter = math.floor(len(window) / 2.0)

    grain= np.multiply( input[0:windowCenter], window[windowCenter:])
    output[0:windowCenter]= grain[0:windowCenter]

    for j in range(1,slotNumber):

        k=0

        grain = np.zeros(grainSize)
        startIndex = math.floor(inSlots[j] - (grainSize/2.0))
        prePoints = grainSize

        startOut= math.floor(outSlot[j] - (grainSize/2.0))
        endGrain = math.floor(inSlots[j] + (grainSize/2.0))

        if(startIndex< 0):

            prePoints = grainSize + startIndex
            startIndex = 0

            while (k < prePoints) and (startOut + k < outSize) and (startIndex + k < len(input)):

                grain[grainSize - prePoints + k] = input[startIndex + k] * window[grainSize - prePoints + k]
                output[startOut + k] = grain[grainSize - prePoints + k]
                k= k + 1
        else:
            while (k < grainSize) and (startOut + k <outSize) and ( startIndex + k < len(input)) and (startIndex + k < endGrain):
                grain[k] = input[startIndex + k]
                grain[k] = grain[k]*window[k]
                output[startOut + k] = grain[k]
                k= k+1


    theWindows = np.zeros(len(output))

    for i in range(0,slotNumber):
        k=0
        firstIndex = math.floor( outSlot[i] - (grainSize/2.0) )
        prePoints = grainSize

        if (firstIndex < 0):
            prePoints = grainSize + firstIndex
            firstIndex = 0

            while (k < prePoints) and (firstIndex + k < len(output)):

                theWindows[firstIndex + k] = theWindows[firstIndex + k] + window[grainSize - prePoints + k]
                k=k+1
        else:
            while (k < prePoints)and(firstIndex + k < len(output)):

                theWindows[firstIndex + k] = theWindows[firstIndex + k] + window[k]
                k=k+1

    avoidError = 1e-10 * np.ones(theWindows.size)
    finalWindows = theWindows + avoidError

    return np.divide(np.array(output), finalWindows)
