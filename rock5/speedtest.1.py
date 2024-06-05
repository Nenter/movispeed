import speedtest

st = speedtest.Speedtest()

print("Download: %s Mbps" % (st.download() / 1024 / 1024))
print("Upload: %s Mbps" % (st.upload() / 1024 / 1024))