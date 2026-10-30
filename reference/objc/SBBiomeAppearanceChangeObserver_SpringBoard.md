# `SBBiomeAppearanceChangeObserver`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _observing;
@"NSDate" _lastAppearanceChangeTimestamp;
@"BPSPublisher" _appearancePublisher;
@"<BPSCancellable>" _cancellable;
```

## Properties

```
@property (T@"NSDate",&,N,V_lastAppearanceChangeTimestamp) lastAppearanceChangeTimestamp;
@property (TB,N,GisObserving,V_observing) observing;
@property (T@"BPSPublisher",R,N,V_appearancePublisher) appearancePublisher;
@property (T@"<BPSCancellable>",&,N,V_cancellable) cancellable;
```

## Instance methods

```
-[SBBiomeAppearanceChangeObserver init];
-[SBBiomeAppearanceChangeObserver dealloc];
-[SBBiomeAppearanceChangeObserver setCancellable:];
-[SBBiomeAppearanceChangeObserver invalidate];
-[SBBiomeAppearanceChangeObserver isObserving];
-[SBBiomeAppearanceChangeObserver _startObserving];
-[SBBiomeAppearanceChangeObserver cancellable];
-[SBBiomeAppearanceChangeObserver setObserving:];
-[SBBiomeAppearanceChangeObserver appearancePublisher];
-[SBBiomeAppearanceChangeObserver lastAppearanceChangeTimestamp];
-[SBBiomeAppearanceChangeObserver setLastAppearanceChangeTimestamp:];
```
