# References and adoption decisions

Reviewed on 2026-09-09. These projects inform the design; none of their code or dependencies has been incorporated.

| Project | Relevant idea | Current decision |
|---|---|---|
| [Generative Agents](https://github.com/joonspk-research/generative_agents) | Experience, retrieval, reflection, and action loop | Borrow the loop without importing the town simulator |
| [AI Town](https://github.com/a16z-infra/ai-town) | An observable social world for AI characters | Revisit if a visual world becomes a requirement |
| [Letta](https://github.com/letta-ai/letta) | Separate persistent core context from external memory | Keep the persona short and retrieve relevant history on demand |
| [Reflexion](https://github.com/noahshinn/reflexion) | Use prior attempts and reflections in subsequent attempts | Borrow feedback evaluation without assuming task results transfer to social outcomes |
| [Graphiti](https://github.com/getzep/graphiti) | Relationships, temporal validity, and source provenance | Keep file-based records for now; evaluate a graph database when scale or query needs justify it |

Further reading: [Generative Agents paper](https://arxiv.org/abs/2304.03442) and [Letta memory architecture](https://github.com/letta-ai/skills/blob/main/letta/letta-api-client/memory-architecture.md).

Evaluate code integration when a concrete retrieval, relationship-update, scaling, or presentation requirement exceeds the current implementation. Review the relevant module's license, dependencies, migration cost, and measurable benefit before adopting it.
