# `_UIUndoTextOperation`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"UITextInputController" _inputController;
@"NSArray" _affectedRanges;
{_NSRange="location"Q"length"Q} _affectedRange;
```

## Properties

```
@property (T{_NSRange=QQ},N,V_affectedRange) affectedRange;
@property (T@"NSArray",C,N,V_affectedRanges) affectedRanges;
@property (T@"UITextInputController",W,N,V_inputController) inputController;
```

## Instance methods

```
-[_UIUndoTextOperation inputController];
-[_UIUndoTextOperation supportsCoalescing];
-[_UIUndoTextOperation setInputController:];
-[_UIUndoTextOperation undoRedo];
-[_UIUndoTextOperation affectedRange];
-[_UIUndoTextOperation affectedRanges];
-[_UIUndoTextOperation initWithAffectedRange:inputController:];
-[_UIUndoTextOperation initWithAffectedRanges:inputController:];
-[_UIUndoTextOperation setAffectedRange:];
-[_UIUndoTextOperation setAffectedRanges:];
```
