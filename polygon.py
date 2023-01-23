with open("D:\workshops\klaworkshop2023\Milestone_Input\Milestone 1\Format_Source.txt", 'r') as f:
    data = f.read()

# Parse the data 
data_list = data.split('\n')
# print(data_list)
f.close()

# class for the polygon
class polygon:
    def __init__(self,layer,datatype,coordinates):
        self.layer = layer
        self.datatype = datatype
        self.coordinates = coordinates

# Class for the data
class MyData():
    def __init__(self):
        self.header = data_list[:7]
        self.ploygons = self.create_polygon()
        self.footer = data_list[-3:]
        
    def create_polygon(self):
        list = []
        
        layer = ""
        datatype = ""
        xy_list = []
        
        for i in range(7,len(data_list)-2):
            if data_list[i] == "boundary":
                layer = (data_list[i+1].split())[1]
                datatype = (data_list[i+2].split())[1]
                
                coordinates_list =  data_list[i+3].split()
                xy = []
                
                for i in range(2,len(coordinates_list)):
                    xy.append(coordinates_list[i])
                    if i%2 == 1:
                        xy_list.append(xy)
                        xy = []
            elif data_list[i] == "endel":
                list.append(polygon(layer,datatype,xy_list))
                layer = ""
                datatype = ""
                xy_list = [] 
        return list
            

# Create an instance of the class
data_instance = MyData()
print("Data Class created")
# writing it to output file
f= open("milestone1.txt","w+")

# adding header
for i in data_instance.header:
     f.write("".join(i))
     f.write("\n")
f.write("\n")

# adding polygon
count = 0
for pol in data_instance.ploygons:
    if count == 2:
        break;
    f.write("boundary\n")
    layer_str = "layer "+str(pol.layer) +"\n"
    f.write(layer_str)
    datatype_str = "datatype "+str(pol.datatype) +"\n"
    f.write(datatype_str)
    xy_str = "xy  "+ str(len(pol.coordinates)) + "  "
    for x in pol.coordinates:
        xy_str  = xy_str + str(x[0]) + " "
        xy_str  = xy_str + str(x[1]) + "  "
    f.write(xy_str)
    f.write("\nendel\n")
    count += 1
    
# adding footer
for i in data_instance.footer:
     f.write("".join(i))
     f.write("\n")
print("Data has been added to output file")

def calculate_area(polygon):
    n = len(polygon)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += polygon[i][0] * polygon[j][1]
        area -= polygon[j][0] * polygon[i][1]
    area = abs(area) / 2.0
    return area