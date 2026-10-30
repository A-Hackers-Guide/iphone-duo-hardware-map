# `BLSHBacklightHostObservable` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `BLSBacklightStateObservable`
- 0 instance variables, 3 properties, 5 instance methods, 0 class methods

## Properties

```
@property (Tq,R,N) backlightDisplayMode;
@property (TQ,R,N) backlightStateChangeTimestamp;
@property (T@"NSString",R,C,N) backlightStateDescription;
```

## Instance methods

```
-[BLSHBacklightHostObservable backlightStateChangeTimestamp];
-[BLSHBacklightHostObservable backlightDisplayMode];
-[BLSHBacklightHostObservable removeObserver:];
-[BLSHBacklightHostObservable backlightStateDescription];
-[BLSHBacklightHostObservable addObserver:];
```
