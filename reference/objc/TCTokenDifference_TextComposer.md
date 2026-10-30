# `TCTokenDifference`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _inputTokens;
@"NSArray" _outputTokens;
@"NSString" _inputText;
@"NSString" _outputText;
{_NSRange="location"Q"length"Q} _inputTokenRange;
{_NSRange="location"Q"length"Q} _outputTokenRange;
{_NSRange="location"Q"length"Q} _inputCharacterRange;
{_NSRange="location"Q"length"Q} _outputCharacterRange;
```

## Properties

```
@property (T{_NSRange=QQ},R,V_inputTokenRange) inputTokenRange;
@property (T{_NSRange=QQ},R,V_outputTokenRange) outputTokenRange;
@property (T@"NSArray",R,C,V_inputTokens) inputTokens;
@property (T@"NSArray",R,C,V_outputTokens) outputTokens;
@property (T{_NSRange=QQ},R,V_inputCharacterRange) inputCharacterRange;
@property (T{_NSRange=QQ},R,V_outputCharacterRange) outputCharacterRange;
@property (T@"NSString",R,C,V_inputText) inputText;
@property (T@"NSString",R,C,V_outputText) outputText;
```

## Instance methods

```
-[TCTokenDifference inputText];
-[TCTokenDifference description];
-[TCTokenDifference inputTokens];
-[TCTokenDifference inputTokenRange];
-[TCTokenDifference initWithInputTokenRange:inTokens:outputTokenRange:inTokens:inputCharacterRange:inInput:outputCharacterRange:inOutput:];
-[TCTokenDifference initWithInputTokenRange:inputTokens:outputTokenRange:outputTokens:inputCharacterRange:inputText:outputCharacterRange:outputText:];
-[TCTokenDifference initWithManager:inputTokenRange:outputTokenRange:];
-[TCTokenDifference inputCharacterRange];
-[TCTokenDifference outputCharacterRange];
-[TCTokenDifference outputText];
-[TCTokenDifference outputTokenRange];
-[TCTokenDifference outputTokens];
```
