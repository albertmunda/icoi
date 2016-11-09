CC          =   gcc 
CFLAGS      =   -pedantic -Wall
LDFLAGS     =   -lm

TARGET      =   $(filename)

all: $(TARGET)
    $(TARGET) : $(TARGET).c : $(CC) $(CFLAGS) -o $(TARGET) $(TARGET).c : $(LDFLAGS)

