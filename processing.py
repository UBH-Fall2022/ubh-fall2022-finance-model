def max_value(data,y): 
  word=""
  for dict in data:
    for key in dict:
      if key==y:
        if dict[key]>word:
          word=dict[key]
  return word

def init_dictionary(data,y):
  out={}
  v=0
  for dict in data:
    for key in dict:
      if key==y:
        if dict[key]==dict[y]:
          out[dict[key]]=v
  return out

def sum_matches(lod,k,v,tgt):
  out=0
  for dict in lod:
    for key in dict:
      if key==k:
        if dict[key]==v:
          out+=float(dict[tgt])
  return out

def portions(num):
    return [num * 0.5,num * 0.3,num * 0.2]

def annualAmount(an,sav):
    data = []
    for i in range(0,11):
        data.append(((an * 0.2) * i)+sav)
    return data


def copy_matching(lod,k,v):
  out=[]
  for dict in lod:
    for key in dict:
      if key==k:
        if dict[key]==v:
          out.append(dict)
  return out