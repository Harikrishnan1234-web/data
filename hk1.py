#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    char s[100], *t;
    printf("Enter expression: ");
    fgets(s, 100, stdin);
    s[strcspn(s, "\n")] = 0;

    for (t = strtok(s, " +-*/=(),;"); t; t = strtok(NULL, " +-*/=(),;")) {
        int dot = 0, i;
        if (isalpha(t[0]) || t[0] == '_')
            for (i = 1; t[i]; i++)
                if (!isalnum(t[i]) && t[i] != '_') break;
        if ((isalpha(t[0]) || t[0] == '_') && !t[i])
            printf("%s → Identifier\n", t);
        else {
            for (i = 0; t[i]; i++) if (t[i] == '.') dot++;
            if (dot == 1) printf("%s → Real Constant\n", t);
            else printf("%s → Integer Constant\n", t);
        }
    }
}