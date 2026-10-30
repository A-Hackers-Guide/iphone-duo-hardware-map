# `UIStatusBarStyleRequest`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSMutableCopying`, `NSCopying`
- 5 instance variables, 5 properties, 20 instance methods, 0 class methods

## Instance variables

```
q _style;
q _legibilityStyle;
@"UIColor" _foregroundColor;
@"NSNumber" _overrideHeight;
d _foregroundAlpha;
```

## Properties

```
@property (T@"NSNumber",R,&,N,V_overrideHeight) overrideHeight;
@property (Tq,R,N,V_style) style;
@property (Tq,R,N,V_legibilityStyle) legibilityStyle;
@property (T@"UIColor",R,&,N,V_foregroundColor) foregroundColor;
@property (Td,R,N,V_foregroundAlpha) foregroundAlpha;
```

## Instance methods

```
-[UIStatusBarStyleRequest mutableCopyWithZone:];
-[UIStatusBarStyleRequest foregroundAlpha];
-[UIStatusBarStyleRequest init];
-[UIStatusBarStyleRequest overrideHeight];
-[UIStatusBarStyleRequest style];
-[UIStatusBarStyleRequest legibilityStyle];
-[UIStatusBarStyleRequest isTranslucent];
-[UIStatusBarStyleRequest hash];
-[UIStatusBarStyleRequest foregroundColor];
-[UIStatusBarStyleRequest copyWithZone:];
-[UIStatusBarStyleRequest isEqual:];
-[UIStatusBarStyleRequest _copyWithZone:class:];
-[UIStatusBarStyleRequest initWithStyle:legacy:legibilityStyle:foregroundColor:];
-[UIStatusBarStyleRequest initWithStyle:legacy:legibilityStyle:foregroundColor:foregroundAlpha:];
-[UIStatusBarStyleRequest initWithStyle:legibilityStyle:foregroundColor:];
-[UIStatusBarStyleRequest initWithStyle:legibilityStyle:foregroundColor:foregroundAlpha:];
-[UIStatusBarStyleRequest initWithStyle:legibilityStyle:foregroundColor:foregroundAlpha:overrideHeight:];
-[UIStatusBarStyleRequest initWithStyle:legibilityStyle:foregroundColor:overrideHeight:];
-[UIStatusBarStyleRequest isDoubleHeight];
-[UIStatusBarStyleRequest isLegacy];
```
