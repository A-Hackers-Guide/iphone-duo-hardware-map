# `_UIRIPDeliveryRecord`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 3 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSMapTable" _receivers;
q _phase;
@"UIEvent" _event;
@"NSSet" _presses;
```

## Properties

```
@property (Tq,R,N,V_phase) phase;
@property (T@"UIEvent",R,N,V_event) event;
@property (T@"NSSet",R,N,V_presses) presses;
```

## Instance methods

```
-[_UIRIPDeliveryRecord phase];
-[_UIRIPDeliveryRecord event];
-[_UIRIPDeliveryRecord description];
-[_UIRIPDeliveryRecord presses];
-[_UIRIPDeliveryRecord diffToRecord:press:];
-[_UIRIPDeliveryRecord initWithPresses:inPhase:withEvent:];
-[_UIRIPDeliveryRecord responder:class:receivedPresses:inPhase:withEvent:];
```
