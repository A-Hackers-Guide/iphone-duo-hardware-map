# `UIPressesEvent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIEvent`
- Protocols: `_UIEventComponentContaining`
- 3 instance variables, 6 properties, 32 instance methods, 0 class methods

## Instance variables

```
@"NSMutableSet" _allPresses;
@"NSHashTable" _terminalEventRegistrants;
@"UIPress" _lastPreparedPress;
```

## Properties

```
@property (T@"UIPress",&,N,V_lastPreparedPress) _lastPreparedPress;
@property (T@"NSSet",R,N) allPresses;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIPressesEvent _allWindows];
-[UIPressesEvent _cleanupAfterDispatch];
-[UIPressesEvent _removeComponents:];
-[UIPressesEvent _removeGestureRecognizer:fromComponents:];
-[UIPressesEvent _gestureRecognizersForWindow:];
-[UIPressesEvent subtype];
-[UIPressesEvent _cloneEvent];
-[UIPressesEvent _sendEventToGestureRecognizer:];
-[UIPressesEvent _pressesForResponder:withPhase:];
-[UIPressesEvent _directionalPressWithStrongestForce];
-[UIPressesEvent _respondersForWindow:];
-[UIPressesEvent _modifierFlags];
-[UIPressesEvent pressesForGestureRecognizer:];
-[UIPressesEvent _cancelComponents:];
-[UIPressesEvent _init];
-[UIPressesEvent _pressesForGestureRecognizer:withPhase:];
-[UIPressesEvent _pressesForPhase:];
-[UIPressesEvent _removePress:];
-[UIPressesEvent type];
-[UIPressesEvent _addGesturesForPress:];
-[UIPressesEvent _componentsForGestureRecognizer:];
-[UIPressesEvent _allPresses];
-[UIPressesEvent _lastPreparedPress];
-[UIPressesEvent _addPress:forDelayedDelivery:];
-[UIPressesEvent allPresses];
-[UIPressesEvent _registerForTerminalEvent:];
-[UIPressesEvent description];
-[UIPressesEvent set_lastPreparedPress:];
-[UIPressesEvent _pressesForWindow:];
-[UIPressesEvent _terminalRegistrantsForPressType:];
-[UIPressesEvent _unregisterForTerminalEvent:];
-[UIPressesEvent _componentsForWindow:];
```
