import g

v1=g.range_i(1000)
tab = [123, 3, 255, 0, 100]

file=open("test1.bin","wb")
file1=open("2k_int.bin","wb")
file1.write(bytes(v1))
file1.close()
file.write(bytes(tab))# zapis jako strinG!!!

#bytearray(newFileBytes))
file.close()

a=""
f = open("test1.bin", "rb")

#print bytearray(newFileBytes)
#print bytes(newFileBytes)

try:
    byte = f.read(1)
    while byte != "":
        
        a+=str(byte)
        byte = f.read(1)
finally:
    f.close()


#print a
