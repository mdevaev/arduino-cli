# Contributor: Devaev Maxim <mdevaev@gmail.com>
# Author: Devaev Maxim <mdevaev@gmail.com>


pkgname="arduino-cli"
pkgver="1.6.5-r3"
pkgrel="1"
pkgdesc="CLI development tools for Arduino without Java and Arduino IDE"
arch=("any")
url="https://github.com/mdevaev/arduino-cli"
license="GPL"
depends=(
	"avr-libc"
	"avr-gcc"
	"avr-binutils"
	"avrdude"
	"make"
)
makedepends=("wget")
conflicts=("arduino")
replaces=("arduino")
options=("!strip")


package() {
	cd $startdir/src
	if [ ! -d $pkgname-$pkgver ]; then
		msg "Downloading tag v$pkgver..."
		wget $url/archive/v$pkgver.tar.gz
		tar -xzf v$pkgver.tar.gz
	fi

	rm -rf $pkgname-build
	cp -r $pkgname-$pkgver $pkgname-build
	cd $pkgname-build

	mkdir -p $pkgdir/usr/share/arduino
	mkdir -p $pkgdir/usr/bin
	cp -a arduino/* $pkgdir/usr/share/arduino
	cp -a Makefile.sketch $pkgdir/usr/share/arduino
}
