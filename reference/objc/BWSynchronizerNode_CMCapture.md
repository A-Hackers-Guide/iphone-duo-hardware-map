# `BWSynchronizerNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 6 instance variables, 0 properties, 15 instance methods, 1 class methods

## Instance variables

```
^{OpaqueCMClock=} _sourceClock;
^{OpaqueCMClock=} _masterClock;
{?="value"q"timescale"i"flags"I"epoch"q} _quantizationFrameDuration;
[16{?="sourceTime"{?="value"q"timescale"i"flags"I"epoch"q}"syncedTime"{?="value"q"timescale"i"flags"I"epoch"q}}] _ptsSyncHistory;
i _oldestPTSSyncHistoryElement;
i _newestPTSSyncHistoryElement;
```

## Class methods

```
+[BWSynchronizerNode initialize];
```

## Instance methods

```
-[BWSynchronizerNode prepareForCurrentConfigurationToBecomeLive];
-[BWSynchronizerNode setMasterClock:];
-[BWSynchronizerNode renderSampleBuffer:forInput:];
-[BWSynchronizerNode quantizationFrameDuration];
-[BWSynchronizerNode dealloc];
-[BWSynchronizerNode initWithMediaType:];
-[BWSynchronizerNode hasNonLiveConfigurationChanges];
-[BWSynchronizerNode masterClock];
-[BWSynchronizerNode setSourceClock:];
-[BWSynchronizerNode sourceClock];
-[BWSynchronizerNode handleDroppedSample:forInput:];
-[BWSynchronizerNode setQuantizationFrameDuration:];
-[BWSynchronizerNode nodeSubType];
-[BWSynchronizerNode didSelectFormat:forInput:];
-[BWSynchronizerNode nodeType];
```
