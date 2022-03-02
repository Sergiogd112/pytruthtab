from eq import *
def main():
    maxn=2**len(inputs)-1
    print(' '*(len(str(maxn))+1)+'|'+in_names.replace(',','|')+'||'+out_names.replace(',','|'))
    for i in range(maxn+1):
        n=i
        for j in range(len(inputs)):
            inputs[j] = n%2
            n=n//2
        
        print((str(i)+' ').rjust(len(str(maxn))+1,' ')+'|'+'|'.join([str(x).center(len(name),' ') for name,x in zip(in_names.split(','),inputs[::-1])])+'||'+'|'.join([str(x).center(len(name),' ') for name,x in zip(out_names.split(','),eq(inputs[::-1]))]))
if __name__ == '__main__':
    main() 