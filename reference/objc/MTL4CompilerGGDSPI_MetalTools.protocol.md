# `MTL4CompilerGGDSPI` (protocol)

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTL4CompilerSPI`
- 0 instance variables, 2 properties, 4 instance methods, 0 class methods

## Properties

```
@property (T@"<MTLBinaryArchive>",R) destinationBinaryArchive;
@property (TB,R) shouldMaximizeConcurrentCompilation;
```

## Instance methods

```
-[MTL4CompilerGGDSPI newDynamicLibraryWithURL:options:error:];
-[MTL4CompilerGGDSPI destinationBinaryArchive];
-[MTL4CompilerGGDSPI newDynamicLibraryWithURL:options:completionHandler:];
-[MTL4CompilerGGDSPI shouldMaximizeConcurrentCompilation];
```
