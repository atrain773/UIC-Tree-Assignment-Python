def get_input(input_message):
    return int(input(input_message))
    
def calculate_offset(width, num_tree_parts):
    return int((width - num_tree_parts) / 2) + 1

def calculate_num_stars(triangle_num, row_num):
    return 2 * (triangle_num + row_num) + 1

def create_char_string(char, num_char):
    char_string = ''
    for i in range(num_char):
        char_string = char_string + char
    return char_string
    
def print_leaves(n, width, triangle_height, offset_char_type, leaf_char_type):
    for triangle_num in range(n):
        print_triangle(triangle_num, width, triangle_height, offset_char_type, leaf_char_type)
    return

def print_triangle(triangle_num, width, triangle_height, offset_char_type, leaf_char_type):
    for row_in_triangle in range(triangle_height):
        num_stars = calculate_num_stars(triangle_num, row_in_triangle)
        offset = calculate_offset(width, num_stars)
        print_leaf_row(offset, num_stars, offset_char_type, leaf_char_type)

def print_leaf_row(offset, num_stars, offset_char_type, leaf_char_type):
    offset_string = create_char_string(offset_char_type, offset - 1)
    star_string = create_char_string(leaf_char_type, num_stars)
    leaf_row_string = offset_string + star_string
    print(leaf_row_string)

def print_trunk(n, width, offset_char_type, wood_char_type):
    for i in range(2 * n):
        print_trunk_row(n, width,offset_char_type, wood_char_type)
    return

def print_trunk_row(n, width,offset_char_type, wood_char_type):
    offset_string = create_char_string(offset_char_type, n)
    trunk_row_string = offset_string + wood_char_type
    print(trunk_row_string)

def print_tree(n, width, triangle_height, offset_char_type, leaf_char_type, wood_char_type):
    print_leaves(n, width, triangle_height, offset_char_type, leaf_char_type)
    print_trunk(n, width,offset_char_type, wood_char_type)

OFFSET_CHAR_TYPE_ = ' '
LEAF_CHAR_TYPE_ = '*'
WOOD_CHAR_TYPE_ = '|||'
INPUT_MESSAGE_ = "Please insert a number: "

N_ = get_input(INPUT_MESSAGE_)
WIDTH_ = 2 * N_ + 3
TRIANGLE_HEIGHT_ = 3


print_tree(N_, WIDTH_, TRIANGLE_HEIGHT_, OFFSET_CHAR_TYPE_, LEAF_CHAR_TYPE_, WOOD_CHAR_TYPE_)
