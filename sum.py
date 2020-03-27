import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-p1', type=str, default = 'output_semeval')
args = parser.parse_args()
files = os.listdir('.')
ans = {}
for f in files:
    if args.p1 in f:
        ans_f = os.listdir(f)
        max_ans = 0
        for mf in ans_f:
            if '.txt' in mf:
                with open(f+'/'+mf, 'r') as F:
                    for line in F:
                        if 'max' in line:
                            cur = eval(line.split(' ')[-1])
                            max_ans = max(cur, max_ans)
        params = '_'.join(f.split('_')[-3:-1])
        if params in ans:
            ans[params].append(max_ans)
        else:
            ans[params] = [max_ans]
res = 0
for key in ans:
    res = max(res, sum(ans[key])/len(ans[key]))
    print(key, sum(ans[key])/len(ans[key]))
    
print("Final RES:")
print(args.p1, res)
                        
