# `MPSGraphDelegatePrecompilationDescriptor`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- 4 instance variables, 4 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSString" _architecture;
q _gpuCoreCount;
@"NSURL" _aneOptionsURL;
q _aneMaxRegions;
```

## Properties

```
@property (T@"NSString",&,V_architecture) architecture;
@property (Tq,V_gpuCoreCount) gpuCoreCount;
@property (T@"NSURL",&,V_aneOptionsURL) aneOptionsURL;
@property (Tq,V_aneMaxRegions) aneMaxRegions;
```

## Instance methods

```
-[MPSGraphDelegatePrecompilationDescriptor architecture];
-[MPSGraphDelegatePrecompilationDescriptor gpuCoreCount];
-[MPSGraphDelegatePrecompilationDescriptor setArchitecture:];
-[MPSGraphDelegatePrecompilationDescriptor aneMaxRegions];
-[MPSGraphDelegatePrecompilationDescriptor aneOptionsURL];
-[MPSGraphDelegatePrecompilationDescriptor initWithArchitecture:];
-[MPSGraphDelegatePrecompilationDescriptor initWithArchitecture:aneOptionsURL:];
-[MPSGraphDelegatePrecompilationDescriptor initWithArchitecture:gpuCoreCount:];
-[MPSGraphDelegatePrecompilationDescriptor initWithArchitecture:gpuCoreCount:aneOptionsURL:];
-[MPSGraphDelegatePrecompilationDescriptor setAneMaxRegions:];
-[MPSGraphDelegatePrecompilationDescriptor setAneOptionsURL:];
-[MPSGraphDelegatePrecompilationDescriptor setGpuCoreCount:];
-[MPSGraphDelegatePrecompilationDescriptor validatePrecompilationOptions];
```
