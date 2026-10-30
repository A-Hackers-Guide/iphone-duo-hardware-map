# `_UITypeSelectKeyInput`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIResponder`
- Protocols: `UIKeyInput`
- 2 instance variables, 27 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"<_UITypeSelectKeyInputDelegate>" _delegate;
@"NSMutableString" _typedText;
```

## Properties

```
@property (T@"NSMutableString",&,N,V_typedText) typedText;
@property (T@"<_UITypeSelectKeyInputDelegate>",W,N,V_delegate) delegate;
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

## Instance methods

```
-[_UITypeSelectKeyInput hasText];
-[_UITypeSelectKeyInput insertText:];
-[_UITypeSelectKeyInput setTypedText:];
-[_UITypeSelectKeyInput typedText];
-[_UITypeSelectKeyInput init];
-[_UITypeSelectKeyInput setDelegate:];
-[_UITypeSelectKeyInput delegate];
-[_UITypeSelectKeyInput __isKindOfTypeSelectKeyInput];
-[_UITypeSelectKeyInput deleteBackward];
-[_UITypeSelectKeyInput resetInput];
```
