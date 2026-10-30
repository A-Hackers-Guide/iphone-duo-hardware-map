# `UITextInput_Internal` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `_UITextSelectionDirectionNavigation_Internal`
- 0 instance variables, 2 properties, 85 instance methods, 0 class methods

## Properties

```
@property (T@"UIResponder<UITextInput>",R,N,G_proxyTextInput) __content;
@property (T@"UIView<UITextInputPrivate>",?,R,N) _textSelectingContainer;
```

## Instance methods

```
-[UITextInput_Internal _deleteToStartOfLine];
-[UITextInput_Internal _deleteToEndOfLine];
-[UITextInput_Internal _range:intersectsRange:];
-[UITextInput_Internal _deleteByWord];
-[UITextInput_Internal _deleteToEndOfParagraph];
-[UITextInput_Internal _rangeOfEnclosingWord:];
-[UITextInput_Internal _hasMarkedText];
-[UITextInput_Internal _textRangeFromNSRange:];
-[UITextInput_Internal _characterBeforeCaretSelection];
-[UITextInput_Internal _deleteForwardByWord];
-[UITextInput_Internal _positionFromPosition:pastTextUnit:inDirection:];
-[UITextInput_Internal _selectionAffinity];
-[UITextInput_Internal _replaceCurrentWordWithText:];
-[UITextInput_Internal _selectedNSRange];
-[UITextInput_Internal _rangeOfTextUnit:enclosingPosition:];
-[UITextInput_Internal _rangeOfSentenceEnclosingPosition:];
-[UITextInput_Internal _expandSelectionToBackwardDeletionClusterWithReinsertionOut:];
-[UITextInput_Internal _extendCurrentSelection:];
-[UITextInput_Internal _fontForCaretSelection];
-[UITextInput_Internal _hasMarkedTextOrRangedSelection];
-[UITextInput_Internal _textLengthToDeleteBeforeSelectedRangeForSmartDelete];
-[UITextInput_Internal _selectionAtDocumentStart];
-[UITextInput_Internal _proxyTextInput];
-[UITextInput_Internal _selectionAtDocumentEnd];
-[UITextInput_Internal _deleteForwardAndNotify:];
-[UITextInput_Internal _findBoundaryPositionClosestToPosition:withGranularity:];
-[UITextInput_Internal _expandSelectionToStartOfWordBeforeCaretSelection];
-[UITextInput_Internal _intersectionOfRange:andRange:];
-[UITextInput_Internal _moveCurrentSelection:];
-[UITextInput_Internal _rangeOfSmartSelectionIncludingRange:];
-[UITextInput_Internal _range:isEqualToRange:];
-[UITextInput_Internal _fullText];
-[UITextInput_Internal _scrollRectToVisible:animated:];
-[UITextInput_Internal _unmarkText];
-[UITextInput_Internal _setSelectionToPosition:];
-[UITextInput_Internal _deleteBackwardAndNotify:];
-[UITextInput_Internal _selectAll];
-[UITextInput_Internal _textRangeFromDirectionalRange:];
-[UITextInput_Internal _setGestureRecognizers];
-[UITextInput_Internal _rangeOfText:endingAtPosition:];
-[UITextInput_Internal _rangeOfParagraphEnclosingPosition:];
-[UITextInput_Internal _indexForTextPosition:];
-[UITextInput_Internal _shouldPerformUICalloutBarButtonReplaceAction:forText:checkAutocorrection:];
-[UITextInput_Internal _setCaretSelectionAtEndOfSelection];
-[UITextInput_Internal _clampedpositionFromPosition:offset:];
-[UITextInput_Internal _fullRange];
-[UITextInput_Internal _replaceDocumentWithText:];
-[UITextInput_Internal _rangeOfLineEnclosingPosition:];
-[UITextInput_Internal _rangeFromCurrentRangeWithDelta:];
-[UITextInput_Internal _selectedRangeWithinMarkedText];
-[UITextInput_Internal _setAttributedMarkedText:selectedRange:];
-[UITextInput_Internal _characterInRelationToPosition:amount:];
-[UITextInput_Internal _findPleasingWordBoundaryFromPosition:];
-[UITextInput_Internal _nsrangeForTextRange:];
-[UITextInput_Internal _wordContainingCaretSelection];
-[UITextInput_Internal _textColorForCaretSelection];
-[UITextInput_Internal _setMarkedText:selectedRange:];
-[UITextInput_Internal _positionAtStartOfWords:beforePosition:];
-[UITextInput_Internal _characterAfterCaretSelection];
-[UITextInput_Internal _rangeSpanningTextUnit:andPosition:];
-[UITextInput_Internal _usesAsynchronousProtocol];
-[UITextInput_Internal _expandSelectionToStartOfWordsBeforeCaretSelection:];
-[UITextInput_Internal _underlineRectsByDocumentLineForSelectionRange:];
-[UITextInput_Internal _range:containsRange:];
-[UITextInput_Internal _isEmptySelection];
-[UITextInput_Internal _characterInRelationToCaretSelection:];
-[UITextInput_Internal _setSelectedTextRange:withAffinityDownstream:];
-[UITextInput_Internal _positionWithinRange:farthestInDirection:];
-[UITextInput_Internal _positionFromPosition:inDirection:offset:withAffinityDownstream:];
-[UITextInput_Internal _selectionAtWordStart];
-[UITextInput_Internal _characterInRelationToRangedSelection:];
-[UITextInput_Internal _normalizedStringForRangeComparison:];
-[UITextInput_Internal _transpose];
-[UITextInput_Internal _textSelectingContainer];
-[UITextInput_Internal _setInternalGestureRecognizers];
-[UITextInput_Internal _shouldSuppressSelectionHandles];
-[UITextInput_Internal _implementsEditMenu];
-[UITextInput_Internal _isInteractiveTextSelectionDisabled];
-[UITextInput_Internal _lastRectForRange:];
-[UITextInput_Internal _logWarningForMenuControllerUsage];
-[UITextInput_Internal _performTextFormattingRestoration];
-[UITextInput_Internal _pointerInteractionDelegate];
-[UITextInput_Internal _prepareForTextFormattingRestoration];
-[UITextInput_Internal _shouldAcceptAutocorrection];
-[UITextInput_Internal _shouldShowEditMenu];
```
