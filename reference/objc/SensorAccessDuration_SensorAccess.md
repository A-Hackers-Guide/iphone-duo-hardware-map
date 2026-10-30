# `SensorAccessDuration`

- Image: [`/System/Library/PrivateFrameworks/SensorAccess.framework/SensorAccess`](../userland/System__Library__PrivateFrameworks__SensorAccess.framework__SensorAccess.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
Q remainingMicrophoneDurationNanoSeconds;
Q remainingCameraDurationNanoSeconds;
Q remainingFaceIDDurationNanoSeconds;
```

## Properties

```
@property (TQ,N,VremainingMicrophoneDurationNanoSeconds) remainingMicrophoneDurationNanoSeconds;
@property (TQ,N,VremainingCameraDurationNanoSeconds) remainingCameraDurationNanoSeconds;
@property (TQ,N,VremainingFaceIDDurationNanoSeconds) remainingFaceIDDurationNanoSeconds;
@property (T@"NSString",N,R) description;
```

## Instance methods

```
-[SensorAccessDuration init];
-[SensorAccessDuration setRemainingMicrophoneDurationNanoSeconds:];
-[SensorAccessDuration init:::];
-[SensorAccessDuration description];
-[SensorAccessDuration setRemainingFaceIDDurationNanoSeconds:];
-[SensorAccessDuration remainingCameraDurationNanoSeconds];
-[SensorAccessDuration remainingFaceIDDurationNanoSeconds];
-[SensorAccessDuration remainingMicrophoneDurationNanoSeconds];
-[SensorAccessDuration setRemainingCameraDurationNanoSeconds:];
```
