import math

# opening the source file
with open("D:\workshops\klaworkshop2023\Milestone_Input\Milestone 4\Source.txt", 'r') as f:
    data = f.read()

# Parse the data 
sou_data_list = data.split('\n')
# print(data_list)
f.close()

# opening the POI file
with open("D:\workshops\klaworkshop2023\Milestone_Input\Milestone 4\POI.txt", 'r') as f:
    data = f.read()

# Parse the data 
poi_data_list = data.split('\n')
# print(data_list)
f.close()


# class for the polygon
class polygon:
    def __init__(self,layer,datatype,coordinates):
        self.layer = layer
        self.datatype = datatype
        self.coordinates = coordinates
        self.perimeter = self.get_perimeter()
        self.area = self.poly_area(x= [inner[0] for inner in coordinates] ,y = [inner[1] for inner in coordinates]  )
    
    def get_perimeter(self):
        perimeter = 0.0
        for i in range(len(self.coordinates)):
            p1 = self.coordinates[i]
            p2 = self.coordinates[i-1]
            perimeter += ((int(p1[0])- int(p2[0]))**2+(int(p1[1]) - int(p2[1]))**2)**0.5
        return perimeter
    
    # Calculate the area of the polygon
    def poly_area(self,x, y):
        area = 0.0
        for i in range(-1, len(x)-1):
            area += (int(x[i]) * int(y[i+1])) - (int(y[i])*int(x[i+1]))
        return 0.5*abs(area)

# Class for the data
class MyData():
    def __init__(self,data_list):
        self.header = data_list[:7]
        self.ploygons = self.create_polygon(data_list)
        self.footer = data_list[-3:]
        
    def create_polygon(self,data_list):
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
data_instance = MyData(data_list=sou_data_list)
print("Source Data Class created")

poi_instance = MyData(data_list= poi_data_list)
poi_poly = poi_instance.ploygons
print("POI Data Class created")


# writing it to output file
f= open("milestone4.txt","w+")

# adding header
for i in data_instance.header:
     f.write("".join(i))
     f.write("\n")
f.write("\n")

# adding polygon
for pol in data_instance.ploygons:
    for p_pol in poi_poly:
        if p_pol.perimeter != 0 and p_pol.area != 0 and ((pol.perimeter /p_pol.perimeter)**2  == (pol.area/p_pol.area)):
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
    
# adding footer
for i in data_instance.footer:
     f.write("".join(i))
     f.write("\n")
print("Data has been added to output file")

