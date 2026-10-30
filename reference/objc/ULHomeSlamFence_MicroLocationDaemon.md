# `ULHomeSlamFence`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 13 instance methods, 0 class methods

## Instance variables

```
f _radiusSquare;
f _deltaPositionX;
f _deltaPositionY;
@"NSUUID" _trajectoryUUID;
```

## Properties

```
@property (Tf,N,V_radiusSquare) radiusSquare;
@property (Tf,N,V_deltaPositionX) deltaPositionX;
@property (Tf,N,V_deltaPositionY) deltaPositionY;
@property (T@"NSUUID",&,N,V_trajectoryUUID) trajectoryUUID;
```

## Instance methods

```
-[ULHomeSlamFence setDeltaPositionY:];
-[ULHomeSlamFence deltaPositionY];
-[ULHomeSlamFence deltaPositionX];
-[ULHomeSlamFence setDeltaPositionX:];
-[ULHomeSlamFence _resetState];
-[ULHomeSlamFence trajectoryUUID];
-[ULHomeSlamFence setTrajectoryUUID:];
-[ULHomeSlamFence didFenceCrossWithOdometryEntry:];
-[ULHomeSlamFence _checkFenceCrossAndResetIfNeeded];
-[ULHomeSlamFence _updateStateWithEntry:];
-[ULHomeSlamFence initWithFenceRadius:];
-[ULHomeSlamFence radiusSquare];
-[ULHomeSlamFence setRadiusSquare:];
```
