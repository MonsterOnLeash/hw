from math import sqrt, radians, cos, sin
dim = input("Choose dimension(2D or 3D):")
vec = list(map(float, input('Give vector coordinates:').split()))
working = True
while working:
    task = input("What to do?:")
    if task == 'help':
        print('help - available tasks')
        print('length - calculate length')
        print('scale - scale by constant')
        print('rotate- rotate by given angle')
        print('exit - exit programme')
        print()
    if task == 'length':
        ans = 0
        for i in vec:
            ans += i**2
        ans = sqrt(ans)
        print(ans)
        print()
    if task == 'scale':
        const = float(input('Choose the constant to multiply by: '))
        for i in range(len(vec)):
            vec[i] *= const
            print(vec[i], end = ' ')
        print()
    if task == 'rotate':
        deg = radians(float(input('angle:')))
        if dim == '2D':
            x1 = vec[0] * cos(deg) - vec[1] * sin(deg)
            y1 = vec[0] * sin(deg) + vec[1] * cos(deg)
            vec[0] = x1
            vec[1] = y1
        if dim == '3D':
            axis = input('choose axis to rotate around: ')
            if axis == 'x':
                vec[1] = vec[1] * cos(deg) - vec[2] * sin(deg)
                vec[2] = vec[1] * sin(deg) + vec[2] * cos(deg)
            elif axis == 'y':
                vec[0] = vec[0] + cos(deg) + vec[2] * sin(deg)
                vec[2] = vec[2] * cos(deg) - vec[0] * sin(deg)
            elif axis == 'z':
                vec[0] = vec[0] * cos(deg) - vec[1] * sin(deg)
                vec[1] = vec[0] * sin(deg) + vec[1] * cos(deg)
        print('resulting vector is:', *vec)
    if task == 'exit':
        working = False
