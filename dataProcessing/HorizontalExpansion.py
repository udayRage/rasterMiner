import glob
import pandas as pd
import raster2tsv
import re


class verticalExpansion:
    def __init__(self, path,fileExtension,outputFolder,startBand, endBand):
        self.path = path + '/*.'+fileExtension
        self.outputFolder = outputFolder
        self.startBand =startBand
        self.endBand = endBand

    def convert(self):
        # reading each file in a folder
        my_df = pd.DataFrame()
        file = glob.glob(self.path)
        listOfDataframes = []
        for file in glob.glob(self.path):
            #extracting output filename
            temp = re.findall(r'\d+', file)
            res = list(map(int, temp))
            out_csv = (self.outputFolder +'/'+ str(res[2]) + '.csv')

            # convert to csv file
            text =''
            for bandNo in range(self.startBand, self.endBand+1):
                text = text + '-band ' + bandNo + ' '
            paramters = text + file + ' ' + out_csv
            raster2tsv.raster2tsv(paramters)
            df = pd.read_csv(out_csv, index_col=None, header=None)
            listOfDataframes.append(df)
            frames = pd.concat(listOfDataframes, axis=0, ignore_index=True)
        print(frames)


if __name__ == '__main__':
    a = verticalExpansion('/home/hp/raster_files','nc')
    a.convert()
