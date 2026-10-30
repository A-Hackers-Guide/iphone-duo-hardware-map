# `CAMBufferObservance`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _removedOnceEnabled;
B _fulfilled;
B _enabled;
@? _predicate;
```

## Properties

```
@property (TB,N,GisFulfilled,V_fulfilled) fulfilled;
@property (TB,N,GisEnabled,V_enabled) enabled;
@property (TB,R,N,GisRemovedOnceEnabled,V_removedOnceEnabled) removedOnceEnabled;
@property (T@?,R,C,N,V_predicate) predicate;
```

## Instance methods

```
-[CAMBufferObservance isEnabled];
-[CAMBufferObservance setEnabled:];
-[CAMBufferObservance predicate];
-[CAMBufferObservance isFulfilled];
-[CAMBufferObservance fulfillWithChange:];
-[CAMBufferObservance initWithPredicate:removedOnceEnabled:];
-[CAMBufferObservance isRemovedOnceEnabled];
-[CAMBufferObservance setFulfilled:];
-[CAMBufferObservance setupObservanceForBuffer:];
-[CAMBufferObservance shouldBeFulfilledByChange:];
-[CAMBufferObservance teardownObservanceForBuffer:];
```
