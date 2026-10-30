# `_ANEVirtualPlatformClient`

- Image: [`/System/Library/PrivateFrameworks/ParavirtualizedANE.framework/ParavirtualizedANE`](../userland/System__Library__PrivateFrameworks__ParavirtualizedANE.framework__ParavirtualizedANE.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 9 properties, 112 instance methods, 21 class methods

## Instance variables

```
B _avpSaveRestoreSupported;
I _negotiatedDataInterfaceVersion;
@"NSMutableDictionary" _aneModelDict;
@"_ANEClient" _aneClient;
@"NSString" _anebaseDirectory;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSString" _guestBuildVersion;
Q _negotiatedCapabilityMask;
@"NSMutableDictionary" _assetsOnDiskUUIDToDirMap;
```

## Properties

```
@property (T@"NSMutableDictionary",R,N,V_aneModelDict) aneModelDict;
@property (T@"_ANEClient",R,N,V_aneClient) aneClient;
@property (T@"NSString",R,N,V_anebaseDirectory) anebaseDirectory;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_queue) queue;
@property (T@"NSString",&,N,V_guestBuildVersion) guestBuildVersion;
@property (TI,N,V_negotiatedDataInterfaceVersion) negotiatedDataInterfaceVersion;
@property (TQ,N,V_negotiatedCapabilityMask) negotiatedCapabilityMask;
@property (TB,N,V_avpSaveRestoreSupported) avpSaveRestoreSupported;
@property (T@"NSMutableDictionary",&,N,V_assetsOnDiskUUIDToDirMap) assetsOnDiskUUIDToDirMap;
```

## Class methods

```
+[_ANEVirtualPlatformClient sharedConnection];
+[_ANEVirtualPlatformClient initialize];
+[_ANEVirtualPlatformClient dictionaryGetUInt64ForKey:key:];
+[_ANEVirtualPlatformClient printStruct:];
+[_ANEVirtualPlatformClient new];
+[_ANEVirtualPlatformClient dictionaryGetInt8ForKey:key:];
+[_ANEVirtualPlatformClient createAssetsOnDiskFromDataBuffer:withDataSize:atDestDirectory:];
+[_ANEVirtualPlatformClient createLastModificationTimeStampFile:fileName:timeSince1970:];
+[_ANEVirtualPlatformClient dictionaryGetDataBytesForKey:key:];
+[_ANEVirtualPlatformClient generateExpectedBaseDirectoryWith:withCSIdentity:withVMID:fileSubDirectory:];
+[_ANEVirtualPlatformClient generateExpectedPathForFileName:withANEBaseDirectory:withCSIdentity:withVMID:fileSubDirectory:];
+[_ANEVirtualPlatformClient getCodeSigningIdentity:];
+[_ANEVirtualPlatformClient getCommandInputSize:];
+[_ANEVirtualPlatformClient getCommandOutputSize:];
+[_ANEVirtualPlatformClient getDataFromIOSurface:withSize:];
+[_ANEVirtualPlatformClient getPrecompiledModelPath:error:];
+[_ANEVirtualPlatformClient isFileModificationTimeStampSame:timeSince1970:];
+[_ANEVirtualPlatformClient isValidBufferSize:];
+[_ANEVirtualPlatformClient needToSaveFile:fileName:timeSince1970:];
+[_ANEVirtualPlatformClient prepareValidationResultForSerialization:];
+[_ANEVirtualPlatformClient sharedConnection:];
```

## Instance methods

```
-[_ANEVirtualPlatformClient dealloc];
-[_ANEVirtualPlatformClient queue];
-[_ANEVirtualPlatformClient negotiatedDataInterfaceVersion];
-[_ANEVirtualPlatformClient negotiatedCapabilityMask];
-[_ANEVirtualPlatformClient compiledModelExistsFor:];
-[_ANEVirtualPlatformClient printDictionary:];
-[_ANEVirtualPlatformClient init:];
-[_ANEVirtualPlatformClient printIOSurfaceDataInBytes:];
-[_ANEVirtualPlatformClient purgeCompiledModelMatchingHash:];
-[_ANEVirtualPlatformClient compiledModelExistsMatchingHash:];
-[_ANEVirtualPlatformClient purgeCompiledModel:];
-[_ANEVirtualPlatformClient echo:];
-[_ANEVirtualPlatformClient loadModel:];
-[_ANEVirtualPlatformClient getDeviceInfo:];
-[_ANEVirtualPlatformClient evaluateWithModel:];
-[_ANEVirtualPlatformClient echoDictionary:];
-[_ANEVirtualPlatformClient generateExpectedModelFilePathFromDictionary:withFileType:error:];
-[_ANEVirtualPlatformClient generatedExpectedBaseDirectoryWithFileType:withInputDictionary:];
-[_ANEVirtualPlatformClient aneClient];
-[_ANEVirtualPlatformClient aneModelDict];
-[_ANEVirtualPlatformClient anebaseDirectory];
-[_ANEVirtualPlatformClient assetExistsForModel:];
-[_ANEVirtualPlatformClient assetReceivedFromGuest:];
-[_ANEVirtualPlatformClient assetsOnDiskUUIDToDirMap];
-[_ANEVirtualPlatformClient asyncAvpHoldMessageReceived:];
-[_ANEVirtualPlatformClient avpSaveRestoreSupported];
-[_ANEVirtualPlatformClient beginRealTimeTask:];
-[_ANEVirtualPlatformClient callCFDictionaryMethod:];
-[_ANEVirtualPlatformClient compileModel:];
-[_ANEVirtualPlatformClient compileModelFromDictionary:];
-[_ANEVirtualPlatformClient compileModelFromDictionary_v246:];
-[_ANEVirtualPlatformClient compiledModelExistsForDictionary:];
-[_ANEVirtualPlatformClient compiledModelExistsForDictionary_v246:];
-[_ANEVirtualPlatformClient compiledModelExistsMatchingHashDictionary:];
-[_ANEVirtualPlatformClient constructANEModel:modelDirectory:];
-[_ANEVirtualPlatformClient copyBytesToIOSurface:dataLength:ioSID:];
-[_ANEVirtualPlatformClient copyData:toIOSurfaceWithID:];
-[_ANEVirtualPlatformClient copyDictionaryUsingJSONSerialization:toIOSurfaceWithID:withMaxSize:outWrittentDataSize:];
-[_ANEVirtualPlatformClient createANEModelInstanceParameters:modelUUID:];
-[_ANEVirtualPlatformClient createAllModelFilesOnHost:];
-[_ANEVirtualPlatformClient createAssetOnHost:dataSize:dataIOSID:filePathComplete:directoryPath:];
-[_ANEVirtualPlatformClient createLLIRBundleOnDiskFromIOSurfaceWithID:destDirectory:llirDataSize:];
-[_ANEVirtualPlatformClient createModelFile:path:ioSID:length:];
-[_ANEVirtualPlatformClient createModelFileAtPath:fromIOSID:withDataLength:shouldAppend:];
-[_ANEVirtualPlatformClient createOptionFilesForCompilation:aneModelKey:options:];
-[_ANEVirtualPlatformClient createOptionFilesForCompilationDictionary:aneModelKey:options:modelDirectory:];
-[_ANEVirtualPlatformClient createValidationResultForNetworkCreateMLIR:];
-[_ANEVirtualPlatformClient doCreateModelFile:aneModelKey:];
-[_ANEVirtualPlatformClient doModelAttributeUpdate:virtualANEModel:];
-[_ANEVirtualPlatformClient doModelAttributeUpdateDictionary:dictionary:];
-[_ANEVirtualPlatformClient doRemoveModelFile:];
-[_ANEVirtualPlatformClient endRealTimeTask:];
-[_ANEVirtualPlatformClient ensureBaseKeeperClientForBaseModelIdentifier:];
-[_ANEVirtualPlatformClient evaluateWithModelDictionary:];
-[_ANEVirtualPlatformClient exchangeBuildVersionInfo:];
-[_ANEVirtualPlatformClient generateExpectedBaseDirectoryFromModel:withCSIdentity:withAssetTransferUUID:];
-[_ANEVirtualPlatformClient generateExpectedModelFilePathFromDictionary:error:];
-[_ANEVirtualPlatformClient generateExpectedPathForFileName:withFileType:withInputDictionary:];
-[_ANEVirtualPlatformClient getANEModelKey:caller:];
-[_ANEVirtualPlatformClient getArrayFromIOSurfaceID:localData:localDataLength:];
-[_ANEVirtualPlatformClient getBytesFromIOSurfaceID:dest:dataLength:];
-[_ANEVirtualPlatformClient getDeviceInfoDictionary:];
-[_ANEVirtualPlatformClient getIOSurface:];
-[_ANEVirtualPlatformClient getObjectFromIOSurfaceID:classType:length:];
-[_ANEVirtualPlatformClient getObjectFromIOSurfaceID:classes:topLevelClass:length:];
-[_ANEVirtualPlatformClient getOptionsDictFromInputDict:];
-[_ANEVirtualPlatformClient getQueueCount];
-[_ANEVirtualPlatformClient guestBuildVersion];
-[_ANEVirtualPlatformClient loadModelFromDictionary:];
-[_ANEVirtualPlatformClient loadModelFromDictionary_v246:];
-[_ANEVirtualPlatformClient loadModelNewInstance:];
-[_ANEVirtualPlatformClient loadModelNewInstanceLegacy:];
-[_ANEVirtualPlatformClient mapIOSurfacesWithModel:];
-[_ANEVirtualPlatformClient mapIOSurfacesWithModelDictionary:ioSIDs:ioSIDsSize:];
-[_ANEVirtualPlatformClient mapMutableWeights:];
-[_ANEVirtualPlatformClient modelAction:buffer:bufferSize:];
-[_ANEVirtualPlatformClient objectWithIOSurfaceID:];
-[_ANEVirtualPlatformClient performMapMutableWeights:];
-[_ANEVirtualPlatformClient performSyncMutableWeights:];
-[_ANEVirtualPlatformClient performUnmapMutableWeights:];
-[_ANEVirtualPlatformClient purgeCompiledModelFromDictionary:];
-[_ANEVirtualPlatformClient purgeCompiledModelFromDictionary_v246:];
-[_ANEVirtualPlatformClient purgeCompiledModelMatchingHashDictionary:];
-[_ANEVirtualPlatformClient removeAllModelFiles:];
-[_ANEVirtualPlatformClient requestWithVirtualANEModel:];
-[_ANEVirtualPlatformClient requestWithVirtualANEModelDictionary:];
-[_ANEVirtualPlatformClient sessionHintWithModel:];
-[_ANEVirtualPlatformClient setAssetsOnDiskUUIDToDirMap:];
-[_ANEVirtualPlatformClient setAvpSaveRestoreSupported:];
-[_ANEVirtualPlatformClient setGuestBuildVersion:];
-[_ANEVirtualPlatformClient setNegotiatedCapabilityMask:];
-[_ANEVirtualPlatformClient setNegotiatedDataInterfaceVersion:];
-[_ANEVirtualPlatformClient storeGuestBuildVersion:];
-[_ANEVirtualPlatformClient syncMutableWeights:];
-[_ANEVirtualPlatformClient teardownFailedInstanceForVirtualModel:programHandle:];
-[_ANEVirtualPlatformClient unLoadModel:];
-[_ANEVirtualPlatformClient unLoadModelDictionary:];
-[_ANEVirtualPlatformClient unmapAllMutableWeightsForVirtualModel:];
-[_ANEVirtualPlatformClient unmapMutableWeights:];
-[_ANEVirtualPlatformClient updateErrorValue:error:];
-[_ANEVirtualPlatformClient updateErrorValueDictionary:error:];
-[_ANEVirtualPlatformClient updateErrorValueForIOSID:error:dictToUpdate:maxIOSurfaceSize:];
-[_ANEVirtualPlatformClient updateMpsConstantsIOSurfaceRefs:fromDictionary:];
-[_ANEVirtualPlatformClient updateOptions:virtualANEModel:];
-[_ANEVirtualPlatformClient updateOptionsDictionary:directoryPath:];
-[_ANEVirtualPlatformClient updatePerformanceStats:aneRequest:];
-[_ANEVirtualPlatformClient updatePerformanceStatsDictionary:aneRequest:];
-[_ANEVirtualPlatformClient updateVirtualANEModel:model:];
-[_ANEVirtualPlatformClient updateVirtualANEModelDictionary:model:cacheURLIdentifierToGuest:];
-[_ANEVirtualPlatformClient validateNetworkCreate:];
-[_ANEVirtualPlatformClient writeDictionaryToIOSurfaceID:dict:writtenDataLength:ioSurfaceMaxSize:];
-[_ANEVirtualPlatformClient writeObjectToIOSurfaceID:obj:writtenDataLength:ioSurfaceMaxSize:];
```
