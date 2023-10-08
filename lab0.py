#Raj Rana
#I pledge my honor that I have abided by the Stevens Honor System.
print("Welcome to Color converstion from RGB to CMY")
r=int(input("Please input a R(Red Value)"))
g=int(input("Please input a G(Green Value)"))
b=int(input("Please input a B(Blue Vlaue)"))
w=max(r/255,g/255,b/255)
c=(w-(r/255))/w
m=(w-(g/255))/w
y=(w-(b/255))/w
k=1-w
print("Here are the new CMYK values",c,",",m,",",y,",",k,"!")
    
