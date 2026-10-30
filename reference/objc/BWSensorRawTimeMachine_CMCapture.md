# `BWSensorRawTimeMachine`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 0 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"BWSensorRawTimeMachineConfiguration" _configuration;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
[5@"NSMutableArray"] _storedBuffers;
[5i] _maxCounts;
[5i] _worstCaseStoredBufferCounts;
i _nonIncreasingPTSFailureCount;
i _nonIncreasingPTSRadarThreshold;
```

## Class methods

```
+[BWSensorRawTimeMachine initialize];
```

## Instance methods

```
-[BWSensorRawTimeMachine flush];
-[BWSensorRawTimeMachine dealloc];
-[BWSensorRawTimeMachine initWithConfiguration:];
-[BWSensorRawTimeMachine attachMatchingHueMapToMainSampleBuffer:mainPTS:mainExposureTime:frameRate:];
-[BWSensorRawTimeMachine copyMatchingSampleBufferWithFrameType:mainPTS:mainExposureTime:frameRate:];
-[BWSensorRawTimeMachine flushFramesUpToPTS:frameRate:];
-[BWSensorRawTimeMachine insertFrame:];
-[BWSensorRawTimeMachine insertHueMap:];
-[BWSensorRawTimeMachine insertSemanticMasks:];
```
