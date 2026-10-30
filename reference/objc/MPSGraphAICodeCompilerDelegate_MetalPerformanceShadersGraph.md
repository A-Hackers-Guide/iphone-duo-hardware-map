# `MPSGraphAICodeCompilerDelegate`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- 9 instance variables, 0 properties, 17 instance methods, 1 class methods

## Instance variables

```
@"NSData" _aiCodeBytecode;
@"NSURL" _aiCodeDirectory;
@"NSString" _mpsgraphPackageName;
@"NSString" _delegateId;
@"MPSGraphDelegatePrecompilationDescriptor" _precompilationDescriptor;
@"MPSGraphDelegateCompilationContext" _compilationContext;
@"NSURL" _intermediateResultDirectory;
@"NSObject<OS_os_log>" _delegateLog;
@? _resourceLookupBlock;
```

## Class methods

```
+[MPSGraphAICodeCompilerDelegate targetSpecOptionsHelpMessage];
```

## Instance methods

```
-[MPSGraphAICodeCompilerDelegate compilationDescriptorWithTargetOptions:];
-[MPSGraphAICodeCompilerDelegate getBytecodeWithDelegateCalls:originalModule:];
-[MPSGraphAICodeCompilerDelegate getFallbackModuleBytecode:vizModule:];
-[MPSGraphAICodeCompilerDelegate getGraphExecutableFromBytecodeReleasingSource:aiCodeModule:sourceCtx:execDescriptor:];
-[MPSGraphAICodeCompilerDelegate getInitializedAICodeBytecode];
-[MPSGraphAICodeCompilerDelegate getInitializedAICodeBytecodeWithPayloadPrefix:delegateId:];
-[MPSGraphAICodeCompilerDelegate getModuleBytecodeFromIRDump:mlirContext:];
-[MPSGraphAICodeCompilerDelegate getModuleBytecodeFromVizSymbols:];
-[MPSGraphAICodeCompilerDelegate getMpsgraphPackageName];
-[MPSGraphAICodeCompilerDelegate getSegmentedAICodeBytecode];
-[MPSGraphAICodeCompilerDelegate getSegmentedAICodeBytecodeWithDelegateId:];
-[MPSGraphAICodeCompilerDelegate initWithAICodeBytecode:aiCodeDirectory:];
-[MPSGraphAICodeCompilerDelegate initWithAICodeBytecode:aiCodeDirectory:precompilationDescriptor:];
-[MPSGraphAICodeCompilerDelegate initWithAICodeBytecode:aiCodeDirectory:precompilationDescriptor:compilationContext:];
-[MPSGraphAICodeCompilerDelegate initWithAICodeBytecode:aiCodeDirectory:precompilationDescriptor:compilationContext:intermediateResultDirectory:];
-[MPSGraphAICodeCompilerDelegate initWithAICodeBytecode:aiCodeDirectory:precompilationDescriptor:compilationContext:intermediateResultDirectory:resourceLookupBlock:];
-[MPSGraphAICodeCompilerDelegate readTargetSpecAttribute:];
```
