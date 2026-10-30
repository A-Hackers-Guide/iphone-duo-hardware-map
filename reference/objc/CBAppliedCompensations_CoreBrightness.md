# `CBAppliedCompensations`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"<CBRampManagerI>" _rampManager;
d _maxHarmony;
d _maxBLR;
B _harmonyEnabled;
B _blrEnabled;
d _blrComp;
d _harmonyComp;
```

## Properties

```
@property (TB,N,V_harmonyEnabled) harmonyEnabled;
@property (TB,N,V_blrEnabled) blrEnabled;
@property (Td,R,V_harmonyComp) harmonyComp;
@property (Td,R,V_blrComp) blrComp;
```

## Instance methods

```
-[CBAppliedCompensations copyStatusInfo];
-[CBAppliedCompensations dealloc];
-[CBAppliedCompensations blrComp];
-[CBAppliedCompensations blrEnabled];
-[CBAppliedCompensations compensationFor:andMax:];
-[CBAppliedCompensations harmonyComp];
-[CBAppliedCompensations harmonyEnabled];
-[CBAppliedCompensations initWithRampManager:maxHarmony:maxBLR:];
-[CBAppliedCompensations setBlrEnabled:];
-[CBAppliedCompensations setHarmonyEnabled:];
```
