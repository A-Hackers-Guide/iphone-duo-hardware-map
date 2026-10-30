# `SBPIPSplitPIPStagingPauseDetector`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 17 instance variables, 9 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"SBPIPSplitPIPSettings" _settings;
d _pointsPerMillimeter;
@"SBTouchHistory" _touchHistory;
[128{?="location"{CGPoint="x"d"y"d}"timestamp"d"speed"d}] _samples;
Q _sampleCount;
Q _nextSampleIndex;
d _lastAccelerationVelocityY;
d _lastHeldTimestamp;
B _hasBrakedInTarget;
B _hasSlowedDownIntoTarget;
B _wasLastSampleInTarget;
B _holding;
d _heldDuration;
d _lastSampleTimestamp;
d _lastApproachStraightness;
d _currentSpeed;
d _recentPeakSpeed;
```

## Properties

```
@property (TB,R,N) hasBraked;
@property (TB,R,N) hasHeldLongEnough;
@property (TB,R,N,GisHolding,V_holding) holding;
@property (TB,R,N,GisSlowInTarget) slowInTarget;
@property (Td,R,N,V_heldDuration) heldDuration;
@property (Td,R,N,V_lastSampleTimestamp) lastSampleTimestamp;
@property (Td,R,N,V_lastApproachStraightness) lastApproachStraightness;
@property (Td,R,N,V_currentSpeed) currentSpeed;
@property (Td,R,N,V_recentPeakSpeed) recentPeakSpeed;
```

## Instance methods

```
-[SBPIPSplitPIPStagingPauseDetector reset];
-[SBPIPSplitPIPStagingPauseDetector isHolding];
-[SBPIPSplitPIPStagingPauseDetector currentSpeed];
-[SBPIPSplitPIPStagingPauseDetector recentPeakSpeed];
-[SBPIPSplitPIPStagingPauseDetector _appendSampleAtLocation:timestamp:speed:];
-[SBPIPSplitPIPStagingPauseDetector _pathStraightnessOverDuration:endingAt:];
-[SBPIPSplitPIPStagingPauseDetector _peakSpeedOverDuration:endingAt:];
-[SBPIPSplitPIPStagingPauseDetector hasBraked];
-[SBPIPSplitPIPStagingPauseDetector hasHeldLongEnough];
-[SBPIPSplitPIPStagingPauseDetector heldDuration];
-[SBPIPSplitPIPStagingPauseDetector initWithSettings:pointsPerMillimeter:];
-[SBPIPSplitPIPStagingPauseDetector isSlowInTarget];
-[SBPIPSplitPIPStagingPauseDetector lastApproachStraightness];
-[SBPIPSplitPIPStagingPauseDetector lastSampleTimestamp];
-[SBPIPSplitPIPStagingPauseDetector noteNoSampleUntilTimestamp:];
-[SBPIPSplitPIPStagingPauseDetector noteSampleAtLocation:timestamp:isInTarget:];
```
