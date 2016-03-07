data(trees)
# summary(trees)
# big75 <- trees$Height >= 75
# Vol1535 <- trees$Volume >=15 & trees$Volume <= 35
# Vol1535
# summary(trees[Vol1535,])
# boxplot(trees)

collen <- dim(trees)[1]
newCol <- c(round(runif(collen,1,2)))
trees <- cbind(trees, newCol)
howmany <- 0

for (i in 0:100){
  trees$newCol <- c(round(runif(collen,1,2)))
  experiment1 <- trees$newCol == 1
  experiment2 <- trees$newCol == 2
  tester <- t.test(trees[experiment1,]$Volume, trees[experiment2,]$Volume)
  #print(tester)
  if (tester$p.value <= 0.05){
    howmany <- howmany + 1
  }
}

print(paste(howmany, "out of 100 t tests came up 'Significant"))