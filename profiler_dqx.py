from databricks.labs.dqx.profiler.profiler import DQProfiler
from databricks.labs.dqx.profiler.generator import DQGenerator
from databricks.labs.dqx.profiler.dlt_generator import DQDltGenerator
from databricks.labs.dqx.config import WorkspaceFileChecksStorageConfig
from databricks.labs.dqx.engine import DQEngine
from databricks.sdk import WorkspaceClient

df = spark.read.table("samples.nyctaxi.trips")

# profile input data
ws = WorkspaceClient()
profiler = DQProfiler(ws)
summary_stats, profiles = profiler.profile(df)

# generate DQX quality rules/checks
generator = DQGenerator(ws)
checks = generator.generate_dq_rules(profiles)

dq_engine = DQEngine(ws)
dlt_generator = DQDltGenerator(ws)

dq_engine.save_checks(checks, config=WorkspaceFileChecksStorageConfig(location="/Workspace/Users/yeshsree14@gmail.com/.bundle/dab_dqx/dev/dqx/checks.yml"))

dlt_expectations = dlt_generator.generate_dlt_rules(profiles, language="SQL")
print(dlt_expectations)


dlt_expectations = dlt_generator.generate_dlt_rules(profiles, language="Python")
# print(dlt_expectations)

dlt_expectations = dlt_generator.generate_dlt_rules(profiles, language="Python_Dict")
# print(dlt_expectations)