# `UIKBInputDelegateManager`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIKeyInput`, `_UITextSelectionDirectionNavigation_Internal`
- 13 instance variables, 42 properties, 150 instance methods, 2 class methods

## Instance variables

```
Q m_delegateConformanceType;
Q m_originalDelegateConformanceType;
B _forwardingInputDelegateConformsToWKInteraction;
B _forwardingInputDelegateConformsToAsyncTextInputClient;
B _forwardingInputDelegateConformsToBETextInput;
B m_firstResponderAdoptsTextInput;
B _shouldRespectForwardingInputDelegate;
B _insideKeyInputDelegateCall;
@"<UIKeyboardImplStateProtocol>" _keyboardStateDelegate;
@"UIResponder<UIKeyInput>" _keyInputDelegate;
@"UITextInteractionSelectableInputDelegate" _selectableDelegate;
@"UIResponder<UIKeyInput>" _forwardingInputDelegate;
@"UIResponder<UIAsyncTextInputClient>" _asyncInputDelegate;
```

## Properties

```
@property (T@"UIResponder<UIKeyInput>",&,N,V_keyInputDelegate) keyInputDelegate;
@property (T@"UIResponder<UIAsyncTextInputClient>",&,N,V_asyncInputDelegate) asyncInputDelegate;
@property (T@"UITextInteractionSelectableInputDelegate",&,N,V_selectableDelegate) selectableDelegate;
@property (TB,N,V_insideKeyInputDelegateCall) insideKeyInputDelegateCall;
@property (T@"<UIKeyboardImplStateProtocol>",W,N,V_keyboardStateDelegate) keyboardStateDelegate;
@property (T@,R,N) asyncCapableInputDelegate;
@property (T@"UIResponder<UIKeyInput>",W,N,V_forwardingInputDelegate) forwardingInputDelegate;
@property (TB,N,V_shouldRespectForwardingInputDelegate) shouldRespectForwardingInputDelegate;
@property (T@"<UIKeyboardInput>",R,N) legacyInputDelegate;
@property (TQ,R,N) delegateConformanceType;
@property (T@"UITextInputTraits",R,N) textInputTraits;
@property (T@"UITextInteractionAssistant",R,N) textInteractionAssistant;
@property (T@"UITextSelectionDisplayInteraction",R,N) selectionDisplayInteraction;
@property (TB,N) continuousSpellCheckingEnabled;
@property (TB,R,N) hasAsyncCapableInputDelegate;
@property (T@"UIView",R,N) automaticallySelectedOverlay;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) selectionClipRect;
@property (TB,R,N) hasText;
@property (Tq,?,N) autocapitalizationType;
@property (Tq,?,N) autocorrectionType;
@property (Tq,?,N) spellCheckingType;
@property (Tq,?,N) smartQuotesType;
@property (Tq,?,N) smartDashesType;
@property (Tq,?,N) smartInsertDeleteType;
@property (Tq,?,N) inlinePredictionType;
@property (Tq,?,N) mathExpressionCompletionType;
@property (Tq,?,N) grammarCheckingType;
@property (Tq,?,N) keyboardType;
@property (Tq,?,N) keyboardAppearance;
@property (Tq,?,N) returnKeyType;
@property (TB,?,N) enablesReturnKeyAutomatically;
@property (TB,?,N,GisSecureTextEntry) secureTextEntry;
@property (T@"NSString",?,C,N) textContentType;
@property (T@"UITextInputPasswordRules",?,C,N) passwordRules;
@property (Tq,?) writingToolsBehavior;
@property (TQ,?) allowedWritingToolsResultOptions;
@property (T@"UIConversationContext",?,&,N) conversationContext;
@property (TB,?,N) allowsNumberPadPopover;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIKBInputDelegateManager isAsyncTextInputEnabled];
+[UIKBInputDelegateManager rangeForTextRange:document:];
```

## Instance methods

```
-[UIKBInputDelegateManager _deleteToStartOfLine];
-[UIKBInputDelegateManager _moveToEndOfWord:withHistory:];
-[UIKBInputDelegateManager asyncWebKitInteractionDelegate];
-[UIKBInputDelegateManager _deleteToEndOfLine];
-[UIKBInputDelegateManager offsetFromPosition:toPosition:];
-[UIKBInputDelegateManager clearForwardingInputDelegateAndResign:];
-[UIKBInputDelegateManager delegateAsResponder];
-[UIKBInputDelegateManager endOfDocument];
-[UIKBInputDelegateManager asyncCapableInputDelegate];
-[UIKBInputDelegateManager hasAsyncCapableInputDelegate];
-[UIKBInputDelegateManager _moveUp:withHistory:];
-[UIKBInputDelegateManager _moveLeft:withHistory:];
-[UIKBInputDelegateManager _range:intersectsRange:];
-[UIKBInputDelegateManager _firstResponderDidChange:];
-[UIKBInputDelegateManager textInRange:];
-[UIKBInputDelegateManager _deleteByWord];
-[UIKBInputDelegateManager textInputTraits];
-[UIKBInputDelegateManager comparePosition:toPosition:];
-[UIKBInputDelegateManager selectionRectsForRange:];
-[UIKBInputDelegateManager asyncInputDelegate];
-[UIKBInputDelegateManager baseWritingDirectionForPosition:inDirection:];
-[UIKBInputDelegateManager insertTextSuggestion:];
-[UIKBInputDelegateManager textRangeFromPosition:toPosition:];
-[UIKBInputDelegateManager textInteractionAssistant];
-[UIKBInputDelegateManager caretRectForPosition:];
-[UIKBInputDelegateManager _deleteToEndOfParagraph];
-[UIKBInputDelegateManager inputSystemSourceSession];
-[UIKBInputDelegateManager hasMarkedText];
-[UIKBInputDelegateManager _moveRight:withHistory:];
-[UIKBInputDelegateManager setAttributedMarkedText:selectedRange:];
-[UIKBInputDelegateManager webInputDelegate];
-[UIKBInputDelegateManager _moveToStartOfWord:withHistory:];
-[UIKBInputDelegateManager positionFromPosition:offset:];
-[UIKBInputDelegateManager hasText];
-[UIKBInputDelegateManager _hasMarkedText];
-[UIKBInputDelegateManager _textRangeFromNSRange:];
-[UIKBInputDelegateManager callKeyboardWillDismiss];
-[UIKBInputDelegateManager textInputView];
-[UIKBInputDelegateManager _textSelectingContainer];
-[UIKBInputDelegateManager delegateConformanceType];
-[UIKBInputDelegateManager _characterBeforeCaretSelection];
-[UIKBInputDelegateManager setBaseWritingDirection:forRange:];
-[UIKBInputDelegateManager beginningOfDocument];
-[UIKBInputDelegateManager updateRespectForwardingInputDelegateFlagInDestination];
-[UIKBInputDelegateManager selectedTextRange];
-[UIKBInputDelegateManager setSelectedTextRange:];
-[UIKBInputDelegateManager clearDelegate];
-[UIKBInputDelegateManager replaceRange:withText:];
-[UIKBInputDelegateManager addTextAlternatives:];
-[UIKBInputDelegateManager _moveToEndOfDocument:withHistory:];
-[UIKBInputDelegateManager insertAttributedText:];
-[UIKBInputDelegateManager _moveToStartOfParagraph:withHistory:];
-[UIKBInputDelegateManager _deleteForwardByWord];
-[UIKBInputDelegateManager insertDictationResult:];
-[UIKBInputDelegateManager handleClearWithInsertBeforeAdvance:];
-[UIKBInputDelegateManager markedTextRange];
-[UIKBInputDelegateManager setupResponderChangeListeners];
-[UIKBInputDelegateManager insideKeyInputDelegateCall];
-[UIKBInputDelegateManager insertText:];
-[UIKBInputDelegateManager unmarkText];
-[UIKBInputDelegateManager updateSelectableInputDelegateIfNecessary];
-[UIKBInputDelegateManager _deleteBackwardAndNotify:reinsertText:];
-[UIKBInputDelegateManager init];
-[UIKBInputDelegateManager __content];
-[UIKBInputDelegateManager unmarkText:];
-[UIKBInputDelegateManager _textLengthToDeleteBeforeSelectedRangeForSmartDelete];
-[UIKBInputDelegateManager updateDelegateConformanceForRemoteTraits];
-[UIKBInputDelegateManager _selectionAtDocumentStart];
-[UIKBInputDelegateManager setAsyncInputDelegate:];
-[UIKBInputDelegateManager _deleteForwardAndNotify:];
-[UIKBInputDelegateManager privateInputDelegate];
-[UIKBInputDelegateManager dealloc];
-[UIKBInputDelegateManager selectedText];
-[UIKBInputDelegateManager textFirstRect];
-[UIKBInputDelegateManager requestTextRectsForString:withCompletionHandler:];
-[UIKBInputDelegateManager _moveCurrentSelection:];
-[UIKBInputDelegateManager privateKeyInputDelegate];
-[UIKBInputDelegateManager selectionIsEndOfWord];
-[UIKBInputDelegateManager delegateRespondsToSelector:];
-[UIKBInputDelegateManager insertTextAfterSelection:];
-[UIKBInputDelegateManager _moveDown:withHistory:];
-[UIKBInputDelegateManager canHandleInputDelegateCommandAction:];
-[UIKBInputDelegateManager moveSelectionToEndOfWord];
-[UIKBInputDelegateManager applyAutocorrection:toString:withCompletionHandler:];
-[UIKBInputDelegateManager _moveToEndOfParagraph:withHistory:];
-[UIKBInputDelegateManager _moveToStartOfLine:withHistory:];
-[UIKBInputDelegateManager correctedTypedText:rangeOfReplacement:];
-[UIKBInputDelegateManager _deleteBackwardWhileOverridingContextAndNotifyAtEnd:deletionCount:reinsertTextInLoop:];
-[UIKBInputDelegateManager legacyInputDelegate];
-[UIKBInputDelegateManager _moveToStartOfDocument:withHistory:];
-[UIKBInputDelegateManager _setSelectionToPosition:];
-[UIKBInputDelegateManager automaticallySelectedOverlay];
-[UIKBInputDelegateManager changedSelection];
-[UIKBInputDelegateManager applyAutocorrection:toString:shouldUnderline:withCompletionHandler:];
-[UIKBInputDelegateManager callShouldReplaceExtendedRange:withText:includeMarkedText:];
-[UIKBInputDelegateManager storeDelegateConformance];
-[UIKBInputDelegateManager setDelegate:];
-[UIKBInputDelegateManager attributedMarkedText];
-[UIKBInputDelegateManager removeAnnotation:removalRangeLength:forAnnotationRange:contextBeforeLength:];
-[UIKBInputDelegateManager requiresKeyEvents];
-[UIKBInputDelegateManager selectionClipRect];
-[UIKBInputDelegateManager requestTextContextForAutocorrectionWithCompletionHandler:];
-[UIKBInputDelegateManager setKeyInputDelegate:];
-[UIKBInputDelegateManager _rangeOfText:endingAtPosition:];
-[UIKBInputDelegateManager privateInputDelegateRespectingForwardingDelegate:];
-[UIKBInputDelegateManager handleKeyWebEvent:withCompletionHandler:];
-[UIKBInputDelegateManager setKeyboardStateDelegate:];
-[UIKBInputDelegateManager setShouldRespectForwardingInputDelegate:];
-[UIKBInputDelegateManager keyboardStateDelegate];
-[UIKBInputDelegateManager markedText];
-[UIKBInputDelegateManager delegateRespectingForwardingDelegate:];
-[UIKBInputDelegateManager insertText:updateInputSource:];
-[UIKBInputDelegateManager insertText:withEnumeratedAnimationStyle:];
-[UIKBInputDelegateManager setContinuousSpellCheckingEnabled:];
-[UIKBInputDelegateManager adjustSelection:completionHandler:];
-[UIKBInputDelegateManager textLastRect];
-[UIKBInputDelegateManager callShouldDeleteBackwardWithCount:];
-[UIKBInputDelegateManager setInsideKeyInputDelegateCall:];
-[UIKBInputDelegateManager selectionIsWord];
-[UIKBInputDelegateManager transposeCharacters];
-[UIKBInputDelegateManager selectionDisplayInteraction];
-[UIKBInputDelegateManager tintColor];
-[UIKBInputDelegateManager shouldSuppressUpdateCandidateView];
-[UIKBInputDelegateManager forwardingInputDelegate];
-[UIKBInputDelegateManager continuousSpellCheckingEnabled];
-[UIKBInputDelegateManager setForwardingInputDelegate:];
-[UIKBInputDelegateManager insertSupplementalItem:candidate:replacementRange:];
-[UIKBInputDelegateManager selectorForCommand:];
-[UIKBInputDelegateManager keyInputDelegate];
-[UIKBInputDelegateManager requestDocumentContext:completionHandler:];
-[UIKBInputDelegateManager _setMarkedText:selectedRange:];
-[UIKBInputDelegateManager _moveToEndOfLine:withHistory:];
-[UIKBInputDelegateManager shiftKeyStateChangedFrom:to:];
-[UIKBInputDelegateManager shouldRespectForwardingInputDelegate];
-[UIKBInputDelegateManager selectableDelegate];
-[UIKBInputDelegateManager collapseSelectionAndAdjustByOffset:];
-[UIKBInputDelegateManager setSelectableDelegate:];
-[UIKBInputDelegateManager shouldDeleteForward];
-[UIKBInputDelegateManager delegateAdoptsWebTextInputPrivate];
-[UIKBInputDelegateManager replaceRange:oldText:withText:forReplaceAction:];
-[UIKBInputDelegateManager insertText:alternatives:style:];
-[UIKBInputDelegateManager deleteBackward];
-[UIKBInputDelegateManager textInputDelegate];
-[UIKBInputDelegateManager canPerformAction:withSender:];
-[UIKBInputDelegateManager replaceRange:oldText:withAttributedText:forReplaceAction:];
-[UIKBInputDelegateManager _deleteBackwardAndNotify:reinsertText:overrideOriginalContextBeforeInputWith:];
-[UIKBInputDelegateManager visibleTextRect];
-[UIKBInputDelegateManager handleKeyWebEvent:];
-[UIKBInputDelegateManager _adjustedTextRange:givenRange:contextBeforeLength:relativeToDocument:];
-[UIKBInputDelegateManager replaceAnnotationRange:contextBeforeLength:withAnnotatedString:relativeReplacementRange:];
```
