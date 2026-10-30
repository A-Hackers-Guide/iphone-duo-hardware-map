# `_CUIThemeSVGRendition`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CUIThemeRendition`
- Protocols: `NSLocking`
- 4 instance variables, 0 properties, 10 instance methods, 0 class methods

## Instance variables

```
^{CGSVGDocument=} _svgDocument;
@"NSData" _fileData;
{CGSize="width"d"height"d} _canvasSize;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
```

## Instance methods

```
-[_CUIThemeSVGRendition canvasSize];
-[_CUIThemeSVGRendition svgDocument];
-[_CUIThemeSVGRendition dealloc];
-[_CUIThemeSVGRendition rawData];
-[_CUIThemeSVGRendition pixelFormat];
-[_CUIThemeSVGRendition lock];
-[_CUIThemeSVGRendition _initWithCSIHeader:version:];
-[_CUIThemeSVGRendition metrics];
-[_CUIThemeSVGRendition unlock];
-[_CUIThemeSVGRendition initWithCSIData:forKey:version:];
```
