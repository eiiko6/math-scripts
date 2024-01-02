# Todo: use classes next time

import math as m
# import fractions as f

def convert(reNumber, imNumber):

    modulus = m.sqrt((reNumber)**2+(imNumber)**2) # Find the modulus

    cosTheta = reNumber/modulus # Find cos axis
    sinTheta = imNumber/modulus # Find sin axis

    Theta = (m.atan2(sinTheta, cosTheta)) # Find the Theta angle
    # We could do `Theta = f.Fraction(m.atan2(sinTheta, cosTheta)).limit_denominator()` to fraction it eventually

    trForm = str(modulus) + "(cos(" + str(Theta) + ") + i*sin(" + str(Theta) + "))" # Assemble the expression as string

    return(trForm) # There you go!

if __name__ == "__main__":
    print(convert(-8, 0)) # Print the function
