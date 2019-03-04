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
    coefficient_odd = [0, 1, -1, 2, -2]
    coefficient_even = [0.5, -0.5, 1.5, -1.5]

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
                if count_brick == 1:
                    y = y
                elif count_brick%2 == 1:
                    y = y + 0.01
                elif count_brick%2 == 0:
                    y = y - 0.01

                z= int((count_layer/2)+1)*h + (int(count_layer/2))*t - 0.03

                #print(0,y,z)

                list_of_positions[count_layer-1][count_brick-1] = (0,y,z)

                count_brick = count_brick + 1

            # if layer is ODD NUMBER OF BRICKS and HORIZONTAL then... (layer 4, 8)
            elif current_layer%2 == 1 and count_layer%2 == 0:

                y= coefficient_odd[count_brick-1]*h
                if count_brick == 1:
                    y = y
                elif count_brick%2 == 1:
                    y = y + 0.01
                elif count_brick%2 == 0:
                    y = y - 0.01

                z= int((count_layer/2)+1)*t + (int((count_layer/2)+1))*h - 0.03 + 0.73
                #print(0,y,z)

                list_of_positions[count_layer-1][count_brick-1] = (0,y,z)

                count_brick = count_brick + 1

            # if layer is EVEN NUMBER OF BRICKS and VERTICAL then... (layer 3, 7)
            elif current_layer%2 == 0 and count_layer%2 == 1:

                y= coefficient_even[count_brick-1]*h

                if count_brick%2 == 1:
                    y = y + 0.01
                else:
                    y = y - 0.01

                z= int((count_layer/2)+1)*h + (int(count_layer/2))*t - 0.03 + 0.73
                #print(0,y,z)
                list_of_positions[count_layer-1][count_brick-1] = (0,y,z)

                count_brick = count_brick + 1

            # if layer is EVEN NUMBER OF BRICKS and HORIZONTAL then... (layer 2, 6)
            elif current_layer%2 == 0 and count_layer%2 == 0:

                y= coefficient_even[count_brick-1]*h
                if count_brick%2 == 1:
                    y = y + 0.01
                else:
                    y = y - 0.01

                z= int((count_layer/2)+1)*t + (int((count_layer/2)+1))*h - 0.03 + 0.73
                #print(0,y,z)
                list_of_positions[count_layer-1][count_brick-1] = (0,y,z)

                count_brick = count_brick + 1


            # move on to next layer
        count_layer = count_layer + 1

    return list_of_positions

def posify(Coordinates):

    block_poses = list()
    #if block_poses[i][j] = int
    for i in range(0,5):
        g = i
        p =  Coordinates[0][g][0]
        u =  Coordinates[0][g][1]
        v =  Coordinates[0][g][2]
        Coordinates[0][g] = block_poses.append(Pose(
                position=Point(x = p, y = u, z = v),
                orientation=overhead_orientation))

    if len(block_poses) == 5: #checks the bottom layer has been added to the list
        for i in range(0,4):
            g = i
            p =  Coordinates[1][g][0]
            u =  Coordinates[1][g][1]
            v =  Coordinates[1][g][2]
            Coordinates[1][g] = block_poses.append(Pose(
                       position=Point(x = p, y = u, z = v),
                      orientation=overhead_orientation))

    if len(block_poses) == 9: #Checks the bottom two layers
        for i in range(0,4):
            g = i
            p =  Coordinates[2][g][0]
            u =  Coordinates[2][g][1]
            v =  Coordinates[2][g][2]
            Coordinates[2][g] = block_poses.append(Pose(
                       position=Point(x = p, y = u, z = v),
                      orientation=overhead_orientation))

    if len(block_poses) == 13: #Checks the bottom three layers
        for i in range(0,3):
            g = i
            p =  Coordinates[3][g][0]
            u =  Coordinates[3][g][1]
            v =  Coordinates[3][g][2]
            Coordinates[3][g] = block_poses.append(Pose(
                       position=Point(x = p, y = u, z = v),
                      orientation=overhead_orientation))

    if len(block_poses) == 16: #Checks the bottom four layers
        for i in range(0,3):
            g = i
            p =  Coordinates[4][g][0]
            u =  Coordinates[4][g][1]
            v =  Coordinates[4][g][2]
            Coordinates[4][g] = block_poses.append(Pose(
                       position=Point(x = p, y = u, z = v),
                      orientation=overhead_orientation))

    if len(block_poses) == 19: #Checks the bottom four layers
        for i in range(0,2):
            g = i
            p =  Coordinates[5][g][0]
            u =  Coordinates[5][g][1]
            v =  Coordinates[5][g][2]
            Coordinates[5][g] = block_poses.append(Pose(
                       position=Point(x = p, y = u, z = v),
                      orientation=overhead_orientation))

    if len(block_poses) == 21:
        for i in range(0,2):
            g = i
            p =  Coordinates[6][g][0]
            u =  Coordinates[6][g][1]
            v =  Coordinates[6][g][2]
            Coordinates[6][g] = block_poses.append(Pose(
                       position=Point(x = p, y = u, z = v),
                      orientation=overhead_orientation))

    if len(block_poses) == 23:
        for i in range(0,1):
            g = i
            p =  Coordinates[7][g][0]
            u =  Coordinates[7][g][1]
            v =  Coordinates[7][g][2]
            Coordinates[7][g] = block_poses.append(Pose(
                       position=Point(x = p, y = u, z = v),
                      orientation=overhead_orientation))

    print (Coordinates)
    return Coordinates
