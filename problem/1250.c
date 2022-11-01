#define r return
#define D d[i][j]
typedef int t;

t s[502][502], d[502][502], m, n, I[]={0,0,1,-1}, J[]={1,-1,0,0};

t c(t i,t j){
    if(i < 1 || j < 1 || i > m || j > n )r 0;
    if(D==-1){
        D=0;
        for(t k = 0; k < 4; k++)
        if(s[i + I[k]][j + J[k]] > s[i][j])
            D += c(i+I[k],j+J[k]);
    }
    r D;
}

t main(){
    scanf("%d%d",&m,&n);
    for(t i = 1; i <= m; i++)
        for(t j = 1; j <= n; j++){
            scanf("%d", &s[i][j]);
            D=-1;
        }
        d[1][1] = 1;
        printf("%d",c(m,n));
}