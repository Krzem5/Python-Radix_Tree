import radix



t=radix.init_tree()
for e in [b"romane",b"romanus",b"romulus",b"rubens",b"ruber",b"rubicon",b"rubicundus"]:
	radix.insert(t,e)
radix.print_tree(t)
print(radix.delete(t,b"rubens"))
print(radix.delete(t,b"invalid_key"))
radix.print_tree(t)
