# `UITextIndirectNonEditableInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITextIndirectEditableInteraction`
- Protocols: `_UIKeyboardTextSelectionGestureControllerDelegate`
- 1 instance variables, 7 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"_UIKeyboardTextSelectionController" _textSelectionController;
```

## Properties

```
@property (T@"UIKeyboardTaskQueue",R,N) taskQueue;
@property (T@"_UIKeyboardTextSelectionController",R,N) textSelectionController;
@property (Td,?,R,N) timestampOfLastTouchesEnded;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UITextIndirectNonEditableInteraction taskQueue];
-[UITextIndirectNonEditableInteraction textSelectionController];
-[UITextIndirectNonEditableInteraction shouldAllowSelectionGestures:atPoint:toBegin:];
-[UITextIndirectNonEditableInteraction finishSetup];
-[UITextIndirectNonEditableInteraction shouldAllowWithTouchTypes:atPoint:toBegin:];
-[UITextIndirectNonEditableInteraction didEndGesture];
-[UITextIndirectNonEditableInteraction initWithView:];
-[UITextIndirectNonEditableInteraction dealloc];
-[UITextIndirectNonEditableInteraction _setupControllersIfNecessaryWithView:];
-[UITextIndirectNonEditableInteraction willBeginGesture];
```
