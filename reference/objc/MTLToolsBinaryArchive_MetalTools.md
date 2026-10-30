# `MTLToolsBinaryArchive`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsObject`
- Protocols: `MTLBinaryArchiveSPI`
- 0 instance variables, 8 properties, 27 instance methods, 0 class methods

## Properties

```
@property (TQ,R) options;
@property (T@"NSArray",R) keys;
@property (T@"NSString",C) label;
@property (T@"<MTLDevice>",R) device;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLToolsBinaryArchive addTileRenderPipelineFunctionsWithDescriptor:error:];
-[MTLToolsBinaryArchive storeTileRenderPipelineDescriptor:];
-[MTLToolsBinaryArchive recompileToArchiveWithURL:error:];
-[MTLToolsBinaryArchive formattedDescription:];
-[MTLToolsBinaryArchive storeRenderPipelineDescriptor:];
-[MTLToolsBinaryArchive device];
-[MTLToolsBinaryArchive label];
-[MTLToolsBinaryArchive addFunctionWithDescriptor:library:error:];
-[MTLToolsBinaryArchive setLabel:];
-[MTLToolsBinaryArchive addTileRenderPipelineFunctionsWithDescriptor:options:error:];
-[MTLToolsBinaryArchive addComputePipelineFunctionsWithDescriptor:options:error:];
-[MTLToolsBinaryArchive pipelineCollection];
-[MTLToolsBinaryArchive enumerateArchivesFromBackingFile:];
-[MTLToolsBinaryArchive keys];
-[MTLToolsBinaryArchive storeMeshRenderPipelineDescriptor:];
-[MTLToolsBinaryArchive addRenderPipelineFunctionsWithDescriptor:error:];
-[MTLToolsBinaryArchive storeComputePipelineDescriptor:];
-[MTLToolsBinaryArchive serializeToURL:error:];
-[MTLToolsBinaryArchive options];
-[MTLToolsBinaryArchive addMeshRenderPipelineFunctionsWithDescriptor:error:];
-[MTLToolsBinaryArchive addMeshRenderPipelineFunctionsWithDescriptor:options:error:];
-[MTLToolsBinaryArchive addLibraryWithDescriptor:error:];
-[MTLToolsBinaryArchive archiveFunctionIds];
-[MTLToolsBinaryArchive serializeToURL:options:error:];
-[MTLToolsBinaryArchive addComputePipelineFunctionsWithDescriptor:error:];
-[MTLToolsBinaryArchive enumerateArchivesFromPipelineCollection:];
-[MTLToolsBinaryArchive addRenderPipelineFunctionsWithDescriptor:options:error:];
```
