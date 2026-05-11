from pathlib import Path
import base64
import streamlit as st

ROOT         = Path(__file__).parent
AWARD_DIR    = ROOT / "assets" / "awards"
RESEARCH_DIR = ROOT / "assets" / "research"
PROJECT_DIR  = ROOT / "assets" / "project"
SCORES_DIR   = ROOT / "assets" / "scores"

# ══════════════════════════════════════════════════════════════
#  数据
# ══════════════════════════════════════════════════════════════

STATS = [
    ("连续两年", "国家奖学金"),
    ("92.3 分", "地震勘探课程均分"),
    ("班级第二", "专业成绩 & 综合测评"),
    ("1 篇在投", "研究论文"),
]

# 奖项数据：(展示名, 类别, 级别, 文件名)
AWARDS = [
    ("2024 年国家奖学金",                              "奖学金",   "国家级",   "2024年国家奖学金.jpg"),
    ("2025 年国家奖学金（公示证明）",                   "奖学金",   "国家级",   "2025年国家奖学金公示证明.jpg"),
    ("2024 年中国海洋大学学习优秀一等奖学金",           "奖学金",   "校级",     "2024年中国海洋大学学习优秀一等奖学金.jpg"),
    ("2025 年中国海洋大学学习优秀一等奖学金",           "奖学金",   "校级",     "2025年中国海洋大学学习优秀一等奖学金.jpg"),
    ("2024 年中国海洋大学优秀学生",                    "综合荣誉", "校级",     "2024年中国海洋大学优秀学生.jpg"),
    ("2025 年中国海洋大学优秀学生",                    "综合荣誉", "校级",     "2025年中国海洋大学优秀学生.jpg"),
    ("2024 年中国海洋大学优秀学生干部",                "综合荣誉", "校级",     "2024年中国海洋大学优秀学生干部.jpg"),
    ("2025 年中国海洋大学优秀学生干部",                "综合荣誉", "校级",     "2025年中国海洋大学优秀学生干部.jpg"),
    ("2025 年中国海洋大学优秀共青团干部",              "综合荣誉", "校级",     "2025年中国海洋大学优秀共青团干部.jpg"),
    ("2025 年中国海洋大学助学公益之星",               "综合荣誉", "校级",     "2025年中国海洋大学助学公益之星.jpg"),
    ("2024 年大学生地质技能及地学知识竞赛二等奖",       "学科竞赛", "校级",     "2024年中国海洋大学大学生地质技能及地学知识竞赛二等奖.jpg"),
    ("第三届全国大学生数据分析科普竞赛一等奖",          "学科竞赛", "全国",     "2024年第三届全国大学生数据分析科普竞赛一等奖.jpg"),
    ("全国大学生英语翻译大赛省级三等奖",               "学科竞赛", "省级",     "2024年全国大学生英语翻译大赛省级三等奖.jpg"),
    ("UNESCO 世界地质公园科普志愿者训练营最佳媒体奖",   "社会实践", "国际平台", "2025年UNESCO世界地质公园科普志愿者训练营最佳媒体奖.jpg"),
    ("海洋地球科学学院青春榜样·创新创业榜样",          "综合荣誉", "院级",     "2025年海洋地球科学学院青春榜样人物创新创业榜样名单.jpg"),
    ("2024 年山东省三下乡社会实践优秀学生",            "社会实践", "省级",     "2024年山东省三下乡社会实践优秀学生名单.jpg"),
    ("2024 年中国海洋大学优秀实践个人",               "社会实践", "校级",     "2024年中国海洋大学优秀实践个人名单.jpg"),
    ("2025 年枣庄市大学生暑期社会实践优秀调研报告三等奖","社会实践","市级",    "2025年枣庄市大学生暑期社会实践优秀调研报告三等奖.jpg"),
    ("第二十一届杰出青年志愿者",                      "志愿服务", "校级",     "第二十一届杰出青年志愿者名单.jpg"),
    ("2025 年中国海洋大学青马工程第 81 期优秀学员",    "综合荣誉", "校级",     "2025年中国海洋大学青马工程第81期优秀学员.jpg"),
]

# 科研成果图
PROJECT_FIGURES = [
    ("网络整体结构",       "network_structure.png",  "三通道地震输入 · 物理正演闭环 · 稀疏井低频先验"),
    ("低频先验构建",       "lowfreq_prior.png",       "用约 0.8% 的稀疏井道恢复宏观趋势"),
    ("反演结果对比",       "inversion_result.png",    "参考阻抗 vs 预测阻抗 vs 低频背景（同色标）"),
    ("残差与绝对误差",     "residual_error.png",      "从空间分布角度评估预测误差与地质结构吻合程度"),
    ("指标统计",          "metric_statistics.png",    "R²=0.9731 · RMSE=0.0783 · MAE=0.0533 · Bias=−0.0082"),
]

QT_FIGURES = [
    ("数据增强与物理参数配置界面", "qt_preprocess_augment.png"),
    ("功能总览与脚本调用流程",    "qt_workflow.png"),
]

# ══════════════════════════════════════════════════════════════
#  CSS（统一变量 + 组件样式）
# ══════════════════════════════════════════════════════════════

def inject_css() -> None:
    st.markdown("""
<style>
/* ── 全局变量 ── */
:root {
  --teal:    #0e7490;
  --teal-lt: #e0f2fe;
  --ink:     #0f1e2a;
  --muted:   #516070;
  --border:  #d9e4ea;
  --bg:      #f4f7fa;
  --white:   #ffffff;
  --gold:    #b45309;
  --gold-lt: #fef9ee;
  --red-lt:  #fdf2f2;
}

/* ── 页面背景 ── */
.stApp { background: var(--bg); color: var(--ink); }
.block-container { max-width: 1080px; padding: 1.6rem 1.4rem 4rem; }
[data-testid="stHeader"] { background: transparent; }
[data-testid="stSidebar"] { display: none; }

/* ── Tab 美化 ── */
[data-testid="stTabs"] button {
  font-size: 1.02rem !important;
  font-weight: 600 !important;
  color: var(--muted) !important;
}
[data-testid="stTabs"] button[aria-selected="true"] {
  color: var(--teal) !important;
  border-bottom: 3px solid var(--teal) !important;
}

/* ── Hero ── */
.hero-wrap {
  background: var(--white);
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 2rem 2.2rem 1.6rem;
  margin-bottom: 1.4rem;
}
.hero-eyebrow {
  color: var(--teal);
  font-weight: 800;
  font-size: .88rem;
  letter-spacing: .06em;
  text-transform: uppercase;
  margin-bottom: .5rem;
}
.hero-name {
  font-size: clamp(2rem, 5vw, 3.4rem);
  font-weight: 900;
  color: var(--ink);
  line-height: 1.08;
  margin: 0 0 .6rem;
}
.hero-sub {
  color: var(--muted);
  font-size: 1.04rem;
  line-height: 1.75;
  margin-bottom: 1.2rem;
}
.hero-commit {
  background: var(--teal-lt);
  border-left: 4px solid var(--teal);
  border-radius: 6px;
  padding: .65rem 1rem;
  color: #0c4a5e;
  font-size: .95rem;
  font-weight: 600;
  margin-top: .8rem;
}

/* ── 数字卡片 ── */
.stat-row {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: .85rem;
  margin-bottom: 1.4rem;
}
.stat-card {
  background: var(--white);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 1rem 1.2rem;
  text-align: center;
}
.stat-num {
  font-size: 1.75rem;
  font-weight: 900;
  color: var(--teal);
  line-height: 1.15;
}
.stat-label {
  font-size: .82rem;
  color: var(--muted);
  margin-top: .25rem;
}

/* ── 申请信 ── */
.letter-wrap {
  background: var(--white);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 2rem 2.4rem 2.2rem;
  line-height: 1.9;
  color: #222e38;
}
.letter-wrap h3 {
  font-size: 1.08rem;
  color: var(--teal);
  margin: 1.6rem 0 .3rem;
  border-bottom: 1px solid var(--border);
  padding-bottom: .3rem;
}
.letter-wrap p { margin: .5rem 0 .85rem; }
.letter-wrap b { color: var(--ink); }

/* ── 金色强调引用 ── */
.callout-gold {
  background: var(--gold-lt);
  border-left: 4px solid var(--gold);
  border-radius: 6px;
  padding: .75rem 1.1rem;
  color: #5c3b0c;
  margin: 1rem 0;
  font-weight: 600;
  font-size: .97rem;
  line-height: 1.7;
}
.callout-teal {
  background: var(--teal-lt);
  border-left: 4px solid var(--teal);
  border-radius: 6px;
  padding: .75rem 1.1rem;
  color: #0c4a5e;
  margin: 1rem 0;
  font-size: .97rem;
  line-height: 1.7;
}

/* ── 能力卡片 ── */
.cap-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: .85rem;
  margin-top: 1rem;
}
.cap-card {
  background: var(--white);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 1rem 1.1rem;
}
.cap-card .cap-icon { font-size: 1.4rem; margin-bottom: .4rem; }
.cap-card .cap-title { font-weight: 700; font-size: .97rem; margin-bottom: .35rem; }
.cap-card .cap-body { color: var(--muted); font-size: .88rem; line-height: 1.62; }

/* ── 研究卡片 ── */
.research-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: .85rem;
  margin-bottom: 1.4rem;
}
.research-card {
  background: var(--white);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 1.1rem 1.2rem;
}
.research-card .tag {
  display: inline-block;
  background: var(--teal-lt);
  color: var(--teal);
  font-size: .78rem;
  font-weight: 700;
  padding: .15rem .6rem;
  border-radius: 999px;
  margin-bottom: .6rem;
}
.research-card h4 { margin: 0 0 .5rem; font-size: 1rem; }
.research-card p  { color: var(--muted); font-size: .9rem; line-height: 1.65; margin: 0; }

/* ── section 标题 ── */
.sec-hd {
  border-top: 1px solid var(--border);
  margin: 1.8rem 0 1rem;
  padding-top: .9rem;
}
.sec-hd h2 { margin: 0 0 .2rem; font-size: 1.3rem; }
.sec-hd p  { color: var(--muted); margin: 0; font-size: .9rem; }

/* ── pill 标签 ── */
.pill {
  display: inline-block;
  padding: .12rem .5rem;
  border: 1px solid var(--border);
  border-radius: 999px;
  font-size: .78rem;
  color: var(--muted);
  margin-right: .3rem;
  margin-bottom: .2rem;
}

/* ── 图片 ── */
div[data-testid="stImage"] img {
  border: 1px solid var(--border);
  border-radius: 8px;
  width: 100%;
}

/* ── 注意 ── */
.notice {
  background: #f8f4ff;
  border: 1px solid #d5c9f0;
  border-radius: 8px;
  padding: .85rem 1rem;
  color: #4a3870;
  font-size: .88rem;
  line-height: 1.65;
}

/* 响应式 */
@media (max-width: 760px) {
  .stat-row     { grid-template-columns: repeat(2, 1fr); }
  .cap-grid     { grid-template-columns: 1fr; }
  .research-grid{ grid-template-columns: 1fr; }
  .letter-wrap  { padding: 1.2rem 1rem; }
}
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
#  工具函数
# ══════════════════════════════════════════════════════════════

def img(path: Path, caption: str = "", width: int = None) -> None:
    if path.exists():
        kwargs = {"use_container_width": True}
        if caption:
            kwargs["caption"] = caption
        st.image(str(path), **kwargs)
    else:
        st.caption(f"⚠ 图片待上传：`{path.name}`")


def sec(title: str, desc: str = "") -> None:
    st.markdown(
        f'<div class="sec-hd"><h2>{title}</h2>'
        + (f'<p>{desc}</p>' if desc else '')
        + '</div>',
        unsafe_allow_html=True,
    )


def show_pdf(path: Path, height: int = 680) -> None:
    """在页面内嵌显示 PDF，同时提供下载按钮。"""
    if not path.exists():
        st.caption(f"⚠ 文件待上传：`{path.name}`")
        return
    raw = path.read_bytes()
    b64 = base64.b64encode(raw).decode()
    st.markdown(
        f'<iframe src="data:application/pdf;base64,{b64}" '
        f'width="100%" height="{height}px" '
        f'style="border:1px solid #d9e4ea;border-radius:8px;"></iframe>',
        unsafe_allow_html=True,
    )
    st.download_button(
        label=f"⬇ 下载 {path.name}",
        data=raw,
        file_name=path.name,
        mime="application/pdf",
        use_container_width=False,
    )


# ══════════════════════════════════════════════════════════════
#  Hero
# ══════════════════════════════════════════════════════════════

def render_hero() -> None:
    # 数字统计行
    stat_html = "".join(
        f'<div class="stat-card"><div class="stat-num">{n}</div>'
        f'<div class="stat-label">{l}</div></div>'
        for n, l in STATS
    )
    st.markdown(f'<div class="stat-row">{stat_html}</div>', unsafe_allow_html=True)

    # 主卡片
    st.markdown("""
<div class="hero-wrap">
  <div class="hero-eyebrow">中国海洋大学 · 勘查技术与工程</div>
  <div class="hero-name">潘高</div>
  <div class="hero-sub">
    诚挚申请攻读 <b>陆文凯老师</b> 的硕士研究生，希望跟随您从事
    <b>人工智能与地球物理反演</b>方向的科研工作。<br>
    本页以申请信为主线，将研究方向、已有成果与支撑材料集中呈现，方便老师快速审阅。
  </div>
  <div class="hero-commit">
    ✦ 入组承诺：若获认可，不再参加其他任何院校夏令营考核，从暑假起全程留京，随时投入课题组科研工作。
  </div>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
#  Tab 1 · 申请信
# ══════════════════════════════════════════════════════════════

def render_letter() -> None:
    st.markdown("""
<div class="letter-wrap">
<p><b>尊敬的陆文凯老师：</b></p>
<p>您好！冒昧打扰您百忙之中的宝贵时间。我是中国海洋大学勘查技术与工程专业学生潘高，此次致信，诚挚申请希望能有机会攻读您的硕士研究生，跟随您从事人工智能与地球物理反演方向的科研工作。</p>

<h3>一、为什么选择您</h3>
<p>我的科研兴趣主要聚焦于<b>地震正演与反演、地震资料处理与解释、人工智能地球物理</b>，以及深度学习/机器学习驱动的智能反演方法，重点探索物理机理约束与数据驱动模型相结合的地震反演新方法。</p>
<div class="callout-gold">
我重点关注到您基于 CycleGAN 及神经网络开展的地球物理反演相关工作——这也是我目前科研工作的重要起点：我已在您相关研究成果基础上完成模型复现，并在此之上开展了自己的创新与改进工作。正因研究方向高度契合，我坚定将您作为首要意向导师。
</div>

<h3>二、入组承诺</h3>
<div class="callout-teal">
若能有幸得到您的认可与接纳，我将<b>不再参加其他任何院校的夏令营考核</b>；愿意从这个暑假开始，直至大四整个学年，<b>全程留在北京</b>跟进课题组科研任务，随时听从老师和组里安排，提前进组适应节奏、投入科研工作。
</div>

<h3>三、进组后我能做什么</h3>
<p>关于科研规划，我完全服从课题组整体安排。您身处自动化专业，课题组横向项目与应用类课题资源丰富，若有横向项目或工程类任务，我会踏实跟进、认真完成；若老师有新的前沿研究思路，我也会积极跟进落地实现；同时，我自身已具备较成熟的研究思路与完整创新 idea，可自主开展既定方向研究——<b>既能配合组里任务，也有可持续深耕的科研内容</b>。</p>

<h3>四、专业基础与工程能力</h3>
<p>地震勘探方向相关专业课<b>均分 92.3 分</b>，专业成绩与综合测评均位列<b>班级第二</b>；连续两年获评<b>国家奖学金</b>、学习优秀一等奖学金等荣誉；曾以队长身份带领团队斩获校级地球物理知识技能竞赛<b>特等奖</b>，并将于 5 月底带队赴中国石油大学（华东）参加全国创新杯决赛。</p>
<p>目前担任中国海洋大学地源地震资料处理实验室助理，熟练掌握 <b>GeoEast、Jason</b> 等主流地球物理处理与反演专业软件，能够独立构建科研初始模型，入组即可上手相关实验工作。凭借扎实的地球物理专业功底，可与您课题组自动化算法方向形成良好互补。</p>

<h3>五、科研自研与工程化能力</h3>
<p>我已形成较成熟的科研工作模式：熟练使用 <b>Streamlit、Qt</b> 搭建标准化工作流，可对算法与模型进行网页端、客户端封装；自建"人工智能 + 文献论文 + GitHub 源码"闭环学习复现体系，能够快速精读文献、复现代码、迭代实验方案；借助 AI 工具自主编写脚本，实现参数寻优、批量实验等流程自动化。熟悉<b>软件著作权</b>全流程申报，可随时协助课题组完成软著申请、材料整理与提交。</p>

<h3>六、核心科研方向</h3>
<p>本科阶段牵头省级大学生创新创业训练计划项目《基于 CycleGAN 与物理约束的地震反演方法研究》，目前已有<b>一篇研究论文在投</b>。</p>
<p>在复现经典双生成器、双判别器架构的基础上，我做出核心创新：</p>
<ul>
  <li>将其中一个生成器替换为<b>确定性地球物理正演模型</b>，把物理正演先验作为强约束直接嵌入网络结构；</li>
  <li>引入 <b>PINN 物理信息约束</b>；</li>
  <li>将网络输入优化为<b>分层多尺度输入</b>，创新设计低频、中频、高频三分量独立生成架构；</li>
  <li>引入<b>稀疏井约束</b>，借助确定性反演结果构建伪标签辅助训练。</li>
</ul>
<p>该研究整体具备良好物理可解释性，思路逻辑贴近 MCMC 等传统贝叶斯反演流程。后续还可灵活嵌入 <b>diffusion 模型</b>，针对多尺度、多频段反演做进一步优化拓展，具备充足的延伸空间。</p>

<h3>七、附加能力</h3>
<p>具备成熟 PPT 制作与项目汇报答辩经验，可承担组内成果汇报、项目申报等材料制作。业余<b>爱好摄影</b>并自备专业设备，作品曾刊发于学习强国、人民日报、中国青年报等主流平台，若组内有学术会议或大型活动拍摄需求，可随时志愿配合。</p>

<h3>八、结语</h3>
<p>本科阶段承蒙<b>张会星老师</b>悉心指导，我逐渐养成了严谨踏实、能吃苦肯投入的科研态度。十分敬佩您在人工智能、神经网络算法与地球物理反演交叉方向的学术积累与工程实践视野，真心渴望能加入您的课题组，把自身专业基础、代码能力与已有研究思路充分发挥，踏实跟随您求学科研。</p>
<p>随信附上个人简历、成绩单、竞赛获奖证书等相关材料，恳请老师在百忙之中抽空审阅。无论结果如何，都由衷感谢老师拨冗阅读，期待能有机会得到您的指点与接纳！</p>
<p style="margin-top:1.5rem;">此致 敬礼！<br><b>申请人：潘高</b><br><span style="color:#516070;">2026 年 5 月 11 日</span></p>
</div>
""", unsafe_allow_html=True)


def render_capabilities() -> None:
    sec("六大支撑能力", "申请信中每一项承诺的具体依据")
    caps = [
        ("📐", "专业基础",     "地震勘探相关课程均分 92.3 分，专业成绩与综合测评均位列班级第二，专业知识体系扎实完备。"),
        ("🖥", "专业软件",     "担任地源地震资料处理实验室助理，熟悉 GeoEast、Jason 等主流处理与反演软件，入组即可上手。"),
        ("⚙️", "工程封装",    "熟练使用 Streamlit、Qt 搭建标准化工作流，能把算法封装为可复用的网页端或客户端工具。"),
        ("🔁", "复现能力",     "自建「AI + 文献 + GitHub」闭环学习体系，能快速精读文献、复现代码、迭代实验。"),
        ("📋", "成果固化",     "熟悉软件著作权全流程申报，可随时协助课题组完成软著申请、材料整理与横向项目结题。"),
        ("🎤", "表达与记录",   "具备成熟 PPT 制作与答辩经验；摄影作品曾刊发于人民日报、中国青年报等主流平台。"),
    ]
    html = "".join(
        f'<div class="cap-card">'
        f'<div class="cap-icon">{icon}</div>'
        f'<div class="cap-title">{title}</div>'
        f'<div class="cap-body">{body}</div>'
        f'</div>'
        for icon, title, body in caps
    )
    st.markdown(f'<div class="cap-grid">{html}</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
#  Tab 2 · 科研成果
# ══════════════════════════════════════════════════════════════

def render_research() -> None:
    sec("核心研究 idea", "把申请信中最关键的科研想法独立展开，让老师看到研究潜力而不只是奖项列表。")
    items = [
        ("核心问题",         "地震反演非唯一性 / 低频缺失 / 物理一致性不足",
         "面向地震数据到阻抗模型反演中的非唯一性、低频信息缺失和深度学习结果物理一致性不足等问题，"
         "牵头省级大创项目《基于 CycleGAN 与物理约束的地震反演方法研究》。"),
        ("主要创新",         "固定正演算子 · PINN 约束 · 多尺度多频段生成架构",
         "将双生成器之一替换为确定性 Ricker 物理正演模型，把正演先验作为强约束嵌入；"
         "同时引入稀疏井低频先验与多尺度分频独立生成架构（低频/中频/高频三分量）。"),
        ("后续拓展",         "Diffusion · 多频段 · 不确定性评价",
         "路线具备良好物理可解释性，可平滑嵌入 diffusion 等生成模型，"
         "进一步探索多尺度反演与不确定性定量评价，具备充足延伸空间。"),
    ]
    html = "".join(
        f'<div class="research-card">'
        f'<span class="tag">{tag}</span>'
        f'<h4>{title}</h4>'
        f'<p>{body}</p>'
        f'</div>'
        for title, tag, body in items
    )
    st.markdown(f'<div class="research-grid">{html}</div>', unsafe_allow_html=True)

    sec("网络结构与初步成果图", "模型结构、低频先验、反演结果与误差指标作为科研叙事的图示佐证。")
    for i in range(0, len(PROJECT_FIGURES), 2):
        cols = st.columns(2)
        for col, (title, fname, desc) in zip(cols, PROJECT_FIGURES[i:i+2]):
            with col:
                st.markdown(f"**{title}**")
                st.caption(desc)
                img(PROJECT_DIR / fname)

    sec("Qt 封装的 CycleGAN 预处理系统",
        "证明我不只是调模型——也能把科研流程封装为可复用工具，降低实验返工成本。")
    st.markdown("""
<div class="callout-teal">
该系统围绕 CycleGAN 矩形训练流水线封装，覆盖 SEGY 重采样、正演模拟、传统反演接入、
数据增强、矩形切割、模型推理、结果合并以及日志状态管理等模块，
把原本分散在多个脚本中的处理步骤整合为可视化流程。
</div>
""", unsafe_allow_html=True)
    cols = st.columns(2)
    for col, (title, fname) in zip(cols, QT_FIGURES):
        with col:
            st.markdown(f"**{title}**")
            img(PROJECT_DIR / fname)

    sec("专利受理与创新项目证明", "作为补充证明，不喧宾夺主。")
    patent_items = [
        (RESEARCH_DIR / "c64e68a0c8a14cc07a8392f526b93c17.jpg", "专利受理：一种立体式型材存取库"),
        (RESEARCH_DIR / "c953f46a69869bc630e740cf7725bbe8.jpg", "专利受理：一种立体式板材存放架"),
        (RESEARCH_DIR / "图片2.png",                            "省级大创项目立项证明"),
        (RESEARCH_DIR / "innovation_project.png",               "创新创业项目材料"),
    ]
    for i in range(0, len(patent_items), 2):
        cols = st.columns(2)
        for col, (path, caption) in zip(cols, patent_items[i:i+2]):
            with col:
                img(path, caption)


# ══════════════════════════════════════════════════════════════
#  Tab 3 · 荣誉证明
# ══════════════════════════════════════════════════════════════

def render_honors() -> None:
    sec("学业荣誉摘要", "以下为申请表中的关键荣誉，原表含敏感信息不公开展示，如需核验请见正式附件材料。")

    summary_groups = [
        ("奖学金", [
            "2024、2025 年 国家奖学金",
            "2024、2025 年 中国海洋大学学习优秀一等奖学金",
        ]),
        ("综合荣誉", [
            "2024、2025 年 优秀学生 / 优秀学生干部",
            "2025 年 优秀共青团干部 / 助学公益之星",
            "第二十一届杰出青年志愿者",
        ]),
        ("学科竞赛", [
            "全国大学生数据分析科普竞赛 一等奖",
            "挑战杯创业计划竞赛 校级金奖（推省）",
            "全国创新杯地震勘探竞赛 决赛队长",
            "校级地球物理竞赛 特等奖",
        ]),
        ("社会实践", [
            "UNESCO 世界地质公园科普志愿者训练营 最佳媒体奖",
            "山东省三下乡社会实践 优秀学生",
            "海洋地球科学学院 创新创业榜样",
        ]),
    ]
    cols = st.columns(4)
    for col, (group, items) in zip(cols, summary_groups):
        with col:
            st.markdown(f"**{group}**")
            for item in items:
                st.markdown(f"- {item}")

    st.markdown('<div class="notice">说明：申请表原件含身份证号、电话、邮箱、住址、照片等敏感信息，公开网页不展示原图。如老师需要核验，可在正式申请材料附件中查看原表及证书扫描件。</div>',
                unsafe_allow_html=True)

    sec("奖项证书图集", "可按类别与级别筛选。")
    categories = ["全部"] + sorted({a[1] for a in AWARDS})
    levels     = ["全部"] + sorted({a[2] for a in AWARDS})
    c1, c2 = st.columns(2)
    cat = c1.selectbox("类别", categories)
    lvl = c2.selectbox("级别", levels)
    filtered = [a for a in AWARDS
                if (cat == "全部" or a[1] == cat)
                and (lvl == "全部" or a[2] == lvl)]
    st.caption(f"当前展示 {len(filtered)} 项")

    for i in range(0, len(filtered), 3):
        cols = st.columns(3)
        for col, (title, cat_, lvl_, fname) in zip(cols, filtered[i:i+3]):
            with col:
                st.markdown(
                    f'<span class="pill">{cat_}</span>'
                    f'<span class="pill">{lvl_}</span>',
                    unsafe_allow_html=True,
                )
                st.markdown(f"**{title}**")
                img(AWARD_DIR / fname)


# ══════════════════════════════════════════════════════════════
#  Tab 4 · 成绩材料
# ══════════════════════════════════════════════════════════════

def render_scores() -> None:
    sec("专业课成绩单 & 排名证明",
        "前两年半完整成绩单 + 学习成绩排名证明，可在线预览或下载原件。")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 前两年半成绩单")
        show_pdf(SCORES_DIR / "transcript.pdf", height=700)
    with col2:
        st.markdown("#### 学习成绩排名证明")
        show_pdf(SCORES_DIR / "ranking.pdf", height=700)

    sec("英语四六级成绩",
        "CET-4 / CET-6 官方成绩单及学校出具的四六级成绩证明。")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("#### CET-4 官方成绩单")
        show_pdf(SCORES_DIR / "CET4.pdf", height=580)
    with col2:
        st.markdown("#### CET-6 官方成绩单")
        show_pdf(SCORES_DIR / "CET6.pdf", height=580)
    with col3:
        st.markdown("#### 学校四六级成绩证明")
        show_pdf(SCORES_DIR / "english_cert.pdf", height=580)


# ══════════════════════════════════════════════════════════════
#  主函数
# ══════════════════════════════════════════════════════════════

def main() -> None:
    st.set_page_config(
        page_title="潘高 · 致陆文凯老师的硕士申请",
        page_icon="📄",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    inject_css()
    render_hero()

    tab1, tab2, tab3, tab4 = st.tabs(["📄 申请信", "🔬 科研成果", "🏆 荣誉证明", "📊 成绩材料"])

    with tab1:
        render_letter()
        render_capabilities()

    with tab2:
        render_research()

    with tab3:
        render_honors()

    with tab4:
        render_scores()

    st.markdown("---")
    st.markdown(
        '<div class="notice">📎 公开边界：本页只展示适合公开的科研、封装系统、奖项与荣誉材料。'
        '身份证、学生证、完整成绩单、四六级等敏感材料不放入公开仓库，请作为私下附件提交。</div>',
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
