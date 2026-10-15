# CLI工程约定

- Go 1.25或更高；基础库通过公开API依赖，MySQL采集使用go.mod锁定驱动；不新增依赖或另写物理解析器。
- 做最小改动，Go修改使用gofmt；错误保留原因链，输出失败及取消不冒充完整成功。
- REQUIREMENTS说明当前范围，TODO只列进行中和明确待办；完成即删除，不写决议或完成流水。
- 固定输入和独立来源不可改写；更新固定输入时同步SOURCE.json并核对原始SHA256。
- 运行适用测试及python3 scripts/check_fixtures.py、python3 scripts/check_docs.py并检查diff。
- 构建跟随当前分支最新提交，记录实际CLI提交及库依赖；go.work仅用于本地联调，正式验证关闭工作区。
- 格式/API支持正文在基础库，参数和应用行为在本项目；不复制兼容矩阵或扩大支持承诺。
