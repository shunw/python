from collections import Counter
import re
def fil_lines(line_info, col_n): 
    # fill out the row, horizontally
    # line_info = '....'
    info_dict = Counter(line_info)
    half_qty = col_n / 2
    
    if info_dict['W'] == half_qty: 
        line_info = line_info.replace('.', 'B')
        return line_info
        
    elif info_dict['B'] == half_qty:
        line_info = line_info.replace('.', 'W')
        return line_info
    return line_info

def fil_vert(row_info, row_n):  
    # fill out the col, vertically
    # line_info = ['.', 'W']
    info_dict = Counter(row_info)
    half_qty = row_n / 2

    if info_dict['W'] == half_qty: 
        row_info = [i.replace('.', 'B') for i in row_info]
        print ('fun: row info for w: ', row_info)
        return row_info
        
    elif info_dict['B'] == half_qty:
        row_info = [i.replace('.', 'W') for i in row_info]
        print ('fun: row info for b: ', row_info)
        return row_info
    return row_info
    
def tp_2_ls(tp_input): 
    return [i for i in tp_input]

def ls_2_tp(ls_input): 
    return (i for i in ls_input)

def make_up(input_grid): 
    '''
    fill out all the defined fill
    by two rules
    '''
    row_n = len(input_grid)
    col_n = len(input_grid[0])
    res = list()
    print ('before change: ', input_grid)
    # for r in input_grid: 
    #     # this is to change the row
    #     r = fil_lines(r, col_n)
    #     res.append(r)
    res_col = list
    for c in range(col_n): 
        temp_c_ls = list()
        
        for r in range(row_n): 
            temp_c_ls.append(input_grid[r][c])
        
        res_1_col = fil_vert(temp_c_ls, row_n).copy()

        for r in range(row_n): 
            # judge and change the grid
            if input_grid[r][c] == res_1_col[r]: continue
            else: 
                list(input_grid[r])[c] = res_1_col[r]
    print (input_grid)
    return input_grid

def unruly(grid):
    # grid is test_case in tuple format
    grid_ls = tp_2_ls(grid)
    make_up(grid_ls)
    return grid


if __name__ == '__main__':
    def grid2spec(grid):
        """To get the game id."""
        import re
        nb_rows, nb_cols = len(grid), len(grid[0])
        spec, length = [f'{nb_cols}x{nb_rows}:'], nb_rows * nb_cols
        for points, item in re.findall(r'(\.*)(B|W)', ''.join(grid)):
            length -= len(points) + 1
            char = chr(ord('a') + len(points))
            spec.append(char.upper() if item == 'B' else char)
        spec.append(chr(ord('a') + length))
        return ''.join(spec)

    def checker(grid, result):
        try:
            result = list(result)
        except TypeError:
            raise AssertionError('You must return an iterable/list/tuple.')
        assert all(isinstance(row, str) for row in result), \
            'Must return an iterable of strings.'
        nb_rows, nb_cols = len(grid), len(grid[0])
        assert len(result) == nb_rows and \
            all(len(row) == nb_cols for row in result), 'Wrong size.'
        forbidden_chars = ''.join(set.union(*map(set, result)) - set('WB.'))
        assert not forbidden_chars, \
            f'Only the chars "WB." are allowed, not {forbidden_chars!r}.'
        forbidden_changes = sum(c1 != c2 for r1, r2 in zip(grid, result)
                                for c1, c2 in zip(r1, r2) if c1 != '.')
        assert not forbidden_changes, \
            f'You changed {forbidden_changes} cells given at the start.'
        miss = sum(row.count('.') for row in result)
        if miss:
            print('You can look what is missing here:')
            print('https://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/'
                  f'unruly.html#{grid2spec(result)}')
            print('You just need to open a new webpage with that url.')
        assert not miss, f'{miss} cells are still empty.'
        columns = map(''.join, zip(*result))
        for _type, lines in (('row', result), ('column', columns)):
            for n, line in enumerate(lines):
                Ws, Bs = map(line.count, 'WB')
                assert Ws == Bs, f'{Ws} W & {Bs} B in {_type} {n} {line!r}.'
                for item in 'WB':
                    assert item * 3 not in line, \
                        f'{item * 3} found in {_type} {n} {line!r}.'

    TESTS = (
        ('......',
         '..B...',
         'W.B.W.',
         '......',
         'W...W.',
         'WW..W.'),
        ('....WW.B',
         'W..B....',
         '.B...W..',
         'BW....W.',
         '........',
         '.WW.....',
         'W...BB.B',
         'W....B..'),
        ('B..........B',
         '..BB.B.W..B.',
         'B........B..',
         '....BW.W...W',
         '.W........W.',
         '.W...B.....B',
         '..B..BB...W.',
         'BW....B.....'),
    )

    # for test_nb, grid in enumerate(TESTS, 1):
    #     result = unruly(grid)
    #     try:
    #         checker(grid, result)
    #     except AssertionError as error:
    #         print(f'You failed the test #{test_nb}:', error.args[0])
    #         print('Your result:', *result, sep='\n')
    #         break
    # else:
    #     print('Well done! Click on "Check" for bigger tests.')

    a = ('....', 'WW..')
    make_up(a)
    # print (a[0].replace('.', 'W'))
    
    # print (re.findall('.', a[0]))