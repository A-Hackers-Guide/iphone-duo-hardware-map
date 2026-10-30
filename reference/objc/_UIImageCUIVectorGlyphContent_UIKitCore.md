# `_UIImageCUIVectorGlyphContent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIImageContent`
- 9 instance variables, 1 properties, 38 instance methods, 0 class methods

## Instance variables

```
@"CUINamedVectorGlyph" _vectorGlyph;
@"_UIImageContent" _vectorContent;
d _glyphScaleFactor;
d _vectorScale;
{CGSize="width"d"height"d} _sizeInPixels;
^{CGImage=} _overrideImageRef;
Ai _isMultiColor;
Aq _numberOfHierarchyLayers;
Aq _numberOfPaletteLayers;
```

## Properties

```
@property (Td,N,V_glyphScaleFactor) glyphScaleFactor;
```

## Instance methods

```
-[_UIImageCUIVectorGlyphContent variableValue];
-[_UIImageCUIVectorGlyphContent sizeInPixels];
-[_UIImageCUIVectorGlyphContent CGImage];
-[_UIImageCUIVectorGlyphContent typeName];
-[_UIImageCUIVectorGlyphContent _provideVectorGlyphCGImageWithSize:scale:hierarchicalColorResolver:];
-[_UIImageCUIVectorGlyphContent containsNamedColorStyles];
-[_UIImageCUIVectorGlyphContent _drawVectorGlyphWithSize:scale:inContext:templateColor:];
-[_UIImageCUIVectorGlyphContent _drawVectorGlyphWithSize:scale:inContext:paletteColors:];
-[_UIImageCUIVectorGlyphContent isCGImage];
-[_UIImageCUIVectorGlyphContent dealloc];
-[_UIImageCUIVectorGlyphContent _drawVectorGlyphWithSize:scale:inContext:hierarchicalColorResolver:];
-[_UIImageCUIVectorGlyphContent _provideCGImageWithSize:scale:];
-[_UIImageCUIVectorGlyphContent _drawVectorGlyphWithSize:scale:inContext:namedColorResolver:];
-[_UIImageCUIVectorGlyphContent contentWithVariableValue:];
-[_UIImageCUIVectorGlyphContent isVectorGlyph];
-[_UIImageCUIVectorGlyphContent canScaleImageToTargetResolution];
-[_UIImageCUIVectorGlyphContent _drawWithSize:scale:inContext:renditionContext:];
-[_UIImageCUIVectorGlyphContent vectorScale];
-[_UIImageCUIVectorGlyphContent _provideVectorGlyphCGImageWithSize:scale:namedColorResolver:];
-[_UIImageCUIVectorGlyphContent _provideVectorGlyphCGImageWithSize:scale:templateColor:];
-[_UIImageCUIVectorGlyphContent containsNamedColorStyle:];
-[_UIImageCUIVectorGlyphContent hash];
-[_UIImageCUIVectorGlyphContent vectorGlyph];
-[_UIImageCUIVectorGlyphContent description];
-[_UIImageCUIVectorGlyphContent setGlyphScaleFactor:];
-[_UIImageCUIVectorGlyphContent canEmitVectorDrawingCommands];
-[_UIImageCUIVectorGlyphContent contentWithCGImage:];
-[_UIImageCUIVectorGlyphContent _prepareForDrawingWithSize:scale:inContext:];
-[_UIImageCUIVectorGlyphContent initWithCUIVectorGlyph:scale:];
-[_UIImageCUIVectorGlyphContent isEqual:];
-[_UIImageCUIVectorGlyphContent numberOfPaletteLayers];
-[_UIImageCUIVectorGlyphContent _provideVectorGlyphCGImageWithSize:scale:paletteColors:];
-[_UIImageCUIVectorGlyphContent numberOfHierarchyLayers];
-[_UIImageCUIVectorGlyphContent _canProvideCGImageDirectly];
-[_UIImageCUIVectorGlyphContent glyphScaleFactor];
-[_UIImageCUIVectorGlyphContent initWithScale:];
-[_UIImageCUIVectorGlyphContent _automaticSymbolConfiguration];
-[_UIImageCUIVectorGlyphContent outlinePath];
```
