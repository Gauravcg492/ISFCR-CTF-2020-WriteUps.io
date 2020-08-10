zero_width_space="\u200b"
#you can't see it, but it's there
def encode_file(filename, message):
    f_in=open(filename, "r")
    f_out=open("_encoded.".join(filename.split(sep=".")), mode="w", encoding="utf-8")

    s_in="".join(f_in.readlines())
    s_out=""
    for i in message:
        s_out=s_out+s_in[0]+(ord(i)*zero_width_space)
        s_in=s_in[1:]
    print(s_out+s_in, end="", file=f_out)
    f_in.close()
    f_out.close()

    return "_encoded.".join(filename.split(sep="."))

def decode(filename):
    f_in=open(filename, "r", encoding="utf-8")
    f_out=open("_decoded.".join(filename.split(sep=".")), mode="w")

    i=1
    s_in="".join(f_in.readlines())
    l=[0]
    while i<len(s_in):
        if s_in[i]!=zero_width_space:
            if l[-1]==i-1:
                break
            l+=[i]
        i+=1
    print("".join([chr(l[i]-l[i-1]-1) for i in range(1,len(l))]), file=f_out)
    
    f_in.close()
    f_out.close()

    return "_decoded.".join(filename.split(sep="."))
