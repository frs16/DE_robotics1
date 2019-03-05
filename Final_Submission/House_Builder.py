from geometry_msgs.msg import (
    PoseStamped,
    Pose,
    Point,
    Quaternion,
)


def house_coordinates():

    t = 0.06  #thickness
    w = 0.09  #width
    h = 0.2  #height

    # coordinates are (x,y,z)
    # middle block is (0,0,170)
    # bottom of table is (0,0,0)

    # one list of all positions in order
    list_of_positions = [[(0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0)],
    [(0,0,0), (0,0,0), (0,0,0), (0,0,0)],[(0,0,0), (0,0,0), (0,0,0), (0,0,0)],
    [(0,0,0), (0,0,0), (0,0,0)], [(0,0,0), (0,0,0), (0,0,0)], [(0,0,0), (0,0,0)],
    [(0,0,0), (0,0,0)], [0,0,0]]



    # number of bricks in each layer
    layers = [5, 4, 4, 3, 3, 2, 2, 1]

    # coefficients for alternating brick picking from middle
    coefficient_odd = [0, 1.1, -1.1, 2.2, -2.2]
    coefficient_even = [-0.55, 0.55, -1.65, 1.65]

    #count layers
    count_layer = 1

    for i in range(len(layers)):

        # iterate through layers
        current_layer = layers[i]

        # count bricks
        count_brick = 1

        # iterate through bricks in layer
        for x in range(current_layer):


            #if layer is ODD NUMBER OF BRICKS and VERTICAL then... (layer 1, 5)
            if current_layer%2 == 1 and count_layer%2 == 1:

                y = coefficient_odd[count_brick-1]*h

                z= int(((count_layer)/2))*(h+t) + h - 0.03 + 0.1

                #print(0,y,z)

                list_of_positions[count_layer-1][count_brick-1] = (0.5,y,z)

                count_brick = count_brick + 1

            # if layer is ODD NUMBER OF BRICKS and HORIZONTAL then... (layer 4, 8)
            elif current_layer%2 == 1 and count_layer%2 == 0:

                y= coefficient_odd[count_brick-1]*h

                z= int(((count_layer)/2))*(h+t) - 0.03 + 0.1
                #print(0,y,z)

                if count_layer == 8:
                    list_of_positions[7]=[(0.5,y,z)]
                else:
                    list_of_positions[count_layer-1][count_brick-1] = (0.5,y,z)

                count_brick += 1

            # if layer is EVEN NUMBER OF BRICKS and VERTICAL then... (layer 3, 7)
            elif current_layer%2 == 0 and count_layer%2 == 1:

                y= coefficient_even[count_brick-1]*h

                z= int(((count_layer)/2))*(h+t) + h - 0.03 + 0.1
                #print(0,y,z)
                list_of_positions[count_layer-1][count_brick-1] = (0.5,y,z)

                count_brick = count_brick + 1

            # if layer is EVEN NUMBER OF BRICKS and HORIZONTAL then... (layer 2, 6)
            elif current_layer%2 == 0 and count_layer%2 == 0:

                y= coefficient_even[count_brick-1]*h

                z= int(((count_layer)/2))*(h+t) - 0.03 + 0.1
                #print(0,y,z)
                list_of_positions[count_layer-1][count_brick-1] = (0.5,y,z)

                count_brick = count_brick + 1


            # move on to next layer
        count_layer = count_layer + 1

    return list_of_positions

def posify(Coordinates, v_orientation, h_orientation):

    #if block_poses[i][j] = int
    for i in range(len(Coordinates)):
        for j in range(len(Coordinates[i])):
            if i % 2:
                p =  Coordinates[i][j][0]
                u =  Coordinates[i][j][1]
                v =  Coordinates[i][j][2]
                Coordinates[i][j] =(Pose(
                        position=Point(x = p, y = u, z = v),
                        orientation=h_orientation))
            else:
                p =  Coordinates[i][j][0]
                u =  Coordinates[i][j][1]
                v =  Coordinates[i][j][2]
                Coordinates[i][j] =(Pose(
                        position=Point(x = p, y = u, z = v),
                        orientation=v_orientation))

    print (Coordinates)
    return Coordinates
