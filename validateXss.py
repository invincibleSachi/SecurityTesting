import requests

def main():
    output={}
    print "main function called"
    with open('./xss-checkpayload.txt') as f:
        content =f.readlines();
        for line in content:
            line=line.strip()
            print line
            payload={'attackVector':line}
            r=requests.post('http://localhost:8080/xss',data=payload)
            if(r.status_code==200):
                output[line]=r.content
    print output
    with open('./output.csv', 'w') as outfile:
        outfile.write('url,result\n')
        for key in output:
            if(output[key]=='valid'):
                outfile.write(key+","+output[key]+'\n')
        outfile.close()

if __name__ == '__main__':
    main()