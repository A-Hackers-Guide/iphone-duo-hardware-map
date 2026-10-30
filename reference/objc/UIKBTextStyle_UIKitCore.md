# `UIKBTextStyle`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 25 instance variables, 25 properties, 55 instance methods, 3 class methods

## Instance variables

```
B _ignoreTextMarginOnKey;
B _isVertical;
B _needsFontCase;
B _usesSymbolImage;
i _fontGrade;
@"NSString" _fontName;
d _fontSize;
d _imageScale;
d _minFontSize;
d _kerning;
d _textOpacity;
@"NSString" _textColor;
@"NSString" _etchColor;
q _alignment;
d _pathWeight;
d _fontWeight;
d _fontWidth;
Q _anchorCorner;
q _selector;
@"NSString" _keycapsFallback;
d _fontSizeForSymbolImage;
d _fontWeightForSymbolImage;
q _symbolScale;
{CGPoint="x"d"y"d} _textOffset;
{CGPoint="x"d"y"d} _etchOffset;
```

## Properties

```
@property (T@"NSString",&,N,V_fontName) fontName;
@property (T@"NSString",&,N,V_keycapsFallback) keycapsFallback;
@property (Td,N,V_fontSize) fontSize;
@property (Td,N,V_fontSizeForSymbolImage) fontSizeForSymbolImage;
@property (Td,N,V_imageScale) imageScale;
@property (Td,N,V_minFontSize) minFontSize;
@property (Td,N,V_kerning) kerning;
@property (Td,N,V_textOpacity) textOpacity;
@property (T@"NSString",&,N,V_textColor) textColor;
@property (T@"NSString",&,N,V_etchColor) etchColor;
@property (Tq,N,V_alignment) alignment;
@property (T{CGPoint=dd},N,V_textOffset) textOffset;
@property (T{CGPoint=dd},N,V_etchOffset) etchOffset;
@property (Td,N,V_pathWeight) pathWeight;
@property (Td,N,V_fontWeight) fontWeight;
@property (Td,N,V_fontWeightForSymbolImage) fontWeightForSymbolImage;
@property (Td,N,V_fontWidth) fontWidth;
@property (Ti,N,V_fontGrade) fontGrade;
@property (TB,N,V_needsFontCase) needsFontCase;
@property (TQ,N,V_anchorCorner) anchorCorner;
@property (Tq,N,V_selector) selector;
@property (TB,N,V_ignoreTextMarginOnKey) ignoreTextMarginOnKey;
@property (TB,N,V_usesSymbolImage) usesSymbolImage;
@property (TB,N,V_isVertical) isVertical;
@property (Tq,N,V_symbolScale) symbolScale;
```

## Class methods

```
+[UIKBTextStyle styleWithFontName:withFontSize:];
+[UIKBTextStyle styleWithFontName:withFallbackFontName:withFontSize:];
+[UIKBTextStyle styleWithTextColor:];
```

## Instance methods

```
-[UIKBTextStyle symbolScale];
-[UIKBTextStyle selector];
-[UIKBTextStyle minFontSize];
-[UIKBTextStyle fontName];
-[UIKBTextStyle setFontName:];
-[UIKBTextStyle setSymbolScale:];
-[UIKBTextStyle setMinFontSize:];
-[UIKBTextStyle fontWeight];
-[UIKBTextStyle fontGrade];
-[UIKBTextStyle fontWeightForSymbolImage];
-[UIKBTextStyle anchorCorner];
-[UIKBTextStyle setFontSize:];
-[UIKBTextStyle setUsesSymbolImage:];
-[UIKBTextStyle setNeedsFontCase:];
-[UIKBTextStyle textColor];
-[UIKBTextStyle fontSize];
-[UIKBTextStyle init];
-[UIKBTextStyle setEtchOffset:];
-[UIKBTextStyle isVertical];
-[UIKBTextStyle setTextColor:];
-[UIKBTextStyle setAnchorCorner:];
-[UIKBTextStyle setPathWeight:];
-[UIKBTextStyle setAlignment:];
-[UIKBTextStyle setImageScale:];
-[UIKBTextStyle setSelector:];
-[UIKBTextStyle imageScale];
-[UIKBTextStyle alignment];
-[UIKBTextStyle etchOffset];
-[UIKBTextStyle keycapsFallback];
-[UIKBTextStyle setTextOffset:];
-[UIKBTextStyle kerning];
-[UIKBTextStyle setFontWeight:];
-[UIKBTextStyle setKeycapsFallback:];
-[UIKBTextStyle setKerning:];
-[UIKBTextStyle fontWidth];
-[UIKBTextStyle setFontGrade:];
-[UIKBTextStyle usesSymbolImage];
-[UIKBTextStyle setIgnoreTextMarginOnKey:];
-[UIKBTextStyle description];
-[UIKBTextStyle setFontWidth:];
-[UIKBTextStyle setIsVertical:];
-[UIKBTextStyle setFontWeightForSymbolImage:];
-[UIKBTextStyle ignoreTextMarginOnKey];
-[UIKBTextStyle textOffset];
-[UIKBTextStyle pathWeight];
-[UIKBTextStyle overlayWithStyle:];
-[UIKBTextStyle setTextOpacity:];
-[UIKBTextStyle setFontSizeForSymbolImage:];
-[UIKBTextStyle setEtchColor:];
-[UIKBTextStyle copyWithZone:];
-[UIKBTextStyle isEqual:];
-[UIKBTextStyle textOpacity];
-[UIKBTextStyle needsFontCase];
-[UIKBTextStyle etchColor];
-[UIKBTextStyle fontSizeForSymbolImage];
```
