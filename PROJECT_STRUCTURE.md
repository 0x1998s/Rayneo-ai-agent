# 📁 项目结构说明

## 🗂️ 总体结构

```
Rayneo-ai-agent/
├── 📁 .github/                      # GitHub配置文件
│   ├── 📁 ISSUE_TEMPLATE/           # Issue模板
│   │   ├── bug_report.md           # Bug报告模板
│   │   └── feature_request.md      # 功能请求模板
│   ├── 📁 workflows/               # GitHub Actions工作流
│   │   └── ci.yml                  # CI/CD流水线
│   └── PULL_REQUEST_TEMPLATE.md    # PR模板
├── 📁 backend/                      # 🚀 后端服务
│   ├── 📁 app/                     # 主应用目录
│   │   ├── 📁 api/                 # API路由层
│   │   │   ├── 📁 v1/              # API版本1
│   │   │   │   ├── auth.py         # 认证接口
│   │   │   │   ├── models.py       # 模型管理接口
│   │   │   │   ├── documents.py    # 文档管理接口
│   │   │   │   ├── workflows.py    # 工作流接口
│   │   │   │   ├── prompts.py      # Prompt管理接口
│   │   │   │   ├── finetune.py     # 微调接口
│   │   │   │   ├── chat.py         # 对话接口
│   │   │   │   └── admin.py        # 管理接口
│   │   │   ├── __init__.py
│   │   │   └── routes.py           # 路由聚合器
│   │   ├── 📁 core/                # 核心配置
│   │   │   ├── config.py           # 应用配置
│   │   │   ├── database.py         # 数据库连接
│   │   │   └── __init__.py
│   │   ├── 📁 models/              # 数据模型
│   │   │   ├── base.py             # 基础模型
│   │   │   ├── user.py             # 用户模型
│   │   │   ├── document.py         # 文档模型
│   │   │   └── __init__.py
│   │   ├── 📁 services/            # 业务服务
│   │   │   └── __init__.py
│   │   ├── 📁 utils/               # 工具函数
│   │   │   ├── logger.py           # 日志工具
│   │   │   └── __init__.py
│   │   ├── main.py                 # 应用入口
│   │   └── __init__.py
│   ├── requirements.txt            # Python依赖
│   └── Dockerfile                  # 后端容器配置
├── 📁 frontend/                     # 🎨 前端应用
│   ├── 📁 public/                  # 静态资源
│   │   ├── index.html              # HTML模板
│   │   └── manifest.json           # PWA配置
│   ├── 📁 src/                     # 源代码
│   │   ├── 📁 components/          # 通用组件
│   │   ├── 📁 pages/               # 页面组件
│   │   ├── 📁 services/            # API服务
│   │   ├── 📁 stores/              # 状态管理
│   │   ├── 📁 types/               # TypeScript类型
│   │   ├── 📁 utils/               # 工具函数
│   │   ├── App.tsx                 # 主应用组件
│   │   ├── App.css                 # 应用样式
│   │   ├── index.tsx               # 应用入口
│   │   └── index.css               # 全局样式
│   ├── package.json                # 前端依赖
│   ├── Dockerfile                  # 前端容器配置
│   ├── Dockerfile.test             # 测试容器配置
│   └── nginx.conf                  # Nginx配置
├── 📁 docs/                        # 📚 文档目录
│   ├── ARCHITECTURE.md             # 架构文档
│   ├── DEVELOPMENT_PLAN.md         # 开发计划
│   ├── DEMO_SUMMARY.md             # 演示总结
│   └── PROJECT_COMPLETION_REPORT.md # 完成度报告
├── 📁 scripts/                     # 📜 脚本目录
│   ├── start.sh                    # Linux/Mac启动脚本
│   └── start.bat                   # Windows启动脚本
├── docker-compose.yml              # 🐳 主要容器编排
├── docker-compose.test.yml         # 🧪 测试容器编排
├── CONTRIBUTING.md                 # 🤝 贡献指南
├── LICENSE                         # 📄 开源许可证
├── CHANGELOG.md                    # 📋 变更日志
├── README.md                       # 📖 项目说明
├── 简介.md                         # 📝 中文简介
└── PROJECT_STRUCTURE.md            # 📁 项目结构说明
```

## 📋 文件说明

### 🔧 配置文件
- **docker-compose.yml**: 主要的容器编排配置，包含所有服务
- **docker-compose.test.yml**: 测试环境的容器配置
- **.github/workflows/ci.yml**: GitHub Actions CI/CD配置
- **backend/requirements.txt**: Python依赖管理
- **frontend/package.json**: Node.js依赖管理

### 📚 文档文件
- **README.md**: 项目主要说明文档，包含安装、使用、API等信息
- **CONTRIBUTING.md**: 贡献指南，说明如何参与项目开发
- **LICENSE**: MIT开源许可证
- **CHANGELOG.md**: 版本变更记录
- **简介.md**: 中文项目简介，面向中文用户
- **docs/**: 详细技术文档目录

### 🚀 应用代码
- **backend/app/**: FastAPI后端应用主目录
- **frontend/src/**: React前端应用源码目录
- **scripts/**: 部署和运维脚本

### 🧪 测试相关
- **backend/tests/**: 后端测试用例（待实现）
- **frontend/src/__tests__/**: 前端测试用例（待实现）
- **docker-compose.test.yml**: 测试环境配置

## 🎯 设计原则

### 1. 模块化设计
- 每个功能模块独立开发和维护
- 清晰的接口定义和依赖关系
- 支持插件化扩展

### 2. 分层架构
```
表现层 (Frontend) → API层 (Gateway) → 业务层 (Services) → 数据层 (Database)
```

### 3. 容器化部署
- 所有服务都支持Docker容器化
- 环境一致性和快速部署
- 支持水平扩展

### 4. 文档驱动
- 完整的项目文档和API文档
- 代码注释和类型提示
- 清晰的开发和部署指南

## 🔄 开发流程

### 1. 开发环境搭建
```bash
# 1. 克隆项目
git clone https://github.com/0x1998s/Rayneo-ai-agent/.git

# 2. 启动开发环境
docker-compose up -d

# 3. 访问应用
# 前端: http://localhost:3000
# 后端: http://localhost:8000/docs
```

### 2. 代码提交流程
1. 创建功能分支
2. 开发和测试
3. 提交Pull Request
4. 代码审查
5. 合并到主分支

### 3. 部署流程
1. 构建Docker镜像
2. 运行测试套件
3. 部署到测试环境
4. 验证功能
5. 部署到生产环境

## 📊 项目指标

### 代码质量
- **测试覆盖率**: 目标 > 80%
- **代码规范**: 100%遵循
- **文档覆盖**: 100%覆盖
- **类型提示**: 100%覆盖

### 性能指标
- **API响应时间**: < 2秒
- **前端加载时间**: < 3秒
- **并发支持**: > 100用户
- **系统可用性**: > 99.9%

---

**注意**: 这个项目结构是基于企业级应用的实践设计，但是也仅是DEMO。
