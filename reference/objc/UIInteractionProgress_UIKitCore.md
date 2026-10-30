# `UIInteractionProgress`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 2 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSPointerArray" _observers;
d _previousPercentComplete;
d _previousUpdateTime;
d _mostRecentUpdateTime;
q _atLeastTwoUpdates;
d _percentComplete;
```

## Properties

```
@property (Td,R,N,V_percentComplete) percentComplete;
@property (Td,R,N) velocity;
```

## Instance methods

```
-[UIInteractionProgress percentComplete];
-[UIInteractionProgress init];
-[UIInteractionProgress velocity];
-[UIInteractionProgress description];
-[UIInteractionProgress endInteraction:];
-[UIInteractionProgress _indexOfObserver:];
-[UIInteractionProgress addProgressObserver:];
-[UIInteractionProgress endInteraction:finalVelocity:];
-[UIInteractionProgress numberOfObservers];
-[UIInteractionProgress removeProgressObserver:];
-[UIInteractionProgress setPercentComplete:];
```
