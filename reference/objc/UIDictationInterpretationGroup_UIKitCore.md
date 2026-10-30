# `UIDictationInterpretationGroup`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 4 properties, 9 instance methods, 1 class methods

## Instance variables

```
B _isLowConfidence;
@"NSArray" _interpretations;
```

## Properties

```
@property (T@"NSArray",R,N,V_interpretations) interpretations;
@property (Td,R,N) bestConfidenceScore;
@property (T@"UIDictationInterpretation",R,N) bestInterpretation;
@property (TB,R,N,V_isLowConfidence) isLowConfidence;
```

## Class methods

```
+[UIDictationInterpretationGroup supportsSecureCoding];
```

## Instance methods

```
-[UIDictationInterpretationGroup encodeWithCoder:];
-[UIDictationInterpretationGroup description];
-[UIDictationInterpretationGroup initWithCoder:];
-[UIDictationInterpretationGroup interpretations];
-[UIDictationInterpretationGroup isLowConfidence];
-[UIDictationInterpretationGroup bestConfidenceScore];
-[UIDictationInterpretationGroup bestInterpretation];
-[UIDictationInterpretationGroup initWithInterpretations:];
-[UIDictationInterpretationGroup initWithInterpretations:isLowConfidence:];
```
