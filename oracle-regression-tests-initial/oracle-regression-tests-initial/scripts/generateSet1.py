import pandas as pd

df = pd.read_csv("testsets.csv", header=None)
setName = "Set1"
row_counts = df.iloc[:, 0].astype(str).str.contains(setName).sum()

if row_counts > 0:
    stages = [f"stage_{i}" for i in range(row_counts)]
    stages_line = f"stages: [{', '.join(stages)}]"
    with open("pipeline_set1.yml", "a") as f:
      f.write(stages_line + "\n")
  
    mask = df.iloc[:, 0].str.contains(setName, na=False)
    for i, (_, row) in enumerate(df[mask].iterrows()):
        project_name = row.iloc[1]
        print(project_name)
        branch_name = row.iloc[2]
        print(branch_name)
        with open("pipeline_set1.yml", "a") as f:
          stagenr="stage_{0}".format(i)
          f.write(stagenr + ":" + "\n")
          f.write("  stage: {0}".format(stagenr) + "\n")
          f.write("  trigger:" + "\n")
          f.write("    project: {0}".format(project_name) + "\n")
          f.write("    branch: {0}".format(branch_name) + "\n")
          f.write("    strategy: depend" + "\n")
          f.write("  variables:" + "\n")
          for j in range(3, len(row)):
              variable_value = row.iloc[j]
              print(variable_value)
              if str(variable_value) != "nan":
                result = str(variable_value).split(':')
                variable = result[0]
                value = result[1]
                f.write("    {0}: {1}".format(variable, value) + "\n")
          
           
