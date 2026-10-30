# `MTKTextureLoaderImageIO`

- Image: [`/System/Library/Frameworks/MetalKit.framework/MetalKit`](../userland/System__Library__Frameworks__MetalKit.framework__MetalKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTKTextureLoaderData`
- 6 instance variables, 0 properties, 8 instance methods, 0 class methods

## Instance variables

```
^{CGImageBlockSet=} _blockSet;
^{__CFData=} _cfData;
{MTLPixelFormatInfo="name"*"flags"I"castClass"Q"type"(?="normal"{MTLNormalPixelFormatInfo="pixelBytes"Q"componentCount"C"alignment"C"pixelBytesRender"Q"pixelBytesRenderMSAA"Q}"compressed"{MTLCompressedPixelFormatInfo="blockBytes"Q"blockWidth"Q"blockHeight"Q"blockDepth"Q})} _pixelFormatInfo;
Q _bytesPerRow;
@"NSData" _imageData;
B _expandRGBToRGBA;
```

## Instance methods

```
-[MTKTextureLoaderImageIO determineCGImageBlockFormatWithComponentType:alphaInfo:andPixelSizeBytes:andColorSpace:isOptimized:options:];
-[MTKTextureLoaderImageIO decodeCGImage:options:];
-[MTKTextureLoaderImageIO initWithCGImage:options:error:];
-[MTKTextureLoaderImageIO dealloc];
-[MTKTextureLoaderImageIO decodeCGImageDataProvider:options:];
-[MTKTextureLoaderImageIO getDataForArrayElement:face:level:depthPlane:bytesPerRow:bytesPerImage:];
-[MTKTextureLoaderImageIO initWithData:options:error:];
-[MTKTextureLoaderImageIO decodeCGImageImageProvider:CGImageProvider:options:];
```
