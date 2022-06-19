test_file = open('test_file.txt', 'r')
string_count = test_file.readlines()
print(f'Lines count: {len(string_count)}')
for i in range(len(string_count)):
    print(f'Line {i+1} has {len(string_count(i).split())} words')
test_file.close()
