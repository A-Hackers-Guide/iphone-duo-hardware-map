# `UITextInputPrivate` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `UITextInput`, `UITextInputTokenizer`, `UITextInputTraits_Private`
- 0 instance variables, 10 properties, 84 instance methods, 0 class methods

## Properties

```
@property (T@"UITextInteractionAssistant",R,N) interactionAssistant;
@property (TB,?,R,N) supportsEmojiImageTextAttachments;
@property (Tq,?,N) selectionGranularity;
@property (Tq,?,R,N) cursorBehavior;
@property (T@"<UITextInputSuggestionDelegate>",?,R,N) textInputSuggestionDelegate;
@property (Tq,?,N) _textInputSource;
@property (T@"RTIInputSystemSourceSession",?,R,N) _rtiSourceSession;
@property (TB,?,R,N) supportsImagePaste;
@property (TB,?,N) _systemCursorAccessoriesDisabled;
@property (TB,?,N) automaticallyAdjustsWritingDirection;
```

## Instance methods

```
-[UITextInputPrivate textInputTraits];
-[UITextInputPrivate selectionRange];
-[UITextInputPrivate interactionAssistant];
-[UITextInputPrivate selectAll];
-[UITextInputPrivate hasContent];
-[UITextInputPrivate hasSelection];
-[UITextInputPrivate _autofillContext];
-[UITextInputPrivate insertTextSuggestion:];
-[UITextInputPrivate isAutoFillMode];
-[UITextInputPrivate addTextAlternatives:];
-[UITextInputPrivate visibleRect];
-[UITextInputPrivate insertDictationResult:withCorrectionIdentifier:];
-[UITextInputPrivate annotatedSubstringForRange:];
-[UITextInputPrivate insertEmojiImageTextAttachment:replacementRange:];
-[UITextInputPrivate _insertAttributedTextWithoutClosingTyping:];
-[UITextInputPrivate selectionGranularity];
-[UITextInputPrivate supportsEmojiImageTextAttachments];
-[UITextInputPrivate textColorForCaretSelection];
-[UITextInputPrivate correctedTypedText:rangeOfReplacement:];
-[UITextInputPrivate automaticallySelectedOverlay];
-[UITextInputPrivate requiresKeyEvents];
-[UITextInputPrivate setSelectionGranularity:];
-[UITextInputPrivate handleKeyWebEvent:withCompletionHandler:];
-[UITextInputPrivate replaceRange:withAnnotatedString:relativeReplacementRange:];
-[UITextInputPrivate automaticallyAdjustsWritingDirection];
-[UITextInputPrivate set_textInputSource:];
-[UITextInputPrivate textInputSuggestionDelegate];
-[UITextInputPrivate selectionInteractionAssistant];
-[UITextInputPrivate _selectionClipRect];
-[UITextInputPrivate rangeWithTextAlternatives:atPosition:];
-[UITextInputPrivate _attributedTextInRange:];
-[UITextInputPrivate _selectionIsFromActivationBehavior];
-[UITextInputPrivate removeEmojiAlternatives];
-[UITextInputPrivate setAutomaticallyAdjustsWritingDirection:];
-[UITextInputPrivate replaceRangeWithTextWithoutClosingTyping:replacementText:];
-[UITextInputPrivate _textInputSource];
-[UITextInputPrivate _visualSelectionRangeForExtent:forPoint:fromPosition:inDirection:];
-[UITextInputPrivate removeAnnotation:forRange:];
-[UITextInputPrivate metadataDictionariesForDictationResults];
-[UITextInputPrivate selectionContainerView];
-[UITextInputPrivate handleKeyWebEvent:];
-[UITextInputPrivate _canSuggestSupplementalItemsForCurrentSelection];
-[UITextInputPrivate _cancelChooseSupplementalItemToInsert];
-[UITextInputPrivate _caretTransformForPosition:];
-[UITextInputPrivate _chooseSupplementalItemToInsert:replacementRange:completionHandler:];
-[UITextInputPrivate _convertPointFromRenderSpace:];
-[UITextInputPrivate _convertPointToRenderSpace:textPosition:];
-[UITextInputPrivate _convertPointToRenderSpace:textRange:];
-[UITextInputPrivate _delayUntilRepeatInsertText:];
-[UITextInputPrivate _didHideCorrections];
-[UITextInputPrivate _hostViewForSelectionHandleWithTrailingHandle:];
-[UITextInputPrivate _insertAttributedText:withAnimation:completion:];
-[UITextInputPrivate _insertSupplementalItem:forString:replacementRange:];
-[UITextInputPrivate _insertionPointEnteredRange:string:supplementalItems:];
-[UITextInputPrivate _insertionPointExitedRangeWithSupplementalItems];
-[UITextInputPrivate _insertsSpaceAfterAcceptingPredictionForSupplementalItem:];
-[UITextInputPrivate _isInteractiveDespiteResponderStatus];
-[UITextInputPrivate _rangeAdjustmentGestureView];
-[UITextInputPrivate _rangeForTextKitRanges:];
-[UITextInputPrivate _replaceRange:withAttributedText:usingAnimation:completion:];
-[UITextInputPrivate _rtiSourceSession];
-[UITextInputPrivate _selectedTextRangeWillChangeToRange:];
-[UITextInputPrivate _selectionContainerViewAboveText];
-[UITextInputPrivate _sendCurrentLocationAction];
-[UITextInputPrivate _shouldRepeatInsertText:];
-[UITextInputPrivate _shouldSuppressSelectionCommands];
-[UITextInputPrivate _supportsTextKit2TextLists];
-[UITextInputPrivate _systemCursorAccessoriesDisabled];
-[UITextInputPrivate _usesContainerForSelectionHandleHitTesting];
-[UITextInputPrivate _willShowCorrections];
-[UITextInputPrivate acceptedAutoFillWord:];
-[UITextInputPrivate autoFillDidInsertWithExplicitInvocationMode:];
-[UITextInputPrivate canPerformDictationAction:];
-[UITextInputPrivate cursorBehavior];
-[UITextInputPrivate fontForCaretSelection];
-[UITextInputPrivate insertText:style:alternatives:];
-[UITextInputPrivate insertTextSuggestion:completionHandler:];
-[UITextInputPrivate modifierFlagsDidChangeFrom:to:];
-[UITextInputPrivate setBottomBufferHeight:];
-[UITextInputPrivate set_systemCursorAccessoriesDisabled:];
-[UITextInputPrivate streamingDictationDidBegin];
-[UITextInputPrivate streamingDictationDidEnd];
-[UITextInputPrivate supportsImagePaste];
-[UITextInputPrivate updateFloatingCursorAtPoint:animated:];
```
