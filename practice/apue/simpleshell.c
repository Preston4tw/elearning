#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>

#define MAXLINE 4096

int main(void) {
  char buf[MAXLINE];
  pid_t pid;
  int status;

  printf("%% ");
  while (fgets(buf, MAXLINE, stdin) != NULL) {
    if (buf[strlen(buf) - 1] == '\n')
      buf[strlen(buf) - 1] = 0;

    if ((pid = fork()) < 0) {
      printf("fork error\n");
      exit(1);
    } else if (pid == 0) { // child
      execlp(buf, buf, (char *)0);
      printf("couldn't execute: %s", buf);
      exit(127);
    }
    // parent
    if ((pid = waitpid(pid, &status, 0)) < 0) {
      printf("waitpid error");
    }
    printf("%% ");
  }
  exit(0);
}
