# `TCTextCompositionOCRTextBoundingBox`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 3 instance variables, 3 properties, 9 instance methods, 1 class methods

## Instance variables

```
f _confidence;
@"NSString" _text;
@"NSArray" _coordinates;
```

## Properties

```
@property (T@"NSString",R,C,N,V_text) text;
@property (T@"NSArray",R,C,N,V_coordinates) coordinates;
@property (Tf,R,N,V_confidence) confidence;
```

## Class methods

```
+[TCTextCompositionOCRTextBoundingBox supportsSecureCoding];
```

## Instance methods

```
-[TCTextCompositionOCRTextBoundingBox text];
-[TCTextCompositionOCRTextBoundingBox encodeWithCoder:];
-[TCTextCompositionOCRTextBoundingBox initWithCoder:];
-[TCTextCompositionOCRTextBoundingBox copyWithZone:];
-[TCTextCompositionOCRTextBoundingBox isEqual:];
-[TCTextCompositionOCRTextBoundingBox confidence];
-[TCTextCompositionOCRTextBoundingBox coordinates];
-[TCTextCompositionOCRTextBoundingBox initWithText:coordinates:];
-[TCTextCompositionOCRTextBoundingBox initWithText:coordinates:confidence:];
```
