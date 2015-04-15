import os,sys,getopt

record=[]
base_=os.getcwd()
result=[]
stack=[]
base=base_

def add_new(len_,type_):
	for item in result:
		if type_.lower()==item[2]:
			item[0]=item[0]+len_
			item[1]=item[1]+1
			return
	result.append([len_,1,type_.lower()])

def count_line(filename):
	if os.path.isfile(base+'/'+filename):
		fp=open(base+'/'+filename)
		content=fp.readlines()
		temp=filename.split('.')
		record.append([filename,len(content),temp[len(temp)-1]])
		fp.close()
		add_new(len(content),temp[len(temp)-1])
	elif os.path.isdir(base+'/'+filename):
		if filename[0]!='.':
			stack.append(base[len(base_):]+'/'+filename)
		

if __name__=="__main__":
	cur_list=os.listdir(base)
	for item in cur_list:
		count_line(item)
	while len(stack)>0:
		base=base_+'/'+stack.pop(0)
		cur_list=os.listdir(base)
		for item in cur_list:
			count_line(item)
	print "filename      #lines      type"
	for item in record:
		print item[0]+'\t'+str(item[1])+'\t'+item[2]
	print"\n\n"
	print "#lines      #files      type"
	for item in result:
		print str(item[0])+'\t'+str(item[1])+'\t'+item[2]