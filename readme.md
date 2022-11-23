## Basic Info
This repository is for ENG2002 Group 7's Application Development Assignment

| Name       | Student ID | Contribution |
|------------|------------|--------------|
| LIN Ju     | 21106434D  |       T2   |
| NI Rouheng | 21102803D  |       T3       |              
| QIN Qijun  | 21101279D  |Structure Construction, T0, T1, T3, T4    |

## Program Naming Convention 程序命名规范

<table border="1" cellpadding="1" cellspacing="1"><tbody><tr><th>类别</th><th>规范</th><th>示例</th></tr><tr><td>Module 模块</td><td>小写字母，单词之间用_分割</td><td>ad_stats.py</td></tr><tr><td>Package 包</td><td>小写字母，单词之间用_分割</td><td>&nbsp;</td></tr><tr><td>Class 类</td><td>大驼峰法</td><td>HerPhoneNumber</td></tr><tr><td>Global Variable 全局变量</td><td>大写字母，单词之间用_分割</td><td>COLOR_WRITE</td></tr><tr><td>Normal Variable 普通变量</td><td>小写字母，单词之间用_分割 或 小驼峰法(开头小写)</td><td>her_phone_number 或 herPhoneNumber</td></tr><tr><td>Instance Variable 实例变量</td><td>以_开头，其他和普通变量一样</td><td>_instance_var</td></tr><tr><td>Private Variable 私有实例变量</td><td>以__开头（两个下划线），其他和普通变量一样</td><td>__private_var</td></tr><tr><td>Specific Variable 专有变量</td><td>以__开头，__结尾，一般为python的自有变量</td><td>__doc__</td></tr><tr><td>Normal Function 普通函数</td><td>小写字母，单词之间用_分割 (本次project不使用大写)</td><td>get_name()</td></tr><tr><td>Private Function 私有函数</td><td>以__开头（两个下划线），其他和普通变量一样</td><td>__get_name()</td></tr><tr><td>File 文件名</td><td>全小写，可使用下划线</td><td>&nbsp;</td></tr></tbody></table>

## File Structure 文件结构

Assignment2
- Assignment2_main.ipynb (用于正式提交)
- A2_for_develop_n_debug.py (用于编写调试)
- phonebook_package (包文件夹)
  - phonebook.py (模块Module)
- user_management_system (包文件夹)
  - user_management_sys.py (模块Module)
  
## Program Framework 程序框架

<img src="https://github.com/ENG2002Gp7Studio/ENG2002_Group7/blob/master/Sources/Program%20Structure.jpg?raw=true" alt="Program Structure">
