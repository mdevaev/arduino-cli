all :
	true

install :
	mkdir -p $(DESTDIR)/usr/share/arduino
	mkdir -p $(DESTDIR)/usr/bin
	cp -a arduino/* $(DESTDIR)/usr/share/arduino
	cp -a tools/Makefile.sketch $(DESTDIR)/usr/share/arduino
	install -m 755 tools/serial_chat.py $(DESTDIR)/usr/bin

