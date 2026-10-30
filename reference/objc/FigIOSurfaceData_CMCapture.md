# `FigIOSurfaceData`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSData`
- 3 instance variables, 0 properties, 6 instance methods, 3 class methods

## Instance variables

```
^{__IOSurface=} _surface;
Q _length;
r^v _bytes;
```

## Class methods

```
+[FigIOSurfaceData initialize];
+[FigIOSurfaceData dataWithIOSurface:];
+[FigIOSurfaceData dataWithIOSurface:length:];
```

## Instance methods

```
-[FigIOSurfaceData dealloc];
-[FigIOSurfaceData length];
-[FigIOSurfaceData initWithIOSurface:];
-[FigIOSurfaceData copyWithZone:];
-[FigIOSurfaceData bytes];
-[FigIOSurfaceData initWithIOSurface:length:];
```
