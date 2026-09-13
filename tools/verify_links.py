#!/usr/bin/env python3
"""Verify candidate reference URLs: HTTP status + page title (identity check)."""
import concurrent.futures as cf
import re
import subprocess

URLS = """
https://grpc.io/docs/what-is-grpc/introduction/
https://cloud.google.com/apis/design
https://martinfowler.com/articles/richardsonMaturityModel.html
https://protobuf.dev/
https://json-schema.org/
https://kafka.apache.org/intro
https://www.databricks.com/glossary/medallion-architecture
https://docs.getdbt.com/docs/introduction
https://c4model.com/
https://adr.github.io/
https://martinfowler.com/bliki/ArchitectureDecisionRecord.html
https://arxiv.org/abs/1603.09320
https://arxiv.org/abs/2210.03629
https://openai.com/index/introducing-structured-outputs-in-the-api/
https://langchain-ai.github.io/langgraph/concepts/low_level/
https://huggingface.co/blog/mteb
https://www.anthropic.com/news/contextual-retrieval
https://learn.microsoft.com/en-us/azure/architecture/patterns/
https://aws.amazon.com/architecture/well-architected/
https://arxiv.org/abs/2310.03714
https://arxiv.org/abs/2305.05176
https://arxiv.org/abs/2406.18665
https://arxiv.org/abs/2404.14618
https://openai.com/index/gpt-4o-fine-tuning/
https://hbr.org/2016/09/know-your-customers-jobs-to-be-done
https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2
https://www.iso.org/standard/42001
https://www.nist.gov/itl/ai-risk-management-framework
https://artificialintelligenceact.eu/
https://www.hhs.gov/hipaa/index.html
https://gdpr-info.eu/
https://genai.owasp.org/llm-top-10/
https://csrc.nist.gov/pubs/sp/800/162/upd2/final
https://csrc.nist.gov/pubs/sp/800/207/final
https://microsoft.github.io/presidio/
https://aws.amazon.com/solutions/whitepapers/saas-tenant-isolation-strategies/
https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html
https://fedramp.gov/
https://openid.net/connect/
https://www.rfc-editor.org/rfc/rfc7644
https://docs.greatexpectations.io/docs/
https://developers.google.com/identity/protocols/oauth2
https://arxiv.org/abs/2306.05685
https://arxiv.org/abs/2309.15217
https://arxiv.org/abs/2211.09110
https://arxiv.org/abs/2202.03629
https://arxiv.org/abs/2304.09848
https://github.com/openai/evals
https://github.com/promptfoo/promptfoo
https://arxiv.org/abs/2310.06770
https://arxiv.org/abs/2104.11315
https://dora.dev/
https://sre.google/sre-book/service-level-objectives/
https://research.google/pubs/pub40801/
https://langfuse.com/docs
https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
https://www.sec.gov/Archives/edgar/data/1321655/000119312520281378/d890410ds1.htm
https://www.uber.com/blog/microservice-architecture/
https://www.uber.com/blog/michelangelo-machine-learning-platform/
https://stripe.com/blog/apis-as-infrastructure
https://www.databricks.com/research/lakehouse-a-new-generation-of-open-platforms-that-unify-data-warehousing-and-advanced-analytics
https://teamtopologies.com/key-concepts
https://martinfowler.com/bliki/TechnicalDebtQuadrant.html
https://sre.google/sre-book/eliminating-toil/
https://arxiv.org/abs/2403.04132
https://arxiv.org/abs/2404.16130
""".split()


def check(url: str) -> str:
    try:
        out = subprocess.run(
            ["curl", "-sL", "--max-time", "25", "-A",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36",
             "-w", "\n__STATUS__%{http_code}", url],
            capture_output=True, text=True, timeout=40,
        ).stdout
    except Exception as exc:  # noqa: BLE001
        return f"ERR   | {exc} | {url}"
    status = out.rsplit("__STATUS__", 1)[-1].strip() if "__STATUS__" in out else "?"
    m = re.search(r"<title[^>]*>(.*?)</title>", out, re.S | re.I)
    title = re.sub(r"\s+", " ", m.group(1)).strip()[:110] if m else "(no title)"
    return f"{status} | {title} | {url}"


with cf.ThreadPoolExecutor(max_workers=12) as pool:
    for line in pool.map(check, URLS):
        print(line)
