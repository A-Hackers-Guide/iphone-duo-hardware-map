# `UIDictationCursorPositionRestorer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
Q __selectionStartOffsetFromBeginningPriorToOperation;
Q __selectionEndOffsetFromEndPriorToOperation;
Q __selectionLengthPriorToOperation;
```

## Properties

```
@property (TQ,N,V__selectionStartOffsetFromBeginningPriorToOperation) _selectionStartOffsetFromBeginningPriorToOperation;
@property (TQ,N,V__selectionEndOffsetFromEndPriorToOperation) _selectionEndOffsetFromEndPriorToOperation;
@property (TQ,N,V__selectionLengthPriorToOperation) _selectionLengthPriorToOperation;
```

## Instance methods

```
-[UIDictationCursorPositionRestorer _restoreCursorLocationWithCompletion:];
-[UIDictationCursorPositionRestorer _selectionEndOffsetFromEndPriorToOperation];
-[UIDictationCursorPositionRestorer _selectionLengthPriorToOperation];
-[UIDictationCursorPositionRestorer _selectionStartOffsetFromBeginningPriorToOperation];
-[UIDictationCursorPositionRestorer _withCurrentSelectionOffsets:];
-[UIDictationCursorPositionRestorer saveCursorLocationAndRestoreAfterPerforming:completion:];
-[UIDictationCursorPositionRestorer setCursorToOffset:completion:];
-[UIDictationCursorPositionRestorer set_selectionEndOffsetFromEndPriorToOperation:];
-[UIDictationCursorPositionRestorer set_selectionLengthPriorToOperation:];
-[UIDictationCursorPositionRestorer set_selectionStartOffsetFromBeginningPriorToOperation:];
```
