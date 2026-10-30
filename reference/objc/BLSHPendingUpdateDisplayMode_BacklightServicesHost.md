# `BLSHPendingUpdateDisplayMode`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHPendingOperation`
- 4 instance variables, 21 properties, 18 instance methods, 2 class methods

## Instance variables

```
B _started;
B _completed;
q _currentDisplayMode;
q _targetDisplayMode;
```

## Properties

```
@property (TB,R,GisFullyCompleted) fullyCompleted;
@property (TB,R,GisStartedButIncomplete) startedButIncomplete;
@property (TB,R) isTwoPhaseUpdate;
@property (TB,R) isDirectRamp;
@property (Tq,R,V_currentDisplayMode) currentDisplayMode;
@property (Tq,R,V_targetDisplayMode) targetDisplayMode;
@property (T@"BLSHPendingUpdateDisplayMode",R,W) first;
@property (T@"BLSHPendingUpdateDisplayMode",R,W) last;
@property (T@"BLSHPendingUpdateDisplayMode",R,W) updateOperation;
@property (T@"BLSHPendingDirectRampDisplayMode",R,W) rampOperation;
@property (T@"BLSHPendingUpdateDisplayMode",R,W) inProgressOperation;
@property (Tq,R) type;
@property (TB,GisStarted,V_started) started;
@property (TB,GisCompleted,V_completed) completed;
@property (TB,?,R,GisBeforeDisplayBlankingChange) beforeDisplayBlankingChange;
@property (T@"BLSHPendingEnvironmentUpdateOperation",?,R) environmentUpdateOperation;
@property (T@"BLSHPendingFlipbookVisualStateOperation",?,R) flipbookOperation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BLSHPendingUpdateDisplayMode operationForUpdateFromCurrentDisplayMode:toTargetDisplayMode:];
+[BLSHPendingUpdateDisplayMode operationForUpdateFromCurrentDisplayMode:toTargetDisplayMode:withConfiguration:];
```

## Instance methods

```
-[BLSHPendingUpdateDisplayMode setCompleted:];
-[BLSHPendingUpdateDisplayMode last];
-[BLSHPendingUpdateDisplayMode initWithCurrentDisplayMode:targetDisplayMode:];
-[BLSHPendingUpdateDisplayMode isStartedButIncomplete];
-[BLSHPendingUpdateDisplayMode isDirectRamp];
-[BLSHPendingUpdateDisplayMode inProgressOperation];
-[BLSHPendingUpdateDisplayMode rampOperation];
-[BLSHPendingUpdateDisplayMode isFullyCompleted];
-[BLSHPendingUpdateDisplayMode currentDisplayMode];
-[BLSHPendingUpdateDisplayMode first];
-[BLSHPendingUpdateDisplayMode isStarted];
-[BLSHPendingUpdateDisplayMode setStarted:];
-[BLSHPendingUpdateDisplayMode targetDisplayMode];
-[BLSHPendingUpdateDisplayMode updateOperation];
-[BLSHPendingUpdateDisplayMode isCompleted];
-[BLSHPendingUpdateDisplayMode isTwoPhaseUpdate];
-[BLSHPendingUpdateDisplayMode type];
-[BLSHPendingUpdateDisplayMode description];
```
