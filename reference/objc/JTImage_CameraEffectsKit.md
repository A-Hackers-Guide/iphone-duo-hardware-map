# `JTImage`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"UIImage" _image;
@"PVImageBuffer" _pvImageBuffer;
```

## Properties

```
@property (T@"UIImage",R,N,V_image) image;
@property (T@"PVImageBuffer",R,N,V_pvImageBuffer) pvImageBuffer;
```

## Class methods

```
+[JTImage jtImageWithUIImage:];
```

## Instance methods

```
-[JTImage image];
-[JTImage bluredImageWithFlippedXAxis:];
-[JTImage hasPVImageBufferAndCanCreateCVPixelBufferWithoutCopy];
-[JTImage initWithPVImage:];
-[JTImage initWithUIImage:];
-[JTImage pvImageBuffer];
```
