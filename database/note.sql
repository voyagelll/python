/* Windows���� */
-- ���� MySQL
	net start mysql 
-- ���� Windows ����
	sc create mysql binPath= mysqld_bin_path()




/* ���ӷ����� */
mysql -h ��ַ -p �˿� -u �û��� -p ����

SHOW PROCESSLIST -- ��ʾ��Щ�߳�������
SHOW VARIABLES   -- ��ʾϵͳ������Ϣ 




/* ���ݿ���� */
SELECT DATABASES();   -- ��ʾ��ǰ���ݿ�
SELECT now();         -- ��ʾ��ǰʱ��
SELECT USER();		  -- ��ʾ��ǰ�û�
SELECT VERSION();     -- ��ʾ��ǰ�汾

-- �������ݿ�
CREATE DATABASE[ IF NOT EXISTS] ���ݿ��� ���ݿ�ѡ��

SHOW DATABASES[LIKE 'PATTERN']      -- �鿴��ǰ�����Ϣ
ALTER DATABASE ���� ѡ����Ϣ         -- �޸����ݿ�ѡ����Ϣ
DROP DATABASE[IF EXISTS] ���ݿ���    -- ɾ�����ݿ�




/* ��Ĳ��� */
-- ������
CREATE [TEMPORARY] TABLE [IF NOT EXISTS] [����.]����
	�ֶ��� �������� [NOT NULL | NULL] [DEFAULT default_value] [AUTO_INCREMENT] [UNIQUE [KEY] | [PRIMARY | KEY]] [COMMENT 'STRING']

	[��ѡ��]
		CHARSET = charset_name  -- ���û���趨�����������ݿ��ַ���
		ENGINE = engine_name    -- ���õ� InnoDB MyISAM Memory/Heap BDB Merge CSV 
			-- 	SHOW ENGINES ��ʾ�洢�����״̬��Ϣ
			--  SHOW ENGINE  ������ {LOGS|STATUS} ��ʾ�洢�������־��״̬��Ϣ
		AUTO_INCREMENT          -- ����

-- �鿴��
SHOW TABLES [LIKE 'PATTERN']  -- �鿴��
SHOW CREATE TABLE ����        -- �鿴�����ϸ��Ϣ 
DESC ����                     -- �������
SHOW TABLE STATUS [FROM db_name] [LIKE 'pattern']  -- �鿴��״̬

-- �޸ı�
ALTER TABLE ���� ���ѡ�eg��ENGINE=MYISAM)

-- ��������
RENAME TABLE ԭ���� TO �±���
RENAME TABLE ԭ���� TO ����.�������ɽ����ƶ�����һ�����ݿ⣩ 

-- �޸ı���ֶ� 
ALTER TABLE ���� ������
	-- ������
		ADD [COLUMN] �ֶζ���       -- �����ֶ�
			[ALTER �ֶ��� | FIRST]  -- �е�λ��
		ADD PRIMARY KEY(�ֶ���)     -- ��������
		ADD UNIQUE KEY(�ֶ���)      -- ����Ψһ����
		ADD INDEX [������] (�ֶ���)  -- ������ͨ����
		DROP [COLUMN] �ֶ���        -- ɾ���ֶ�
		MODIFY [COLUMN] �ֶ��� �ֶ�����  -- ���ֶ������޸�
		CHANGE [COLUMN] ԭ�ֶ��� ���ֶ��� �ֶ����� -- �޸��ֶ���
		DROP PRIMARY KEY            -- ɾ������������AUTO_INCREMENT ����ɾ�� AUTO_INCREMENT)
		DROP INDEX ������            -- ɾ������
		DROP FOREIGN KEY ���        -- ɾ�����

DROP TABLE ����                               -- ɾ����
TRUNCATE TABLE ����                           -- ��ձ� 
CREATE TABLE ���� LIKE Ҫ���Ƶı���            -- ���Ʊ�ṹ
CREATE TABLE ���� SELECT * FROM Ҫ���Ƶı���   -- ���Ʊ�Ľṹ������
-- �����Ƿ�����
CHECK TABLE  TABLE1 [, TABLE2]...[OPTION]...  
-- �Ż���
OPTIMIZE [LOCAL | NO_WRITE_TO_BINLOG] TABLE TABLE1 [,TABLE2]...  
-- �޸���
REPAIR [LOCAL | NO_WRITE_TO_BINLOG] TABLE TABLE1 [,TABLE2]...[QUICK] [EXTENDED] [USE_FROM] 
-- ������
ANALYZE [LOCAL | NO_WRITE_TO_BINLOG] TABLE TABLE1 [TABLE2]...    




/* ���ݲ��� */
-- ��
	INSERT [INTO] ���� [COLUMNS] VALUES [, VALUES...]
	-- �ڲ����ֵ����������Ψһ������ͻʱ�����������������е���Ϣ
	INSERT INTO TABLE_NAME VALUES/SET/SELECT ON DUPLICATE KEY UPDATE COLUMN=VALUE ...;
-- ɾ
	DELETE FROM ���� [condition] [ORDER BY COLUMN] [LIMIT NUM]
	TRUNCATE TABLE 
	-- DELETE TRUNCATE ����
		TRUNCATE : ɾ�������ؽ������ڴ������ı��ǣ��ᱣ��������
		DELETE : ����ɾ��
-- �� 
	UPDATE TABLE_NAME SET COLUMN_NAME = VALUE [COLUMN_NAME=VALUE] [CONDITION]
-- ��
	SELECT COLUMNS FROM TABLE_NAME [CONDITION]




/* �������ͣ������ͣ� */
-- ����
	tinyint    1�ֽ�		-128~127
	smallint   2�ֽ�     -32768~32767
	mediumint  3�ֽ�     -8388608~8388607
	int        4�ֽ�   
	bigint     8�ֽ�

-- ������
	float      4�ֽ�
	double     8�ֽ�
	��������Ҫָ����λ����С��λ��
	float(M, D), double(M, D)    M��ʾ��λ����D��ʾС��λ��

-- ������
	decimal  -- �ɱ䳤��
	decimal(M, D)    M��ʾ��λ����D��ʾС��λ��
	����һ����ȷ����ֵ�����ᷢ�����ݵĸı�

-- �ַ������� char varchar
	char    �����ַ������ٶȿ죬���˷ѿռ䣨���255���ַ���������޹أ�
	varchar �߳��ַ������ٶ���������ʡ�ռ䣨���65535���ַ���������йأ�
	varchar �����Ч����65532����Ϊvarchar�ڴ��ַ���ʱ����һ���ֽ��ǿյģ��������κ����ݣ�Ȼ���������ֽ�������ַ����ĳ��ȡ�

-- blob text 
	blob �������ַ������ֽ��ַ���)
		tinyblob, blob, mediumblob, longblob
	text �Ƕ������ַ���������Ҫ�������ȣ�
		tinytext�� text��mediumtext�� longtext

-- binary 
	������char ��varchar�����ڱ���������ַ���
	char�� varchar, text  ��Ӧ binary��varbinary�� blob

-- ʱ�����������
	datetime    8�ֽ�    ���ڼ�ʱ��    1000-01-01�� 00��00��00 ~ 9999-12-31 23��59��59
	date        3�ֽ�	 ����
	timestamp   4�ֽ�                 19700101000000 ~ 2038-01-19 03��14��07
	time        3�ֽ�     ʱ��         -838:59:59 ~ 838:59:59
	year        1�ֽ�     ��          1901 ~ 2155





/* �����ԣ���Լ���� */
-- primary key 
	- ��Ψһ��ʶ��¼���ֶΣ�������Ϊ����
	- һ����ֻ����һ������

-- unique Ψһ����
	- ʹ��ĳ�ֶε�ֵ����Ϊ�ظ�

-- foreign key ���Լ��
	- ��������������ӱ�����������
	ALTER TABLE t1 ADD CONSTRAINT `t1_t2_fk` FOREIGN KEY(t1_id) references t12(id);
	��������ı��Ϊ�ӱ����ָ��ı���Ϊ����




/* ����淶 */
-- ��һ��ʽ
	�ֶβ����ٷ�
-- �ڶ���ʽ
	�����ڲ��ֺ�������
-- ������ʽ
	�����ڴ��ݺ�������




/* SELECT */
SELECT [ALL | DISTINCT] select_expr FROM -> WHERE -> GROUP BY [�ϼƺ���] -> HAVING -> ORDER BY -> LIMIT ~ OFFSET ~
	
		


/* ���뵼�� */
- �������ݣ� SELECT * INTO outfile �ļ���ַ [���Ƹ�ʽ] FROM ����;    
- �������ݣ� LOAD DATA [local] infile �ļ���ַ [replace|IGNORE] INTO TABLE ���� [���Ƹ�ʽ];
	-- Ĭ���ļ���ַ��C:/ProgramData/MySQL/MySQL Server 8.0/Uploads
	-- replace|IGNORE ������Ψһ����¼���ظ��Ĵ���

	- ���Ƹ�ʽ
		Ĭ�ϣ�fields terminated by '\t' enclosed by '' escaped by '\\'
		terminated by 'string'    -- ��ֹ
		enclosed by 'char'        -- ����
		escaped by 'char'         -- ת�� 




/* �����뻹ԭ */
- ����
	mysqldump [options] db_name [tables]

	eg�� mysqldump -u�û��� -p���� ���� [����1, 2...] > (D:/D.sql)

- ���� 
	- ��¼����� 
		source �����ļ�
	- �ǵ�¼�����
		mysql -u�û��� -p���� ���� < �����ļ�




/* ��ͼ */
- ����
	    ��ͼ��һ��������������ɲ�ѯ���塣ͬ��ʵ�ı�һ������ͼ����һϵ�д������Ƶ��к������ݡ�
	������ͼ���������ݿ����Դ洢������ֵ����ʽ���ڡ��к��������������ɶ�����ͼ�Ĳ�ѯ�������õı�
	������������ͼʱ��̬���ɡ�
- ����
	��ȫ������ʹ���ӵĴ��������

- ������ͼ
	CREATE [OR REPLACE] [ALGORITHM={UNDEFINED|MERGE|TEMPLATE}] VIEW VIEW_NAME [(column_list)] AS select_statment
	-- ��ͼ�㷨
		-- MERGE ����ͼ�Ĳ�ѯ��䣬���ⲿ��ѯ��Ҫ�Ⱥϲ���ִ��
		-- TEMPLATE ����ͼִ����Ϻ��γ���ʱ����������ѯ
		-- UNDEFINED δ���壨Ĭ�ϣ���ָ����mysql����ȥѡ����Ӧ���㷨

- �鿴�ṹ
	SHOW CREATE VIEW VIEW_NAME 

- ɾ����ͼ
	DROP VIEW [IF EXISTS] VIEW_NAME ...

- �޸���ͼ
	ALTER VIEW VIEW_NAME [(COLUMN_LIST)] AS select_statment




/* ���� */
������ָ�߼��ϵ�һ���������ɲ����ĸ�����Ԫ��Ҫôȫ�ɹ�Ҫôȫʧ��
	- InnoDB ����Ϊ����ȫ������

- ������: START TRANSACTION ���� BEGIN 
- �����ύ: COMMIT 
- ����ع�: ROLLBACK

-- ���������
	1��ԭ���ԣ�Atomicity����������һ�����ɷָ�Ĺ�����Ԫ�������еĲ���Ҫô��������Ҫô��������
	2��һ���ԣ�Consistency��������ǰ�����ݵ������Ա��뱣��һ�¡� ������������У�������������
	3�������ԣ�Isolation��������û������������ݿ�ʱ��һ���û��������ܱ������û������������ţ�
	                      �����������֮�������Ҫ�໥����
    4���־��ԣ�Durability����һ������һ�����ύ���������ݿ��е����ݸı��������Ե�

-- ע��
	* ���ݿⶨ������(DDL) ��䲻�ܻع�
	* �����ܱ�Ƕ�� 

-- �����
	SAVEPOINT                  -- ����һ�����񱣴��
	ROLLBACK TO SAVEPOINT      -- �ع��������
	RELEASE SAVEPOINT          -- ɾ�������

-- InnoDB �Զ��ύ��������
	SET autocommit = 0|1       -- 0��ʾ�ر��Զ��ύ��1��ʾ�����Զ��ύ




/* ���� */
������ֻ���ڷ�ֹ�����ͻ��˽��в������ض�д
MyISAM��֧�ֱ����� InnoDB��֧������
-- ����
	LOCK TABLES table_name [AS alias]
-- ����
	UNLOCK TABLES 




/* ������ */
	��������������йص��������ݿ���󣬵��ñ�����ض��¼�ʱ��������Ķ���
	������ ��¼�����ӡ��޸ġ�ɾ��

-- ����������
CREATE TRIGGER trigger_name trigger_time trigger_event ON table_name FOR EACH ROW trigger_stmt
	- trigger_time����������Ķ���ʱ�䡣��������before �� after����ָ�������������ڼ����������֮ǰ��֮�������
	- trigger_event: ָ���˼����������������� 
		INSERT: �����в����ʱ���������
		UPDATE: ����ĳһ��ʱ���������
		DELETE: �ӱ���ɾ��ĳһ��ʱ�����������
	- table_name�� �����������Եı���������ʱ�����ͼ
	- trigger_stmt: ���������򼤻�ʱִ�е���䡣 ִ�ж����䣬��ʹ��BEGIN...END �������ṹ

-- ɾ��������
DROP TRIGGER trigger_name

-- �ַ����Ӻ���
concat��str1, str2...)
concat_ws(separater, str1, str2...)

-- ��֧���
if condition then
	execute_express
elseif condition_1 then 
	execute_express_1
else 
	execute_express_2
end if;

-- �޸Ľ�����
delimiter �Զ����������
	SQL���
�Զ����������

-- �����ִ��
	- ֻҪ��Ӽ�¼���ͻᴥ������
	- insert into on duplicate key update �ᴥ����
		���û���ظ���¼���ᴥ����before insert�� after insert 
		������ظ���¼�����£��ᴥ����before insert�� before update�� after update
		������ظ���¼����û�з������£��򴥷��� before insert�� before update 
	- replace �﷨ ����м�¼����ִ�У� before insert�� before delete��after delete, after insert 


/* ���� */
-- �½�
	CREATE FUNCTION function_name (�����б�) RETURNS ����ֵ����
		������

-- ɾ��
	DROP FUNCTION [IF EXISTS] function_name;

-- �鿴
	SHOW FUNCTION STATUS LIKE 'PATTERN'
	SHOW CREATE FUNCTION function_name

-- �޸� 
	ALTER FUNCTION function_name ����ѡ��  




/* �洢���� */
-- ����
	- �洢������һ�δ洢�����ݿ��е�sql���롣
	- һ���洢����ͨ���������һ��ҵ���߼������籨������������
	- һ������ͨ��רעĳ�����ܣ���Ϊ�����������ģ������ڴ洢�����е��ú����� 
	  �洢���̲��ܱ����ã����Լ�ִ�У�ͨ�� call ִ��

-- ����
CREATE PROCEDURE name�������б�
	BEGIN 
		������
	END

	- �����б���ͬ�ں����Ĳ����б���Ҫָ���������� 
				IN�������� 
				OUT�������
				INOUT�������





/* ���ú��� */
-- ��ֵ����
abs(x)          -- ����ֵ abs(-10.9) = 10
format(x, d)    -- ��ʽ��ǧ��λ��ֵ format(1234567.456, 2) = 1,234,567.46
ceil(x)         -- ����ȡ�� ceil(10.1) = 11
floor(x)        -- ����ȡ�� floor (10.1) = 10
round(x)        -- ��������ȥ��
mod(m, n)       -- m%n m mod n ���� 10%3=1
pi()            -- ���Բ����
pow(m, n)       -- m^n
sqrt(x)         -- ����ƽ����
rand()          -- �����
truncate(x, d)  -- ��ȡdλС��

-- ʱ�����ں���
now(), current_timestamp();     -- ��ǰ����ʱ��
current_date();                 -- ��ǰ����
current_time();                 -- ��ǰʱ��
date('yyyy-mm-dd hh:ii:ss');    -- ��ȡ���ڲ���
time('yyyy-mm-dd hh:ii:ss');    -- ��ȡʱ�䲿��
date_format('yyyy-mm-dd hh:ii:ss', '%d %y %a %d %m %b %j'); -- ��ʽ��ʱ��
unix_timestamp();               -- ���unixʱ���
from_unixtime();                -- ��ʱ������ʱ��

-- �ַ�������
length(string)          -- string���ȣ��ֽ�
char_length(string)     -- string���ַ�����
substring(str, position [,length])      -- ��str��position��ʼ,ȡlength���ַ�
replace(str ,search_str ,replace_str)   -- ��str����replace_str�滻search_str
instr(string ,substring)    -- ����substring�״���string�г��ֵ�λ��
concat(string [,...])   -- �����ִ�
charset(str)            -- �����ִ��ַ���
lcase(string)           -- ת����Сд
left(string, length)    -- ��string2�е������ȡlength���ַ�
load_file(file_name)    -- ���ļ���ȡ����
locate(substring, string [,start_position]) -- ͬinstr,����ָ����ʼλ��
lpad(string, length, pad)   -- �ظ���pad����string��ͷ,ֱ���ִ�����Ϊlength
ltrim(string)           -- ȥ��ǰ�˿ո�
repeat(string, count)   -- �ظ�count��
rpad(string, length, pad)   --��str����pad����,ֱ������Ϊlength
rtrim(string)           -- ȥ����˿ո�
strcmp(string1 ,string2)    -- ���ַ��Ƚ����ִ���С

-- ���̺���
case when [condition] then result [when [condition] then result ...] [else result] end   ���֧
if(expr1,expr2,expr3)  ˫��֧��

-- �ۺϺ���
count()
sum();
max();
min();
avg();
group_concat()

-- ��������
md5();
default();




/* �û���Ȩ�޹��� */
-- root ��������
	1.use mysql;	
	2.UPDATE `user` SET PASSWORD=PASSWORD("new_password") WHERE `user` ='root';
	3.FLUSH PRIVILEGES;  -- ˢ��Ȩ�� 





