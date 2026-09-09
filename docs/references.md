# 参考项目及取舍

核对日期：2026-09-09。当前只参考设计，未复制以下项目代码，也未添加它们的依赖。

| 项目 | 参考点 | 当前取舍 |
|---|---|---|
| [Generative Agents](https://github.com/joonspk-research/generative_agents) | 经历、检索、反思与行动的循环 | 借鉴循环，不搬小镇模拟环境 |
| [AI Town](https://github.com/a16z-infra/ai-town) | 可围观的角色社交世界 | 如果以后需要可视化世界，再考虑 |
| [Letta](https://github.com/letta-ai/letta) | 常驻核心记忆和外部记忆分开 | 保持简短角色，按需提供相关历史 |
| [Reflexion](https://github.com/noahshinn/reflexion) | 上次尝试和反思用于下次尝试 | 借鉴反馈评估；不直接外推任务实验到社交效果 |
| [Graphiti](https://github.com/getzep/graphiti) | 关系、时间与来源溯源 | 先用现有文件记录；规模和查询需求出现后再评估图数据库 |

[Generative Agents 论文](https://arxiv.org/abs/2304.03442)；[Letta 记忆架构](https://github.com/letta-ai/skills/blob/main/letta/letta-api-client/memory-architecture.md)。

决定是否整合代码的条件：先出现现有实现难以解决的检索、关系更新、规模或展示需求，再针对一个明确模块评估。引入前检查许可证、依赖、迁移成本与可测收益。
