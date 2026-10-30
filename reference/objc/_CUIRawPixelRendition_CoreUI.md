# `_CUIRawPixelRendition`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CUIThemeRendition`
- 7 instance variables, 0 properties, 11 instance methods, 0 class methods

## Instance variables

```
i _pixelFormat;
I _nimages;
@"NSData" _rawData;
[16^{CGImage}] _image;
^{CGImage=} _unslicedImage;
@"CUIRenditionMetrics" _renditionMetrics;
@"CUIRenditionSliceInformation" _sliceInformation;
```

## Instance methods

```
-[_CUIRawPixelRendition isScaled];
-[_CUIRawPixelRendition unslicedImage];
-[_CUIRawPixelRendition dealloc];
-[_CUIRawPixelRendition sliceInformation];
-[_CUIRawPixelRendition imageForSliceIndex:];
-[_CUIRawPixelRendition unslicedSize];
-[_CUIRawPixelRendition pixelFormat];
-[_CUIRawPixelRendition _initWithCSIHeader:version:];
-[_CUIRawPixelRendition metrics];
-[_CUIRawPixelRendition maskForSliceIndex:];
-[_CUIRawPixelRendition initWithCSIData:forKey:version:];
```
