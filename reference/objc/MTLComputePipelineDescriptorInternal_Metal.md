# `MTLComputePipelineDescriptorInternal`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLComputePipelineDescriptor`
- 1 instance variables, 0 properties, 89 instance methods, 0 class methods

## Instance variables

```
{MTLComputePipelineDescriptorPrivate="label"@"NSString""computeFunction"@"<MTLFunction>""threadGroupSizeIsMultipleOfThreadExecutionWidth"B"maxTotalThreadsPerThreadgroup"S"stageInputDescriptor"@"MTLStageInputOutputDescriptor""driverCompilerOptions"@"NSDictionary""gpuCompilerSPIOptions"@"NSDictionary""buffers"@"MTLPipelineBufferDescriptorArrayInternal""binaryArchives"@"NSArray"""(?="preloadedLibraries"@"NSArray""insertLibraries"@"NSArray")"pipelineLibrary"@"<MTLPipelineLibrary>""supportIndirectCommandBuffers"B"shaderValidation"q"shaderValidationState"q"textureWriteRoundingMode"q"forceResourceIndex"B"resourceIndex"Q"globalConstantsTag"Q"pluginData"@"NSDictionary""needsCustomBorderColorSamplers"B"openGLMode"b1"openCLMode"b1"internalPipeline"b1"reserved"b29"functionPointers"@"NSArray""linkedFunctions"@"MTLLinkedFunctions""maxStackCallDepth"Q"supportAddingBinaryFunctions"B"profileControl"@"MTLProfileControl""maxAccelerationStructureTraversalDepth"Q"requiredThreadsPerThreadgroup"{?="width"Q"height"Q"depth"Q}"name"@"NSString""forwardProgressUsage"q"contentionRelief"q"optimizeForPersistentKernel"B} _private;
```

## Instance methods

```
-[MTLComputePipelineDescriptorInternal openGLModeEnabled];
-[MTLComputePipelineDescriptorInternal supportIndirectCommandBuffers];
-[MTLComputePipelineDescriptorInternal pipelineLibrary];
-[MTLComputePipelineDescriptorInternal setProfileControl:];
-[MTLComputePipelineDescriptorInternal setOpenGLModeEnabled:];
-[MTLComputePipelineDescriptorInternal setResourceIndex:];
-[MTLComputePipelineDescriptorInternal resourceIndex];
-[MTLComputePipelineDescriptorInternal setForceResourceIndex:];
-[MTLComputePipelineDescriptorInternal setPluginData:];
-[MTLComputePipelineDescriptorInternal forceResourceIndex];
-[MTLComputePipelineDescriptorInternal setSupportIndirectCommandBuffers:];
-[MTLComputePipelineDescriptorInternal setPipelineLibrary:];
-[MTLComputePipelineDescriptorInternal binaryArchives];
-[MTLComputePipelineDescriptorInternal internalPipeline];
-[MTLComputePipelineDescriptorInternal gpuCompilerSPIOptions];
-[MTLComputePipelineDescriptorInternal supportAddingBinaryFunctions];
-[MTLComputePipelineDescriptorInternal needsCustomBorderColorSamplers];
-[MTLComputePipelineDescriptorInternal setShaderValidationState:];
-[MTLComputePipelineDescriptorInternal setRequiredThreadsPerThreadgroup:];
-[MTLComputePipelineDescriptorInternal pluginData];
-[MTLComputePipelineDescriptorInternal dynamicLibraries];
-[MTLComputePipelineDescriptorInternal setTextureWriteRoundingMode:];
-[MTLComputePipelineDescriptorInternal setDriverCompilerOptions:];
-[MTLComputePipelineDescriptorInternal formattedDescription:];
-[MTLComputePipelineDescriptorInternal validateWithDevice:error:];
-[MTLComputePipelineDescriptorInternal init];
-[MTLComputePipelineDescriptorInternal buffers];
-[MTLComputePipelineDescriptorInternal label];
-[MTLComputePipelineDescriptorInternal setLabel:];
-[MTLComputePipelineDescriptorInternal textureWriteFPRoundingMode];
-[MTLComputePipelineDescriptorInternal maxCallStackDepth];
-[MTLComputePipelineDescriptorInternal linkedFunctions];
-[MTLComputePipelineDescriptorInternal setMaxCallStackDepth:];
-[MTLComputePipelineDescriptorInternal dealloc];
-[MTLComputePipelineDescriptorInternal shaderValidation];
-[MTLComputePipelineDescriptorInternal setSupportAddingBinaryFunctions:];
-[MTLComputePipelineDescriptorInternal setGpuCompilerSPIOptions:];
-[MTLComputePipelineDescriptorInternal preloadedLibraries];
-[MTLComputePipelineDescriptorInternal reset];
-[MTLComputePipelineDescriptorInternal maxAccelerationStructureTraversalDepth];
-[MTLComputePipelineDescriptorInternal newPipelineScript];
-[MTLComputePipelineDescriptorInternal driverCompilerOptions];
-[MTLComputePipelineDescriptorInternal setBinaryLibraries:];
-[MTLComputePipelineDescriptorInternal setPreloadedLibraries:];
-[MTLComputePipelineDescriptorInternal openCLModeEnabled];
-[MTLComputePipelineDescriptorInternal setGlobalConstantsTag:];
-[MTLComputePipelineDescriptorInternal setInsertLibraries:];
-[MTLComputePipelineDescriptorInternal textureWriteRoundingMode];
-[MTLComputePipelineDescriptorInternal setTextureWriteFPRoundingMode:];
-[MTLComputePipelineDescriptorInternal profileControl];
-[MTLComputePipelineDescriptorInternal setDynamicLibraries:];
-[MTLComputePipelineDescriptorInternal _descriptorPrivate];
-[MTLComputePipelineDescriptorInternal setMaxTotalThreadsPerThreadgroup:];
-[MTLComputePipelineDescriptorInternal setOptimizeForPersistentKernel:];
-[MTLComputePipelineDescriptorInternal setBinaryArchives:];
-[MTLComputePipelineDescriptorInternal validateWithDevice:];
-[MTLComputePipelineDescriptorInternal setMaxAccelerationStructureTraversalDepth:];
-[MTLComputePipelineDescriptorInternal requiredThreadsPerThreadgroup];
-[MTLComputePipelineDescriptorInternal maxTotalThreadsPerThreadgroup];
-[MTLComputePipelineDescriptorInternal insertLibraries];
-[MTLComputePipelineDescriptorInternal setLinkedFunctions:];
-[MTLComputePipelineDescriptorInternal setContentionRelief:];
-[MTLComputePipelineDescriptorInternal shaderValidationState];
-[MTLComputePipelineDescriptorInternal setShaderValidation:];
-[MTLComputePipelineDescriptorInternal threadGroupSizeIsMultipleOfThreadExecutionWidth];
-[MTLComputePipelineDescriptorInternal setOpenCLModeEnabled:];
-[MTLComputePipelineDescriptorInternal setFunctionPointers:];
-[MTLComputePipelineDescriptorInternal setForwardProgressUsage:];
-[MTLComputePipelineDescriptorInternal hash];
-[MTLComputePipelineDescriptorInternal setNeedsCustomBorderColorSamplers:];
-[MTLComputePipelineDescriptorInternal description];
-[MTLComputePipelineDescriptorInternal contentionRelief];
-[MTLComputePipelineDescriptorInternal setName:];
-[MTLComputePipelineDescriptorInternal setInternalPipeline:];
-[MTLComputePipelineDescriptorInternal forwardProgressUsage];
-[MTLComputePipelineDescriptorInternal setThreadGroupSizeIsMultipleOfThreadExecutionWidth:];
-[MTLComputePipelineDescriptorInternal globalConstantsTag];
-[MTLComputePipelineDescriptorInternal setComputeFunction:];
-[MTLComputePipelineDescriptorInternal setStageInputDescriptor:];
-[MTLComputePipelineDescriptorInternal copyWithZone:];
-[MTLComputePipelineDescriptorInternal isEqual:];
-[MTLComputePipelineDescriptorInternal name];
-[MTLComputePipelineDescriptorInternal newSerializedComputeDataWithFlags:options:];
-[MTLComputePipelineDescriptorInternal binaryLibraries];
-[MTLComputePipelineDescriptorInternal optimizeForPersistentKernel];
-[MTLComputePipelineDescriptorInternal stageInputDescriptor];
-[MTLComputePipelineDescriptorInternal computeFunction];
-[MTLComputePipelineDescriptorInternal functionPointers];
-[MTLComputePipelineDescriptorInternal newSerializedComputeData];
```
