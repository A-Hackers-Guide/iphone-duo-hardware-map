# `MTKTextureLoaderData`

- Image: [`/System/Library/Frameworks/MetalKit.framework/MetalKit`](../userland/System__Library__Frameworks__MetalKit.framework__MetalKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 9 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"NSString" _imageOrigin;
Q _numArrayElements;
Q _numFaces;
Q _numMipmapLevels;
Q _width;
Q _height;
Q _depth;
Q _textureType;
Q _pixelFormat;
```

## Properties

```
@property (T@"NSString",N,V_imageOrigin) imageOrigin;
@property (TQ,N,V_numArrayElements) numArrayElements;
@property (TQ,N,V_numFaces) numFaces;
@property (TQ,N,V_numMipmapLevels) numMipmapLevels;
@property (TQ,N,V_width) width;
@property (TQ,N,V_height) height;
@property (TQ,N,V_depth) depth;
@property (TQ,N,V_textureType) textureType;
@property (TQ,N,V_pixelFormat) pixelFormat;
```

## Instance methods

```
-[MTKTextureLoaderData setDepth:];
-[MTKTextureLoaderData depth];
-[MTKTextureLoaderData init];
-[MTKTextureLoaderData dealloc];
-[MTKTextureLoaderData textureType];
-[MTKTextureLoaderData getDataForArrayElement:face:level:depthPlane:bytesPerRow:bytesPerImage:];
-[MTKTextureLoaderData numFaces];
-[MTKTextureLoaderData setHeight:];
-[MTKTextureLoaderData pixelFormat];
-[MTKTextureLoaderData setWidth:];
-[MTKTextureLoaderData width];
-[MTKTextureLoaderData setPixelFormat:];
-[MTKTextureLoaderData height];
-[MTKTextureLoaderData imageOrigin];
-[MTKTextureLoaderData setTextureType:];
-[MTKTextureLoaderData numMipmapLevels];
-[MTKTextureLoaderData setImageOrigin:];
-[MTKTextureLoaderData numArrayElements];
-[MTKTextureLoaderData setNumArrayElements:];
-[MTKTextureLoaderData setNumFaces:];
-[MTKTextureLoaderData setNumMipmapLevels:];
```
