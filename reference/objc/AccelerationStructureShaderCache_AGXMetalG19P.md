# `AccelerationStructureShaderCache`

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 1 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"<MTLDevice>" _device;
{array<Library, 6UL>="__elems_"[6{Library="_library"{pair<id<MTLLibrary>, id<MTLBinaryArchive>>="first"@"<MTLLibrary>""second"@"<MTLBinaryArchive>"}"_mutex"{UnfairLock="m_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}}}]} _libraries;
{array<Library, 6UL>="__elems_"[6{Library="_library"{pair<id<MTLLibrary>, id<MTLBinaryArchive>>="first"@"<MTLLibrary>""second"@"<MTLBinaryArchive>"}"_mutex"{UnfairLock="m_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}}}]} _assertLibraries;
[172[6{KernelEntry="_pso"[2@"<MTLComputePipelineState>"]"_mutex"{UnfairLock="m_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}}"_maxThreadsPerThreadgroup"[2I]"_threadExecutionWidth"[2I]}]] _kernels;
```

## Properties

```
@property (T@"<MTLDevice>",R) device;
```

## Instance methods

```
-[AccelerationStructureShaderCache initWithDevice:];
-[AccelerationStructureShaderCache device];
-[AccelerationStructureShaderCache threadExecutionWidth:assertLib:];
-[AccelerationStructureShaderCache compilePipeline:backend:assertLib:];
-[AccelerationStructureShaderCache findKernelsMissingFromBinaryArchive:assertLib:];
-[AccelerationStructureShaderCache getLibrary:assertLib:];
-[AccelerationStructureShaderCache maxThreadsPerThreadgroup:assertLib:];
```
