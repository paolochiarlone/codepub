BINARY := testreboot
CFLAGS += -Wall -O0

.PHONY: all
all: $(BINARY)

$(BINARY): testreboot.o

.PHONY: clean
clean:
	-rm -f *.o $(BINARY)
