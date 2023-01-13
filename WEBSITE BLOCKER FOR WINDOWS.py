#import pandas as pd

print("------------------ WEBSITE BLOCKER FOR WINDOWS ------------------")
print("by: Pablo Cortinhas\n")

dns = input("Inform the DNS you want to add. If you don't know which one to use,"
            "recommend this one (208.67.222.123): ")
sites = [ ]
for i in range(0,10):
    x = input("Write the website you want to block or type (0) to exit: ")
    if x == "0":
        break
    else:
        sites.append(x)

print('\n\n------------------ COPY ------------------')   

while True:
    try:
        print(dns,sites[0])
        print(dns,sites[1])
        print(dns,sites[3])
        print(dns,sites[4])
        print(dns,sites[5])
        print(dns,sites[6])
        print(dns,sites[7])
        print(dns,sites[8])
        print(dns,sites[9])
    except IndexError:
        break

print("\n\n1- Open notepad as administrator 2- Open the folder: "
"(C: » Windows » System32 » Drivers » etc) "
"3- Choose all files and open (hosts)."
"\nIn the last line, add dns and sites obtained here. "
"Then just save and restart your browser.\n")