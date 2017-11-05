from Bio import SeqIO
import random

path = 'C:\\Users\\Lorin\\Documents\\Challenge 4-selected\\'
outputPath = 'C:\\Users\\Lorin\\Documents\\Challenge 4-selected\\'
filenames = ["SRS016297.denovo_duplicates_marked.trimmed.singleton.fastq",
             "SRS015895.denovo_duplicates_marked.trimmed.singleton.fastq"]

seqTypeName = 'SRS016297_SRS015895'
#file = path + filename
nullType = '1'
i = 0
length = []

class Training():

    def __init__(self):
        self.training_file = open(outputPath+seqTypeName+".txt", "w")
        self.seqType = '0'
        self.createTraining()
        self.training_file.close()

    def createTraining(self):
        # Open a file
        #print(file)
        for filename in filenames:
            file = path + filename
            print(file)
            seqRec1 = SeqIO.parse(file, 'fastq')
            if filename in "SRS015895.denovo_duplicates_marked.trimmed.singleton.fastq":
                self.seqType = '1'
                print(self.seqType)
            file = ""
            for sequence_steps in seqRec1:
                firstStep = 0
                secStep = firstStep + 60
                seqSixty = str(sequence_steps._seq[firstStep:secStep])
                seqListArray = self.commaSeparate(seqSixty, self.seqType) # Last arg is seqType
                if seqListArray and (not 'N' in seqListArray):
                    self.training_file.write(str(seqListArray)+ '\n')
                # randSeq = self.random_seq() # Generate random sequence, length 60
                # seqListArray = self.commaSeparate(randSeq, nullType)  # Last arg is random seqType - 16
                # self.training_file.write(str(seqListArray)+ '\n')

    def commaSeparate(self, seqSixty, seqType):
        if len(seqSixty) == 60:
            seqArray = seqSixty.replace('C', '1')
            seqArray = seqArray.replace('T', '2')
            seqArray = seqArray.replace('G', '3')
            seqArray = seqArray.replace('A', '4')
            seqListArray = ''
            for seqChar in seqArray:  # 60 Chars
                seqListArray += str(seqChar) + ','
            seqListArray += seqType  # CHANGE WITH EACH NEW FILE
            return seqListArray
        else:
            return ''

    def random_seq(self):
        sixtyRandom = ''.join(random.choice(['C','T','G','A']) for x in range(60))
        return sixtyRandom

if __name__ == '__main__':
    #import TechGui
    Training()