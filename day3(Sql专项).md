#day3（Sql专项）

---
><h2>数据库 
>><h3>数据库语言的分类
    
        DQL 数据库查询语言 查
        DML 数据库操作语言 增删改
        DDL 数据库定义语言 定义表、数据库
        DCL 数据库控制语言 是用来设置或更改数据库用户或角色权限的语句，包括（grant,deny,revoke等）语句。这个比较少用到
>><h4>DDL
    
        查看数据库 show databases
        创建数据库 create database if not exists tablename
        删除表    drop table tablename
        查看表结构  desc tablename
    
>><h4>完整性约束
    
        mysql:
        主键 外键 非空 唯一 主键自增
        oracle：
        主键 外键 非空 唯一 check 
        
        主键自带 非空and唯一 特性
    

<h3>DDL练习
        
        --DDL 数据库定义语言
        SHOW DATABASES; --查看所有数据仓库
        
        CREATE DATABASE rg01; --创建数据库
        
        USE rg01;  --切换到rg01数据库
        
        SHOW TABLES; --查看数据库内表
        /*
        常用的数据通常用int类型来表示 占用内存空间小  通常跟数据字典联查
        数据字典格式
        id 主键
        value 名称
        编码	名称对应的编码
        exp：
        02 济南站 3701
        */
        CREATE TABLE stu(
            name VARCHAR(20), 
            age  DOUBLE(7,2),
            sex INT(2)  
            
        );
        -- 查看表结构
        DESC stu;
        
        -- 查看建表语句
        SHOW CREATE TABLE stu;
        
        -- 追加成绩的一列
        
        ALTER TABLE stu ADD score DOUBLE(5,2) NOT NULL;
        
        -- 修改列的类型
        -- 修改名字为char类型并且是非空字段
        ALTER TABLE stu MODIFY name CHAR(20) not null;
        
        -- 添加id主键
        
        ALTER TABLE stu ADD id int(3) PRIMARY KEY;
        
        -- 修改stu表列sex为gender

        ALTER TABLE stu CHANGE sex gender INT(2);
        
        
        -- 删除列stu表的classname列
        
        alter TABLE stu add classname VARCHAR(20);
        
        ALTER TABLE stu DROP classname;

                    
        -- 修改表名为student
        
        ALTER TABLE stu RENAME TO student;
        DESC student;


<h3>DML练习

        
        
        /*
        DML数据库操作语言
        */
        -- 插入数据  两种方式等价
        INSERT INTO student(name,age,gender,score,id) VALUES('lisantao',12,01,99,1);
        
        INSERT INTO student VALUES('lisantao1',13,02,99,2);
        
        SELECT * from student;
        
        
        INSERT INTO student(id,score,name) VALUES(3,100,'ls');
        
        
        -- 修改数据
            
        UPDATE student set age = 19;
        UPDATE student SET age = 18 WHERE id=3;
        
        SELECT * FROM student;
        
        -- 把性别为空的记录设置成0
        UPDATE student set gender = 0 where  gender IS null;
        
        -- 把名字为ls的记录 score改为90
        
        UPDATE student set gender = 0,score  =90 WHERE name='ls';
        
        
        -- 删除表中的数据
        -- 删除name为ls的记录
        DELETE from stu where name='ls'




<h3>DQL数据库查询语言
       
        --  查询学生表信息
        select * from student;
        -- DQL练习
        -- CREATE TABLE dept(
        -- 	deptno INT primary key,
        -- 	dname		varchar(14),
        -- 	loc		varchar(13)
        -- );
        -- INSERT INTO dept values(10, 'ACCOUNTING', 'NEW YORK');
        -- INSERT INTO dept values(20, 'RESEARCH', 'DALLAS');
        -- INSERT INTO dept values(30, 'SALES', 'CHICAGO');
        -- INSERT INTO dept values(40, 'OPERATIONS', 'BOSTON');
        -- CREATE TABLE emp(
        -- 	empno		INT,
        -- 	ename		VARCHAR(50),
        -- 	job		VARCHAR(50),
        -- 	mgr		INT,
        -- 	hiredate	DATE,
        -- 	sal		DECIMAL(7,2),
        -- 	comm		decimal(7,2),
        -- 	deptno		INT,
        --     constraint fk_dept_dp foreign key(deptno) references dept(deptno)
        -- ) ;
        -- INSERT INTO emp values(7369,'SMITH','CLERK',7902,'1980-12-17',800,NULL,20);
        -- INSERT INTO emp values(7499,'ALLEN','SALESMAN',7698,'1981-02-20',1600,300,30);
        -- INSERT INTO emp values(7521,'WARD','SALESMAN',7698,'1981-02-22',1250,500,30);
        -- INSERT INTO emp values(7566,'JONES','MANAGER',7839,'1981-04-02',2975,NULL,20);
        -- INSERT INTO emp values(7654,'MARTIN','SALESMAN',7698,'1981-09-28',1250,1400,30);
        -- INSERT INTO emp values(7698,'BLAKE','MANAGER',7839,'1981-05-01',2850,NULL,30);
        -- INSERT INTO emp values(7782,'CLARK','MANAGER',7839,'1981-06-09',2450,NULL,10);
        -- INSERT INTO emp values(7788,'SCOTT','ANALYST',7566,'1987-04-19',3000,NULL,20);
        -- INSERT INTO emp values(7839,'KING','PRESIDENT',NULL,'1981-11-17',5000,NULL,10);
        -- INSERT INTO emp values(7844,'TURNER','SALESMAN',7698,'1981-09-08',1500,0,30);
        -- INSERT INTO emp values(7876,'ADAMS','CLERK',7788,'1987-05-23',1100,NULL,20);
        -- INSERT INTO emp values(7900,'JAMES','CLERK',7698,'1981-12-03',950,NULL,30);
        -- INSERT INTO emp values(7902,'FORD','ANALYST',7566,'1981-12-03',3000,NULL,20);
        -- INSERT INTO emp values(7934,'MILLER','CLERK',7782,'1982-01-23',1300,NULL,10);
        -- 
        
        
        /*
        字段控制查询
        ·去除重复记录 DISTINCT
        ·把null转换为数值0的函数 IFNULL(expr1,expr2)
        ·给列起别名是可以省略as关键字
        分组查询
        ·GROUP BY
        ·HAVING 对分组后约束
        ·limit限制条数
        */
        -- 查看emp表中的职位
        select DISTINCT job from emp;
        -- 
        
        SELECT IFNULL(mgr,100) FROM emp;
        
        SELECT deptno FROM emp GROUP BY deptno;
        
        SELECT * from emp LIMIT 8,6;
        -- 查询mgr》9000的记录的全部信息
        SELECT * from emp HAVING mgr>9000;
        -- 工资大于1000的记录
        
        SELECT * from emp where sal>1000;
        --	查询id - 7369和7566
        SELECT * from emp where empno = 7368 OR empno = 7566;
        
        SELECT * from emp  where empno in (7368,7566,123,4123)
        
        -- 模糊查询
        SELECT * from emp where ename like '%s%';
        
        SELECT * from emp where ename like 's%';
        
        SELECT * from emp where ename like '_s%';
        
        -- 查询每一个部门工资的总和
        
        SELECT deptno,SUM(sal) from emp  GROUP BY deptno;
        
        -- 查询部门工资大于10000 的部门
        SELECT deptno from emp  GROUP BY deptno HAVING SUM(sal)>10000;
        
        -- 工资总和
        
        SELECT sal+IFNULL(comm,0) FROM emp;
        
        -- 查询工资收入在第六到第十名的信息
        
        SELECT * from emp ORDER BY sal DESC LIMIT 5,5;

<h3>联合查询
        
        /*
        联合查询
        多表连查
        合并结果集 
        联合查询
        */
        -- 查询 部门编号 部门名称 员工编号 员工名称 合并结果集
        SELECT deptno,dname from dept UNION ALL SELECT empno,ename from emp;
        
        
        -- 连接查询 求出多个表的乘积 存在问题 会产生笛卡尔积
        -- INNER JOIN on 来定义内链接
        
        SELECT * from dept d,emp e;
        SELECT * FROM dept d INNER JOIN emp e ON d.deptno = e.deptno;
        
        SELECT * from dept d,emp e where d.deptno = e.deptno;
        INSERT INTO dept VALUES(50,'python','jn')
        -- 左连接 右连接
        SELECT * from dept d  LEFT JOIN emp e ON d.deptno = e.deptno; -- 16条记录
        SELECT * from dept d  RIGHT JOIN emp e ON d.deptno = e.deptno; -- 14条记录 
        
        
        
        -- 自查询 嵌套查询 出现位置 where之后作为条件的一部分 from之后作为被查询的一张表
        
        SELECT deptno,dname from dept where deptno>10;
        SELECT * from dept WHERE deptno in (
        SELECT deptno from dept where deptno>10);
        
        
        SELECT * from emp order by sal DESC
        -- 对于from查询 要把结果集起一个别名 
        SELECT * from (SELECT * from emp order by sal DESC) as e WHERE e.sal>2000;
        
        
        
        
        /*
        多表联查 
        
        1.合并 结果集 union union all
        2.连接查询 内链接和外连接 外连接（左外连接，内外连接） oracle还有全外连接
        3.自查询（嵌套查询）where from from之后需要起别名
        */


<h2>SQL实训练习题
        
        /*
        1．实训题
        根据人力资源管理系统数据库中数据信息，完成下列操作。
        （1）	查询10号部门的所有员工信息。
            SELECT * FROM emp WHERE deptno = 10;
        （2）	查询所有职位编号为“SAlESMAN”的员工的员工号、员工名和部门号。
            SELECT empno,ename,deptno from emp where job = 'SALESMAN';
        （3）	查询每个员工的员工号、工资、奖金以及工资与奖金的和。
            SELECT empno,sal,IFNULL(comm,0),sal+IFNULL(comm,0) FROM emp;
        （4）	查询10号部门中职位编号为“ANALYST”和30号部门中职位编号为“clerk”的员工的信息。
            SELECT * FROM emp WHERE deptno = 10 and job='ANALYST' UNION ALL SELECT * FROM emp WHERE deptno = 30 and job='CLERK';
        （5）	查询所有职位名称不是“manager”且工资大于或等于2000的员工的详细信息。
            SELECT * from emp where sal>=2000 and job != 'manager';
        （6）	查询有奖金的员工的不同职位编号和名称
            SELECT DISTINCT job from emp WHERE comm>0;
        查询没有奖金或奖金低于100元的员工信息。
            SELECT * from emp where ename not in (SELECT  ename from emp WHERE comm>100);
        （7）	查询员工名（first_name）中不包含字母“S”的员工。
            SELECT ename from emp where ename not LIKE '%s%'
        （8）	查询员工的姓名和入职日期，并按入职日期从先到后进行排序。
            SELECT ename,hiredate from emp ORDER BY hiredate;
        （9）	显示所有员工的姓名、职位、工资和奖金，按职位降序排序，若职位相同则按工资升序排序。
            SELECT ename,job,sal,IFNULL(comm,0) from emp ORDER BY job desc,sal ASC;
        （10）	查询所有员工的姓名及其直接上级的姓名。
            select e.ename,m.ename  from emp e left join emp m on e.mgr=m.empno;
              查询各个部门号、部门名称、部门所在地以及部门领导的姓名。
            select d.deptno,d.dname,d.loc,e.ename  from dept d left join emp e on d.deptno=e.deptno AND e.job='manager';
        （11）	查询所有部门及其员工信息，包括那些没有员工的部门。
                SELECT * from dept d LEFT JOIN emp e  on e.deptno =  d.deptno
        （12）	查询所有员工及其部门信息，包括那些还不属于任何部门的员工。
                SELECT * from emp e LEFT JOIN dept d  on e.deptno =  d.deptno
        （13）	查询所有员工的员工号、员工名、部门名称、职位名称、工资和奖金。
                    select e.empno,e.ename,m.dname,e.job,e.sal,IFNULL(e.comm,0) from dept m,emp e WHERE e.deptno = m.deptno;
        （14）	查询至少有一个员工的部门信息。
        select * from employees where department_id in(select distinct department_id from employees)
        
        
        （15）	查询工资比7902号员工工资高的所有员工信息。
                SELECT * from emp where sal>(SELECT sal from emp WHERE empno=7902);
        
        （16）	查询工资高于公司平均工资的所有员工信息。
                SELECT * from emp WHERE sal>(SELECT avg(sal) from emp)
        （17）	查询各个部门中不同职位的最高工资
                SELECT max(sal) from emp GROUP BY deptno;
        （18）	查询各个部门的人数及平均工资
            SELECT avg(sal) from emp GROUP BY deptno;
        （19）	统计各个职位的员工人数与平均工资。
            SELECT count(empno),avg(sal) from emp GROUP BY job;
        （20）	统计每个部门中各职位的人数与平均工资。
                SELECT count(ename),avg(sal) from emp GROUP BY deptno;
        （21）	查询平均工资低于6000元的部门及其员工信息。
                SELECT e.*,d.* from emp e JOIN dept d on (e.deptno = d.deptno and 
                e.deptno in (SELECT e.deptno from emp GROUP BY e.deptno HAVING avg(sal)<6000));
        
        查询在销售部工作的员工的姓名信息。
        SELECT e.ename from emp e where deptno = (SELECT deptno from dept where dname='SALES');
        （22）	查询与7902号员工从事相同工作的所有员工信息。
                SELECT * from emp where job = (SELECT job from emp WHERE empno = 7902);
        （23）	查询工资高于7902号部门中所有员工的工资的员工姓名和工资。
                    SELECT ename,sal from emp where sal>(SELECT max(sal) from emp where deptno = (SELECT deptno from emp where empno = 7902 ));
        （24）	查询每个部门中的员工数量、平均工资
                    SELECT COunt(ename),avg(sal) from emp GROUP BY deptno;
        （25）	查询人数最多的部门信息。
                    SELECT * from dept where deptno = (SELECT deptno from  (SELECT count(*) as num,deptno from emp GROUP BY deptno ORDER BY num desc LIMIT 1) as e);
        （26）	查询所有员工中工资排序在5~10名之间的员工信息。
                SELECT ename from emp ORDER BY sal LIMIT 4,6;
        （27）	查询员工信息，要求以首字母大写的方式显示所有员工姓（last_name）和员工名（first_name）。
        select concat (UPPER(substring(ename,1,1)) , LOWER(substring(ename,2,length(ename)-1))) from emp; 
        （28）	查询员工名（first_name）正好为6个字符的员工的信息。
            SELECT * from emp where ename LIKE '______';
        （29）	查询员工名（first_name）的第2个字母为“M”的员工信息。
            SELECT * from emp where ename LIKE '_M%';
        （30）	查询所有员工名（first_name），如果包含字母“s”，则用“S”替换。
            select ename,REPLACE(ename,'S','s') from emp where ename like '%s%'; 
        （31）	查询在2月份入职的所有员工信息。
                select * from emp where MONTHNAME(hiredate)= 'February';
        
        */
 

-----
Date：2019.06.19  
Author:Dawn  
Location:Jinan   
Wechat：llmllm_llm  
>>[新浪微博](https://weibo.com/u/5034954422)
![BigData](https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1561595835&di=03f6e32d6baf29edfe9f71974cdcdf4d&imgtype=jpg&er=1&src=http%3A%2F%2Fwww.uml.org.cn%2Fsjjm%2Fimages%2F2014060322.jpg "区块链")
