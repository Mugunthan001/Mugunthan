#include <stdio.h>
int main(void)
{
int m,n,i,c;
scanf("%d %d",&m,&n);
if(m>=1 && n<10)
c=1;
else if(n>=10 && n<=99)
c=2;
else
c=3;
switch(c)
{
case 1:
if(m>=1 && n<10)
{
for(i=m;i<=n;i++)
{
printf("%d",i);
if(i==n)
continue;
else
printf(" ");
}
}
break;
case 2:
if(m>=1 && n<100)
{
for(i=m;i<=n;i++)
{
if(i==n)
printf("%d",i);
else if(i>=10)
printf("%d ",i);
else
printf("0%d ",i);
}
}
break;
case 3:
if(m>=1 && n<1000)
{
for(i=m;i<=n;i++)
{
if(i==n)
printf("%d",i);
else if(i>=100 && i<n)
printf("%d ",i);
else if(i>=10 && i<100)
printf("0%d ",i);
else
printf("00%d ",i);
}
}
break;
}
return 0;
}
