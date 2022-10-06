# Command line arguments
PLATFORM=$1

# Constants
VERSION="85.0.4183.83-0ubuntu0.20.04.2"
ARCH=`echo ${PLATFORM} | cut -d '/' -f 2`
ARCH=amr64
URLBASE="http://archive.ubuntu.com/ubuntu/pool/universe/c/chromium-browser"

# Download
#wget ${URLBASE}/chromium-codecs-ffmpeg_${VERSION}_${ARCH}.deb
#wget ${URLBASE}/chromium-codecs-ffmpeg-extra_${VERSION}_${ARCH}.deb
#wget ${URLBASE}/chromium-browser_${VERSION}_{ARCH}.deb
#wget ${URLBASE}/chromium-chromedriver_${VERSION}_${ARCH}.deb

# Install
dpkg -i /taixTracking/resources/temp/docker/chromium-codecs-ffmpeg_${ARCH}.deb
dpkg -i /taixTracking/resources/temp/docker/chromium-codecs-ffmpeg-extra_${ARCH}.deb
dpkg -i /taixTracking/resources/temp/docker/chromium-browser_${ARCH}.deb
dpkg -i /taixTracking/resources/temp/docker/chromium-chromedriver_${ARCH}.deb
rm -rf /var/lib/apt/lists/*