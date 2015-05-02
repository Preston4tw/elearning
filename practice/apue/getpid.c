#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main(void) {
  printf("hello world from process id %d\n", getpid());
  exit(0);
}
