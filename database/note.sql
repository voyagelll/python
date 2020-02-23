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
	INSERT [INTO] 表名 [COLUMNS] VALUES [, VALUES...]
	-- 在插入的值出现主键或唯一索引冲突时，更新其他非主键列的信息
	INSERT INTO TABLE_NAME VALUES/SET/SELECT ON DUPLICATE KEY UPDATE COLUMN=VALUE ...;
-- 删
	DELETE FROM 表名 [condition] [ORDER BY COLUMN] [LIMIT NUM]
	TRUNCATE TABLE 
	-- DELETE TRUNCATE 区别
		TRUNCATE : 删除表在重建（用于带分区的表是，会保留分区）
		DELETE : 逐条删除
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




/* SELECT */
SELECT [ALL | DISTINCT] select_expr FROM -> WHERE -> GROUP BY [合计函数] -> HAVING -> ORDER BY -> LIMIT ~ OFFSET ~
	
		


/* 导入导出 */
- 导出数据： SELECT * INTO outfile 文件地址 [控制格式] FROM 表名;    
- 导出数据： LOAD DATA [local] infile 文件地址 [replace|IGNORE] INTO TABLE 表名 [控制格式];
	-- 默认文件地址：C:/ProgramData/MySQL/MySQL Server 8.0/Uploads
	-- replace|IGNORE 对现有唯一键记录的重复的处理

	- 控制格式
		默认：fields terminated by '\t' enclosed by '' escaped by '\\'
		terminated by 'string'    -- 终止
		enclosed by 'char'        -- 包裹
		escaped by 'char'         -- 转义 




/* 备份与还原 */
- 导出
	mysqldump [options] db_name [tables]

	eg： mysqldump -u用户名 -p密码 库名 [表名1, 2...] > (D:/D.sql)

- 导入 
	- 登录情况下 
		source 备份文件
	- 非登录情况下
		mysql -u用户名 -p密码 库名 < 备份文件




/* 视图 */
- 定义
	    视图是一张虚拟表，其内容由查询定义。同真实的表一样，视图包含一系列带有名称的列和行数据。
	但是视图并不在数据库中以存储的数据值集形式存在。行和列数据来自自由定义视图的查询所有引用的表，
	并且在引用视图时动态生成。
- 作用
	安全，可以使复杂的穿易于理解

- 创建视图
	CREATE [OR REPLACE] [ALGORITHM={UNDEFINED|MERGE|TEMPLATE}] VIEW VIEW_NAME [(column_list)] AS select_statment
	-- 视图算法
		-- MERGE 将视图的查询语句，与外部查询需要先合并再执行
		-- TEMPLATE 将视图执行完毕后，形成临时表，在做外层查询
		-- UNDEFINED 未定义（默认），指的是mysql自主去选择相应的算法

- 查看结构
	SHOW CREATE VIEW VIEW_NAME 

- 删除视图
	DROP VIEW [IF EXISTS] VIEW_NAME ...

- 修改视图
	ALTER VIEW VIEW_NAME [(COLUMN_LIST)] AS select_statment




/* 事务 */
事务是指逻辑上的一组操作，组成操作的各个单元，要么全成功要么全失败
	- InnoDB 被成为事务安全型引擎

- 事务开启: START TRANSACTION 或者 BEGIN 
- 事务提交: COMMIT 
- 事务回滚: ROLLBACK

-- 事务的特征
	1、原子性（Atomicity）：事务是一个不可分割的工作单元，事务中的操作要么都发生，要么都不发生
	2、一致性（Consistency）：事务前后数据的完整性必须保持一致。 整个事务过程中，操作是连续的
	3、隔离性（Isolation）：多个用户并发访问数据库时，一个用户的事务不能被其他用户的事务所干扰，
	                      多个并发事务之间的数据要相互隔离
    4、持久性（Durability）：一个事务一旦被提交，它对数据库中的数据改变是永久性的

-- 注意
	* 数据库定义语言(DDL) 语句不能回滚
	* 事务不能被嵌套 

-- 保存点
	SAVEPOINT                  -- 设置一个事务保存点
	ROLLBACK TO SAVEPOINT      -- 回滚到保存点
	RELEASE SAVEPOINT          -- 删除保存点

-- InnoDB 自动提交特性设置
	SET autocommit = 0|1       -- 0表示关闭自动提交，1表示开启自动提交




/* 锁表 */
表锁定只用于防止其它客户端进行不正当地读写
MyISAM：支持表锁， InnoDB：支持行锁
-- 锁定
	LOCK TABLES table_name [AS alias]
-- 解锁
	UNLOCK TABLES 




/* 触发器 */
	出发程序是与表有关的命名数据库对象，当该表出现特定事件时，将激活改对象
	监听： 记录的增加、修改、删除

-- 创建触发器
CREATE TRIGGER trigger_name trigger_time trigger_event ON table_name FOR EACH ROW trigger_stmt
	- trigger_time：出发程序的动作时间。（可以是before 或 after，以指定出发程序是在激活它的语句之前或之后出发）
	- trigger_event: 指明了激活触发程序的语句的类型 
		INSERT: 将新行插入表时激活触发程序
		UPDATE: 更改某一行时激活触发程序
		DELETE: 从表中删除某一行时触发激活程序
	- table_name： 必须是永久性的表，不能是临时表或视图
	- trigger_stmt: 当触发程序激活时执行的语句。 执行多个语句，可使用BEGIN...END 复合语句结构

-- 删除触发器
DROP TRIGGER trigger_name

-- 字符连接函数
concat（str1, str2...)
concat_ws(separater, str1, str2...)

-- 分支语句
if condition then
	execute_express
elseif condition_1 then 
	execute_express_1
else 
	execute_express_2
end if;

-- 修改结束符
delimiter 自定义结束符号
	SQL语句
自定义结束符号

-- 特殊的执行
	- 只要添加记录，就会触发程序
	- insert into on duplicate key update 会触发：
		如果没有重复记录，会触发：before insert， after insert 
		如果有重复记录并更新，会触发：before insert， before update， after update
		如果有重复记录但是没有发生更新，则触发： before insert， before update 
	- replace 语法 如果有记录，则执行： before insert， before delete，after delete, after insert 


/* 函数 */
-- 新建
	CREATE FUNCTION function_name (参数列表) RETURNS 返回值类型
		函数体

-- 删除
	DROP FUNCTION [IF EXISTS] function_name;

-- 查看
	SHOW FUNCTION STATUS LIKE 'PATTERN'
	SHOW CREATE FUNCTION function_name

-- 修改 
	ALTER FUNCTION function_name 函数选项  




/* 存储过程 */
-- 定义
	- 存储过程是一段存储在数据库中的sql代码。
	- 一个存储过程通常用于完成一段业务逻辑，例如报名，订单入库等
	- 一个函数通常专注某个功能，视为其他程序服务的，可以在存储过程中调用函数。 
	  存储过程不能被调用，是自己执行，通过 call 执行

-- 创建
CREATE PROCEDURE name（参数列表）
	BEGIN 
		过程体
	END

	- 参数列表：不同于函数的参数列表，需要指明参数类型 
				IN：输入型 
				OUT：输出型
				INOUT：混合型





/* 内置函数 */
-- 数值函数
abs(x)          -- 绝对值 abs(-10.9) = 10
format(x, d)    -- 格式化千分位数值 format(1234567.456, 2) = 1,234,567.46
ceil(x)         -- 向上取整 ceil(10.1) = 11
floor(x)        -- 向下取整 floor (10.1) = 10
round(x)        -- 四舍五入去整
mod(m, n)       -- m%n m mod n 求余 10%3=1
pi()            -- 获得圆周率
pow(m, n)       -- m^n
sqrt(x)         -- 算术平方根
rand()          -- 随机数
truncate(x, d)  -- 截取d位小数

-- 时间日期函数
now(), current_timestamp();     -- 当前日期时间
current_date();                 -- 当前日期
current_time();                 -- 当前时间
date('yyyy-mm-dd hh:ii:ss');    -- 获取日期部分
time('yyyy-mm-dd hh:ii:ss');    -- 获取时间部分
date_format('yyyy-mm-dd hh:ii:ss', '%d %y %a %d %m %b %j'); -- 格式化时间
unix_timestamp();               -- 获得unix时间戳
from_unixtime();                -- 从时间戳获得时间

-- 字符串函数
length(string)          -- string长度，字节
char_length(string)     -- string的字符个数
substring(str, position [,length])      -- 从str的position开始,取length个字符
replace(str ,search_str ,replace_str)   -- 在str中用replace_str替换search_str
instr(string ,substring)    -- 返回substring首次在string中出现的位置
concat(string [,...])   -- 连接字串
charset(str)            -- 返回字串字符集
lcase(string)           -- 转换成小写
left(string, length)    -- 从string2中的左边起取length个字符
load_file(file_name)    -- 从文件读取内容
locate(substring, string [,start_position]) -- 同instr,但可指定开始位置
lpad(string, length, pad)   -- 重复用pad加在string开头,直到字串长度为length
ltrim(string)           -- 去除前端空格
repeat(string, count)   -- 重复count次
rpad(string, length, pad)   --在str后用pad补充,直到长度为length
rtrim(string)           -- 去除后端空格
strcmp(string1 ,string2)    -- 逐字符比较两字串大小

-- 流程函数
case when [condition] then result [when [condition] then result ...] [else result] end   多分支
if(expr1,expr2,expr3)  双分支。

-- 聚合函数
count()
sum();
max();
min();
avg();
group_concat()

-- 其他函数
md5();
default();




/* 用户和权限管理 */
-- root 重置密码
	1.use mysql;	
	2.UPDATE `user` SET PASSWORD=PASSWORD("new_password") WHERE `user` ='root';
	3.FLUSH PRIVILEGES;  -- 刷新权限 





