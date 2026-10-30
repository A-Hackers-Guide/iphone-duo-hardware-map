# `_MTLFunctionInternal`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLFunction`
- 11 instance variables, 0 properties, 68 instance methods, 0 class methods

## Instance variables

```
{MTLFunctionData="bitCodeOffset"Q"bitCodeFileSize"Q"publicArgumentsOffset"Q"privateArgumentsOffset"Q"sourceArchiveOffset"Q"reflectionDataOffset"Q"airMajorVersion"S"airMinorVersion"S"languageMajorVersion"S"languageMinorVersion"S"bitcodeHash"{?="key"[32C]}"bitcodeType"C"pluginData"@"NSData""renderTargetArrayIndexType"C"patchType"b2"controlPointCount"b6"functionInputs"@"NSObject<OS_dispatch_data>""baseFunctionData"{pair<MTLUINT256_t, std::optional<std::string>>="first"{?="key"[32C]}"second"{optional<std::string>=""(?="__null_state_"c"__val_"{basic_string<char, std::char_traits<char>, std::allocator<char>>=""{?="__rep_"(__rep="__s"{__short="__data_"[23c]"__size_"b7"__is_long_"b1}"__l"{__long="__data_"*"__size_"Q"__cap_"b63"__is_long_"b1})}})"__engaged_"B}}"airScript"@"NSObject<OS_dispatch_data>"} _functionData;
C _publicMetadataInitialized;
C _privateMetadataInitialized;
C _sourceArchiveMetadataInitialized;
C _stitchableFunctionMetadataInitialized;
^v _programObject;
@"NSString" _filePath;
q _lineNumber;
@"NSString" _inheritedLibraryPath;
@"NSObject<OS_dispatch_queue>" _functionQueue;
{shared_ptr<TrackingData>="__ptr_"^{TrackingData}"__cntrl_"^{__shared_weak_count}} _trackingData;
```

## Instance methods

```
-[_MTLFunctionInternal airScript];
-[_MTLFunctionInternal setPluginData:];
-[_MTLFunctionInternal setRelocations:];
-[_MTLFunctionInternal setPrecompiledOutput:];
-[_MTLFunctionInternal stageInputAttributes];
-[_MTLFunctionInternal arguments];
-[_MTLFunctionInternal renderTargetArrayIndexType];
-[_MTLFunctionInternal pluginData];
-[_MTLFunctionInternal requiredLLVMVersion];
-[_MTLFunctionInternal setOptions:];
-[_MTLFunctionInternal setVertexAttributes:];
-[_MTLFunctionInternal baseFunctionData];
-[_MTLFunctionInternal functionConstantsDictionary];
-[_MTLFunctionInternal importedLibraries];
-[_MTLFunctionInternal stitchedLibraryTrackingData];
-[_MTLFunctionInternal vertexAttributes];
-[_MTLFunctionInternal functionInputs];
-[_MTLFunctionInternal setReturnType:];
-[_MTLFunctionInternal dealloc];
-[_MTLFunctionInternal precompiledOutput];
-[_MTLFunctionInternal programObject];
-[_MTLFunctionInternal newSpecializedFunctionWithDescriptor:destinationArchive:functionCache:sync:completionHandler:];
-[_MTLFunctionInternal initializeStitchableFunctionMetadata];
-[_MTLFunctionInternal specializedFunctionHash:requestData:airScript:constants:specializedName:privateFunctions:completionHandler:];
-[_MTLFunctionInternal bitCodeFileSize];
-[_MTLFunctionInternal stripped];
-[_MTLFunctionInternal lineNumber];
-[_MTLFunctionInternal inheritedLibraryPath];
-[_MTLFunctionInternal initializePublicMetadata];
-[_MTLFunctionInternal initializePrivateMetadata];
-[_MTLFunctionInternal setArguments:];
-[_MTLFunctionInternal setTrackingData:];
-[_MTLFunctionInternal initWithName:type:libraryData:functionData:inheritedLibraryPath:device:];
-[_MTLFunctionInternal specializedFunctionTrackingData];
-[_MTLFunctionInternal setLineNumber:];
-[_MTLFunctionInternal setStageInputAttributes:];
-[_MTLFunctionInternal patchType];
-[_MTLFunctionInternal specializationAirScript];
-[_MTLFunctionInternal setFunctionConstants:];
-[_MTLFunctionInternal needsFunctionConstantValues];
-[_MTLFunctionInternal setSourceArchiveOffset:];
-[_MTLFunctionInternal newSpecializedFunctionWithDescriptor:destinationArchive:functionCache:error:];
-[_MTLFunctionInternal reflectionData];
-[_MTLFunctionInternal setUnpackedFilePath:];
-[_MTLFunctionInternal newSpecializedFunctionWithDescriptor:destinationArchive:functionCache:compilerTask:error:];
-[_MTLFunctionInternal sourceArchiveOffset];
-[_MTLFunctionInternal relocations];
-[_MTLFunctionInternal filePath];
-[_MTLFunctionInternal bitCodeOffset];
-[_MTLFunctionInternal storeTrackingDataWithDescriptor:function:variantHash:];
-[_MTLFunctionInternal bitcodeType];
-[_MTLFunctionInternal importedSymbols];
-[_MTLFunctionInternal functionData];
-[_MTLFunctionInternal bitCodeHash];
-[_MTLFunctionInternal newSpecializedFunctionWithDescriptor:destinationArchive:functionCache:sync:compilerTask:completionHandler:];
-[_MTLFunctionInternal initializeSourceArchive];
-[_MTLFunctionInternal setFilePath:];
-[_MTLFunctionInternal bindings];
-[_MTLFunctionInternal returnType];
-[_MTLFunctionInternal bitcodeDataInternal];
-[_MTLFunctionInternal patchControlPointCount];
-[_MTLFunctionInternal functionConstants];
-[_MTLFunctionInternal newFunctionWithPluginData:bitcodeType:];
-[_MTLFunctionInternal unpackedFilePath];
-[_MTLFunctionInternal setFunctionConstantSpecializationHash:];
-[_MTLFunctionInternal setBitcodeType:];
-[_MTLFunctionInternal initWithName:type:libraryData:functionData:device:];
-[_MTLFunctionInternal stitchingAirScript];
```
