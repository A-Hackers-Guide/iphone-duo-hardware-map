# `_CUIThemePixelRendition`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CUIThemeRendition`
- 11 instance variables, 0 properties, 17 instance methods, 0 class methods

## Instance variables

```
I _nimages;
[16^{CGImage}] _image;
^{CGImage=} _unslicedImage;
@"CUIRenditionMetrics" _renditionMetrics;
@"CUIRenditionSliceInformation" _sliceInformation;
@"_CSIRenditionBlockData" _cachedBlockDataBGRX;
@"_CSIRenditionBlockData" _cachedBlockDataRGBX;
@"_CSIRenditionBlockData" _cachedBlockDataGray;
Q _sourceRowbytes;
@"NSMutableArray" _layers;
{CGSize="width"d"height"d} _unslicedSize;
```

## Instance methods

```
-[_CUIThemePixelRendition isScaled];
-[_CUIThemePixelRendition isTiled];
-[_CUIThemePixelRendition unslicedImage];
-[_CUIThemePixelRendition edgesOnly];
-[_CUIThemePixelRendition dealloc];
-[_CUIThemePixelRendition sliceInformation];
-[_CUIThemePixelRendition copySharedBlockDataWithPixelFormat:];
-[_CUIThemePixelRendition imageForSliceIndex:];
-[_CUIThemePixelRendition unslicedSize];
-[_CUIThemePixelRendition pixelFormat];
-[_CUIThemePixelRendition setSharedBlockData:];
-[_CUIThemePixelRendition layerReferences];
-[_CUIThemePixelRendition _initWithCSIHeader:version:];
-[_CUIThemePixelRendition metrics];
-[_CUIThemePixelRendition maskForSliceIndex:];
-[_CUIThemePixelRendition sourceRowbytes];
-[_CUIThemePixelRendition initWithCSIData:forKey:version:];
```
