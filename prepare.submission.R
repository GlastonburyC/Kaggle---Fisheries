library(gtools)

sub=read.table('submit.csv',head=T,sep=",")
sub=sub[mixedorder(sub[,1]),]
sub$images = unlist(lapply(sub[,1],function(x) strsplit(as.character(x),"_r")[[1]][1]))

#sub_final=aggregate(sub[c('ALB','BET','DOL','LAG','NoF','OTHER','SHARK','YFT')], by=sub['images'], mean)
sub_final=aggregate(sub[c('ALB','BET','DOL','LAG','NoF','OTHER','SHARK','YFT')], by=sub['images'], max)

colnames(sub_final)[1]="image"
sub_final$image=paste0(sub$image,".jpg")

#write.table(sub_final,"submit.mean.csv",col.names=T,row.names=F,sep=",",quote=F)
write.table(sub_final,"submit.max.csv",col.names=T,row.names=F,sep=",",quote=F)
