# `CBColorALSSelectionPolicy`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBALSSelectionPolicyBase`
- Protocols: `CBALSSelectionPolicyProtocol`
- 3 instance variables, 4 properties, 3 instance methods, 0 class methods

## Instance variables

```
@"CBCoexTracker" _coexTracker;
@"<CBALSEventProtocol>" _lastGoodCairns;
d _lastGoodCairnsTimestamp;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CBColorALSSelectionPolicy dealloc];
-[CBColorALSSelectionPolicy select:];
-[CBColorALSSelectionPolicy initWithLogCategory:displayId:coexTracker:];
```
