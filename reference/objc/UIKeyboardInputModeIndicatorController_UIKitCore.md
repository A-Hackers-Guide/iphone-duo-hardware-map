# `UIKeyboardInputModeIndicatorController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 19 instance methods, 1 class methods

## Instance variables

```
@"<UIKeyboardInputModeIndicatorControllerDelegate>" _delegate;
@"UIDelayedAction" _dismissAction;
@"UIDelayedAction" _idleAction;
```

## Properties

```
@property (T@"UIDelayedAction",&,N,V_dismissAction) dismissAction;
@property (T@"UIDelayedAction",&,N,V_idleAction) idleAction;
@property (T@"<UIKeyboardInputModeIndicatorControllerDelegate>",W,N,V_delegate) delegate;
```

## Class methods

```
+[UIKeyboardInputModeIndicatorController enabled];
```

## Instance methods

```
-[UIKeyboardInputModeIndicatorController inputModeChanged];
-[UIKeyboardInputModeIndicatorController clear];
-[UIKeyboardInputModeIndicatorController hardwareKeyboardDettached];
-[UIKeyboardInputModeIndicatorController enabled];
-[UIKeyboardInputModeIndicatorController inputModeUpdateTime];
-[UIKeyboardInputModeIndicatorController inputModeSelectorDidOpen];
-[UIKeyboardInputModeIndicatorController willResignActive];
-[UIKeyboardInputModeIndicatorController keyboardWindowEnabled:];
-[UIKeyboardInputModeIndicatorController idleAction];
-[UIKeyboardInputModeIndicatorController setIdleAction:];
-[UIKeyboardInputModeIndicatorController showIndicatorWithReason:force:];
-[UIKeyboardInputModeIndicatorController setDelegate:];
-[UIKeyboardInputModeIndicatorController idle];
-[UIKeyboardInputModeIndicatorController delegate];
-[UIKeyboardInputModeIndicatorController setDismissAction:];
-[UIKeyboardInputModeIndicatorController dismissAction];
-[UIKeyboardInputModeIndicatorController keyPressed];
-[UIKeyboardInputModeIndicatorController dismissIndicator];
-[UIKeyboardInputModeIndicatorController presentIndicatorWithReason:force:];
```
