# `UITextSelection`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 9 properties, 60 instance methods, 0 class methods

## Instance variables

```
@"UIResponder<UITextInputPrivate>" _document;
q _granularity;
@"UITextRange" _selectedRange;
@"UITextRange" _base;
@"UITextRange" _initialExtent;
B _isCommitting;
```

## Properties

```
@property (T@"UIResponder<UITextInputPrivate>",R,W,N,V_document) document;
@property (T@"UITextRange",&,N,V_selectedRange) selectedRange;
@property (Tq,N,V_granularity) granularity;
@property (TB,R,N) isValid;
@property (TB,R,N,V_isCommitting) isCommitting;
@property (TB,R,N) willSelectionChange;
@property (T@"UITextRange",&,N,V_base) base;
@property (T@"UITextRange",&,N,V_initialExtent) initialExtent;
@property (T@"DOMRange",R,N,G_domRange) domRange;
```

## Instance methods

```
-[UITextSelection setSelectedRange:];
-[UITextSelection selectedRange];
-[UITextSelection base];
-[UITextSelection clearSelection];
-[UITextSelection granularity];
-[UITextSelection collapseSelection];
-[UITextSelection setGranularity:];
-[UITextSelection _boundedOrInvertedSelectionRangeForExtent:forPoint:fromPosition:inDirection:];
-[UITextSelection commit];
-[UITextSelection setRangedSelectionInitialExtentToCurrentSelectionStart];
-[UITextSelection debugDescription];
-[UITextSelection document];
-[UITextSelection updateBaseAndInitialExtent];
-[UITextSelection alterSelectionGranularity:];
-[UITextSelection closestCaretRectForPoint:inSelection:];
-[UITextSelection setBase:];
-[UITextSelection setSelectionWithFirstPoint:secondPoint:];
-[UITextSelection pointAtEndOfLine:];
-[UITextSelection selectionChanged];
-[UITextSelection initWithDocument:];
-[UITextSelection dealloc];
-[UITextSelection selectedText];
-[UITextSelection setRangedSelectionExtentPoint:baseIsStart:];
-[UITextSelection _domRange];
-[UITextSelection offsetInMarkedText];
-[UITextSelection caretRectAtBeginOfDocument];
-[UITextSelection setRangedSelectionBaseToCurrentSelectionEnd];
-[UITextSelection invalidate];
-[UITextSelection setRangedSelectionExtentPoint:baseIsStart:allowFlipping:];
-[UITextSelection clearRangedSelectionInitialExtent];
-[UITextSelection caretRect];
-[UITextSelection moveCaretToBoundaryOfWhitespaceOrLine];
-[UITextSelection setRangedSelectionInitialExtentToCurrentSelectionEnd];
-[UITextSelection setSelectionWithPoint:];
-[UITextSelection setRangedSelectionWithExtentPoint:];
-[UITextSelection selectionRects];
-[UITextSelection isValid];
-[UITextSelection setGranularRangedSelectionWithExtentPoint:];
-[UITextSelection alterSelection:granularity:];
-[UITextSelection clipPoint:inRect:];
-[UITextSelection isRangedSelectionSpanningDocument];
-[UITextSelection aggressivelyExpandSelectionToSmartSelectionContainingCaretSelection];
-[UITextSelection aggressivelyExpandSelectionToWordContainingCaretSelection];
-[UITextSelection setRangedSelectionBaseToCurrentSelection];
-[UITextSelection setHybridSelectionWithPoint:];
-[UITextSelection underlineRectsForRange:];
-[UITextSelection caretRectAtEndOfDocument];
-[UITextSelection setRangedSelectionBaseToCurrentSelectionStart];
-[UITextSelection willSelectionChange];
-[UITextSelection wordContainingCaretSelection];
-[UITextSelection pointAtStartOfLine:];
-[UITextSelection increaseSelectionGranularity];
-[UITextSelection selectAll];
-[UITextSelection initialExtent];
-[UITextSelection hasEditableSelection];
-[UITextSelection smartExtendRangedSelection:downstream:];
-[UITextSelection setInitialExtent:];
-[UITextSelection _allowsSelectionInversion];
-[UITextSelection extendSelectionToPoint:];
-[UITextSelection isCommitting];
```
