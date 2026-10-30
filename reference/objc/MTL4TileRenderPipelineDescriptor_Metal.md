# `MTL4TileRenderPipelineDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTL4PipelineDescriptor`
- 8 instance variables, 8 properties, 22 instance methods, 0 class methods

## Instance variables

```
B _threadgroupSizeMatchesTileSize;
B _supportBinaryLinking;
@"MTL4StaticLinkingDescriptor" _staticLinkingDescriptor;
@"MTL4FunctionDescriptor" _tileFunctionDescriptor;
Q _rasterSampleCount;
@"MTLTileRenderPipelineColorAttachmentDescriptorArray" _colorAttachments;
Q _maxTotalThreadsPerThreadgroup;
{?="width"Q"height"Q"depth"Q} _requiredThreadsPerThreadgroup;
```

## Properties

```
@property (T@"MTL4FunctionDescriptor",C,N,V_tileFunctionDescriptor) tileFunctionDescriptor;
@property (TQ,N,V_rasterSampleCount) rasterSampleCount;
@property (T@"MTLTileRenderPipelineColorAttachmentDescriptorArray",R,V_colorAttachments) colorAttachments;
@property (TB,N,V_threadgroupSizeMatchesTileSize) threadgroupSizeMatchesTileSize;
@property (TQ,N,V_maxTotalThreadsPerThreadgroup) maxTotalThreadsPerThreadgroup;
@property (T{?=QQQ},N,V_requiredThreadsPerThreadgroup) requiredThreadsPerThreadgroup;
@property (T@"MTL4StaticLinkingDescriptor",C,N,V_staticLinkingDescriptor) staticLinkingDescriptor;
@property (TB,N,V_supportBinaryLinking) supportBinaryLinking;
```

## Instance methods

```
-[MTL4TileRenderPipelineDescriptor colorAttachments];
-[MTL4TileRenderPipelineDescriptor setRasterSampleCount:];
-[MTL4TileRenderPipelineDescriptor setRequiredThreadsPerThreadgroup:];
-[MTL4TileRenderPipelineDescriptor staticLinkingDescriptor];
-[MTL4TileRenderPipelineDescriptor init];
-[MTL4TileRenderPipelineDescriptor rasterSampleCount];
-[MTL4TileRenderPipelineDescriptor tileFunctionDescriptor];
-[MTL4TileRenderPipelineDescriptor dealloc];
-[MTL4TileRenderPipelineDescriptor setThreadgroupSizeMatchesTileSize:];
-[MTL4TileRenderPipelineDescriptor setTileFunctionDescriptor:];
-[MTL4TileRenderPipelineDescriptor reset];
-[MTL4TileRenderPipelineDescriptor threadgroupSizeMatchesTileSize];
-[MTL4TileRenderPipelineDescriptor setMaxTotalThreadsPerThreadgroup:];
-[MTL4TileRenderPipelineDescriptor requiredThreadsPerThreadgroup];
-[MTL4TileRenderPipelineDescriptor maxTotalThreadsPerThreadgroup];
-[MTL4TileRenderPipelineDescriptor setStaticLinkingDescriptor:];
-[MTL4TileRenderPipelineDescriptor hash];
-[MTL4TileRenderPipelineDescriptor copyWithZone:];
-[MTL4TileRenderPipelineDescriptor isEqual:];
-[MTL4TileRenderPipelineDescriptor _staticLinkingDescriptorNoAlloc];
-[MTL4TileRenderPipelineDescriptor setSupportBinaryLinking:];
-[MTL4TileRenderPipelineDescriptor supportBinaryLinking];
```
