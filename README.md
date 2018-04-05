# The code below was edited and forked

As mentioned below, this method adjusts the RCparams in matplotlib
to apply default settings to plots in order to make them satisfy
IEEE plot format requirements.

A couple of adjustments were made to the original RCparams to make it
run on my machine, this mostly involved removing fonts.

A little extra functionality was also added, possibly making it easier 
to adjust the width of plots in the script (primarily single column and
double column plots), additional functionality was added to allow the 
height and width of the plots to be adjusted, as-well-as adding extra space
below the plot to accommodate large legends and 3D plots. This is commented
in the code, with the function. As I need additional functionality I tend to
add it.

As with matplotlib generally, sometimes the code needs to be executed twice
to apply/change settings, maybe be a wee bit vigilant with this at first

-Paul




# This project is Deprecated.

See the native matplotlib support for styles
###http://matplotlib.org/users/style_sheets.html

-- 
 mplrc is a python module which provides an easy way to change
 matplotlib's plotting configuration for specific publications. 
 
 once installed, you can apply the matplotlib configuration 
 like  so

import mplrc.ieee.transaction


then all plots after this line will follow the conventions defined by 
ieee.transactions. if there is no module matching your publication
and you make one, please submit it to us!


-alex

