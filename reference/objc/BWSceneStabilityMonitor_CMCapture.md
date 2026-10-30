# `BWSceneStabilityMonitor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 8 properties, 12 instance methods, 1 class methods

## Instance variables

```
B _isLastSceneStable;
f _stabilityMetric;
{?="value"q"timescale"i"flags"I"epoch"q} _stableStartTime;
{?="value"q"timescale"i"flags"I"epoch"q} _unstableStartTime;
B _isAFCompletedOnLastFrame;
B _processedSceneMotion;
f _sceneMotionOffsetX;
f _sceneMotionOffsetY;
{?="refRows"^i"refCols"^i"qualityX"f"qualityY"f"sceneStable"B"stabilityMetric"f} _aeMatrixStorage;
{?="offsetX"f"offsetY"f"qualityX"f"qualityY"f"height"i"width"i"refRowSum"^i"refColSum"^i"sceneStable"B"stabilityMetric"f"lastPTS"{?="value"q"timescale"i"flags"I"epoch"q}} _pixelSumStorage;
i _lastAFStatus;
```

## Properties

```
@property (TB,R,N,GisStable,V_isLastSceneStable) stable;
@property (Tf,R,N,V_stabilityMetric) stabilityMetric;
@property (T{?=qiIq},R,N,V_stableStartTime) stableStartTime;
@property (T{?=qiIq},R,N,V_unstableStartTime) unstableStartTime;
@property (TB,R,N,GisAFCompleted,V_isAFCompletedOnLastFrame) afCompleted;
@property (TB,R,N,V_processedSceneMotion) processedSceneMotion;
@property (Tf,R,N,V_sceneMotionOffsetX) sceneMotionOffsetX;
@property (Tf,R,N,V_sceneMotionOffsetY) sceneMotionOffsetY;
```

## Class methods

```
+[BWSceneStabilityMonitor initialize];
```

## Instance methods

```
-[BWSceneStabilityMonitor init];
-[BWSceneStabilityMonitor dealloc];
-[BWSceneStabilityMonitor reset];
-[BWSceneStabilityMonitor isStable];
-[BWSceneStabilityMonitor stableStartTime];
-[BWSceneStabilityMonitor stabilityMetric];
-[BWSceneStabilityMonitor calculateStabilityWithPixelBuffer:pts:metadataDictionary:forceSceneMotion:];
-[BWSceneStabilityMonitor isAFCompleted];
-[BWSceneStabilityMonitor processedSceneMotion];
-[BWSceneStabilityMonitor sceneMotionOffsetX];
-[BWSceneStabilityMonitor sceneMotionOffsetY];
-[BWSceneStabilityMonitor unstableStartTime];
```
