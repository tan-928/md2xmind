# 0 A.D. 游戏引擎系统功能树

## 程序入口与核心系统
### 主程序
#### 程序入口: `main()` - `source/main.cpp`
##### 被程序启动时调用，解析命令行参数
##### 调用 `source/main.cpp -> RunGameOrAtlas()` 选择运行模式
##### 初始化基础系统和错误处理

#### 游戏运行控制: `RunGameOrAtlas()` - `source/main.cpp`
##### 在 `source/main.cpp:508` 定义
##### 根据命令行参数决定启动游戏还是Atlas编辑器
##### 调用 `source/main.cpp -> MainControllerInit()` 和 `source/main.cpp -> MainControllerShutdown()`

#### 主控制器初始化: `MainControllerInit()` - `source/main.cpp`
##### 在 `source/main.cpp:478` 定义
##### 初始化引擎核心系统

#### 主控制器清理: `MainControllerShutdown()` - `source/main.cpp`
##### 在 `source/main.cpp:486` 定义
##### 清理引擎资源

### 事件处理
#### 主输入处理: `MainInputHandler()` - `source/main.cpp`
##### 在 `source/main.cpp:171` 定义
##### 处理SDL事件，包括窗口调整、退出请求等
##### 调用 `source/main.cpp -> QuitEngine()` 或其他控制函数

#### 事件循环: `PumpEvents()` - `source/main.cpp`
##### 在 `source/main.cpp:254` 定义
##### 处理SDL事件队列

#### 退出控制: `QuitEngine()` - `source/main.cpp`
##### 在 `source/main.cpp:152` 定义
##### 设置全局退出标志

#### 重启控制: `RestartEngine()` - `source/main.cpp`
##### 在 `source/main.cpp:157` 定义
##### 设置引擎重启标志

### 帧渲染控制
#### 帧更新: `Frame()` - `source/main.cpp`
##### 在 `source/main.cpp:363` 定义
##### 调用游戏逻辑更新和渲染
##### 调用 `LimitFPS()` 控制帧率

#### 帧率限制: `LimitFPS()` - `source/main.cpp`
##### 在 `source/main.cpp:281` 定义
##### 控制游戏运行帧率

#### 非可视帧: `NonVisualFrame()` - `source/main.cpp`
##### 在 `source/main.cpp:457` 定义
##### 用于无界面模式下的逻辑更新

## 游戏核心系统
### 游戏对象
#### 游戏类: `CGame` - `source/ps/Game.h`
##### 在 `source/ps/Game.h:38` 定义
##### 负责管理整个游戏的生命周期
##### 包含 `m_World`, `m_Simulation2`, `m_GameView` 等核心对象

#### 游戏启动: `StartGame()` - `source/ps/Game.h`
##### 在 `source/ps/Game.h:82` 声明
##### 使用给定属性和保存状态启动游戏
##### 调用 `source/ps/Game.h -> ReallyStartGame()`

#### 游戏更新: `Update()` - `source/ps/Game.h`
##### 在 `source/ps/Game.h:93` 声明
##### 每帧更新游戏逻辑，包含deltaRealTime参数
##### 调用模拟系统和视图系统更新

#### 视觉回放: `StartVisualReplay()` - `source/ps/Game.h`
##### 在 `source/ps/Game.h:86` 声明
##### 启动视觉回放功能

### 世界管理
#### 世界类: `CWorld` - `source/ps/World.h`
##### 管理游戏世界状态
##### 被 `CGame` 引用为 `m_World`

#### 地形管理: `CTerrain` - `source/graphics/Terrain.h`
##### 在图形系统中定义
##### 管理地形网格和高度图

## 模拟系统 (Simulation2)
### 模拟核心
#### 模拟主类: `CSimulation2` - `source/simulation2/Simulation2.h`
##### 在 `source/simulation2/Simulation2.h:49` 定义
##### 公共API，大部分代码通过此API与模拟系统交互
##### 被 `CGame` 引用为 `m_Simulation2`

#### 模拟初始化: `LoadScripts()` - `source/simulation2/Simulation2.h`
##### 在 `source/simulation2/Simulation2.h:65` 声明
##### 加载指定目录中的所有脚本
##### 调用 `source/simulation2/Simulation2.h -> LoadDefaultScripts()`

#### 状态重置: `ResetState()` - `source/simulation2/Simulation2.h`
##### 在 `source/simulation2/Simulation2.h:135` 声明
##### 初始化或重新初始化完整的模拟状态

### 实体管理
#### 实体创建: `AddEntity()` - `source/simulation2/Simulation2.h`
##### 在 `source/simulation2/Simulation2.h:184` 声明
##### 创建新实体并添加到世界中
##### 支持指定模板名称和首选ID

#### 实体销毁: `DestroyEntity()` - `source/simulation2/Simulation2.h`
##### 在 `source/simulation2/Simulation2.h:191` 声明
##### 将实体添加到销毁队列

#### 实体清理: `FlushDestroyedEntities()` - `source/simulation2/Simulation2.h`
##### 在 `source/simulation2/Simulation2.h:202` 声明
##### 实际执行实体销毁操作

### 组件系统
#### 攻击组件接口: `ICmpAttack` - `source/simulation2/components/ICmpAttack.h`
##### 在 `source/simulation2/components/ICmpAttack.h:28` 定义
##### 定义攻击相关功能接口
##### 实现 `GetRepeatTime()`, `GetAttackTypes()` 方法

#### 位置组件: `ICmpPosition` - `source/simulation2/components/ICmpPosition.h`
##### 管理实体的位置和朝向
##### 提供移动和旋转功能

#### 单位移动: `ICmpUnitMotion` - `source/simulation2/components/CCmpUnitMotion.h`
##### 在 `source/simulation2/components/CCmpUnitMotion.h` 定义
##### 处理单位移动逻辑

#### 视野组件: `ICmpVision` - `source/simulation2/components/ICmpVision.h`
##### 管理实体的视野范围

#### 所有权组件: `ICmpOwnership` - `source/simulation2/components/ICmpOwnership.h`
##### 管理实体的所有者关系

### 管理器组件
#### AI管理器: `ICmpAIManager` - `source/simulation2/components/ICmpAIManager.h`
##### 在 `source/simulation2/components/ICmpAIManager.h` 定义
##### 管理AI系统

#### 路径查找: `ICmpPathfinder` - `source/simulation2/components/ICmpPathfinder.h`
##### 实现路径查找算法

#### 范围管理器: `ICmpRangeManager` - `source/simulation2/components/ICmpRangeManager.h`
##### 管理实体间的距离和视野关系

#### 阻挡管理器: `ICmpObstructionManager` - `source/simulation2/components/ICmpObstructionManager.h`
##### 管理实体的碰撞和阻挡

#### 模板管理器: `ICmpTemplateManager` - `source/simulation2/components/ICmpTemplateManager.h`
##### 管理实体模板

## 图形渲染系统
### 渲染核心
#### 渲染器主类: `CRenderer` - `source/renderer/Renderer.h`
##### 在 `source/renderer/Renderer.h:54` 定义
##### 高级渲染接口，管理整帧渲染
##### 实现单例模式，通过 `g_Renderer` 全局访问

#### 帧渲染: `RenderFrame()` - `source/renderer/Renderer.h`
##### 在 `source/renderer/Renderer.h:85` 声明
##### 渲染完整的一帧

#### 渲染器初始化: `Open()` - `source/renderer/Renderer.h`
##### 在 `source/renderer/Renderer.h:79` 声明
##### 执行必要的初始化操作

#### 窗口调整: `Resize()` - `source/renderer/Renderer.h`
##### 在 `source/renderer/Renderer.h:82` 声明
##### 调整渲染器视图大小

### 场景渲染
#### 场景渲染器: `CSceneRenderer` - `source/renderer/SceneRenderer.h`
##### 管理3D场景的渲染
##### 被 `CRenderer` 调用

#### 游戏视图: `CGameView` - `source/graphics/GameView.h`
##### 在 `source/graphics/GameView.h` 定义
##### 管理游戏的视图和摄像机
##### 被 `CGame` 引用为 `m_GameView`

#### 摄像机: `CCamera` - `source/graphics/Camera.h`
##### 在 `source/graphics/Camera.h` 定义
##### 管理3D摄像机位置和朝向

#### 摄像机控制: `CameraController` - `source/graphics/CameraController.h`
##### 处理摄像机的用户控制

### 资源管理
#### 纹理管理器: `CTextureManager` - `source/graphics/TextureManager.h`
##### 管理纹理资源的加载和缓存
##### 通过 `CRenderer::GetTextureManager()` 访问

#### 材质管理器: `CMaterialManager` - `source/graphics/MaterialManager.h`
##### 管理材质资源

#### 着色器管理器: `CShaderManager` - `source/renderer/ShaderManager.h`
##### 管理着色器程序
##### 通过 `CRenderer::GetShaderManager()` 访问

#### 字体管理器: `CFontManager` - `source/graphics/FontManager.h`
##### 管理字体资源
##### 通过 `CRenderer::GetFontManager()` 访问

### 特效渲染
#### 地形渲染器: `CTerrainRenderer` - `source/renderer/TerrainRenderer.h`
##### 渲染地形网格

#### 水面管理器: `CWaterManager` - `source/renderer/WaterManager.h`
##### 管理水面渲染效果

#### 阴影贴图: `CShadowMap` - `source/renderer/ShadowMap.h`
##### 实现阴影映射

#### 粒子渲染器: `CParticleRenderer` - `source/renderer/ParticleRenderer.h`
##### 渲染粒子效果

#### 天空管理器: `CSkyManager` - `source/renderer/SkyManager.h`
##### 管理天空盒渲染

## GUI系统
### GUI核心
#### GUI管理器: `CGUIManager` - `source/gui/GUIManager.h`
##### 在 `source/gui/GUIManager.h:48` 定义
##### GUI系统的外部接口
##### 管理GUI页面栈

#### GUI主类: `CGUI` - `source/gui/CGUI.h`
##### 在 `source/gui/CGUI.h` 定义
##### 单个GUI页面的核心类

#### 页面切换: `SwitchPage()` - `source/gui/GUIManager.h`
##### 在 `source/gui/GUIManager.h:64` 声明
##### 加载新GUI页面并激活

#### 页面推入: `PushPage()` - `source/gui/GUIManager.h`
##### 在 `source/gui/GUIManager.h:70` 声明
##### 推入新页面到页面栈

#### 页面弹出: `PopPage()` - `source/gui/GUIManager.h`
##### 在 `source/gui/GUIManager.h:76` 声明
##### 从页面栈弹出当前页面

### GUI组件
#### GUI文本: `CGUIText` - `source/gui/CGUIText.h`
##### 渲染GUI文本元素

#### GUI精灵: `CGUISprite` - `source/gui/CGUISprite.h`
##### 管理GUI精灵图像

#### 滚动条: `CGUIScrollBarVertical` - `source/gui/CGUIScrollBarVertical.h`
##### 实现垂直滚动条

#### GUI设置: `CGUISetting` - `source/gui/CGUISetting.h`
##### 管理GUI设置和属性

### GUI渲染
#### GUI渲染器: `CGUIRenderer` - `source/gui/GUIRenderer.h`
##### 负责GUI元素的渲染

#### 工具提示: `CGUITooltip` - `source/gui/GUITooltip.h`
##### 管理工具提示显示

## 网络系统
### 网络核心
#### 网络客户端: `CNetClient` - `source/network/NetClient.h`
##### 管理网络客户端连接

#### 网络服务器: `CNetServer` - `source/network/NetServer.h`
##### 管理网络服务器功能

#### 网络会话: `CNetSession` - `source/network/NetSession.h`
##### 管理网络会话

### 大厅系统
#### XMPP客户端: `IXmppClient` - `source/lobby/IXmppClient.h`
##### 处理大厅聊天和匹配

## 音频系统
### 声音管理
#### 声音管理器: `ISoundManager` - `source/soundmanager/ISoundManager.h`
##### 音频系统的主接口

#### 声音组件: `ICmpSound` - `source/simulation2/components/ICmpSound.h`
##### 实体的声音播放组件

## 脚本系统
### 脚本接口
#### 脚本接口: `CScriptInterface` - `source/scriptinterface/ScriptInterface.h`
##### JavaScript与C++的桥接

#### 脚本引擎: `CScriptEngine` - `source/scriptinterface/ScriptEngine.h`
##### 管理JavaScript引擎

#### 脚本上下文: `CScriptContext` - `source/scriptinterface/ScriptContext.h`
##### 管理脚本执行上下文

## 配置与数据管理
### 配置系统
#### 配置数据库: `CConfigDB` - `source/ps/ConfigDB.h`
##### 在 `source/ps/ConfigDB.h` 定义
##### 管理游戏配置数据

#### 全局变量: `Globals` - `source/ps/Globals.h`
##### 定义全局变量和常量

### 文件系统
#### 文件系统: `Filesystem` - `source/ps/Filesystem.h`
##### 提供虚拟文件系统接口

#### 模组管理: `CMod` - `source/ps/Mod.h`
##### 管理游戏模组

### 保存与加载
#### 保存游戏: `CSavedGame` - `source/ps/SavedGame.h`
##### 管理游戏保存和加载

#### 回放系统: `CReplay` - `source/ps/Replay.h`
##### 管理游戏回放功能

## 工具与实用程序
### 调试工具
#### 调试渲染器: `CDebugRenderer` - `source/renderer/DebugRenderer.h`
##### 提供调试可视化功能

#### 控制台: `CConsole` - `source/ps/CConsole.h`
##### 游戏内控制台界面

#### 日志系统: `CLogger` - `source/ps/CLogger.h`
##### 管理日志输出

### 性能分析
#### 性能分析器: `CProfiler2` - `source/ps/Profiler2.h`
##### 提供性能分析功能

#### 性能查看器: `CProfileViewer` - `source/ps/ProfileViewer.h`
##### 显示性能分析结果

### 输入处理
#### 热键系统: `CHotkey` - `source/ps/Hotkey.h`
##### 管理键盘快捷键

#### 触摸输入: `CTouchInput` - `source/ps/TouchInput.h`
##### 处理触摸设备输入

#### 游戏手柄: `CJoystick` - `source/ps/Joystick.h`
##### 处理游戏手柄输入

## 地图编辑器 (Atlas)
### Atlas核心
#### Atlas启动: `StartAtlas()` - `source/main.cpp`
##### 在 `source/main.cpp:162` 定义
##### 启动Atlas地图编辑器

## 低级系统
### 字符串处理
#### 字符串类: `CStr` - `source/ps/CStr.h`
##### 自定义字符串类

#### 字符串内化: `CStrIntern` - `source/ps/CStrIntern.h`
##### 字符串内化优化

### 容器和数据结构
#### 智能指针: `Future` - `source/ps/Future.h`
##### 异步操作的Future实现

#### 任务管理器: `CTaskManager` - `source/ps/TaskManager.h`
##### 管理后台任务

### 数学库
#### 数学函数: 位于 `source/maths/` 目录
##### 提供各种数学计算功能

## 第三方库集成
### 外部库
#### 第三方库: 位于 `source/third_party/` 目录
##### 集成各种第三方库

#### 库管理: 位于 `libraries/` 目录
##### 管理依赖库

## 测试系统
### 测试框架
#### 测试设置: `test_setup.cpp` - `source/test_setup.cpp`
##### 测试框架的初始化代码

#### 组件测试: 位于各个模块的 `tests/` 子目录
##### 各模块的单元测试 