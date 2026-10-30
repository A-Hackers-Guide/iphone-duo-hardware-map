# `UIHBClickGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- Protocols: `UIPressesEventTerminalRegistration`
- 4 instance variables, 7 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"UIPressesEvent" _registeredEventForTerminalEvents;
Q _lastSeenClickCount;
B _recognizesOnPressPhaseBegan;
Q _clickCount;
```

## Properties

```
@property (TQ,N,V_clickCount) clickCount;
@property (TB,N,V_recognizesOnPressPhaseBegan) recognizesOnPressPhaseBegan;
@property (T@"NSArray",R,N) allowedPressTypes;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIHBClickGestureRecognizer _resetGestureRecognizer];
-[UIHBClickGestureRecognizer clickCount];
-[UIHBClickGestureRecognizer _fail];
-[UIHBClickGestureRecognizer pressesCancelled:withEvent:];
-[UIHBClickGestureRecognizer pressesEnded:withEvent:];
-[UIHBClickGestureRecognizer initWithTarget:action:];
-[UIHBClickGestureRecognizer pressesBegan:withEvent:];
-[UIHBClickGestureRecognizer pressesChanged:withEvent:];
-[UIHBClickGestureRecognizer setClickCount:];
-[UIHBClickGestureRecognizer _succeed];
-[UIHBClickGestureRecognizer setRecognizesOnPressPhaseBegan:];
-[UIHBClickGestureRecognizer pressesEventDidReceiveTerminal:];
-[UIHBClickGestureRecognizer _processPresses:];
-[UIHBClickGestureRecognizer recognizesOnPressPhaseBegan];
```
