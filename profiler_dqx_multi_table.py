from databricks.labs.dqx.profiler.profiler import DQProfiler
from databricks.labs.dqx.profiler.generator import DQGenerator
from databricks.labs.dqx.engine import DQEngine
from databricks.labs.dqx.config import WorkspaceFileChecksStorageConfig
from databricks.sdk import WorkspaceClient

ws = WorkspaceClient()
profiler = DQProfiler(ws)
generator = DQGenerator(ws)
dq_engine = DQEngine(ws)

# Profile several tables by name
results = profiler.profile_tables_for_patterns(
  patterns=["samples.nyctaxi.trips", "samples.bakehouse.sales_transactions"]
)


# Process results for each table
for table, (summary_stats, profiles) in results.items():
  

  checks = generator.generate_dq_rules(profiles)

  table_name = table.split(".")[-1]
  file_name = f"{table_name}_checks.yml"

  save_path = f"/Workspace/Users/yeshsree14@gmail.com/.bundle/dab_dqx/dev/dqx/{file_name}"
  dq_engine.save_checks(checks, config=WorkspaceFileChecksStorageConfig(location=save_path))

  print(f"Table: {table}")
  print(f"Table statistics: {summary_stats}")
  print(f"Generated profiles: {profiles}")



# # Generate and save checks for each table separately
# for table, (summary_stats, profiles) in results.items():

#     print(f"Processing table: {table}")

#     checks = generator.generate_dq_rules(profiles)

#     table_name = table.split(".")[-1]
#     file_name = f"{table_name}_checks.yml"

#     save_path = f"/Workspace/Users/yeshsree14@gmail.com/.bundle/dab_dqx/dev/dqx/{file_name}"

#     # Save checks YAML
#     dq_engine.save_checks(
#         checks,
#         config=WorkspaceFileChecksStorageConfig(location=save_path)
#     )

#     print(f"Saved checks file: {save_path}")