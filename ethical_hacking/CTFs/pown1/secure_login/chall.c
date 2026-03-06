#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <time.h>

typedef struct user {
    char username[40];
    char password[40];
} user;

void hello(user user){
    printf("\nHello %s\n", user.username);
    fflush(stdout);
}

void show_menu(user user){
    hello(user);
    puts("");
    puts("1. Change username");
    puts("2. Change password");
    puts("3. Get Flag");
    puts("4. Exit");
    printf("> ");
    fflush(stdout);
}

void ins_username(user* user){
    printf("Insert your Username: ");
    fflush(stdout);

    int len = read(0, user->username, 40);
    if(user->username[len-1] == '\n')
        user->username[len-1] = '\0';
    else
        while ((getchar()) != '\n');
}

void ins_password(user* user){
    printf("Insert your Password: ");
    fflush(stdout);

    int len = read(0, user->password, 40);
    if(user->password[len-1] == '\n')
        user->password[len-1] = '\0';
    else
        while ((getchar()) != '\n');
    
    puts("Password uploaded!");
    fflush(stdout);
}

void suus(user* user){
    ins_username(user);
    hello(*user);
}

user u;
int main() {

    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);

    user admin;
    strncpy(admin.username, "admin", 40);
    FILE* f = fopen("passwd.txt", "r");
    fgets(admin.password, 40, f);

    user u;

    puts("Please Login. It's Secure.");
    ins_username(&u);
    ins_password(&u);

    while(1){
        show_menu(u);
        
        int choice;
        char ret;
        scanf("%d%c", &choice, &ret);

        switch(choice) {
            case 0:
                suus(&admin);
                break;
            case 1:
                ins_username(&u);
                break;
            case 2:
                ins_password(&u);
                break;
            case 3:
                if(strncmp(u.username, "admin", 40) == 0 && strncmp(u.password, admin.password, 40) == 0){
                    char flag[41];
                    FILE* f = fopen("flag.txt", "r");
                    fgets(flag, 41, f);
                    printf("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n");
                    printf("\tWelcome back Admin, here is your flag:\n");
                    printf("\t%s\n", flag);
                    printf("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n");
                    fflush(stdout);
                } else {
                    printf("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n");
                    puts("\tYou need to be admin to get the flag!");
                    printf("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n");
                    fflush(stdout);
                }
                break;
            case 4:
                puts("Bye!");
                fflush(stdout);
                return 0;
            default:
                puts("Invalid choice!");
                fflush(stdout);
                break;
        }
    }
}
