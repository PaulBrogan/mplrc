#       transaction.py
#       
#       Copyright 2011 alex arsenovic <arsenovic@virginia.edu>
#
#       This fork was carried out by Paul Brogan pbrogan02@qub.ac.uk
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#



#import matplotlib as mpl



  
def apply(col = 2, axis =1, width = 1, height = 1, borderBottom = 1, 
          borderLeft = 1, borderRight = 1):
    """col is column width, col = 1 means single column, col = 2 full page width
    
    axis = 1 means single axis (typically left) axis = 2 means twin axis (twinx)
    
    width = 1, height = 1 means keep standard width and height, but somethimes 
    these need to be adjusted, so there they are, play around.
    
    borderBottom = 1, is standard border, but increasing this will add extra 
    space e.g. to accomodate a large legend or to fit a 3D plot
    """
    import matplotlib.pyplot as plt
    import sys
    
    plt.rcParams.update(plt.rcParamsDefault)
    
    def defaults():
        
        params = {\
        'backend': 'GTKAgg',
        
        'font.family': 'serif',
        'font.serif': 'Times',
        'font.sans-serif' : ['Helvetica', 'Avant Garde', 'Computer Modern Sans serif'],    
        
        'axes.linewidth': 0.75,
        
        'text.usetex': True,
    
        'figure.dpi':300,    
    
        'savefig.dpi':600    
        }
        
        return(params)
        
    def defaultsCol1():
        
        params = {\
                  
        'figure.figsize': (3.5, 2.5),
        
        'figure.subplot.left' : 0.155,
        'figure.subplot.right': 0.95,
        'figure.subplot.bottom': 0.15,
        'figure.subplot.top': .95,
        
        'axes.labelsize': 9,
        'axes.linewidth': .75,
        
        'font.size': 9,
    
        'legend.fontsize': 7,
        'xtick.labelsize': 7,
        'ytick.labelsize': 7,    
    
        'lines.linewidth':1.25    
        }
            
        return(params)  
            
    
    def defaultsCol2():
        
        params = {\
                  
        'figure.figsize': (7, 5),
    
        'figure.subplot.left' : 0.125,
        'figure.subplot.right': 0.9,
        'figure.subplot.bottom': 0.1,
        'figure.subplot.top': .95,
        
        'grid.color'       :   'black',
        'grid.linestyle'   :   '-' ,
        'grid.linewidth'   :   0.5,     # in points
        'grid.alpha'       :   1.0, 
        
        'axes.axisbelow' : True,
        'axes.labelsize': 12,
        
        'text.dvipnghack' : None,
        
        'font.size': 12,
    
        'legend.fontsize': 10,
        'xtick.labelsize': 12,
        'ytick.labelsize': 12,    
    
        'lines.linewidth':2.0  
        }
        
        return(params)   
    try:
        
        params = defaults()
        #print('col = ', col)
        if col == 1:  
            params.update(defaultsCol1())
            print('im in col 1')
            
            if axis == 2:
                params['figure.subplot.right'] = 0.9

            
        elif col == 2:
            params.update(defaultsCol2())
            if axis == 2:
                params['figure.subplot.right'] = 0.875
        
        if height > 1:
            
            x, y = params['figure.figsize']
            params['figure.figsize'] = (x, ((height + 1)/2)*y)
            print('###########',x,y)
            print('###########',x, ((height + 1)/2)*y)

        if width > 1:
            x, y = params['figure.figsize']
            params['figure.figsize'] = (((height + 1)/2)*x, y)
            
        if borderBottom != 1:
            params['figure.subplot.bottom'] *= borderBottom
            
        if borderLeft != 1:
            params['figure.subplot.left'] *= borderLeft
            
        if borderRight != 1:
            params['figure.subplot.right'] *= borderRight
        
        plt.rcParams.update(params)
        
    except:
        print("FAILED TO APPLY IEEE FORMAT_error", sys.exc_info()[:2])