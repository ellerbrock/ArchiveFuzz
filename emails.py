from collections import Counter
import re
import os

# status : completed 
# todo   : nothing

# function for finding the emails from web-archive
def email_enumerator(url , domain , r):
    first_sub = ' \u001b[32m|\u001b[0m'
    second_sub = '\u001b[32m|--\u001b[0m'
    print("\n\u001b[32m  [~] Email enumeration started\u001b[0m")
    print(" \u001b[32m  |")
    
    # I was/am actually dumb , I didn't think of image names like "name@2x.jpg" , this will also be considered as an email as per my regex
    # so I blacklisted some extensions , and removed them from the raw_data , so if you get any falsepositives , add them to the below re.sub funtion
    # below line is for removing false positives 
    
    r = re.sub('(-p-|mp4|webm|JPG|pdf|html|jpg|jpeg|png|gif|bmp|svg|1x|2x|3x|4x|5x|6x|7x|9x|10x|11x|12x|13x|14x|15x)' , '' , r) 
    any_email_pattern    = "([a-zA-Z0-9+._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]{2,7})" # pattern for matching  email 
    any_emails     = re.findall(any_email_pattern , r) # list of all the emails 
    cnt = Counter(any_emails) # removing duplicate emails
    print("   "+second_sub+"[+] Total unique emails found        : " + str(len(cnt))) # printing no of unique subdomains

    filename = domain+"-output/"+domain+"-emails.txt" #defining the filename
    if len(cnt)>0: # if no of emails are not zero
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc: # a check to protect againsts the Racecondition issues
                if exc.errno != errno.EEXIST:
                    raise
        # if the file already exists , empty the file, this happens when you run the scan against same target multiple times
        with open(filename, 'w') as empty:
            empty.write('')

        # writing the subdomains in file
        
        for i in cnt.keys():
            with open(filename, "a") as f:
                f.write(i+"\n") # writing all the emails in a file 
        print("   "+second_sub+"[+] Emails saved in                  : {} ".format(filename))

    print("   "+second_sub+"[+] Email scan finished ")
