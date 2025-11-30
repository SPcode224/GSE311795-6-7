#-*- coding:utf-8 -*-
### Trimming a Fastq file
#### Loading Modules

import sys, os, subprocess, time, gzip


### Input Address Setting

dict = {}
dict['script']          = sys.argv[0]
dict['input_folder']    = sys.argv[1]
dict['output_folder']   = sys.argv[2]
dict['sample']          = sys.argv[3]


#### Session Information

print("=" * 50)
print("Start time :", time.ctime())
print("Sever :", subprocess.check_output("uname -a", shell=True, universal_newlines=True).split()[1])
print("Java :",subprocess.check_output("java -version | sed -n 1p", shell = True, universal_newlines=True))
print("Python :",subprocess.check_output("python --version | sed -n 1p", shell = True, universal_newlines=True))
print("R :",subprocess.check_output("R --version | sed -n 1p", shell = True, universal_newlines=True))
print("Perl :", subprocess.check_output("perl -version | sed -n 2p", shell = True, universal_newlines=True))
print("Run script : nohup python -u {script} {input_folder} {output_folder} {sample} &> {sample}.trimfastq.log &". format(**dict))
#print("Thread option : {thread}". format(**dict))
print("=" * 50)


#### Input Fastq files

forward = gzip.open("{input_folder}/{sample}_1.fastq.gz". format(**dict), 'rb')
reverse = gzip.open("{input_folder}/{sample}_2.fastq.gz". format(**dict), 'rb')
output_1 = gzip.open("{output_folder}/trim.{sample}_1.fastq.gz". format(**dict), 'wb')
output_2 = gzip.open("{output_folder}/trim.{sample}_2.fastq.gz". format(**dict), 'wb')


#### Trimming

print("{sample} sample trimming start". format(**dict))
dict['start_time']      = time.time()

for i, line in enumerate(forward):
	dict['fw'] = line.rstrip().decode()
	dict['rev'] = reverse.readline().rstrip().decode()
	if i % 4 == 1:
		dict['fw2'] = dict['fw'][0:50]
		dict['rev2'] = dict['rev'][0:50]
		output_1.write("{fw2}\n". format(**dict). encode())
		output_2.write("{rev2}\n". format(**dict). encode())
	elif i % 4 == 3:
		dict['fw2'] = dict['fw'][0:50]
		dict['rev2'] = dict['rev'][0:50]
		output_1.write("{fw2}\n". format(**dict). encode())
		output_2.write("{rev2}\n". format(**dict). encode())
	else:
		output_1.write("{fw}\n". format(**dict). encode())
		output_2.write("{rev}\n". format(**dict). encode())

dict['end_time']        = time.time() - dict['start_time']
print('{sample} sample trimming end'. format(**dict))
print('{sample} sample trimming end time : {end_time}'. format(**dict))
print("=" * 50)

#### Close File

forward.close()
reverse.close()
output_1.close()
output_2.close()
