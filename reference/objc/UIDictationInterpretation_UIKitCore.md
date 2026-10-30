# `UIDictationInterpretation`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 4 properties, 12 instance methods, 2 class methods

## Instance variables

```
@"NSArray" _tokens;
d _averageConfidenceScore;
```

## Properties

```
@property (Td,N,V_averageConfidenceScore) averageConfidenceScore;
@property (T@"NSArray",R,N,V_tokens) tokens;
@property (TB,R,N) removeSpaceBefore;
@property (TB,R,N) removeSpaceAfter;
```

## Class methods

```
+[UIDictationInterpretation supportsSecureCoding];
+[UIDictationInterpretation serializedInterpretationFromTokens:transform:];
```

## Instance methods

```
-[UIDictationInterpretation tokens];
-[UIDictationInterpretation encodeWithCoder:];
-[UIDictationInterpretation description];
-[UIDictationInterpretation initWithCoder:];
-[UIDictationInterpretation isEqual:];
-[UIDictationInterpretation initWithTokens:];
-[UIDictationInterpretation averageConfidenceScore];
-[UIDictationInterpretation initWithTokens:score:];
-[UIDictationInterpretation removeSpaceAfter];
-[UIDictationInterpretation removeSpaceBefore];
-[UIDictationInterpretation serializedInterpretationWithTransform:];
-[UIDictationInterpretation setAverageConfidenceScore:];
```
