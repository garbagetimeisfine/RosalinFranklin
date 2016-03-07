ch6 <- read.csv("C:/Users/Patrick/Documents/Python/RosalinFranklin/AllesinaLab-isc-e278c8656868/r/data/H938_Euro_chr6.geno", sep = " ", header = TRUE)
dim(ch6)
head(ch6)
tail(ch6)

sum(ch6$nA2A2) + sum(ch6$nA1A1.) + sum(ch6$nA1A2.)

sum(rowSums(ch6[,5:7]))

homozygouscount <- ch6$nA2A2 == 124 | ch6$nA1A1. == 124
dim(ch6[homozygouscount,])

homozygous99 <- ch6$nA2A2 >= 123 | ch6$nA1A1. >= 123
dim(ch6[homozygous99,])