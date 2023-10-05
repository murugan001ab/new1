ob1=open('new3.csv','r')
rec_rect={}
all_rec_disr={}
col_nms=[]
all_col_val=[]
for lines in ob1:
    if not col_nms:
        col_nms=lines.split(",")
    else:
        col_values=lines.split(",")
        all_col_val.append(col_values)
#print(col_nms,all_col_val)
for x in range(len(col_nms)):
    rec_rect[col_nms[x]]=all_col_val[x][x]
print(
    all_rec_disr
)