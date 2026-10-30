# `BLSHAsyncDisplayPowerResourceHint`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSDisplayPowerResourceHint`
- 1 instance variables, 4 properties, 2 instance methods, 2 class methods

## Instance variables

```
@"<BLSDisplayPowerResourceHint>" _hint;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BLSHAsyncDisplayPowerResourceHint hintWithHint:];
+[BLSHAsyncDisplayPowerResourceHint sharedHighPriorityQueue];
```

## Instance methods

```
-[BLSHAsyncDisplayPowerResourceHint updateState:];
-[BLSHAsyncDisplayPowerResourceHint initWithHint:];
```
