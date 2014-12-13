import urllib

def parse_w2ui_request_form(rform):
  data   = {}
  to_fix = {}
  for k in rform:
    k = urllib.unquote_plus(k)
    v = urllib.unquote_plus(rform[k])
    while True: 
      i = k.find('[]')
      if i == -1: break
      kk = k[:i]
      to_fix.setdefault(kk,0)
      k = '%s[%d]%s' % (kk,to_fix[kk],k[(i+2):])
      to_fix[kk] += 1 
    k = k.replace(']','').split('[')
    if len(k) == 1:
      data[k[0]] = v
    else:
      data.setdefault(k[0],{})
      d = data[k[0]]
      for kk in k[1:-1]:
        d.setdefault(kk,{})
        d = d[kk]
      d[k[-1]] = v
  def d2l(struct):
    if type(struct) == dict:
      for k,v in struct.iteritems():
        if type(v) == dict:
          keys = set(v.keys())
          rng  = range(len(keys))
          if keys == set(map(str,rng)):
            struct[k] = [ d2l(v[str(i)]) for i in rng ]
    return struct
  data = d2l(data) 
  return data

