import pandas as pd
import geopandas as gpd
import PIL
import io


dr = pd.read_csv(r"C:\Users\Rohit Kumar\Desktop\dataset.csv")

dr = dr.groupby("CNTRYNAME").sum()
#create a transpose of dataframe
dr_tr = dr.T

# Read in the world map 
world = gpd.read_file(r"C:\Users\Rohit Kumar\Desktop\world map\World_Map.shp")
world.replace("Depocratic Republic of Congo","Zaire", inplace = True)
world.replace("Bahamas","Bahamas, The", inplace = True)
world.replace("Brunei Darussalam","Brunei", inplace = True)
world.replace("Belarus","Byelarus", inplace = True)
world.replace("Falkland Islands (Malvinas)","Falkland Islands (Islas Malvinas)", inplace = True)
world.replace("Viet Nam","Vietnam", inplace = True)
world.replace("United Republic of Tanzania","Tanzania, United Republic of", inplace = True)
world.replace("Syrian Arab Republic","Syria", inplace = True)
world.replace("Korea, Republic of","South Korea", inplace = True)
world.replace("Cote d'Ivoire","Ivory Coast", inplace = True)

#merging the data
merge = world.join(dr, on = "NAME", how = "right")

image_frames = []

for dates in merge.columns.to_list()[2:97]:

    #plot
    ax = merge.plot(column = dates,
                cmap = 'OrRd',
                figsize = (10,10),
                legend = True,
                scheme = "user_defined",
                classification_kwds = {'bins':[10,20,50,100,500,1000,5000,10000,50000]},
                edgecolor = 'black',
                linewidth = 0.4)

    #title for map
    ax.set_title('Daily increase in covid-19 cases - ' + dates , fontdict = {'fontsize':20}, pad = 12.5)
    ax.set_axis_off()
    ax.get_legend().set_bbox_to_anchor((0.2,0.65))
    
    img = ax.get_figure()
    
    f= io.BytesIO()
    img.savefig(f, format = 'png', bbox_inches = 'tight')
    f.seek(0)
    image_frames.append(PIL.Image.open(f))
    
# creating a gif
image_frames[0].save('Covid-19 map.gif', format = 'GIF',
                     append_images = image_frames[1:],
                    save_all = True, duration = 300,
                    loop = 1)
                
f.close() 

  
    
    