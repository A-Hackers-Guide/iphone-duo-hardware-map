# `_UIFindNavigatorResponder`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIResponder`
- Protocols: `UITextInputTraits_Private`, `UITextInput`
- 12 instance variables, 115 properties, 58 instance methods, 0 class methods

## Instance variables

```
B _canBecomeFirstResponder;
B _showsCollapsedInputView;
@"UIView" _collapsedInputView;
B _isChangingInputModes;
@"UITextPosition" beginningOfDocument;
@"UITextPosition" endOfDocument;
@"<UITextInputDelegate>" inputDelegate;
@"UITextRange" markedTextRange;
@"NSDictionary" markedTextStyle;
@"UITextRange" selectedTextRange;
@"<UITextInputTokenizer>" tokenizer;
@"_UIFindNavigatorViewController" _findNavigatorViewController;
```

## Properties

```
@property (T@"_UIFindNavigatorViewController",&,N,V_findNavigatorViewController) findNavigatorViewController;
@property (TB,R,N,V_isChangingInputModes) isChangingInputModes;
@property (TB,N,V_canBecomeFirstResponder) canBecomeFirstResponder;
@property (T@"NSString",?,C,N) recentInputIdentifier;
@property (T{_NSRange=QQ},?,N) validTextRange;
@property (T@"NSIndexSet",?,C,N) PINEntrySeparatorIndexes;
@property (T^{__CFCharacterSet=},?,N) textTrimmingSet;
@property (T@"UIColor",?,&,N) insertionPointColor;
@property (T@"UIColor",?,&,N) selectionBarColor;
@property (T@"UIColor",?,&,N) selectionHighlightColor;
@property (T@"UIImage",?,&,N) selectionDragDotImage;
@property (T@"UIColor",?,&,N) selectionBorderColor;
@property (Td,?,N) selectionBorderWidth;
@property (Td,?,N) selectionCornerRadius;
@property (T{UIEdgeInsets=dddd},?,N) selectionEdgeInsets;
@property (T@"UIColor",?,&,N) matchHighlightColor;
@property (T@"UIColor",?,&,N) underlineColorForTextAlternatives;
@property (T@"UIColor",?,&,N) underlineColorForSpelling;
@property (TQ,?,N) insertionPointWidth;
@property (Ti,?,N) textLoupeVisibility;
@property (Ti,?,N) textSelectionBehavior;
@property (T@,?,N) textSuggestionDelegate;
@property (TB,?,N) isSingleLineDocument;
@property (TB,?,N) contentsIsSingleValue;
@property (TB,?,N) hasDefaultContents;
@property (TB,?,N) acceptsPayloads;
@property (TB,?,N) acceptsEmoji;
@property (TB,?,N) acceptsInitialEmojiKeyboard;
@property (TB,?,N) acceptsDictationSearchResults;
@property (TB,?,N) useAutomaticEndpointing;
@property (TB,?,N) showDictationButton;
@property (TB,?,N) forceEnableDictation;
@property (TB,?,N) forceDisableDictation;
@property (TB,?,N) preferKeyboardInput;
@property (TB,?,N) forceSpellingDictation;
@property (TB,?,N) forceDefaultDictationInfo;
@property (Tq,?,N) forceDictationKeyboardType;
@property (TB,?,N) preferOnlineDictation;
@property (Ti,?,N) emptyContentReturnKeyType;
@property (TB,?,N) returnKeyGoesToNextResponder;
@property (TB,?,N) acceptsFloatingKeyboard;
@property (TB,?,N) forceFloatingKeyboard;
@property (T{UIEdgeInsets=dddd},?,N) floatingKeyboardEdgeInsets;
@property (TB,?,N) acceptsSplitKeyboard;
@property (TB,?,N) displaySecureTextUsingPlainText;
@property (TB,?,N) displaySecureEditsUsingPlainText;
@property (TB,?,N) learnsCorrections;
@property (TB,?,N) typingAdaptationDisabled;
@property (Ti,?,N) shortcutConversionType;
@property (TB,?,N) suppressReturnKeyStyling;
@property (TB,?,N) useInterfaceLanguageForLocalization;
@property (TB,?,N) deferBecomingResponder;
@property (TB,?,N) enablesReturnKeyOnNonWhiteSpaceContent;
@property (T@"NSString",?,C,N) autocorrectionContext;
@property (T@"NSString",?,C,N) responseContext;
@property (T@"UIInputContextHistory",?,&,N) inputContextHistory;
@property (TB,?,N) disableInputBars;
@property (TB,?,N) isCarPlayIdiom;
@property (Td,?,N) preferredInputViewHeight;
@property (Tq,?,N) textScriptType;
@property (TB,?,N) loadKeyboardsForSiriLanguage;
@property (T@"_UISupplementalLexicon",?,&,N) supplementalLexicon;
@property (T@"UIImage",?,&,N) supplementalLexiconAmbiguousItemIcon;
@property (TB,?,N) disablePrediction;
@property (TB,?,N) disableGenmojiCreationSuggestions;
@property (Tq,?,N) inlineCompletionType;
@property (Tq,?,N) allowsTextAnimationsType;
@property (TQ,?,N) keyboardSuggestionOptions;
@property (TB,?,N) hidePrediction;
@property (TB,?,N) disableHandwritingKeyboard;
@property (TB,?,N) intelligenceCursorEnabled;
@property (TB,?,N,GisDevicePasscodeEntry) devicePasscodeEntry;
@property (TB,?,R,N) wasEverSecureTextEntry;
@property (Tq,?,N) preferredKeyboardStyle;
@property (TB,?,N) prefersCompactNumberPadLayout;
@property (T@"UITextRange",?,R,N) textRangeForServicesInteraction;
@property (TQ,?) writingToolsAllowedInputOptions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
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
@property (T@"UITextRange",C,VselectedTextRange) selectedTextRange;
@property (T@"UITextRange",R,N,VmarkedTextRange) markedTextRange;
@property (T@"NSDictionary",C,N,VmarkedTextStyle) markedTextStyle;
@property (T@"UITextPosition",R,N,VbeginningOfDocument) beginningOfDocument;
@property (T@"UITextPosition",R,N,VendOfDocument) endOfDocument;
@property (T@"<UITextInputDelegate>",W,N,VinputDelegate) inputDelegate;
@property (T@"<UITextInputTokenizer>",R,N,Vtokenizer) tokenizer;
@property (T@"UIView",?,R,N) textInputView;
@property (Tq,?,N) selectionAffinity;
@property (T@,?,R,N) insertDictationResultPlaceholder;
@property (TB,?,N) supportsAdaptiveImageGlyph;
@property (TB,?,R,N,GisEditable) editable;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},?,R,N) unobscuredContentRect;
@property (TB,R,N) hasText;
```

## Instance methods

```
-[_UIFindNavigatorResponder markedTextStyle];
-[_UIFindNavigatorResponder firstRectForRange:];
-[_UIFindNavigatorResponder offsetFromPosition:toPosition:];
-[_UIFindNavigatorResponder endOfDocument];
-[_UIFindNavigatorResponder tokenizer];
-[_UIFindNavigatorResponder textInRange:];
-[_UIFindNavigatorResponder comparePosition:toPosition:];
-[_UIFindNavigatorResponder selectionRectsForRange:];
-[_UIFindNavigatorResponder baseWritingDirectionForPosition:inDirection:];
-[_UIFindNavigatorResponder textRangeFromPosition:toPosition:];
-[_UIFindNavigatorResponder caretRectForPosition:];
-[_UIFindNavigatorResponder positionFromPosition:offset:];
-[_UIFindNavigatorResponder hasText];
-[_UIFindNavigatorResponder setBaseWritingDirection:forRange:];
-[_UIFindNavigatorResponder beginningOfDocument];
-[_UIFindNavigatorResponder selectedTextRange];
-[_UIFindNavigatorResponder setSelectedTextRange:];
-[_UIFindNavigatorResponder replaceRange:withText:];
-[_UIFindNavigatorResponder markedTextRange];
-[_UIFindNavigatorResponder inputAccessoryView];
-[_UIFindNavigatorResponder setInputDelegate:];
-[_UIFindNavigatorResponder inputDelegate];
-[_UIFindNavigatorResponder acceptsInitialEmojiKeyboard];
-[_UIFindNavigatorResponder insertText:];
-[_UIFindNavigatorResponder unmarkText];
-[_UIFindNavigatorResponder inputAccessoryViewController];
-[_UIFindNavigatorResponder forceDisableDictation];
-[_UIFindNavigatorResponder inputView];
-[_UIFindNavigatorResponder setMarkedTextStyle:];
-[_UIFindNavigatorResponder keyboardAppearance];
-[_UIFindNavigatorResponder closestPositionToPoint:withinRange:];
-[_UIFindNavigatorResponder characterRangeByExtendingPosition:inDirection:];
-[_UIFindNavigatorResponder positionFromPosition:inDirection:offset:];
-[_UIFindNavigatorResponder takeTraitsFrom:];
-[_UIFindNavigatorResponder nextResponder];
-[_UIFindNavigatorResponder positionWithinRange:farthestInDirection:];
-[_UIFindNavigatorResponder closestPositionToPoint:];
-[_UIFindNavigatorResponder setMarkedText:selectedRange:];
-[_UIFindNavigatorResponder canBecomeFirstResponder];
-[_UIFindNavigatorResponder characterRangeAtPoint:];
-[_UIFindNavigatorResponder deleteBackward];
-[_UIFindNavigatorResponder setFindNavigatorViewController:];
-[_UIFindNavigatorResponder _alwaysRequireInlineCandidateView];
-[_UIFindNavigatorResponder _didPersistFindUI:];
-[_UIFindNavigatorResponder _disallowsPresentationOfKeyboardShortcutHUD];
-[_UIFindNavigatorResponder _ui_findNavigatorResponder];
-[_UIFindNavigatorResponder _willPersistFindUI:];
-[_UIFindNavigatorResponder becomeFirstResponderAndFocusFindField];
-[_UIFindNavigatorResponder findNavigatorViewController];
-[_UIFindNavigatorResponder hostingTypeForTraitCollection:];
-[_UIFindNavigatorResponder initWithFindNavigatorViewController:];
-[_UIFindNavigatorResponder inputDashboardViewController];
-[_UIFindNavigatorResponder isChangingInputModes];
-[_UIFindNavigatorResponder nextFirstResponder];
-[_UIFindNavigatorResponder responderForKeyboardAppearance];
-[_UIFindNavigatorResponder setCanBecomeFirstResponder:];
-[_UIFindNavigatorResponder textInputContextIdentifier];
-[_UIFindNavigatorResponder textInputMode];
```
