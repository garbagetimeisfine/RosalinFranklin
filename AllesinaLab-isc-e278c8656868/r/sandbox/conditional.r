z <- readline(prompt = "Enter a number: ")
z <- as.numeric(z)

if (z %% 2 == 0) {
  print(paste(z, "is even"))
} else {
  print(paste(z, "is odd"))
}

if (z >= 100) {
  print( z ^ 3)
}

if (z %% 17 == 0) {
  print(sqrt(z))
}

if (z < 10) { 
  print(c(1:z))
}