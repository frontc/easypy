# 拼音田字格默写纸生成器

一个基于 FastAPI 的 Web 应用，用于生成带拼音的田字格默写纸，专为小学生语文练习设计。

## 功能特性

- **智能分词**：支持空格、逗号、制表符、换行等多种分隔符
- **拼音转换**：基于 `pypinyin` 词组模式，自动为汉字标注带声调拼音
- **田字格渲染**：CSS 绘制的标准田字格，300dpi 打印不失真
  - 外框实线，内部十字虚线
  - 每个田字格 52px × 52px，A4 纸一行约 10 个字
- **拼音标注**：每个字上方标注拼音（黑色），拼音区域无背景线条
- **默写模式**：可选择隐藏拼音或显示空白田字格，供学生默写练习
- **打印优化**：一键打印 A4 纸张，自动隐藏交互元素，防止跨页截断

## 技术栈

| 组件 | 技术 |
|------|------|
| 后端 | Python 3.11+、FastAPI、pypinyin |
| 前端 | 原生 HTML5 + CSS3 + Vanilla JS |
| 部署 | Docker / Docker Compose |

## 快速开始

### 方式一：直接运行（开发环境）

```bash
# 1. 克隆项目
cd /Users/lefer/project/easypy

# 2. 创建虚拟环境
python3 -m venv .venv
source .venv/bin/activate

# 3. 安装依赖
pip install -r requirements.txt

# 4. 启动服务
python main.py
```

访问 http://localhost:8000

### 方式二：Docker 部署（推荐）

```bash
# 1. 构建并启动
docker compose up -d

# 2. 查看日志
docker compose logs -f

# 3. 停止服务
docker compose down
```

访问 http://localhost:8000

## 使用说明

1. 在文本框中输入词语，支持以下分隔符：
   - 半角空格：`春天 花开`
   - 全角空格：`春天　花开`
   - 中文逗号：`春天，花开`
   - 英文逗号：`春天,花开`
   - 制表符：`春天<Tab>花开`
   - 换行符：`春天\n花开`
2. 点击「生成默写纸」按钮或按 `Ctrl + Enter`
3. 可选功能：
   - 勾选「显示拼音」— 在田字格上方显示拼音
   - 勾选「显示空白田字格」— 不显示汉字，留空供默写
4. 点击「打印」按钮直接打印 A4 纸张

## 项目结构

```
easypy/
├── main.py                 # FastAPI 后端应用
├── requirements.txt        # Python 依赖清单
├── templates/
│   └── index.html          # 前端页面（含 CSS + JS）
├── static/                 # 静态文件目录
├── Dockerfile              # Docker 构建配置
├── docker-compose.yml      # Docker Compose 配置
└── README.md               # 项目说明文档
```

## API 接口

### `POST /api/convert`

将中文词语文本转换为词语和拼音数据。

**请求体：**

```json
{
  "text": "方序 语文 默写"
}
```

**响应：**

```json
{
  "words": [
    { "word": "方序", "pinyin": ["fāng", "xù"] },
    { "word": "语文", "pinyin": ["yǔ", "wén"] },
    { "word": "默写", "pinyin": ["mò", "xiě"] }
  ]
}
```

### `GET /`

返回田字格默写纸生成器的主页面。

## 许可证

MIT
