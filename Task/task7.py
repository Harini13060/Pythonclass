my_dict={"apple":3,"banana":1,"orange":2}
sorted_dict={k:v for k,v in sorted(my_dict.items(),key=lambda item:item[1])}
print(sorted_dict)