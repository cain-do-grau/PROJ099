var_name = input()
var_counter = -1
var_yes = True
var_destiny = -1
print('\n'*100)
for U in range(0,len(var_name)):
    var_destiny = var_destiny + 1
    var_yes = True
    var_counter = -1
    for i in range(0,len(var_name)):
        var_counter = var_counter + 1
        if var_counter == var_destiny:
            if var_yes == True:
                print(var_name[var_counter], end='')
                var_yes = False
        else:
            print('*', end='')
    print()