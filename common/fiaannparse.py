# -*- coding: utf-8 -*-
"""
Functions for parsing the FIA annotation output


"""

import pandas as pd

def parseAnnotationExcel(filename, sheetname = 'Sheet1'):
    #parses an annotation EXCEL file into a dictionary
    keggDict = {}
    xl = pd.ExcelFile(filename)
    df1 = xl.parse(sheetname)
    for index, row in df1.iterrows():    
        if not ('+' in row[4] or '[-' in row[4]): #don't include the isotopes
            for kegger in row.id.split(';'):
                if kegger not in keggDict.keys():
                    keggDict[kegger] = {}
                    keggDict[kegger]['ion'] = int(row[8])
                    keggDict[kegger]['score'] = int(row[5])
                    keggDict[kegger]['name'] = row[1]
                elif int(row[5]) > keggDict[kegger]['score']:
                    keggDict[kegger]['ion'] = int(row[8])
                    keggDict[kegger]['score'] = int(row[5])
           
    return keggDict

def revParseAnnotationExcel(filename, sheetname = 'Sheet1'):
    revDict = {}
    xl = pd.ExcelFile(filename)
    df1 = xl.parse(sheetname)
    for index, row in df1.iterrows(): 
        if not ('+' in row[4] or '[-' in row[4]): #don't include the isotopes
            ind=row[8]
            for kegg_id in row.id.split(';'):
                if ind not in revDict.keys():
                    revDict[ind]={}
                    revDict[ind]['kegg'] = [kegg_id]
                    revDict[ind]['score'] = int(row[5])
                    revDict[ind]['name'] = [row[1]]
                else:
                    revDict[ind]['kegg'].append(kegg_id)
                    revDict[ind]['name'].append(row[1])
    return revDict
