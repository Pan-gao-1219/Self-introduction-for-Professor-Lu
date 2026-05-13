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
    ("552 / 522", "CET-4 / CET-6"),
    ("92.3 分", "地震勘探课程均分"),
    ("1 / 14", "卓越班排名（含普通班综合 2 / 49）"),
]

# ── 高含金量奖项（详细介绍，独立展示）──
# 每项：icon, 标题, 年份, 级别标签, 含金量说明, [证书文件名列表]
HIGHLIGHT_AWARDS = [
    (
        "🏆",
        "国家奖学金（连续两年）",
        "2024 · 2025",
        "国家级",
        "由教育部直接颁发，是本科阶段可获得的<b>国家最高级别奖学金</b>，全国高校评定比例约 0.2%，须学业成绩与综合素质均位居全校顶尖方可入选。所在专业同年级共 49 人（卓越工程师班 14 人 + 普通班 35 人），<b>跨班综合学习成绩排名第 2 / 49，卓越班内排名第 1 / 14</b>，方具推荐资格。连续两年均通过认定，说明本科阶段始终保持顶尖水准，而非偶发性发挥。",
        ["2024年国家奖学金.jpg", "2025年国家奖学金公示证明.jpg", "2025年国家奖学金_cert.jpg"],
    ),
    (
        "🥇",
        "第三届全国大学生数据分析科普竞赛 一等奖",
        "2024 年 11 月",
        "全国",
        "全国性学科竞赛，面向全国高校本科生，赛题综合考核<b>统计分析、数据可视化与科学传播</b>能力。全国参赛团队逾千支，<b>各赛区合计一等奖获奖比例约 3%—5%</b>，含金量显著高于省赛奖项。体现跨学科数据处理与展示能力，与人工智能及地球物理反演方向的综合实践能力直接挂钩。",
        ["2024年第三届全国大学生数据分析科普竞赛一等奖.jpg"],
    ),
    (
        "🌍",
        "UNESCO 世界地质公园科普志愿者训练营 最佳媒体奖",
        "2025 年 7 月",
        "国际平台",
        "由 <b>UNESCO（联合国教科文组织）</b>认可的世界地质公园体系主办，面向全国高校优选参营，最佳媒体奖是营内最高单项荣誉之一，评选综合考量<b>科普策划、摄影记录与媒体传播</b>综合能力，代表在国际科学传播场景下的突出表现。",
        ["2025年UNESCO世界地质公园科普志愿者训练营最佳媒体奖.jpg"],
    ),
    (
        "🌐",
        "全国大学生英语翻译大赛 省级三等奖",
        "2024 年 3 月",
        "省级",
        "全国性英语类学科竞赛，分省赛道评选，省级获奖代表在全省英语综合实力处于较高水平。对于从事人工智能与地球物理交叉研究方向的研究生而言，<b>阅读英文文献、撰写英文论文</b>是日常工作基础，该成绩对此有直接佐证意义。",
        ["2024年全国大学生英语翻译大赛省级三等奖.jpg"],
    ),
    (
        "🔬",
        "大学生地质技能及地学知识竞赛 二等奖",
        "2024 年 4 月",
        "校级专业赛",
        "由中国海洋大学主办，考核<b>地质野外技能、地球物理理论与实践操作</b>，是勘查技术与工程专业最核心的专业竞赛，获奖代表专业技能处于全校前列。以<b>队长身份</b>带队参赛，体现了专业领导力与团队协作能力，同时积累了后续参加全国创新杯决赛的竞赛经验。",
        ["2024年中国海洋大学大学生地质技能及地学知识竞赛二等奖.jpg"],
    ),
    (
        "✨",
        "海洋地球科学学院青春榜样人物 · 创新创业榜样",
        "2025 年 11 月",
        "院级最高荣誉",
        "学院年度评选的个人最高荣誉之一，专门表彰在<b>创新创业领域取得突出成绩</b>的学生，<b>全院仅两人获评（含硕博研究生）</b>，入选须在创新项目、竞赛获奖或成果落地方面有具体贡献。该荣誉是对省级大创项目、竞赛获奖、软著申请等一系列成果的综合认定，也是课题组跨学科合作潜力的有力背书。",
        ["2025年海洋地球科学学院青春榜样人物创新创业榜样名单.jpg"],
    ),
]

# ── 全量奖项证书（可筛选图集）──
AWARDS = [
    ("2024 年国家奖学金",                               "奖学金",   "国家级",   "2024年国家奖学金.jpg"),
    ("2025 年国家奖学金公示证明",                        "奖学金",   "国家级",   "2025年国家奖学金公示证明.jpg"),
    ("2025 年国家奖学金证书",                            "奖学金",   "国家级",   "2025年国家奖学金_cert.jpg"),
    ("2024 年学习优秀一等奖学金",                        "奖学金",   "校级",     "2024年中国海洋大学学习优秀一等奖学金.jpg"),
    ("2025 年学习优秀一等奖学金",                        "奖学金",   "校级",     "2025年中国海洋大学学习优秀一等奖学金.jpg"),
    ("第三届全国大学生数据分析科普竞赛一等奖",            "学科竞赛", "全国",     "2024年第三届全国大学生数据分析科普竞赛一等奖.jpg"),
    ("全国大学生英语翻译大赛省级三等奖",                  "学科竞赛", "省级",     "2024年全国大学生英语翻译大赛省级三等奖.jpg"),
    ("大学生地质技能及地学知识竞赛二等奖",                "学科竞赛", "校级",     "2024年中国海洋大学大学生地质技能及地学知识竞赛二等奖.jpg"),
    ("中国海洋大学地球物理知识竞赛特等奖",              "学科竞赛", "校级",     ""),
    ("UNESCO 世界地质公园科普志愿者训练营最佳媒体奖",     "社会实践", "国际平台", "2025年UNESCO世界地质公园科普志愿者训练营最佳媒体奖.jpg"),
    ("海洋地球科学学院青春榜样·创新创业榜样",            "综合荣誉", "院级",     "2025年海洋地球科学学院青春榜样人物创新创业榜样名单.jpg"),
    ("2024 年优秀学生",                                 "综合荣誉", "校级",     "2024年中国海洋大学优秀学生.jpg"),
    ("2025 年优秀学生",                                 "综合荣誉", "校级",     "2025年中国海洋大学优秀学生.jpg"),
    ("2024 年优秀学生干部",                             "综合荣誉", "校级",     "2024年中国海洋大学优秀学生干部.jpg"),
    ("2025 年优秀学生干部",                             "综合荣誉", "校级",     "2025年中国海洋大学优秀学生干部.jpg"),
    ("2025 年优秀共青团干部",                           "综合荣誉", "校级",     "2025年中国海洋大学优秀共青团干部.jpg"),
    ("2025 年助学公益之星",                             "综合荣誉", "校级",     "2025年中国海洋大学助学公益之星.jpg"),
    ("2025 年青马工程第 81 期优秀学员（全院一人）",       "综合荣誉", "校级",     "2025年中国海洋大学青马工程第81期优秀学员.jpg"),
    ("2025-2026 学年学生会标兵分会（全校 3 个）",        "综合荣誉", "校级",     "2025-2026学年学生会标兵分会优秀分会.jpg"),
    ("第二十一届杰出青年志愿者（全校 10 人含硕博）",     "志愿服务", "校级",     "第二十一届杰出青年志愿者名单.jpg"),
    ("青年志愿服务先进集体（全校 10 个）",              "志愿服务", "校级",     "青年志愿服务先进集体名单.jpg"),
    ("青鸟计划枣聚英才青鸟驿站站长",                    "社会实践", "省级平台", "青鸟计划枣聚英才青鸟驿站站长聘书.jpg"),
    ("2024 年山东省三下乡社会实践优秀学生",              "社会实践", "省级",     "2024年山东省三下乡社会实践优秀学生名单.png"),
    ("2024 年优秀实践个人",                             "社会实践", "校级",     "2024年中国海洋大学优秀实践个人名单.jpg"),
    ("2025 年枣庄市暑期社会实践优秀调研报告三等奖",       "社会实践", "市级",     "2025年枣庄市大学生暑期社会实践优秀调研报告三等奖.jpg"),
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

/* ── 重点奖项卡片 ── */
.highlight-card {
  background: var(--white);
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 1.4rem 1.8rem 1.2rem;
  margin-bottom: 1.2rem;
}
.highlight-card-header {
  display: flex;
  align-items: flex-start;
  gap: .9rem;
  margin-bottom: .75rem;
}
.ha-icon {
  font-size: 2rem;
  line-height: 1;
  flex-shrink: 0;
  padding-top: .15rem;
}
.ha-title-block { flex: 1; }
.ha-title {
  font-size: 1.1rem;
  font-weight: 800;
  color: var(--ink);
  margin: 0 0 .3rem;
}
.ha-meta {
  display: flex;
  align-items: center;
  gap: .5rem;
  flex-wrap: wrap;
}
.ha-year { color: var(--muted); font-size: .88rem; }
.ha-badge {
  display: inline-block;
  padding: .1rem .55rem;
  border-radius: 999px;
  font-size: .78rem;
  font-weight: 700;
}
.ha-badge-nation { background: #fef3c7; color: #92400e; border: 1px solid #fcd34d; }
.ha-badge-intl   { background: #d1fae5; color: #065f46; border: 1px solid #6ee7b7; }
.ha-badge-prov   { background: #dbeafe; color: #1e3a8a; border: 1px solid #93c5fd; }
.ha-badge-school { background: #f3e8ff; color: #5b21b6; border: 1px solid #c4b5fd; }
.ha-desc {
  font-size: .91rem;
  color: #374151;
  line-height: 1.78;
  border-left: 3px solid var(--teal-lt);
  padding-left: 1rem;
  margin-bottom: 1rem;
}

/* ── 页面导航 Tab 栏 ── */
.page-nav {
  position: sticky;
  top: 0;
  z-index: 100;
  background: var(--white);
  border: 1px solid var(--border);
  border-radius: 12px;
  display: flex;
  margin-bottom: 1.8rem;
  overflow: hidden;
  box-shadow: 0 2px 10px rgba(0,0,0,.08);
}
.page-nav a {
  flex: 1;
  padding: 1.1rem .5rem;
  text-align: center;
  font-size: 1.08rem;
  font-weight: 700;
  color: var(--muted);
  text-decoration: none !important;
  border-right: 1px solid var(--border);
  transition: background .15s, color .15s;
  letter-spacing: .01em;
}
.page-nav a:last-child { border-right: none; }
.page-nav a:hover {
  background: var(--teal-lt);
  color: var(--teal);
}

/* 响应式 */
@media (max-width: 760px) {
  .stat-row     { grid-template-columns: repeat(2, 1fr); }
  .cap-grid     { grid-template-columns: 1fr; }
  .research-grid{ grid-template-columns: 1fr; }
  .letter-wrap  { padding: 1.2rem 1rem; }
  .page-nav a   { font-size: .88rem; padding: .9rem .3rem; }
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

    # 照片 + 二维码 base64
    import base64 as _b64
    photo_path = ROOT / "assets" / "photo.jpg"
    qr_path    = ROOT / "assets" / "qr.png"
    photo_html = ""
    if photo_path.exists():
        photo_b64 = _b64.b64encode(photo_path.read_bytes()).decode()
        photo_html = (
            f'<div style="flex-shrink:0;text-align:center;padding-top:.3rem;">'
            f'<img src="data:image/jpeg;base64,{photo_b64}" '
            f'style="width:108px;height:144px;object-fit:cover;border-radius:8px;'
            f'border:1px solid #d9e4ea;">'
            f'<div style="font-size:.78rem;color:#516070;margin-top:.55rem;line-height:1.7;">'
            f'📞&nbsp;18306376923<br>📧&nbsp;1534827320@qq.com'
            f'</div></div>'
        )

    # 主卡片
    st.markdown(f"""
<div class="hero-wrap">
  <div style="display:flex;gap:1.6rem;align-items:flex-start;">
    <div style="flex:1;">
      <div class="hero-eyebrow">中国海洋大学 · 勘查技术与工程</div>
      <div class="hero-name">潘高</div>
      <div class="hero-sub">
        诚挚申请攻读 <b>陆文凯老师</b> 的硕士（博士）研究生，希望跟随您从事
        <b>人工智能与地球物理反演</b>方向的科研工作。
      </div>
      <div class="hero-commit">
        ✦ 入组承诺：若获认可，不再参加其他任何院校夏令营考核，从暑假起全程留京，随时投入课题组科研工作，同时也愿意以直博方式继续深造。
      </div>
    </div>
    {photo_html}
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
我重点关注到您基于 CycleGAN 及神经网络开展的地球物理反演相关工作——这也是我目前科研工作的重要起点：我已在您相关研究成果基础上完成模型复现，并在此之上开展了自己的创新与改进工作。正因研究方向高度契合，我坚定将您作为意向导师。
</div>

<h3>二、入组承诺</h3>
<div class="callout-teal">
若能有幸得到您的认可与接纳，我将<b>不再参加其他任何院校的夏令营考核</b>；愿意从这个暑假开始，直至大四整个学年，<b>全程留在北京</b>跟进课题组科研任务，随时听从老师和组里安排，提前进组适应节奏、投入科研工作。此外，我也愿意以<b>直博</b>方式继续深造，长期专注于本方向的研究。
</div>

<h3>三、进组后我能做什么</h3>
<p>关于科研规划，我完全服从课题组整体安排。若有横向项目或工程类任务，我会踏实跟进、认真完成；若老师有新的前沿研究思路，我也会积极跟进落地实现；同时，我自身已具备较成熟的研究思路与完整创新 idea，可自主开展既定方向研究——<b>既能配合组里任务，也有可持续深耕的科研内容</b>。</p>

<h3>四、专业基础与工程能力</h3>
<p>地震勘探方向相关专业课<b>均分 92.3 分</b>，专业成绩位列<b>卓越工程师班第一、含普通班综合第二</b>；连续两年获评<b>国家奖学金</b>、学习优秀一等奖学金等荣誉；曾以队长身份带领团队斩获校级地球物理知识技能竞赛<b>特等奖</b>，并将于 5 月底带队赴中国石油大学（华东）参加全国创新杯决赛。</p>
<p>目前担任中国海洋大学地源地震资料处理实验室助理，熟练掌握 <b>GeoEast、Jason</b> 等主流地球物理处理与反演专业软件，能够独立构建科研初始模型，入组即可上手相关实验工作。凭借扎实的地球物理专业功底，可与您课题组自动化算法方向形成良好互补。</p>

<h3>五、科研自研与工程化能力</h3>
<ul>
  <li>熟练使用 <b>Streamlit、Qt</b> 搭建标准化工作流，可对算法与模型进行网页端、客户端封装。</li>
  <li>自建"人工智能 + 文献论文 + GitHub 源码"闭环学习复现体系，能够快速精读文献、复现代码、迭代实验方案。</li>
  <li>借助 AI 工具自主编写脚本，实现参数寻优、批量实验等流程自动化。</li>
  <li>熟悉<b>软件著作权</b>全流程申报，可随时协助课题组完成软著申请、材料整理与提交。</li>
</ul>

<h3>六、核心科研方向</h3>
<p>自<b>大二下学期</b>起接触科研，便深度投入其中，牵头省级大学生创新创业训练计划项目《基于 CycleGAN 与物理约束的地震反演方法研究》，目前已有<b>一篇研究论文在投</b>。所有实验在个人独立开展、<b>配备一张 RTX 5060 Ti 显卡</b>的条件下完成，算力有限，但仍取得了较为完整的成果。</p>
<p>在复现经典双生成器、双判别器架构的基础上，我做出核心创新：</p>
<ul>
  <li>将其中一个生成器替换为<b>确定性地球物理正演模型</b>，把物理正演先验作为强约束直接嵌入网络结构；</li>
  <li>引入 <b>PINN 物理信息约束</b>；</li>
  <li>将网络从 <b>1D 扩展到 2D</b>，实现二维空间连续性建模；</li>
  <li>引入<b>稀疏井约束</b>，借助确定性反演结果构建伪标签辅助训练。</li>
</ul>
<p>该研究整体具备良好物理可解释性，思路逻辑贴近 MCMC 等传统贝叶斯反演流程。后续规划引入<b>多尺度分频独立生成架构</b>（低频、中频、高频三分量），并可灵活嵌入 <b>diffusion 模型</b>，针对多尺度、多频段反演做进一步优化拓展。</p>

<h3>七、附加能力</h3>
<ul>
  <li>PPT 制作已达到<b>商业级别</b>，曾为学院年度总结汇报、老师横向项目路演及多次创赛答辩制作全套演示文稿，对信息层次、视觉规范与汇报节奏均有成熟把握，可承担课题组各类对外汇报与项目申报材料的制作。</li>
  <li>业余<b>爱好摄影</b>并自备专业设备，作品曾刊发于学习强国、人民日报、中国青年报等主流平台，若组内有学术会议或活动拍摄需求，可随时配合。</li>
</ul>
<div class="callout-teal" style="margin-top:.8rem;">
  📞 <b>18306376923</b>　　📧 <b>1534827320@qq.com</b><br>
  对我有任何感兴趣的地方，如果您有时间，我都随时可以线下与您面谈。
</div>

<h3>八、结语</h3>
<p>本科阶段承蒙<b>张会星老师</b>悉心指导，我逐渐养成了严谨踏实、能吃苦肯投入的科研态度。十分敬佩您在人工智能、神经网络算法与地球物理反演交叉方向的学术积累与工程实践视野，真心渴望能加入您的课题组，把自身专业基础、代码能力与已有研究思路充分发挥，踏实跟随您求学科研。</p>
<p>随信附上个人简历、成绩单、竞赛获奖证书等相关材料，恳请老师在百忙之中抽空审阅。无论结果如何，都由衷感谢老师拨冗阅读，期待能有机会得到您的指点与接纳！</p>
<p>从 2025 年开始，我就把成为您的学生当作了我奋斗的目标。</p>
<p style="margin-top:1.5rem;">此致 敬礼！<br><b>申请人：潘高</b><br><span style="color:#516070;">2026 年 5 月 11 日</span></p>
</div>
""", unsafe_allow_html=True)


def render_network_preview() -> None:
    sec("核心网络结构图", "三通道地震输入 · 物理正演闭环 · 稀疏井低频先验")
    title, fname, desc = PROJECT_FIGURES[0]
    st.caption(desc)
    img(PROJECT_DIR / fname)


# ══════════════════════════════════════════════════════════════
#  Tab 2 · 科研成果
# ══════════════════════════════════════════════════════════════

def render_research() -> None:
    sec("核心研究方向")
    items = [
        ("核心问题",         "地震反演非唯一性 / 低频缺失 / 物理一致性不足",
         "面向地震数据到阻抗模型反演中的非唯一性、低频信息缺失和深度学习结果物理一致性不足等问题，"
         "牵头省级大创项目《基于 CycleGAN 与物理约束的地震反演方法研究》。"),
        ("主要创新",         "固定正演算子 · PINN 约束 · 1D→2D · 确定性反演伪标签",
         "将双生成器之一替换为确定性 Ricker 物理正演模型，把正演先验作为强约束嵌入；"
         "网络从 1D 扩展至 2D 实现空间连续建模；"
         "引入稀疏井约束，借助确定性反演结果构建伪标签辅助训练。"),
        ("后续规划",         "多尺度分频架构 · Diffusion · 不确定性评价",
         "计划引入低频/中频/高频三分量独立生成架构实现多尺度分频建模；"
         "路线可平滑嵌入 diffusion 等生成模型，进一步探索不确定性定量评价。"),
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

    sec("Qt 封装的 CycleGAN 预处理系统")
    st.markdown("""
<div class="callout-teal">
该系统围绕 CycleGAN 矩形训练流水线封装，覆盖 SEGY 重采样、正演模拟、传统反演接入、
数据增强、矩形切割、模型推理、结果合并以及日志状态管理等模块，
把原本分散在多个脚本中的处理步骤整合为可视化流程。
</div>
""", unsafe_allow_html=True)
    qr_path = ROOT / "assets" / "qr.png"
    qt_cols = st.columns([1, 1, 0.45])
    for col, (title, fname) in zip(qt_cols[:2], QT_FIGURES):
        with col:
            st.markdown(f"**{title}**")
            img(PROJECT_DIR / fname)
    with qt_cols[2]:
        st.markdown("**扫码运行程序**")
        img(qr_path)

    sec("创新项目证明")
    _, mid, _ = st.columns([1, 2, 1])
    with mid:
        img(RESEARCH_DIR / "innovation_project.png", "省级大创项目立项证明")


# ══════════════════════════════════════════════════════════════
#  Tab 3 · 荣誉证明
# ══════════════════════════════════════════════════════════════

def render_honors() -> None:
    _BADGE = {
        "国家级":    "ha-badge-nation",
        "全国":      "ha-badge-nation",
        "国际平台":  "ha-badge-intl",
        "省级":      "ha-badge-prov",
        "省级平台":  "ha-badge-prov",
        "市级":      "ha-badge-prov",
        "校级":      "ha-badge-school",
        "校级专业赛":"ha-badge-school",
        "院级":      "ha-badge-school",
    }

    # ── 荣誉总览清单 ──
    sec("荣誉总览", "本科阶段全部获奖与荣誉称号。")

    CAT_ORDER = ["奖学金", "学科竞赛", "综合荣誉", "社会实践", "志愿服务"]
    from collections import defaultdict
    groups = defaultdict(list)
    for title, cat, level, _ in AWARDS:
        groups[cat].append((title, level))

    col_a, col_b = st.columns(2)
    for i, cat in enumerate(CAT_ORDER):
        items = groups.get(cat, [])
        if not items:
            continue
        col = col_a if i % 2 == 0 else col_b
        rows = "".join(
            f'<div style="display:flex;align-items:center;gap:.45rem;'
            f'padding:.35rem 0;border-bottom:1px solid #f0f4f7;">'
            f'<span class="ha-badge {_BADGE.get(lvl,"ha-badge-school")}">{lvl}</span>'
            f'<span style="font-size:.9rem;color:#1a2b38;">{t}</span>'
            f'</div>'
            for t, lvl in items
        )
        col.markdown(
            f'<div style="background:#fff;border:1px solid #d9e4ea;border-radius:10px;'
            f'padding:1rem 1.2rem;margin-bottom:1rem;">'
            f'<div style="font-weight:800;font-size:.95rem;color:#0e7490;'
            f'margin-bottom:.5rem;">{cat}</div>'
            f'{rows}</div>',
            unsafe_allow_html=True,
        )

    # ── 证书图片 ──
    sec("证书材料", "可按类别或级别筛选查看原始证书。")
    with st.expander(f"📂 展开查看证书原件（共 {len(AWARDS)} 项）", expanded=False):
        categories = ["全部"] + sorted({a[1] for a in AWARDS})
        levels     = ["全部"] + sorted({a[2] for a in AWARDS})
        c1, c2 = st.columns(2)
        cat_sel = c1.selectbox("类别", categories)
        lvl_sel = c2.selectbox("级别", levels)
        filtered = [a for a in AWARDS
                    if (cat_sel == "全部" or a[1] == cat_sel)
                    and (lvl_sel == "全部" or a[2] == lvl_sel)]
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
        "前两年半完整成绩单 + 学习成绩排名证明（卓越班 + 普通班共 49 人中排名第 2，卓越班 14 人中排名第 1）。")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 前两年半成绩单")
        img(SCORES_DIR / "transcript_p1.jpg", "第 1 页")
        img(SCORES_DIR / "transcript_p2.jpg", "第 2 页")
    with col2:
        st.markdown("#### 学习成绩排名证明")
        img(SCORES_DIR / "ranking.jpg")

    sec("英语四六级成绩", "CET-4 552 分 · CET-6 522 分")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### CET-4　**552 分**")
        img(SCORES_DIR / "CET4.jpg")
    with col2:
        st.markdown("#### CET-6　**522 分**")
        img(SCORES_DIR / "CET6.jpg")


# ══════════════════════════════════════════════════════════════
#  主函数
# ══════════════════════════════════════════════════════════════

def render_nav() -> None:
    st.markdown("""
<div class="page-nav">
  <a href="#sec-letter">📄 申请信</a>
  <a href="#sec-research">🔬 科研成果</a>
  <a href="#sec-honors">🏆 荣誉证明</a>
  <a href="#sec-scores">📊 成绩材料</a>
</div>
""", unsafe_allow_html=True)


def _page_banner(icon: str, title: str, anchor: str) -> None:
    st.markdown(
        f'<div id="{anchor}" style="scroll-margin-top:80px;"></div>'
        f'<div style="background:var(--teal);border-radius:12px;padding:1rem 1.8rem;'
        f'margin:3rem 0 1.6rem;display:flex;align-items:center;gap:.9rem;">'
        f'<span style="font-size:1.5rem;">{icon}</span>'
        f'<span style="font-size:1.35rem;font-weight:900;color:#fff;">{title}</span>'
        f'</div>',
        unsafe_allow_html=True,
    )


def main() -> None:
    st.set_page_config(
        page_title="潘高 · 致陆文凯老师的硕士申请",
        page_icon="📄",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    inject_css()
    render_hero()
    render_nav()

    _page_banner("📄", "申请信", "sec-letter")
    render_letter()
    render_network_preview()

    _page_banner("🔬", "科研成果", "sec-research")
    render_research()

    _page_banner("🏆", "荣誉证明", "sec-honors")
    render_honors()

    _page_banner("📊", "成绩材料", "sec-scores")
    render_scores()



if __name__ == "__main__":
    main()
