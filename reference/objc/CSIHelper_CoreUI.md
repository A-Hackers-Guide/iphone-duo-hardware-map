# `CSIHelper`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 16 instance variables, 0 properties, 1 instance methods, 0 class methods

## Instance variables

```
{_slice="x"I"y"I"width"I"height"I} slice;
@"NSData" csiData;
^{_csibitmap=I(?=I{_csibitmapflags=b1b1b30})II[0C]} bmp;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} renditionLock;
@"_CUIThemePixelRendition" rendition;
@"_CSIRenditionBlockData" sharedBlockDataBGRX;
@"_CSIRenditionBlockData" sharedBlockDataRGBX;
@"_CSIRenditionBlockData" sharedBlockDataGray;
@"_CSIRenditionBlockData" retainedBlockData;
@"NSString" blockDataCacheKeyBGRX;
@"NSString" blockDataCacheKeyRGBX;
@"NSString" blockDataCacheKeyGray;
Q sourceRowbytes;
b1 shouldCache;
b1 usedForDataProvider;
b30 _reserved;
```

## Instance methods

```
-[CSIHelper dealloc];
```
