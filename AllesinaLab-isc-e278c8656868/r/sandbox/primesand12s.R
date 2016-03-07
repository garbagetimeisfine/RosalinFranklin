z <- seq(1, 1000, 3)
for (k in z) {
  if (k %% 4 == 0) {
    print(k)
  }
}

X <- readline(prompt = "Enter a number:")
X <- as.numeric(X)

isthisspecial <- TRUE
i <- 2
while (i < X){
  if (X %% i == 0) {
    isthisspecial <- FALSE
    break
  }
  i <- i + 1
}

if (isthisspecial == T){
  print(X)
}