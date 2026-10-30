# `_UIImageIOSurfaceContent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIImageContent`
- 3 instance variables, 0 properties, 22 instance methods, 0 class methods

## Instance variables

```
^{__IOSurface=} _surface;
^{__IOSurface=} _hdrSurface;
d _headroom;
```

## Instance methods

```
-[_UIImageIOSurfaceContent layerContents];
-[_UIImageIOSurfaceContent initWithIOSurface:scale:];
-[_UIImageIOSurfaceContent sizeInPixels];
-[_UIImageIOSurfaceContent isHDR];
-[_UIImageIOSurfaceContent typeName];
-[_UIImageIOSurfaceContent dealloc];
-[_UIImageIOSurfaceContent makeSDRVersion];
-[_UIImageIOSurfaceContent imageMaximumHeadroom];
-[_UIImageIOSurfaceContent _drawWithSize:scale:inContext:renditionContext:];
-[_UIImageIOSurfaceContent imageRendererFormat];
-[_UIImageIOSurfaceContent canWriteToImageIO];
-[_UIImageIOSurfaceContent initWithSDRIOSurface:HDRIOSurface:scale:];
-[_UIImageIOSurfaceContent hash];
-[_UIImageIOSurfaceContent description];
-[_UIImageIOSurfaceContent alternateIOSurface];
-[_UIImageIOSurfaceContent addContentToDestination:properties:];
-[_UIImageIOSurfaceContent _prepareForDrawingWithSize:scale:inContext:];
-[_UIImageIOSurfaceContent isIOSurface];
-[_UIImageIOSurfaceContent isEqual:];
-[_UIImageIOSurfaceContent IOSurface];
-[_UIImageIOSurfaceContent prefersProvidingNonCGImageContentsDirectlyForRendering];
-[_UIImageIOSurfaceContent initWithScale:];
```
