# `_UIKeyboardTextSelectionController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 16 properties, 73 instance methods, 0 class methods

## Instance variables

```
B _hasInteractionAssistant;
B _hasSelectionInteractionAssistant;
B _hasTextInputView;
@"UITextPosition" _cursorPosition;
@"UITextSelection" _selection;
@"UITextRange" _initialSelection;
q _selectionGranularity;
@"UITextRange" _selectionBase;
@"UIResponder<UITextInput>" _inputDelegate;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _caretRectForCursorPosition;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_caretRectForCursorPosition) caretRectForCursorPosition;
@property (T@"UITextRange",&,N,V_initialSelection) initialSelection;
@property (T@"UITextRange",&,N,V_selectionBase) selectionBase;
@property (T@"UIResponder<UITextInput>",R,W,N,V_inputDelegate) inputDelegate;
@property (T@"UITextInteractionAssistant",R,N) interactionAssistant;
@property (T@"<UISelectionInteractionAssistant>",R,N) selectionInteractionAssistant;
@property (Tq,N,V_selectionGranularity) selectionGranularity;
@property (T@"UITextPosition",&,N) cursorPosition;
@property (T@"UIView",R,N) textInputView;
@property (TB,R,N) hasCaretSelection;
@property (TB,R,N) hasRangedSelection;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) caretRectForFirstSelectedPosition;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) caretRectForLastSelectedPosition;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) caretRectForLeftmostSelectedPosition;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) caretRectForRightmostSelectedPosition;
@property (T@"UITextSelection",R,N) selection;
```

## Instance methods

```
-[_UIKeyboardTextSelectionController selectionDidChange];
-[_UIKeyboardTextSelectionController selection];
-[_UIKeyboardTextSelectionController textInputView];
-[_UIKeyboardTextSelectionController setSelectedTextRange:];
-[_UIKeyboardTextSelectionController setCursorPosition:];
-[_UIKeyboardTextSelectionController initialSelection];
-[_UIKeyboardTextSelectionController modifySelectionWithExtentPoint:executionContext:];
-[_UIKeyboardTextSelectionController beginSelectionChange];
-[_UIKeyboardTextSelectionController interactionAssistant];
-[_UIKeyboardTextSelectionController cursorPositionIsContainedByRange:];
-[_UIKeyboardTextSelectionController cursorPosition];
-[_UIKeyboardTextSelectionController endSelectionChange];
-[_UIKeyboardTextSelectionController inputDelegate];
-[_UIKeyboardTextSelectionController beginLoupeGestureAtPoint:translation:];
-[_UIKeyboardTextSelectionController selectionBase];
-[_UIKeyboardTextSelectionController beginRangedMagnifierAtPoint:];
-[_UIKeyboardTextSelectionController updateSelectionWithExtentPoint:executionContext:];
-[_UIKeyboardTextSelectionController beginSelectionWithBaseAtSelectionBoundaryInDirection:initialExtentPoint:executionContext:];
-[_UIKeyboardTextSelectionController endLoupeMagnifierAtPoint:];
-[_UIKeyboardTextSelectionController selectPositionAtBoundary:inDirection:executionContext:];
-[_UIKeyboardTextSelectionController setInitialSelection:];
-[_UIKeyboardTextSelectionController beginSelectionWithBasePositionAtBoundary:inDirection:withInitialExtentPoint:executionContext:];
-[_UIKeyboardTextSelectionController caretRectForCursorPosition];
-[_UIKeyboardTextSelectionController updateSelectionWithExtentPosition:executionContext:];
-[_UIKeyboardTextSelectionController endSelection];
-[_UIKeyboardTextSelectionController updateFloatingCursorAtPoint:];
-[_UIKeyboardTextSelectionController selectionGranularity];
-[_UIKeyboardTextSelectionController initWithInputDelegate:];
-[_UIKeyboardTextSelectionController hasRangedSelection];
-[_UIKeyboardTextSelectionController caretRectForFirstSelectedPosition];
-[_UIKeyboardTextSelectionController endLoupeGestureAtPoint:translation:];
-[_UIKeyboardTextSelectionController updateRangedMagnifierAtPoint:];
-[_UIKeyboardTextSelectionController caretRectForLeftmostSelectedPosition];
-[_UIKeyboardTextSelectionController setSelectionGranularity:];
-[_UIKeyboardTextSelectionController selectImmediatePositionAtBoundary:inDirection:executionContext:];
-[_UIKeyboardTextSelectionController updateSelectionWithExtentPoint:andExtentPosition:executionContext:];
-[_UIKeyboardTextSelectionController updateSelectionRects];
-[_UIKeyboardTextSelectionController setCaretRectForCursorPosition:];
-[_UIKeyboardTextSelectionController willBeginHighlighterGesture];
-[_UIKeyboardTextSelectionController updateSelectionWithExtentPoint:withBoundary:executionContext:];
-[_UIKeyboardTextSelectionController caretRectForRightmostSelectedPosition];
-[_UIKeyboardTextSelectionController willHandoffLoupeMagnifier];
-[_UIKeyboardTextSelectionController restartSelection];
-[_UIKeyboardTextSelectionController selectTextWithGranularity:atPoint:executionContext:];
-[_UIKeyboardTextSelectionController willBeginFloatingCursor:];
-[_UIKeyboardTextSelectionController selectPositionAtPoint:executionContext:];
-[_UIKeyboardTextSelectionController setRangedSelectionShouldShowGrabbers:];
-[_UIKeyboardTextSelectionController showSelectionCommands];
-[_UIKeyboardTextSelectionController hasCaretSelection];
-[_UIKeyboardTextSelectionController updateGestureRecognizers];
-[_UIKeyboardTextSelectionController textDidChange];
-[_UIKeyboardTextSelectionController switchToRangedSelection];
-[_UIKeyboardTextSelectionController updateImmediateSelectionWithExtentAtBoundary:inDirection:executionContext:];
-[_UIKeyboardTextSelectionController endFloatingCursor];
-[_UIKeyboardTextSelectionController updateSelectionWithExtentAtBoundary:inDirection:relativeToSelection:executionContext:];
-[_UIKeyboardTextSelectionController updateLoupeGestureAtPoint:translation:velocity:];
-[_UIKeyboardTextSelectionController selectPositionAtPoint:granularity:executionContext:];
-[_UIKeyboardTextSelectionController beginFloatingCursorAtPoint:];
-[_UIKeyboardTextSelectionController selectionInteractionAssistant];
-[_UIKeyboardTextSelectionController endRangedMagnifierAtPoint:];
-[_UIKeyboardTextSelectionController beginSelection];
-[_UIKeyboardTextSelectionController selectPositionAtPoint:granularity:completionHandler:];
-[_UIKeyboardTextSelectionController selectPositionAtBoundary:inDirection:relativeToSelection:executionContext:];
-[_UIKeyboardTextSelectionController updateSelectionWithExtentAtBoundary:inDirection:executionContext:];
-[_UIKeyboardTextSelectionController caretRectForLastSelectedPosition];
-[_UIKeyboardTextSelectionController boundedDeltaForTranslation:cursorLocationBase:];
-[_UIKeyboardTextSelectionController beginLoupeMagnifierAtPoint:];
-[_UIKeyboardTextSelectionController setSelectionBase:];
-[_UIKeyboardTextSelectionController selectTextWithGranularity:atPoint:completionHandler:];
-[_UIKeyboardTextSelectionController scrollSelectionToVisible];
-[_UIKeyboardTextSelectionController selectedRectInLineWithPoint:];
-[_UIKeyboardTextSelectionController updateLoupeMagnifierAtPoint:];
-[_UIKeyboardTextSelectionController resetCursorPosition];
```
