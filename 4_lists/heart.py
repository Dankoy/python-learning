
 
grid = [['.', '.', '.', '.', '.', '.'], ['.', 'O', 'O', '.', '.', '.'], ['O', 'O', 'O', 'O', '.', '.'], ['O', 'O', 'O', 'O', 'O', '.'], ['.', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', '.'], ['O', 'O', 'O', 'O', '.', '.'], ['.', '0', 'O', '.', '.', '.'], ['.', '.', '.', '.', '.', '.']]

i=0
for i in range(len(grid[i])):
    j=0
    for j in range(len(grid)):
        print(grid[j][i], end=' ')
    print('')
