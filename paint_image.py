__author__ = 'antonioirizar'


def paint_image(matrix_image):
    with open('paint_image.ou', 'w') as f:
        for i in xrange(len(matrix_image)):
            for j in xrange(len(matrix_image[i])):
                if matrix_image[i][j]:
                    f.write('#')
                else:
                    f.write('.')
            f.write('\n')
    f.close()
