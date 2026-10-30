# `JFXPixelBufferPool`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 2 properties, 6 instance methods, 0 class methods

## Instance variables

```
^{__CVPixelBufferPool=} _pixelBufferPool;
I _type;
{CGSize="width"d"height"d} _size;
```

## Properties

```
@property (T{CGSize=dd},R,N,V_size) size;
@property (TI,R,N,V_type) type;
```

## Instance methods

```
-[JFXPixelBufferPool initWithSize:];
-[JFXPixelBufferPool dealloc];
-[JFXPixelBufferPool size];
-[JFXPixelBufferPool type];
-[JFXPixelBufferPool createPixelBuffer];
-[JFXPixelBufferPool initWithSize:type:];
```
