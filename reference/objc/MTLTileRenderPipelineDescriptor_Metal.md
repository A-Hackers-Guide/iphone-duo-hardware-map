# `MTLTileRenderPipelineDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 4 instance variables, 14 properties, 10 instance methods, 2 class methods

## Instance variables

```
B _supportAddingBinaryFunctions;
@"NSArray" _preloadedLibraries;
Q _maxCallStackDepth;
{?="width"Q"height"Q"depth"Q} _requiredThreadsPerThreadgroup;
```

## Properties

```
@property (T@"NSString",C,D,N) label;
@property (T@"<MTLFunction>",&,D,N) tileFunction;
@property (TQ,D,N) rasterSampleCount;
@property (T@"MTLTileRenderPipelineColorAttachmentDescriptorArray",R,D) colorAttachments;
@property (TB,D,N) threadgroupSizeMatchesTileSize;
@property (T@"MTLPipelineBufferDescriptorArray",R,D) tileBuffers;
@property (TQ,D,N) maxTotalThreadsPerThreadgroup;
@property (T@"NSArray",C,D,N) binaryArchives;
@property (T@"NSArray",C,N,V_preloadedLibraries) preloadedLibraries;
@property (T@"MTLLinkedFunctions",C,D,N) linkedFunctions;
@property (TB,N,V_supportAddingBinaryFunctions) supportAddingBinaryFunctions;
@property (TQ,N,V_maxCallStackDepth) maxCallStackDepth;
@property (Tq,D,N) shaderValidation;
@property (T{?=QQQ},N,V_requiredThreadsPerThreadgroup) requiredThreadsPerThreadgroup;
```

## Class methods

```
+[MTLTileRenderPipelineDescriptor allocWithZone:];
+[MTLTileRenderPipelineDescriptor alloc];
```

## Instance methods

```
-[MTLTileRenderPipelineDescriptor supportAddingBinaryFunctions];
-[MTLTileRenderPipelineDescriptor setRequiredThreadsPerThreadgroup:];
-[MTLTileRenderPipelineDescriptor maxCallStackDepth];
-[MTLTileRenderPipelineDescriptor setMaxCallStackDepth:];
-[MTLTileRenderPipelineDescriptor setSupportAddingBinaryFunctions:];
-[MTLTileRenderPipelineDescriptor preloadedLibraries];
-[MTLTileRenderPipelineDescriptor reset];
-[MTLTileRenderPipelineDescriptor setPreloadedLibraries:];
-[MTLTileRenderPipelineDescriptor requiredThreadsPerThreadgroup];
-[MTLTileRenderPipelineDescriptor copyWithZone:];
```
