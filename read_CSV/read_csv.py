#
# Read a csv file
# 

def main():

    inp = open( "sighting.csv", "r")

    sightings = []

    line = inp.readline()
    while line != "":
        row = line.strip().split( ",")
        sightings.append( row)
        line = inp.readline()
    inp.close()
    print( sightings) 

    for i in range( 0, len( sightings)):
        for j in range( 0, len( sightings[i])): 
            print( f"{sightings[i][j]:>12}", end="")
    print()
    
    print( "row 2", sightings[1])
    print( "cell 2, 3", sightings[1][2])

    col_list = []
    col = 2
    for i in range( 0, len(sightings)):
        col_list.append( sightings[i][2])

    print( "col", col_list)

main()
    
