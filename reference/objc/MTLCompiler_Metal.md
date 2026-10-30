# `MTLCompiler`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 5 properties, 110 instance methods, 0 class methods

## Instance variables

```
@"_MTLDevice" _device;
@"NSString" _pluginPath;
@"NSObject<OS_dispatch_queue>" _compilerQueue;
^v _compilerConnectionManager;
I _compilerId;
Q _compilerFlags;
{shared_ptr<MTLCompilerCache>="__ptr_"^{MTLCompilerCache}"__cntrl_"^{__shared_weak_count}} _shaderCache;
```

## Properties

```
@property (T@"NSString",R,C,V_pluginPath) pluginPath;
@property (T@"NSObject<OS_dispatch_queue>",R,V_compilerQueue) compilerQueue;
@property (T^v,R,V_compilerConnectionManager) compilerConnectionManager;
@property (TI,R,V_compilerId) compilerId;
@property (TQ,R,V_compilerFlags) compilerFlags;
```

## Instance methods

```
-[MTLCompiler pipelineCacheStats];
-[MTLCompiler unloadShaderCaches];
-[MTLCompiler getShaderCacheKeys];
-[MTLCompiler copyShaderCacheToPath:];
-[MTLCompiler libraryCacheStats];
-[MTLCompiler allowLibrariesFromOtherPlatforms];
-[MTLCompiler initializeVendorPluginFunctionId:airScript:driverCompilerOptions:compiledNextStageVariant:vendorPlugin:];
-[MTLCompiler hashKeyForStatelessCompilationRequest:];
-[MTLCompiler addRenderPipelineStateWithDescriptor:destinationBinaryArchive:options:error:];
-[MTLCompiler compilerConnectionManager];
-[MTLCompiler getProgramObject:destinationArchive:sourceBinaryArchives:variantKey:requiredKeys:failOnMiss:];
-[MTLCompiler getDataForScript:device:function:functionType:compilerOptions:compilerOptionsSize:compiledNextStageVariant:dataSize:];
-[MTLCompiler compileBuiltinRequest:completionHandler:];
-[MTLCompiler compilerQueue];
-[MTLCompiler reflectionWithFunction:options:sync:pipelineLibrary:completionHandler:];
-[MTLCompiler compilerFlags];
-[MTLCompiler newRenderPipelineStateWithTileDescriptorInternal:options:reflection:destinationBinaryArchive:error:compilerTask:completionHandler:];
-[MTLCompiler tileVariantEntryWithDescriptor:airDescriptor:options:serializedTileDataDescriptor:asyncCompile:destinationBinaryArchive:tileProgram:kernelDriverCompileTimeData:compileTimeStatistics:compilerTask:];
-[MTLCompiler addFunctionKeys:function:driverData:frameworkData:compilerOptions:];
-[MTLCompiler newRenderPipelineStateWithDescriptorInternal:options:reflection:destinationBinaryArchive:error:compilerTask:completionHandler:];
-[MTLCompiler statelessBackendCompileRequestInternal:sync:compilerHash:reflectionOnly:completionHandler:];
-[MTLCompiler reflectionWithFunction:options:compilerTask:completionHandler:];
-[MTLCompiler createMeshStageAndLinkPipelineWithFragment:fragmentVariant:objectFunction:serializedObjectDescriptor:meshFunction:serializedMeshDescriptor:descriptor:airDescriptor:destinationArchive:options:reflection:compileStatistics:fragmentCompileTimeData:pipelineArchiverId:error:compilerTask:completionHandler:];
-[MTLCompiler initWithTargetData:cacheUUID:pluginPath:device:compilerFlags:fallbackDeviceFeatureProfile:];
-[MTLCompiler pluginPath];
-[MTLCompiler statelessBackendCompileRequestInternal:sync:compilerHash:reflectionOnly:compilerTask:completionHandler:];
-[MTLCompiler releaseCompilerOutputBlocks:];
-[MTLCompiler compileRequest:compilerTask:completionHandler:];
-[MTLCompiler hashKeyForLibraryRequest:];
-[MTLCompiler createErrorMessageWithRequest:key:cacheType:itemLookedFor:];
-[MTLCompiler getBuiltInFunctionId:];
-[MTLCompiler dealloc];
-[MTLCompiler cacheLegacyCompilerData:cachedData:hashMap:libraryData:functionCache:];
-[MTLCompiler compileRequest:binaryArchives:failOnBinaryArchiveMiss:pipelineCache:sync:completionHandler:];
-[MTLCompiler newRenderPipelineStateWithTileDescriptor:options:reflection:error:completionHandler:];
-[MTLCompiler compileFunctionRequest:compilerTask:completionHandler:];
-[MTLCompiler reflectionWithFunction:options:sync:pipelineLibrary:binaryArchives:completionHandler:];
-[MTLCompiler compileDynamicLibraryWithDescriptor:computePipelineDescriptor:completionHandler:];
-[MTLCompiler reflectionWithFunction:options:sync:binaryArchives:completionHandler:];
-[MTLCompiler pipelineStateWithVariant:descriptor:options:computeProgram:kernelDriverCompileTimeData:serializedComputeDataDescriptor:compileTimeStatistics:reflection:error:completionHandler:];
-[MTLCompiler validateLanguageAndAIRVersionForFunction:completionHandler:];
-[MTLCompiler compileFunction:serializedData:stateData:options:compilerTask:completionHandler:];
-[MTLCompiler compileBuiltinRequest:compilerTask:completionHandler:];
-[MTLCompiler computeVariantEntryWithDescriptor:airDescriptor:options:serializedComputeDataDescriptor:asyncCompile:pipelineCache:destinationBinaryArchive:computeProgram:kernelDriverCompileTimeData:compileTimeStatistics:compilerTask:];
-[MTLCompiler downgradeFunctionRequest:targetLLVMVersion:frameworkData:compilerTask:error:];
-[MTLCompiler compileFunction:visibleFunctions:visibleFunctionGroups:frameworkData:driverKeyData:options:pipelineCache:sync:completionHandler:];
-[MTLCompiler compileStatelessFunctionRequest:reflectionOnly:compilerTask:completionHandler:];
-[MTLCompiler compileRequest:pipelineCache:sync:compilerTask:completionHandler:];
-[MTLCompiler addTileRenderPipelineStateWithDescriptor:destinationBinaryArchive:options:error:];
-[MTLCompiler initWithTargetData:cacheUUID:pluginPath:device:compilerFlags:];
-[MTLCompiler releaseCompilerOutputBlocks:hashMap:];
-[MTLCompiler addLegacyCompiledOutput:cachedCompiledOutput:importedSymbols:importedLibraries:hashKey:type:functionCache:];
-[MTLCompiler compilerId];
-[MTLCompiler compileRequest:completionHandler:];
-[MTLCompiler compileRequest:binaryArchives:failOnBinaryArchiveMiss:pipelineCache:sync:compilerTask:completionHandler:];
-[MTLCompiler compileRequestInternal:binaryArchives:failOnBinaryArchiveMiss:pipelineCache:sync:completionHandler:];
-[MTLCompiler createBinaryArchiveAsRecompileTarget:completionHandler:];
-[MTLCompiler createBinaryArchiveAsRecompileTarget:compilerTask:completionHandler:];
-[MTLCompiler addLegacyCompiledOutput:importedSymbols:importedLibraries:hashKey:type:functionCache:];
-[MTLCompiler getFunctionId:];
-[MTLCompiler getFunctionKeyWithRenderPipelineDescriptor:options:unfilteredOptions:airScript:function:functionType:compiledNextStageVariant:keySize:];
-[MTLCompiler getFunctionId:airScript:vendorPluginFunctionId:bitcodeHashList:];
-[MTLCompiler reflectionWithFunction:options:sync:pipelineLibrary:compilerTask:completionHandler:];
-[MTLCompiler compileDynamicLibraryWithDescriptor:computePipelineDescriptor:compilerTask:completionHandler:];
-[MTLCompiler renderPipelineStateWithTileVariant:descriptor:options:tileProgram:kernelDriverCompileTimeData:serializedTileDataDescriptor:compileTimeStatistics:reflection:error:compilerTask:completionHandler:];
-[MTLCompiler compileFunction:visibleFunctions:privateVisibleFunctions:visibleFunctionGroups:frameworkData:driverKeyData:options:pipelineCache:sync:completionHandler:];
-[MTLCompiler reflectionWithFunction:options:sync:binaryArchives:compilerTask:completionHandler:];
-[MTLCompiler compileBuiltinRequestInternal:compilerTask:completionHandler:];
-[MTLCompiler newComputePipelineStateWithDescriptorInternal:options:pipelineCache:destinationBinaryArchive:reflection:error:compilerTask:completionHandler:];
-[MTLCompiler compileFunction:frameworkData:driverKeyData:options:pipelineCache:sync:completionHandler:];
-[MTLCompiler compileRequest:binaryArchives:sync:compilerTask:completionHandler:];
-[MTLCompiler addComputePipelineStateWithDescriptor:destinationBinaryArchive:options:error:];
-[MTLCompiler compileFunction:serializedPipelineData:stateData:linkDataSize:frameworkLinking:options:pipelineCache:sync:compilerTask:completionHandler:];
-[MTLCompiler compileFunction:serializedPipelineData:stateData:linkDataSize:frameworkLinking:options:sync:completionHandler:];
-[MTLCompiler compileLibraryRequest:compilerTask:completionHandler:];
-[MTLCompiler newRenderPipelineStateWithDescriptorInternal:options:reflection:destinationBinaryArchive:error:completionHandler:];
-[MTLCompiler releaseHashMaps:];
-[MTLCompiler compileFunction:serializedData:stateData:options:completionHandler:];
-[MTLCompiler downgradeRequest:frameworkData:compilerTask:error:];
-[MTLCompiler compileStatelessFunctionRequest:reflectionOnly:completionHandler:];
-[MTLCompiler requiredKeysForFunction:variantKey:frameworkData:compilerOptions:driverCompilerOptions:airScript:archives:compiledNextStageVariant:];
-[MTLCompiler compileLibraryRequest:completionHandler:];
-[MTLCompiler reflectionWithFunction:options:sync:compilerTask:completionHandler:];
-[MTLCompiler reflectionWithFunction:options:sync:pipelineLibrary:binaryArchives:compilerTask:completionHandler:];
-[MTLCompiler compileFunctionRequest:completionHandler:];
-[MTLCompiler newRenderPipelineStateWithDescriptor:options:reflection:error:completionHandler:];
-[MTLCompiler createVertexStageAndLinkPipelineWithFragment:fragmentVariant:vertexFunction:serializedVertexDescriptor:descriptor:airDescriptor:destinationArchive:options:reflection:compileStatistics:fragmentCompileTimeData:pipelineArchiverId:error:completionHandler:];
-[MTLCompiler newComputePipelineStateWithDescriptor:options:reflection:error:completionHandler:];
-[MTLCompiler compileRequestInternal:binaryArchives:failOnBinaryArchiveMiss:pipelineCache:sync:compilerTask:completionHandler:];
-[MTLCompiler compileRequest:pipelineCache:compilerTask:completionHandler:];
-[MTLCompiler reflectionWithFunction:options:completionHandler:];
-[MTLCompiler compileRequest:pipelineCache:sync:completionHandler:];
-[MTLCompiler generateMachOWithID:binaryEntries:machOSpecializedData:machOType:Path:platform:bitcodeList:completionHandler:];
-[MTLCompiler createVertexStageAndLinkPipelineWithFragment:fragmentVariant:vertexFunction:serializedVertexDescriptor:descriptor:airDescriptor:destinationArchive:options:reflection:compileStatistics:fragmentCompileTimeData:pipelineArchiverId:error:compilerTask:completionHandler:];
-[MTLCompiler newLinkedFunctionsBitcodeFromRequest:hashKey:];
-[MTLCompiler getFunctionKeyWithRenderPipelineDescriptor:options:unfilteredOptions:airScript:function:functionType:compiledNextStageVariant:keySize:functionDriverData:functionDriverSize:];
-[MTLCompiler compileFunctionRequestInternal:frameworkLinking:linkDataSize:reflectionOnly:compilerTask:completionHandler:];
-[MTLCompiler compileFunction:frameworkData:driverKeyData:options:pipelineCache:completionHandler:];
-[MTLCompiler getProgramObjectForFunction:variantKey:requiredKeys:sourceBinaryArchives:];
-[MTLCompiler reflectionWithFunction:options:sync:completionHandler:];
-[MTLCompiler getHashForScript:device:function:functionType:compilerOptions:compilerOptionsSize:compiledNextStageVariant:];
-[MTLCompiler generateMachOWithID:binaryEntries:machOSpecializedData:machOType:Path:platform:bitcodeList:compilerTask:completionHandler:];
-[MTLCompiler compileDynamicLibraryWithDescriptor:computePipelineDescriptor:compilerTask:error:];
-[MTLCompiler getFunctionId:airScript:vendorPluginFunctionId:];
-[MTLCompiler compileDynamicLibraryWithDescriptor:computePipelineDescriptor:error:];
-[MTLCompiler compileRequest:binaryArchives:sync:completionHandler:];
-[MTLCompiler compileFunction:serializedPipelineData:stateData:linkDataSize:frameworkLinking:options:pipelineCache:sync:completionHandler:];
-[MTLCompiler initializeFunctionRequestScriptAndFunctionId:script:driverCompilerOptions:compiledNextStageVariant:];
-[MTLCompiler addMeshRenderPipelineStateWithDescriptor:destinationBinaryArchive:options:error:];
-[MTLCompiler compileRequest:pipelineCache:completionHandler:];
```
