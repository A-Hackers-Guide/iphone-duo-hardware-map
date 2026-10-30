# `MPSGraphExecutableDescriptor`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- 7 instance variables, 8 properties, 17 instance methods, 0 class methods

## Instance variables

```
B _isAICodeBytecode;
B _includeDebugInfo;
B _addUniqueIdToMLIRLocations;
@? _variableFetchHandler;
@"MPSGraphCompilationDescriptor" _compilationDescriptor;
Q _aneProfilingMask;
@"NSDictionary" _perDeviceDescriptorCompilationOptions;
```

## Properties

```
@property (TQ) compilerOptions;
@property (T@?,C,V_variableFetchHandler) variableFetchHandler;
@property (T@"MPSGraphCompilationDescriptor",&,V_compilationDescriptor) compilationDescriptor;
@property (TB,V_isAICodeBytecode) isAICodeBytecode;
@property (TB,V_includeDebugInfo) includeDebugInfo;
@property (TB,V_addUniqueIdToMLIRLocations) addUniqueIdToMLIRLocations;
@property (TQ,V_aneProfilingMask) aneProfilingMask;
@property (T@"NSDictionary",&,N,V_perDeviceDescriptorCompilationOptions) perDeviceDescriptorCompilationOptions;
```

## Instance methods

```
-[MPSGraphExecutableDescriptor init];
-[MPSGraphExecutableDescriptor compilerOptions];
-[MPSGraphExecutableDescriptor compilationDescriptor];
-[MPSGraphExecutableDescriptor setCompilationDescriptor:];
-[MPSGraphExecutableDescriptor setCompilerOptions:];
-[MPSGraphExecutableDescriptor includeDebugInfo];
-[MPSGraphExecutableDescriptor setIncludeDebugInfo:];
-[MPSGraphExecutableDescriptor addUniqueIdToMLIRLocations];
-[MPSGraphExecutableDescriptor aneProfilingMask];
-[MPSGraphExecutableDescriptor isAICodeBytecode];
-[MPSGraphExecutableDescriptor perDeviceDescriptorCompilationOptions];
-[MPSGraphExecutableDescriptor setAddUniqueIdToMLIRLocations:];
-[MPSGraphExecutableDescriptor setAneProfilingMask:];
-[MPSGraphExecutableDescriptor setIsAICodeBytecode:];
-[MPSGraphExecutableDescriptor setPerDeviceDescriptorCompilationOptions:];
-[MPSGraphExecutableDescriptor setVariableFetchHandler:];
-[MPSGraphExecutableDescriptor variableFetchHandler];
```
