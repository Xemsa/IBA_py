#2.1
'''
    *
   * *
  *   *
 *     *
***   ***
  *   *
  *   *
  *****
'''

print(" Простой вариант")
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

print(" С переносами")
print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****",sep="\n")

print(" С разделителем")
print("    *","   * *","  *   *"," *     *","***   ***","  *   *","  *   *","  *****",sep="\n")

print(" Масштабируемый")
n=3;
s=" "
z="*"
print(s*4*n,z,sep="");
print(s*3*n,z,sep="",end="");   print(s*((2*n)-1),z,sep="")
print(s*2*n,z,sep="",end="");   print(s*((4*n)-1),z,sep="")
print(s*1*n,z,sep="",end="");   print(s*((6*n)-1),z,sep="")
print(2*(z+s*(n-1)),z,sep="",end=""); print(s*((4*n)-1),2*(z+s*(n-1)),z,sep="")
print(s*2*n,z,sep="",end="");   print(s*((4*n)-1),z,sep="")
print(s*2*n,z,sep="",end="");   print(s*((4*n)-1),z,sep="")
print(s*2*n,z,sep="",end="");   print(z*((4*n)-1),z,sep="")

