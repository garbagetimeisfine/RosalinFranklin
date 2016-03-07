is_triangular <- function(y){
  #checks if a number is tirangular
  n <- (sqrt(8 * y + 1) - 1) / 2
  if (as.integer(n) == n){
    return(TRUE)
  }
  return(FALSE)
}

find_triangular <- function(max_number){
  #build vector in loop concatinating on new tir numbers
  to_test <- 1:max_number
  triangular_numbers <- numeric(0)
  for(i in to_test){
    if(is_triangular(i)){
      triangular_numbers <- c(triangular_numbers, i)
    }
  }
  print(paste("there are", length(triangular_numbers), 
              "triangular numbers between 1 and", max_number))
  return(triangular_numbers)
}