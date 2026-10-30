# `_UIStatusBarStyleAttributes`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 15 instance variables, 16 properties, 35 instance methods, 3 class methods

## Instance variables

```
B _scaledFixedWidthBar;
q _style;
q _mode;
@"UITraitCollection" _traitCollection;
q _effectiveLayoutDirection;
d _iconScale;
q _symbolScale;
q _iconSize;
@"UIFont" _font;
@"UIFont" _emphasizedFont;
@"UIFont" _smallFont;
@"UIColor" _textColor;
@"UIColor" _imageTintColor;
@"UIColor" _imageDimmedTintColor;
@"NSArray" _imageNamePrefixes;
```

## Properties

```
@property (T@"UITraitCollection",C,N,V_traitCollection) traitCollection;
@property (TB,N,GisScaledFixedWidthBar,V_scaledFixedWidthBar) scaledFixedWidthBar;
@property (Tq,R,N,V_style) style;
@property (Tq,R,N,V_mode) mode;
@property (Tq,R,N,V_effectiveLayoutDirection) effectiveLayoutDirection;
@property (Td,N,V_iconScale) iconScale;
@property (Tq,N,V_symbolScale) symbolScale;
@property (Tq,N,V_iconSize) iconSize;
@property (T@"UIFont",C,N,V_font) font;
@property (T@"UIFont",C,N,V_emphasizedFont) emphasizedFont;
@property (T@"UIFont",C,N,V_smallFont) smallFont;
@property (T@"UIColor",C,N,V_textColor) textColor;
@property (T@"UIColor",C,N,V_imageTintColor) imageTintColor;
@property (T@"UIColor",C,N,V_imageDimmedTintColor) imageDimmedTintColor;
@property (T@"NSArray",C,N,V_imageNamePrefixes) imageNamePrefixes;
@property (TB,R,N,GisRounded) rounded;
```

## Class methods

```
+[_UIStatusBarStyleAttributes supportsSecureCoding];
+[_UIStatusBarStyleAttributes overriddenStyleAttributes];
+[_UIStatusBarStyleAttributes styleAttributesForStatusBar:style:];
```

## Instance methods

```
-[_UIStatusBarStyleAttributes symbolScale];
-[_UIStatusBarStyleAttributes setIconSize:];
-[_UIStatusBarStyleAttributes setSymbolScale:];
-[_UIStatusBarStyleAttributes iconSize];
-[_UIStatusBarStyleAttributes iconScale];
-[_UIStatusBarStyleAttributes setTraitCollection:];
-[_UIStatusBarStyleAttributes setImageNamePrefixes:];
-[_UIStatusBarStyleAttributes setIconScale:];
-[_UIStatusBarStyleAttributes traitCollection];
-[_UIStatusBarStyleAttributes textColor];
-[_UIStatusBarStyleAttributes effectiveLayoutDirection];
-[_UIStatusBarStyleAttributes setTextColor:];
-[_UIStatusBarStyleAttributes setImageDimmedTintColor:];
-[_UIStatusBarStyleAttributes style];
-[_UIStatusBarStyleAttributes imageTintColor];
-[_UIStatusBarStyleAttributes fontForStyle:];
-[_UIStatusBarStyleAttributes emphasizedFont];
-[_UIStatusBarStyleAttributes setImageTintColor:];
-[_UIStatusBarStyleAttributes imageDimmedTintColor];
-[_UIStatusBarStyleAttributes styleAttributesWithOverrides:];
-[_UIStatusBarStyleAttributes isScaledFixedWidthBar];
-[_UIStatusBarStyleAttributes smallFont];
-[_UIStatusBarStyleAttributes encodeWithCoder:];
-[_UIStatusBarStyleAttributes mode];
-[_UIStatusBarStyleAttributes setSmallFont:];
-[_UIStatusBarStyleAttributes description];
-[_UIStatusBarStyleAttributes initWithCoder:];
-[_UIStatusBarStyleAttributes setScaledFixedWidthBar:];
-[_UIStatusBarStyleAttributes font];
-[_UIStatusBarStyleAttributes copyWithZone:];
-[_UIStatusBarStyleAttributes isRounded];
-[_UIStatusBarStyleAttributes isEqual:];
-[_UIStatusBarStyleAttributes imageNamePrefixes];
-[_UIStatusBarStyleAttributes setEmphasizedFont:];
-[_UIStatusBarStyleAttributes setFont:];
```
