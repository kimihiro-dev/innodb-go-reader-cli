# InnoDB Go Reader CLI

基于[innodb-go-reader](https://github.com/kimihiro-dev/innodb-go-reader)的命令行应用，提供metadata、page、export、query、check、space、stats、visualize、schema和manifest十个命令。物理解码与rowio/stats来自库；本项目管理命令、实例元数据采集、文件发布和HTML展示。

## 本地联合开发

需要Go 1.25或更高版本。将两个仓库放在同一父目录，在本项目根目录首次运行：

```sh
go work init . ../innodb-go-reader
go build -o /tmp/innodb-reader ./cmd/innodb-reader
/tmp/innodb-reader metadata testdata/mysql8045/lesson_rows.ibd
go test -race -timeout=25m ./...
```

已有go.work时用`go work use`补充目录。go.work/go.work.sum忽略提交，工作区只影响本项目目录，不影响父目录的其他项目。go.mod/go.sum记录可远程取得的真实库版本；工作区仅用于本地联调，交付前关闭工作区验证。只改CLI时可以直接使用已记录的真实库版本，无需检出库源码。

## 使用与验证

- [CLI指南](docs/CLI.md)：参数、输入准备、带类型无损输出及失败处理。
- [构建指引](docs/RELEASING.md)：各平台构建和手动发布。
- [当前需求](docs/REQUIREMENTS.md)、[约定](docs/CONVENTIONS.md)、[当前任务](docs/TODO.md)。
- [库支持矩阵](https://github.com/kimihiro-dev/innodb-go-reader/blob/main/docs/format/83-release-support-matrix.md)：物理格式及API的权威范围。

```sh
python3 scripts/check_fixtures.py
python3 scripts/check_docs.py
go vet ./...
```

独立验证使用`GOWORK=off go test -mod=readonly ./...`和`GOWORK=off go build -mod=readonly ./cmd/innodb-reader`核对独立构建。物理输入是调用方提供的稳定文件，schema只采集定义，不提供物理备份、事务恢复或双快照比较。

## 固定输入来源

[testdata/SOURCE.json](testdata/SOURCE.json)按基础库相对路径记录本项目固定输入的字节数和SHA256。复制文件保留原始字节和独立SQL来源；检查器可用`--source ../innodb-go-reader/testdata`额外核对来源副本。完整物理验证证据仍由基础库维护。
