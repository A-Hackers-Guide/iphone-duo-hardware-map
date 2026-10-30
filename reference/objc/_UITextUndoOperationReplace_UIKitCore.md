# `_UITextUndoOperationReplace`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIUndoTextOperation`
- 3 instance variables, 0 properties, 5 instance methods, 0 class methods

## Instance variables

```
{_NSRange="location"Q"length"Q} _replacementRange;
@"NSAttributedString" _attributedString;
@"NSArray" _replacements;
```

## Instance methods

```
-[_UITextUndoOperationReplace _undoRedoForMultipleSelectedRanges];
-[_UITextUndoOperationReplace initWithAffectedRanges:inputController:replacementTextLength:];
-[_UITextUndoOperationReplace initWithAffectedRange:inputController:replacementRange:];
-[_UITextUndoOperationReplace _undoRedo];
-[_UITextUndoOperationReplace undoRedo];
```
