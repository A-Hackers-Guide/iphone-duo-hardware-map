# `_UIImageMultiVectorGlyphContent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIImageContent`
- 7 instance variables, 0 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _glyphs;
@"NSArray" _colors;
@"NSArray" _offsets;
@"NSArray" _scaleFactors;
{CGSize="width"d"height"d} _sizeInPixels;
{CGPoint="x"d"y"d} _anchorPoint;
^{CGImage=} _imageRef;
```

## Instance methods

```
-[_UIImageMultiVectorGlyphContent sizeInPixels];
-[_UIImageMultiVectorGlyphContent CGImage];
-[_UIImageMultiVectorGlyphContent typeName];
-[_UIImageMultiVectorGlyphContent containsNamedColorStyles];
-[_UIImageMultiVectorGlyphContent isCGImage];
-[_UIImageMultiVectorGlyphContent dealloc];
-[_UIImageMultiVectorGlyphContent isVectorGlyph];
-[_UIImageMultiVectorGlyphContent canScaleImageToTargetResolution];
-[_UIImageMultiVectorGlyphContent _drawWithSize:scale:inContext:renditionContext:];
-[_UIImageMultiVectorGlyphContent vectorScale];
-[_UIImageMultiVectorGlyphContent description];
-[_UIImageMultiVectorGlyphContent canEmitVectorDrawingCommands];
-[_UIImageMultiVectorGlyphContent _prepareForDrawingWithSize:scale:inContext:];
-[_UIImageMultiVectorGlyphContent isEqual:];
-[_UIImageMultiVectorGlyphContent initWithScale:];
-[_UIImageMultiVectorGlyphContent initWithSize:glyphs:colors:offsets:scaleFactors:anchorPoint:];
```
