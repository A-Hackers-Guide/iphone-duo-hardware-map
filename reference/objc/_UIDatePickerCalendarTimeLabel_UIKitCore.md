# `_UIDatePickerCalendarTimeLabel`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIIndirectScribbleInteractionDelegate`, `UITextInputTraits_Private`, `UIKeyInput`
- 14 instance variables, 120 properties, 84 instance methods, 1 class methods

## Instance variables

```
@"UIIndirectScribbleInteraction" _scribbleInteraction;
@"UITextField" _hiddenField;
@"UIView" _inputView;
{CGSize="width"d"height"d} _lastSize;
B _roundsToMinuteInterval;
B _allowsTextInput;
@"_UIDatePickerCalendarTimeFormat" _timeFormat;
@"<_UIDatePickerCalendarTimeLabelDelegate>" _delegate;
@"_UIDatePickerCalendarTimeValueStore" _inputValue;
Q _insertedDigitCount;
@"_UIDatePickerCalendarTimeLabelStateMachineContext" _stateContext;
q _inputScope;
@"NSNumberFormatter" _inputFormatter;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _timeOfDayRect;
```

## Properties

```
@property (TB,N,V_allowsTextInput) allowsTextInput;
@property (TQ,N,V_insertedDigitCount) insertedDigitCount;
@property (T@"_UIDatePickerCalendarTimeLabelStateMachineContext",R,N,V_stateContext) stateContext;
@property (Tq,R,N,V_inputScope) inputScope;
@property (T@"NSNumberFormatter",&,N,V_inputFormatter) inputFormatter;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) hourRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) minuteRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_timeOfDayRect) timeOfDayRect;
@property (TB,R,N) scribbleInteractionIsActive;
@property (T@"_UIDatePickerCalendarTimeFormat",&,N,V_timeFormat) timeFormat;
@property (Tq,N) minuteInterval;
@property (TB,N,V_roundsToMinuteInterval) roundsToMinuteInterval;
@property (Tq,R,N) decrementBehaviour;
@property (T@"<_UIDatePickerCalendarTimeLabelDelegate>",W,N,V_delegate) delegate;
@property (T@"UIFont",C,N) font;
@property (T@"NSString",R,N) text;
@property (T@"NSAttributedString",R,N) attributedText;
@property (T@"NSString",C,N) hourText;
@property (T@"NSString",C,N) minuteText;
@property (T@"NSString",R,N) timeOfDayText;
@property (T@"_UIDatePickerCalendarTimeValueStore",R,N,V_inputValue) inputValue;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
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
@property (TB,R,N) hasText;
```

## Class methods

```
+[_UIDatePickerCalendarTimeLabel supportsScribbleInteraction];
```

## Instance methods

```
-[_UIDatePickerCalendarTimeLabel isSingleLineDocument];
-[_UIDatePickerCalendarTimeLabel focusGroupIdentifier];
-[_UIDatePickerCalendarTimeLabel hasText];
-[_UIDatePickerCalendarTimeLabel stateContext];
-[_UIDatePickerCalendarTimeLabel hourRect];
-[_UIDatePickerCalendarTimeLabel setMinuteInterval:];
-[_UIDatePickerCalendarTimeLabel insertText:];
-[_UIDatePickerCalendarTimeLabel text];
-[_UIDatePickerCalendarTimeLabel becomeFirstResponder];
-[_UIDatePickerCalendarTimeLabel _canChangeFirstResponder:toResponder:];
-[_UIDatePickerCalendarTimeLabel layoutSubviews];
-[_UIDatePickerCalendarTimeLabel keyCommands];
-[_UIDatePickerCalendarTimeLabel roundsToMinuteInterval];
-[_UIDatePickerCalendarTimeLabel keyboardType];
-[_UIDatePickerCalendarTimeLabel resignFirstResponder];
-[_UIDatePickerCalendarTimeLabel canBecomeFocused];
-[_UIDatePickerCalendarTimeLabel setDelegate:];
-[_UIDatePickerCalendarTimeLabel tintColorDidChange];
-[_UIDatePickerCalendarTimeLabel inputView];
-[_UIDatePickerCalendarTimeLabel stateMachineUpdateFromState:toState:];
-[_UIDatePickerCalendarTimeLabel initWithTimeFormat:minuteInterval:];
-[_UIDatePickerCalendarTimeLabel endEditingWheels];
-[_UIDatePickerCalendarTimeLabel timeFormat];
-[_UIDatePickerCalendarTimeLabel minuteInterval];
-[_UIDatePickerCalendarTimeLabel displaysTimeOfDayLabel];
-[_UIDatePickerCalendarTimeLabel attributedText];
-[_UIDatePickerCalendarTimeLabel decrementBehaviour];
-[_UIDatePickerCalendarTimeLabel _treatMinutesAsHoursForState:];
-[_UIDatePickerCalendarTimeLabel delegate];
-[_UIDatePickerCalendarTimeLabel minuteRect];
-[_UIDatePickerCalendarTimeLabel takeTraitsFrom:];
-[_UIDatePickerCalendarTimeLabel beginEditingWheels];
-[_UIDatePickerCalendarTimeLabel willBeginWritingInScribbleInteraction];
-[_UIDatePickerCalendarTimeLabel font];
-[_UIDatePickerCalendarTimeLabel pushCurrentStateIntoUI];
-[_UIDatePickerCalendarTimeLabel canBecomeFirstResponder];
-[_UIDatePickerCalendarTimeLabel initWithFrame:];
-[_UIDatePickerCalendarTimeLabel deleteBackward];
-[_UIDatePickerCalendarTimeLabel canPerformAction:withSender:];
-[_UIDatePickerCalendarTimeLabel setRoundsToMinuteInterval:];
-[_UIDatePickerCalendarTimeLabel setFont:];
-[_UIDatePickerCalendarTimeLabel allowsTextInput];
-[_UIDatePickerCalendarTimeLabel pushCurrentStateIntoUIAndNotify];
-[_UIDatePickerCalendarTimeLabel _resetTextInput];
-[_UIDatePickerCalendarTimeLabel editingInteractionConfiguration];
-[_UIDatePickerCalendarTimeLabel _digits:fromText:count:];
-[_UIDatePickerCalendarTimeLabel _pointIsInsideHourSide:];
-[_UIDatePickerCalendarTimeLabel _roundInputToClosestIntervalIfNeeded];
-[_UIDatePickerCalendarTimeLabel _stateMachineSendEvent:];
-[_UIDatePickerCalendarTimeLabel _suppressSoftwareKeyboard];
-[_UIDatePickerCalendarTimeLabel _uiTest_becomeFirstResponder];
-[_UIDatePickerCalendarTimeLabel _uiTest_resignFirstResponder];
-[_UIDatePickerCalendarTimeLabel applyTextAttributesForState:inputScope:updater:];
-[_UIDatePickerCalendarTimeLabel attributedTextWithRanges:];
-[_UIDatePickerCalendarTimeLabel didReceiveDownArrowKey:];
-[_UIDatePickerCalendarTimeLabel didReceiveLeftArrowKey:];
-[_UIDatePickerCalendarTimeLabel didReceiveRightArrowKey:];
-[_UIDatePickerCalendarTimeLabel didReceiveUpArrowKey:];
-[_UIDatePickerCalendarTimeLabel didTapInputLabelAtLocation:];
-[_UIDatePickerCalendarTimeLabel hourText];
-[_UIDatePickerCalendarTimeLabel indirectScribbleInteraction:didFinishWritingInElement:];
-[_UIDatePickerCalendarTimeLabel indirectScribbleInteraction:focusElementIfNeeded:referencePoint:completion:];
-[_UIDatePickerCalendarTimeLabel indirectScribbleInteraction:frameForElement:];
-[_UIDatePickerCalendarTimeLabel indirectScribbleInteraction:isElementFocused:];
-[_UIDatePickerCalendarTimeLabel indirectScribbleInteraction:requestElementsInRect:completion:];
-[_UIDatePickerCalendarTimeLabel indirectScribbleInteraction:shouldDelayFocusForElement:];
-[_UIDatePickerCalendarTimeLabel indirectScribbleInteraction:willBeginWritingInElement:];
-[_UIDatePickerCalendarTimeLabel inputFormatter];
-[_UIDatePickerCalendarTimeLabel inputScope];
-[_UIDatePickerCalendarTimeLabel inputValue];
-[_UIDatePickerCalendarTimeLabel insertedDigitCount];
-[_UIDatePickerCalendarTimeLabel minuteText];
-[_UIDatePickerCalendarTimeLabel processTapOutside];
-[_UIDatePickerCalendarTimeLabel scribbleInteractionIsActive];
-[_UIDatePickerCalendarTimeLabel setAllowsTextInput:];
-[_UIDatePickerCalendarTimeLabel setHourText:];
-[_UIDatePickerCalendarTimeLabel setInputFormatter:];
-[_UIDatePickerCalendarTimeLabel setInputScope:];
-[_UIDatePickerCalendarTimeLabel setInsertedDigitCount:];
-[_UIDatePickerCalendarTimeLabel setMinuteText:];
-[_UIDatePickerCalendarTimeLabel setTimeFormat:];
-[_UIDatePickerCalendarTimeLabel timeOfDayRect];
-[_UIDatePickerCalendarTimeLabel timeOfDayText];
-[_UIDatePickerCalendarTimeLabel wheelChanged];
```
