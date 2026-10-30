# `UIKeyboardTypingStyleEstimator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 1 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSTimer" _tapTypingFlipTimer;
d _lastContinuousPathEvent;
Q _currentTypingStyle;
@"<UIKeyboardTypingStyleEstimatorDelegate>" _delegate;
```

## Properties

```
@property (T@"<UIKeyboardTypingStyleEstimatorDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[UIKeyboardTypingStyleEstimator setDelegate:];
-[UIKeyboardTypingStyleEstimator delegate];
-[UIKeyboardTypingStyleEstimator _setTypingStyleEstimation:];
-[UIKeyboardTypingStyleEstimator beganContinuousPath];
-[UIKeyboardTypingStyleEstimator cancelContinuousPath];
-[UIKeyboardTypingStyleEstimator currentTypingStyleEstimation];
-[UIKeyboardTypingStyleEstimator endedContinuousPath];
-[UIKeyboardTypingStyleEstimator tapTypedKey];
```
