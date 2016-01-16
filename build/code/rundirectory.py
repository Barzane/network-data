# -*- coding: utf-8 -*-

import os, glob, shutil

import add_network_measures, filter_data, carrier_dummy
import competitive_dummy, airport_mktshr_hhi, bin_to_txt
import convert_bin_to_text, merge_bin, analysis_full_bin

#print
#
#print 'clear contents of \output and \\temp and \input'
#
#for folder in ['..\\output\\*', '..\\temp\\*', '..\\input\\*']:
#
#    folder_contents = glob.glob(folder)
#
#    for filename in folder_contents:
#        os.remove(filename)

full_sample = True

if full_sample:
    
    time_periods = [(y, q) for y in range(1999, 2014) for q in range(1, 5)]
    
else:
    
    time_periods = [(2013, 3), (2013, 4)]

#for (year, quarter) in time_periods:
#
#    print
#    print str(year) + 'Q' + str(quarter)
#    
#    print 'copy data_year_quarter.bin datafile from ..\data to \input'
#    
#    src = '..\\..\\data\\data_' + str(year) + '_' + str(quarter) + '.bin'
#    dst = '..\\input\\data_' + str(year) + '_' + str(quarter) + '.bin'
#    
#    shutil.copyfile(src, dst)
#    
#    print 'add network measures to data_year_quarter.bin, save to \\temp'
#    
#    add_network_measures.add_network(year, quarter)
#    
#    low_route_threshold = 10
#    
#    print 'remove carriers with low number of routes (threshold = ' + str(low_route_threshold) + '), save to \\temp'
#    
#    filter_data.filter_low_routes_by_carrier(year, quarter, low_route_threshold)
#    
##    print 'add carrier dummies, save to \\temp'
##    
##    carrier_dummy.add_dummies(year, quarter)
#    
#    print 'add Dai et al (2014) monopoly, duopoly, competitive dummies, save to \\temp'
#    print '...Evans & Kessides (1993) IV function called by competitive_dummy.py'
#    
#    competitive_dummy.add_dummies(year, quarter)
#    
#    print 'add airport-level marketshare and airport-level hhi, save to \\temp'
#    
#    airport_mktshr_hhi.add_variables(year, quarter)
#    
#    print 'convert bin to txt, save txt to \output'
#    
#    bin_to_txt.convert_to_txt(year, quarter)
#    
#    print 'move bin from \\temp to \output'
#    
#    src = '..\\temp\\data_' + str(year) + '_' + str(quarter) + '.bin'
#    dst = '..\\output\\data_' + str(year) + '_' + str(quarter) + '.bin'
#    
#    shutil.move(src, dst)
#
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
