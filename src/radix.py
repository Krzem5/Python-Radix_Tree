def init_tree():
	return {"v":b"","l":[],"id":-1,"_nid":0}



def insert(t,v):
	r=t
	i=0
	while (True):
		end=True
		ml=0
		nn=None
		for e in r["l"]:
			cml=0
			for j in range(0,len(e["v"])):
				if (i+j>=len(v) or v[i+j]!=e["v"][j]):
					break
				else:
					cml+=1
			if (cml==len(e["v"])):
				i+=len(e["v"])
				if (i==len(v)):
					e["id"]=t["_nid"]
					t["_nid"]+=1
					return
				r=e
				end=False
				break
			else:
				if (cml>ml):
					ml=cml
					nn=e
		if (end==False):
			continue
		if (ml==0):
			r["l"].append({"v":v[i:],"l":[],"id":t["_nid"]})
			t["_nid"]+=1
		else:
			if (len(nn["l"])==0):
				nn["l"].append({"v":nn["v"][ml:],"l":[],"id":nn["id"]})
				nn["l"].append({"v":v[i+ml:],"l":[],"id":t["_nid"]})
				nn["v"]=nn["v"][:ml]
				nn["id"]=-1
				t["_nid"]+=1
			else:
				tmp={"v":nn["v"][ml:],"l":nn["l"].copy(),"id":nn["id"]}
				nn["l"].clear()
				nn["l"].append(tmp)
				nn["l"].append({"v":v[i+ml:],"l":[],"id":t["_nid"]})
				nn["v"]=nn["v"][:ml]
				nn["id"]=-1
				t["_nid"]+=1
		break



def delete(t,v):
	r=t
	i=0
	l=[t]
	while (True):
		end=True
		for e in r["l"]:
			cml=0
			for j in range(0,len(e["v"])):
				if (i+j>=len(v) or v[i+j]!=e["v"][j]):
					break
				else:
					cml+=1
			if (cml==len(e["v"])):
				i+=len(e["v"])
				l.append(e)
				if (i==len(v)):
					for j in range(len(l)-1,0,-1):
						if (len(l[j]["l"])>0):
							for k in l[j]["l"]:
								if (k["v"]==l[j+1]["v"]):
									l[j]["l"].remove(k)
									break
							if (len(l[j]["l"])==0):
								continue
							if (len(l[j]["l"])==1 and l[j]["id"]==-1):
								e=l[j]["l"][0]
								for m,k in enumerate(l[j-1]["l"]):
									if (k["v"]==l[j]["v"]):
										l[j-1]["l"][m]={"v":l[j]["v"]+e["v"],"l":e["l"],"id":e["id"]}
								break
							l[j]["id"]=-1
							break
					return True
				r=e
				end=False
				break
		if (end==False):
			continue
		return False



def print_tree(t):
	def _print_node(n,i):
		if (len(n["l"])>0):
			print(i+str(n["v"],"utf-8")+":"+("" if n["id"]==-1 else " ("+str(n["id"])+")"))
			i+=" "*len(n["v"])
			for k in n["l"]:
				_print_node(k,i)
		else:
			print(i+str(n["v"],"utf-8")+("" if n["id"]==-1 else " ("+str(n["id"])+")"))
	for k in t["l"]:
		_print_node(k,"")
