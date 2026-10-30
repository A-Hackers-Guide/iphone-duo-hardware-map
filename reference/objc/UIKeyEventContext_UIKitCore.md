# `UIKeyEventContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
B _documentIsEditable;
B _shouldInsertChar;
B _shouldEvaluateForInputSystemHandling;
@"UIKeyEvent" _keyEvent;
```

## Properties

```
@property (T@"UIKeyEvent",R,N,V_keyEvent) keyEvent;
@property (TB,N,V_documentIsEditable) documentIsEditable;
@property (TB,N,V_shouldInsertChar) shouldInsertChar;
@property (TB,N,V_shouldEvaluateForInputSystemHandling) shouldEvaluateForInputSystemHandling;
```

## Instance methods

```
-[UIKeyEventContext init];
-[UIKeyEventContext documentIsEditable];
-[UIKeyEventContext initWithKeyEvent:];
-[UIKeyEventContext keyEvent];
-[UIKeyEventContext setDocumentIsEditable:];
-[UIKeyEventContext setShouldEvaluateForInputSystemHandling:];
-[UIKeyEventContext setShouldInsertChar:];
-[UIKeyEventContext shouldEvaluateForInputSystemHandling];
-[UIKeyEventContext shouldInsertChar];
```
