# `MTKTextureLoaderMDL`

- Image: [`/System/Library/Frameworks/MetalKit.framework/MetalKit`](../userland/System__Library__Frameworks__MetalKit.framework__MetalKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTKTextureLoaderData`
- 2 instance variables, 0 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"MDLTexture" _texture;
{MTLPixelFormatInfo="name"*"flags"I"castClass"Q"type"(?="normal"{MTLNormalPixelFormatInfo="pixelBytes"Q"componentCount"C"alignment"C"pixelBytesRender"Q"pixelBytesRenderMSAA"Q}"compressed"{MTLCompressedPixelFormatInfo="blockBytes"Q"blockWidth"Q"blockHeight"Q"blockDepth"Q})} _pixelFormatInfo;
```

## Instance methods

```
-[MTKTextureLoaderMDL dealloc];
-[MTKTextureLoaderMDL getDataForArrayElement:face:level:depthPlane:bytesPerRow:bytesPerImage:];
-[MTKTextureLoaderMDL determineFormatFromChannelEncoding:channelCount:error:];
-[MTKTextureLoaderMDL initWithMDLTexture:options:error:];
```
