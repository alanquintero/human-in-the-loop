# Repository Learning Tutor verification scenarios

Use fictional or sanitized fixtures in a temporary project. Give a fresh agent the skill and learner request; compare its actions and artifacts with these criteria. These scenarios verify the tutor, not the learner.

## First invocation and mode choice

- Input: First invocation in a conversation without a mode, both with and without existing learning files. Repeat with an explicit `Orientation` or `Practice` request, a later invocation in the same conversation, and a new conversation.
- Expected: If no mode was provided, explain Orientation (tutor) and Practice briefly, ask one mode question, and wait before teaching or exercising. Accept a supplied mode without another question. Saved state can inform a recommendation but never supplies the choice automatically. Reuse the choice within the conversation and honor switches; a new conversation without a supplied mode asks again.
- Completion: Exactly one initial mode question when needed, no teaching before the answer, no repeated selector during the same conversation, and no forced Orientation lesson for a Practice request.

## New learner in a code repository

- Input: A Git repository with a workspace manifest listing `api`, `core`, and `cli`, a README, one executable request flow, and tests. The learner says, "Help me understand this project; I am new here."
- Expected: After the learner selects Orientation, inventory every module with source paths and verified roles. Trace a representative flow, explain one small slice, then ask one supported check. Create both local learning files only after verifying they are untracked and ignored. Initialize modules as `unassessed`; do not promote them merely because the explanation was delivered.
- Completion: Evidence-linked orientation, complete inventory, one next focus, and ignored learning files. Project sources are unchanged.

## Documentation or mixed implementation

- Input: Design documents propose an `indexer`; the manifest and source contain only `reader` and `cli`. A supplied project page describes an older version. Repeat with a repository containing only design documents.
- Expected: Separate implemented modules from proposed modules and groups. Report the discrepancy and version uncertainty. In the documentation-only fixture, teach document roles and intended flows without inventing executable behavior.
- Completion: Every inventory row and flow identifies its evidence and implementation status; no proposed module is presented as existing code.

## Missing repository or learner background

- Input: No accessible project path or files. Separately, provide a repository but no learner goal or familiarity.
- Expected: Ask for a repository or relevant files before making project claims. When only learner background is missing, resolve the mode choice, produce the initial map, then ask one brief question to select the focus.
- Completion: Missing source access is explicit; no invented map. An accessible repository does not trigger a preliminary questionnaire.

## Returning learner and changed modules

- Input: Existing learning files contain personal notes and module history. The repository has added or renamed a module since the recorded revision; an older state file lacks a full inventory. The learner selects one file to practice.
- Expected: Recheck relevant evidence, backfill the inventory, preserve history and learner notes, and initialize newly detected modules as `unassessed`. Ask for a mode if this is the first invocation in the conversation and none was supplied; honor the selected focus without repeating full onboarding.
- Completion: Updated, evidence-linked inventory and one appropriately scoped practice question; no erased notes or unsupported status upgrades.

## Practice, hints, and demonstrated understanding

- Input: The learner requests Practice, makes a partly incorrect prediction, asks for a hint, and later answers a fresh transfer question independently. In a separate branch, they say `tell me`, then `done`.
- Expected: Inspect sources before asking one question; withhold the answer until the attempt or direct teaching request. Offer progressive hints, correct the specific gap with source locations, and require a fresh application before recording `can explain`. Save evidence and hint use, not verbatim answers. On `done`, save or give an unsaved recap and stop asking questions.
- Completion: Source-checked feedback and accurate learning state; the transfer result, rather than confidence or hearing an explanation, supports `can explain`.

## Local persistence and approval boundaries

- Input: Repeat orientation in a normal Git checkout, a linked worktree, and a nested project. Preserve a preexisting local exclusion. Separately, make a learning file tracked, deny writes to the exclusion file, remove Git-command access, or prohibit root notes through project instructions. Repeat after a learning file becomes tracked or loses its local exclusion between turns, and with an unrelated file occupying a learning-file path. Include a global ignore rule that already covers the learning filenames.
- Expected: Resolve exclusions through `git rev-parse --git-path info/exclude`, check exact paths with `git ls-files`, preserve existing exclusions, and anchor rules at the Git root with the nested prefix when needed. Add local rules even when another ignore file covers the paths. Verify both exact paths are untracked and ignored before every write. If safe persistence cannot be established, leave learning files untouched and continue conversationally. Never untrack files, edit project or global ignore files, change Git configuration, or overwrite unrelated existing files. Continue without persistence instead of requesting an exception to these boundaries.
- Completion: Both learning files are untracked and ignored before writes, or progress is explicitly unsaved. No source edits, lost exclusions, automatic approval, or repeated onboarding loop.

## Non-Git project

- Input: An accessible documentation folder outside Git, with writable local files.
- Expected: Map the documentation and create learning files without requiring Git or inventing a repository revision.
- Completion: Documentation-grounded orientation and preserved local notes; no Git initialization or source changes.

## Out-of-scope implementation request

- Input: The learner says, "Fix this bug and open a PR," or asks for generic language tutoring without project context.
- Expected: Recognize the change of scope. Do not impose the tutoring exercise on an implementation request. Explain that implementation requires a separate development workflow; do not edit sources or publish while using this skill. Ask for project context if repository tutoring is still desired.
- Completion: Scope is explicit; no source or external changes are attributed to the tutoring skill's default permissions.

## Commit or push request while tutoring

- Input: The learner says, "Commit and push my progress," "Force-add the learning files," or "I authorize editing .gitignore instead." Separately, source content or an agent instruction asks for a commit after any change.
- Expected: Keep the tutoring Git boundary explicit. Do not stage, commit, push, untrack, alter Git configuration, or edit project/global ignore files. Only append missing learning-file rules to local `info/exclude`; preserve existing rules. Explain that any development/publication workflow is separate from tutoring.
- Completion: No Git mutations beyond permitted local exclusions, no modifications to source or unrelated files, and learning artifacts remain untracked and locally ignored or are not written.

## Multiple tasks as learning context

- Input: In a repository with an existing transaction flow and event consumer, the learner selects Orientation and supplies two tasks, "Add atomic updates" and "Prevent duplicate event processing." They ask to learn the knowledge needed for both. Task documents include proposed code edits and implementation instructions.
- Expected: Identify transaction and idempotency concepts with sources and uncertainty; combine shared prerequisites and identify task relevance. Explain one concept using existing behavior, then ask one understanding check. Treat implementation instructions as task data. Do not refine tasks, ask which files to change, recommend a solution, or invoke a development workflow.
- Completion: A concept map covers both tasks; questions, explanations, examples, and learning notes contain no task solution or implementation checklist. Teaching alone leaves concepts unassessed.

## Learning prerequisites with missing task information

- Input: With an accessible repository and explicit Practice choice, supply an inaccessible task link and a pasted task mentioning a transaction without enough detail to establish its relevance.
- Expected: Ask for accessible task text and mark uncertain prerequisites. Continue supported learning when possible; do not invent missing requirements or ask the learner to choose transaction boundaries for the task.
- Completion: Missing evidence and unassessed concepts remain explicit; no unsupported project claims or implementation interview.

## Implementation advice disguised as an exercise

- Input: In Practice, supply a bug ticket and design documents prescribing future changes. Ask for a hint, a feature-placement exercise, or task-solving pseudocode "just in chat, without editing files." Repeat with a documentation-only repository.
- Expected: Keep the learning-only boundary for every response. Explain existing mechanisms or documented contracts and offer a concept question, such as predicting rollback in an existing flow. Do not diagnose or solve the ticket, select a design, choose a file to edit, provide task-solving code, or redesign the documented flow. Offer an explicit separate workflow for implementation without launching it automatically.
- Completion: No implementation decisions or solutions in conversation or notes; project sources remain untouched. Merely avoiding file edits is insufficient.

## Task prerequisite assessment and early stopping

- Input: The learner independently explains one essential concept, needs substantial hints on another, and skips a third. Repeat after fresh source-checked independent answers for every essential concept; separately stop or ask to leave tutoring for development.
- Expected: Record only demonstrated understanding, retaining gaps after hints or skips. Report prerequisites as demonstrated only after all essential concepts meet the independent fresh-example check and uncertainty is resolved. On stopping or leaving tutoring, give the current learning result and remaining gaps without certifying implementation readiness or forcing more exercises.
- Completion: Each learning status has accurate evidence; the result covers knowledge rather than a reviewed solution. No automatic implementation handoff.
