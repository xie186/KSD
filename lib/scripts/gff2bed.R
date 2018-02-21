args = commandArgs(trailingOnly=TRUE)
# test if there is at least one argument: if not, return an error
if (length(args)==0 | length(args)==1) {
  stop("Two argument must be supplied (input file).n", call.=FALSE)
}

library(GenomicFeatures)
txdb <- makeTxDbFromGFF(args[1], format="gff")
genes <- genes(txdb)
write.table(as.data.frame(genes)[,c(-4)], file=args[2], row.names=F, col.names=F, sep="\t", quote=F)
