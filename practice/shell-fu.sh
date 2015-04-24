#!/bin/bash

# Describe in depth what happens here
list=$(ls)

# My thoughts prior to reviewing strace
# $(ls) is evaluated first

# Search $PATH looking for ls
# When found, fork() and exec()
# The subprocess executes ls with stdin and stderr connected to /dev/null
# stdout is connected to the parent shell
# ls exits
# list environment variable is set to stdout


# The actual strace

# The subshell happens first
# Bash sets up a pipe to communicate with the subshell
8312  pipe([3, 4])                      = 0
# ? Don't block CHLD and INT signals ?
8312  rt_sigprocmask(SIG_BLOCK, [CHLD], [], 8) = 0
8312  rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
8312  rt_sigprocmask(SIG_BLOCK, [INT CHLD], [], 8) = 0
# For some reason a second pipe is created which is very quickly thrown away
8312  pipe([5, 6])                      = 0
# clone() to create a child process, pid 8322
8312  clone(child_stack=0, flags=CLONE_CHILD_CLEARTID|CLONE_CHILD_SETTID|SIGCHLD, child_tidptr=0x7f3df8636a10) = 8322
# Set process group id of 8322 to 8312
8312  setpgid(8322, 8312)               = 0
# Another call to rt_sigprocmask
8312  rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
# I don't understand what is happening here
8312  rt_sigaction(SIGCHLD, {0x446490, [], SA_RESTORER|SA_RESTART, 0x7f3df7c74eb0}, {0x446490, [], SA_RESTORER|SA_RESTART, 0x7f3df7c74eb0}, 8) = 0
# The second pipe is closed
8312  close(5)                          = 0
8312  close(6)                          = 0
# The write end of the first pipe is closed by the parent
8312  close(4)                          = 0
# The parent then starts a read on the read end of the pipe between parent and
# child, though the child end hasn't opened the pipe for writing yet
8312  read(3,  <unfinished ...>)
# More not understood signalling setup
8322  rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
8322  rt_sigaction(SIGTSTP, {SIG_IGN, [], SA_RESTORER, 0x7f3df7c74eb0}, {SIG_IGN, [], SA_RESTORER, 0x7f3df7c74eb0}, 8) = 0
8322  rt_sigaction(SIGTTIN, {SIG_IGN, [], SA_RESTORER, 0x7f3df7c74eb0}, {SIG_IGN, [], SA_RESTORER, 0x7f3df7c74eb0}, 8) = 0
8322  rt_sigaction(SIGTTOU, {SIG_IGN, [], SA_RESTORER, 0x7f3df7c74eb0}, {SIG_IGN, [], SA_RESTORER, 0x7f3df7c74eb0}, 8) = 0
# Set the process group id to the parent
8322  setpgid(8322, 8312)               = 0
# Close the fds for the second pipe
8322  close(5)                          = 0
8322  close(6)                          = 0
# More not understood signalling setup
8322  rt_sigaction(SIGINT, {SIG_DFL, [], SA_RESTORER, 0x7f3df7c74eb0}, {0x45dc10, [], SA_RESTORER, 0x7f3df7c74eb0}, 8) = 0
8322  rt_sigaction(SIGQUIT, {SIG_DFL, [], SA_RESTORER, 0x7f3df7c74eb0}, {SIG_IGN, [], SA_RESTORER, 0x7f3df7c74eb0}, 8) = 0
8322  rt_sigaction(SIGTERM, {SIG_DFL, [], SA_RESTORER, 0x7f3df7c74eb0}, {0x45d760, [], SA_RESTORER|SA_RESTART, 0x7f3df7c74eb0}, 8) = 0
8322  rt_sigaction(SIGCHLD, {SIG_DFL, [], SA_RESTORER|SA_RESTART, 0x7f3df7c74eb0}, {0x446490, [], SA_RESTORER|SA_RESTART, 0x7f3df7c74eb0}, 8) = 0
8322  rt_sigaction(SIGCHLD, {0x446490, [], SA_RESTORER|SA_RESTART, 0x7f3df7c74eb0}, {SIG_DFL, [], SA_RESTORER|SA_RESTART, 0x7f3df7c74eb0}, 8) = 0
8322  rt_sigaction(SIGINT, {0x45dc10, [], SA_RESTORER, 0x7f3df7c74eb0}, {SIG_DFL, [], SA_RESTORER, 0x7f3df7c74eb0}, 8) = 0
# Close fd1 (stdout) and reopen it with the same file handle as fd4, the pipe to
# parent process
8322  dup2(4, 1)                        = 1
# fd4 is no longer necessary, fd3 never was
8322  close(4)                          = 0
8322  close(3)                          = 0
# More not understood signalling setup
8322  rt_sigprocmask(SIG_BLOCK, NULL, [], 8) = 0
# Scan $PATH for ls
8322  stat(".", {st_mode=S_IFDIR|0775, st_size=4096, ...}) = 0
8322  stat("/home/preston/bin/ls", 0x7fff0cbc95d0) = -1 ENOENT (No such file or directory)
8322  stat("/home/preston/bin/ls", 0x7fff0cbc95d0) = -1 ENOENT (No such file or directory)
8322  stat("/usr/local/bin/ls", 0x7fff0cbc95d0) = -1 ENOENT (No such file or directory)
8322  stat("/usr/bin/ls", 0x7fff0cbc95d0) = -1 ENOENT (No such file or directory)
8322  stat("/bin/ls", {st_mode=S_IFREG|0755, st_size=118368, ...}) = 0
8322  stat("/bin/ls", {st_mode=S_IFREG|0755, st_size=118368, ...}) = 0
# Verify we have permissions to execute /bin/ls
8322  geteuid()                         = 1000
8322  getegid()                         = 1000
8322  getuid()                          = 1000
8322  getgid()                          = 1000
8322  access("/bin/ls", X_OK)           = 0
8322  stat("/bin/ls", {st_mode=S_IFREG|0755, st_size=118368, ...}) = 0
8322  geteuid()                         = 1000
8322  getegid()                         = 1000
8322  getuid()                          = 1000
8322  getgid()                          = 1000
8322  access("/bin/ls", R_OK)           = 0
8322  stat("/bin/ls", {st_mode=S_IFREG|0755, st_size=118368, ...}) = 0
8322  stat("/bin/ls", {st_mode=S_IFREG|0755, st_size=118368, ...}) = 0
8322  geteuid()                         = 1000
8322  getegid()                         = 1000
8322  getuid()                          = 1000
8322  getgid()                          = 1000
8322  access("/bin/ls", X_OK)           = 0
8322  stat("/bin/ls", {st_mode=S_IFREG|0755, st_size=118368, ...}) = 0
8322  geteuid()                         = 1000
8322  getegid()                         = 1000
8322  getuid()                          = 1000
8322  getgid()                          = 1000
8322  access("/bin/ls", R_OK)           = 0
# More not understood signalling setup
8322  rt_sigaction(SIGHUP, {SIG_IGN, [], SA_RESTORER, 0x7f3df7c74eb0}, NULL, 8) = 0
8322  rt_sigaction(SIGILL, {SIG_DFL, [], SA_RESTORER, 0x7f3df7c74eb0}, NULL, 8) = 0
8322  rt_sigaction(SIGTRAP, {SIG_DFL, [], SA_RESTORER, 0x7f3df7c74eb0}, NULL, 8) = 0
8322  rt_sigaction(SIGABRT, {SIG_DFL, [], SA_RESTORER, 0x7f3df7c74eb0}, NULL, 8) = 0
8322  rt_sigaction(SIGFPE, {SIG_DFL, [], SA_RESTORER, 0x7f3df7c74eb0}, NULL, 8) = 0
8322  rt_sigaction(SIGBUS, {SIG_DFL, [], SA_RESTORER, 0x7f3df7c74eb0}, NULL, 8) = 0
8322  rt_sigaction(SIGSEGV, {SIG_DFL, [], SA_RESTORER, 0x7f3df7c74eb0}, NULL, 8) = 0
8322  rt_sigaction(SIGSYS, {SIG_DFL, [], SA_RESTORER, 0x7f3df7c74eb0}, NULL, 8) = 0
8322  rt_sigaction(SIGPIPE, {SIG_DFL, [], SA_RESTORER, 0x7f3df7c74eb0}, NULL, 8) = 0
8322  rt_sigaction(SIGALRM, {SIG_DFL, [], SA_RESTORER, 0x7f3df7c74eb0}, NULL, 8) = 0
8322  rt_sigaction(SIGXCPU, {SIG_DFL, [], SA_RESTORER, 0x7f3df7c74eb0}, NULL, 8) = 0
8322  rt_sigaction(SIGXFSZ, {SIG_DFL, [], SA_RESTORER, 0x7f3df7c74eb0}, NULL, 8) = 0
8322  rt_sigaction(SIGVTALRM, {SIG_DFL, [], SA_RESTORER, 0x7f3df7c74eb0}, NULL, 8) = 0
8322  rt_sigaction(SIGUSR1, {SIG_DFL, [], SA_RESTORER, 0x7f3df7c74eb0}, NULL, 8) = 0
8322  rt_sigaction(SIGUSR2, {SIG_DFL, [], SA_RESTORER, 0x7f3df7c74eb0}, NULL, 8) = 0
8322  rt_sigaction(SIGINT, {SIG_DFL, [], SA_RESTORER, 0x7f3df7c74eb0}, {0x45dc10, [], SA_RESTORER, 0x7f3df7c74eb0}, 8) = 0
8322  rt_sigaction(SIGQUIT, {SIG_DFL, [], SA_RESTORER, 0x7f3df7c74eb0}, {SIG_DFL, [], SA_RESTORER, 0x7f3df7c74eb0}, 8) = 0
8322  rt_sigaction(SIGTERM, {SIG_DFL, [], SA_RESTORER, 0x7f3df7c74eb0}, {SIG_DFL, [], SA_RESTORER, 0x7f3df7c74eb0}, 8) = 0
8322  rt_sigaction(SIGCHLD, {SIG_DFL, [], SA_RESTORER|SA_RESTART, 0x7f3df7c74eb0}, {0x446490, [], SA_RESTORER|SA_RESTART, 0x7f3df7c74eb0}, 8) = 0
# exec ls
8322  execve("/bin/ls", ["ls"], [/* 21 vars */]) = 0
# ?
8322  brk(0)                            = 0xdb7000
# Load all dynamic libraries
8322  open("/lib/x86_64-linux-gnu/libpcre.so.3", O_RDONLY|O_CLOEXEC) = 3
8322  read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\0\26\0\0\0\0\0\0"..., 832) = 832
8322  fstat(3, {st_mode=S_IFREG|0644, st_size=444608, ...}) = 0
8322  mmap(NULL, 2540072, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7f1363209000
8322  mprotect(0x7f1363275000, 2093056, PROT_NONE) = 0
8322  mmap(0x7f1363474000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x6b000) = 0x7f1363474000
8322  close(3)                          = 0
# etc
8322  mmap(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f1363e6e000
8322  mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f1363e6c000
8322  arch_prctl(ARCH_SET_FS, 0x7f1363e6c840) = 0
8322  mprotect(0x7f136382f000, 16384, PROT_READ) = 0
8322  mprotect(0x7f1362dfa000, 4096, PROT_READ) = 0
8322  mprotect(0x7f1363003000, 4096, PROT_READ) = 0
8322  mprotect(0x7f1363207000, 4096, PROT_READ) = 0
8322  mprotect(0x7f1363474000, 4096, PROT_READ) = 0
8322  mprotect(0x7f1363a41000, 4096, PROT_READ) = 0
8322  mprotect(0x7f1363c63000, 4096, PROT_READ) = 0
8322  mprotect(0x61b000, 4096, PROT_READ) = 0
8322  mprotect(0x7f1363e89000, 4096, PROT_READ) = 0
8322  munmap(0x7f1363e71000, 89339)     = 0
8322  set_tid_address(0x7f1363e6cb10)   = 8322
8322  set_robust_list(0x7f1363e6cb20, 24) = 0
8322  rt_sigaction(SIGRTMIN, {0x7f1362be8a10, [], SA_RESTORER|SA_SIGINFO, 0x7f1362bf1c90}, NULL, 8) = 0
8322  rt_sigaction(SIGRT_1, {0x7f1362be8aa0, [], SA_RESTORER|SA_RESTART|SA_SIGINFO, 0x7f1362bf1c90}, NULL, 8) = 0
8322  rt_sigprocmask(SIG_UNBLOCK, [RTMIN RT_1], NULL, 8) = 0
8322  getrlimit(RLIMIT_STACK, {rlim_cur=8192*1024, rlim_max=RLIM64_INFINITY}) = 0
8322  statfs("/sys/fs/selinux", 0x7ffffc0bba50) = -1 ENOENT (No such file or directory)
8322  statfs("/selinux", 0x7ffffc0bba50) = -1 ENOENT (No such file or directory)
8322  brk(0)                            = 0xdb7000
8322  brk(0xdd8000)                     = 0xdd8000
8322  open("/proc/filesystems", O_RDONLY) = 3
8322  fstat(3, {st_mode=S_IFREG|0444, st_size=0, ...}) = 0
8322  mmap(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f1363e86000
8322  read(3, "nodev\tsysfs\nnodev\trootfs\nnodev\tb"..., 1024) = 278
8322  read(3, "", 1024)                 = 0
8322  close(3)                          = 0
8322  munmap(0x7f1363e86000, 4096)      = 0
8322  open("/usr/lib/locale/locale-archive", O_RDONLY|O_CLOEXEC) = 3
8322  fstat(3, {st_mode=S_IFREG|0644, st_size=1607664, ...}) = 0
8322  mmap(NULL, 1607664, PROT_READ, MAP_PRIVATE, 3, 0) = 0x7f1363ce3000
8322  close(3)                          = 0
8322  ioctl(1, SNDCTL_TMR_TIMEBASE or SNDRV_TIMER_IOCTL_NEXT_DEVICE or TCGETS, 0x7ffffc0bb6a0) = -1 ENOTTY (Inappropriate ioctl for device)
8322  ioctl(1, TIOCGWINSZ, 0x7ffffc0bb770) = -1 ENOTTY (Inappropriate ioctl for device)
# Open the current directory
8322  openat(AT_FDCWD, ".", O_RDONLY|O_NONBLOCK|O_DIRECTORY|O_CLOEXEC) = 3
# getdents!
8322  getdents(3, /* 4 entries */, 32768) = 112
8322  getdents(3, /* 0 entries */, 32768) = 0
8322  close(3)                          = 0
8322  fstat(1, {st_mode=S_IFIFO|0600, st_size=0, ...}) = 0
8322  mmap(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f1363e86000
# Pass the output back through the pipe to the parent
8322  write(1, "fu.out\nshell-fu.sh\n", 19 <unfinished ...>
8312  <... read resumed> "fu.out\nshell-fu.sh\n", 128) = 19
8312  read(3,  <unfinished ...>
8322  <... write resumed> )             = 19
# Close the pipe on the child side
8322  close(1 <unfinished ...>
8312  <... read resumed> "", 128)       = 0
# Close the pipe on the parent side
8312  close(3)                          = 0
8312  rt_sigprocmask(SIG_BLOCK, [CHLD], [], 8) = 0
# Wait for the child to exit
8312  wait4(-1,  <unfinished ...>
8322  <... close resumed> )             = 0
8322  munmap(0x7f1363e86000, 4096)      = 0
# Child exits
8322  close(2)                          = 0
8322  exit_group(0)                     = ?
8322  +++ exited with 0 +++
8312  <... wait4 resumed> [{WIFEXITED(s) && WEXITSTATUS(s) == 0}], WSTOPPED|WCONTINUED, NULL) = 8322
8312  rt_sigprocmask(SIG_BLOCK, [CHLD TSTP TTIN TTOU], [CHLD], 8) = 0
8312  ioctl(255, SNDRV_TIMER_IOCTL_SELECT or TIOCSPGRP, [8312]) = 0
8312  rt_sigprocmask(SIG_SETMASK, [CHLD], NULL, 8) = 0
8312  rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
8312  --- SIGCHLD {si_signo=SIGCHLD, si_code=CLD_EXITED, si_pid=8322, si_status=0, si_utime=0, si_stime=0} ---
8312  wait4(-1, 0x7fff0cbc93d0, WNOHANG|WSTOPPED|WCONTINUED, NULL) = -1 ECHILD (No child processes)
8312  rt_sigreturn()                    = 0
8312  rt_sigaction(SIGINT, {0x45dc10, [], SA_RESTORER, 0x7f3df7c74eb0}, {0x45dc10, [], SA_RESTORER, 0x7f3df7c74eb0}, 8) = 0
8312  rt_sigprocmask(SIG_BLOCK, [CHLD TSTP TTIN TTOU], [], 8) = 0
8312  ioctl(255, SNDRV_TIMER_IOCTL_SELECT or TIOCSPGRP, [8312]) = 0
8312  rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
8312  rt_sigaction(SIGINT, {0x45dc10, [], SA_RESTORER, 0x7f3df7c74eb0}, {0x45dc10, [], SA_RESTORER, 0x7f3df7c74eb0}, 8) = 0
8312  rt_sigprocmask(SIG_BLOCK, [HUP INT QUIT ALRM TERM TSTP TTIN TTOU], [], 8) = 0
8312  rt_sigaction(SIGINT, {0x4aab80, [], SA_RESTORER, 0x7f3df7c74eb0}, {0x45dc10, [], SA_RESTORER, 0x7f3df7c74eb0}, 8) = 0
8312  rt_sigaction(SIGTERM, {0x4aab80, [], SA_RESTORER, 0x7f3df7c74eb0}, {0x45d760, [], SA_RESTORER|SA_RESTART, 0x7f3df7c74eb0}, 8) = 0
8312  rt_sigaction(SIGHUP, {0x4aab80, [], SA_RESTORER, 0x7f3df7c74eb0}, {0x45dea0, [HUP INT ILL TRAP ABRT BUS FPE USR1 SEGV USR2 PIPE ALRM TERM XCPU XFSZ VTALRM SYS], SA_RESTORER, 0x7f3df7c74eb0}, 8) = 0
8312  rt_sigaction(SIGQUIT, {0x4aab80, [], SA_RESTORER, 0x7f3df7c74eb0}, {SIG_IGN, [], SA_RESTORER, 0x7f3df7c74eb0}, 8) = 0
8312  rt_sigaction(SIGQUIT, {SIG_IGN, [], SA_RESTORER, 0x7f3df7c74eb0}, {0x4aab80, [], SA_RESTORER, 0x7f3df7c74eb0}, 8) = 0
8312  rt_sigaction(SIGALRM, {0x4aab80, [], SA_RESTORER, 0x7f3df7c74eb0}, {0x45dea0, [HUP INT ILL TRAP ABRT BUS FPE USR1 SEGV USR2 PIPE ALRM TERM XCPU XFSZ VTALRM SYS], SA_RESTORER, 0x7f3df7c74eb0}, 8) = 0
8312  rt_sigaction(SIGTSTP, {0x4aab80, [], SA_RESTORER, 0x7f3df7c74eb0}, {SIG_IGN, [], SA_RESTORER, 0x7f3df7c74eb0}, 8) = 0
8312  rt_sigaction(SIGTSTP, {SIG_IGN, [], SA_RESTORER, 0x7f3df7c74eb0}, {0x4aab80, [], SA_RESTORER, 0x7f3df7c74eb0}, 8) = 0
8312  rt_sigaction(SIGTTOU, {0x4aab80, [], SA_RESTORER, 0x7f3df7c74eb0}, {SIG_IGN, [], SA_RESTORER, 0x7f3df7c74eb0}, 8) = 0
8312  rt_sigaction(SIGTTOU, {SIG_IGN, [], SA_RESTORER, 0x7f3df7c74eb0}, {0x4aab80, [], SA_RESTORER, 0x7f3df7c74eb0}, 8) = 0
8312  rt_sigaction(SIGTTIN, {0x4aab80, [], SA_RESTORER, 0x7f3df7c74eb0}, {SIG_IGN, [], SA_RESTORER, 0x7f3df7c74eb0}, 8) = 0
8312  rt_sigaction(SIGTTIN, {SIG_IGN, [], SA_RESTORER, 0x7f3df7c74eb0}, {0x4aab80, [], SA_RESTORER, 0x7f3df7c74eb0}, 8) = 0
8312  rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
8312  rt_sigaction(SIGWINCH, {0x4aa1a0, [], SA_RESTORER|SA_RESTART, 0x7f3df7c74eb0}, {0x45d750, [], SA_RESTORER, 0x7f3df7c74eb0}, 8) = 0
# Write out the prompt
8312  write(2, "(utopic)preston@localhost:~/code"..., 53) = 53
# Wait for input
8312  read(0, "\4", 1)                  = 1
...
# Exit
8312  write(2, "exit\n", 5)             = 5
...
# Write the history file
8312  stat("/home/preston/.bash_eternal_history", {st_mode=S_IFREG|0600, st_size=94913, ...}) = 0
8312  open("/home/preston/.bash_eternal_history", O_WRONLY|O_APPEND) = 3
8312  write(3, "#1429861182\nlist=$(ls)\n", 23) = 23
8312  close(3)                          = 0
...
# Exit
8312  exit_group(0)                     = ?
8312  +++ exited with 0 +++
