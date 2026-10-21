# Source-based reproduction

Nischit Girish Kumar · NEXUS Research Initiative — Independent Research  
Reviewed 21 October 2026. No raw datasets are redistributed with PHANTOM.

## Choose the reproduction scope

| Scope | What the public package supports | Additional requirements |
|---|---|---|
| Publication and presentation | Rebuild aggregate figures and papers; run the invented teaching example and five public-material tests; inspect the synthetic dashboard | Dependencies in the repository README; no source dataset required |
| Source preparation | Obtain the original releases, verify identifiers, inspect schema, apply the documented date windows and eligibility rules | Your own authorized source access and local data-processing environment |
| Exact historical/final experiment | Inspect published methods, seeds, gates and aggregate results | Separately cleared frozen research code, exact phase configurations/runtime receipts, population mappings, development-clone references and protected evaluator resources; these are not bundled |

Acquiring the source data alone is not sufficient to reproduce the exact protected evaluation. Independent implementations can follow the paper and supplement, but must identify any differences and must not claim byte-identical reproduction without the missing artifacts. September 2026 is already consumed evaluation evidence; using it again does not create a new unseen final test. These instructions do not authorize running or changing the frozen PHANTOM v1 experiment.

## 1. Deezer development source

**Dataset citation:** Tran, Viet Anh (2024). *Deezer listening events dataset*, version v1. Zenodo. DOI: [10.5281/zenodo.13890194](https://doi.org/10.5281/zenodo.13890194).

**Required accompanying paper:** Tran, Viet-Anh; Salha-Galvan, Guillaume; Sguerra, Bruno; and Hennequin, Romain (2024). *Transformers Meet ACT-R: Repeat-Aware and Sequential Listening Session Recommendation*. Proceedings of the 18th ACM Conference on Recommender Systems. [DOI 10.1145/3640457.3688139](https://doi.org/10.1145/3640457.3688139).

**Official source/download page:** [Zenodo record 13890194](https://zenodo.org/records/13890194). Select `recsys24_deezer_dataset.tar.gz`, version v1, published 4 October 2024. The publisher lists MD5 `7e2990b694e056d260139f09c9c72243`. The frozen audit recorded 7,798,952,650 archive bytes and a matching published MD5. MD5 identifies this archive for compatibility; it is not a modern authenticity guarantee. Record a local SHA-256 and retain the publisher metadata with your acquisition receipt.

**Access conditions:** the inspected record's License section did not expose a resolved license value. Confirm applicable permission with the official source or rights holder before reuse. A publicly downloadable archive does not itself establish redistribution rights. PHANTOM does not mirror its events, embeddings or sampled histories.

**Required coverage:** 1 March 2022 00:00:00 UTC inclusive through 1 September 2022 00:00:00 UTC exclusive. The frozen audit observed 184 dates and a final timestamp of 31 August 2022 23:59:58 UTC. Individual historical experiments use bounded subsets; do not substitute the entire archive for those populations.

**Schema from the frozen source audit:** 500 event Parquet files with non-null `int64` fields `user_id`, `track_id`, `session_id`, `ts`. Treat `ts` as UTC epoch seconds. The separate embedding file has 50,000 track rows, 128-dimensional finite vectors and a supplied `art_id` association. Embeddings are not required for the final ListenBrainz population detector. The observed event catalog contains 43,803 tracks; do not confuse the two counts.

**Preparation and validation:**

1. Keep the acquired archive unchanged outside the public repository. Record source URL, acquisition time, version, size and digest. Extract locally and inventory every member.
2. Decode every Parquet shard, validate field types/nullability, and filter with the half-open UTC range above. Use bounded batches or a disk-backed query engine; the full event table is too large for casual in-memory loading.
3. Retain all source rows and exact duplicates. Audit duplicate multiplicity separately. The reference audit contains 704,728,520 events, 3,444,027 users and 2,435,880 excess duplicates.
4. Preserve `session_id` as a source label. All 70,472,852 source sessions contain exactly ten rows; do not reinterpret them as complete natural listening sessions or impose an arbitrary order on timestamp ties.
5. For development sampling, preserve every observed in-window row for each selected user. The recorded development sample contains 671,410 rows, 3,252 users and 19,380 tracks. Exact membership depends on the phase-specific sampling configuration and receipts, which are not part of the public subset. Do not invent a sampling seed to match these counts.
6. Keep original event rows available to validate row/marginal/duplicate invariants. Detector-specific unique-presence projections are derived views, not destructive deduplication of the source.

These counts and schema details come from the frozen PHANTOM audit, rather than a fresh read of the raw data in Phase 13.

## 2. ListenBrainz external and prospective source

**Dataset citation:** MetaBrainz Foundation / ListenBrainz (2026). *ListenBrainz full export, snapshot 2723, 15 October 2026, 00:00:02*. Spark listening-event archive. Identify the snapshot and the archive digest below when reporting reproduction.

**Official entry points:** [ListenBrainz data downloads](https://listenbrainz.org/data/), [dump documentation](https://listenbrainz.readthedocs.io/en/latest/users/listenbrainz-dumps.html), and the [recorded snapshot directory](https://data.metabrainz.org/pub/musicbrainz/listenbrainz/fullexport/listenbrainz-dump-2723-20261015-000002-full/).

**Exact recorded artifact:** `listenbrainz-spark-dump-2723-20261015-000002-full.tar`.

**Committed publisher SHA-256:** `3dae80f8f587c39a2c09c7036bb25af392063b796d8b8f6e52b7e89e51e112a4`.

The frozen acquisition compared publisher checksum metadata with this commitment and hashed downloaded projections. It used HTTP byte ranges and did **not** independently recompute the digest of the entire remote archive. A researcher downloading the full artifact should recompute its SHA-256 locally and compare it. The snapshot URL is retained from the acquisition record; current availability could not be revalidated by the Phase 13 web reader. If it has rotated out, request that exact snapshot from the official provider. Do not silently use the newest dump, a JSON API response, or a differently packaged archive and claim exact identity.

**Access conditions:** the [official terms](https://listenbrainz.org/terms-of-service/) describe user listen data and text as CC0. Check the current source terms and access requirements yourself. PHANTOM still excludes raw histories and real-user mappings from its public package. This source license does not release PHANTOM's protected evaluator truth or clear unrelated research code.

| Use | UTC window, start inclusive/end exclusive | Frozen source/population reference |
|---|---|---|
| External validation | `2022-05-01T00:00:00Z` to `2022-05-29T00:00:00Z` | 16,006,621 window events; 16,783 users; 16,185 eligible users; 4,032 selected listeners; 4,004,802 selected original events |
| Prospective final | `2026-09-01T00:00:00Z` to `2026-09-29T00:00:00Z` | 4,032 selected listeners in 42 groups of 96; 3,714,102 selected original events |

**Schema actually consumed by the frozen Spark adapter:** Parquet fields `user_id`, `recording_msid`, `listened_at`. `user_id` is the snapshot's anonymous integer identifier. `recording_msid` is the exact recording key. `listened_at` is read at nanosecond resolution; each accepted value must be an integral UTC epoch second. Generic dump documentation may describe another packaging generation: inspect the named artifact, and reject an incompatible schema instead of silently changing adapters. `user_name` from a JSON API is not an interchangeable identifier.

**Preparation and eligibility:**

1. Acquire the committed artifact from an official source. Retain archive identity, publisher checksum receipt, local checksums and Parquet-member inventory privately. Read all members needed to cover the complete requested UTC window; a single shard is not sufficient evidence of coverage.
2. Validate the three required columns. Reject non-integral-second timestamps. Convert nanoseconds to epoch seconds and apply `start <= timestamp < end`. Do not shift dates, fuzzy-merge recording keys or infer missing event identities.
3. Map exact users and recording keys into distinct, deterministic integer namespaces; check for collisions. The frozen adapter uses `ListenBrainz_user_id` and `ListenBrainz_recording_msid` namespaces with a SHA-256-derived 63-bit mapping. An independent mapping can preserve scientific semantics, but cannot claim exact array hashes without the original serialization and ordering rules.
4. Preserve all in-window records, including duplicates, for each selected user. “Complete history” here means the complete observed source window, not an individual's complete lifetime listening history.
5. Eligible users have at least 10 events and at least 2 distinct tracks in that window. Group exact history clones using track-relabel-invariant timestamp profiles before partitioning. Keep each clone component together across the 42 groups.
6. The May sampling seed is `41201`. The final sampling seed is `41290`; apply it to component assignment and selection. The retained configuration includes a historical prose label mentioning `41201`, but the final executable sampling value and population manifest are `41290`. Require 96 selected users in each group; stop as incompatible if a required group cannot be filled.
7. Before final selection, exclude all 16,783 users observed in the May window, not only the selected May subset. Check against documented development-history clone signatures and stop on a conflict. These exact real-user exclusions and development references are protected and omitted. Authorized access is necessary to reproduce the same final membership; this guide does not reconstruct or publish those identities.
8. Perform selection and compatibility checks before constructing worlds or observing detector results. Do not replace an incompatible population with a favorable subset. Maintain deterministic source-row lineage, group/user/time/item ordering, and the original duplicate multiplicities.

**Methods after source preparation:** the supplement specifies the controlled 32-slot/eight-item construction, seeds `41291`, `41292`, `41293`, 4,095 null draws with seed `41101`, threshold `3.0`, 2,000 whole-block resamples with seed `41102`, and scientific gates. These parameters describe the completed study; they are not a substitute for cleared executable code or protected evaluation resources. The original verifier receipt-serialization failure and subsequent forensic confirmation remain part of the provenance.

**Permitted identity check:** the final selected substrate's recorded SHA-256 is `0bf62b9935e29f0783df882b330d6bbdebe4f0f83ea2f1de9104af42dda65084`. This is a file identifier for an independently authorized reproduction, not a download link or disclosure of the substrate. Different row encoding, ordering or software versions may alter bytes even when semantic checks agree; report the distinction.

## 3. Reproduction receipt

Record source citation/URL, snapshot and filename, permission basis, acquired bytes/checksums, schema and null checks, exact UTC range, preprocessing/version information, eligibility counts, clone/exclusion policy, selected-group counts, duplicate invariants and any deviations. Store raw records, mappings and protected receipts privately. Publish only cleared aggregates and permitted identifiers.

Use the repository README commands for the released teaching example, tests, figures, paper builds and local website. Those commands require no raw-data download and execute no frozen scientific evaluation. Full experimental reproduction remains conditional on the separately withheld resources above.
