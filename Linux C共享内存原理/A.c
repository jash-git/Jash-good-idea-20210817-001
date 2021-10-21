#include <stdio.h>
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
    
    shmid = shmget(key, SHM_SIZE, IPC_CREAT|IPC_EXCL|0666);
    if (shmid < 0) {
        printf("failed to create share memory\n");
        return -1;
    }
    
    addr = shmat(shmid, NULL, 0);
    if (addr <= 0) {
        printf("failed to map share memory\n");
        return -1;
    }
    
    sprintf(addr, "%s", "Hello World\n");
    
    return 0;
}