library(gtools)

sub=read.table('submit.csv',head=T,sep=",")
sub=sub[mixedorder(sub[,1]),]
sub$images = unlist(lapply(sub[,1],function(x) strsplit(as.character(x),"_r")[[1]][1]))

sub_final=aggregate(sub[c('ALB','BET','DOL','LAG','NoF','OTHER','SHARK','YFT')], by=sub['images'], mean)

colnames(sub_final)[1]="image"
sub_final$image=paste0(sub_final$image,".jpg")

write.table(sub_final,"submit.mean.aug10000.csv",sep=",",quote=F,col.names=T,row.names=F)


#max_prob=as.matrix(apply(sub[,2:(ncol(sub)-1)], 1, function(x) max(x)))
#sub_final$max=max_prob
#sub_final_max=aggregate(sub_final, by=sub_final['images'], max)

#sub_final_max$max=NULL
#sub_final_max$image=NULL

#colnames(sub_final_max)[1]="image"
#sub_final_max$image=paste0(sub_final_max$image,".jpg")

#sub_final_max[,10]=NULL
#write.table(sub_final_max,"submit.max.aug10000.csv",sep=",",quote=F,col.names=T,row.names=F)
