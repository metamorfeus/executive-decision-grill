# About this public copy of the independent-sessions records

These folders are the records of three test rounds run on 13 October 2026 (see section 9 of
`tests/TEST-REPORT.html`). This is a **cleaned copy**, made on 9 November 2026 for publication. The
untouched originals are kept privately by the author.

## What was removed

The first round's author also wrote four **sealed** scenarios (SEAL-1 to SEAL-4) with their expected-behaviour
lists. They have never been opened or run. They are held back for one final, untouched test before a release, so
they must stay unseen, and are not published. Every file that names them was removed:

- `2026-10-13_pilot-v1.4/inputs/helpers-author/author-record-sealed.md` (SHA-256 `d1588385cbbbd52d1c8391f129785e785e6d00747d8289e0bed4eb0bc6048172`)
- `2026-10-13_pilot-v1.4/inputs/helpers-author/check_scenarios.py` (SHA-256 `7968dd17485972b6d91a59a6efe3600f2649890732599baf851f9b75d119983e`)
- `2026-10-13_pilot-v1.4/inputs/helpers-author/result.json` (SHA-256 `f0a630f616c4d0e3383dc7a457bebbc3b26930d87f9aba31502ad9aeccb640df`)
- `2026-10-13_pilot-v1.4/inputs/helpers-author/scenarios-sealed.md` (SHA-256 `580a2509f3290dd92c53b4d6b93956d70eb6c0f81e444b2349ad369cd0c91a09`)
- `2026-10-13_pilot-v1.4/inputs/helpers-author/task_prompt.md` (SHA-256 `a60e4bcf51b3fff87472484d27b69ca441d366a0a1dd541c017cd1c5e94454e2`)
- `2026-10-13_pilot-v1.4/inputs/helpers-keywriter/keywriter-record.md` (SHA-256 `92895ce811f96bc02af2f115a6680b3e088e44ae75f2fea5b468338cddbc7277`)
- `2026-10-13_pilot-v1.4/inputs/helpers-keywriter/result.json` (SHA-256 `a6c23899fd2a18d2f8e34d635ff776d65793579d1a8614eb4533565dd44fcb20`)
- `2026-10-13_pilot-v1.4/inputs/helpers-keywriter/task_prompt.md` (SHA-256 `cc38610a4d994bd4f021f3202667ef21402db1a0e157ec3bc089d852168abd7a`)
- `2026-10-13_pilot-v1.4/inputs/helpers-keywriter/watch-for-sealed.md` (SHA-256 `fb3dfcdd4553e67dc93442a54ebefd93c7277be311c6c01d89b31904fdadb26e`)

Because the author's prompt, result and check script also held the development scenarios, those three files
are gone too. The development scenarios and their lists are still here, in `scenarios-dev.md`,
`scenarios-replay.md`, `watch-for-dev.md` and `watch-for-replay.md`.

## What was changed

A local Windows user name in the path to the Claude command-line program was replaced with `<you>`. Nothing
else in these files changed.

- `2026-10-13_pilot-v1.4/inputs/tools/run_conversation.py` (before `f3715e907a3c7c1d6430299038283b82ff34b9cc4f068b656acbdf6b16d5465f`, after `72438bcf39a2bbcf54122c7a8c7debd2701aa72a15b9371400a26bceab4ec072`)
- `2026-10-13_pilot2-v1.4/inputs/tools/run_conversation.py` (before `05a4521afa9a4b01a1c76c5734c6953c882f2a1635a819046a93918863a1c22e`, after `4c25e4bcca8fb3d27deaea0f1406515224498c139fb954e91fbc37a86204cfa7`)
- `2026-10-13_pilot3-v1.5/inputs/tools/run_conversation.py` (before `05a4521afa9a4b01a1c76c5734c6953c882f2a1635a819046a93918863a1c22e`, after `4c25e4bcca8fb3d27deaea0f1406515224498c139fb954e91fbc37a86204cfa7`)

## Fingerprints

The `inputs.sha256` and `record.sha256` files are the originals. They still list the removed files, and the three
changed files will not match them. To check, go into a round's `inputs` folder and run
`sha256sum -c ../inputs.sha256`. The expected failures are the removed and changed files above, plus two
that were already there before this copy was made: in the second round, `tools/build_sheets.py` and
`tools/reader_task_prompt.md` do not match their fingerprints in the untouched originals either. They were
most likely edited after the fingerprints were taken; the round's README does not say.

Git is told to store every file in this folder byte for byte (see `.gitattributes`), so these fingerprints
match on any computer, not only on the author's.

The first round's `README.md` still describes its inputs as they were before this copy was made, including
the sealed scenarios and the helper files listed above. It was left unchanged so that it keeps matching its
fingerprint; this note is the correction.

Local folder paths (`C:\OD\...`) in these records are left as they were, as in the published transcripts.

## Addendum, 11 November 2026: the sealed scenarios were run

The four sealed scenarios and their watch-for lists were used, unchanged, for the final test of version 1.5 on
11 November 2026. They are now published in `2026-11-11_final-heldback-v1.5/inputs/heldback/` as
`scenarios-held-back.md` and `watch-for-held-back.md`. Their SHA-256 values are the ones listed above for
`scenarios-sealed.md` and `watch-for-sealed.md`, which shows they are the files held back on 13 October. The
other removed helper files stay private. The statement above that the scenarios "have never been opened or run"
was true when this note was written.
