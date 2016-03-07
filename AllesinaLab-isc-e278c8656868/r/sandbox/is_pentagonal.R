is_pentagonal <- function(x1,x2,x3){
  #checks if a number is tirangular
  y <- x1 + x2 + x3
  n <- (sqrt(24 * y + 1) + 1) / 6
  if (as.integer(n) == n){
    return(TRUE)
  }
  return(FALSE)
}