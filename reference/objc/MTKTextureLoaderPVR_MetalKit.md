# `MTKTextureLoaderPVR`

- Image: [`/System/Library/Frameworks/MetalKit.framework/MetalKit`](../userland/System__Library__Frameworks__MetalKit.framework__MetalKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTKTextureLoaderData`
- 4 instance variables, 0 properties, 5 instance methods, 1 class methods

## Instance variables

```
I _pvrFormat;
I _numSurfaces;
@"NSData" _imageData;
{MTLPixelFormatInfo="name"*"flags"I"castClass"Q"type"(?="normal"{MTLNormalPixelFormatInfo="pixelBytes"Q"componentCount"C"alignment"C"pixelBytesRender"Q"pixelBytesRenderMSAA"Q}"compressed"{MTLCompressedPixelFormatInfo="blockBytes"Q"blockWidth"Q"blockHeight"Q"blockDepth"Q})} _pixelFormatInfo;
```

## Class methods

```
+[MTKTextureLoaderPVR isPVRFile:];
```

## Instance methods

```
-[MTKTextureLoaderPVR dealloc];
-[MTKTextureLoaderPVR getDataForArrayElement:face:level:depthPlane:bytesPerRow:bytesPerImage:];
-[MTKTextureLoaderPVR initWithData:options:error:];
-[MTKTextureLoaderPVR determineBlockSize:blocksWide:blocksHigh:bytesPerBlock:fromFormat:width:andHeight:];
-[MTKTextureLoaderPVR determineFormat:options:];
```
