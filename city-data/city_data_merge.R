library(splitstackshape)
library(sqldf)
wd <- "/Users/Dani/Dropbox/city-data"
setwd(wd)
file_list <-list.files()

for (file in file_list){
    filepath <- file.path(wd ,paste(file,sep=""))
    name <- substr(file, 1, 4)
    data.frame(assign(name, read.csv(filepath, sep = ",")))
}


m <- merge(walk, Medi, by='City', all=TRUE)
n <-merge(m, COLi, by='City', all=TRUE)
p <-merge(n, weat, by='City', all=TRUE)
q <-merge(p, crim, by='City', all=TRUE)
final<- q[!(is.na(q$Walk.Score) | q$Walk.Score==""), ]

final_unique <- sqldf("SELECT DISTINCT *
                     FROM final
      
                    ")