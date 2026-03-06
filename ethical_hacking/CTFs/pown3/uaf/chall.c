#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define PWD_LEN 0x20

void random_pass(char *pass, size_t len) {
    FILE *f = fopen("/dev/urandom", "r");
    if(f == NULL) {
        perror("fopen");
        exit(1);
    }
    fread(pass, 1, len, f);
    fclose(f);

    for(size_t i = 0; i < len; i++) {
        pass[i] = ((unsigned char)(pass[i]) % ('z' - 'a')) + 'a';
    }

    pass[len] = '\0';
}

void print_flag() {
    char flag[0x100];
    FILE *f = fopen("flag.txt", "r");
    if(f == NULL) {
        printf("Flag file not found. Contact an admin.\n");
        exit(1);
    }
    fgets(flag, 0x100, f);
    printf("%s\n", flag);
}

int main() {

    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    setbuf(stderr, NULL);

    char *admin_password = NULL;
    char *user_password = NULL;
    char buffer[PWD_LEN + 1];

    while(1) {
        printf("1. Create admin account\n");
        printf("2. Login as admin\n");
        printf("3. Delete admin account\n");
        printf("4. Create user account\n");
        printf("5. Login as user\n");
        printf("6. Delete user account\n");
        printf("7. Exit\n");

        int choice;
        printf("> ");
        scanf("%d", &choice);

        switch(choice) {
            case 1:
                admin_password = (char *)malloc(PWD_LEN + 1);
                random_pass(admin_password, PWD_LEN + 1);
                printf("Admin acount created successfully\n");
                printf("The password is safely stored at %p\n", admin_password);
                break;
            case 2:
                if(admin_password == NULL) {
                    printf("Admin account does not exist\n");
                    break;
                }
                printf("Password: ");
                scanf("%33s", buffer);
                if(strncmp(admin_password, buffer, PWD_LEN) == 0) {
                    printf("Logged in as admin, here is your flag:\n");
                    print_flag();
                } else {
                    printf("Invalid password\n");
                }
                break;
            case 3:
                free(admin_password);
                printf("Memory at %p has been freed\n", admin_password);
                break;
            case 4:
                user_password = (char *)malloc(PWD_LEN + 1);
                random_pass(user_password, PWD_LEN + 1);
                printf("User acount created successfully, password: %s\n", user_password);
                printf("The password is safely stored at %p\n", user_password);
                break;
            case 5:
                if(user_password == NULL) {
                    printf("User account does not exist\n");
                    break;
                }
                printf("Password: ");
                scanf("%33s", buffer);
                if(strncmp(user_password, buffer, PWD_LEN) == 0) {
                    printf("Logged in as user, no flag for you :/\n");
                } else {
                    printf("Invalid password\n");
                }
                break;
            case 6:
                free(user_password);
                printf("Memory at %p has been freed\n", user_password);
                break;
            case 7:
                return 0;
        }
    }
    
    return 0;
}