#!/usr/bin/env python3
"""Round 2: verify replacement / additional reference URLs."""
import concurrent.futures as cf
import re
import subprocess

URLS = """
https://blog.palantir.com/a-day-in-the-life-of-a-palantir-forward-deployed-software-engineer-45ef2de257b1
https://blog.palantir.com/dev-versus-delta-demystifying-engineering-roles-at-palantir-ad44c2a6e87
https://blog.palantir.com/the-baseline-team-and-forward-deployed-infrastructure-engineering-at-palantir-efd84e72e40b
https://blog.palantir.com/ontology-oriented-software-development-68d7353fdb12
https://blog.palantir.com/how-palantir-foundrys-ontology-deploys-data-science-to-the-front-line-7a9679bdfd01
https://www.uber.com/us/en/blog/microservice-architecture/
https://www.uber.com/us/en/blog/michelangelo-machine-learning-platform/
https://www.uber.com/us/en/blog/from-predictive-to-generative-ai/
https://stripe.com/blog/api-versioning
https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/saas-tenant-isolation-strategies.html
https://cloud.google.com/blog/products/ai-machine-learning/rag-vs-fine-tuning
https://queue.acm.org/detail.cfm?id=3454124
https://docs.langchain.com/oss/python/langgraph/graph-api
https://developers.openai.com/api/docs/guides/evaluation-best-practices
https://developers.openai.com/resources/evals
https://platform.openai.com/docs/guides/structured-outputs
https://platform.openai.com/docs/guides/fine-tuning
https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching
https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.600-1.pdf
https://github.com/pgvector/pgvector
https://github.com/NVIDIA/NeMo-Guardrails
https://github.com/openai/tiktoken
https://opentelemetry.io/docs/
https://docs.smith.langchain.com/
https://www.enterpriseintegrationpatterns.com/
https://martinfowler.com/bliki/ConwaysLaw.html
https://hbr.org/1995/05/leading-change-why-transformation-efforts-fail
https://www.svpg.com/product-vs-feature-teams/
https://hai.stanford.edu/ai-index
https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
https://arxiv.org/abs/2504.20879
https://arxiv.org/abs/2406.12624
https://arxiv.org/abs/2308.11432
https://www.cisa.gov/resources-tools/resources/guidelines-secure-ai-system-development
https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/considerations/tenancy-models
https://developers.google.com/machine-learning/crash-course
https://www.evidentlyai.com/ml-in-production/model-monitoring
https://docs.ragas.io/
https://github.com/confident-ai/deepeval
https://www.palantir.com/docs/foundry/
https://blog.palantir.com/apollo-continuous-delivery-6b9f0d2b8f8b
https://aws.amazon.com/compliance/soc-faqs/
https://cloud.google.com/security/compliance/soc-2
https://www.microsoft.com/en-us/trust-center/compliance/iso-certified
""".split()


def check(url: str) -> str:
    try:
        out = subprocess.run(
            ["curl", "-sL", "--max-time", "25", "-A",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36",
             "-w", "\n__STATUS__%{http_code}", url],
            capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=40,
        ).stdout
    except Exception as exc:  # noqa: BLE001
        return f"ERR   | {exc} | {url}"
    status = out.rsplit("__STATUS__", 1)[-1].strip() if "__STATUS__" in out else "?"
    m = re.search(r"<title[^>]*>(.*?)</title>", out, re.S | re.I)
    title = re.sub(r"\s+", " ", m.group(1)).strip()[:110] if m else "(no title)"
    return f"{status} | {title} | {url}"


with cf.ThreadPoolExecutor(max_workers=12) as pool:
    for line in sorted(pool.map(check, URLS)):
        print(line)
