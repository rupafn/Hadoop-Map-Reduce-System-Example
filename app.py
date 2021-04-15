input = 'Hadoop is a big data framework. Hadoop can store vast data. Hadoop processes big data. Hadoop can analyse vast data. Hadoop is easy'
# split the above input into 4
split_doc = input.split('.')
mapper_phase = {}

for i in range(0, len(split_doc)):
    text = split_doc[i].split(' ')
    mapper_phase[i] = {}
    for txt in text:
        if(txt in mapper_phase[i].keys()):
            mapper_phase[i][txt] = mapper_phase[i][txt]+1
        else:
            mapper_phase[i][txt] = 1
# shuffle and sort
sorted = {}
for i in mapper_phase:
    for txt in mapper_phase[i]:
        if txt not in sorted.keys():
            sorted[txt] = []
            
        sorted[txt].append(txt)
# Reduce
for i in sorted:
    sorted[i] = len(sorted[i])
print(sorted)
