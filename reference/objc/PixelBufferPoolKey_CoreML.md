# `PixelBufferPoolKey`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 2 instance variables, 2 properties, 6 instance methods, 0 class methods

## Instance variables

```
I _pixelFormatType;
{CGSize="width"d"height"d} _frameSize;
```

## Properties

```
@property (T{CGSize=dd},R,N,V_frameSize) frameSize;
@property (TI,R,N,V_pixelFormatType) pixelFormatType;
```

## Instance methods

```
-[PixelBufferPoolKey initWithSize:pixelFormatType:];
-[PixelBufferPoolKey hash];
-[PixelBufferPoolKey copyWithZone:];
-[PixelBufferPoolKey isEqual:];
-[PixelBufferPoolKey pixelFormatType];
-[PixelBufferPoolKey frameSize];
```
