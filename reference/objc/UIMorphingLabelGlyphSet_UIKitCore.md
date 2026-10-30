# `UIMorphingLabelGlyphSet`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 8 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"UIMorphingLabel" _label;
@"NSAttributedString" _attributedString;
^{__CTLine=} _line;
@"NSMutableArray" _glyphViews;
Q _glyphCount;
^S _glyphs;
^{CGRect={CGPoint=dd}{CGSize=dd}} _glyphFrames;
^{CGPoint=dd} _glyphPositions;
{CGPoint="x"d"y"d} _lineOrigin;
d _lineWidth;
```

## Properties

```
@property (TQ,R,N,V_glyphCount) glyphCount;
@property (Tr^S,R,N,V_glyphs) glyphs;
@property (Tr^{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_glyphFrames) glyphFrames;
@property (Tr^{CGPoint=dd},R,N,V_glyphPositions) glyphPositions;
@property (T@"NSArray",R,N,V_glyphViews) glyphViews;
@property (T@"NSAttributedString",R,N,V_attributedString) attributedString;
@property (T{CGPoint=dd},R,N,V_lineOrigin) lineOrigin;
@property (Td,R,N,V_lineWidth) lineWidth;
```

## Instance methods

```
-[UIMorphingLabelGlyphSet lineWidth];
-[UIMorphingLabelGlyphSet attributedString];
-[UIMorphingLabelGlyphSet placeGlyphs];
-[UIMorphingLabelGlyphSet dealloc];
-[UIMorphingLabelGlyphSet glyphPositions];
-[UIMorphingLabelGlyphSet boundingRectForGlyphsInRange:];
-[UIMorphingLabelGlyphSet glyphViews];
-[UIMorphingLabelGlyphSet initWithLabel:attributedString:];
-[UIMorphingLabelGlyphSet glyphFrames];
-[UIMorphingLabelGlyphSet lineOrigin];
-[UIMorphingLabelGlyphSet glyphs];
-[UIMorphingLabelGlyphSet removeGlyphs];
-[UIMorphingLabelGlyphSet glyphCount];
-[UIMorphingLabelGlyphSet buildGlyphViews];
```
