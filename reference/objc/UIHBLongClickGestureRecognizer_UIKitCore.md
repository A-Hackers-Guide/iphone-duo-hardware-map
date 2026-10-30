# `UIHBLongClickGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- Protocols: `UIPressesEventTerminalRegistration`
- 3 instance variables, 6 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"UIPressesEvent" _registeredEventForTerminalEvents;
Q _lastSeenClickCount;
Q _numberOfClicksRequired;
```

## Properties

```
@property (TQ,N,V_numberOfClicksRequired) numberOfClicksRequired;
@property (T@"NSArray",R,N) allowedPressTypes;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIHBLongClickGestureRecognizer numberOfClicksRequired];
-[UIHBLongClickGestureRecognizer _resetGestureRecognizer];
-[UIHBLongClickGestureRecognizer _fail];
-[UIHBLongClickGestureRecognizer pressesCancelled:withEvent:];
-[UIHBLongClickGestureRecognizer pressesEnded:withEvent:];
-[UIHBLongClickGestureRecognizer setNumberOfClicksRequired:];
-[UIHBLongClickGestureRecognizer initWithTarget:action:];
-[UIHBLongClickGestureRecognizer pressesBegan:withEvent:];
-[UIHBLongClickGestureRecognizer pressesChanged:withEvent:];
-[UIHBLongClickGestureRecognizer _succeed];
-[UIHBLongClickGestureRecognizer _requiredClickCountMetForPress:];
-[UIHBLongClickGestureRecognizer pressesEventDidReceiveTerminal:];
-[UIHBLongClickGestureRecognizer _effectiveNumberOfClicksRequired];
-[UIHBLongClickGestureRecognizer _processPresses:];
```
