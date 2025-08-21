import pandas as pd # type: ignore
import json

# 加载数据
df = pd.read_excel("attack_data.xlsx")

# 数据清洗
df['risk_level'] = pd.cut(df['avg_risk'], 
                          bins=[-0.1, 0.3, 0.7, 1.5],
                          labels=["低风险", "中风险", "高风险"])

# 生成排行榜
top_10 = df.sort_values(['success_rate', 'avg_risk'], ascending=[False, False]).head(10)

# 统计信息
type_stats = df.groupby('cmd_types').agg(
    avg_success=('success_rate', 'mean'),
    high_risk_count=('avg_risk', lambda x: sum(x > 0.7))
)

# 保存数据为 JSON 文件
top_10.to_json("data/top_10.json", orient="records")
type_stats.to_json("data/type_stats.json", orient="records")