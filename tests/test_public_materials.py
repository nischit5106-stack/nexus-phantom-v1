import importlib.util,json,unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("toy",R/"demo/toy_permutation.py");toy=importlib.util.module_from_spec(spec);spec.loader.exec_module(toy)
class PublicMaterials(unittest.TestCase):
 def test_same_actor_is_not_coordination(self):
  self.assertEqual(toy.coactivity([(1,2,0),(1,3,0)]),0)
 def test_duplicate_invariance(self):
  rows=[(1,4,0),(2,4,0),(3,5,0)]
  self.assertEqual(toy.coactivity(rows),toy.coactivity(rows*5))
 def test_actor_labels_do_not_change_toy_statistic(self):
  rows=[(1,4,0),(2,4,0),(3,5,0)]
  self.assertEqual(toy.coactivity(rows),toy.coactivity([(100-u,i,t) for u,i,t in rows]))
 def test_published_aggregate_denominators(self):
  d=json.loads((R/"tables/final_evaluation_aggregates.json").read_text())
  self.assertEqual(d["groups"]*d["listeners_per_group"],d["listeners"])
  self.assertEqual(d["pairs"]*2,d["worlds"])
  self.assertEqual(len(d["blocks"]),d["groups"])
 def test_no_research_data_containers(self):
  forbidden={".parquet",".npy",".npz",".pickle",".pkl",".sqlite",".duckdb"}
  self.assertFalse([str(p.relative_to(R)) for p in R.rglob("*") if p.suffix in forbidden])
if __name__=="__main__":unittest.main()
