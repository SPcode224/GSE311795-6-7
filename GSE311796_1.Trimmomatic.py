#-*- coding:utf-8 -*-
### Trimmomatic
#### Loading Modules

import sys, subprocess, time


#### Tool Addres

dict = {}
dict['trimmomatic'] = "/mnt/gmi-l1/_90.User_Data/hsp224/Program/Trimmomatic-0.39/trimmomatic-0.39.jar"
dict['adapter'] = "/mnt/gmi-l1/_90.User_Data/hsp224/Program/Trimmomatic-0.39/adapters/TruSeq3-PE-2.fa"
dict['java'] = "/usr/bin/java"

#### Option

dict['thread'] = 2


#### Input Address Setting


dict['script'] = sys.argv[0]
dict['input_folder'] = sys.argv[1]
dict['output_folder'] = sys.argv[2]
dict['sample'] = sys.argv[3]


#### Session Information

print("=" * 50)
print("Start time :", time.ctime())
print("Sever :", subprocess.check_output("uname -a", shell=True, universal_newlines=True).split()[1])
print("Java :",subprocess.check_output("java -version | sed -n 1p", shell = True, universal_newlines=True))
print("Python :",subprocess.check_output("python --version | sed -n 1p", shell = True, universal_newlines=True))
print("R :",subprocess.check_output("R --version | sed -n 1p", shell = True, universal_newlines=True))
print("Perl :", subprocess.check_output("perl -version | sed -n 2p", shell = True, universal_newlines=True))
print("Run script : nohup python -u {script} {input_folder} {output_folder} &> {sample}.trim.log &". format(**dict))
print("Thread option : {thread}". format(**dict))
print("=" * 50)


#### Trimmomatic

dict['start_time']      = time.time()
subprocess.check_call("{java} -jar {trimmomatic} PE -threads {thread} \
                      {input_folder}/{sample}_1.fastq.gz {input_folder}/{sample}_2.fastq.gz \
                      {output_folder}/{sample}_1P.fastq.gz {output_folder}/{sample}_1U.fastq.gz \
                      {output_folder}/{sample}_2P.fastq.gz {output_folder}/{sample}_2U.fastq.gz \
                      ILLUMINACLIP:{adapter}:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36 \
                      && touch {sample}.trim.success || touch {sample}.trim.fail". format(**dict), shell = True)
dict['end_time']        = time.time() - dict['start_time']
print("=" * 50)
print("Running {sample} Trimmomatic time : {end_time} second". format(**dict))
print("=" * 50)

'''
#### Trimmomatic
##### Public : DART-seq
dict['start_time']      = time.time()
subprocess.check_call("{java} -jar {trimmomatic} SE -threads {thread} \
					  {input_folder}/{sample}.fastq \
					  {output_folder}/{sample}.trim.fastq.gz \
					  ILLUMINACLIP:{adapter}:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36 \
					  && touch {sample}.trim.success || touch {sample}.trim.fail". format(**dict), shell = True)
dict['end_time']        = time.time() - dict['start_time']
print("=" * 50)
print("Running {sample} Trimmomatic time : {end_time} second". format(**dict))
print("=" * 50)
'''
