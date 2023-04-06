#include <unistd.h>
#include <linux/reboot.h>
#include <sys/reboot.h>

int main()
{
    // to avoid losing data
    sync();
    reboot(LINUX_REBOOT_CMD_POWER_OFF);
    //reboot(LINUX_REBOOT_CMD_RESTART);
}
