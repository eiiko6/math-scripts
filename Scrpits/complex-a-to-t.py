import math as m
import fractions as f

# Define those yourself ;P
reNumber = -8 # Rational part
imNumber = 0 # Imaginary part

modulus = m.sqrt((reNumber)**2+(imNumber)**2) # Find the modulus

cosθ = reNumber/modulus # Find cos axis
sinθ = imNumber/modulus # Find sin axis

θ = (m.atan2(sinθ, cosθ)) # Find the θ angle
# We could do `θ = f.Fraction(m.atan2(sinθ, cosθ)).limit_denominator()` to fraction it eventually

trForm = str(modulus) + "(cos(" + str(θ) + ") + i*sin(" + str(θ) + "))" # Assemble the expression as string

print(trForm) # There you go!
