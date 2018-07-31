import matplotlib.image as img
 
import matplotlib.pyplot as plot
 
myfile = "pictures/test.jpg"
 
myimage = img.imread(myfile)
 
plot.imshow(myimage)
 
plot.show()