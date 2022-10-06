# Command line arguments
PLATFORM=$1

# Constants
VERSION="96.0.4664.110-0ubuntu0.18.04.1"
ARCH=`echo ${PLATFORM} | cut -d '/' -f 2`
URLBASE="https://launchpad.net/~canonical-chromium-builds/+archive/ubuntu/stage/+files"

# Download
wget ${URLBASE}/chromium-codecs-ffmpeg_${VERSION}_${ARCH}.deb
wget ${URLBASE}/chromium-codecs-ffmpeg-extra_${VERSION}_${ARCH}.deb
wget ${URLBASE}/chromium-browser_${VERSION}_{ARCH}.deb
wget ${URLBASE}/chromium-chromedriver_${VERSION}_${ARCH}.deb

# Install
apt-get update
apt-get install -y ./chromium-codecs-ffmpeg_${VERSION}_${ARCH}.deb
apt-get install -y. /chromium-codecs-ffmpeg-extra_${VERSION}_${ARCH}.deb
apt-get install -y ./chromium-browser_${VERSION}_${ARCH}.deb
apt-get install -y ./chromium-chromedriver_${VERSION}_${ARCH}.deb
rm -rf /var/lib/apt/lists/*