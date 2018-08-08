#
#  File:
#    NUG_xy_plot_simple_PyNGL.py
#
#  Synopsis:
#    Illustrates how to customize curves and a legend in an XY plot
#
#  Categories:
#    xy plots
#
#  Author:
#    Karin Meier-Fleischer
#  
#  Date of initial publication:
#    October 2015
#
#  Description:
#    This example shows how to create an XY plot with different
#    styles of lines and a legend to match.
#
#  Effects illustrated:
#    o  Drawing a multi-curve XY plot using markers and lines
#    o  Customizing a legend
# 
#  Output:
#    A single visualization is produced.
#
#  Notes: The data for this example can be downloaded from 
#    http://www.ncl.ucar.edu/Document/Manuals/NCL_User_Guide/Data/
#     
"""
  NCL User Guide Python Example:   NUG_xy_plot_simple_PyNGL.py

     - marker
     - different line colors
     - legend
     - title
     - x-labels
     - y-labels

  09.10.15  kmf
"""
import numpy as np
import Ngl, Nio
import os

#-- create x-values
x2 = np.arange(100)

#-- create y-values
data   = np.arange(1,40,5)
linear = np.arange(100)
square = [v * v for v in np.arange(0,10,0.1)]

#-- retrieve maximum size of plotting data
maxdim = max(len(data),len(linear),len(square))

#-- create 2D arrays to hold 1D arrays above
y = -999.*np.ones((3,maxdim),'f')                   #-- assign y array containing missing values
y[0,0:(len(data))]   = data
y[1,0:(len(linear))] = linear
y[2,0:(len(square))] = square

#-- open a workstation
wks_type              = "png"                 #-- output type
wks_name              = os.path.basename(__file__).split(".")[0]
wks                   =  Ngl.open_wks(wks_type,wks_name)

#-- set resources
res                        =  Ngl.Resources()       #-- generate an res object for plot
res.tiMainString           = "Title string"         #-- set x-axis label
res.tiXAxisString          = "x-axis label"         #-- set x-axis label
res.tiYAxisString          = "y-axis label"         #-- set y-axis label

res.vpWidthF               =  0.9                   #-- viewport width
res.vpHeightF              =  0.6                   #-- viewport height

res.caXMissingV            =  -999.                 #-- indicate missing value
res.caYMissingV            =  -999.                 #-- indicate missing value

#-- marker and line settings
res.xyLineColors           =  ["blue","green","red"] #-- set line colors
res.xyLineThicknessF       =  3.0                    #-- define line thickness
res.xyDashPatterns         =  [0,0,2]                #-- ( none, solid, cross )
res.xyMarkLineModes        =  ["Markers","Lines","Markers"] #-- marker mode for each line
res.xyMarkers              =  [16,0,2]               #-- marker type of each line
res.xyMarkerSizeF          =  0.01                   #-- default is 0.01
res.xyMarkerColors         =  ["blue","green","red"] #-- set marker colors

#-- legend settings
res.xyExplicitLegendLabels = [" data"," linear"," square"]  #-- set explicit legend labels
res.pmLegendDisplayMode    = "Always"               #-- turn on the drawing
res.pmLegendOrthogonalPosF = -1.13                  #-- move the legend upwards
res.pmLegendParallelPosF   =  0.15                  #-- move the legend to the right
res.pmLegendWidthF         =  0.2                   #-- change width
res.pmLegendHeightF        =  0.10                  #-- change height
res.lgBoxMinorExtentF      =  0.16                  #-- legend lines shorter

#-- draw the plot
plot = Ngl.xy(wks,x2,y,res)

#-- the end
Ngl.end()
