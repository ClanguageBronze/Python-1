import folium
from html2image import Html2Image
from PIL import Image

def ReturnMap(X,Y):
    hti=Html2Image()
    x=float(X)
    y=float(Y)
    g_map=folium.Map(location=[x,y],zoom_start=38)
    marker=folium.Marker([X,Y],popup='campus seven'
                    ,icon=folium.Icon(color='blue'))
    marker.add_to(g_map)
    g_map.save('C:/Users/user/Documents/GitHub/Python/map1.html')
    hti.screenshot(url='C:/Users/user/Documents/GitHub/Python/map1.html', save_as='map.png')
    rimg = Image.open("map.png")
    Img = rimg.resize((960, 540))
    Img.save("map.png")
