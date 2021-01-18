import numpy as np

def main ():
    students = [
        'Drak Twining',
        'Drak Twining',
        'Drak Twining',
        'Drak Twining',
        'Drak Twining',
        'Drak Twining',
        'Drak Twining',
        'Drak Twining',
        'Drak Twining',
        'Dylan Terrell',
        'dmskd sdkmkd',
        'sjd skd kskd']

    rng = np.random.default_rng()
    count = 0 
    for student in students:
        print(student)
        count = count + 1
        if count % 4 == 0:
            print('')

# end of main()
if __name__ == "__main__":
    main()
