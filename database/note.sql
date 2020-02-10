/* Windows服务 */
-- 启动 MySQL
	net start mysql 
-- 创建 Windows 服务
	sc create mysql binPath= mysqld_bin_path()


/* 连接服务器 */
mysql -h 地址 -p 端口 -u 用户名 -p 密码

SHOW PROCESSLIST -- 显示哪些线程在运行
SHOW VARIABLES   -- 显示系统变量信息 


/* 数据库擦做 */
SELECT DATABASES();   -- 显示当前数据库
SELECT now();         -- 显示当前时间
SELECT USER();		  -- 显示当前用户
SELECT VERSION();     -- 显示当前版本

-- 创建数据库
CREATE DATABASE[ IF NOT EXISTS] 数据库名 数据库选项

SHOW DATABASES[LIKE 'PATTERN']      -- 查看当前库的信息
ALTER DATABASE 库名 选项信息         -- 修改数据库选项信息
DROP DATABASE[IF EXISTS] 数据库名    -- 删除数据库


/* 表的操作 */
-- 创建表
CREATE [TEMPORARY] TABLE [IF NOT EXISTS] [库名.]表名
	字段名 数据类型 [NOT NULL | NULL] [DEFAULT default_value] [AUTO_INCREMENT] [UNIQUE [KEY] | [PRIMARY | KEY]] [COMMENT 'STRING']

	[表选项]
		CHARSET = charset_name  -- 如果没有设定，则适用数据库字符集
		ENGINE = engine_name    -- 常用的 InnoDB MyISAM Memory/Heap BDB Merge CSV 
			-- 	SHOW ENGINES 显示存储引擎的状态信息
			--  SHOW ENGINE  引擎名 {LOGS|STATUS} 显示存储引擎的日志或状态信息
		AUTO_INCREMENT          -- 自增

-- 查看表
SHOW TABLES [LIKE 'PATTERN']  -- 查看表
SHOW CREATE TABLE 表名        -- 查看表的详细信息 
DESC 表名                     -- 表的描述
SHOW TABLE STATUS [FROM db_name] [LIKE 'pattern']  -- 查看表状态

-- 修改表
ALTER TABLE 表名 表的选项（eg：ENGINE=MYISAM)

-- 表重命名
RENAME TABLE 原表名 TO 新表名
RENAME TABLE 原表名 TO 库名.表名（可将表移动到另一个数据库） 

-- 修改表的字段 
ALTER TABLE 表名 操作名
	-- 操作名
		ADD [COLUMN] 字段定义       -- 增加字段
			[ALTER 字段名 | FIRST]  -- 列的位置
		ADD PRIMARY KEY(字段名)     -- 创建主键
		ADD UNIQUE KEY(字段名)      -- 创建唯一索引
		ADD INDEX [索引名] (字段名)  -- 创建普通索引
		DROP [COLUMN] 字段名        -- 删除字段
		MODIFY [COLUMN] 字段名 字段属性  -- 对字段属性修改
		CHANGE [COLUMN] 原字段名 新字段名 字段属性 -- 修改字段名
		DROP PRIMARY KEY            -- 删除主键（如有AUTO_INCREMENT 须先删除 AUTO_INCREMENT)
		DROP INDEX 索引名            -- 删除索引
		DROP FOREIGN KEY 外键        -- 删除外键

DROP TABLE 表名                               -- 删除表
TRUNCATE TABLE 表名                           -- 清空表 
CREATE TABLE 表名 LIKE 要复制的表名            -- 复制表结构
CREATE TABLE 表名 SELECT * FROM 要复制的表名   -- 复制表的结构和数据
-- 检查表是否有误
CHECK TABLE  TABLE1 [, TABLE2]...[OPTION]...  
-- 优化表
OPTIMIZE [LOCAL | NO_WRITE_TO_BINLOG] TABLE TABLE1 [,TABLE2]...  
-- 修复表
REPAIR [LOCAL | NO_WRITE_TO_BINLOG] TABLE TABLE1 [,TABLE2]...[QUICK] [EXTENDED] [USE_FROM] 
-- 分析表
ANALYZE [LOCAL | NO_WRITE_TO_BINLOG] TABLE TABLE1 [TABLE2]...    


/* 数据操作 */
-- 增
	INSERT [INTO] 表名 [COLUMNS] VALUES [VALUES...]
-- 删
	DELETE FROM 表名 [condition]
-- 改 
	UPDATE TABLE_NAME SET COLUMN_NAME = VALUE [COLUMN_NAME=VALUE] [CONDITION]
-- 查
	SELECT COLUMNS FROM TABLE_NAME [CONDITION]


/* 数据类型（列类型） */
-- 整形
	tinyint    1字节		-128~127
	smallint   2字节     -32768~32767
	mediumint  3字节     -8388608~8388607
	int        4字节   
	bigint     8字节

-- 浮点型
	float      4字节
	double     8字节
	定义是需要指定总位数和小数位数
	float(M, D), double(M, D)    M表示总位数，D表示小数位数

-- 定点数
	decimal  -- 可变长度
	decimal(M, D)    M表示总位数，D表示小数位数
	保存一个精确的数值，不会发生数据的改变

-- 字符串类型 char varchar
	char    定常字符串，速度快，但浪费空间（最多255个字符，与编码无关）
	varchar 边长字符串，速度慢，但节省空间（最多65535个字符，与编码有关）
	varchar 最大有效长度65532，因为varchar在存字符串时，第一个字节是空的，不存在任何数据，然后还需两个字节来存放字符串的长度。

-- blob text 
	blob 二进制字符串（字节字符串)
		tinyblob, blob, mediumblob, longblob
	text 非二进制字符串（不需要给定长度）
		tinytext， text，mediumtext， longtext

-- binary 
	类似于char 和varchar，用于保存二进制字符串
	char， varchar, text  对应 binary，varbinary， blob

-- 时间和日期类型
	datetime    8字节    日期及时间    1000-01-01： 00：00：00 ~ 9999-12-31 23：59：59
	date        3字节	 日期
	timestamp   4字节                 19700101000000 ~ 2038-01-19 03：14：07
	time        3字节     时间         -838:59:59 ~ 838:59:59
	year        1字节     年          1901 ~ 2155


/* 列属性（列约束） */
-- primary key 
	- 能唯一标识记录的字段，可以作为主键
	- 一个表只能有一个主键

-- unique 唯一索引
	- 使得某字段的值不能为重复

-- foreign key 外键约束
	- 用于限制主表与从表数据完整性
	ALTER TABLE t1 ADD CONSTRAINT `t1_t2_fk` FOREIGN KEY(t1_id) references t12(id);
	存在外键的表成为子表，外键指向的表，成为父表


/* 建表规范 */
-- 第一范式
	字段不可再分
-- 第二范式
	不存在部分函数依赖
-- 第三范式
	不存在传递函数依赖
	









