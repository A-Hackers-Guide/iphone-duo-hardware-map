# `UIForceStageInteractionProgress`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIInteractionProgress`
- Protocols: `NSObservable`, `NSObserver`
- 4 instance variables, 5 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSObservation" _observation;
B _completed;
B _started;
B _completesAtTargetState;
```

## Properties

```
@property (TB,N,V_completesAtTargetState) completesAtTargetState;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIForceStageInteractionProgress _reset];
-[UIForceStageInteractionProgress init];
-[UIForceStageInteractionProgress dealloc];
-[UIForceStageInteractionProgress receiveObservedValue:];
-[UIForceStageInteractionProgress completesAtTargetState];
-[UIForceStageInteractionProgress setCompletesAtTargetState:];
```
