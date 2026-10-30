# `_CUIInternalLinkRendition`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CUIThemeRendition`
- 11 instance variables, 0 properties, 24 instance methods, 0 class methods

## Instance variables

```
I _nimages;
[16{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}] _imageRect;
[16^{CGImage}] _image;
^{CGImage=} _unslicedImage;
@"CUIRenditionMetrics" _renditionMetrics;
@"CUIRenditionSliceInformation" _sliceInformation;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _frame;
@"CUIStructuredThemeStore" _sourceProvider;
@"CUIRenditionKey" _referenceKey;
{CGSize="width"d"height"d} _originalUncroppedSize;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _alphaCroppedFrame;
```

## Instance methods

```
-[_CUIInternalLinkRendition properties];
-[_CUIInternalLinkRendition isScaled];
-[_CUIInternalLinkRendition isTiled];
-[_CUIInternalLinkRendition unslicedImage];
-[_CUIInternalLinkRendition edgesOnly];
-[_CUIInternalLinkRendition data];
-[_CUIInternalLinkRendition dealloc];
-[_CUIInternalLinkRendition isOpaque];
-[_CUIInternalLinkRendition sliceInformation];
-[_CUIInternalLinkRendition linkingToRendition];
-[_CUIInternalLinkRendition _sourceRendition];
-[_CUIInternalLinkRendition _setStructuredThemeStore:];
-[_CUIInternalLinkRendition isInternalLink];
-[_CUIInternalLinkRendition bitmapEncoding];
-[_CUIInternalLinkRendition imageForSliceIndex:];
-[_CUIInternalLinkRendition alphaCroppedRect];
-[_CUIInternalLinkRendition originalUncroppedSize];
-[_CUIInternalLinkRendition unslicedSize];
-[_CUIInternalLinkRendition pixelFormat];
-[_CUIInternalLinkRendition _destinationFrame];
-[_CUIInternalLinkRendition _initWithCSIHeader:version:];
-[_CUIInternalLinkRendition metrics];
-[_CUIInternalLinkRendition maskForSliceIndex:];
-[_CUIInternalLinkRendition initWithCSIData:forKey:version:];
```
