# `CBColorFloorCoex`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBCoexSource`, `CBCoexFilter`
- 4 instance variables, 7 properties, 10 instance methods, 0 class methods

## Instance variables

```
f _currentAngle;
@"NSObject<OS_os_log>" _logHandle;
f currentNits;
Q _coexState;
```

## Properties

```
@property (Tf,VcurrentNits) currentNits;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<CBCoexSource>",R,N) source;
@property (TQ,R,N,V_coexState) coexState;
```

## Instance methods

```
-[CBColorFloorCoex currentNits];
-[CBColorFloorCoex init];
-[CBColorFloorCoex setCurrentNits:];
-[CBColorFloorCoex handleALSEvent:];
-[CBColorFloorCoex description];
-[CBColorFloorCoex source];
-[CBColorFloorCoex canPairWithALS:];
-[CBColorFloorCoex coexState];
-[CBColorFloorCoex handleSourceEvent:];
-[CBColorFloorCoex newFiltersForALS:logCategory:];
```
