# `MTLTelemetryTexture`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsTexture`
- 3 instance variables, 0 properties, 11 instance methods, 0 class methods

## Instance variables

```
Q mipmapClipType;
@"MTLTextureDescriptor" _telemetryDescriptor;
@"MTLTelemetryDevice" _telemetryDevice;
```

## Instance methods

```
-[MTLTelemetryTexture newTextureViewWithPixelFormat:textureType:levels:slices:];
-[MTLTelemetryTexture newTextureViewWithPixelFormat:textureType:levels:slices:swizzle:];
-[MTLTelemetryTexture newTextureViewWithPixelFormat:];
-[MTLTelemetryTexture accumTextureDistribution:category:pixelFormat:baseAddr:rowBytes:isLinear:];
-[MTLTelemetryTexture initMipmapClipType];
-[MTLTelemetryTexture initWithBaseTexture:device:buffer:descriptor:offset:bytesPerRow:];
-[MTLTelemetryTexture initWithBaseTexture:device:descriptor:];
-[MTLTelemetryTexture initWithBaseTexture:device:descriptor:plane:];
-[MTLTelemetryTexture initWithBaseTexture:device:texture:descriptor:];
-[MTLTelemetryTexture initWithBaseTexture:device:texture:pixelFormat:];
-[MTLTelemetryTexture initWithBaseTexture:device:texture:pixelFormat:textureType:levels:slices:swizzle:];
```
