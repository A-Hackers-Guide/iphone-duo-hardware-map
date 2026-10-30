# `MTLBinaryArchive` (protocol)

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 2 properties, 10 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",C) label;
@property (T@"<MTLDevice>",R) device;
```

## Instance methods

```
-[MTLBinaryArchive addTileRenderPipelineFunctionsWithDescriptor:error:];
-[MTLBinaryArchive device];
-[MTLBinaryArchive label];
-[MTLBinaryArchive addFunctionWithDescriptor:library:error:];
-[MTLBinaryArchive setLabel:];
-[MTLBinaryArchive addRenderPipelineFunctionsWithDescriptor:error:];
-[MTLBinaryArchive serializeToURL:error:];
-[MTLBinaryArchive addMeshRenderPipelineFunctionsWithDescriptor:error:];
-[MTLBinaryArchive addLibraryWithDescriptor:error:];
-[MTLBinaryArchive addComputePipelineFunctionsWithDescriptor:error:];
```
