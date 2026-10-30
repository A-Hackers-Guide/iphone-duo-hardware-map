# `_ANEVirtualClient`

- Image: [`/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine`](../userland/System__Library__PrivateFrameworks__AppleNeuralEngine.framework__AppleNeuralEngine.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 2 properties, 85 instance methods, 32 class methods

## Instance variables

```
{unordered_map<unsigned long long, MutableWeightsBufferEntry, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<std::pair<const unsigned long long, MutableWeightsBufferEntry>>>="__table_"{__hash_table<std::__hash_value_type<unsigned long long, MutableWeightsBufferEntry>, std::__unordered_map_hasher<unsigned long long, std::pair<const unsigned long long, MutableWeightsBufferEntry>, std::hash<unsigned long long>, std::equal_to<unsigned long long>>, std::__unordered_map_equal<unsigned long long, std::pair<const unsigned long long, MutableWeightsBufferEntry>, std::equal_to<unsigned long long>, std::hash<unsigned long long>>, std::allocator<std::pair<const unsigned long long, MutableWeightsBufferEntry>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, MutableWeightsBufferEntry>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, MutableWeightsBufferEntry>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, MutableWeightsBufferEntry>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, MutableWeightsBufferEntry>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _mutableWeightsBufferMap;
I _connect;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Properties

```
@property (TI,R,N,V_connect) connect;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_queue) queue;
```

## Class methods

```
+[_ANEVirtualClient deserializeHostErrorFromData:];
+[_ANEVirtualClient dictionaryGetUInt32ForKey:key:];
+[_ANEVirtualClient updateError:errorLength:error:];
+[_ANEVirtualClient sharedConnection];
+[_ANEVirtualClient createCFDictionaryFromIOSurface:dataLength:];
+[_ANEVirtualClient getCodeSigningIdentity];
+[_ANEVirtualClient populateNSString:toBuffer:maxLength:];
+[_ANEVirtualClient dictionaryGetUInt64ForKey:key:];
+[_ANEVirtualClient createIOSurface:ioSID:];
+[_ANEVirtualClient copyData:toExistingIOSurfaceRef:];
+[_ANEVirtualClient printStruct:];
+[_ANEVirtualClient new];
+[_ANEVirtualClient getPatternsForModelType:];
+[_ANEVirtualClient updatePerformanceStats:performanceStatsLength:perfStatsRawIOSurfaceRef:performanceStatsRawLength:hwExecutionTime:];
+[_ANEVirtualClient dictionaryGetNSStringForKey:key:];
+[_ANEVirtualClient assetTransferLockForUUID:];
+[_ANEVirtualClient copyDictionaryDataToStruct:dictionary:];
+[_ANEVirtualClient printIOSurfaceDataInBytes:];
+[_ANEVirtualClient findMatchingAssetPaths:inDirectory:];
+[_ANEVirtualClient setCodeSigningIdentity:];
+[_ANEVirtualClient dictionaryGetInt64ForKey:key:];
+[_ANEVirtualClient populateUUID:maxLength:fromString:];
+[_ANEVirtualClient copyLLIRBundleToIOSurface:writtenDataSize:];
+[_ANEVirtualClient extractMpsConstantsIOSurfaceIDs:ioSIDArray:keysArray:];
+[_ANEVirtualClient getObjectFromIOSurface:classType:length:];
+[_ANEVirtualClient dictionaryGetInt8ForKey:key:];
+[_ANEVirtualClient shouldUsePrecompiledPath:options:shouldUseChunking:chunkingThreshold:];
+[_ANEVirtualClient getDictionaryWithJSONEncodingFromIOSurface:withArchivedDataSize:];
+[_ANEVirtualClient populateCSIdentity:maxLength:];
+[_ANEVirtualClient updateError:errorLength:errorCode:error:];
+[_ANEVirtualClient findPathsMatchingPattern:inDirectory:];
+[_ANEVirtualClient doesPath:matchPattern:withFullPath:];
```

## Instance methods

```
-[_ANEVirtualClient connect];
-[_ANEVirtualClient transferAssetsToHostAtPathUnlocked:withUUID:modelType:];
-[_ANEVirtualClient isInternalBuild];
-[_ANEVirtualClient compileModel:options:qos:error:];
-[_ANEVirtualClient hostBuildVersionStr];
-[_ANEVirtualClient transferFileToHostWithPath:withUUID:withModelInputPath:overWriteFileNameWith:withExistingIOSurface:];
-[_ANEVirtualClient callIOUserClient:inParams:outParams:];
-[_ANEVirtualClient transferAssetsToHostAtPath:withUUID:modelType:];
-[_ANEVirtualClient aneBoardtype];
-[_ANEVirtualClient exchangeBuildVersionInfo];
-[_ANEVirtualClient copyDictionaryToIOSurface:copiedDataSize:createdIOSID:];
-[_ANEVirtualClient createIOSurfaceWithData:size:ioSID:];
-[_ANEVirtualClient init];
-[_ANEVirtualClient hasANE];
-[_ANEVirtualClient createIOSurfaceWithData:length:ioSID:];
-[_ANEVirtualClient readWeightFilename:];
-[_ANEVirtualClient transferFileToHostWithPath:withChunkSize:withUUID:withModelInputPath:overWriteFileNameWith:];
-[_ANEVirtualClient outputDictIOSurfaceSize];
-[_ANEVirtualClient initWithSingletonAccess];
-[_ANEVirtualClient validateEnvironmentForPrecompiledBinarySupport];
-[_ANEVirtualClient compileModelLegacy:options:qos:error:];
-[_ANEVirtualClient dealloc];
-[_ANEVirtualClient transferFileToHostWithPath:withChunkSize:withUUID:overWriteFileNameWith:];
-[_ANEVirtualClient updateError:error:];
-[_ANEVirtualClient purgeCompiledModelLegacy:];
-[_ANEVirtualClient copyOptions:dictionary:vmData:];
-[_ANEVirtualClient copyModelOptionFiles:options:dictionary:vmData:];
-[_ANEVirtualClient beginRealTimeTask];
-[_ANEVirtualClient callIOUserClientWithDictionary:inDictionary:error:];
-[_ANEVirtualClient queue];
-[_ANEVirtualClient mapIOSurfacesWithModel:request:cacheInference:error:];
-[_ANEVirtualClient loadModel:options:qos:error:];
-[_ANEVirtualClient unloadModel:options:qos:error:];
-[_ANEVirtualClient doEvaluateWithModel:options:request:qos:completionEvent:error:];
-[_ANEVirtualClient aneSubTypeAndVariant];
-[_ANEVirtualClient aneArchitectureTypeStr];
-[_ANEVirtualClient numANECores];
-[_ANEVirtualClient doEvaluateWithModelLegacy:options:request:qos:completionEvent:error:];
-[_ANEVirtualClient endRealTimeTask];
-[_ANEVirtualClient sessionHintWithModel:hint:options:report:error:];
-[_ANEVirtualClient negotiatedDataInterfaceVersion];
-[_ANEVirtualClient copyModelMetaData:options:dictionary:vmData:];
-[_ANEVirtualClient copyModelAttributesToDictionary:dictionary:vmData:];
-[_ANEVirtualClient getDeviceInfo];
-[_ANEVirtualClient updatePerformanceStats:];
-[_ANEVirtualClient releaseIOSurfaces:];
-[_ANEVirtualClient negotiatedCapabilityMask];
-[_ANEVirtualClient compiledModelExistsFor:];
-[_ANEVirtualClient doMapMutableWeightsForModel:andProcedure:mappedWeightsBuffer:size:error:];
-[_ANEVirtualClient loadModelNewInstanceLegacy:options:modelInstParams:qos:error:];
-[_ANEVirtualClient mapMutableWeightsForModel:andProcedure:mappedWeightsBuffer:size:error:];
-[_ANEVirtualClient printDictionary:];
-[_ANEVirtualClient loadModelLegacy:options:qos:error:];
-[_ANEVirtualClient sendGuestBuildVersion];
-[_ANEVirtualClient doUnmapMutableWeightsForModel:andProcedure:];
-[_ANEVirtualClient copyFilesInDirectoryToIOSurfaces:ioSurfaceRefs:ioSurfaceSizes:fileNames:];
-[_ANEVirtualClient copyOptions:vmData:];
-[_ANEVirtualClient doSyncMutableWeightsForModel:andProcedure:fromOffset:withSize:error:];
-[_ANEVirtualClient assetExistsOnHost:];
-[_ANEVirtualClient copyAllModelFiles:dictionary:ioSurfaceRefs:];
-[_ANEVirtualClient unmapMutableWeightsForModel:andProcedure:];
-[_ANEVirtualClient numANEs];
-[_ANEVirtualClient syncMutableWeightsForModel:andProcedure:fromOffset:withSize:error:];
-[_ANEVirtualClient copyErrorValue:];
-[_ANEVirtualClient purgeCompiledModelMatchingHash:];
-[_ANEVirtualClient copyErrorValue:vmData:];
-[_ANEVirtualClient transferFileToHostWithPath:withUUID:withModelInputPath:overWriteFileNameWith:chunkSizeBytes:withExistingIOSurface:];
-[_ANEVirtualClient compiledModelExistsMatchingHash:];
-[_ANEVirtualClient copyModelOptionFiles:options:vmData:];
-[_ANEVirtualClient checkKernReturnValue:selector:outParams:];
-[_ANEVirtualClient evaluateWithModel:options:request:qos:error:];
-[_ANEVirtualClient getValidateNetworkVersion];
-[_ANEVirtualClient doJsonParsingMatchWeightName:];
-[_ANEVirtualClient parallelDecompressedData:];
-[_ANEVirtualClient doMapIOSurfacesWithModel:request:cacheInference:error:];
-[_ANEVirtualClient purgeCompiledModel:];
-[_ANEVirtualClient getModelAttribute:];
-[_ANEVirtualClient createValidationResultForNetworkCreateMLIR:validation_params:];
-[_ANEVirtualClient validateNetworkCreate:uuid:function:directoryPath:scratchPadPath:milTextData:];
-[_ANEVirtualClient copyModelMetaData:options:dictionary:vmData:shouldEncodeKey:];
-[_ANEVirtualClient compiledModelExistsForLegacy:];
-[_ANEVirtualClient transferDirectoryMetaDataToHost:withUUID:];
-[_ANEVirtualClient echo:];
-[_ANEVirtualClient loadModelNewInstance:options:modelInstParams:qos:error:];
-[_ANEVirtualClient copyModel:options:vmData:];
```
