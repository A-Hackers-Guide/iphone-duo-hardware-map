# `_UITextUndoOperationTyping`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIUndoTextOperation`
- 3 instance variables, 0 properties, 7 instance methods, 0 class methods

## Instance variables

```
{_NSRange="location"Q"length"Q} _replacementRange;
@"NSMutableAttributedString" _attributedString;
@"NSArray" _replacements;
```

## Instance methods

```
-[_UITextUndoOperationTyping _undoRedoForMultipleSelectedRanges];
-[_UITextUndoOperationTyping initWithAffectedRanges:inputController:replacementTextLength:];
-[_UITextUndoOperationTyping supportsCoalescing];
-[_UITextUndoOperationTyping initWithAffectedRange:inputController:replacementRange:];
-[_UITextUndoOperationTyping coalesceAffectedRange:replacementRange:selectedRange:textStorage:];
-[_UITextUndoOperationTyping _undoRedo];
-[_UITextUndoOperationTyping undoRedo];
```
