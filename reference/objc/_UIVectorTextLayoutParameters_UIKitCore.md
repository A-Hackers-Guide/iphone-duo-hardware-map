# `_UIVectorTextLayoutParameters`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIVectorTextLayoutParameters`, `NSCopying`
- 5 instance variables, 9 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"NSAttributedString" _attributedText;
Q _numberOfLines;
@"UITraitCollection" _traitCollection;
q _lineBreakMode;
{CGSize="width"d"height"d} _withinSize;
```

## Properties

```
@property (T@"NSAttributedString",C,N,V_attributedText) attributedText;
@property (TQ,N,V_numberOfLines) numberOfLines;
@property (T{CGSize=dd},N,V_withinSize) withinSize;
@property (T@"UITraitCollection",&,N,V_traitCollection) traitCollection;
@property (Tq,N,V_lineBreakMode) lineBreakMode;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIVectorTextLayoutParameters parametersSuitableForView:];
```

## Instance methods

```
-[_UIVectorTextLayoutParameters setTraitCollection:];
-[_UIVectorTextLayoutParameters initWithParameters:];
-[_UIVectorTextLayoutParameters traitCollection];
-[_UIVectorTextLayoutParameters numberOfLines];
-[_UIVectorTextLayoutParameters setAttributedText:];
-[_UIVectorTextLayoutParameters attributedText];
-[_UIVectorTextLayoutParameters setNumberOfLines:];
-[_UIVectorTextLayoutParameters copyWithZone:];
-[_UIVectorTextLayoutParameters setLineBreakMode:];
-[_UIVectorTextLayoutParameters lineBreakMode];
-[_UIVectorTextLayoutParameters _copyFromParameters:];
-[_UIVectorTextLayoutParameters isEqualToParameters:];
-[_UIVectorTextLayoutParameters setWithinSize:];
-[_UIVectorTextLayoutParameters withinSize];
```
