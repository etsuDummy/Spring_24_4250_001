CC = gcc
CX = g++
CFLAGS = -I. -Wall
LFLAGS=

OBJS = CSCI-4250-cpr2.o
PRGS = CSCI-4250-cpr2


all: $(PRGS)

CSCI-4250-cpr2: $(OBJS)
	$(CX) -o $@ $^ $(CFLAGS) $(LFLAGS)
	strip $@

$(OBJS): %.o : %.cpp amh14.h
	$(CX) $(CFLAGS) -c $< -o $@

.PHONY: clean
clean:
	-rm -f $(OBJS) $(PRGS)