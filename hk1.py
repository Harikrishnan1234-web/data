1
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


**7. Three Address Code Generator**

```c
#include <stdio.h>
#include <string.h>

int main() {
    char expr[20];
    printf("Enter expression (a=b+c*d): ");
    gets(expr);
    char a = expr[0], b = expr[2], c = expr[4], d = expr[6];
    printf("t1 = %c * %c\n", c, d);
    printf("t2 = %c + t1\n", b);
    printf("%c = t2\n", a);
    return 0;
}
```

---

### **8. Type Checker**

```c
#include <stdio.h>
#include <string.h>

int main() {
    char var1[10], var2[10], type1[10], type2[10];
    printf("Enter variable1 name and type: ");
    scanf("%s%s", var1, type1);
    printf("Enter variable2 name and type: ");
    scanf("%s%s", var2, type2);
    if (strcmp(type1, type2) == 0)
        printf("No type error\n");
    else
        printf("Type Mismatch Error\n");
    return 0;
}
```

---

### **9. Code Optimization Example**

```c
#include <stdio.h>

int main() {
    int a = 2, b = 4;
    int c = a * 2;
    int d = a * 2;  // Common sub-expression

    printf("Before Optimization: %d %d\n", c, d);
    d = c;  // Optimized
    printf("After Optimization: %d %d\n", c, d);
}
```

---

### **10. Intermediate Code → Machine Code**

```c
#include <stdio.h>
#include <string.h>

int main() {
    char op[5], arg1[5], arg2[5], res[5];
    printf("Enter Quadruple (op arg1 arg2 result): ");
    scanf("%s%s%s%s", op, arg1, arg2, res);
    printf("MOV R1,%s\n", arg1);
    printf("%s R1,%s\n", op, arg2);
    printf("MOV %s,R1\n", res);
}
```
