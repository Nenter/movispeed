import speedtest
import subprocess

st = speedtest.Speedtest()

subprocess.call("scriptInicio.sh")
print("Download: %s Mbps" % (st.download() / 1024 / 1024))

print("Upload: %s Mbps" % (st.upload() / 1024 / 1024))
subprocess.call("scriptFin.sh")
