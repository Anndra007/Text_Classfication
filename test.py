dataset = 'THUCNews'
results = [x.strip() for x in open(
            dataset + '/data/class.txt').readlines('utf-8')]
print(results)