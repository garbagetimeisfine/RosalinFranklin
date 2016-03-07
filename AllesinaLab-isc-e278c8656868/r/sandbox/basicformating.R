A <- matrix(c(1,2,3,4),2,2)

A %*% A
B <- solve(A)
B %*% A
diag(A)
C <- matrix(1,3,2)
C
C %*% t(C)
Z <- matrix(1:9, 3, 3)
dim(C)
Z[1,]
Z[,2]
Z[2:3,1:2]
Z[c(1,3),c(1,3)]

M<- array(1:24, c(4,3,2))
dim(M[,1,, drop = FALSE])

taco <- list(Names = c("a","b", "c"), Values = c(1,2,3))

hi <- "d;afjl;dkjfalskdjf jdjjd'dog taco corn ; fasdlkfjalsdkj"
strsplit(hi,';')

sprintf("%s is a total douch bag he kicked that puppy %d times", "Tyler", 32)

substr(hi,26,27)
sub("dog","WHAT THE FUCK IS THAT",hi)

nchar(paste(hi, "what.... oh dear", sep = "XXX&&xxx"))
toupper(hi)
tolower(hi)