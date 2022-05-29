import qbittorrentapi as qb
import time
import math


qbt_client = qb.Client(
    host="",
    port=,
    username="",
    password="")


try:
    qbt_client.auth_log_in()
except qb.LoginFailed as e:
    print(e)
    

# https://stackoverflow.com/a/14822210
def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])
        


# Console starts here
print("\nqBittorrent Stats\n")

print(f"Connection Status: {qbt_client.transfer_info()['connection_status'].capitalize()}")
print(f"Session Upload: {convert_size(size_bytes=qbt_client.transfer_info()['up_info_data'])}")
print(f"Session Download: {convert_size(size_bytes=qbt_client.transfer_info()['dl_info_data'])}")


if qbt_client.transfer_info()['up_rate_limit'] == 0:
    print("UP Rate limit: None")
else:
    print(f"UP Rate limit: {convert_size(size_bytes=qbt_client.transfer_info()['up_rate_limit'])}/s")


if qbt_client.transfer_info()['dl_rate_limit'] == 0:
    print("DL Rate limit: None\n")
else:
    print(f"DL Rate limit: {convert_size(size_bytes=qbt_client.transfer_info()['dl_rate_limit'])}/s\n")
    

while True:
    if qbt_client.transfer_info()['connection_status'] == "disconnected":
        print("qBittorrent is disconnected.")
        break
    else:
        up = qbt_client.transfer_info()["up_info_speed"]
        dl = qbt_client.transfer_info()["dl_info_speed"]
        
        up = convert_size(size_bytes=up)
        dl = convert_size(size_bytes=dl)
        
        upstr = f"Upload: {up}/s"
        dlstr = f"Download: {dl}/s"
        
        print(upstr.ljust(20, " ") + " |  " + dlstr)
        
        time.sleep(1.5)