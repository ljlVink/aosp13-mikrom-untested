import requests,sys,os
#header_app="http://aospxref.com/android-13.0.0_r3/raw/"
header_app="http://aospxref.com/android-13.0.0_r3/raw/"
Filepath=sys.argv[1]
x=Filepath.split('\\')
file=x[len(x)-1]
print(file)
if not os.path.exists(Filepath[:-len(file)-1]):
    print(
        Filepath[:-len(file)-1]
    )
    os.makedirs(Filepath[:-len(file)-1])
url=header_app+Filepath
req=requests.get(url.replace('\\','/'))
open(Filepath,'wb').write(req.content)