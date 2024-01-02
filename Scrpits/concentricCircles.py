import math as m

def calc_area(radius):
    return m.pi * radius**2

def main():
    rep = input("Is there the same distance between the circles? (yes/no) ").lower()
    
    if rep == "yes":
        rmax = float(input("What is the radius of the target in cm? "))
        dist = float(input("What is the distance in cm between 2 circles? "))
        
        radi = []
        areas = []
        
        while rmax > dist:
            radi.append(rmax)
            rmax -= dist
        
        for i in range(len(radi)):
            areas.append(calc_area(radi[i]) - calc_area(radi[i] - dist))
            print(f"The area of disk {i + 1} is {areas[i]:.2f} cm²")

        last_circle_area = calc_area(radi[-1] - dist)
        print(f"The area of the central circle is {last_circle_area:.2f} cm²")

    elif rep == "no":
        nbcrcl = int(input("How many circles are there? "))
        print("Please give the raduses in descending order:")
        radi = [float(input(f"What is the radius of circle {i + 1}? ")) for i in range(nbcrcl)]

        # Check for errors in the radiuses
        if radi != sorted(radi, reverse=True):
            print("Warning: Radiuses should be provided in descending order. Calculation result may be inaccurate.")
            return

        areas = [calc_area(radi[i]) - calc_area(radi[i + 1]) if i < nbcrcl - 1 else calc_area(radi[i]) for i in range(nbcrcl)]
        
        for i in range(nbcrcl):
            print(f"The area of disk {i + 1} is {areas[i]:.2f} cm²")

if __name__ == "__main__":
    main()
