# 🤝 贡献指南

感谢您对 Rayneo AI Agent 项目的兴趣！

## 📋 贡献类型

- 🐛 **Bug修复**
- ✨ **新功能开发**
- 📚 **文档改进**
- 🧪 **测试用例**
- 🎨 **UI/UX改进**
- 🔧 **性能优化**

## 🚀 快速开始

### 1. Fork 项目

点击右上角的 "Fork" 按钮，将项目复制到您的GitHub账户。

### 2. 克隆到本地

```bash
git clone https://github.com/YOUR_USERNAME/Rayneo-ai-agent.git
cd Rayneo-ai-agent
```

### 3. 创建功能分支

```bash
git checkout -b feature/your-feature-name
# 或
git checkout -b bugfix/your-bugfix-name
```

### 4. 设置开发环境

```bash
# 后端环境
cd backend
pip install -r requirements.txt

# 前端环境
cd ../frontend
npm install

# Docker环境（推荐）
docker-compose up -d
```

## 📝 开发规范

### 代码风格

#### Python (后端)
- 使用 **PEP 8** 代码风格
- 使用 **Black** 进行代码格式化
- 使用 **isort** 进行导入排序
- 使用 **mypy** 进行类型检查

```bash
# 安装开发工具
pip install black isort mypy flake8

# 格式化代码
black backend/
isort backend/
```

#### TypeScript/React (前端)
- 使用 **Prettier** 进行代码格式化
- 使用 **ESLint** 进行代码检查
- 遵循 **React Hooks** 最佳实践

```bash
# 格式化代码
npm run lint
npm run lint:fix
```

### 提交信息规范

使用 [Conventional Commits](https://www.conventionalcommits.org/) 规范：

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

**类型 (type):**
- `feat`: 新功能
- `fix`: Bug修复
- `docs`: 文档更新
- `style`: 代码格式化
- `refactor`: 代码重构
- `test`: 测试相关
- `chore`: 构建/工具相关

**示例:**
```
feat(models): 添加新的模型管理功能

- 实现模型列表展示
- 添加模型拉取功能
- 更新API接口

Closes #123
```

## 🧪 测试

### 后端测试

```bash
cd backend
pytest tests/ -v --cov=.
```

### 前端测试

```bash
cd frontend
npm test
```

### 集成测试

```bash
docker-compose -f docker-compose.test.yml up --build
```

## 📚 文档

### API文档
- 使用 **FastAPI** 自动生成 OpenAPI 文档
- 访问 `http://localhost:8000/docs`

### 代码文档
- Python: 使用 **Google风格** 的docstring
- TypeScript: 使用 **JSDoc** 注释

**Python示例:**
```python
async def process_document(
    self, 
    file_path: str, 
    file_type: str = "pdf"
) -> Dict[str, Any]:
    """处理文档并返回结果.
    
    Args:
        file_path: 文档文件路径
        file_type: 文档类型，可选 'pdf', 'docx', 'txt'
        
    Returns:
        包含处理结果的字典
        
    Raises:
        ValueError: 当文件格式不支持时
    """
```

## 🔍 代码审查

### Pull Request 流程

1. **创建PR**: 从您的功能分支创建PR到 `main` 分支
2. **填写模板**: 使用PR模板描述您的更改
3. **等待审查**: 维护者会审查您的代码
4. **处理反馈**: 根据反馈修改代码
5. **合并**: 审查通过后合并到主分支

### PR检查清单

- [ ] 代码遵循项目风格指南
- [ ] 添加了必要的测试
- [ ] 所有测试都通过
- [ ] 更新了相关文档
- [ ] 提交信息符合规范
- [ ] 没有合并冲突

## 🐛 Bug报告

使用 [Bug报告模板](.github/ISSUE_TEMPLATE/bug_report.md) 创建Issue，包含：

- 详细的问题描述
- 复现步骤
- 期望行为
- 环境信息
- 错误日志

## ✨ 功能请求

使用 [功能请求模板](.github/ISSUE_TEMPLATE/feature_request.md) 创建Issue，包含：

- 功能描述
- 使用场景
- 实现建议
- 优先级

## 🏷️ 发布流程

### 版本号规范

使用 [语义化版本](https://semver.org/lang/zh-CN/)：`MAJOR.MINOR.PATCH`

- **MAJOR**: 不兼容的API更改
- **MINOR**: 向后兼容的功能添加
- **PATCH**: 向后兼容的Bug修复

### 发布步骤

1. 更新版本号
2. 更新CHANGELOG.md
3. 创建Release标签
4. 发布到GitHub Releases

## 📞 获取帮助

如果您有任何问题：

1. 查看 [文档](./docs/)
2. 搜索现有 [Issues](https://github.com/0x1998s/Rayneo-ai-agent/issues)
3. 创建新的Issue
4. 联系维护者:
   - 微信: Joeng_Jimmy
   - 邮箱: jemmy_yang@yeah.net

---

**感谢您的贡献！** 🎉
