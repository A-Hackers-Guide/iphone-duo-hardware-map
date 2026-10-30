# `MTLBinaryArchive` (protocol)

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
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
