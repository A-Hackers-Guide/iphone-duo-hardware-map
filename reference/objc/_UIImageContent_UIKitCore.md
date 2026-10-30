# `_UIImageContent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 18 properties, 72 instance methods, 1 class methods

## Instance variables

```
d _scale;
B _isDecompressing;
{CGSize="width"d"height"d} _sizeInPixels;
```

## Properties

```
@property (Td,R,N,V_scale) scale;
@property (T{CGSize=dd},R,N,V_sizeInPixels) sizeInPixels;
@property (T{CGSize=dd},R,N) size;
@property (T@"NSString",R,N) typeName;
@property (T^{CGImage=},R,N) CGImage;
@property (T^{CGImageSource=},R,N) CGImageSource;
@property (T@,R,N) layerContents;
@property (T@"CIImage",R,N) CIImage;
@property (T^{__IOSurface=},R,N) IOSurface;
@property (T^{__IOSurface=},R,N) alternateIOSurface;
@property (T^{CGPDFPage=},R,N) CGPDFPage;
@property (T^{CGSVGDocument=},R,N) CGSVGDocument;
@property (T@"CUINamedVectorGlyph",R,N) vectorGlyph;
@property (Td,R,N) variableValue;
@property (T@"UIImageSymbolConfiguration",R,N) _automaticSymbolConfiguration;
@property (Td,R,N) vectorScale;
@property (T@"UIBezierPath",R,N) outlinePath;
@property (TB,N,V_isDecompressing) isDecompressing;
```

## Class methods

```
+[_UIImageContent empty];
```

## Instance methods

```
-[_UIImageContent layerContents];
-[_UIImageContent variableValue];
-[_UIImageContent sizeInPixels];
-[_UIImageContent CGImage];
-[_UIImageContent isHDR];
-[_UIImageContent typeName];
-[_UIImageContent debugDescription];
-[_UIImageContent _provideVectorGlyphCGImageWithSize:scale:hierarchicalColorResolver:];
-[_UIImageContent containsNamedColorStyles];
-[_UIImageContent init];
-[_UIImageContent debugQuickLookObject];
-[_UIImageContent contentPreparedForDisplay];
-[_UIImageContent _drawVectorGlyphWithSize:scale:inContext:templateColor:];
-[_UIImageContent _drawVectorGlyphWithSize:scale:inContext:paletteColors:];
-[_UIImageContent isCGImage];
-[_UIImageContent prepareContentForDisplayWithCompletionHandler:];
-[_UIImageContent _drawVectorGlyphWithSize:scale:inContext:hierarchicalColorResolver:];
-[_UIImageContent isPreparedCGImage];
-[_UIImageContent makeSDRVersion];
-[_UIImageContent _provideCGImageWithSize:scale:];
-[_UIImageContent _drawVectorGlyphWithSize:scale:inContext:namedColorResolver:];
-[_UIImageContent contentWithVariableValue:];
-[_UIImageContent isCGPDFPage];
-[_UIImageContent isVectorGlyph];
-[_UIImageContent imageMaximumHeadroom];
-[_UIImageContent size];
-[_UIImageContent canScaleImageToTargetResolution];
-[_UIImageContent scale];
-[_UIImageContent _drawWithSize:scale:inContext:renditionContext:];
-[_UIImageContent vectorScale];
-[_UIImageContent CGSVGDocument];
-[_UIImageContent _provideVectorGlyphCGImageWithSize:scale:namedColorResolver:];
-[_UIImageContent imageRendererFormat];
-[_UIImageContent _provideVectorGlyphCGImageWithSize:scale:templateColor:];
-[_UIImageContent canWriteToImageIO];
-[_UIImageContent containsNamedColorStyle:];
-[_UIImageContent hash];
-[_UIImageContent vectorGlyph];
-[_UIImageContent optimizeContentForImageSize:completionHandler:];
-[_UIImageContent alternateIOSurface];
-[_UIImageContent _drawVectorCommandsWithSize:scale:inContext:renditionContext:];
-[_UIImageContent canEmitVectorDrawingCommands];
-[_UIImageContent contentWithCGImage:];
-[_UIImageContent addContentToDestination:properties:];
-[_UIImageContent CGPDFPage];
-[_UIImageContent _prepareForDrawingWithSize:scale:inContext:];
-[_UIImageContent isIOSurface];
-[_UIImageContent isDecompressing];
-[_UIImageContent isEqual:];
-[_UIImageContent numberOfPaletteLayers];
-[_UIImageContent IOSurface];
-[_UIImageContent _provideVectorGlyphCGImageWithSize:scale:paletteColors:];
-[_UIImageContent contentOptimizedForImageSize:];
-[_UIImageContent hasCGImage];
-[_UIImageContent isCGSVGDocument];
-[_UIImageContent numberOfHierarchyLayers];
-[_UIImageContent prefersProvidingNonCGImageContentsDirectlyForRendering];
-[_UIImageContent _canProvideCGImageDirectly];
-[_UIImageContent initWithScale:];
-[_UIImageContent _automaticSymbolConfiguration];
-[_UIImageContent renditionWithSize:scale:renditionContext:];
-[_UIImageContent outlinePath];
-[_UIImageContent CIImage];
-[_UIImageContent CGImageSource];
-[_UIImageContent CGPDFPageSize];
-[_UIImageContent CGSVGDocumentSize];
-[_UIImageContent _isSameSymbolImageContentExceptVariableValue:];
-[_UIImageContent _setCGImageSource:];
-[_UIImageContent canRenderCIImage];
-[_UIImageContent isCGImageOnly];
-[_UIImageContent isCIImage];
-[_UIImageContent setIsDecompressing:];
```
