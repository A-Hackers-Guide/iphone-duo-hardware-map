# `SBPressSequenceObserver`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSUUID" _sosTriggerUUID;
@"NSString" _pressName;
@"SBPressCollector" _pressCollector;
```

## Properties

```
@property (T@"NSString",R,N,V_pressName) pressName;
@property (T@"SBPressCollector",R,N,V_pressCollector) pressCollector;
```

## Instance methods

```
-[SBPressSequenceObserver init];
-[SBPressSequenceObserver dealloc];
-[SBPressSequenceObserver _notePowerDownImminent];
-[SBPressSequenceObserver _setPressCollector:];
-[SBPressSequenceObserver initWithPressName:];
-[SBPressSequenceObserver noteDidBeginSOSWithUUID:];
-[SBPressSequenceObserver pressCollector];
-[SBPressSequenceObserver pressCollector:didCollectSequence:];
-[SBPressSequenceObserver pressName];
```
