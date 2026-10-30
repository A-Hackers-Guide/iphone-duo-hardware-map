# `DYMTLTextureResize`

- Image: [`/System/Library/PrivateFrameworks/MTLToolsDeviceSupport.framework/MTLToolsDeviceSupport`](../userland/System__Library__PrivateFrameworks__MTLToolsDeviceSupport.framework__MTLToolsDeviceSupport.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 17 instance variables, 1 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"<MTLDepthStencilState>" _thumbnailDepthStencilState;
@"<MTLSamplerState>" _downscaleSampler;
@"<MTLSamplerState>" _upscaleSampler;
@"<MTLBuffer>" _quadPositions;
@"<MTLBuffer>" _quadTexCoords;
@"<MTLBuffer>" _quadIndicies;
@"<MTLFunction>" _thumbnailColorFragment;
@"<MTLFunction>" _thumbnailDepthFragment;
@"<MTLFunction>" _thumbnailStencilFragment;
@"<MTLRenderPipelineState>" _thumbnailPipeline;
@"MTLRenderPipelineDescriptor" _thumbnailPipelineDescriptor;
@"MTLTextureDescriptor" _thumbnailTextureDescriptor;
@"MTLRenderPassDescriptor" _thumbnailRenderPass;
q configureThumbnail;
@"NSMutableDictionary" _thumbnailDictionary;
@"NSMutableDictionary" _fragmentFunctionForPixelFormatCache;
@"<MTLDevice>" _device;
```

## Properties

```
@property (T@"<MTLDevice>",R,V_device) device;
```

## Class methods

```
+[DYMTLTextureResize forDevice:];
```

## Instance methods

```
-[DYMTLTextureResize initWithDevice:];
-[DYMTLTextureResize device];
-[DYMTLTextureResize resolveMultisampleTexture:slice:level:depthPlane:commandBuffer:];
-[DYMTLTextureResize _texture2DFromTexture:level:slice:depthPlane:commandBuffer:];
-[DYMTLTextureResize generateThumbnailFromTexture:commandBuffer:resolution:withFence:];
-[DYMTLTextureResize resizeTexture:resolution:level:slice:depthPlane:inBuffer:withType:completion:];
-[DYMTLTextureResize stencilTextureFromTexture:commandBuffer:];
-[DYMTLTextureResize textureFromTexture:slice:level:depthPlane:commandBuffer:];
-[DYMTLTextureResize dataTypeForReturnType:];
-[DYMTLTextureResize generateFragmentFunctionForPixelFormat:texture:];
-[DYMTLTextureResize returnTypeForPixelFormat:];
-[DYMTLTextureResize textureTypeForPixelFormat:];
```
