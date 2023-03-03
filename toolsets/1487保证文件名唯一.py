"""1487 保证文件名唯一
给你一个长度为 n 的字符串数组 names 。你将会在文件系统中创建 n 个文件夹：在第 i 分钟，新建名为 names[i] 的文件夹。

由于两个文件 不能 共享相同的文件名，因此如果新建文件夹使用的文件名已经被占用，系统会以 (k) 的形式为新文件夹的文件名添加后缀，其中 k 是能保证文件名唯一的 最小正整数 。

返回长度为 n 的字符串数组，其中 ans[i] 是创建第 i 个文件夹时系统分配给该文件夹的实际名称

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/making-file-names-unique
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""

"""对于需要被创建的文件名 \textit{name}name，如果文件系统中不存在名为 \textit{name}name 的文件夹，那么直接创建即可，否则我们需要从 k=1k=1 开始，尝试使用添加后缀 kk 的新文件名创建新文件夹。

使用哈希表 \textit{index}index 记录已创建的文件夹的下一后缀序号，遍历 \textit{names}names 数组，记当前遍历的文件名为 \textit{name}name：

如果 \textit{name}name 不在哈希表中，那么说明文件系统不存在名为 \textit{name}name 的文件夹，我们直接创建该文件夹，并且记录对应文件夹的下一后缀序号为 11。

如果 \textit{name}name 在哈希表中，那么说明文件系统已经存在名为 \textit{name}name 的文件夹，我们在哈希表找到 \textit{name}name 的下一后缀序号 kk，逐一尝试直到添加后缀 kk 的新文件名不存在于哈希表中，然后创建该文件夹。需要注意的是，创建该文件夹后，有两个文件名的下一后缀序号需要修改，首先文件名 \textit{name}name 的下一后缀序号为 k+1k+1，其次，文件名 \textit{name}name 添加后缀 kk 的新文件名的下一后缀序号为 11。

"""

class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        ans = []
        index = {}
        for name in names:
            if name not in index:
                ans.append(name)
                index[name] = 1
            else:
                k = index[name]
                while name + '(' + str(k) + ')' in index:
                    k += 1
                t = name + '(' + str(k) + ')'
                ans.append(t)
                index[name] = k + 1
                index[t] = 1
        return ans
