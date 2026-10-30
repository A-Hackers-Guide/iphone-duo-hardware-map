# `BWFrameRateGovernorNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 14 instance variables, 0 properties, 17 instance methods, 1 class methods

## Instance variables

```
B _dropsStillBracketFramesToMaintainConsistentFrameRate;
B _dropsStartupFramesWithUnstableAE;
i _aeStabilityTuning;
B _preservesMotionDataFromDroppedFrames;
{?="value"q"timescale"i"flags"I"epoch"q} _lastEmittedPTS;
{?="value"q"timescale"i"flags"I"epoch"q} _lastEmittedStreamingFrameDuration;
i _activeBracketSequenceRate;
@"BWMotionDataPreserver" _motionDataPreserver;
q _frameCount;
i _invalidFrameCount;
B _aeStableAfterStartStreaming;
i _aeStableTimeoutFrameCount;
i _ltmStableTimeoutFrameCount;
i _numFramesSinceAEBecameStable;
```

## Class methods

```
+[BWFrameRateGovernorNode initialize];
```

## Instance methods

```
-[BWFrameRateGovernorNode prepareForCurrentConfigurationToBecomeLive];
-[BWFrameRateGovernorNode renderSampleBuffer:forInput:];
-[BWFrameRateGovernorNode aeStabilityTuning];
-[BWFrameRateGovernorNode init];
-[BWFrameRateGovernorNode dealloc];
-[BWFrameRateGovernorNode preservesMotionDataFromDroppedFrames];
-[BWFrameRateGovernorNode dropsStartupFramesWithUnstableAE];
-[BWFrameRateGovernorNode dropsStillBracketFramesToMaintainConsistentFrameRate];
-[BWFrameRateGovernorNode setDropsStillBracketFramesToMaintainConsistentFrameRate:];
-[BWFrameRateGovernorNode setDropsStartupFramesWithUnstableAE:];
-[BWFrameRateGovernorNode didReachEndOfDataForConfigurationID:input:];
-[BWFrameRateGovernorNode setPreservesMotionDataFromDroppedFrames:];
-[BWFrameRateGovernorNode nodeSubType];
-[BWFrameRateGovernorNode didSelectFormat:forInput:];
-[BWFrameRateGovernorNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWFrameRateGovernorNode nodeType];
-[BWFrameRateGovernorNode setAeStabilityTuning:];
```
