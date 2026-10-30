# `_UITextDocumentInterface`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIInputViewControllerInterface`
- Protocols: `UITextDocumentProxy`, `UITextDocumentProxy_Private`
- 4 instance variables, 38 properties, 45 instance methods, 0 class methods

## Instance variables

```
@"<_UITextDocumentInterfaceDelegate>" _delegate;
@"_UIInputViewControllerState" _controllerState;
@"_UIInputViewControllerOutput" _controllerOutput;
@"TIKeyboardOutput" _keyboardOutput;
```

## Properties

```
@property (T@"_UIInputViewControllerState",&,N,G_controllerState,V_controllerState) controllerState;
@property (T@"_UIInputViewControllerOutput",&,N,G_controllerOutput,V_controllerOutput) controllerOutput;
@property (T@"TIDocumentState",R,N,G_documentState) documentState;
@property (T@"TITextInputTraits",R,N,G_textInputTraits) textInputTraits;
@property (T@"TIKeyboardOutput",R,N,G_keyboardOutput,V_keyboardOutput) keyboardOutput;
@property (T@"<_UITextDocumentInterfaceDelegate>",W,N,G_delegate,V_delegate) delegate;
@property (T@"NSString",R,N) documentContextBeforeInput;
@property (T@"NSString",R,N) documentContextAfterInput;
@property (T@"NSString",R,N) selectedText;
@property (T@"UITextInputMode",R,N) documentInputMode;
@property (T@"NSUUID",R,C,N) documentIdentifier;
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
@property (T@"NSString",R,N) markedText;
@property (TB,R,N) needsInputModeSwitchKey;
```

## Instance methods

```
-[_UITextDocumentInterface documentInputMode];
-[_UITextDocumentInterface hasText];
-[_UITextDocumentInterface autocapitalizationType];
-[_UITextDocumentInterface smartDashesType];
-[_UITextDocumentInterface insertText:];
-[_UITextDocumentInterface unmarkText];
-[_UITextDocumentInterface documentContextBeforeInput];
-[_UITextDocumentInterface selectedText];
-[_UITextDocumentInterface spellCheckingType];
-[_UITextDocumentInterface _textInputTraits];
-[_UITextDocumentInterface keyboardType];
-[_UITextDocumentInterface setForwardingInterface:];
-[_UITextDocumentInterface _delegate];
-[_UITextDocumentInterface setDelegate:];
-[_UITextDocumentInterface smartInsertDeleteType];
-[_UITextDocumentInterface enablesReturnKeyAutomatically];
-[_UITextDocumentInterface _controllerState];
-[_UITextDocumentInterface documentIdentifier];
-[_UITextDocumentInterface markedText];
-[_UITextDocumentInterface keyboardAppearance];
-[_UITextDocumentInterface _createControllerOutputIfNecessary];
-[_UITextDocumentInterface _setHasDictation:];
-[_UITextDocumentInterface needsInputModeSwitchKey];
-[_UITextDocumentInterface _setInputModeList:touchBegan:fromLocation:updatePoint:];
-[_UITextDocumentInterface _setPrimaryLanguage:];
-[_UITextDocumentInterface _willPerformOutputOperation];
-[_UITextDocumentInterface adjustTextPositionByCharacterOffset:];
-[_UITextDocumentInterface documentContextAfterInput];
-[_UITextDocumentInterface _setProceedShouldReturnIfPossibleForASP];
-[_UITextDocumentInterface _handleInputViewControllerState:];
-[_UITextDocumentInterface _controllerOutput];
-[_UITextDocumentInterface textContentType];
-[_UITextDocumentInterface _keyboardOutput];
-[_UITextDocumentInterface isSecureTextEntry];
-[_UITextDocumentInterface _setShouldDismiss];
-[_UITextDocumentInterface _setShouldAdvanceInputMode];
-[_UITextDocumentInterface setMarkedText:selectedRange:];
-[_UITextDocumentInterface _didPerformOutputOperation];
-[_UITextDocumentInterface setControllerOutput:];
-[_UITextDocumentInterface _documentState];
-[_UITextDocumentInterface autocorrectionType];
-[_UITextDocumentInterface deleteBackward];
-[_UITextDocumentInterface setControllerState:];
-[_UITextDocumentInterface smartQuotesType];
-[_UITextDocumentInterface returnKeyType];
```
