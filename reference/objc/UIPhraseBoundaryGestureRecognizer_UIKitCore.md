# `UIPhraseBoundaryGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UILongPressGestureRecognizer`
- 5 instance variables, 4 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"UIDelayedAction" _secondDelayTimer;
B _secondDelayElapsed;
@"UIResponder<UITextInput>" _textInput;
d _secondDelay;
@ _userData;
```

## Properties

```
@property (T@"UIResponder<UITextInput>",W,N,V_textInput) textInput;
@property (Td,N,V_secondDelay) secondDelay;
@property (TB,R,N,V_secondDelayElapsed) secondDelayElapsed;
@property (T@,W,N,V_userData) userData;
```

## Instance methods

```
-[UIPhraseBoundaryGestureRecognizer _resetGestureRecognizer];
-[UIPhraseBoundaryGestureRecognizer setState:];
-[UIPhraseBoundaryGestureRecognizer initWithTarget:action:];
-[UIPhraseBoundaryGestureRecognizer userData];
-[UIPhraseBoundaryGestureRecognizer _startEnoughTimeElapsedTimer];
-[UIPhraseBoundaryGestureRecognizer setUserData:];
-[UIPhraseBoundaryGestureRecognizer setSecondDelay:];
-[UIPhraseBoundaryGestureRecognizer clearAllTimers];
-[UIPhraseBoundaryGestureRecognizer secondDelay];
-[UIPhraseBoundaryGestureRecognizer secondDelayElapsed];
-[UIPhraseBoundaryGestureRecognizer secondDelayElapsed:];
-[UIPhraseBoundaryGestureRecognizer setTextInput:];
-[UIPhraseBoundaryGestureRecognizer textInput];
```
