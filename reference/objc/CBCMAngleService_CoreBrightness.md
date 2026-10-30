# `CBCMAngleService`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBAngleServiceProtocol`
- 2 instance variables, 7 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"CMAngleManager" _cmManager;
B _started;
```

## Properties

```
@property (TB,R,GisStarted,V_started) started;
@property (Tf,R,GgetMinAngleDegrees) minAngleDegrees;
@property (Tf,R,GgetMaxAngleDegrees) maxAngleDegrees;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CBCMAngleService isStarted];
-[CBCMAngleService init];
-[CBCMAngleService stop];
-[CBCMAngleService dealloc];
-[CBCMAngleService description];
-[CBCMAngleService startAngleUpdatesToQueue:handler:];
-[CBCMAngleService canPairWithALS:];
-[CBCMAngleService getMaxAngleDegrees];
-[CBCMAngleService getMinAngleDegrees];
-[CBCMAngleService newFiltersForALS:logCategory:];
```
