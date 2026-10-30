# `MTLBinaryArchiveSPI` (protocol)

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLBinaryArchive`
- 0 instance variables, 2 properties, 17 instance methods, 0 class methods

## Properties

```
@property (TQ,R) options;
@property (T@"NSArray",R) keys;
```

## Instance methods

```
-[MTLBinaryArchiveSPI storeTileRenderPipelineDescriptor:];
-[MTLBinaryArchiveSPI recompileToArchiveWithURL:error:];
-[MTLBinaryArchiveSPI formattedDescription:];
-[MTLBinaryArchiveSPI storeRenderPipelineDescriptor:];
-[MTLBinaryArchiveSPI addTileRenderPipelineFunctionsWithDescriptor:options:error:];
-[MTLBinaryArchiveSPI addComputePipelineFunctionsWithDescriptor:options:error:];
-[MTLBinaryArchiveSPI pipelineCollection];
-[MTLBinaryArchiveSPI enumerateArchivesFromBackingFile:];
-[MTLBinaryArchiveSPI keys];
-[MTLBinaryArchiveSPI storeMeshRenderPipelineDescriptor:];
-[MTLBinaryArchiveSPI storeComputePipelineDescriptor:];
-[MTLBinaryArchiveSPI options];
-[MTLBinaryArchiveSPI addMeshRenderPipelineFunctionsWithDescriptor:options:error:];
-[MTLBinaryArchiveSPI archiveFunctionIds];
-[MTLBinaryArchiveSPI serializeToURL:options:error:];
-[MTLBinaryArchiveSPI enumerateArchivesFromPipelineCollection:];
-[MTLBinaryArchiveSPI addRenderPipelineFunctionsWithDescriptor:options:error:];
```
