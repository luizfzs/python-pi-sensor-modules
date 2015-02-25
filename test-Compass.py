#=====================================#
# Author: Luiz Felipe Zafra Saggioro  #
#=====================================#


from Compass import Compass

compass = Compass(0x1e)

print compass.getOrientation()
