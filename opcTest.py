import OpenOPC
import pywintypes

def readopc(tags):
    pywintypes.datetime = pywintypes.TimeType
    opc = OpenOPC.client()

    opc.connect('Matrikon.OPC.Simulation.1')
    try:
        data = opc.read(tags, group='Group0', update=1)
    except OpenOPC.TimeoutError:
        print("TimeoutError occured")

    return data

def writeToFile(path, data):
    for (tagName, value, conf, timeStamp) in data:
        fileName=path+tagName+'.csv'
        line=str(value)+';'+str(conf)+';'+str(timeStamp)+'\n'

        with open(fileName, "a") as f:
            f.write(line)

if __name__=='__main__':
    tags = ['Random.Int1','Random.Int4']
    data = readopc(tags)
    writeToFile('C:\\temp\\',data)