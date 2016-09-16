'''
@Author:        Albert Mundu
@Description:   To read coordinates from the given file
'''

class ReadData(object):
    '''class ReadData'''
    def __init__(self,samplefile=None):
        '''ReadData(samplefile): takes a file as an argument'''
        self.file=open(samplefile,'r')

    def getxy(self):
        """getxy returns x,y1,y2 after reading a line from a file"""
        data=self.file.readline().split(' ')
        if data[0]=='':
            return (None,None,None)
        else:
            return int(data[0]),int(data[1]),int(data[2])

    def getfptr(self):
        return self.file

    def close(self):
        self.file.close()