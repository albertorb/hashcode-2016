def create_image_with_commands(list_commands, len_i, len_j):
    print(len_i)
    print len_j
    new_image = [[False for j in xrange(len_j)] for i in xrange(len_i)]
    for command in list_commands:
        # eraser
        print(command)
        if command[0] == 0:
            if new_image[command[1]][command[2]] is True:
                new_image[command[1]][command[2]] = False
            # else:
            #     raise Exception("Eraser when it is False")

        # square
        elif command[0] == 1:
            center_i = command[1]
            center_j = command[2]
            size = command[3]
            start_i = center_i - size
            end_i = center_i + size + 1
            start_j = center_j - size
            end_j = center_j + size + 1
            for i in xrange(start_i, end_i):
                for j in xrange(start_j, end_j):
                    new_image[i][j] = True
        # line
        elif command[0] == 2:
            first_cell_i = command[1]
            first_cell_j = command[2]
            second_cell_i = command[3]
            second_cell_j = command[4]
            horizontal = first_cell_i - second_cell_i
            vertical = first_cell_j - second_cell_j
            if horizontal == 0 and vertical == 0:
                new_image[first_cell_i][first_cell_j] = True
            elif horizontal == 0:
                if vertical < 0:
                    start_j = first_cell_j
                    end_j = second_cell_j + 1
                else:
                    start_j = second_cell_j
                    end_j = first_cell_j + 1
                for j in xrange(start_j, end_j):
                    new_image[first_cell_i][j] = True
            elif vertical == 0:
                if horizontal < 0:
                    start_i = first_cell_i
                    end_i = second_cell_i + 1
                else:
                    start_i = second_cell_i
                    end_i = first_cell_i + 1
                for i in xrange(start_i, end_i):
                    new_image[i][first_cell_j] = True
            else:
                raise Exception("problems with command line")
        else:
            raise Exception("Invalid command %i" % command[0])
    return new_image


def score_image_without_commands(image_original, new_image):
    score = 0
    equals = True
    for i in xrange(len(image_original)):
        for j in xrange(len(image_original[i])):
            if image_original[i][j] == new_image[i][j]:
                score += 2
            else:
                equals = False
    return equals, score


def score_image_with_commands(image_original, list_commands):
    # 0 eraser
    # 1 square
    # 2 line
    new_image = create_image_with_commands(list_commands, len(image_original), len(image_original[0]))
    equals, score = score_image_without_commands(image_original, new_image)
    score -= len(list_commands)
    return equals, score
