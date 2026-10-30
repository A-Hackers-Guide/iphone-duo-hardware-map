# `_UILegibilitySettings`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`, `BSXPCCoding`
- 10 instance variables, 14 properties, 34 instance methods, 2 class methods

## Instance variables

```
q _style;
@"UIColor" _contentColor;
@"UIColor" _primaryColor;
@"UIColor" _secondaryColor;
@"UIColor" _shadowColor;
d _shadowRadius;
d _shadowAlpha;
d _imageOutset;
d _minFillHeight;
@"NSString" _shadowCompositingFilterName;
```

## Properties

```
@property (Tq,N,V_style) style;
@property (T@"NSString",C,N,V_shadowCompositingFilterName) shadowCompositingFilterName;
@property (T@"UIColor",&,N,V_primaryColor) primaryColor;
@property (T@"UIColor",&,N,V_secondaryColor) secondaryColor;
@property (T@"UIColor",&,N,V_shadowColor) shadowColor;
@property (T@"UIColor",&,N,V_contentColor) contentColor;
@property (Td,N,V_shadowRadius) shadowRadius;
@property (Td,N,V_shadowAlpha) shadowAlpha;
@property (Td,N,V_imageOutset) imageOutset;
@property (Td,N,V_minFillHeight) minFillHeight;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UILegibilitySettings supportsSecureCoding];
+[_UILegibilitySettings sharedInstanceForStyle:];
```

## Instance methods

```
-[_UILegibilitySettings setShadowAlpha:];
-[_UILegibilitySettings shadowAlpha];
-[_UILegibilitySettings setShadowRadius:];
-[_UILegibilitySettings setContentColor:];
-[_UILegibilitySettings initWithXPCDictionary:];
-[_UILegibilitySettings dealloc];
-[_UILegibilitySettings setPrimaryColor:];
-[_UILegibilitySettings initWithStyle:];
-[_UILegibilitySettings contentColor];
-[_UILegibilitySettings style];
-[_UILegibilitySettings shadowColor];
-[_UILegibilitySettings setStyle:];
-[_UILegibilitySettings secondaryColor];
-[_UILegibilitySettings encodeWithXPCDictionary:];
-[_UILegibilitySettings encodeWithCoder:];
-[_UILegibilitySettings description];
-[_UILegibilitySettings setSecondaryColor:];
-[_UILegibilitySettings initWithCoder:];
-[_UILegibilitySettings primaryColor];
-[_UILegibilitySettings setShadowColor:];
-[_UILegibilitySettings copyWithZone:];
-[_UILegibilitySettings isEqual:];
-[_UILegibilitySettings shadowRadius];
-[_UILegibilitySettings setShadowCompositingFilterName:];
-[_UILegibilitySettings setImageOutset:];
-[_UILegibilitySettings imageOutset];
-[_UILegibilitySettings initWithContentColor:];
-[_UILegibilitySettings initWithContentColor:contrast:];
-[_UILegibilitySettings initWithStyle:contentColor:];
-[_UILegibilitySettings initWithStyle:primaryColor:secondaryColor:shadowColor:];
-[_UILegibilitySettings minFillHeight];
-[_UILegibilitySettings setMinFillHeight:];
-[_UILegibilitySettings setPropertiesForStyle:];
-[_UILegibilitySettings shadowCompositingFilterName];
```
