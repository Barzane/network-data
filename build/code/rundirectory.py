# -*- coding: utf-8 -*-

import os, glob, shutil

import add_network_measures
import filter_data
import carrier_dummy
import competitive_dummy
import airport_mktshr_hhi
import bin_to_txt
import convert_bin_to_text
import merge_bin
import analysis_full_bin

def horizontal():
    
    print
    print '-'*90
    print
    
    return None

def manual_transfer_reminder():

    print 'manually transfer data_yyyy_q.bin datafiles (output from data-bin) to data\\ before run'
    print
    print '** DISK SPACE REQUIREMENT: ~ 171 MB to store 84 quarterly datafiles (1993_1 to 2013_4) **'
    print
    
#    raw_input('press a key to continue')
    
    return None

def clear_output_temp_input():
    
    print 'clear contents of \output and \\temp and \input'

    for folder in ['..\\output\\*', '..\\temp\\*', '..\\input\\*']:
    
        folder_contents = glob.glob(folder)
    
        for filename in folder_contents:
            
            os.remove(filename)
    
    return None

horizontal()
   
manual_transfer_reminder()
horizontal()
    
clear_output_temp_input()
horizontal()

full_sample = False

if full_sample:
    
    time_periods = [(y, q) for y in range(1999, 2014) for q in range(1, 5)]
    
else:
    
    time_periods = [(2013, 3), (2013, 4)]

for (year, quarter) in time_periods:

    print str(year) + 'Q' + str(quarter)
    
    print '\ncopy data_year_quarter.bin datafile from ..\data to \input'
    
    src = '..\\..\\data\\data_' + str(year) + '_' + str(quarter) + '.bin'
    dst = '..\\input\\data_' + str(year) + '_' + str(quarter) + '.bin'
    
    shutil.copyfile(src, dst)
    
#    print 'add network measures to data_year_quarter.bin, save to \\temp'
    
    add_network_measures.add_network(year, quarter)
    
    sss
    
    low_route_threshold = 10
    
    print 'remove carriers with low number of routes (threshold = ' + str(low_route_threshold) + '), save to \\temp'
    
    filter_data.filter_low_routes_by_carrier(year, quarter, low_route_threshold)
    
#    print 'add carrier dummies, save to \\temp'
#    
#    carrier_dummy.add_dummies(year, quarter)
    
    print 'add Dai et al (2014) monopoly, duopoly, competitive dummies, save to \\temp'
    print '...Evans & Kessides (1993) IV function called by competitive_dummy.py'
    
    competitive_dummy.add_dummies(year, quarter)
    
    print 'add airport-level marketshare and airport-level hhi, save to \\temp'
    
    airport_mktshr_hhi.add_variables(year, quarter)
    
    print 'convert bin to txt, save txt to \output'
    
    bin_to_txt.convert_to_txt(year, quarter)
    
    print 'move bin from \\temp to \output'
    
    src = '..\\temp\\data_' + str(year) + '_' + str(quarter) + '.bin'
    dst = '..\\output\\data_' + str(year) + '_' + str(quarter) + '.bin'
    
    shutil.move(src, dst)

#print 'merge .bin output files'
#
#merge_bin.wrapper(time_periods)    
#
#print 'convert .bin to .txt'
#
#convert_bin_to_text.convert()

print 'analyzing full-sample data .bin'

analysis_full_bin.analysis()

print 'move pyc files (byte code) from \code to \\temp'

src = '.\\'
dst = '..\\temp\\'

for folder in [src + '*.pyc']:
    
    folder_contents = glob.glob(folder)
    
    for filename in folder_contents:        
        filename_split = filename.split('\\')[-1]
        shutil.move(filename, dst + filename_split)
