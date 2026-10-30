# `BKSMutableHIDUISensorMode`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BKSHIDUISensorMode`
- 0 instance variables, 20 properties, 24 instance methods, 0 class methods

## Properties

```
@property (TB,D,N) estimatedProximityMode;
@property (TB,D,N) proximityDetectionModeWasInherited;
@property (Tq,D,N) versionedPID;
@property (T@"NSString",&,D,N) reason;
@property (TQ,D,N) changeSource;
@property (Ti,D,N) proximityDetectionMode;
@property (Tq,D,N) displayState;
@property (TB,D,N) postEventWithCurrentDetectionMask;
@property (TB,D,N) digitizerEnabled;
@property (TB,D,N) pocketTouchesExpected;
@property (TB,D,N) tapToWakeEnabled;
@property (TB,D,N) coverGestureEnabled;
@property (TB,D,N) alwaysOnGesturesEnabled;
@property (TB,D,N) wakeOnSwipeEnabled;
@property (TB,D,N) wakeOnLongPressEnabled;
@property (TB,D,N) wakeOnTapThroughEnabled;
@property (TB,D,N) wakeOnSwipeThroughEnabled;
@property (TB,D,N) wakeOnLongPressThroughEnabled;
@property (T@"NSSet",C,D,N) multitouchHostStateKeys;
@property (T@"NSSet",C,D,N) proximityHostStateKeys;
```

## Instance methods

```
-[BKSMutableHIDUISensorMode setChangeSource:];
-[BKSMutableHIDUISensorMode setDisplayState:];
-[BKSMutableHIDUISensorMode setPocketTouchesExpected:];
-[BKSMutableHIDUISensorMode setTapToWakeEnabled:];
-[BKSMutableHIDUISensorMode copy];
-[BKSMutableHIDUISensorMode setEstimatedProximityMode:];
-[BKSMutableHIDUISensorMode initWithReason:];
-[BKSMutableHIDUISensorMode setReason:];
-[BKSMutableHIDUISensorMode setWakeOnLongTapThroughEnabled:];
-[BKSMutableHIDUISensorMode setProximityDetectionMode:];
-[BKSMutableHIDUISensorMode setWakeOnTapThroughEnabled:];
-[BKSMutableHIDUISensorMode setProximityDetectionModeWasInherited:];
-[BKSMutableHIDUISensorMode setWakeOnLongPressEnabled:];
-[BKSMutableHIDUISensorMode _setMultitouchSettingKey:enabled:];
-[BKSMutableHIDUISensorMode setMultitouchHostStateKeys:];
-[BKSMutableHIDUISensorMode setVersionedPID:];
-[BKSMutableHIDUISensorMode setWakeOnSwipeThroughEnabled:];
-[BKSMutableHIDUISensorMode copyWithZone:];
-[BKSMutableHIDUISensorMode setWakeOnSwipeEnabled:];
-[BKSMutableHIDUISensorMode setCoverGestureEnabled:];
-[BKSMutableHIDUISensorMode setAlwaysOnGesturesEnabled:];
-[BKSMutableHIDUISensorMode setPostEventWithCurrentDetectionMask:];
-[BKSMutableHIDUISensorMode setProximityHostStateKeys:];
-[BKSMutableHIDUISensorMode setDigitizerEnabled:];
```
