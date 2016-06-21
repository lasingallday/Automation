set serveroutput on;
exec update_taxstinfo;
commit;
exec taxsp_full_tax_update('L:\taxtestutl','newmast');
exec taxsp_full_zip_update('L:\taxtestutl','zipseq');
exec taxsp_full_prod_update('L:\taxtestutl','prodseq');
exec taxsp_excp_load('L:\taxtestutl','excprule');
quit;
/