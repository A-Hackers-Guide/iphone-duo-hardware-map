# `PixelMetalBufferPair`

- Image: [`/System/Library/PrivateFrameworks/ISPKit.framework/ISPKit`](../userland/System__Library__PrivateFrameworks__ISPKit.framework__ISPKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 4 properties, 10 instance methods, 1 class methods

## Instance variables

```
^{__CVBuffer=} _pixelBuffer;
^{__CVBuffer=} _cvMetalTexture;
@"<MTLTexture>" _texture;
@"<MTLBuffer>" _buffer;
Q _bytesPerRow;
```

## Properties

```
@property (T^{__CVBuffer=},R,N,V_pixelBuffer) pixelBuffer;
@property (T@"<MTLTexture>",R,N,V_texture) texture;
@property (T@"<MTLBuffer>",R,N,V_buffer) buffer;
@property (TQ,R,N,V_bytesPerRow) bytesPerRow;
```

## Class methods

```
+[PixelMetalBufferPair metalPixelFormatForCVPixelFormat:plane:];
```

## Instance methods

```
-[PixelMetalBufferPair buffer];
-[PixelMetalBufferPair pixelBuffer];
-[PixelMetalBufferPair bytesPerRow];
-[PixelMetalBufferPair dealloc];
-[PixelMetalBufferPair texture];
-[PixelMetalBufferPair createTextureWithTextureCache:pixelBuffer:mtlPixelFormat:plane:usage:];
-[PixelMetalBufferPair initWithPixelBuffer:textureCache:plane:usage:];
-[PixelMetalBufferPair initWithPixelBufferAsBuffer:device:plane:];
-[PixelMetalBufferPair initWithWidth:height:cvPixelFormat:textureCache:plane:usage:];
-[PixelMetalBufferPair initWithWidth:height:cvPixelFormat:textureCache:usage:];
```
