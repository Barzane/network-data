# -*- coding: utf-8 -*-

import cPickle

def convert_to_txt(year, quarter):
    
    print '\nconvert bin to txt, save txt to \output'
    
    src = '..\\temp\\data_' + str(year) + '_' + str(quarter) + '.bin'
    
    f = open(src, 'rb')
    data = cPickle.load(f)
    f.close()
            
    def createText(dataDict):
        
        outputString = ''
        
        firstKey = dataDict.keys()[0].split('_')
        filenameOut = 'data_' + firstKey[-2] + '_' + firstKey[-1] + '.txt'
        
        headerLine = 'origin' + '\t' + 'dest' + '\t' + 'carrier' + '\t' + 'year' + '\t' + 'quarter' + '\t'
        
        def keytest(data, cle):
        
            x = sorted(data[cle].keys(), key = lambda v: v.upper())
        
            return x
        
        varList = keytest(dataDict, dataDict.keys()[0])
        
        for i in varList:
            headerLine += str(i)
            headerLine += '\t'
            
        headerLine = headerLine.rstrip()
        headerLine += '\n'
        
        outputString += headerLine
        
        nb = 0
        
        for key in dataDict.keys():
            
            nb += 1
            
            dataLine = key.split('_')
            
            for j in varList:
                dataLine += [dataDict[key][j]]
                
            for item in dataLine:
                outputString += str(item)
                outputString += '\t'
                
            outputString = outputString.rstrip()
            outputString += '\n'
            
        outputString = outputString.rstrip()
                
        h = open('..\\output\\'+filenameOut, 'wb')
        h.write(outputString)
        h.close()
        
        return None
    
    createText(data)
    
    return None
