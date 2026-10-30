# `UIDictationScoredToken`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIDictationToken`
- Protocols: `NSSecureCoding`
- 1 instance variables, 1 properties, 6 instance methods, 1 class methods

## Instance variables

```
d _confidenceScore;
```

## Properties

```
@property (Td,R,N,V_confidenceScore) confidenceScore;
```

## Class methods

```
+[UIDictationScoredToken supportsSecureCoding];
```

## Instance methods

```
-[UIDictationScoredToken confidenceScore];
-[UIDictationScoredToken encodeWithCoder:];
-[UIDictationScoredToken initWithCoder:];
-[UIDictationScoredToken isEqual:];
-[UIDictationScoredToken _descriptionExtra];
-[UIDictationScoredToken initWithText:removeSpaceBefore:removeSpaceAfter:confidenceScore:];
```
