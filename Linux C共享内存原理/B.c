#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>

#define SHM_PATH "/tmp/shm"
#define SHM_SIZE 128

int main(int argc, char *argv[])
{
    int shmid;
    char *addr;
    key_t key = ftok(SHM_PATH, 0x6666);
    
    char buf[128];
    
    shmid = shmget(key, SHM_SIZE, IPC_CREAT);
    if (shmid < 0) {
        printf("failed to get share memory\n");
        return -1;
    }
    
    addr = shmat(shmid, NULL, 0);
    if (addr <= 0) {
        printf("failed to map share memory\n");
        return -1;
    }
    
    strcpy(buf, addr, 128);
    printf("%s", buf);
    
    return 0;
}