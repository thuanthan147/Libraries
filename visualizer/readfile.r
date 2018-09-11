library(gdata)
library(XLConnect)
library(foreign)

read_file <- function(fileName){
fileNameHolder <- unlist(strsplit(fileName, "."))
formatFile <- fileNameHolder[length(fileNameHolder] - 1]
if (formatFile == "xls" | formatFile == "xlsx"){
myData <- read.xls(fileName)
} else if (formatFile == "mtp"){
myData <- read.mtp(fileName)
} else if (formatFile == "spss"){
myData <- read.spss(fileName, to.data.frame=TRUE)
} else if (formatFile == "txt"){
myData <- read.table(fileName)
} else if (formatFile == "csv"){
myData = read.csv(fileName)
}
return(myData)
}

