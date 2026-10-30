# `MTKTextureLoaderPVR3`

- Image: [`/System/Library/Frameworks/MetalKit.framework/MetalKit`](../userland/System__Library__Frameworks__MetalKit.framework__MetalKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTKTextureLoaderData`
- 4 instance variables, 0 properties, 6 instance methods, 1 class methods

## Instance variables

```
i _pvrCompressedFormat;
{MTLPixelFormatInfo="name"*"flags"I"castClass"Q"type"(?="normal"{MTLNormalPixelFormatInfo="pixelBytes"Q"componentCount"C"alignment"C"pixelBytesRender"Q"pixelBytesRenderMSAA"Q}"compressed"{MTLCompressedPixelFormatInfo="blockBytes"Q"blockWidth"Q"blockHeight"Q"blockDepth"Q})} _pixelFormatInfo;
I _metaDataSize;
@"NSData" _imageData;
```

## Class methods

```
+[MTKTextureLoaderPVR3 isPVR3File:];
```

## Instance methods

```
-[MTKTextureLoaderPVR3 dealloc];
-[MTKTextureLoaderPVR3 getDataForArrayElement:face:level:depthPlane:bytesPerRow:bytesPerImage:];
-[MTKTextureLoaderPVR3 initWithData:options:error:];
-[MTKTextureLoaderPVR3 determineBlockSize:blocksWide:blocksHigh:bytesPerBlock:fromFormat:width:andHeight:];
-[MTKTextureLoaderPVR3 determineFormat:colorSpace:channelType:options:];
-[MTKTextureLoaderPVR3 parseMetadataWithError:];
```
