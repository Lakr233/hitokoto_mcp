# Hitokoto MCP Server

基于 MCP (Model Context Protocol) 的一言服务器，提供随机中文诗词、名言等内容的 API 服务。

## 安装依赖

```bash
pip install -r requirements.txt
```

## 启动服务器

```bash
python hitokoto_mcp_server.py --port 8124
```

## 可用工具

### get_hitokoto()

获取随机一言，返回一句中文诗词或名言。

## 使用示例

启动服务器后，可以通过 MCP 客户端连接到 `http://localhost:8124` 来使用这个工具。

## 数据来源

数据来自 `hitokoto.json` 文件，包含了大量的中文诗词、名言等内容。服务器直接调用 `hitokoto.py` 模块来获取随机内容。
