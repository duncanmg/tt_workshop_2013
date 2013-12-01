#! /bin/ksh

# for F in tt_workshop03 tt_workshop04 tt_workshop05 tt_workshop06 tt_workshop07 tt_workshop08 tt_workshop09 tt_workshop10 tt_workshop11 tt_workshop12 tt_workshop13 tt_workshop14 tt_workshop15 tt_workshop16 tt_workshop17 tt_workshop18 tt_workshop19 tt_workshop20 tt_workshop21 tt_workshop22 tt_workshop23 tt_workshop24 tt_workshop25 tt_workshop26 tt_workshop27 tt_workshop28 tt_workshop29 tt_workshop30
for F in tt_workshop02 
do
cp -r /home/duncan/* /home/$F
find /home/$F -name "*" -exec chown $F:tt_workshop {} \;
vi /home/$F/htdocs/index.htm
done

