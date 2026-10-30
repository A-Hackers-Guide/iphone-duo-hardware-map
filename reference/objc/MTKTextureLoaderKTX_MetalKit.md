# `MTKTextureLoaderKTX`

- Image: [`/System/Library/Frameworks/MetalKit.framework/MetalKit`](../userland/System__Library__Frameworks__MetalKit.framework__MetalKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTKTextureLoaderData`
- 3 instance variables, 0 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"NSData" _imageData;
{MTLPixelFormatInfo="name"*"flags"I"castClass"Q"type"(?="normal"{MTLNormalPixelFormatInfo="pixelBytes"Q"componentCount"C"alignment"C"pixelBytesRender"Q"pixelBytesRenderMSAA"Q}"compressed"{MTLCompressedPixelFormatInfo="blockBytes"Q"blockWidth"Q"blockHeight"Q"blockDepth"Q})} _pixelFormatInfo;
B _packedRowStride;
```

## Class methods

```
+[MTKTextureLoaderKTX isKTXFile:];
```

## Instance methods

```
-[MTKTextureLoaderKTX dealloc];
-[MTKTextureLoaderKTX getDataForArrayElement:face:level:depthPlane:bytesPerRow:bytesPerImage:];
-[MTKTextureLoaderKTX initWithData:options:error:];
-[MTKTextureLoaderKTX determineFormatFromSizedFormat:];
-[MTKTextureLoaderKTX determineFormatFromType:format:internalFormat:baseInternalFormat:];
-[MTKTextureLoaderKTX parseKey:value:error:];
-[MTKTextureLoaderKTX parseKeyValueBytes:length:error:];
```
