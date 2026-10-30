# `_UIKeyboardInputModeSwitchContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 4 instance methods, 1 class methods

## Instance variables

```
@"UIKeyboardInputMode" _previousInputMode;
@"UIKeyboardInputMode" _nextInputMode;
```

## Properties

```
@property (T@"UIKeyboardInputMode",&,N,V_previousInputMode) previousInputMode;
@property (T@"UIKeyboardInputMode",&,N,V_nextInputMode) nextInputMode;
```

## Class methods

```
+[_UIKeyboardInputModeSwitchContext inputModeSwitchContextFromInputMode:toInputMode:];
```

## Instance methods

```
-[_UIKeyboardInputModeSwitchContext nextInputMode];
-[_UIKeyboardInputModeSwitchContext previousInputMode];
-[_UIKeyboardInputModeSwitchContext setNextInputMode:];
-[_UIKeyboardInputModeSwitchContext setPreviousInputMode:];
```
