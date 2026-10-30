# `_UIFocusEventDelivery`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 2 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"UIFocusSystem" _focusSystem;
d _lastDeliveredTimestamp;
q _lastDeliveredMovement;
@"NSMutableSet" _keyboardPressEventForwardingMap;
```

## Properties

```
@property (T@"UIFocusSystem",R,N) focusSystem;
@property (T@"NSMutableSet",R,N,V_keyboardPressEventForwardingMap) keyboardPressEventForwardingMap;
```

## Instance methods

```
-[_UIFocusEventDelivery init];
-[_UIFocusEventDelivery focusSystem];
-[_UIFocusEventDelivery keyboardPressEventForwardingMap];
-[_UIFocusEventDelivery _movementParticipatesInCooldown:];
-[_UIFocusEventDelivery initWithFocusSystem:];
-[_UIFocusEventDelivery shouldDeliverFocusKeyboardEvent:toResponder:];
-[_UIFocusEventDelivery shouldSkipKeyboardShortcutLeaf:whenDeliveringFocusKeyboardEvent:toResponder:];
-[_UIFocusEventDelivery willDeliverFocusKeyboardEvent:];
```
