# VICE timing backends

A backend bridges one verified VICE debugger/monitor interface to C64Scene's canonical evidence format.

Invocation contract:

    backend <vice-executable> <prg>

Standard output must contain one marker per observed frame:

    C64SCENE_TIMING frame=<n> line=<n> cycle=<n>

A backend must document:

- supported VICE version/range;
- exact monitor/debug mechanism used;
- how the breakpoint at `stable_start` is resolved;
- where raster line and cycle are obtained;
- any emulator options that affect timing.

Backends must not derive a cycle number from host timestamps, border transitions, guessed instruction counts, or undocumented text parsing.

No backend is considered verified merely because it exists. Verification evidence belongs with qualification documentation.
