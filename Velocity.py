
import math

def Velocity ( Energy, Mass ):
    Velocity = math.sqrt( Energy * 2000 / Mass )

    return Velocity

print ( Velocity ( 15.5, 0.547 ) )