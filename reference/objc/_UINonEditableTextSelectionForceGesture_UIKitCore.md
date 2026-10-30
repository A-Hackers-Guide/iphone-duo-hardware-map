# `_UINonEditableTextSelectionForceGesture`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UITextSelectionForceGesture`
- Protocols: `_UIKeyboardTextSelectionGestureControllerDelegate`
- 3 instance variables, 9 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"<_UINonEditableTextSelectionForceGestureDelegate>" forceGestureDelegate;
@"_UIKeyboardTextSelectionController" _textSelectionController;
@"_UIKeyboardTextSelectionGestureController" _gestureController;
```

## Properties

```
@property (T@"_UIKeyboardTextSelectionController",&,N,V_textSelectionController) textSelectionController;
@property (T@"_UIKeyboardTextSelectionGestureController",&,N,V_gestureController) gestureController;
@property (T@"<_UINonEditableTextSelectionForceGestureDelegate>",W,N,VforceGestureDelegate) forceGestureDelegate;
@property (T@"UIKeyboardTaskQueue",R,N) taskQueue;
@property (Td,?,R,N) timestampOfLastTouchesEnded;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UINonEditableTextSelectionForceGesture taskQueue];
-[_UINonEditableTextSelectionForceGesture textSelectionController];
-[_UINonEditableTextSelectionForceGesture dealloc];
-[_UINonEditableTextSelectionForceGesture initWithTextInput:];
-[_UINonEditableTextSelectionForceGesture willBeginGesture];
-[_UINonEditableTextSelectionForceGesture _shouldDelayUntilForceLevelRequirementIsMet];
-[_UINonEditableTextSelectionForceGesture forceGestureDelegate];
-[_UINonEditableTextSelectionForceGesture gestureController];
-[_UINonEditableTextSelectionForceGesture setForceGestureDelegate:];
-[_UINonEditableTextSelectionForceGesture setGestureController:];
-[_UINonEditableTextSelectionForceGesture setTextSelectionController:];
```
