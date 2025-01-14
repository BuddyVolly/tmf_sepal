### TILE SHOWING THE RESULTS

from sepal_ui import sepalwidgets as sw
from sepal_ui import mapping as sm
import ipyvuetify as v

from component.message import cm
from component.scripts import * 
from component import parameter as pm

# create an empty result tile that will be filled with displayable plot, map, links, text
class VisualizationTile(sw.Tile):
    
    def __init__(self, aoi_io, io, **kwargs):
        
        # gather the io
        self.aoi_io = aoi_io
        self.io = io
        
        # create an output alert 
        self.output = sw.Alert()
                        
        # add the widgets 
        self.m = sm.SepalMap()
              
        # construct the Tile with the widget we have initialized 
        super().__init__(
            id_    = "visualization_widget", # the id will be used to make the Tile appear and disapear
            title  = cm.visualization.title, # the Title will be displayed on the top of the tile
            inputs = [self.m],
            output = self.output
        )
        
                
    def _on_change(self, change):

        # Display the map
        display_result(
            self.aoi_io.get_aoi_ee(),
            self.io.dataset,
            self.m, 
            self.io.year_beg,
            self.io.year_end
        )
        
        
