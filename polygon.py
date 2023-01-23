with open("D:\workshops\klaworkshop2023\Milestone_Input\Milestone 1\Format_Source.txt", 'r') as f:
    data = f.read()

# Parse the data 
data_list = data.split('\n')
# print(data_list)

# class for the polygon
class polygon:
    def __init__(self,layer,datatype,coordinates):
        self.layer = layer
        self.datatype = datatype
        self.coordinates = coordinates

# Create a class for the data
class MyData():
    def __init__(self):
        self.header = data_list[:7]
        self.ploygons = self.create_polygon()
        self.footer = data_list[-2:]
        
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

ploy = data_instance.ploygons
print(ploy[0].coordinates)
