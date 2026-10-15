# CLI项目需求

## 当前范围

通过基础库公开API提供十个现有CLI命令、可信5.7元数据采集和HTML报告。模块为`github.com/kimihiro-dev/innodb-go-reader-cli`，二进制为`innodb-reader`。物理格式、类型、损坏分类、预算和成功范围由[库支持矩阵](https://github.com/kimihiro-dev/innodb-go-reader/blob/main/docs/format/83-release-support-matrix.md)定义，本项目不复制物理解码。

## 输入与输出

参数、清单、无损协议、退出码、stdout/stderr分工及原子输出保护沿用[CLI指南](CLI.md)。固定输入按testdata/SOURCE.json保存来源和摘要，损坏测试只使用临时副本。MySQL驱动只用于元数据采集，不提供物理备份、事务恢复或快照比较。

## 开发与交付

go.mod/go.sum记录已推送基础库提交对应的真实伪版本或发布版本，构建无需相邻库目录或本地replace。本地可用忽略提交的go.work联合开发；交付前关闭工作区执行独立测试和构建。

验收包括现有CLI/采集/HTML测试、race/vet、固定输入及文档检查；共享协议、版本支持和原始证据不因拆分改变。远程仓库创建、推送和发布单独授权。
