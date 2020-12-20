select sum(sayi) from gunluk_rapor where durum = 0 and date(zaman) = date()
select sum(sayi) from gunluk_rapor where durum = 0 and date(zaman) = date('now','localtime')
select sum(sayi) from gunluk_rapor where durum = 1 and date(zaman) = date()
select * from gunluk_rapor where date(zaman) = date('now','localtime') 
select date('now','localtime')
select datetime()
SELECT date('now');
SELECT DATE('now', 'start of month', '+1 month', '-1 day');