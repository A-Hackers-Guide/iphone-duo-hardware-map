# `_CUIThemeVectorGlyphRendition`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CUIThemeRendition`
- Protocols: `NSLocking`
- 16 instance variables, 0 properties, 21 instance methods, 0 class methods

## Instance variables

```
^{CGSVGDocument=} _svgDocument;
@"NSData" _fileData;
I _standardPointSize;
@"NSArray" _vectorSizes;
d _baseline;
d _capline;
{?="top"d"left"d"bottom"d"right"d} _alignmentRectInsets;
B _isAlignmentRect;
{CGSize="width"d"height"d} _canvasSize;
f _templateVersion;
B _isInterpolatable;
B _isBinarySpec;
q _renderingMode;
s _containsMulticolorLayers;
s _containsHierarchicalLayers;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
```

## Instance methods

```
-[_CUIThemeVectorGlyphRendition canvasSize];
-[_CUIThemeVectorGlyphRendition svgDocument];
-[_CUIThemeVectorGlyphRendition vectorGlyphCapLine];
-[_CUIThemeVectorGlyphRendition dealloc];
-[_CUIThemeVectorGlyphRendition _initalizeMetadataFromCSIData:version:];
-[_CUIThemeVectorGlyphRendition vectorGlyphRenderingMode];
-[_CUIThemeVectorGlyphRendition vectorGlyphReferencePointSize];
-[_CUIThemeVectorGlyphRendition vectorGlyphAvailableSizes];
-[_CUIThemeVectorGlyphRendition containsHierarchicalLayers];
-[_CUIThemeVectorGlyphRendition rawData];
-[_CUIThemeVectorGlyphRendition isInterpolatable];
-[_CUIThemeVectorGlyphRendition vectorGlyphTemplateVersion];
-[_CUIThemeVectorGlyphRendition vectorGlyphAlignmentRectInsets];
-[_CUIThemeVectorGlyphRendition pixelFormat];
-[_CUIThemeVectorGlyphRendition lock];
-[_CUIThemeVectorGlyphRendition containsMulticolorLayers];
-[_CUIThemeVectorGlyphRendition _initWithCSIHeader:version:];
-[_CUIThemeVectorGlyphRendition metrics];
-[_CUIThemeVectorGlyphRendition unlock];
-[_CUIThemeVectorGlyphRendition vectorGlyphBaseline];
-[_CUIThemeVectorGlyphRendition initWithCSIData:forKey:version:];
```
