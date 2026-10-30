# `EspressoMetalKernelsCache`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 2 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"<MTLLibrary>" m_ShaderLibrary;
@"<MTLLibrary>" m_DefaultLibrary;
@"<MTLDevice>" _device;
B isSupportingiOSGPUFamilyV2;
@"NSObject<OS_dispatch_queue>" dictionary_write_queue;
@"NSMutableDictionary" auxLibraries;
@"NSMutableDictionary" m_kernelCache_rw;
{mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}} setup_mutex;
@"NSString" _kernelPrefix;
@"NSDictionary" _m_kernelCache;
```

## Properties

```
@property (T@"NSDictionary",&,V_m_kernelCache) m_kernelCache;
@property (T@"NSString",&,N,V_kernelPrefix) kernelPrefix;
```

## Instance methods

```
-[EspressoMetalKernelsCache initWithDevice:];
-[EspressoMetalKernelsCache shouldUseTexArray];
-[EspressoMetalKernelsCache wasSetup];
-[EspressoMetalKernelsCache loadLibraryNamed:];
-[EspressoMetalKernelsCache addLibraryAtPath:];
-[EspressoMetalKernelsCache lazySetup];
-[EspressoMetalKernelsCache m_kernelCache];
-[EspressoMetalKernelsCache kernelForFunction:cacheString:withConstants:];
-[EspressoMetalKernelsCache setM_kernelCache:];
-[EspressoMetalKernelsCache kernelForFunction:];
-[EspressoMetalKernelsCache kernelPrefix];
-[EspressoMetalKernelsCache setKernelPrefix:];
```
