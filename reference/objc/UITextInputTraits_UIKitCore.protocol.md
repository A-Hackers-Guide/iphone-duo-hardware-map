# `UITextInputTraits` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 20 properties, 40 instance methods, 0 class methods

## Properties

```
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
```

## Instance methods

```
-[UITextInputTraits setAutocorrectionType:];
-[UITextInputTraits setSpellCheckingType:];
-[UITextInputTraits mathExpressionCompletionType];
-[UITextInputTraits setConversationContext:];
-[UITextInputTraits setSmartQuotesType:];
-[UITextInputTraits inlinePredictionType];
-[UITextInputTraits setAllowsNumberPadPopover:];
-[UITextInputTraits setKeyboardAppearance:];
-[UITextInputTraits setKeyboardType:];
-[UITextInputTraits setReturnKeyType:];
-[UITextInputTraits setSmartDashesType:];
-[UITextInputTraits conversationContext];
-[UITextInputTraits setSecureTextEntry:];
-[UITextInputTraits setPasswordRules:];
-[UITextInputTraits setMathExpressionCompletionType:];
-[UITextInputTraits autocapitalizationType];
-[UITextInputTraits passwordRules];
-[UITextInputTraits setAutocapitalizationType:];
-[UITextInputTraits allowsNumberPadPopover];
-[UITextInputTraits setInlinePredictionType:];
-[UITextInputTraits setEnablesReturnKeyAutomatically:];
-[UITextInputTraits setSmartInsertDeleteType:];
-[UITextInputTraits setTextContentType:];
-[UITextInputTraits smartDashesType];
-[UITextInputTraits spellCheckingType];
-[UITextInputTraits keyboardType];
-[UITextInputTraits smartInsertDeleteType];
-[UITextInputTraits enablesReturnKeyAutomatically];
-[UITextInputTraits grammarCheckingType];
-[UITextInputTraits setGrammarCheckingType:];
-[UITextInputTraits keyboardAppearance];
-[UITextInputTraits writingToolsBehavior];
-[UITextInputTraits setAllowedWritingToolsResultOptions:];
-[UITextInputTraits allowedWritingToolsResultOptions];
-[UITextInputTraits textContentType];
-[UITextInputTraits isSecureTextEntry];
-[UITextInputTraits autocorrectionType];
-[UITextInputTraits setWritingToolsBehavior:];
-[UITextInputTraits smartQuotesType];
-[UITextInputTraits returnKeyType];
```
