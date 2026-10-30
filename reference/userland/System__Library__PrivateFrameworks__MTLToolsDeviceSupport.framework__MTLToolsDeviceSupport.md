# `/System/Library/PrivateFrameworks/MTLToolsDeviceSupport.framework/MTLToolsDeviceSupport`

iOS 27.2 dyld shared cache image. Version `310.8.0.0.0`. **[DSC]**

## Linked libraries (11)

- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/System/Library/PrivateFrameworks/GPUTools.framework/GPUTools`
- `/System/Library/PrivateFrameworks/GPUToolsCore.framework/GPUToolsCore`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`
- `/System/Library/Frameworks/IOSurface.framework/IOSurface`
- `/System/Library/Frameworks/Metal.framework/Metal`
- `/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libc++.1.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 15 classes, 6 protocols, 271 methods, 143 properties

### Class pages

Every class and protocol, with its methods: [`DYCAMetalLayerInfo`](../objc/DYCAMetalLayerInfo_MTLToolsDeviceSupport.md), [`DYCapturableObject`](../objc/DYCapturableObject_MTLToolsDeviceSupport.protocol.md), [`DYGraphicsAPIInfo`](../objc/DYGraphicsAPIInfo_MTLToolsDeviceSupport.protocol.md), [`DYMTLCaptureScopeInfo`](../objc/DYMTLCaptureScopeInfo_MTLToolsDeviceSupport.md), [`DYMTLCommandQueueInfo`](../objc/DYMTLCommandQueueInfo_MTLToolsDeviceSupport.md), [`DYMTLDerivedCounterSupport`](../objc/DYMTLDerivedCounterSupport_MTLToolsDeviceSupport.md), [`DYMTLDeviceProfile`](../objc/DYMTLDeviceProfile_MTLToolsDeviceSupport.md), [`DYMTLPixelHistoryTextureSupport`](../objc/DYMTLPixelHistoryTextureSupport_MTLToolsDeviceSupport.md), [`DYMTLShaderProfilerResult`](../objc/DYMTLShaderProfilerResult_MTLToolsDeviceSupport.md), [`DYMTLTextureResize`](../objc/DYMTLTextureResize_MTLToolsDeviceSupport.md), [`DYShaderAnalyzerResult`](../objc/DYShaderAnalyzerResult_MTLToolsDeviceSupport.md), [`DYShaderProfiler`](../objc/DYShaderProfiler_MTLToolsDeviceSupport.md), [`DYShaderProfilerDrawCallInfo`](../objc/DYShaderProfilerDrawCallInfo_MTLToolsDeviceSupport.md), [`DYShaderProfilerProgramInfo`](../objc/DYShaderProfilerProgramInfo_MTLToolsDeviceSupport.md), [`DYShaderProfilerResult`](../objc/DYShaderProfilerResult_MTLToolsDeviceSupport.md), [`DYShaderProfilerTimingWrapper`](../objc/DYShaderProfilerTimingWrapper_MTLToolsDeviceSupport.md), [`NSCoding`](../objc/NSCoding_MTLToolsDeviceSupport.protocol.md), [`NSCopying`](../objc/NSCopying_MTLToolsDeviceSupport.protocol.md), [`NSObject`](../objc/NSObject_MTLToolsDeviceSupport.protocol.md), [`NSSecureCoding`](../objc/NSSecureCoding_MTLToolsDeviceSupport.protocol.md), [`ShaderBinaryInfo`](../objc/ShaderBinaryInfo_MTLToolsDeviceSupport.md)

### Classes

`DYCAMetalLayerInfo`, `DYMTLCaptureScopeInfo`, `DYMTLCommandQueueInfo`, `DYMTLDerivedCounterSupport`, `DYMTLDeviceProfile`, `DYMTLPixelHistoryTextureSupport`, `DYMTLShaderProfilerResult`, `DYMTLTextureResize`, `DYShaderAnalyzerResult`, `DYShaderProfiler`, `DYShaderProfilerDrawCallInfo`, `DYShaderProfilerProgramInfo`, `DYShaderProfilerResult`, `DYShaderProfilerTimingWrapper`, `ShaderBinaryInfo`

### Protocols

`DYCapturableObject`, `DYGraphicsAPIInfo`, `NSCoding`, `NSCopying`, `NSObject`, `NSSecureCoding`

### Properties

```
@property (T@"NSString",R,N) capturableObjectType;
@property (T@"NSString",R,N) displayName;
@property (TQ,R,N) streamRef;
@property (T@"NSDictionary",R,N) defaultSamplePositions;
@property (T@"NSString",?,R,N) descriptionForBugReport;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (class, TB,R) supportsSecureCoding;
@property (TQ,R,N,V_deviceAddress) deviceAddress;
@property (TQ,R,N,V_layerAddress) layerAddress;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_frame) frame;
@property (T@"NSString",R,C,N,V_name) name;
@property (TQ,R,N,V_layerStreamRef) layerStreamRef;
@property (T@"NSString",R,N) capturableObjectType;
@property (T@"NSString",R,N,V_displayName) displayName;
@property (TQ,R,N) streamRef;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R,N,V_deviceAddress) deviceAddress;
@property (TQ,R,N,V_scopeAddress) scopeAddress;
@property (TQ,R,N,V_scopeStreamRef) scopeStreamRef;
@property (T@"NSString",R,C,N,V_label) label;
@property (TB,R,N,V_isDefaultCapturable) isDefaultCapturable;
@property (T@"NSString",R,N) capturableObjectType;
@property (T@"NSString",R,N,V_displayName) displayName;
@property (TQ,R,N) streamRef;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,N,V_streamRef) streamRef;
@property (TQ,R,N,V_deviceAddress) deviceAddress;
@property (TQ,R,N,V_deviceStreamRef) deviceStreamRef;
@property (TQ,R,N,V_queueAddress) queueAddress;
@property (TQ,R,N,V_toolsQueueAddress) toolsQueueAddress;
@property (T@"NSString",R,N,V_label) label;
@property (TB,N,V_canBeCaptured) canBeCaptured;
@property (TB,N,V_isOpenGLQueue) isOpenGLQueue;
@property (TB,N,V_isInternalQueue) isInternalQueue;
@property (T@"NSString",R,N) capturableObjectType;
@property (T@"NSString",R,N,V_displayName) displayName;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSMutableDictionary",R,N,V_counterDictionary) counterDictionary;
@property (T@"NSString",R,N,V_derivedCounterScript) derivedCounterScript;
@property (T@"NSString",R,N,V_analysisScript) analysisScript;
@property (T@"NSMutableDictionary",R,N,V_configurationVariables) configurationVariables;
@property (T@"NSString",R,N,V_metalPluginName) metalPluginName;
@property (TQ,R,N,V_streamRef) streamRef;
@property (T@"NSArray",R,N,V_supportedFeatureSets) supportedFeatureSets;
@property (T@"NSArray",R,N,V_supportedGPUFamilies) supportedGPUFamilies;
@property (T@"NSDictionary",R,N,V_defaultSamplePositions) defaultSamplePositions;
@property (T@"NSString",R,N,V_name) name;
@property (T@"NSNumber",R,N,V_registryID) registryID;
@property (T@"NSString",R,N) capturableObjectType;
@property (T@"NSString",R,N) displayName;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",?,R,N) descriptionForBugReport;
@property (T@"NSArray",&,N,V_encoderTilerParamBufBytesUsedArray) encoderTilerParamBufBytesUsedArray;
@property (T@"NSNumber",&,N,V_parameterBufferMaxSize) parameterBufferMaxSize;
@property (T@"NSNumber",&,N,V_parameterBufferMaxSizeEverMemless) parameterBufferMaxSizeEverMemless;
@property (T@"NSNumber",&,N,V_parameterBufferMaxSizeNeverMemless) parameterBufferMaxSizeNeverMemless;
@property (T@"NSDictionary",&,N,V_parameterBufferPercentFullDict) parameterBufferPercentFullDict;
@property (T@"NSDictionary",&,N,V_softwareCounterInfo) softwareCounterInfo;
@property (T@"NSMutableData",&,N,V_unknownUSCSamples) unknownUSCSamples;
@property (T@"NSMutableDictionary",&,N,V_perRingPerFrameLimiterData) perRingPerFrameLimiterData;
@property (T@"<MTLDevice>",R,V_device) device;
@property (Td,N,V_totalCost) totalCost;
@property (T@"NSDictionary",&,N,V_drawCallCost) drawCallCost;
@property (T@"NSDictionary",&,N,V_perFileCost) perFileCost;
@property (T@"NSDictionary",&,N,V_totalPerLineCost) totalPerLineCost;
@property (T@"NSDictionary",&,N,V_drawCallPerLineCost) drawCallPerLineCost;
@property (T@"NSDictionary",&,N,V_perFileLineCostDictForCI) perFileLineCostDictForCI;
@property (T@"NSArray",&,N,V_allShaderKeys) allShaderKeys;
@property (TI,N,V_drawCallIndex) drawCallIndex;
@property (TI,N,V_functionIndex) functionIndex;
@property (TI,N,V_pipelineStateIndex) pipelineStateIndex;
@property (TQ,N,V_pipelineStateId) pipelineStateId;
@property (TQ,N,V_pipelineStateFunctionIndex) pipelineStateFunctionIndex;
@property (TI,N,V_encoderIndex) encoderIndex;
@property (TQ,N,V_encoderStateId) encoderStateId;
@property (TQ,N,V_encoderFunctionIndex) encoderFunctionIndex;
@property (TI,N,V_commandBufferIndex) commandBufferIndex;
@property (Ti,N,V_subCommandIndex) subCommandIndex;
@property (T@"DYShaderProfilerProgramInfo",&,N,V_programInfo) programInfo;
@property (T{DYShaderProfilerTiming={Statistics=ddd}{Statistics=ddd}},R,N,V_vertexTiming) vertexTiming;
@property (T{DYShaderProfilerTiming={Statistics=ddd}{Statistics=ddd}},R,N,V_fragmentTiming) fragmentTiming;
@property (T{DYShaderProfilerTiming={Statistics=ddd}{Statistics=ddd}},R,N,V_computeTiming) computeTiming;
@property (T{DYShaderProfilerTiming={Statistics=ddd}{Statistics=ddd}},R,N,V_timing) timing;
@property (T@"NSArray",R,N,V_allShaderKeys) allShaderKeys;
@property (TI,N,V_programIndex) programIndex;
@property (TQ,N,V_programId) programId;
@property (TQ,N,V_pipelineStateFunctionIndex) pipelineStateFunctionIndex;
@property (TB,N,V_valid) valid;
@property (TI,R,N,V_programPipelineIndex) programPipelineIndex;
@property (TQ,R,N,V_pipelineStateId) pipelineStateId;
@property (T@"NSMutableArray",R,N,V_drawCallInfoList) drawCallInfoList;
@property (T{DYShaderProfilerTiming={Statistics=ddd}{Statistics=ddd}},R,N,V_vertexTiming) vertexTiming;
@property (T{DYShaderProfilerTiming={Statistics=ddd}{Statistics=ddd}},R,N,V_fragmentTiming) fragmentTiming;
@property (T{DYShaderProfilerTiming={Statistics=ddd}{Statistics=ddd}},R,N,V_computeTiming) computeTiming;
@property (T{DYShaderProfilerTiming={Statistics=ddd}{Statistics=ddd}},R,N,V_timing) timing;
@property (T@"NSMutableArray",&,N,V_drawCallInfoList) drawCallInfoList;
@property (T@"NSMutableArray",&,N,V_programPipelineInfoList) programPipelineInfoList;
@property (T{DYShaderProfilerTiming={Statistics=ddd}{Statistics=ddd}},N,V_vertexTiming) vertexTiming;
@property (T{DYShaderProfilerTiming={Statistics=ddd}{Statistics=ddd}},N,V_fragmentTiming) fragmentTiming;
@property (T{DYShaderProfilerTiming={Statistics=ddd}{Statistics=ddd}},N,V_computeTiming) computeTiming;
@property (T{DYShaderProfilerTiming={Statistics=ddd}{Statistics=ddd}},N,V_timing) timing;
@property (TQ,N,V_frameTime) frameTime;
@property (TI,N,V_deviceUtilization) deviceUtilization;
@property (TI,N,V_encoderCount) encoderCount;
@property (Td,N,V_gpuTime) gpuTime;
@property (T@"NSArray",&,N,V_blitTimeData) blitTimeData;
@property (T@"NSMutableDictionary",&,N,V_blitEncoderTimeInfo) blitEncoderTimeInfo;
@property (T@"NSMutableArray",&,N,V_shaderProfilingFrameTimes) shaderProfilingFrameTimes;
@property (Td,N,V_shaderProfilingTime) shaderProfilingTime;
@property (T@"NSDictionary",&,N,V_derivedCountersData) derivedCountersData;
@property (T@"NSMutableArray",R,N,V_encoderInfoList) encoderInfoList;
@property (T@"NSMutableArray",R,N,V_encoderFunctionIndexList) encoderFunctionIndexList;
@property (T@"NSMutableArray",R,N,V_programInfoList) programInfoList;
@property (T@"NSMutableDictionary",R,N,V_encoderFunctionIndexToEncoderIndexMap) encoderFunctionIndexToEncoderIndexMap;
@property (T@"NSMutableArray",&,N,V_effectiveKickTimes) effectiveKickTimes;
@property (T@"NSMutableArray",&,N,V_effectivePerEncoderDrawKickTimes) effectivePerEncoderDrawKickTimes;
@property (T@"NSMutableArray",&,N,V_averagePerDrawKickDurations) averagePerDrawKickDurations;
@property (T@"NSMutableArray",&,N,V_loadActionTimes) loadActionTimes;
@property (T@"NSMutableArray",&,N,V_storeActionTimes) storeActionTimes;
@property (TI,N,V_commandBufferCount) commandBufferCount;
@property (T@"NSMutableArray",&,N,V_perCommandBufferEncoderCount) perCommandBufferEncoderCount;
@property (T@"NSDictionary",&,N,V_encoderIndexToLabelMap) encoderIndexToLabelMap;
@property (T{DYShaderProfilerTiming={Statistics=ddd}{Statistics=ddd}},N,V_timing) timing;
@property (T@"NSData",&,N,V_binary) binary;
@property (T@"NSString",&,N,V_type) type;
@property (T@"NSNumber",&,N,V_dylib) dylib;
@property (T@"NSMutableData",&,N,V_uscSamples) uscSamples;
@property (T@"DYShaderAnalyzerResult",&,N,V_analyzerResult) analyzerResult;
```

## Strings (5,386)

First 3,000 of 5,386.
```
MTLLogicOpAnd
kDYFEMTLRenderCommandEncoder_setVertexSamplerStates_withRange
[%@ drawIndexedPatches:%@ patchStart:%@ patchCount:%@ patchIndexBuffer:%@ patchIndexBufferOffset:%@ controlPointIndexBuffer:%@ controlPointIndexBufferOffset:%@ instanceCount:%@ baseInstance:%@ tessellationFactorBuffer:%@ tessellationFactorB
[%@ compileVisibleFunction:%@ withDescriptor:%@ destinationBinaryArchive:%@ error:%@]
fragment shader info
iOS_GPUFamily1_v4
MTLHeapTypePlacement
OpaqueWhite
kDYFEMTLDevice_addTextureToGlobalResourceTable
kDYFEMTLAccelerationStructure_restoreMTLAccelerationStructure
kDYFEMTLBinaryArchive_addTileRenderPipelineFunctionsWithDescriptor_error
kDYFEMTLDevice_newDynamicLibrary_error
[%@ newComputePipelineStateWithName:%@ options:%@ reflection:%@ error:%@]
MTLFXTemporalScaler
MTLPixelFormatRG16Unorm
kDYFEMTLComputeCommandEncoder_insertUncompressedToCompressedFlush
[%@ copyFromTexture:%@ sourceSlice:%@ sourceLevel:%@ sourceOrigin:%@ sourceSize:%@ toBuffer:%@ destinationOffset:%@ destinationBytesPerRow:%@ destinationBytesPerImage:%@]
[%@ addBinaryEntry:%@ forKey:%@]
[%@ endResidency]
[%@ addAllocations:%@ count:%@]
MTLAttributeFormatHalf3
MTLBlendFactorOneMinusDestinationColor
Polygon
MTLStepFunctionThreadPositionInGridXIndexed
kDYFEMTLComputeCommandEncoder_setSamplerState_atIndex
kDYFEMTLDevice_newBufferWithBytesNoCopy_length_options_deallocator
MTLSynchronizationTypeCommit
MTLCommandEncoderTypeRender
MTLCommandEncoderTypeResourceState
MTLCompareFunctionGreaterEqual
MTLVertexAmplificationModeMask
PrivateTraceBuffer
RGB10A8_2P_sRGB
MTLVertexFormatChar3Normalized
kDYFEMTLDevice_newLibraryWithDescriptorSPI_error
kDYFEMTLFragmentRenderCommandEncoder_setFragmentSamplerState_lodMinClamp_lodMaxClamp_atIndex
kDYFEMTLDevice_sparseTileSizeInBytesForSparsePageSize
Back
MTLMathFloatingPointFunctionsFast
MTLPixelFormatRGB10_420_2P
Metal
kDYFEMTLFragmentRenderCommandEncoder_setFragmentTexture_baseLevel_atIndex
kDYFEMTLIndirectCommandBuffer_dealloc
kDYFEMTLParallelRenderCommandEncoder_setLabel
MTLTextureCompressionFeedbackUnsupportedTextureUsageShaderAtomic
TemporalScalerExeucutionMode
[%@ executeBarrier]
[%@ supportsFeatureSet:%@]
[%@ setBarrier]
AccelerationStructureCommandEncoderSetAccelerationStructureDescriptor
command-buffers
DeviceRemoved
TriangleSPI
MTLLogicOpOr
MTLValidationCodeBuffer
kDYFEMTLBlitCommandEncoder_copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toBuffer_destinationOffset_destinationBytesPerRow_destinationBytesPerImage_options
kDYFEMTLRenderCommandEncoder_updateFence_afterStages
[%@ drawPrimitives:%@ vertexStart:%@ vertexCount:%@]
[%@ writeSerializedAccelerationStructureSize:%@ toBuffer:%@ offset:%@]
Half4x2
MTLTextureColorSpaceConversionMatrixDefault
MTLRelocation
kDYFEMTLIndirectCommandBuffer_uniqueIdentifier
[%@ executeCommandsInBuffer:%@ indirectBuffer:%@ indirectBufferOffset:%@]
FractionalEven
kDYFEMTLBinaryArchive_writeToURL_error
[%@ loadTexture:%@ slice:%@ level:%@ size:%@ bytesPerRow:%@ bytesPerImage:%@ dstOrigin:%@ handle:%@ handleOffset:%@]
YCBCR10_444_2P
[%@ constantDataAtIndex:%@]
YCBCRA8_444_1P
kDYFEMTLBlitCommandEncoder_sampleCountersInBuffer_atSampleIndex_withBarrier
[%@ setTileBytes:%@ length:%@ atIndex:%@]
MTLAttributeFormatShort4
YCBCR10_444_2P_PACKED_PQ
kDYFEMTLBuffer_waitUntilComplete
[%@ supportsTextureSampleCount:%@]
[%@ removeAllocations:%@ count:%@]
Invert
kDYFEMTLCommandBuffer_encodeCacheControlFinalizeOperation_resourceGroups_count
kDYFEMTLDevice_newLibraryWithDAG_functions_error
kDYFEMTLFragmentRenderCommandEncoder_setDepthBias_slopeScale_clamp
MTLLanguageVersion1_1
MTLPixelFormatRGBA32Float
Maximum
MTLValidationCodeNewSamplerState
[%@ setVertexBytes:%@ length:%@ atIndex:%@]
MTLAccelerationStructureCommandSubstreamSelectMethodRoundRobin
MTLPixelFormatRGB8_444_2P
MTLPixelFormatYCBCR12_422_2P_PACKED
MTLCurveBasisBSpline
MTLCurveEndCapsSphere
MTLGPUFamilyApple9
Sparse
MTLIndexTypeUInt32
kDYFEMTLComputeCommandEncoder_setBuffer_offset_atIndex
[%@ updateFence:%@]
[%@ encodeDashboardFinalizeForResourceGroup:%@ dashboard:%@ values:%@ indices:%@ count:%@]
iOS_GPUFamily2_v2
CompileWarning
kDYFEMTLRenderCommandEncoder_drawIndexedPrimitives_indexType_indexBuffer_indexBufferOffset_indirectBuffer_indirectBufferOffset
[%@ deserializePrimitiveAccelerationStructure:%@ fromBytes:%@ withDescriptor:%@]
MTLGPUPriorityLow
MTLVideoCommandEncoderSPI
kDYFEMTLRenderCommandEncoder_setTileBuffers_offsets_withRange
[%@ setFragmentSamplerStates:%@ lodMinClamps:%@ lodMaxClamps:%@ withRange:%@]
MTLDeviceFeatureProfilewatchOS_1
MTLPipelineOptionPrivatePerformanceStatistics
MTLPixelFormatPVRTC_RGB_4BPP
%@\n%@
BGRA4Unorm
MTLQosOpportunistic
kDYFEMTLRenderCommandEncoder_drawIndexedPatches_patchIndexBuffer_patchIndexBufferOffset_controlPointIndexBuffer_controlPointIndexBufferOffset_indirectBuffer_indirectBufferOffset
[%@ newFunctionWithName:%@ constantValues:%@ completionHandler:%@]
[%@ encodePrimaryGradientToCommandBuffer:%@ encoder:%@ options:%@ pluginOptions:%@ primaryBuffer:%@ primaryInfo:%@ secondaryBuffer:%@ secondaryInfo:%@ gradientBuffer:%@ gradientInfo:%@ destination:%@ destinationInfo:%@ accumulate:%@ predica
Line
BC3_RGBA_sRGB
MTLFunctionHandle
UnsupportedTextureUsageShaderAtomic
kDYFEMTLDevice_newResourceGroupFromResources_count
kDYFEMTLResidencySet_generationForHeap
[%@ encodeStartWhile:%@ offset:%@ comparison:%@ referenceValue:%@]
[%@ fillTexture:%@ level:%@ slice:%@ region:%@ color:%@]
[%@ setMeshBytes:%@ length:%@ atIndex:%@]
Half4
AtomicStore
MTLBinaryArchiveSerializationDeviceAspectAlways
MTLDynamicLibraryTypeRebuild
kDYFEMTLRenderCommandEncoder_setVertexBytes_length_attributeStride_atIndex
kDYFEMTLRenderCommandEncoder_useResources_count_usage
TextureResourceUsage
MTLPixelFormatBGRA10Unorm
MTLRenderCommandEncoderSplitReasonTooManyDepthBiasEmits
MTLTextureColorSpaceConversionMatrixBT601Full
[%@ removeResources:%@ count:%@]
Normalize
MTLPixelFormatYCBCR10_444_1P
kDYFEMTLIndirectRenderCommand_reset
[%@ newArgumentEncoderWithBufferIndex:%@ reflection:%@ pipelineLibrary:%@]
MTLFunctionOptionStoreFunctionInMetalScript
MTLFence
kDYFEMTLDevice_newSharedEventWithMachPort
kDYFEMTLDevice_setCompilerProcessesCount
Float4x2
PVRTC_RGBA_4BPP_sRGB
YCBCR12_422_2P_PACKED_HLG
kDYFEMTLIndirectRenderCommand_setFragmentBuffer_offset_atIndex
[%@ newIOHandleWithURL:%@ error:%@]
MTLDataTypeUInt8
DeviceAspect
MTLVertexFormatChar4
MTLAccelerationStructure
[%@ deserializeAccelerationStructure:%@ fromBuffer:%@ serializedBufferOffset:%@]
[%@ encodeEndWhile]
_frg
StreamingCodec
MTLFeatureSet_iOS_GPUFamily3_v4
ASTC_8x6_HDR
IsLossyLevel3Compatible
kDYFEMTLBlitCommandEncoder_synchronizeResource
[%@ waitForFence:%@ beforeStages:%@]
MTLBindingAccessReadWrite
MTLCurveTypeFlat
MTLDataTypeChar2
MTLLoadActionLoad
YCBCR10_420_2P_PACKED_PQ
kDYFEMTLCommandBuffer_debugCommandEncoder
kDYFEMTLIndirectCommandBuffer_doesAliasResource
[%@ presentDrawable:%@ atTime:%@]
_norm
DeveloperTools
kDYFEMTLDevice_newComputePipelineDescriptorWithSerializedData_deserializationContext
[%@ setVertexSamplerStates:%@ lodMinClamps:%@ lodMaxClamps:%@ withRange:%@]
[%@ newDefaultLibraryWithBundle:%@ error:%@]
MTLPixelFormatRG8Unorm
IsMSAACapable
kDYFEMTLCounterSet_dealloc
kDYFEMTLDevice_newLogStateWithDescriptor_error
kDYFEMTLIOCommandQueue_commandBuffer
[%@ newRenderPipelineStateWithTileDescriptor:%@ error:%@]
AccelerationStructureStorageBuffer
MTLDataTypeUInt16
BGR5A1Unorm
IsCompressed
MTLTextureColorSpaceConversionMatrixBT601Video
MTLSharedTextureHandle
kDYFEMPSExternalCNNUnary_maxBatchSize
kDYFEMTLCommandQueue_setCompletionQueue
kDYFEMTLDevice_newArgumentEncoderWithBufferBinding
_vtx
MTLAccelerationStructureInstanceOptionNonOpaque
EnableResourcePatchingInstrumentation
Curves
MTLResourceGroupCacheHintFlush
kDYFEMTLLibrary_serializeToURL_error
[%@ presentDrawable:%@ afterMinimumDuration:%@]
[%@ setVertexAmplificationCount:%@ viewMappings:%@]
RowLinearPVRTC
MTLComputeFPRoundToInfinityBit
kDYFEMTLAccelerationStructureCommandEncoder_useResource_usage
[%@ setAlphaTestReferenceValue:%@]
SpecializedFunctionsAspectIfAvailable
MTLFeatureSet_iOS_GPUFamily4_v2
ASTC_5x5_LDR
AMDGPU
[%@ saveSlice:%@ level:%@ zPlane:%@ normalize:%@ blitOption:%@ toPath:%@]
MTLBinaryArchiveLoadToRecompile
MTLPrecompiledDataTypeTileReflectionData
MTLRenderCommandEncoderSplitReasonTooManyResources
kDYFEMTLRenderPipelineState_newVisibleFunctionTableFromVertexStageWithDescriptor
[%@ setFragmentBytes:%@ length:%@ atIndex:%@]
FloatRG11B10
UShort
kDYFEMTLIOCommandBuffer_encodeWaitForEvent_value
PrivateMesh
Half4x3
tvOS_6
kDYFEMTLCaptureScope_dealloc
kDYFEMTLDevice_newRenderPipelineStateWithDescriptor_options_completionHandler
kDYFEMTLDevice_setCommandBufferErrorOptions
[%@ drawIndexedPatches:%@ patchStart:%@ patchCount:%@ patchIndexBuffer:%@ patchIndexBufferOffset:%@ controlPointIndexBuffer:%@ controlPointIndexBufferOffset:%@ instanceCount:%@ baseInstance:%@]
Last
kDYFEMTLIntersectionFunctionTable_isAliasable
PrivateExplicit
iOS_9
iOS_GPUFamily1_v1
MTLLibraryOptimizationLevelSize
kDYFEMTLComputeCommandEncoder_useResidencySets_count
kDYFEMTLFunction_reflectionWithOptions_binaryArchives
kDYFEMTLIndirectRenderCommand_drawPrimitives_vertexStart_vertexCount_instanceCount_baseInstance
kDYFEMTLRenderCommandEncoder_setObjectVisibleFunctionTables_withBufferRange
toolsQueueAddress
BlendColor
Never
Depth32Float_Stencil8
[%@ setProfilingEnabled:%@]
[%@ newComputePipelineDescriptorWithName:%@ error:%@]
[%@ setObjectTextures:%@ withRange:%@]
Char3Normalized
RGB10_444_2P_PACKED
MTLSparseTextureRegionAlignmentModeInward
kDYFEMTLArgumentEncoder_setRenderPipelineStates_withRange
kDYFEMTLRenderPipelineState_setEmulationVertexShaderIntermediateBufferSlot
kDYFEMTLTexture_getBytes_bytesPerRow_bytesPerImage_fromRegion_mipmapLevel_slice
[%@ enqueue]
[%@ setFragmentBuffers:%@ offsets:%@ withRange:%@]
Int2
MTLGenericBVHTypePrimitiveSPI
MTLVREyeLeft
[%@ setFragmentTexture:%@ atTextureIndex:%@ samplerState:%@ atSamplerIndex:%@]
MTLPixelFormatYCBCR10_444_2P
MTLIndirectComputeCommand
MTLRasterizationRateMap
MTLDataTypeFloat2x4
Automatic
BT2020Full
MTLVertexFormatShort3
kDYFEMTLRenderPipelineState_newObjectIntersectionFunctionTableWithDescriptor
kDYFEMTLTexture_newTextureViewWithPixelFormat_textureType_levels_slices_swizzle
[%@ newVertexIntersectionFunctionTableWithDescriptor:%@]
MTLFunctionOptionCompileToBinary
MTLFunctionOptionNone
MTLPixelFormatYCBCR8_422_2P
OpenCL
[%@ startCaptureWithCommandQueue: %@]
_cmp
MTLArgumentImageBlockKindPrivateImplicit
IsHalfCompatible
kDYFEMTLParallelRenderCommandEncoder_setSeparateCommits
MTLPipelineLibraryMetallibFileName
Vector
MTLStepFunctionPerPatch
kDYFEMTLBuffer_heapOffset
kDYFEMTLRenderPipelineState_setEmulationMeshMaxPrimitiveCount
MTLCompilerFlagNone
WorldSpaceData
MTLVisibilityResultModeCounting
kDYFEMPSExternalCNNConvolution_reloadWeightsAndBiases
[%@ startCaptureWithScope:%@]
[%@ newRenderPipelineStateWithAdditionalBinaryFunctions:%@ error:%@]
MTLPixelFormatR16Sint
kDYFEMTLComputeCommandEncoder_setBufferOffset_attributeStride_atIndex
[%@ setMeshIntersectionFunctionTable:%@ atBufferIndex:%@]
v32@?0@\"NSString\"8@\"NSMutableData\"16^B24
MTLDataTypeHalf3x4
MTLGPUMemoryErrorAddress
MTLPixelFormatRGB10A2Unorm_PQ
MTLPixelFormatYCBCR12_422_2P
MTLSamplerReductionModeSupportNone
kDYFEMTLIndirectRenderCommand_setTessellationFactorScale
[%@ setVertexAccelerationStructure:%@ atBufferIndex:%@]
#include <metal_stdlib>\nusing namespace metal;\nstruct VertexOutput\n{\n    vec<float, 4> pos [[position]];\n    vec<float, 2> uv;\n};\nvertex VertexOutput passthroughVertex(uint vid [[ vertex_id ]],\n                                      
MTLDeviceFeatureProfiletvOS_5
InvOr
R32Uint
YCBCR12_422_2P_PACKED
SamplerArgumentBufferEncoding
kDYFEMTLDevice_deserializePrimitiveAccelerationStructure_fromBytes_withDescriptor
kDYFEMTLEvent_setLabel
BoundingBox
RenderCommandEncoder
MTLVertexFormatFloatRG11B10
kDYFEMTLDevice_newRenderPipelineStateWithMeshDescriptor_completionHandler
kDYFEMTLIOCommandBuffer_loadBuffer_offset_size_handle_handleOffset
kDYFEMTLIntersectionFunctionTable_setGlobalBuffer
kDYFEMTLRenderCommandEncoder_setVertexAccelerationStructure_atBufferIndex
kDYFEMTLTexture_gpuResourceID
kDYFEMTLAccelerationStructure_dealloc
[%@ setObjectTexture:%@ atIndex:%@]
[%@ setKernelBuffer:%@ offset:%@ attributeStride:%@ atIndex:%@]
compute-pipeline-state
Apple7
kDYFEMTLAccelerationStructure_allocationInfo
kDYFEMTLIOCommandQueue_commandBufferWithUnretainedReferences
kDYFEMTLRenderCommandEncoder_memoryBarrierWithResources_count_afterStages_beforeStages
[%@ dealloc]
[%@ setFragmentTextures:%@ withRange:%@]
[%@ useHeaps:%@ count:%@]
[%@ sampleCountersAtInterval:%@ sampleBuffer:%@ error:%@]
CiSululuiululul
Bool
MTLDataTypeChar3
kDYFEMTLBlitCommandEncoder_optimizeContentsForGPUAccess_slice_level
kDYFEMTLDepthStencilState_dealloc
kDYFEMTLDevice_supportsTextureWriteRoundingMode
kDYFEMTLRenderCommandEncoder_setObjectIntersectionFunctionTable_atBufferIndex
[%@ objectFunctionHandleWithFunction:%@]
RGB10A8_2P_PQ
MTLStitchedLibraryOptionAllowBadLegacyDAGs
MTLStoreActionOptionCustomSamplePositions
kDYFEMTLAccelerationStructure_state
kDYFEMTLComputeCommandEncoder_setSamplerState_lodMinClamp_lodMaxClamp_atIndex
kDYFEMTLParallelRenderCommandEncoder_renderCommandEncoder
[%@ newObjectIntersectionFunctionTableWithDescriptor:%@]
parallel-render-passes
MTLBinaryArchiveSerializationChecksum
MTLFeatureSet_iOS_GPUFamily2_v1
MTLPrecompiledDataTypeCustomStart
TextureBuffer
MTLVertexStepFunctionPerVertex
[%@ newRasterizationRateMapWithDescriptor:%@]
[%@ requestResidency]
PrivateFunctionPointer
MTLBindingTypeBuffer
YCBCR12_444_2P_PACKED
kDYFEMPSExternalNDArrayBinary_encodeToCommandBuffer_encoder_options_pluginOptions_primaryBuffer_primaryInfo_secondaryBuffer_secondaryInfo_destinationBuffer_destinationInfo_predicationBuffer_predicationOffset
kDYFEMTLAccelerationStructureCommandEncoder_waitForFence
kDYFEMTLComputeCommandEncoder_useResources_count_usage
kDYFEMTLIndirectRenderCommand_nop
[%@ meshFunctionHandleWithFunction:%@]
Sampler
MTLAttributeFormatShort3Normalized
MTLColorWriteMaskAlpha
YCBCR10_444_2P_sRGB
MTLSparsePageSize256
[%@ setTileTextures:%@ withRange:%@]
%@/%@
kDYFEMTLDevice_getBVHBuilderLock
BufferParentGPUAddressAndSize
MTLDataTypeComputePipeline
MTLFunctionTypeObject
AtomicLoad
MTLSamplerReductionModeMaximum
[%@ setSkipRender:%@]
[%@ maxBatchSize]
MTLCurveBasisLinear
MTLLanguageVersion2_1
MTLVertexFormatUChar2
kDYFEMTLDevice_newFunctionWithGLIR_inputsDescription_functionType
kDYFEMTLIOCommandQueue_continueCommandBuffer_retainReferences
[%@ writeToURL:%@ error:%@]
[%@ setPrivateData:%@]
MTLAccelerationStructureUsagePreferFastBuild
MTLDeviceFeatureProfileiOS_6
R12Uint_PACKED
kDYFEMTLVideoCommandEncoder_endEncoding
MTLHeapCurrentAllocatedSize
MTLIntersectionFunctionSignatureTriangleData
MTLProvokingVertexModeLast
MTLVertexFormatUShort2
kDYFEMTLVideoCommandEncoder_dealloc
MTLComparisonNotEqual
MTLStencilOperationDecrementClamp
MTLVertexFormatInt2
[%@ newIOFileHandleWithURL:%@ compressionMethod:%@ error:%@]
MTLHeapAliasedResources_deprecated
MTLPixelFormatR10Unorm_PACKED
kDYFEMPSPlugin_newNDArrayConvolution2DGradientWithDescriptor
[%@ newBinaryArchiveWithDescriptor:%@ error:%@]
[%@ setObjectAccelerationStructure:%@ atBufferIndex:%@]
MTLPixelFormatABGR4Unorm
MTLValidationCodeAcelerationStructureCommandEncoder
MTLFragmentRenderCommandEncoder
MTLDataTypeDouble2
MTLFeatureSet_tvOS_GPUFamily1_v4
Device
_MTLArgumentBufferResourceTypeCount
kDYFEMTLBlitCommandEncoder_optimizeContentsForCPUAccess
Q
YCBCR10_420_2P_HLG
YCBCR10_420_2P_PACKED_sRGB
MTLVertexFormatUChar2Normalized
[%@ newTextureViewWithPixelFormat:%@]
[%@ newFunctionWithDescriptor:%@ completionHandler:%@]
[%@ serializePrimitiveAccelerationStructure:%@ toBuffer:%@ serializedBufferOffset:%@]
[%@ newVisibleFunctionTableWithDescriptor:%@ stage:%@]
MTLTextureTypeCubeArray
kDYFEMTLRenderPipelineState_newVisibleFunctionTableFromObjectStageWithDescriptor
Visible
ASTC_8x4_LDR
kDYFEMTLComputeCommandEncoder_setBuffer_offset_attributeStride_atIndex
kDYFEMTLDevice_newFunctionWithGLIR_functionType
[%@ finish]
[%@ drawIndexedPatches:%@ patchIndexBuffer:%@ patchIndexBufferOffset:%@ controlPointIndexBuffer:%@ controlPointIndexBufferOffset:%@ indirectBuffer:%@ indirectBufferOffset:%@]
RG10Unorm_PACKED
kDYFEMTLFragmentRenderCommandEncoder_setStencilFrontReferenceValue_backReferenceValue
[%@ deserializeAccelerationStructure:%@ primitiveAccelerationStructures:%@ fromBuffer:%@ serializedBufferOffset:%@]
Warning
ASTC_12x10_LDR
kDYFEMTLHeap_usedSize
kDYFEMTLIntersectionFunctionTable_setResponsibleProcess
kDYFEMTLRenderCommandEncoder_setVertexBuffers_offsets_withRange
MTLArgumentTypePrivateComputePipeline
MTLDataTypeFloat4x2
ASTC_4x4_sRGB
kDYFEMPSExternalMatrixMultiplication_encodeToCommandBuffer_encoder_options_batchSize_resultRows_resultColumns_interiorColumns_alpha_beta_A_aInfo_B_bInfo_C_cInfo
kDYFEMTLDevice_requiresIndirectionForAllResourceTypes
kDYFEMTLIndirectComputeCommand_setKernelBuffer_offset_atIndex
[%@ serializeToURL:%@ options:%@ error:%@]
SourceAlphaSaturated
MTLBuiltInMeshGridProperties
Clip
MTLPixelFormatYCBCR8_444_2P
[%@ functionPointerHandleWithFunction:%@]
[%@ deserializePrimitiveAccelerationStructureFromBytes:%@ withDescriptor:%@]
MTLFunctionInfo
MTLAttributeFormatUChar2Normalized
Relaxed
MTLPixelFormatR8Uint
RGB10A2Uint
IsLossyLevel2Compatible
MTLPixelFormatFlagsIsUShortCompatible
MTLTextureSwizzleShiftAlpha
MTLVertexFormatShort2Normalized
MTLDataTypeBFloat4x2
kDYFECAMetalLayer_setFramebufferOnly
[%@ newSharedEvent]
ThreadsPerSimdgroup
MTLDynamicLibraryTypeCompatible
kDYFEMTLFXTemporalScaler_setExposureTexture
[%@ setMeshTexture:%@ atIndex:%@]
Char3
MTLAttributeFormatUChar3
MTLLogicOperationNor
kDYFEMTLIOScratchBufferAllocator_dealloc
[%@ setKernelBuffer:%@ offset:%@ atIndex:%@]
[%@ sparseTileSizeWithTextureType:%@ pixelFormat:%@ sampleCount:%@ sparsePageSize:%@]
BufferHeapOffset
[%@ setBounds:%@ contentsScale:%@ windowBounds:%@)
PrivateDepthStencilState
MTLDataTypeUChar3
MTLDynamicLibraryLoadSkipAIRValidation
MTLShaderValidationDefault
kDYFEMTLDevice_newLateEvalEvent
kDYFEMTLIOCommandBuffer_popDebugGroup
kDYFEMTLRenderCommandEncoder_setFragmentSamplerStates_lodMinClamps_lodMaxClamps_withRange
[%@ setReset:%@]
MTLAttributeFormatShort3
MTLCompilerFlagLoadVertexAttributeData
MTLDataTypeImageBlock
kDYFEMTLDevice_newFunctionWithGLCoreIR_functionType
kDYFEMTLParallelRenderCommandEncoder_setStencilStoreActionOptions
MTLLogicOpNor
MTLStorageModePrivate
RenderPipelineDescriptor
kDYFEMTLIndirectRenderCommand_setMeshBuffer_offset_atIndex
kDYFEMTLRenderCommandEncoder_setMeshBufferOffset_atIndex
MTLDataTypePrivateVoid
MTLResourceStorageModeManaged
kDYFEMTLHeap_newAccelerationStructureWithDescriptor_offset
kDYFEMTLRenderCommandEncoder_sampleCountersInBuffer_atIndex_allowOverlap
MTLAccelerationStructureInstanceDescriptorTypeIndirect
MTLAttributeFormatChar3
MTLDeviceFeatureProfileiOS_9B
MTLLogicOperationClear
RGB10_420_2P
kDYFEMTLBlitCommandEncoder_fillBuffer_range_pattern4
[%@ read:%@ size:%@ offset:%@ stagingBuffer:%@ stagingBufferSize:%@]
[%@ doesAliasAllResources:%@ count:%@]
[%@ setObjectBufferOffset:%@ atIndex:%@]
[%@ setPrivateDataOffset:%@]
MTLPixelFormatBC1_RGBA_sRGB
MTLPixelFormatR8Unorm
MTLPixelFormatRGB10A8_2P_XR10
YCBCR10_444_1P
kDYFEMTLDevice_newRenderPipelineStateWithMeshDescriptor_options_completionHandler
[%@ setCullMode:%@]
[%@ setTexture:%@ baseLevel:%@ atIndex:%@]
MTLDataTypeFloat2x3
[%@ newAccelerationStructureWithSize:%@]
[%@ addHeap:%@]
MTLArgumentTypeTexture
MTLMeshTopologyKindNone
2
iOS_GPUFamily3_v3
[%@ drawIndexedPrimitives:%@ indexCount:%@ indexType:%@ indexBuffer:%@ indexBufferOffset:%@]
[%@ sampleTimestamps:%@ gpuTimestamp:%@]
PrivateImplicit
MTLBlendFactorOneMinusSource1Color
BFloat3x4
MTLMotionEstimationPipeline
kDYFEMTLComputeCommandEncoder_memoryBarrierWithScope
[%@ tileFunctionHandleWithFunction:%@]
Bool16
MTLDataTypeHalf2x4
MTLPrecompiledDataTypeComputeReflectionData
kDYFEMTLRenderCommandEncoder_dispatchThreadsPerTile_inRegion
kDYFEMTLTexture_newRemoteTextureViewForDevice
[%@ setVertexVisibleFunctionTables:%@ withBufferRange:%@]
PageFault
MTLGPUFamilyApple10
ColumnMajor
VertexReflectionData
Lossy
kDYFEMTLVisibleFunctionTable_setBuffer_offset_atIndex
kDYFEMTLTexture_waitUntilComplete
CiSululuiulululululb
PrivateByVal
MTLPixelFormatASTC_6x6_sRGB
MTLPixelFormatFlagsIsFloatCompatible
ThreadPositionInGridY
MTLTextureRotationTranspose
Committed
MTLMathFloatingPointFunctionsPrecise
[%@ setResponsibleTaskIDs:%@ count:%@]
watchOS_1
YCBCR12_422_2P
MTLPixelFormatYCBCR12_444_2P_XR
MTLStoreActionMultisampleResolve
Private_TAAU
kDYFEMPSPlugin_newCNNNeuronWithNeuronType_neuronParameterAArray_count
[%@ optimizeContentsForGPUAccess:%@ slice:%@ level:%@]
[%@ endIndirectCommandBuffer]
int2
kDYFEMTLAccelerationStructureCommandEncoder_serializePrimitiveAccelerationStructure_toBuffer_serializedBufferOffset
kDYFEMTLRenderCommandEncoder_setTileVisibleFunctionTables_withBufferRange
[%@ setVertexVisibleFunctionTable:%@ atBufferIndex:%@]
[%@ setThreadgroupDistributionModeWithClusterGroupIndex:%@]
kDYFEMTLFragmentRenderCommandEncoder_setScissorRect
IndirectCommandBuffer
Indirect
WriteOnly
RoundToNearestBit
Apple5
MTLGenericBVHTypeInstanceMotionSPI
MTLPrimitiveKindNone
kDYFEMTLComputeCommandEncoder_setVisibleFunctionTable_atBufferIndex
MTLAccelerationStructureUsageRefit
RenderPipeline
MTLGPUAddressSpaceThreadgroup
MTLGPUFamilyApple6
R10Uint_X6
MTLPixelFormatFlagsIsRestrictedFormatAccess
kDYFEMTLDevice_newAccelerationStructureWithBuffer_offset
kDYFEMTLParallelRenderCommandEncoder_setColorStoreAction_atIndex
GPU Time
MTLCommandBufferStatusError
InstanceMotion
Noop
MTLPixelFormatYCBCR10_422_2P_PACKED_XR
IsPVRTC
kDYFEMPSPlugin_newMatrixVectorMultiplicationWithTranspose_rows_columns_alpha_beta
kDYFEMTLComputeCommandEncoder_setThreadgroupDistributionModeWithClusterGroupIndex
MTLDataTypeFloat3
MTLDataTypeHalf8
RGBA16Unorm
Intersection
MTLPixelFormatASTC_5x5_LDR
kDYFEMTLFragmentRenderCommandEncoder_pushDebugGroup
kDYFEMTLVisibleFunctionTable_setBuffers_offsets_withRange
[%@ getTextureAccessCounters:%@ region:%@ mipLevel:%@ slice:%@ resetCounters:%@ countersBuffer:%@ countersBufferOffset:%@]
iOS_8
MTLVisibilityResultModeBoolean
kDYFEMTLBuffer_newTiledTextureWithDescriptor_offset_bytesPerRow
[%@ setTileSamplerStates:%@ withRange:%@]
failed to dlopen interpose dylib: %s
com.apple.MTKTextureLoader
MTLPixelFormatBGRA4Unorm
YCBCR10_444_2P_HLG
MTLPixelFormatYCBCR10_444_2P_HLG
[%@ copyFromTexture:%@ sourceSlice:%@ sourceLevel:%@ sourceOrigin:%@ sourceSize:%@ toBuffer:%@ destinationOffset:%@ destinationBytesPerRow:%@ destinationBytesPerImage:%@ options:%@]
MTLDynamicLibraryInfo
Double3
BC2_RGBA_sRGB
MTLTriangleFillModePoint
MTLIndirectCommandBuffer
kDYFEMTLIndirectRenderCommand_setObjectBuffer_offset_atIndex
[%@ functionHandleWithFunction:%@]
[%@ setMeshSamplerStates:%@ lodMinClamps:%@ lodMaxClamps:%@ withRange:%@]
[%@ encodeToCommandBuffer:%@ encoder:%@ optionsAndBatchSize:%@ inputMatrix:%@ inputMatrixInfo:%@ weightMatrix:%@ weightMatrixInfo:%@ biasVector:%@ biasVectorInfo:%@ resultMatrix:%@ resultMatrixInfo:%@ alpha:%@ numberOfFeatureVectorsAndInput
Subtract
MTLDynamicLibraryErrorUnresolvedInstallName
kDYFEMTLDevice_newBufferWithIOSurface
MTLPixelFormatASTC_5x4_LDR
MTLFXSpatialScalerColorProcessingModeHDR
kDYFEMTLComputeCommandEncoder_enableNullBufferBinds
[%@ newRenderPipelineStateWithMeshDescriptor:%@ options:%@ completionHandler:%@]
command-queue
EncoderExecutionStatus
Unsupported
MTLPixelFormatFlagsIsLossyLevel3Compatible
WeightedAverage
kDYFEMTLDevice_newSharedEventWithHandle
return
UShort4
kDYFEMTLHeap_newTextureWithDescriptor_atOffset
kDYFEMTLRenderCommandEncoder_drawPatches_patchStart_patchCount_patchIndexBuffer_patchIndexBufferOffset_instanceCount_baseInstance
MTLResourceUsageRead
kDYFEMTLAccelerationStructure_isAliasable
kDYFEMTLComputePipelineState_functionHandleWithFunction
[%@ newTextureViewWithPixelFormat:%@ textureType:%@ levels:%@ slices:%@ resourceIndex:%@]
MTLCommandBufferErrorStackOverflow
ASTC_6x6_HDR
MTLUnmappedDepthValueZero
[%@ drawPrimitives:%@ indirectBuffer:%@ indirectBufferOffset:%@]
[%@ setIsOpenGLQueue:%@]
[%@ dispatchThreads:%@ threadsPerThreadgroup:%@]
[%@ commitAdds]
tvOS_2
UInt2
MTLGenericBVHHeaderVersionInitialSPI
BGRA10Unorm_HLG
kDYFEMTLDevice_reserveResourceIndicesForResourceType_indices_indexCount
[%@ executeCommandsInBuffer:%@ startIndex:%@]
[%@ loadDynamicLibrariesForComputeDescriptor:%@ options:%@ error:%@]
UInt4
Mac2
Char16
MTLPixelFormatBGR5A1Unorm
MTLResourceCPUCacheModeWriteCombined
MTLValidationCodeResourceStateCommandEncoderMoveMappings
MTLVertexFormatInt1010102Normalized
MTLArgumentEncoder
kDYFEMTLComputePipelineState_newIntersectionFunctionTableWithDescriptor
kDYFEMTLResidencySet_addAllocations_count
IsLossyLevel1Compatible
IntelGPU
kDYFEMTLAccelerationStructure_heapOffset
kDYFEMTLComputePipelineState_newComputePipelineStateWithAdditionalBinaryFunctions_error
[%@ setVertexTexture:%@ baseLevel:%@ atIndex:%@]
[%@ dropResourceGroups:%@ count:%@]
[%@ setVertexIntersectionFunctionTables:%@ withBufferRange:%@]
MTLBinaryArchiveSerializationDescriptorAspectAlways
[%@ encodeToCommandBuffer:%@]
[%@ newArgumentEncoderWithBufferIndex:%@]
[%@ newFunctionWithDescriptor:%@ error:%@]
MTLPixelFormatFlagsIsMSAACapable
MTLResourceGroupCacheHintInvalidate
kDYFEMTLDevice_newArgumentBufferLayoutWithStructType
kDYFEMTLSharedEventHandle_dealloc
MTLFunctionConstantsArray
Float
MTLCompilerFlagPackVaryings
MTLDataTypeBFloat4x3
Float16
Num
IsStencilRenderable
[%@ setFragmentIntersectionFunctionTable:%@ atBufferIndex:%@]
-analysis.js
MTLBuiltInArgumentThreadsPerThreadgroup
MTLGPUOperationAtomicCompareExchange
ASTC_8x4_sRGB
0Degrees
kDYFEMTLComputeCommandEncoder_setImageblockWidth_height
RGB10A2Unorm
MTLDispatchTypeConcurrent
MTLEventOptionSupportRollback
DrawMeshThreadgroups
kDYFEMTLAccelerationStructureCommandEncoder_deserializeInstanceAccelerationStructure_primitiveAccelerationStructures_fromBuffer_serializedBufferOffset
[%@ setResponsibleProcess:%@]
RenderTargets
MTLDeviceLocationBuiltIn
kDYFEMTLDevice_describeCounter
[%@ setBytes:%@ length:%@ attributeStride:%@ atIndex:%@]
[%@ newResidencySetWithDescriptor:%@ error:%@]
BFloat4
MTLGPUMemoryErrorNull
BGRA10_XR_PACKED
MTLPixelFormatRG11B10Float
kDYFEMTLRenderCommandEncoder_setDepthClipMode
kDYFEMTLTexture_newSharedHandle
[%@ newAccelerationStructureWithDescriptor:%@ offset:%@]
MTLDataTypeBFloat4
MTLPixelFormatYCBCR10_420_2P_HLG
MTLValidationCodePixelFormat
[%@ newFence]
kDYFEMTLIOFileHandle_setLabel
kDYFEMTLCommandBuffer_commitAndWaitUntilSubmitted
kDYFEMTLDevice_minLinearTextureAlignmentForPixelFormat
kDYFEMTLHeap_setPurgeableState
MTLDataTypeDouble4
ASTC_10x8_sRGB
MTLPixelFormatFlagsIsStencilRenderable
kDYFEMTLDevice_newFunctionWithGLESIR_inputsDescription_functionType
kDYFEMTLIOCommandBuffer_copyStatusToBuffer_offset
AccessRevoked
MTLPixelFormatPVRTC_RGBA_4BPP
MTLSamplerMipFilterNearest
MTLValidationCodeIOHandle
[%@ setFragmentBufferOffset:%@ atIndex:%@]
[%@ encodeToCommandBuffer:%@ encoder:%@ options:%@ pluginOptions:%@ primaryBuffer:%@ primaryInfo:%@ secondaryBuffer:%@ secondaryInfo:%@ destinationBuffer:%@ destinationInfo:%@ predicationBuffer:%@ predicationOffset:%@ ]
YCBCR12_420_2P_XR
Compute
Write
kDYFEMTLRenderCommandEncoder_setObjectBufferOffset_atIndex
[%@ isWriteComplete]
MTLBuiltInArgumentThreadPositionInThreadgroup
MTLDataTypeUChar
MTLPixelFormatASTC_8x6_LDR
BC5_RGUnorm
MTLPixelFormatEAC_RGBA8_sRGB
kDYFEMTLAccelerationStructure_restoreMTLAccelerationStructure_instance
kDYFEMTLBuffer__aneIOSurface
MTLBuiltInArgumentInstanceID
Depth32Float
R10Unorm_X6_PQ
MTLPrimitiveTypeQuad
MTLTextureRotation90DegreesClockwise
kDYFEMTLDevice_newIOFileHandleWithURL_error
[%@ newComputePipelineStateWithFunction:%@ options:%@ reflection:%@ error:%@]
FrameEnd
MTLPixelFormatBGRA10Unorm_PACKED_HLG
[%@ resourceIndexFromIndirectBufferAddress:%@]
RG10Unorm_X12
BT709Video
kDYFEMTLDevice_setRawBVHBuilderPtr
kDYFEMTLComputeCommandEncoder_encodeStartWhile_offset_comparison_referenceValue
kDYFEMTLDevice_supportsTextureWriteFPRoundingMode
kDYFEMTLTexture_newTextureViewWithPixelFormat_textureType_levels_slices_swizzle_resourceIndex
tex.sparse_sample(samp, in.uv).value()
Float2
LessThanOrEqual
kDYFECAMetalDrawable_dealloc
kDYFEMTLRenderPipelineState_meshFunctionHandleWithFunction
[%@ newRenderPipelineStateWithTileDescriptor:%@ options:%@ reflection:%@ error:%@]
kDYFEMTLComputePipelineState_functionPointerHandlesWithFunctions_range
[%@ decompress:%@ size:%@ offset:%@ stagingBuffer:%@ stagingBufferSize:%@]
BaseVertex
RG16Sint
LineLoop
kDYFEMTLAccelerationStructure_resourceUsage
kDYFEMTLBlitCommandEncoder_copyIndirectCommandBuffer_sourceRange_destination_destinationIndex
kDYFEMTLDevice_newMotionEstimationPipelineWithDescriptor
kDYFEMTLVideoCommandEncoder_pushDebugGroup
MTLLibraryTypeExecutable
MTLPixelFormatASTC_5x5_sRGB
kDYFEMTLBlitCommandEncoder_copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_options
kDYFEMTLDevice_newAccelerationStructureWithSize_withDescriptor
MTLGenericBVHTypePrimitiveMotionSPI
AccelerationStructureChildren
Command Queue 0x%llx
ASTC_12x12_HDR
256
ThreadPositionInGridX
MTLIntersectionFunctionTable
kDYFEMTLComputeCommandEncoder_setBuffers_offsets_attributeStrides_withRange
kDYFEMTLRenderCommandEncoder_setTileTextures_withRange
RGBA16Snorm
MTLPixelFormatRGB10A8_2P_XR10_sRGB
MTLSourceLanguageMetal
kDYFEMTLComputeCommandEncoder_executeCommandsInBuffer_startIndex
kDYFEMTLRenderCommandEncoder_drawPrimitives_vertexStart_vertexCount_instanceCount
kDYFEMTLRenderCommandEncoder_setPrimitiveRestartEnabled
[%@ setOutputTexture:%@]
streamRef
RGBA8Sint
MTLPixelFormatYCBCR8_420_2P_sRGB
Outward
[%@ unmapShaderSampleBuffer]
[%@ newBufferWithBytesNoCopy:%@ length:%@ options:%@ atResourceIndex:%@ deallocator:%@]
MTLCommandBufferStatusScheduled
kDYFEMTLDevice_supportsFamily
Resource
MTLDynamicLibrarySerializationChecksum
MTLPixelFormatRG16Uint
OptIn
kDYFEMPSPlugin_newCNNConvolutionGradientWithDescriptor_convolutionData
kDYFEMTLAccelerationStructureCommandEncoder_endEncoding
kDYFEMTLCommandQueue_insertDebugCaptureBoundary
kDYFEMTLRenderCommandEncoder_setVertexTexture_baseLevel_atIndex
tvOS_GPUFamily2_v1
ASTC_12x10_sRGB
kDYFEMTLRenderCommandEncoder_setMeshIntersectionFunctionTables_withBufferRange
[%@ newComputePipelineStateWithDescriptor:%@ error:%@]
BufferResourceUsage
passthroughVertex
Pending
MTLPrimitiveTopologyClassTriangle
MTLPrimitiveTypeTriangleFan
MTLValidationCodeCommandQueue
kDYFEMTLFragmentRenderCommandEncoder_insertDebugSignpost
kDYFEMTLRenderCommandEncoder_pushDebugGroup
Half2
MTLPurgeableStateMakeResident
[%@ reserveResourceIndicesForResourceType:%@ indices:%@ indexCount:%@]
[%@ setColorResolveTexture:%@ slice:%@ depthPlane:%@ level:%@ yInvert:%@ atIndex:%@]
MTLPixelFormatASTC_4x2_HDR
MTLTextureRotation180DegreesClockwise
MTLCounter
Implicit
MTLDataTypeShort2
High
PerPatch
MTLTextureCompressionFeedbackUnsupportedSmallTexture
MTLVertexFormatUInt3
MTLVertexFormatUShortNormalized
kDYFEMTLCaptureManager_startCaptureWithDescriptor_error
MTLMatrixLayoutColumnMajor
MTLPrimitiveTopologyClassLine
TextureDescriptor
kDYFEMTLFXSpatialScaler_setOutputTexture
kDYFEMTLRenderCommandEncoder_setMeshBytes_length_atIndex
[%@ getBinaryDataForKey:%@]
[%@ setObjectSamplerState:%@ atIndex:%@]
MTLMultisampleDepthResolveFilterSample0
_MTLArgumentBufferResourceTypeConstant
MTLTexture
kDYFEMTLRenderCommandEncoder_textureBarrier
MTLPrecompiledDataTypeVertexReflectionData
MTLSparseTexturesTierNone
kDYFEMTLBinaryArchive_addRenderPipelineFunctionsWithDescriptor_error
kDYFEMTLCommandBuffer_addPurgedResource
kDYFEMTLCommandBuffer_dropResourceGroups_count
MTLArgumentTypeImageblock
PrivateDebugInstrumentation
MTLPixelFormatRG10Uint_PACKED
kDYFEMTLFXTemporalScaler_setJitterOffsetY
[%@ waitUntilScheduled]
MTLPatchTypeNone
kDYFEMTLCommandBuffer_encodeSignalEvent_value_agentMask
[%@ newPipelineLibraryWithFilePath:%@ error:%@]
External
MTLVertexFormatShort3Normalized
_MTLArgumentBufferResourceTypePipelineState
kDYFEMTLIntersectionFunctionTable_setBuffer_offset_atIndex
MTLPipelineOptionEnableAssertions
MTLQosLow
MTLLogState
kDYFEMTLCommandBuffer_waitUntilCompleted
kDYFEMTLDevice_maximumComputeSubstreams
%@_%lu.json
MTLWindingClockwise
Private_Bicubic
kDYFEMTLBlitCommandEncoder_updateTextureMapping_mode_indirectBuffer_indirectBufferOffset
kDYFEMTLRenderCommandEncoder_sampleCountersInBuffer_atSampleIndex_withBarrier
kDYFEMTLRenderPipelineState_newTileIntersectionFunctionTableWithDescriptor
[%@ writeGenericBVHStructureOfAccelerationStructure:%@ headerBuffer:%@ headerBufferOffset:%@ innerNodeBuffer:%@ innerNodeBufferOffset:%@ leafNodeBuffer:%@ leafNodeBufferOffset:%@ primitiveBuffer:%@ primitiveBufferOffset:%@]
[%@ setOpaqueCurveIntersectionFunctionWithSignature:%@ withRange:%@]
tvOS_5
[%@ waitUntilCompleted]
[%@ setSamplerStates:%@ withRange:%@]
[%@ removeHeap:%@]
kDYFEMTLFragmentRenderCommandEncoder_setFragmentTexture_atIndex
kDYFEMTLHeap_isPurgeable
kDYFEMTLRenderCommandEncoder_setTriangleFillMode
[%@ drawIndexedPrimitives:%@ indexCount:%@ indexType:%@ indexBuffer:%@ indexBufferOffset:%@ instanceCount:%@ baseVertex:%@ baseInstance:%@]
[%@ formattedDescription:%@]
[%@ writeGenericBVHStructureSizesOfAccelerationStructure:%@ toBuffer:%@ sizesBufferOffset:%@]
deviceStreamRef
MTLFeatureSet_iOS_GPUFamily2_v4
UnsupportedLinearLayout
kDYFEMTLBlitCommandEncoder_copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin
RGB8_444_2P
kDYFEMTLDevice_setShaderDebugInfoCaching
[%@ useResource:%@ usage:%@ stages:%@]
[%@ setOpaqueTriangleIntersectionFunctionWithSignature:%@ atIndex:%@]
[%@ removeAllResources]
MTLGPUFamilyApple8
kDYFEMTLBuffer_contents
kDYFEMTLBuffer_removeAllDebugMarkers
[%@ resourceStateCommandEncoder]
MTLDataTypeChar8
MTLStepFunctionThreadPositionInGridYIndexed
kDYFEMTLBinaryArchive_addTileRenderPipelineFunctionsWithDescriptor_options_error
kDYFEMTLComputeCommandEncoder_useHeaps_count
.xy
MTLPixelFormatRGBX16Uint
MTLPixelFormatFlagsIsULongCompatible
MTLPrecompiledDataTypeTileFunction
Right
kDYFECAMetalDrawable_present
<%@: %p %@>
MTLDataTypeLong8
MTLLogicOpNand
MTLPixelFormatRGB10_444_2P
Pow2
kDYFEMTLAccelerationStructure_gpuResourceID
IgnorePlatformValidation
MTLDynamicLibraryEnableResourcePatchingInstrumentation
MTLFeatureSet_iOS_GPUFamily2_v2
MTLPixelFormatYCBCR10_420_2P_PACKED_HLG
YCBCR12_422_2P_HLG
[%@ encodeToCommandBuffer:%@ computeCommandEncoder:%@ options:%@ pluginOptions:%@ sourceTexture:%@ sourceInfo:%@ destinationTexture:%@ destinationInfo:%@ ]
UChar2
MTLBindingAccessReadOnly
MTLPixelFormatBC5_RGUnorm
TriangleFan
MTLStoreActionStore
kDYFEMTLAccelerationStructureCommandEncoder_setLabel
kDYFEMTLDevice_loadDynamicLibrariesForFunction_insertLibraries_options_error
ASTC_8x8_HDR
MTLPixelFormatDepth32Float_Stencil8
MTLPixelFormatRGB10A8_2P_sRGB
MTLRenderStageObject
kDYFEMTLIOCommandBuffer_setStatus
[%@ compileVisibleFunction:%@ withDescriptor:%@ completionHandler:%@]
RenderPiplineAllocatedSize
MTLAttribute
AlreadyCapturing
kDYFEMTLResidencySet_containsResource
ThreadgroupsPerGrid
CatmullRom
tvOS_GPUFamily1_v2
kDYFEMTLDevice_supportsTextureSampleCount
kDYFEMTLRenderCommandEncoder_setStencilResolveTexture_slice_depthPlane_level
kDYFEMTLRenderCommandEncoder_setVertexBuffer_offset_atIndex
MTLResourceStorageModePrivate
kDYFEMTLFragmentRenderCommandEncoder_drawTrianglesWithPositions_vertexCount_vertexVaryings_varyingCountPerVertex
kDYFEMTLIndirectComputeCommand_setImageblockWidth_height
kDYFEMTLRenderCommandEncoder_setObjectTexture_atIndex
kDYFEMTLTexture_newTextureViewWithPixelFormat
Float2x4
MTLPixelFormatBC7_RGBAUnorm_sRGB
MTLPixelFormatYCBCR12_422_2P_PACKED_PQ
kDYFEMTLRenderCommandEncoder_setVisibilityResultMode_offset
uint4
name
CiSulbbulb
AtDrawBoundary
MTLPixelFormatRGBA16Float
iOS_10
kDYFEMTLDevice_createNewUtilityBuffer
MTLAttributeFormatUCharNormalized
ASTC_5x5_sRGB
MTLVREyeRight
[%@ useDeviceResourceTableForType:%@]
tex.sample(samp, in.uv)
MTLCompareFunctionNotEqual
MTLPixelFormatYCBCR10_444_2P_PACKED_XR
MTLShaderValidationDisabled
kDYFEMTLBuffer_makeAliasable
kDYFEMTLRenderCommandEncoder_useRenderPipelineState
[%@ encodeEndDoWhile:%@ offset:%@ comparison:%@ referenceValue:%@]
MTLBlendFactorSourceAlpha
MTLBuiltInArgumentPatchID
ASTC_10x5_HDR
kDYFEMTLRenderCommandEncoder_setTileSamplerState_lodMinClamp_lodMaxClamp_atIndex
[%@ addScheduledHandler:%@]
[%@ newBufferWithDescriptor:%@]
LoadSkipAIRValidation
Inward
kDYFEMTLDevice_newVisibleFunctionTableWithDescriptor
VisibleFunctionTableAllocatedSize
kDYFEMPSExternalMatrixMultiplication_encodeToCommandBuffer_encoder_options_batchSize_resultRowsAndResultColumnsAndInteriorColumns_alphaAndBeta_A_aInfo_B_bInfo_C_cInfo_predicationBuffer_predicationOffset
kDYFEMTLAccelerationStructure_doesAliasResource
kDYFEMTLRenderCommandEncoder_setStencilResolveTexture_slice_depthPlane_level_yInvert
[%@ minimumTextureBufferAlignmentForPixelFormat:%@]
MTLBuiltInArgumentThreadIndexInThreadgroup
ASTC_10x8_HDR
MTLPixelFormatFlagsIsFilterable
Repeat
[%@ setObjectSamplerStates:%@ withRange:%@]
[%@ setEmulationMeshSize:%@]
kDYFEMTLArgumentEncoder_setFunctionTables_withRange
kDYFEMTLDevice_newTextureWithDescriptor_iosurface_plane
kDYFEMTLIndirectRenderCommand_setTileArgument_offset_atIndex
[%@ newRasterizationRateMapWithScreenSize:%@ layerCount:%@ layers:%@]
MTLDynamicLibraryEnableResourceUsageInstrumentation
MTLPrecompiledDataTypeVertexFunction
ShaderRead
kDYFEMTLArgumentEncoder_dealloc
kDYFEMTLDevice_newSharedEventWithOptions
kDYFEMTLRenderCommandEncoder_setMeshVisibleFunctionTables_withBufferRange
[%@ synchronizeTexture:%@ slice:%@ level:%@]
[%@ encodeStartIf:%@ offset:%@ comparison:%@ referenceValue:%@]
NilBinding
MTLDataTypeHalf4x2
MTLDeviceLocationUnspecified
kDYFEMTLRenderCommandEncoder_setFragmentBuffer_offset_atIndex
MTLRenderMeshBuiltInBinding
MTLCompareFunctionEqual
MTLPixelFormatRGB10_422_2P_PACKED
MTLTessellationFactorStepFunctionPerInstance
kDYFEMTLDevice_newBufferWithLength_options
kDYFEMTLDevice_newFunctionWithGLCoreIR_inputsDescription_functionType
kDYFEMTLIOHandle_getHandleOffset_offset
kDYFEMTLIndirectComputeCommand_setImageBlockWidth_height
kDYFEMTLParallelRenderCommandEncoder_setStencilStoreAction
kDYFEMTLRenderCommandEncoder_executeCommandsInBuffer_startIndex
MTLDataTypeUInt
CustomStart
Enabled
[%@ reserveGPUAddressRange:%@]
[%@ invalidateCompressedTexture:%@ slice:%@ level:%@]
[%@ newFragmentIntersectionFunctionTableWithDescriptor:%@]
PVRTC_RGBA_4BPP
kDYFEMTLSharedEvent_waitUntilSignaledValue_timeoutMS
DebugError
PrivateZeroOutFragmentShaderRTAI
BT601Full
ArgumentEncoder
kDYFEMTLArgumentEncoder_setComputePipelineState_atIndex
[%@ supportsSampleCount:%@]
[%@ newFunctionWithGLESIR:%@ functionType:%@]
PrivateIndirectCommandBuffer
MTLPixelFormatYCBCR12_420_2P_XR
kDYFEMTLFunctionPointerHandle_dealloc
kDYFEMTLPipelineCache_dealloc
[%@ refitAccelerationStructure:%@ descriptor:%@ destination:%@ scratchBuffer:%@ scratchBufferOffset:%@]
[%@ setStatus:%@]
ContinueCommandBuffer
VisibleFunctionTableGPUAddress
MTLDataTypeBFloat16
MTLTextureSwizzleAlpha
kDYFEMTLDevice_newRenderPipelineStateWithTileDescriptor_options_completionHandler
kDYFEMTLFunction_dealloc
kDYFEMTLRenderCommandEncoder_setVertexBytes_length_atIndex
[%@ memoryBarrierWithScope:%@]
[%@ newSharedEventWithMachPort:%@]
MTLBlendFactorBlendColor
MTLCPUCacheModeDefaultCache
[%@ setTexture:%@ atIndex:%@]
[%@ removeComputePipelineFunctionsWithDescriptor:%@ error:%@]
[%@ newCNNSoftMax]
MTLPixelFormatR16Unorm
YCBCR10_422_2P_sRGB
IsIntCompatible
MTLPrecompiledDataTypeFragmentFunction
[%@ setFrontFacingWinding:%@]
Float3
MTLDataTypeDouble
kDYFEMTLAccelerationStructure_setLabel
[%@ newVisibleFunctionTableWithDescriptor:%@]
v32@?0@\"NSString\"8@16^B24
Green
MTLDataTypeShort
MTLDataTypeULong4
X32_Stencil8
kDYFEMTLDevice_newRasterizationRateMapWithScreenSize_layerCount_layers
kDYFEMTLIOHandle_readIntoStagingBuffer_offset_stagingBuffer_stagingBufferSize
MTLComputeBuiltinArgument
MTLDataTypeSampler
DrawMeshThreads
MTLPixelFormatRGB10A2Unorm
kDYFEMTLDevice_heapAccelerationStructureSizeAndAlignWithSize
0
kDYFEMTLHeap_dealloc
kDYFEMTLResourceStateCommandEncoder_updateTextureMapping_mode_indirectBuffer_indirectBufferOffset
[%@ textureBarrier]
MTLBlendOperationSubtract
ImageBlock
iOS_GPUFamily1_v3
IsFilterable
kDYFEMTLCommandQueue_getBackgroundGPUPriority
kDYFEMTLRenderCommandEncoder_setTileSamplerStates_withRange
[%@ setImageblockWidth:%@ height:%@]
[%@ stagingBufferSize:%@ offset:%@]
MTLPixelFormatASTC_12x12_HDR
kDYFEMTLVisibleFunctionTable_uniqueIdentifier
[%@ startCaptureWithDevice: %@]
[%@ loadBuffer:%@ offset:%@ size:%@ handle:%@ handleOffset:%@]
[%@ setBuffer:%@ offset:%@ attributeStride:%@ atIndex:%@]
Clamp
tvOS_3
RealTime
BGRA10Unorm_PACKED
MTLPixelFormatRGB9E5Float
MTLPixelFormatYCBCR10_444_2P_PQ
kDYFEMTLAccelerationStructureCommandEncoder_writeCompactedAccelerationStructureSize_toBuffer_offset
kDYFEMTLDevice_newLibraryWithData_error
MTLPixelFormatASTC_6x5_sRGB
MTLPixelFormatRGBA32Sint
RGBX8Unorm
kDYFEMTLIndirectComputeCommand_setKernelArgument_offset_atIndex
[%@ loadBytes:%@ size:%@ sourceHandle:%@ sourceHandleOffset:%@]
HeapCurrentAllocatedSize
[%@ encodeBatchToCommandBuffer:%@ computeCommandEncoder:%@ options:%@ sourceTextures:%@ sourceInfo:%@ destinationTextures:%@ destinationInfo:%@ zeroPadSizeX:%@ zeroPadSizeY:%@ predicationBuffer:%@ predicationOffset:%@ ]
MTLArgumentTypePrivateMesh
YCBCR12_422_2P_PACKED_PQ
Event
kDYFECAMetalLayer_setBounds_contentsScale
kDYFEMTLHeap_newBufferWithLength_options_atOffset
[%@ newPrecompiledRenderPipelineStateWithDescriptor:%@ options:%@ pipelineCache:%@ completionHandler:%@]
MTLCaptureDestinationDeveloperTools
CustomSampleDepthStore
kDYFEMTLAccelerationStructureCommandEncoder_deserializeInstanceAccelerationStructure_primitiveAccelerationStructures_fromBuffer_serializedBufferOffset_withDescriptor
[%@ setVisibilityResultMode:%@ offset:%@]
[%@ requiresIndirectionForAllResourceTypes]
[%@ encodeBatchToCommandBuffer:%@ computeCommandEncoder:%@ options:%@ pluginOptions:%@ sourceTextures:%@ sourceInfo:%@ destinationTextures:%@ destinationInfo:%@ predicationBuffer:%@ predicationOffset:%@ ]
Random
MTLTextureSwizzleZero
kDYFEMTLIOCommandBuffer_signalEvent_value
[%@ addBufferToGlobalResourceTable:%@]
[%@ loadBuffer:%@ offset:%@ size:%@ sourceHandle:%@ sourceHandleOffset:%@]
[%@ useResidencySet:%@]
DecrementWrap
kDYFEMTLBuffer_invalidateRange
MTLBarrierScopeTextures
kDYFEMTLRenderPipelineState_uniqueIdentifier
[%@ supportsTextureWriteFPRoundingMode:%@]
MTLBufferRobustnessSupportInvalidAccess
SupportRollback
MTLPixelFormatR32Float
MTLPixelFormatYCBCR10_420_2P_PACKED_XR
MTLRenderBuiltinVertexArgument
MTLImageFilterFunctionArgumentTypeOutputSPI
RGBX32Float
MTLShaderValidationEnabled
kDYFECAMetalLayer_setDevice
[%@ copyFromTexture:%@ toTexture:%@]
library
MTLIntersectionFunctionSignatureNone
MTLTessellationControlPointIndexTypeUInt16
[%@ setDepthStencilState:%@]
MTLAttributeFormatHalf4
EAC_RGBA8_sRGB
YCBCR12_444_2P
Int4
MTLDataTypeTexture
Counting
kDYFEMTLTexture_isAliasable
[%@ addDebugMarker:%@ range:%@]
[%@ deserializePrimitiveAccelerationStructure:%@ fromBuffer:%@ serializedBufferOffset:%@ withDescriptor:%@]
PrivateRenderPipeline
kDYFEMTLVisibleFunctionTable_doesAliasAllResources_count
MTLAccelerationStructureInstanceOptionOpaque
MTLArgumentTypePrivatePointer
MTLFeatureSet_iOS_GPUFamily1_v1
MTLRoundingModeRTNE
MTLValidationCodeEvent
[%@ setDepthStoreAction:%@]
MetalPluginName
MTLIOErrorURLInvalid
MTLPurgeableStateEmpty
kDYFEMTLAccelerationStructureCommandEncoder_useHeap
[%@ encodeCacheControlTagOperation:%@ resourceGroups:%@ count:%@]
[%@ newAccelerationStructureWithBuffer:%@ offset:%@]
MTLAccelerationStructureUsagePrivateDeterministicBuild
MTLGPUOperationAtomicStore
MTLHazardTrackingModeDefault
MTLPixelFormatRGBA16Float_XR
_MTLArgumentBufferResourceTypeVisibleFunctionTable
kDYFEMTLComputeCommandEncoder_setTexture_atIndex
kDYFEMTLDevice_newBufferWithBytes_length_options
[%@ newDynamicLibrary:%@ error:%@]
MTLTextureCompressionFeedbackUnsupportedTextureUsagePixelFormatView
kDYFEMTLRenderCommandEncoder_setRenderPipelineState
Float4
MTLCounterSet
kDYFEMTLSamplerState_uniqueIdentifier
[%@ newBufferWithBytesNoCopy:%@ length:%@ options:%@ gpuAddress:%@ deallocator:%@]
MTLBlendFactorSourceColor
Always
kDYFEMTLDevice_deserializeInstanceAccelerationStructure_fromBytes_primitiveAccelerationStructures_withDescriptor
[%@ newVisibleFunctionTableFromFragmentStageWithDescriptor:%@]
MTLColorWriteMaskNone
Half4x4
kDYFEMTLCommandQueue_commandBufferWithUnretainedReferences
kDYFEMTLEvent_dealloc
kDYFEMTLParallelRenderCommandEncoder_insertDebugSignpost
kDYFEMTLVisibleFunctionTable_setGlobalBufferOffset
AtomicFetchAnd
MTLHazardTrackingModeUntracked
MTLVertexFormatShortNormalized
kDYFEMTLRenderCommandEncoder_setColorStoreAction_atIndex
[%@ commitAndWaitUntilSubmitted]
TriangleFrontFacingWindingCounterClockwise
Timeout
MTLDataTypeBFloat3x2
MTLDataTypeHalf4
BC4_RSnorm
MTLTextureColorSpaceConversionMatrixBT2020Full
kDYFEMTLTexture_newTextureViewWithPixelFormat_resourceIndex
[%@ useHeap:%@]
MTLAttributeFormatShort2
UShort8
MTLPixelFormatYCBCR12_444_2P_PACKED_XR
IsWriteable
InsertMemoryBarrier
kDYFEMTLRenderCommandEncoder_setFragmentSamplerState_atIndex
MTLCounterSampleBufferErrorInvalid
Precise
BC5_RGSnorm
MTLVertexFormatUShort
kDYFECAMetalLayer_nextDrawable
kDYFEMTLAccelerationStructure_children
kDYFEMTLBlitCommandEncoder_synchronizeTexture_slice_level
kDYFEMTLCounter_dealloc
R16Float
kDYFEMTLDevice_newComputePipelineStateWithDescriptor_completionHandler
kDYFEMTLTexture_containsResource
[%@ setResourceIndirectionEnabled:%@]
[%@ loadTexture:%@ slice:%@ level:%@ size:%@ sourceBytesPerRow:%@ sourceBytesPerImage:%@ destinationOrigin:%@ sourceHandle:%@ sourceHandleOffset:%@]
UShortNormalized
MTLPixelFormatA1BGR5Unorm
ASTC_4x4_HDR
kDYFEMTLBuffer_didModifyRange
[%@ invalidateRange:%@]
1
MTLPipelineOptionPrivateFailOnFSCacheMiss
ASTC_5x4_LDR
kDYFEMTLRasterizationRateMap_formattedDescription
com.apple.CoreImage
kDYFEMTLDevice_setIndirectArgumentBufferDecodingData
kDYFEMTLBinaryArchive_addMeshRenderPipelineFunctionsWithDescriptor_error
kDYFEMTLDevice_addIndirectCommandBufferToGlobalResourceTable
kDYFEMTLFXTemporalScaler_setMotionVectorScaleX
kDYFEMTLIndirectRenderCommand_setThreadgroupMemoryLength_offset_atIndex
kDYFEMTLRenderCommandEncoder_drawMeshThreadgroups_threadsPerObjectThreadgroup_threadsPerMeshThreadgroup
[%@ newLibraryWithCIFiltersForComputePipeline:%@ imageFilterFunctionInfo:%@ error:%@]
EnableResourceUsageInstrumentation
Keep
kDYFEMTLLibrary_newExternFunctionWithName
[%@ encodeToCommandBuffer:%@ encoder:%@ options:%@ batchSize:%@ inputMatrix:%@ inputMatrixInfo:%@ weightMatrix:%@ weightMatrixInfo:%@ biasVector:%@ biasVectorInfo:%@ resultMatrix:%@ resultMatrixInfo:%@ alpha:%@ numberOfFeatureVectors:%@ inp
MTLArgumentImageBlockKindPrivateExplicit
MTLBufferRobustnessSupportNilBinding
Bool2
MTLFeatureSet_iOS_GPUFamily4_v1
MTLPixelFormatASTC_12x10_sRGB
PVRTC_RGBA_2BPP_sRGB
kDYFEMTLAccelerationStructureCommandEncoder_writeGeometryOfAccelerationStructure_toBuffer_geometryBufferOffset
kDYFEMTLDevice_newProfileWithExecutionSize
macOS_1
MTLPixelFormatYCBCR10_422_2P_PACKED_sRGB
MTLTagTypeInstancing
kDYFEMTLRenderCommandEncoder_setObjectSamplerStates_lodMinClamps_lodMaxClamps_withRange
[%@ newSharedHandle]
MTLAllocationTypeUnknown
MTLLoadActionDontCare
RG8Uint
kDYFEMTLBinaryArchive_getArchiveIDWithError
kDYFEMTLIOCommandBuffer_waitForEvent_value
[%@ removeHeaps:%@ count:%@]
[%@ encodeSignalEventScheduled:%@ value:%@]
PrivateComputePipeline
MTLBlendFactorOneMinusSource1Alpha
ULong16
MTLFeatureSet_macOS_GPUFamily2_v1
MTLPixelFormatBGRA10Unorm_PACKED_sRGB
kDYFEMPSExternalMatrixMultiplication_encodeToCommandBuffer_encoder_options_batchSize_A_aInfo_B_bInfo_C_cInfo
kDYFEMTLIndirectComputeCommand_setThreadgroupMemoryLength_atIndex
[%@ newFunctionWithGLCoreIR:%@ functionType:%@]
MTLBuiltInArgumentThreadExecutionWidth
MTLGenericBVHPrimitiveTypeCurveSPI
YCBCR12_420_2P_PACKED_XR
MTLResourceCPUCacheModeDefaultCache
LibraryType
ASTC_10x10_sRGB
MTLPixelFormatEAC_RG11Snorm
MTLPixelFormatYCBCR10_444_2P_PACKED_HLG
kDYFEMTLBinaryLibrary_getBinaryDataWithKey
kDYFEMTLIndirectCommandBuffer_isComplete
[%@ newVisibleFunctionTableFromVertexStageWithDescriptor:%@]
[%@ copyStatusToBuffer:%@ offset:%@]
uint
MTLDataTypeBFloat2x4
DepthStencilState
Apple8
[%@ newSamplerStateWithDescriptor:%@]
[%@ newRenderPipelineDescriptorWithSerializedData:%@ deserializationContext:%@]
[%@ isComplete]
[%@ newTileIntersectionFunctionTableWithDescriptor:%@]
defaultSamplePositions
MTLAttributeFormatFloatRGB9E5
[%@ newCNNPoolingMaxWithKernelWidth:%@ kernelHeight:%@ strideInPixelsX:%@ strideInPixelsY:%@ ]
MTLBinaryArchiveSerializationSpecializedFunctionsAspectIfAvailable
LoadVertexAttributeData
MTLDataTypeHalf3x2
ForcedManually
kDYFEMTLAccelerationStructureCommandEncoder_insertDebugSignpost
kDYFEMTLDevice_newSharedEvent
kDYFEMTLRenderCommandEncoder_drawMeshThreads_threadsPerObjectThreadgroup_threadsPerMeshThreadgroup
command-queues
MTLPixelFormatYCBCR12_422_2P_XR
MTLValidationCodePipelineState
kDYFEMTLAccelerationStructureCommandEncoder_writeSerializedAccelerationStructureSize_toBuffer_offset
kDYFEMTLFunction_newArgumentEncoderWithBufferIndex_reflection_pipelineLibrary
canBeCaptured
MTLDataTypeChar16
MTLPipelineOptionBindingInfo
MTLPipelineOptionPrivateFunctionWithNoReflection
Map
DescriptorAspectIfAvailable
PatchID
BFloat
Double16
MTLGPUFamilyApple3
AllowBadLegacyDAGs
[%@ functionHandleWithFunction:%@ stage:%@]
MTLPixelFormatRG16Bfloat
kDYFEMTLCommandBuffer_resourceStateCommandEncoder
kDYFEMTLDevice_newArgumentEncoderWithArguments
[%@ setShouldMaximizeConcurrentCompilation:%@]
MTLDashboardStreamingCodec
kDYFEMTLCaptureManager_newCaptureScopeWithCommandQueue
[%@ newIndirectComputeCommandEncoderWithBuffer:%@]
VisibleFunctionTableGPUResourceID
scopeStreamRef
MTLDataTypeChar
1_1
MTLSparseTextureMappingModeMap
kDYFEMTLAccelerationStructureCommandEncoder_writeCompactedAccelerationStructureSize_toBuffer_offset_sizeDataType
kDYFEMTLCommandBuffer_resourceStateCommandEncoderWithDescriptor
kDYFEMTLDevice_newAccelerationStructureWithBuffer_offset_resourceIndex
kDYFEMTLDevice_newHeapWithDescriptor
[%@ setMotionVectorScaleX:%@]
OneMinusBlendColor
MTLDataTypeFloat3x4
iOS_GPUFamily2_v3
Raytracing2024
And
Set
[%@ commitAndWaitUntilSubmittedWithDeadline:%@]
YCBCR10_444_2P_PQ
[%@ deserializeInstanceAccelerationStructure:%@ primitiveAccelerationStructures:%@ fromBuffer:%@ serializedBufferOffset:%@ withDescriptor:%@]
CiSululuiululululbb
MTLIntersectionFunctionSignatureMaxLevels
3_2
MTLPixelFormatASTC_8x6_HDR
BGRA10Unorm_PACKED_sRGB
kDYFEMPSExternalCNNPoolingAverage_encodeToCommandBuffer_computeCommandEncoder_options_sourceTexture_sourceInfo_destinationTexture_destinationInfo_zeroPadSizeX_zeroPadSizeY
kDYFEMTLRenderCommandEncoder_setObjectAccelerationStructure_atBufferIndex
[%@ newTextureViewWithPixelFormat:%@ textureType:%@ levels:%@ slices:%@ swizzle:%@ resourceIndex:%@]
ThreadPositionInGrid
iOS_GPUFamily2_v4
MTLLanguageVersion3_1
RGB10_420_2P_PACKED
MTLPixelFormatYCBCR10_444_2P_sRGB
MPSExternalCNNConvolutionGradient
[%@ optimizeIndirectCommandBuffer:%@ withRange:%@]
texturedQuadFragmentDepth
%@
SkipStageInputLoading
MTLLogLevelDebug
MTLStoreActionDontCare
RenderPassDescriptor
kDYFEMPSExternalMatrixMultiplication_encodeToCommandBuffer_encoder_options_batchSize_resultRows_resultColumns_interiorColumns_alpha_beta_A_aInfo_B_bInfo_C_cInfo_predicationBuffer_predicationOffset
kDYFEMTLIntersectionFunctionTable_setFunction_atIndex
MTLFeatureSet_iOS_GPUFamily1_v3
[%@ addComputePipelineStateWithDescriptor:%@ error:%@]
[%@ setEmulationObjectShaderIntermediateBufferSlot:%@]
[%@ newCNNPoolingAverageWithKernelWidth:%@ kernelHeight:%@ strideInPixelsX:%@ strideInPixelsY:%@ ]
NewSamplerState
InstanceAccelerationStructure
MTLCompareFunctionNever
MTLPixelFormatRG8Uint
UnsupportedPixelFormat
MTLArgumentTypeThreadgroupMemory
MTLBlendFactorSourceAlphaSaturated
RGB10A8Uint_2P
MTLPixelFormatYCBCR12_444_2P_PACKED_PQ
kDYFEMTLDevice_copyShaderCacheToPath
kDYFEMTLDevice_newSharedTextureWithHandle
kDYFEMTLLibrary_newFunctionWithName_constantValues_error
Apple6
ConcurrentDispatch
MTLPixelFormatEAC_RG11Unorm
CounterClockwise
kDYFEMTLBuffer_allocationID
kDYFEMTLComputeCommandEncoder_waitForProgress
kDYFEMTLParallelRenderCommandEncoder_endEncoding
MTLDataTypeFloat4x4
MTLLogLevelError
MTLPixelFormatA8Unorm
MTLPixelFormatASTC_10x8_sRGB
MTLStencilOperationInvert
UIScreen
kDYFEMTLCommandBuffer_encodeSignalEventScheduled_value
[%@ updateFence:%@ afterStages:%@]
GreaterThan
MTLDataTypeShort4
kDYFEMTLHeap_newAccelerationStructureWithSize_offset_resourceIndex
[%@ isShareable]
[%@ addResidencySet:%@]
Nearest
MTLStencilOperationIncrementClamp
MTLTagTypeExtendedLimits
kDYFEMTLAccelerationStructureCommandEncoder_refitAccelerationStructure_descriptor_destination_scratchBuffer_scratchBufferOffset
kDYFEMTLAccelerationStructureCommandEncoder_updateFence
kDYFEMTLRenderCommandEncoder_setVertexBuffers_offsets_attributeStrides_withRange
kDYFEMTLVisibleFunctionTable_allocationID
[%@ setVertexIntersectionFunctionTable:%@ atBufferIndex:%@]
MTLBlendFactorZero
MTLDataTypeRGBA16Snorm
MTLPixelFormatYCBCR8_422_1P_REV
MTLVertexStepFunctionConstant
kDYFEMTLIOHandle_decompress_size_offset_stagingBuffer_stagingBufferSize
kDYFEMTLResidencySet_addHeap
[%@ setListIndex:%@]
MTLLogicOperationNoop
MTLPixelFormatASTC_10x10_HDR
vertex shader key
MTLRenderStageVertex
kDYFEMTLResidencySet_countForHeap
[%@ newLibraryWithDescriptor:%@ completionHandler:%@]
MTLCommandBufferStatusNotEnqueued
kDYFEMTLArgumentEncoder_setVisibleFunctionTables_withBufferRange
kDYFEMTLDevice_newLibraryWithStitchedDescriptor_completionHandler
kDYFEMTLResourceStateCommandEncoder_updateTextureMappings_mode_regions_mipLevels_slices_numRegions
[%@ setGPUPriority:%@ offset:%@]
macOS_GPUFamily1_v2
kDYFEMTLAccelerationStructureCommandEncoder_writeDeserializedAccelerationStructureSize_serializedOffset_toBuffer_sizeBufferOffset
kDYFEMTLIndirectRenderCommand_dispatchThreadsPerTile
kDYFEMTLTexture_replaceRegion_mipmapLevel_slice_withBytes_bytesPerRow_bytesPerImage
MTLPixelFormatYCBCR10_422_2P
kDYFEMTLFragmentRenderCommandEncoder_setDepthStencilState
[%@ setCurrentUtilityBufferIndex:%@]
UInt_InstanceID
FractionalOdd
[%@ setIntersectionFunctionTables:%@ withRange:%@]
[%@ setMeshSamplerState:%@ lodMinClamp:%@ lodMaxClamp:%@ atIndex:%@]
Greedy
kDYFEMTLAccelerationStructure_allocatedSize
Hidden
MTLCompilerFlagIgnorePlatformValidation
[%@ setVertexBuffer:%@ offset:%@ attributeStride:%@ atIndex:%@]
Common3
MTLValidationCodeIndirectCommandBuffer
ResourceStateCommandEncoder
kDYFEMTLAccelerationStructureCommandEncoder_pushDebugGroup
kDYFEMTLDevice_deserializeInstanceAccelerationStructureFromBytes_primitiveAccelerationStructures_withDescriptor
kDYFEMTLIndirectRenderCommand_setFragmentArgument_offset_atIndex
[%@ createNewUtilityBuffer]
[%@ writeDeserializedPrimitiveAccelerationStructureSizes:%@ serializedOffset:%@ toBuffer:%@ sizesBufferOffset:%@]
air.position
MTLDataTypeShort3
kDYFEMTLCaptureManager_stopCapture
[%@ copyFromBuffer:%@ sourceOffset:%@ sourceBytesPerRow:%@ sourceBytesPerImage:%@ sourceSize:%@ toTexture:%@ destinationSlice:%@ destinationLevel:%@ destinationOrigin:%@]
[%@ setExecutionEnabled:%@]
[%@ commandBufferWithDescriptor:%@]
InstanceSPI
MTLSamplerAddressModeClampToEdge
MTLVertexFormatHalf4
MTLIOCommandBuffer
kDYFEMTLAccelerationStructureCommandEncoder_writeDeserializedPrimitiveAccelerationStructureSizes_serializedOffset_toBuffer_sizesBufferOffset
kDYFEMTLIOCommandBuffer_tryCancel
[%@ flushTexture:%@ slice:%@ mipmapLevel:%@]
YCBCR10_420_2P_PACKED_HLG
MTLStepFunctionPerInstance
MTLTessellationPartitionModePow2
kDYFEMTLCommandQueue_setBackgroundGPUPriority
kDYFEMTLDevice_setResourceIndirectionEnabled
kDYFEMTLRenderCommandEncoder_setTileIntersectionFunctionTables_withBufferRange
kDYFEMTLResidencySet_removeAllocation
[%@ setIntersectionFunctionTable:%@ atBufferIndex:%@]
Count
MTLPixelFormatB5G6R5Unorm
[%@ encodeStartElse]
AccelerationStructureCommandEncoderSetAccelerationStructureChildren
MTLRenderObjectBuiltInBinding
Medium
MTLPixelFormatYCBCR10_444_2P_PACKED_PQ
MTLPixelFormatYCBCR8_422_1P
kDYFEMTLDevice_newLibraryWithSource_options_completionHandler
AccelerationStructureResourceUsage
MTLDeviceFeatureProfileiOS_9
PrivateForceLateReflection
RGB10A2Unorm_PQ
[%@ setDisableRunTimeCompilation:%@]
[%@ encodeToCommandBuffer:%@ encoder:%@ options:%@ batchSize:%@ resultRows:%@ resultColumns:%@ interiorColumns:%@ alpha:%@ beta:%@ A:%@ aInfo:%@ B:%@ bInfo:%@ C:%@ cInfo:%@ predicationBuffer:%@ predicationOffset:%@ transA:%@ transB:%@ ]
MTLCounterSampleBufferErrorInternal
BSpline
MTLImageFilterFunctionArgumentTypeImageBlockSPI
MTLPixelFormatASTC_10x6_HDR
MTLPixelFormatRGBA8Snorm
Left
[%@ insertDebugSignpost:%@]
InstanceID
MTLPixelFormatFlagsIsDepthRenderable
NSHMDMetalSession
kDYFEMTLFXSpatialScaler_dealloc
kDYFEMTLResidencySet_containsHeap
kDYFEUIScreen_setInterfaceOrientation
[%@ setStencilReferenceValue:%@]
[%@ concurrentDispatchThreads:%@ threadsPerThreadgroup:%@]
MTLAccelerationStructureRefitOptionVertexData
PPAttrib
R32Float
[%@ setFunctionTables:%@ withRange:%@]
[%@ setValue:%@ atIndex:%@]
MTLDeviceFeatureProfilemacOS_3
kDYFEMTLAccelerationStructureCommandEncoder_deserializeAccelerationStructure_fromBuffer_offset
kDYFEMTLRenderCommandEncoder_setTileTexture_atIndex
kDYFEMTLTexture_allocatedSize
kDYFEMTLVideoCommandEncoder_generateMotionVectorsForTexture_previousTexture_resultBuffer_bufferOffset
[%@ newVisibleFunctionTableFromMeshStageWithDescriptor:%@]
[%@ addHeaps:%@ count:%@]
[%@ encodeToCommandBuffer:%@ computeCommandEncoder:%@ options:%@ sourceTexture:%@ sourceInfo:%@ destinationTexture:%@ destinationInfo:%@ ]
UShort3Normalized
NotEnqueued
iOS_GPUFamily3_v1
_MTLArgumentBufferPatchingTypeIndexed
kDYFEMTLRenderCommandEncoder_setFragmentVisibleFunctionTables_withBufferRange
kDYFEMTLRenderPipelineState_fragmentFunctionHandleWithFunction
[%@ generationForHeap:%@]
MTLCommandBufferWaitForEventFulfilled
iOS_2
MTLDeviceFeatureProfileiOS_8
MTLGenericBVHHeaderVersionUniqueIdentifier
MTLIndirectCommandTypeDraw
MTLMathModeSafe
BC2_RGBA
kDYFEMTLFXTemporalScaler_dealloc
kDYFEMTLFXTemporalScaler_setPreExposure
MTLDataTypeUShort16
R8Unorm_sRGB
MTLPixelFormatRGBA16Snorm
MTLTextureSwizzleShiftGreen
kDYFEMTLComputeCommandEncoder_useComputePipelineState
kDYFEMTLVisibleFunctionTable_setResponsibleProcess
[%@ physicalCoordinate:%@ forLayer:%@]
subtype
MTLAllocationTypeResource
_MTLMachOTypeAppleGPU
kDYFEMTLBinaryLibrary_removeComputePipelineFunctionsWithDescriptor_error
kDYFEMTLBuffer_newTextureWithDescriptor_offset_bytesPerRow
kDYFEMTLDevice_pollSampleBuffer_resolvedBuffer
kDYFEMTLIndirectCommandBuffer_isAliasable
RestoreMTLTextureIOSurfaceDataForPlane
CiSululuiulbulb
MTLDataTypeRGB9E5Float
MTLGPUPriorityDisabled
MTLIndirectCommandTypeDrawIndexed
MTLLibraryTypeDynamic
ComputePipelineDescriptor
kDYFEMTLRenderCommandEncoder_setVertexSamplerState_atIndex
[%@ indirectArgumentBufferDecodingData]
IsFloatCompatible
kDYFEMTLBuffer_gpuVirtualAddress
kDYFEMTLDevice_serializeStructType_version
kDYFEMTLRasterizationRateMap_mapScreenToPhysicalCoordinates_forLayer
[%@ loadDynamicLibrariesForComputeDescriptor:%@ error:%@]
[%@ newAccelerationStructureWithSize:%@ resourceIndex:%@]
AccelerationStructureTimeSinceTouched
MaxLevels
MTLDynamicLibraryInstallName
MTLDynamicLibraryExportedFunction
MTLPixelFormatYCBCR10_444_2P_XR
kDYFEMTLRenderCommandEncoder_drawPrimitives_indirectBuffer_indirectBufferOffset
[%@ setDepthResolveTexture:%@ slice:%@ depthPlane:%@ level:%@]
[%@ fillTexture:%@ level:%@ slice:%@ region:%@ color:%@ pixelFormat:%@]
[%@ harvestedNewBufferWithBytes:%@ length:%@ options:%@]
Curve
kDYFEMTLVisibleFunctionTable_setValue_atIndex
MTLPixelFormatASTC_12x12_LDR
AcelerationStructureCommandEncoder
MTLFXTemporalScalerVersion_End
[%@ setRawBVHBuilderPtr:%@]
kDYFEMTLFXSpatialScaler_setColorTexture
[%@ setGlobalBufferOffset:%@]
MTLArgumentTypeIntersectionFunctionTable
BFloat3
UnsupportedSmallTexture
_MTLArgumentBufferPatchingTypeNone
kDYFEMTLCommandBuffer_commit
kDYFEMTLDevice_newPrecompiledComputePipelineStateWithDescriptor_options_pipelineCache_completionHandler
ULong2
MTLGPUPriorityRealTime
kDYFEMTLDevice_newDynamicLibraryWithURL_error
kDYFEMTLLibrary_newIntersectionFunctionWithDescriptor_completionHandler
[%@ useResources:%@ count:%@ usage:%@]
[%@ newSharedTextureWithDescriptor:%@]
MTLDeviceFeatureProfileiOS_7
Object
CommandQueue
kDYFEMTLAccelerationStructure_timeSinceTouched
kDYFEMTLCommandBuffer_accelerationStructureCommandEncoder
kDYFEMTLDevice_newRenderPipelineStateWithTileDescriptor_completionHandler
IntersectionFunctionTableAllocationID
MTLDynamicLibraryTypeNoVendorSlice
MTLPixelFormatBC6H_RGBUfloat
kDYFEMTLLateEvalEvent_setSignaledValue
[%@ pollSampleBuffer:%@ resolvedBuffer:%@]
MTLFeatureSet_iOS_GPUFamily2_v5
kDYFEMTLVisibleFunctionTable_isAliasable
kDYFENSHMDMetalSession_nextDrawable
[%@ encodeToCommandBuffer:%@ encoder:%@ options:%@ batchSize:%@ resultRows:%@ resultColumns:%@ interiorColumns:%@ alpha:%@ beta:%@ A:%@ aInfo:%@ B:%@ bInfo:%@ C:%@ cInfo:%@ ]
IOCommandQueue
MTLValidationCodeSamplerDescriptor
kDYFEMTLCommandBuffer_blitCommandEncoderWithDescriptor
kDYFEMTLRenderCommandEncoder_setThreadgroupMemoryLength_atIndex
fragment shader key
MTLCullModeFront
BGRA10_XR_sRGB
IsULongCompatible
1D
MTLValidationCodeRasterizationRateMap
MTLVertexFormatInvalid
kDYFEMTLBuffer_newRemoteBufferViewForDevice
/System/Library/Extensions/%@.bundle/%@
%lu 
kDYFEMTLDevice_newRenderPipelineStateWithMeshDescriptor_options_reflection_error
kDYFEMTLRenderCommandEncoder_setTessellationFactorScale
kDYFEMTLRenderPipelineState_objectFunctionHandleWithFunction
kDYFEMTLVisibleFunctionTable_makeAliasable
[%@ setLineWidth:%@]
[%@ updateTextureMappings:%@ mode:%@ regions:%@ mipLevels:%@ slices:%@ numRegions:%@]
MTLDeviceLocationSlot
MTLPixelFormatEAC_R11Snorm
R10Unorm_X6_HLG
MTLTextureCompressionFootprintLossless
kDYFEMTLFragmentRenderCommandEncoder_setColorStoreActionOptions_atIndex
kDYFEMTLRenderCommandEncoder_executeCommandsInBuffer_withRange
BuiltInAmplificationID
kDYFEMTLBuffer_addDebugMarker_range
[%@ generationForResource:%@]
BFloat4x4
Min
ClampToZero
kDYFEMPSPlugin_newNDArrayConvolution2DWithDescriptor
kDYFEMTLFunction_reflectionWithOptions_pipelineLibrary
[%@ newIntersectionFunctionWithDescriptor:%@ completionHandler:%@]
MTLAccelerationStructureInstanceOptionNone
MTLLogicOperationInvAnd
MTLVertexFormatHalf2
kDYFEMTLRenderCommandEncoder_setFragmentTexture_baseLevel_atIndex
kDYFEMTLResourceStateCommandEncoder_moveTextureMappingsFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin
Tiny
MTLPixelFormatASTC_10x10_LDR
kDYFEMTLBinaryArchive_addComputePipelineFunctionsWithDescriptor_options_error
[%@ newRenderPipelineStateWithDescriptor:%@ error:%@]
UShort2
PrivateVoid
kDYFEMTLDevice_offsetFromIndirectBufferAddress
kDYFEMTLRenderCommandEncoder_dealloc
ETC2_RGB8A1_sRGB
MTLPrimitiveTopologyClassPoint
MTLRenderStageTile
kDYFEMTLCommandBuffer_sampledComputeCommandEncoderWithDispatchType_programInfoBuffer_capacity
kDYFEMTLDevice_compileVisibleFunction_withDescriptor_error
[%@ newRenderPipelineStateWithMeshDescriptor:%@ error:%@]
DYGuestAppClient *DYGetMTLGuestAppClient()
ASTC_6x5_HDR
MTLValidationCodeTextureDescriptor
_MTLMachOTypeIntelGPU
kDYFEMTLCounterSampleBuffer_dealloc
kDYFEMTLIndirectCommandBuffer_restoreOptimizedRanges
[%@ getBVHBuilderLock]
[%@ bitCodeListForFunctions]
MTLFeatureSet_iOS_GPUFamily5_v1
MTLPixelFormatYCBCR8_420_2P
kDYFEMPSExternalCNNUnary_encodeToCommandBuffer_computeCommandEncoder_options_pluginOptions_sourceTexture_sourceInfo_destinationTexture_destinationInfo
[%@ popDebugGroup]
MTLGPUOperationAtomicFetchMax
RG10Uint_X12
kDYFEMTLAccelerationStructureCommandEncoder_useResources_count_usage
kDYFEMTLIOScratchBuffer_dealloc
kDYFEMTLRenderCommandEncoder_setDepthBias_slopeScale_clamp
kDYFEMTLRenderCommandEncoder_setMeshIntersectionFunctionTable_atBufferIndex
[%@ accelerationStructureSizesWithDescriptor:%@]
kDYFEMTLBuffer_isPurgeable
kDYFEMTLComputePipelineState_functionHandlesWithFunctions
[%@ setStageInRegion:%@]
MTLComputeArgument
MTLDeviceFeatureProfilewatchOS_3
MTLFeatureSet_watchOS_GPUFamily2_v1
[%@ setParentGPUAddress:%@]
MTLBinaryArchiveSerializationDescriptorAspectIfAvailable
MTLPixelFormatYCBCR10_422_2P_HLG
MTLProvokingVertexModeFirst
CAMetalLayer
kDYFEMTLRenderCommandEncoder_setMeshBuffers_offsets_withRange
kDYFEMTLIOCommandBuffer_loadTexture_slice_level_size_sourceBytesPerRow_sourceBytesPerImage_destinationOrigin_sourceHandle_sourceHandleOffset
[%@ newBufferWithLength:%@ options:%@]
[%@ optimizeContentsForGPUAccess:%@]
MTLGLFragmentInputTypeGeneric
RGBA16Float_XR
kDYFEMTLArgumentEncoder_setBuffers_offsets_withRange
[%@ encodeSecondaryGradientToCommandBuffer:%@ encoder:%@ options:%@ pluginOptions:%@ primaryBuffer:%@ primaryInfo:%@ secondaryBuffer:%@ secondaryInfo:%@ gradientBuffer:%@ gradientInfo:%@ destination:%@ destinationInfo:%@ accumulate:%@ predi
MTLCompareFunctionLessEqual
MTLDataTypeUChar16
1DArray
MTLFXSpatialScalerVersionPrivate_v1
kDYFEMTLIOHandle_read_size_offset_stagingBuffer_stagingBufferSize
kDYFEMTLTexture_replaceRegion_mipmapLevel_withBytes_bytesPerRow
[%@ optimizeContentsForCPUAccess:%@]
Add
MTLPipelineOptionPrivateFrameworkGeneratedReflection
MTLPixelFormatASTC_10x8_LDR
MTLStepFunctionThreadPositionInGridX
kDYFEMTLAccelerationStructureCommandEncoder_setAccelerationStructureDescriptor
kDYFEMTLTexture_setLabel
kDYFEMTLVideoCommandEncoder_waitForFence
depth-stencil-state
MTLAttributeFormatChar4Normalized
MTLPixelFormatYCBCR10_422_2P_PACKED
kDYFEMTLAccelerationStructure_setResponsibleProcess
[%@ setTessellationFactorBuffer:%@ offset:%@ instanceStride:%@]
LoadPatchData
YCBCR10_444_1P_PQ
[%@ newLibraryWithSource:%@ options:%@ error:%@]
[%@ dispatchThreadsPerTile:%@ inRegion:%@]
MTLCompilerFlagSkipStageInputLoading
MTLLogicOpRevOr
RenderPassCommitAndReset
MTLTagTypeInstanceMotion
[%@ newVisibleFunctionTableFromObjectStageWithDescriptor:%@]
MTLTextureSwizzleShiftBlue
kDYFEMTLRenderCommandEncoder_setColorResolveTexture_slice_depthPlane_level_yInvert_atIndex
[%@ resolveCountersWithIndexRange:%@ sampleBuffer:%@ resolvedBuffer:%@]
[%@ newEventWithOptions:%@]
MTLPixelFormatBC2_RGBA
MTLPixelFormatBC3_RGBA_sRGB
kDYFEMTLIOCommandQueue_setLabel
[%@ setFragmentBuffer:%@ offset:%@ atIndex:%@]
ConditionalEventAbort
MTLDeadlineExecutionInvalid
PrivateShaderValidationChecksDisable
MTLPixelFormatASTC_8x5_HDR
MTLLateEvalEvent
kDYFEMTLDevice_utilityBufferForRenderCommandEncoder
kDYFEMTLFunction_newArgumentEncoderWithBufferIndex_reflection_binaryArchives
[%@ heapTextureSizeWithDescriptor:%@]
MTLDynamicLibrarySerializationDeviceAspect
MTLLogLevelNotice
[%@ setVertexArgument:%@ offset:%@ atIndex:%@]
[%@ addIndirectCommandBufferToGlobalResourceTable:%@]
[%@ newNDArrayConvolution2DGradientWithDescriptor:%@ ]
PerCounterDrawCallData
Level1
MTLVertexFormatFloat4
kDYFEMTLIOCommandBuffer_encodeSignalEvent_value
[%@ addMeshRenderPipelineFunctionsWithDescriptor:%@ error:%@]
IndirectCommandBufferGPUResourceID
MTLArgumentTypePrivateValue
kDYFEMTLRenderCommandEncoder_setStencilStoreActionOptions
[%@ newSharedEventWithHandle:%@]
[%@ sparseTileSizeWithTextureType:%@ pixelFormat:%@ sampleCount:%@]
[%@ newCNNConvolutionWithDescriptor:%@ convolutionData:%@ ]
MTLRenderFragmentArgument
MTLLogStateErrorInvalid
MTLPrecompiledDataTypePipelineData
MTLStitchedLibraryOptionFailOnBinaryArchiveMiss
[%@ setColorStoreAction:%@ atIndex:%@]
command-buffer
Depth16Unorm
MTLPixelFormatR16Float
kDYFEMTLComputeCommandEncoder_setBuffers_offsets_withRange
kDYFEMTLDeadlineProfile_dealloc
Clear
PrivateAlmondRequest
YCBCR10_444_1P_XR
MTLPurgeableStateKeepCurrent
MTLTextureCompressionTypeLossless
kDYFEMTLRenderCommandEncoder_setTileSamplerState_atIndex
[%@ setViewport:%@]
[%@ newBufferWithLength:%@ options:%@ atResourceIndex:%@]
Half2x3
kDYFEMTLFXSpatialScaler_setInputContentWidth
store action shader key
MTLDataTypeStruct
MTLDepthClipModeClamp
MTLPixelFormatPVRTC_RGB_2BPP
YCBCR12_420_2P_PACKED_PQ
kDYFEMTLDevice_getRawBVHBuilderPtr
[%@ drawPatches:%@ patchIndexBuffer:%@ patchIndexBufferOffset:%@ indirectBuffer:%@ indirectBufferOffset:%@]
[%@ setParentGPUSize:%@]
RevOr
kDYFEMTLFXTemporalScaler_setFence
kDYFEMTLIOCommandBuffer_addBarrier
kDYFEMTLIntersectionFunctionTable_setOpaqueTriangleIntersectionFunctionWithSignature_atIndex
MTLCommandBufferErrorNotPermitted
MTLTextureLayout
kDYFEMTLBinaryLibrary_serializeToURL_error
kDYFEMTLRenderCommandEncoder_drawIndexedPrimitives_indexCount_indexType_indexBuffer_indexBufferOffset_instanceCount_baseVertex_baseInstance
[%@ insertDebugCaptureBoundary]
[%@ sampledComputeCommandEncoderWithDispatchType:%@ programInfoBuffer:%@ capacity:%@]
v32@?0@\"DYShaderProfilerDrawCallInfo\"8Q16^B24
MTLPixelFormatYCBCR12_444_2P_PACKED
MTLFXTemporalScalerExecutionModeANE
IndirectCommandBufferAllocatedSize
DynamicLibraryInstallName
DepthFromDepthStencil
MTLCommandEncoderTypeAccelerationStructure
MTLRenderPipelineState
kDYFEMTLBuffer_setLabel
MTLGPUFamilyApple1
RG12Unorm_X8
MTLBlendOperationAdd
RG11B10Float
MTLVertexFormatUShort2Normalized
MTLFXSpatialScalerColorProcessingModePerceptual
kDYFEMTLRenderCommandEncoder_setDepthCleared
[%@ newLibraryWithDescriptorSPI:%@ error:%@]
MTLDataTypeRG16Unorm
kDYFEMTLAccelerationStructureCommandEncoder_deserializeAccelerationStructure_primitiveAccelerationStructures_fromBuffer_serializedBufferOffset
kDYFEMTLBuffer_setPurgeableState
MTLTextureUsageNoConcurrentAccess
kDYFEMTLRenderCommandEncoder_setPrimitiveRestartEnabled_index
DisableTriangleCulling
MTLIndexTypeUInt16
MTLPixelFormatBGRA10Unorm_HLG
MTLFeatureSet_iOS_GPUFamily3_v2
Util4
kDYFEMTLAccelerationStructure_uniqueIdentifier
kDYFEMTLBlitCommandEncoder_popDebugGroup
kDYFEMTLCommandBuffer_pushDebugGroup
kDYFEMTLRenderCommandEncoder_setMeshBuffer_offset_atIndex
[%@ drawTrianglesWithPositions:%@ vertexCount:%@ triangleIndices:%@ triangleCount:%@]
MTLCommandEncoderErrorStateAffected
LZMA
Component
[%@ newAccelerationStructureWithSize:%@ offset:%@]
Untracked
MTLLanguageVersion2_2
MTLPurgeableStateNonVolatile
MTLSparsePageSize64
kDYFEMTLRenderCommandEncoder_setStencilStoreAction
[%@ newCommandQueueWithDescriptor:%@]
perCommandBufferEncoderCount
Red
MTLCurveEndCapsNone
RGB9E5Float
RGBA8Uint
MTLPixelFormatYCBCR10_420_2P_PACKED_sRGB
kDYFEMTLIntersectionFunctionTable_isWriteComplete
[%@ setVertexBuffer:%@ offset:%@ atIndex:%@]
Half2x4
iOS_GPUFamily3_v4
[%@ setStencilResolveTexture:%@ slice:%@ depthPlane:%@ level:%@ yInvert:%@]
[%@ useResourceGroup:%@ usage:%@]
[%@ setMeshIntersectionFunctionTables:%@ withBufferRange:%@]
[%@ allocateScratchBufferWithMinimumSize:%@]
ComputePiplineAllocatedSize
MTLArgumentTypePrivateByVal
MTLBuiltInArgumentThreadPositionInGrid
MTLAttributeFormatChar2Normalized
RGBX16Uint
MTLPixelFormatFlagsIsIntCompatible
kDYFEMTLComputeCommandEncoder_setThreadgroupPackingDisabled
kDYFEMTLRenderCommandEncoder_setVertexVisibleFunctionTable_atBufferIndex
Begin
MTLDataTypeFloat8
BT2020Video
kDYFEMTLResourceStateCommandEncoder_endEncoding
kDYFEMTLVisibleFunctionTable_dealloc
MTLCaptureErrorNotSupported
MTLImageFilterFunctionArgumentTypeBufferSPI
ImageBlockSPI
MTLLanguageVersion3_0
MTLPipelineOptionPrivateDebugInstrumentation
MTLPixelFormatBGRA10_XR_PACKED_sRGB
RGBX32Sint
MTLFunctionLog
MTLAttributeFormatChar2
Bool3
2DArray
kDYFEMTLDevice_newCommandQueueWithDescriptor
kDYFEMTLRenderCommandEncoder_setDepthResolveTexture_slice_depthPlane_level_yInvert
[%@ newFunctionWithName:%@ constantValues:%@ functionCache:%@ error:%@]
[%@ newRenderPipelineStateWithName:%@ options:%@ reflection:%@ error:%@]
MTLDataTypeUChar4
BoundingBoxSPI
MTLPrecompiledDataTypeComputeFunction
MTLSharedEventHandle
kDYFEMTLIndirectCommandBuffer_waitUntilComplete
kDYFEMTLResourceStateCommandEncoder_harvested_updateTextureMapping_mode_region_mipLevel_slice
[%@ supportsRasterizationRateMapWithLayerCount:%@]
MTLArgumentTypePrivateIndirectConstant
MTLPixelFormatASTC_10x8_HDR
kDYFEMTLRenderCommandEncoder_setTileAccelerationStructure_atBufferIndex
[%@ newBufferWithBytesNoCopy:%@ length:%@ options:%@ deallocator:%@]
MTLAttributeFormatHalf
kDYFEMTLCommandQueue_dealloc
kDYFEMTLCommandQueue_setExecutionEnabled
kDYFEMTLFunctionStitchingNode_dealloc
MTLAttributeFormatUShort4
kDYFEMTLIOCommandBuffer_setLabel
MTLAttributeFormatUInt_VertexID
_End
kDYFEMTLDevice_newSpatialScalerWithDescriptor
kDYFEMTLIndirectComputeCommand_endIndirectCommandBuffer
[%@ setJitterOffsetX:%@]
[%@ addRenderPipelineFunctionsWithDescriptor:%@ options:%@ error:%@]
[%@ setEmulationObjectShaderPSO:%@]
ComputePipelineStateUniqueIdentifier
v32@?0@\"MTLArgument\"8Q16^B24
MTLLibraryErrorCompileWarning
MTLPixelFormatBC4_RSnorm
OptOut
MTLVertexFormatUChar4Normalized_BGRA
kDYFEMTLCommandQueue_setIsOpenGLQueue
kDYFEMTLDevice_newIntersectionFunctionTableWithDescriptor
kDYFEMTLDevice_useDeviceResourceTableForType
MTLDataTypeIndirectCommandBuffer
Max
MTLPixelFormatYCBCRA8_444_1P
StorageModeMemoryless
MTLStencilOperationIncrementWrap
kDYFECAMetalLayer_setBounds_contentsScale_windowBounds_windowProperties
kDYFEMTLCommandBuffer_setListIndex
[%@ setColorTexture:%@]
Short
SingleClusterGroup
kDYFEMTLDevice_newComputePipelineStateWithFunction_error
HeapTimeSinceTouched
render-encoders
ASTC_8x5_sRGB
MTLBlitOptionNone
Dynamic
YCBCR10_422_2P_PACKED_HLG
kDYFEMTLIndirectRenderCommand_drawMeshThreadgroups_threadsPerObjectThreadgroup_threadsPerMeshThreadgroup
[%@ drawIndexedPatches:%@ patchStart:%@ patchCount:%@ patchIndexBuffer:%@ patchIndexBufferOffset:%@ controlPointIndexBuffer:%@ controlPointIndexBufferOffset:%@ instanceCount:%@ baseInstance:%@ tessellationFactorBuffer:%@ tessellationFactorB
MTLDataTypeFloat3x2
kDYFEMTLFragmentRenderCommandEncoder_drawTrianglesWithPositions_vertexCount_triangleIndices_triangleCount
kDYFEMTLRasterizationRateMap_dealloc
kDYFEMTLRenderCommandEncoder_drawPrimitives_vertexStart_vertexCount_instanceCount_baseInstance
AccelerationStructureGPUResourceID
MTLBinaryArchiveErrorCompilationFailure
ReverseSubtract
MTLBuiltInArgumentBaseInstance
MTLPatchTypeQuad
CubeArray
kDYFEMTLDevice_newEventWithOptions
[%@ renderCommandEncoder]
[%@ addLoggingForType:%@ handler:%@]
MTLFeatureSet_macOS_GPUFamily1_v3
MTLLogicOperationOr
MTLPixelFormatStencil8
MTLTextureCompressionFeedbackUnsupportedTextureType
MTLFunctionStitchingNode
kDYFEMPSExternalNDArrayBinaryGradient_encodePrimaryGradientToCommandBuffer_encoder_options_pluginOptions_primaryBuffer_primaryInfo_secondaryBuffer_secondaryInfo_gradientBuffer_gradientInfo_destination_destinationInfo_accumulate_predicationB
kDYFEMTLVideoCommandEncoder_setLabel
MTLCommandBufferScheduled_deprecated
MTLBuiltInArgumentThreadIndexInSimdgroup
FileNotFound
RGBA16Bfloat
MTLSamplerAddressModeClampToHalfBorderColor
MTLTextureCompressionFeedbackUnsupportedDevice
MTLTextureUsageShaderAtomic
kDYFEMTLRenderCommandEncoder_setClipPlane_p2_p3_p4_atIndex
kDYFEMTLVisibleFunctionTable_allocatedSize
iOS_GPUFamily5_v1
ASTC_4x2_HDR
90DegreesClockwise
MTLValidationCodeMeshPipelineDescriptor
kDYFECAMetalLayer_setColorspace
kDYFEMTLBlitCommandEncoder_fillTexture_level_slice_region_color
kDYFEMTLFXTemporalScaler_setJitterOffsetX
kDYFEMTLIndirectComputeCommand_reset
Indexed
CAMetalDrawable
MTLIOScratchBuffer
kDYFEMTLRenderCommandEncoder_setAlphaTestReferenceValue
kDYFEMTLSharedTextureHandle_dealloc
_quadLibrary != nil
MetalStatistics
ASTC_6x5_sRGB
kDYFEMTLIntersectionFunctionTable_doesAliasAllResources_count
[%@ setReactiveMaskTexture:%@]
[%@ encodeWaitForEvent:%@ value:%@]
[%@ newSharedEventHandle]
[%@ newArgumentEncoderWithBufferIndex:%@ reflection:%@ binaryArchives:%@]
MTLFXSpatialScalerVersionPrivate_Bicubic
kDYFEMTLDynamicLibrary_dealloc
[%@ setFunction:%@ atIndex:%@]
[%@ addResidencySets:%@ count:%@]
MTLEvent
kDYFEMTLRenderCommandEncoder_setObjectBuffers_offsets_withRange
Half8
BaseInstance
BGRA8Unorm
[%@ newComputePipelineStateWithFunction:%@ error:%@]
[%@ resolveCounterRange:%@]
[%@ newLibraryWithDAG:%@ functions:%@ error:%@]
[%@ resourceStateCommandEncoderWithDescriptor:%@]
[%@ moveTextureMappingsFromTexture:%@ sourceSlice:%@ sourceLevel:%@ sourceOrigin:%@ sourceSize:%@ toTexture:%@ destinationSlice:%@ destinationLevel:%@ destinationOrigin:%@]
MTLIOCompressionMethodLZMA
DontCare
kDYFEMTLCommandQueue_commandBufferWithDescriptor
kDYFEMTLStackTraceEntry_dealloc
TextureResourceIndex
MTLBlitCommandEncoder
kDYFEMTLRenderCommandEncoder_setLabel
MTLDataTypeFloat4x3
MTLIOPriorityNormal
CustomSamplePositions
MTLArgumentTypeBuffer
SingleCluster
[%@ drawMeshThreads:%@ threadsPerObjectThreadgroup:%@ threadsPerMeshThreadgroup:%@]
TextureTimeSinceTouched
OneMinusSourceAlpha
Affected
FragmentFunction
MTLQosMedium
MTLVertexFormatInt4
kDYFEMTLHeap_currentAllocatedSize
kDYFEMTLHeap_newAccelerationStructureWithSize
kDYFEMTLRasterizationRateMap_physicalSizeForLayer
MTLDataTypeVisibleFunctionTable
MTLGPUAddressSpaceRayPayload
MTLPipelineOptionPrivateStitchingReflection
MTLPixelFormatBC6H_RGBFloat
[%@ generateMipmapsForTexture:%@]
[%@ setWritableHeapsEnabled:%@]
AccelerationStructureResourceIndex
MTLPixelFormatYCBCR10_420_2P_sRGB
kDYFEMTLDevice_addComputePipelineStateToGlobalResourceTable
kDYFEMTLHeap_timeSinceTouched
kDYFEMTLResidencySet_commitAdds
[%@ setResourceIndex:%@]
MTLVertexAttribute
MTLProvokingVertexModeSecond
MTLRenderStageMesh
MTLTextureSwizzleBlue
kDYFEMTLRenderCommandEncoder_setVertexVisibleFunctionTables_withBufferRange
[%@ optimizeContentsForCPUAccess:%@ slice:%@ level:%@]
functions
Short4Normalized
MTLPixelFormatASTC_10x5_LDR
kDYFEMTLDevice_newDynamicLibrary_computeDescriptor_error
kDYFEMTLDevice_newTextureWithBytesNoCopy_length_descriptor_deallocator
[%@ drawPrimitives:%@ vertexStart:%@ vertexCount:%@ instanceCount:%@ baseInstance:%@]
[%@ setTileBuffers:%@ offsets:%@ withRange:%@]
[%@ setFunctions:%@ withRange:%@]
%@/MetalStatistics%@
MTLPatchTypeTriangle
MTLPixelFormatYCBCR12_444_2P
[%@ contents]
kDYFEMTLCommandBuffer_dealloc
kDYFEMTLDevice_newAccelerationStructureWithDescriptor
2_3
PrivatePostVertexDump
GBGR422
PipelineData
kDYFEMTLResidencySet_dealloc
[%@ removeResidencySets:%@ count:%@]
Failed to load property file at %@, reason: %@
MTLDeviceFeatureProfileiOS_4
Nand
PrivateEnableResourcePatchingInstrumentation
MTLVertexFormatCharNormalized
kDYFEMTLIOCommandBuffer_barrier
kDYFEMTLPipelineLibrary_setLabel
IndirectCommandBufferAllocationID
float2
MTLLogLevelFault
_v1
kDYFEMTLComputeCommandEncoder_setBytes_length_atIndex
kDYFEMTLSamplerState_gpuResourceID
Unknown Unknown
CiUul
Float3x3
kDYFEMTLRenderCommandEncoder_setFragmentBuffers_offsets_withRange
kDYFEMTLTexture_uniqueIdentifier
MTLPixelFormatRG12Uint_X8
kDYFEMTLRenderCommandEncoder_setObjectVisibleFunctionTable_atBufferIndex
[%@ newDynamicLibraryFromURL:%@ error:%@]
MTLLogicOpEquiv
MTLStepFunctionPerVertex
MTLBlendFactorOneMinusBlendAlpha
Compatible
2_2
MTLMessageTypeWarning
MTLQosHigh
Float2x3
CommandEncoder
kDYFEMTLAccelerationStructure_setDescriptor
kDYFEMTLCommandQueue_addResidencySet
YCBCR10_444_1P_sRGB
kDYFEMTLDevice_newBufferWithBytesNoCopy_length_options_atResourceIndex_deallocator
[%@ setScissorRect:%@]
MTLPixelFormatASTC_4x4_HDR
MTLBuiltInArgumentInvalid
Internal
IsBlendable
kDYFEMTLParallelRenderCommandEncoder_popDebugGroup
[%@ removeResource:%@]
R16Unorm
PrivateInlinedSymbols
MTLFXSpatialScalerVersionPrivate_ASE
kDYFEMTLComputeCommandEncoder_useResource_usage
kDYFEMTLDevice_heapTextureSizeAndAlignWithDescriptor
kDYFEMTLDevice_resourceIndexFromIndirectBufferAddress
All
MTLDataTypeBool2
MTLLogicOpXor
MTLSamplerAddressModeClampToBorderColor
MTLTextureType2DMultisample
MTLTransformTypeComponent
MTLHeapAliasedResources
GPUFamilies=
MTLAccelerationStructureRefitOptionPerPrimitiveData
MTLBlendOperationMax
tvOS_7
RevAnd
MTLPrimitiveTypePoint
kDYFEMTLDevice_newTiledTextureWithBytesNoCopy_length_descriptor_offset_bytesPerRow
[%@ dispatchThreadsWithIndirectBuffer:%@ indirectBufferOffset:%@]
AGXMetalStatistics
Long3
MTLLibraryErrorUnsupported
MTLPixelFormatRGBX8Snorm
kDYFEMTLDevice_newRenderPipelineStateWithDescriptor_error
[%@ addTextureToGlobalResourceTable:%@]
[%@ setFramebufferOnly:%@]
MTLIOStatusCancelled
RGB10A2Unorm_sRGB
kDYFEMPSPlugin_newCNNNeuronWithNeuronType_neuronParameterA_neuronParameterB_neuronParameterC
kDYFEMTLDevice_newCommandQueue
[%@ computeCommandEncoderWithParallelExecution]
MTLPixelFormatRGBX32Sint
_MTLArgumentBufferResourceTypeAccelerationStructure
kDYFEMTLHeap_newAccelerationStructureWithDescriptor
kDYFEMTLIndirectCommandBuffer_doesAliasAnyResources_count
kDYFEMTLTexture_isShareable
Round
BC7_RGBAUnorm
R12Unorm_X4
MTLPixelFormatFlagsIsColorRenderable
MTLVertexStepFunctionPerPatchControlPoint
kDYFEMTLDevice_newDefaultLibraryWithBundle_error
MTLArgumentBuffersTier1
MTLBuiltInArgumentThreadsPerGrid
MTLFunctionTypeVisible
Instancing
RGBX32Uint
YCBCR10_422_2P_PACKED_XR
MTLResourceStorageModeMemoryless
kDYFEMTLBlitCommandEncoder_endEncoding
gDYMTLObjectRemappingBlock
PrivateFunctionWithNoReflection
PrivateShaderValidationChecksEnable
YCBCR10_444_2P_XR
kDYFEMTLIntersectionFunctionTable_isComplete
kDYFEMTLRenderCommandEncoder_setMeshAccelerationStructure_atBufferIndex
kDYFEMTLRenderCommandEncoder_setObjectSamplerStates_withRange
[%@ presentDrawable:%@]
MTLAttributeFormatFloat3
UnsupportedOptOut
MTLTriangleFillModeLines
[%@ vertexFunctionHandleWithFunction:%@]
MTLDefaultLibrary
MTLCompareFunctionGreater
MTLCompilerErrorEarlyExit
macOS_GPUFamily2_v1
MTLTextureTypeCube
kDYFEMTLCommandQueue_getGPUPriority
[%@ copyFromTexture:%@ sourceSlice:%@ sourceLevel:%@ toTexture:%@ destinationSlice:%@ destinationLevel:%@ sliceCount:%@ levelCount:%@]
[%@ setObjectVisibleFunctionTable:%@ atBufferIndex:%@]
Mac1
R10Unorm_X6_sRGB
MTLStencilOperationDecrementWrap
Replace
[%@ clearBarrier]
[%@ enqueueBarrier]
UnexpectedElement
MTLCommandBufferErrorProtectionViolation
Zlib
BGRA10Unorm_sRGB
MTLRenderCommandEncoder
kDYFEMTLDevice_heapAccelerationStructureSizeAndAlignWithDescriptor
kDYFEMTLRenderCommandEncoder_setVertexBufferOffset_attributeStride_atIndex
[%@ setPrimitiveRestartEnabled:%@ index:%@]
supportedGPUFamilies
ResourceStateCommandEncoderMoveMappings
MTLFunctionPointerHandle
kDYFEMTLIntersectionFunctionTable_setBuffers
kDYFEMTLRenderCommandEncoder_setFragmentIntersectionFunctionTable_atBufferIndex
[%@ copyParameterDataToBuffer:%@ atOffset:%@]
RestoreMTLAccelerationStructureInstance
IntersectionFunctionTableGPUResourceID
MTLIndirectArgumentBuffersTier2
MTLThreadgroupDistributionModeSingleClusterGroup
_MTLMachOTypeAMDGPU
[%@ newCaptureScopeWithDevice:%@]
NO
Apple2
kDYFEMPSExternalCNNConvolution_exportWeightsAndBiasesWithCommandBuffer_encoder_weights_weightsDataType_biases_predicationBuffer_predicationOffset
kDYFEMTLDevice_setResourcesPurgeableState_newState_oldState_count
kDYFEMTLRenderCommandEncoder_drawPatches_patchIndexBuffer_patchIndexBufferOffset_indirectBuffer_indirectBufferOffset
[%@ waitForFence:%@]
[%@ setBackgroundGPUPriority:%@]
[%@ computeCommandEncoderWithDispatchType:%@ substreamCount:%@]
MTLGPUPriorityNormal
MTLSamplerBorderColorOpaqueWhite
MTLCommandBufferStatusCommitted
BGRA10Unorm_PQ
RGBA16Sint
Managed
Private_BRNet3
kDYFEMTLRenderPipelineState_resourceIndex
OneMinusSource1Alpha
MTLLogicOperationCopy
RenderTarget
MTLVertexFormatChar4Normalized
kDYFEMPSPlugin_newCNNSoftMax
kDYFEMTLCommandBuffer_computeCommandEncoder
kDYFEMTLFragmentRenderCommandEncoder_setStencilStoreAction
kDYFEMTLRenderPipelineState_setEmulationMeshShaderIntermediateBufferSlot
frame
StageInGridSize
MTLPixelFormatEAC_R11Unorm
kDYFEMTLCommandBuffer_accelerationStructureCommandEncoderWithDescriptor
[%@ setStencilStoreActionOptions:%@]
[%@ setColorspace:%@]
Nor
MTLReadWriteTextureTier1
MTLTextureCompressionFeedbackUnsupportedTextureUsageShaderWrite
kDYFEMTLRenderCommandEncoder_setMeshSamplerState_atIndex
[%@ setCompilerProcessesCount:%@]
[%@ reloadWeightsAndBiases:%@ ]
render-pipeline-states
RayPayload
Flush
MTLTagTypeMaxLevels
kDYFEMTLBinaryArchive_addLibrary_computePipelineDescriptor_error
kDYFEMTLFunction_newArgumentEncoderWithBufferIndex_pipelineLibrary
kDYFEMTLRenderCommandEncoder_executeCommandsInBuffer_indirectBuffer_indirectBufferOffset
[%@ setTileSamplerStates:%@ lodMinClamps:%@ lodMaxClamps:%@ withRange:%@]
[%@ setCompletionQueue:%@]
MTLDataTypeHalf4x3
MTLPixelFormatBC4_RUnorm
HeapUsedSize
vertex fetch shader key
MTLCommandBufferErrorMemoryless
kDYFEMTLArgumentEncoder_setLabel
kDYFEMTLDevice_sampleTimeStamps_gpuTimeStamp
[%@ newLateEvalEvent]
MTLAttributeFormatFloatRG11B10
MTLBinaryArchiveSkipAIRValidation
MTLBinaryArchiveSupportAIRNT
MTLGPUPriorityNormalHigh
kDYFEMTLComputeCommandEncoder_executeCommandsInBuffer_withRange
kDYFEMTLIndirectCommandBuffer_containsResource
kDYFEMTLTexture_formattedDescription
MTLDataTypeLong4
MTLPixelFormatBC3_RGBA
YCBCR8_422_2P
kDYFEMTLTexture_mipmapInfo
IVRCompositor::PostPresentHandoff()
VertexID
1_0
MTLValidationCodeFramebuffer
MTLCaptureManager
kDYFEMTLComputePipelineState_gpuResourceID
kDYFEMTLDevice_newIndirectCommandBufferWithDescriptor_maxCommandCount_options
kDYFEMTLDynamicLibrary_installName
kDYFEMTLTexture_harvested_replaceRegion_mipmapLevel_slice_withBytes_bytesPerRow_bytesPerImage
MTLAttributeFormatUShort
BuiltInMeshGridProperties
kDYFEMTLDevice_newBufferWithBytes_length_options_gpuAddress
MTLPixelFormatYCBCR10_420_2P_PACKED_PQ
[%@ computeCommandEncoder]
[%@ tileSizeWithTextureType:%@ pixelFormat:%@ sampleCount:%@]
[%@ requiredLinearTextureBytesPerRowForDescriptor:%@]
MTLPixelFormatR10Unorm_X6
MTLPixelFormatRG10Unorm_X12
InverseCopy
MirrorClampToEdge
UnsupportedHeapTypeSparse
MTLTextureSwizzleOne
kDYFEMTLBinaryArchive_storeMeshRenderPipelineDescriptor
kDYFEMTLBuffer_isComplete
kDYFEMTLDevice_newFunctionWithGLESIR_functionType
[%@ serializeAccelerationStructure:%@ toBuffer:%@ offset:%@]
-[DYMTLTextureResize initWithDevice:]
kDYFEMTLFragmentRenderCommandEncoder_setColorStoreAction_atIndex
kDYFEMTLRenderCommandEncoder_endEncoding
MTLDataTypeUShort3
macOS_3
MTLFunctionTypeKernel
MTLIOCompressionMethodLZBitmap
TooManyDepthBiasEmits
StoreAndMultisampleResolve
[%@ convertSparseTileRegions:%@ toPixelRegions:%@ withTileSize:%@ numRegions:%@]
MTLPixelFormatRG10Uint_X12
[%@ setVertexSamplerStates:%@ withRange:%@]
MTLDataTypeBFloat3x3
MTLHazardTrackingModeTracked
kDYFEMTLVisibleFunctionTable_setValue_withRange
layerStreamRef
MTLGLFragmentInputTypePPAttrib
PrivateStitchingReflection
kDYFEMTLRenderCommandEncoder_setDepthStencilState
kDYFEMTLResidencySet_removeHeap
MTLBlendFactorBlendAlpha
MTLDataTypeHalf3
MTLDataTypeR8Unorm
kDYFEMTLBuffer_setParentGPUSize
[%@ setVertexSamplerState:%@ lodMinClamp:%@ lodMaxClamp:%@ atIndex:%@]
[%@ waitForProgress:%@]
[%@ newLibraryWithDescriptor:%@ error:%@]
float4
Failed to load analysis file at %@, reason: %@
MTLDataTypeRGBA16Unorm
RGBA8Unorm
IsPQ
kDYFEMTLIndirectRenderCommand_drawPatches_patchStart_patchCount_patchIndexBuffer_patchIndexBufferOffset_instanceCount_baseInstance_tessellationFactorBuffer_tessellationFactorBufferOffset_tessellationFactorBufferInstanceStride
[%@ setGPUPriority:%@]
ReadWrite
MTLCommandBufferErrorInvalidResource
MTLPixelFormatRG16Snorm
MTLStoreActionUnknown
kDYFEMTLFragmentRenderCommandEncoder_setFragmentTextures_withRange
[%@ setVertexSamplerState:%@ lodMinClamp:%@ lodMaxClamp:%@ lodBias:%@ atIndex:%@]
YCBCR12_444_2P_PACKED_XR
MTLSamplerBorderColorSPICustom
kDYFEMTLArgumentEncoder_newArgumentEncoderForBufferAtIndex
kDYFEMTLHeap_setLabel
kDYFEMTLRelocation_dealloc
[%@ getArchiveIDWithError:%@]
libraries
-derived.js
MTLDataTypeHalf3x3
MTLGenericBVHHeaderVersionPerPrimitiveData
MTLPixelFormatRGB10A2Unorm_HLG
kDYFEMTLTexture_invalidateRegion
MTLBufferRobustnessSupportNotSupported
MTLCommandEncoderTypeCompute
MTLPixelFormatASTC_8x4_LDR
YCBCR10_444_2P_PACKED
MTLValidationCodeLibrary
RasterizationRateMap
MTLLogLevelInfo
kDYFEMTLHeap_newBufferWithLength_options
[%@ writeMeshShaderEmulatorDataStructureHeader:%@ meshShaderPSO:%@ scalingFactor:%@]
[%@ accelerationStructureCommandEncoder]
Float8
MTLPixelFormatRGB10A2Uint
MTLTextureType1D
MTLWindingCounterClockwise
[%@ memoryBarrierWithResources:%@ count:%@]
[%@ setStencilResolveTexture:%@ slice:%@ depthPlane:%@ level:%@]
[%@ setEmulationMeshShaderPSO:%@]
load action shader key
tvOS_GPUFamily2_v2
MTLPixelFormatFlagsIsCompressed
kDYFEMTLComputeCommandEncoder_setIntersectionFunctionTables_withBufferRange
kDYFEMTLFXSpatialScaler_encodeToCommandBuffer
kDYFEMTLIntersectionFunctionTable_setOpaqueCurveIntersectionFunctionWithSignature_withRange
kDYFEMTLResidencySet_countForResource
[%@ newFunctionWithPluginData:%@ bitcodeType:%@]
-counters.plist
OneMinusSource1Color
MTLDeviceFeatureProfileiOS_1
MTLGPUPriorityHigh
UniqueIdentifier
kDYFEMTLPipelineLibrary_newComputePipelineDescriptorWithName_error
[%@ setObjectIntersectionFunctionTable:%@ atBufferIndex:%@]
[%@ addMeshRenderPipelineFunctionsWithDescriptor:%@ options:%@ error:%@]
MTLCompilerFlagEmulateIndirectAccelerationStructures
EAC_RG11Snorm
MTLPixelFormatYCBCR10_422_2P_PQ
MTLTextureType2D
MTLVertexFormatUInt1010102Normalized
kDYFEMPSExternalMatrixMultiplication_encodeToCommandBuffer_encoder_options_batchSize_resultRows_resultColumns_interiorColumns_alpha_beta_A_aInfo_B_bInfo_C_cInfo_predicationBuffer_predicationOffset_transA_transB
kDYFEMTLDevice_newLibraryWithSource_options_error
[%@ setDepthTexture:%@]
RG8Snorm
YCBCR10_420_2P_PACKED_XR
kDYFEMTLBinaryArchive_addRenderPipelineFunctionsWithDescriptor_options_error
kDYFEMTLDevice_serializeComputePipelineDescriptor
[%@ setGlobalBuffer:%@]
[%@ setVertexBufferOffset:%@ attributeStride:%@ atIndex:%@]
AccelerationStructureAllocatedSize
Float4x3
MTLPixelFormatASTC_4x4_LDR
MTLPixelFormatBGR10A2Unorm_PQ
kDYFEMTLBlitCommandEncoder_copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin
kDYFEMTLRenderCommandEncoder_useResidencySet
[%@ tileSizeWithSparsePageSize:%@ textureType:%@ pixelFormat:%@ sampleCount:%@]
[%@ deserializePrimitiveAccelerationStructure:%@ fromBuffer:%@ serializedBufferOffset:%@]
MTLPixelFormatBC7_RGBAUnorm
Util3
kDYFEMTLCaptureManager_notifySubmissionForEyeSPI_iosurface_bounds_submitFlags
kDYFEMTLCommandQueue_setLabel
kDYFEMTLLibrary_setOverrideTriple
kDYFEMTLVisibleFunctionTable_setFunctions_withRange
[%@ newBinaryLibraryWithOptions:%@ url:%@ error:%@]
[%@ encodeToCommandBuffer:%@ encoder:%@ options:%@ batchSize:%@ inputMatrix:%@ inputMatrixInfo:%@ weightMatrix:%@ weightMatrixInfo:%@ biasVector:%@ biasVectorInfo:%@ resultMatrix:%@ resultMatrixInfo:%@ alpha:%@ numberOfFeatureVectors:%@ inp
Functions
MTLPipelineOptionPrivateCompileTimeStatistics
MTLPixelFormatX24_Stencil8
[%@ setViewports:%@ count:%@]
Char4
MTLDeviceFeatureProfilewatchOS_2
RGB10A2Unorm_HLG
RGBX8Uint
MTLSamplerAddressModeRepeat
/System/Library/Extensions/%@.bundle/Contents/%@
MacCatalyst2
ASTC_10x6_HDR
[%@ waitUntilComplete]
[%@ encodeSecondaryGradientToCommandBuffer:%@ encoder:%@ options:%@ pluginOptions:%@ primary:%@ primaryInfo:%@ secondary:%@ secondaryInfo:%@ gradient:%@ gradientInfo:%@ destination:%@ destinationInfo:%@ accumulate:%@ predicationBuffer:%@ pr
compute kernel info
MTLAttributeFormatShort4Normalized
Draw
MTLMathModeFast
MTLPixelFormatASTC_4x2_sRGB
MTLPixelFormatASTC_8x8_HDR
MTLPixelFormatR32Uint
RG10Unorm_X12_sRGB
FunctionNotFound
MTLPixelFormatASTC_10x6_sRGB
kDYFEMTLCaptureScope_beginScope
/System/Library/Extensions/%@.bundle/Contents/Resources/%@
UChar8
MTLPixelFormatR10Unorm_X6_HLG
[%@ containsHeap:%@]
BufferVirtualGPUAddress
~/Library/Developer/MetalStatistics
kDYFEMTLCaptureManager_startCaptureWithScope
kDYFEMTLRenderCommandEncoder_setObjectBytes_length_atIndex
kDYFEMTLRenderCommandEncoder_setScissorRects_count
[%@ resourceIndex]
isOpenGLQueue
Source1Alpha
MTLCounterSampleBufferErrorOutOfMemory
BFloat4x2
MTLLanguageVersion2_3
ASTC_10x6_sRGB
MTLPixelFormatBC2_RGBA_sRGB
MTLPixelFormatBGRA10_XR_sRGB
v8@?0
MTLCompilerErrorFatalError
R8Unorm
MTLPixelFormatRGBX8Sint
UnsupportedTextureType
kDYFEMTLBinaryArchive_addComputePipelineStateWithDescriptor_error
kDYFEMTLDevice_newRenderPipelineDescriptorWithSerializedData_deserializationContext
kDYFEMTLDevice_newArgumentEncoderWithArguments_count
MTLDataTypeShort8
kDYFEMTLCommandBuffer_videoCommandEncoder
kDYFEMTLIOCommandQueue_enqueueBarrier
[@ saveContentsToPath:%@]
Error
MTLDataTypeLong2
kDYFEMTLCommandBuffer_presentDrawable
kDYFEMTLDevice_harvested_newBufferWithBytes_length_options
kDYFEMTLRenderCommandEncoder_setFragmentTextures_withRange
kDYFEMTLRenderPipelineState_timeSinceTouched
[%@ setFragmentTexture:%@ baseLevel:%@ atIndex:%@]
[%@ heapTextureSizeAndAlignWithDescriptor:%@]
BuiltInMesh
ComputeFunction
kDYFEMTLComputePipelineState_newComputePipelineStateWithAdditionalBinaryFunctions
[%@ newExternFunctionWithName:%@]
MTLDynamicLibrary
kDYFEMTLCommandBuffer_setResourceGroups_count
kDYFEMTLComputePipelineState_uniqueIdentifier
[%@ setTileArgument:%@ offset:%@ atIndex:%@]
[%@ writeGeometryOfAccelerationStructure:%@ toBuffer:%@ geometryBufferOffset:%@]
[%@ setEmulationVertexShaderIntermediateBufferSlot:%@]
R16Snorm
Common1
MTLIndirectRenderCommand
kDYFEMTLBlitCommandEncoder_invalidateCompressedTexture_slice_level
[%@ setEnableBarrier:%@]
TextureAllocationID
ComputePipelineStateGPUResourceID
TileReflectionData
MTLValidationCodeVertexDescriptor
[%@ newBufferWithIOSurface:%@]
[%@ newLibraryWithImageFilterFunctionsSPI:%@ imageFilterFunctionInfo:%@ error:%@]
[%@ newCNNNeuronWithNeuronType:%@ neuronParameterAArray:%@ count:%@ ]
kDYFEMTLArgumentEncoder_constantDataAtIndex
kDYFEMTLCommandQueue_setGPUPriority
kDYFEMTLCommandQueue_setSkipRender
kDYFEMTLHeap_newAccelerationStructureWithSize_resourceIndex
kDYFEMTLTexture_newSharedTextureHandle
IndirectCommandBufferOptimizeRanges
MTLColorWriteMaskRed
MTLCommandBufferErrorConditionalEventAbort
PVRTC_RGBA_2BPP
kDYFEMTLLateEvalEvent_dealloc
MTLMessageTypeError
Constant
kDYFEMTLCaptureScope_setLabel
kDYFEMTLFXTemporalScaler_setMotionVectorScaleY
kDYFEMTLRenderCommandEncoder_setDepthResolveTexture_slice_depthPlane_level
kDYFEMTLRenderCommandEncoder_setDepthStoreActionOptions
kDYFEMTLRenderCommandEncoder_useResources_count_usage_stages
kDYFEMTLRenderPipelineState_setEmulationPayloadMemoryLength
IndirectCommandBufferTimeSinceTouched
DepthResolvedSample
PVRTC_RGB_4BPP_sRGB
Util2
kDYFEMTLBinaryLibrary_addComputePipelineFunctionsWithDescriptor_error
MTLCommandBufferErrorTimeout
kDYFEMTLResidencySet_removeAllResources
MTLAttributeFormatUShort4Normalized
MTLBlendFactorOneMinusBlendColor
MTLDataTypeBool4
Large
MTLDeviceFeatureProfileiOS_3
MTLLanguageVersion2_0
kDYFEMTLLateEvalEvent_waitUntilSignaledValue_timeoutMS
kDYFEMTLRenderCommandEncoder_setMeshTextures_withRange
MTLCompareFunctionAlways
MTLLogicOperationInverseCopy
IsUIntCompatible
kDYFEMTLBlitCommandEncoder_setLabel
kDYFEMTLIntersectionFunctionTable_timeSinceTouched
kDYFEMTLSharedEvent_dealloc
MTLTextureCompressionFootprintLevel1
[%@ newComputePipelineStateWithDescriptor:%@ completionHandler:%@]
MotionSPI
MTLStorageModeManaged
WriteCombined
MTLCommandBufferErrorOptionEncoderExecutionStatus
MTLVertexAmplificationModeCount
kDYFEMTLAccelerationStructureCommandEncoder_setAccelerationStructureState
kDYFEMTLDevice_reserveGPUAddressRange
PrivateIndirectConstant
ThreadIndexInSimdgroup
kDYFEMTLFXTemporalScaler_setMotionTexture
Apple4
MTLTessellationFactorStepFunctionPerPatch
kDYFEMTLAccelerationStructureCommandEncoder_copyAndCompactAccelerationStructure_toAccelerationStructure
[%@ supportsVertexAmplificationCount:%@]
MTLDataTypeRG8Snorm
UInt8
MTLPixelFormatRGB8_420_2P
3D
void init_interpose_api(void *)
PrivateFrameworkGeneratedReflection
kDYFEMTLBinaryLibrary_setLabel
kDYFEMTLDevice_minimumTextureBufferAlignmentForPixelFormat
[%@ newLogStateWithDescriptor:%@ error:%@]
MTLDataTypeBFloat3x4
3_1
MTLPixelFormatFlagsIsSRGB
MTLLanguageVersion2_4
kDYFEMTLVisibleFunctionTable_setGlobalBuffer
[%@ doesAliasResource:%@]
[%@ setMeshBuffer:%@ offset:%@ atIndex:%@]
[%@ texture]
[%@ newMatrixMultiplicationWithTransposeLeft:%@ transposeRight:%@ resultRows:%@ resultColumns:%@ interiorColumns:%@ alpha:%@ beta:%@ ]
DependencyLoadFailure
MTLPixelFormatRG8Sint
MTLTagTypeCurveData
[%@ setBuffers:%@ offsets:%@ withRange:%@]
MTLPixelFormatASTC_8x8_LDR
MTLDeadlineProfile
kDYFEMTLIntersectionFunctionTable_gpuResourceID
Float4x4
MTLPixelFormatYCBCR12_422_2P_PQ
MTLQosExclusive
Framebuffer
kDYFEMTLCommandQueue_getSPIStats
MTLDevicePartitionDefault
MPSExternalCNNUnary
kDYFEMTLRenderCommandEncoder_useHeap
[%@ setRenderPipelineStates:%@ withRange:%@]
[%@ setObjectBuffers:%@ offsets:%@ withRange:%@]
[%@ setEmulationPrimitiveTopology:%@]
vertex fetch shader info
MTLTextureColorSpaceConversionMatrixBT709Video
MTLFunctionPrivateArgument
[%@ setDepthReversed:%@]
MTLTextureCompressionFeedbackUnsupportedLinearLayout
kDYFEMPSPlugin_newMatrixMultiplicationWithTransposeLeft_transposeRight_resultRows_resultColumns_interiorColumns_alpha_beta
[%@ setTextures:%@ withRange:%@]
[%@ doesAliasAnyResources:%@ count:%@]
MTLLibraryOriginalFilePath
EAC_R11Snorm
MTLSharedEvent
kDYFEMTLBuffer_resourceUsage
kDYFEMTLIOCommandBuffer_commit
[%@ addComputePipelineFunctionsWithDescriptor:%@ options:%@ error:%@]
iOS_GPUFamily1_v2
MTLPixelFormatASTC_8x5_LDR
RG16Bfloat
_MTLArgumentBufferResourceTypeTexture
[%@ copyFromBuffer:%@ sourceOffset:%@ toBuffer:%@ destinationOffset:%@ size:%@]
[%@ setSubmissionQueue:%@]
MTLBindingTypeIntersectionFunctionTable
MTLBlitOptionToolsClient
MTLDynamicLibrarySerializationAtomic
MTLGenericBVHHeaderVersionCurves
MTLAccelerationStructureCommandEncoder
kDYFEMTLSharedEvent_newSharedEventHandle
[%@ newAccelerationStructureWithSize:%@ offset:%@ resourceIndex:%@]
MTLBindingTypeTexture
kDYFEMTLBinaryArchive_getBinaryDataForKey
[%@ setRenderPipelineState:%@]
[%@ setSignaledValue:%@]
[%@ nextDrawable]
v32@?0@8@16^B24
MTLDataTypeUChar2
A8Unorm
MTLPixelFormatR8Sint
MTLTextureUsageUnknown
kDYFEMTLBinaryArchive_dealloc
kDYFEMTLFragmentRenderCommandEncoder_setFragmentSamplerStates_lodMinClamps_lodMaxClamps_withRange
ShortNormalized
EnableInstrumentation
Cancelled
kDYFEMTLResidencySet_commitRemoves
[%@ commitWithDeadline:%@]
RenderPipelineStateTimeSinceTouched
render-pipeline-state
Explicit
MTLLogicOperationXor
MTLPipelineOptionPrivateAlmondRequest
MTLPixelFormatYCBCR12_420_2P_PACKED
MTLTessellationFactorStepFunctionPerPatchAndPerInstance
TileRenderPipelineDescriptor
GPU
kDYFEMTLIntersectionFunctionTable_waitUntilComplete
NonOpaque
AtomicExchange
MPSExternalNDArrayBinaryGradient
kDYFEMPSExternalCNNUnary_encodeBatchToCommandBuffer_computeCommandEncoder_options_pluginOptions_sourceTextures_sourceInfo_destinationTextures_destinationInfo_predicationBuffer_predicationOffset
kDYFEMTLResidencySet_commit
kDYFEMTLResidencySet_setCurrentGeneration
[%@ newPrecompiledComputePipelineStateWithDescriptor:%@ options:%@ pipelineCache:%@ completionHandler:%@]
[%@ buildAccelerationStructure:%@ descriptor:%@ scratchBuffer:%@ scratchBufferOffset:%@]
kDYFEMTLFunction_newFunctionWithPluginData_bitcodeType
texture-views
MTLCurveBasisBezier
180DegreesClockwise
kDYFEMTLBuffer_timeSinceTouched
kDYFEMTLCommandBuffer_setLabel
kDYFEMTLComputeCommandEncoder_setStageInRegionWithIndirectBuffer_indirectBufferOffset
[%@ bitCodeWithHash:%@]
MTLRenderTileArgument
MTLArgumentBuffersTier2
Validation
MTLTextureTypeTextureBuffer
[%@ setSeparateCommits:%@]
[%@ beginScope]
[%@ setFragmentVisibleFunctionTables:%@ withBufferRange:%@]
Sample
MPSExternalMatrixVectorMultiplication
kDYFEMTLIndirectRenderCommand_drawPatches_patchStart_patchCount_patchIndexBuffer_patchIndexBufferOffset_instanceCount_baseInstance_tessellationFactorBuffer_tessellationFactorBufferOffset_tessellationFactorBufferInstanceStride_tessellationFa
MTLCommandEncoderErrorStateFaulted
MTLDataTypeULong2
RGBA32Float
MTLVertexFormatUChar3
kDYFEMTLRenderCommandEncoder_setObjectSamplerState_lodMinClamp_lodMaxClamp_atIndex
RestoreMTLBufferContents
MTLAllocationTypeHeap
MTLCompilerTestModeDefault
BGR10_XR_sRGB
MTLPixelFormatYCBCR10_444_1P_PQ
16
kDYFEMTLCommandBuffer_parallelRenderCommandEncoderWithDescriptor
kDYFEMTLComputeCommandEncoder_dispatchThreads_threadsPerThreadgroup
kDYFEMTLFunctionPrivateArgument_dealloc
[%@ refitAccelerationStructure:%@ descriptor:%@ destination:%@ scratchBuffer:%@ scratchBufferOffset:%@ options:%@]
BlendAlpha
MTLIOPriorityLow
MTLPipelineOptionBufferTypeInfo
MTLStoreActionStoreAndMultisampleResolve
kDYFEMTLAccelerationStructureCommandEncoder_dealloc
kDYFEMTLCaptureManager_startCaptureWithDevice
[%@ setDepthResolveTexture:%@ slice:%@ depthPlane:%@ level:%@ yInvert:%@]
Flat
MTLMessageTypeDebugError
R16Bfloat
PerPatchControlPoint
kDYFEMTLRenderCommandEncoder_setTileSamplerStates_lodMinClamps_lodMaxClamps_withRange
[%@ makeAliasable]
MTLCurveEndCapsDisk
BFloat2x3
kDYFEMTLCommandQueue_setProfilingEnabled
kDYFEMTLComputeCommandEncoder_setFunctionTable_atIndex
kDYFEMTLRenderPipelineState_functionHandleWithFunction_stage
AccelerationStructureState
kDYFEMTLDevice_compileVisibleFunction_withDescriptor_destinationBinaryArchive_error
kDYFEMTLDevice_resolveCountersWithIndexRange_sampleBuffer
[%@ setIndirectCommandBuffers:%@ withRange:%@]
[%@ setMeshSamplerState:%@ atIndex:%@]
activePerEncoderDrawCallCount
EarlyExit
AtStageBoundary
MTLLogicOperationRevAnd
ASTC_10x6_LDR
MTLPixelFormatRGB10A8_2P
Volatile
MTLCaptureScope
RG10Uint_PACKED
MTLPixelFormatFlagsIsWriteable
MTLTransformFeedbackActive
kDYFEMTLArgumentEncoder_setComputePipelineStates_withRange
kDYFEMTLComputeCommandEncoder_encodeStartIf_offset_comparison_referenceValue
kDYFEMTLResidencySet_commitResidency
[%@ setObjectSamplerState:%@ lodMinClamp:%@ lodMaxClamp:%@ atIndex:%@]
MTLDataTypeFloat3x3
PrivateCompileTimeStatistics
ETC2_RGB8A1
store action shader info
Equal
MTLTextureCompressionFootprintLevel3
MTLCounterSampleBuffer
[%@ newComputePipelineDescriptorWithSerializedData:%@ deserializationContext:%@]
[%@ setEmulationMeshShaderIntermediateBufferSlot:%@]
MTLBuiltInMesh
MTLPixelFormatETC2_RGB8_sRGB
RGBA32Uint
kDYFEMTLCommandBuffer_sampledComputeCommandEncoderWithDescriptor_programInfoBuffer_capacity
kDYFEMTLDevice_setGPUAssertionsEnabled
kDYFEMTLIntersectionFunctionTable_setOpaqueCurveIntersectionFunctionWithSignature_atIndex
kDYFEMTLIntersectionFunctionTable_setVisibleFunctionTables_withBufferRange
MTLBlendFactorDestinationAlpha
MTLPixelFormatYCBCR10_444_1P_sRGB
kDYFEMTLBlitCommandEncoder_invalidateCompressedTexture
kDYFEMTLLibrary_newFunctionWithDescriptor_completionHandler
[%@ renderCommandEncoderWithDescriptor:%@]
[%@ encodeBatchToCommandBuffer:%@ computeCommandEncoder:%@ options:%@ pluginOptions:%@ primaryTextures:%@ primaryInfo:%@ secondaryTextures:%@ secondaryInfo:%@ weightsGradient:%@ biasesGradient:%@ accumulate:%@ predicationBuffer:%@ predicati
YCBCR10_422_2P_PACKED_PQ
MTLVertexFormatChar
kDYFEMTLBlitCommandEncoder_resolveCounters_inRange_destinationBuffer_destinationOffset
kDYFEMTLComputeCommandEncoder_encodeEndWhile
kDYFEMTLDevice_newLibraryWithStitchedDescriptor_error
[%@ addAllocation:%@]
float
UnsupportedTextureUsageShaderWrite
kDYFEMTLDevice_newLibraryWithCIFiltersForComputePipeline_imageFilterFunctionInfo_error
kDYFEMTLFunction_functionConstantIndexByName_type
[%@ resetCommandsInBuffer:%@ withRange:%@]
[%@ fillTexture:%@ level:%@ slice:%@ region:%@ bytes:%@ length:%@]
MTLAttributeFormatInt2
MTLLibraryErrorFileNotFound
YCBCR12_444_2P_PACKED_PQ
2DMultisampleArray
MPSExternalCNNConvolution
kDYFEMTLDevice_compileVisibleFunction_withDescriptor_completionHandler
[%@ supportsVersion:%@]
[%@ setMeshVisibleFunctionTables:%@ withBufferRange:%@]
MTLDataTypeInt
kDYFEMTLDevice_newRenderPipelineStateWithDescriptor_completionHandler
    Supported GPU families:
CharNormalized
MTLDynamicLibraryErrorInvalidFile
MTLPixelFormatR16Snorm
StorageModePrivate
kDYFEMTLBlitCommandEncoder_updateFence
kDYFEMTLCommandBuffer_setSharedIndirectionTable
MTLArgumentTypePrivateIndirectCommandBuffer
InternalError
MTLDataTypeRG16Snorm
MTLPixelFormatYCBCR10_420_2P_PACKED
kDYFEMTLCommandBuffer_popDebugGroup
[%@ addBinaryEntry:%@]
[%@ loadDynamicLibrariesForFunction:%@ insertLibraries:%@ options:%@ error:%@]
[%@ newIntersectionFunctionTableWithDescriptor:%@ stage:%@]
EnableAssertions
kDYFEMTLRenderPipelineState_newVisibleFunctionTableFromFragmentStageWithDescriptor
IntersectionFunctionTableUniqueIdentifier
GreaterEqual
MTLPixelFormatASTC_8x6_sRGB
MTLPixelFormatFlagsIsBlendable
MTLTextureType3D
MTLVertexFormatUShort4
kDYFEMTLRenderCommandEncoder_setTessellationFactorBuffer_offset_instanceStride
kDYFEMTLResourceStateCommandEncoder_waitForFence
kDYFEMTLTexture_makeAliasable
MTLDataTypeHalf
kDYFEMTLDevice_convertSparseTileRegions_toPixelRegions_withTileSize_numRegions
kDYFENSHMDMetalSession_setDrawableSize
[%@ setBackgroundTrackingPID:%@]
[%@ commitAndHold]
[%@ newProfileWithExecutionSize:%@]
MTLPixelFormatASTC_5x5_HDR
MTLAttributeFormatInt3
MTLAttributeFormatShort
MTLGPUFamilyCommon1
MTLTransformTypePackedFloat4x3
kDYFEMTLBlitCommandEncoder_resetTextureAccessCounters_region_mipLevel_slice
kDYFEMTLMotionEstimationPipeline_dealloc
kDYFEMTLResidencySet_addResources_count
Char8
Quad
MTLPixelFormatYCBCR8_444_2P_sRGB
MTLSparsePageSize16
kDYFEMTLCommandQueue_setBackgroundGPUPriority_offset
[%@ dispatchBarrier]
[%@ blitCommandEncoderWithDescriptor:%@]
[%@ setIntersectionFunctionTables:%@ withBufferRange:%@]
MTLPixelFormatYCBCR10_422_2P_XR
MTLTextureRotation270DegreesClockwise
IsSRGB
MTLLanguageVersion1_0
MTLDataTypeFloat2
Ciululbbbul
MTLDataTypeArray
kDYFEMTLIntersectionFunctionTable_setOpaqueTriangleIntersectionFunctionWithSignature_withRange
BGRG422
AGX
MTLBindingTypeObjectPayload
ASTC_12x10_HDR
MTLPixelFormatBGRA10_XR_PACKED
MTLValidationCodeIOCommandBuffer
[%@ indirectComputeCommandAtIndex:%@]
RG8Unorm
AtomicFetchOr
kDYFEMTLDevice_newSamplerStateWithDescriptor
R8Snorm
kDYFEMTLAccelerationStructureCommandEncoder_serializeInstanceAccelerationStructure_primitiveAccelerationStructures_toBuffer_serializedBufferOffset
kDYFEMTLRasterizationRateMap_screenCoordinate_forLayer
MTLAccelerationStructureUsageExtendedLimits
UChar2Normalized
MTLCurveAdjacencyEnd
QuadStrip
kDYFEMTLArgumentEncoder_setIntersectionFunctionTable_atIndex
kDYFEMTLDeserializationContext_dealloc
kDYFEMTLFragmentRenderCommandEncoder_setFragmentSamplerState_atIndex
[%@ memoryBarrierWithScope:%@ afterStages:%@ beforeStages:%@]
MTLPixelFormatRGB10A8_2P_HLG
kDYFEMTLIndirectComputeCommand_setKernelBuffer_offset_attributeStride_atIndex
kDYFEMTLRenderCommandEncoder_setVertexSamplerStates_lodMinClamps_lodMaxClamps_withRange
ASTC_10x5_sRGB
kDYFEMTLBinaryArchive_addMeshRenderPipelineFunctionsWithDescriptor_options_error
kDYFEMTLRenderCommandEncoder_setObjectSamplerState_atIndex
GreaterThanOrEqual
MTLIOCompressionMethodLZ4
kDYFEMTLCommandBuffer_setResponsibleTaskIDs_count
#include <metal_stdlib>\nusing namespace metal;\n\nstruct VertexOutput\n{\n    vec<float, 4> pos [[position]];\n    vec<float, 2> uv;\n};\n\n\nfragment %@ texturedQuadFragment(VertexOutput in [[ stage_in ]],\n                               
Serial
MTLDispatchTypeSerial
MTLLogicOperationInvOr
kDYFEMTLIntersectionFunctionTable_allocationID
kDYFEMTLTexture_saveSlice_level_zPlane_normalize_blitOption_toPath
[%@ end]
[%@ newDynamicLibrary:%@ computeDescriptor:%@ error:%@]
RGBA8Snorm
tvOS_GPUFamily1_v1
Copy
kDYFEMTLRenderCommandEncoder_setMeshVisibleFunctionTable_atBufferIndex
[%@ setMetalAssertionsEnabled:%@]
[%@ newFunctionWithName:%@]
YCBCR12_444_2P_HLG
kDYFEMTLIndirectCommandBuffer_makeAliasable
[%@ newMatrixFullyConnected]
Bezier
YCBCR12_420_2P_PACKED_HLG
kDYFEMTLComputeCommandEncoder_useResourceGroup_usage
kDYFEMTLDevice_newCommandQueueWithMaxCommandBufferCount
[%@ setPreExposure:%@]
[%@ exportWeightsAndBiasesWithCommandBuffer:%@ encoder:%@ weights:%@ weightsDataType:%@ biases:%@ predicationBuffer:%@ predicationOffset:%@ ]
MTLTextureUsageVideo
[%@ setShaderDebugInfoCaching:%@]
[%@ computeCommandEncoderWithDescriptor:%@]
Address
VertexFunction
kDYFEMPSExternalNDArrayBinaryGradient_encodeSecondaryGradientToCommandBuffer_encoder_options_pluginOptions_primaryBuffer_primaryInfo_secondaryBuffer_secondaryInfo_gradientBuffer_gradientInfo_destination_destinationInfo_accumulate_predicatio
[%@ setStageInRegionWithIndirectBuffer:%@ indirectBufferOffset:%@]
[%@ concurrentDispatchThreadgroups:%@ threadsPerThreadgroup:%@]
BGRA10Unorm
kDYFEMTLBuffer_setResponsibleProcess
MTLPixelFormatBGR10_XR
[%@ setStencilFrontReferenceValue:%@ backReferenceValue:%@]
MTLBindingTypeImageblock
DenormBit
RGBX16Sint
MTLTextureUsageRenderTarget
kDYFEMTLArgumentEncoder_setIndirectCommandBuffer_atIndex
kDYFEMTLSamplerState_resourceIndex
[%@ setVertexTextures:%@ withRange:%@]
device:0x%llx, queue:0x%llx, toolsQueue:0x%llx, label:%@, canBeCaptured:%@, isOpenGL:%@, isInternal: %@
RandomLocation
kDYFEMTLRenderCommandEncoder_useResource_usage
[%@ encodeBatchToCommandBuffer:%@ computeCommandEncoder:%@ options:%@ pluginOptions:%@ primaryTextures:%@ primaryInfo:%@ secondaryTextures:%@ secondaryInfo:%@ destinationTextures:%@ destinationInfo:%@ predicationBuffer:%@ predicationOffset:
PrivateStruct
MTLDataTypeVector
MTLPixelFormatFlagsIsASTC
kDYFEMTLBuffer_saveContentsToPath
[%@ newTextureLayoutWithDescriptor:%@ isHeapOrBufferBacked:%@]
MTLPixelFormatASTC_5x4_HDR
kDYFEMPSExternalCNNConvolutionGradient_encodeBatchToCommandBuffer_computeCommandEncoder_options_pluginOptions_primaryTextures_primaryInfo_secondaryTextures_secondaryInfo_weightsGradient_biasesGradient_accumulate_predicationBuffer_predicatio
kDYFEMTLDevice_sampleTimestamps_gpuTimestamp
[%@ doCorruptCBSPI:%@]
[%@ memoryBarrierWithResources:%@ count:%@ afterStages:%@ beforeStages:%@]
[%@ setComputePipelineState:%@ atIndex:%@]
MTLCommandEncoderErrorStateCompleted
RG16Unorm
[%@ setVertexBufferOffset:%@ atIndex:%@]
[%@ startCollectingPipelineDescriptors]
.xyzw
MTLTextureColorSpaceConversionMatrixUtil1
kDYFECAMetalLayer_setPresentsWithTransaction
kDYFEMTLPipelineLibrary_setDisableRunTimeCompilation
[%@ newFunctionWithName:%@ constantValues:%@ pipelineLibrary:%@ completionHandler:%@]
Imageblock
YCBCR8_420_2P
kDYFEMTLIntersectionFunctionTable_setVisibleFunctionTable_atBufferIndex
kDYFEMTLRenderCommandEncoder_setTileBuffer_offset_atIndex
[%@ copyFromTexture:%@ sourceSlice:%@ sourceLevel:%@ sourceOrigin:%@ sourceSize:%@ toTexture:%@ destinationSlice:%@ destinationLevel:%@ destinationOrigin:%@]
None
Info
MTLPixelFormatASTC_6x6_HDR
UnsupportedDevice
_MTLArgumentBufferResourceTypeIntersectionFunctionTable
kDYFEMTLBlitCommandEncoder_copyFromBuffer_sourceOffset_toBuffer_destinationOffset_size
kDYFEMTLDevice_newFence
kDYFEMTLDevice_unmapShaderSampleBuffer
BGR10A2Unorm_sRGB
RGB10_444_2P
YCBCR10_444_1P_HLG
kDYFEMPSExternalMatrixFullyConnected_encodeToCommandBuffer_encoder_options_batchSize_inputMatrix_inputMatrixInfo_weightMatrix_weightMatrixInfo_biasVector_biasVectorInfo_resultMatrix_resultMatrixInfo_alpha_numberOfFeatureVectors_inputFeature
kDYFEMTLCommandBuffer_encodeIndirectArgumentsForBuffer_data
[%@ drawIndexedPrimitives:%@ indexCount:%@ indexType:%@ indexBuffer:%@ indexBufferOffset:%@ instanceCount:%@]
[%@ sampleCountersInBuffer:%@ atIndex:%@ allowOverlap:%@]
TextureMipmapInfo
MTLDataTypeIntersectionFunctionTable
MTLPixelFormatYCBCR10_444_2P_PACKED
Private_v1
[%@ newCNNConvolutionWithDescriptor:%@ dataSource:%@ fullyConnected:%@ ]
NoVertexFragmentLinking
MTLDataTypeInt2
ULong
YCBCR10_422_2P_HLG
MTLPixelFormatFlagsIsHLG
MTLPixelFormatFlagsIsLossyLevel1Compatible
MTLTextureCompressionFeedbackUnsupportedPixelFormat
kDYFEMTLDevice_writeMeshShaderEmulatorDataStructureHeader_meshShaderPSO_scalingFactor
MTLBuiltInArgumentPositionInPatch
ThreadsPerQuadgroup
Apple1
MTLPixelFormatRGB10_422_2P
kDYFEMTLIndirectCommandBuffer_setResponsibleProcess
kDYFEMTLRasterizationRateMap_physicalCoordinate_forLayer
[%@ nop]
[%@ startCaptureWithDescriptor:%@ error:%@]
kDYFEMTLLibrary_newFunctionWithName_constantValues_completionHandler
MTLCommandBufferStatusCompleted
MTLPrimitiveTypeTriangleStrip
kDYFEMTLDevice_newComputePipelineStateWithImageFilterFunctionsSPI_imageFilterFunctionInfo_error
[%@ addBarrier]
IndirectCommandBufferUniqueIdentifier
Sample0
MTLPixelFormatDepth24Unorm_Stencil8
MTLStepFunctionThreadPositionInGridY
kDYFEMPSExternalCNNPoolingAverage_encodeBatchToCommandBuffer_computeCommandEncoder_options_sourceTextures_sourceInfo_destinationTextures_destinationInfo_zeroPadSizeX_zeroPadSizeY_predicationBuffer_predicationOffset
kDYFEMTLFragmentRenderCommandEncoder_drawTrianglesWithPositions_vertexCount_vertexVaryings_varyingCountPerVertex_triangleIndices_triangleCount
[%@ sparseTileSizeInBytesForSparsePageSize:%@]
MTLFunctionTypeFragment
kDYFEMTLBuffer_setParentGPUAddress
[%@ addRenderPipelineFunctionsWithDescriptor:%@ error:%@]
MTLColorWriteMaskAll
URLInvalid
Equiv
MTLPixelFormatYCBCR10_422_2P_PACKED_HLG
MTLStackTraceEntry
kDYFEMTLRenderPipelineState_newRenderPipelineStateWithAdditionalBinaryFunctions_error
kDYFEMTLResidencySet_removeHeaps_count
[%@ drawMeshThreadgroups:%@ threadsPerObjectThreadgroup:%@ threadsPerMeshThreadgroup:%@]
Short2Normalized
MTLValidationCodeCommandEncoder
kDYFEMTLHeap_maxAvailableSizeWithAlignment
kDYFEMTLIndirectRenderCommand_endIndirectCommandBuffer
[%@ setVertexBuffers:%@ offsets:%@ attributeStrides:%@ withRange:%@]
MTLArgumentTypePrivateBuiltIn
MTLPrimitiveKindCurve
NotMipmapped
kDYFEMTLBuffer_dealloc
kDYFEMTLFragmentRenderCommandEncoder_popDebugGroup
[%@ getIndirectCommandBufferHeaderSize]
MTLBlendFactorOneMinusSourceAlpha
MTLCaptureDestinationGPUTraceDocument
MTLPipelineOptionPrivateInlinedSymbols
MTLPixelFormatFlagsIsDualPlane
[%@ setPresentsWithTransaction:%@]
MTLSamplerReductionModeMinimum
MTLTextureUsageShaderRead
kDYFEMTLBuffer_indirectCommandBufferData
[%@ setUtilityBuffers:%@]
kDYFEMTLFragmentRenderCommandEncoder_setFragmentSamplerStates_withRange
CompilerPluginRequiresSerializedBitcode
MTLSparseTexturesTier3
YCBCR12_444_2P_XR
kDYFEMTLBlitCommandEncoder_copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_options
kDYFEMTLComputeCommandEncoder_setComputePipelineState
kDYFEMTLIndirectRenderCommand_setVertexBuffer_offset_atIndex
ASTC_8x6_LDR
kDYFEMTLComputeCommandEncoder_setTextures_withRange
[%@ encodeSignalEvent:%@ value:%@ agentMask:%@]
tvOS_GPUFamily1_v4
MTLPixelFormatETC2_RGB8A1
kDYFEMTLRenderCommandEncoder_useResidencySets_count
[%@ writeCompactedAccelerationStructureSize:%@ toBuffer:%@ offset:%@]
SamplerStateUniqueIdentifier
DrawPatches
CurveData
MTLValidationCodeResource
kDYFEMTLArgumentEncoder_setFunctionTable_atIndex
kDYFEMTLIOCommandQueue_dealloc
[%@ newFunctionWithName:%@ constantValues:%@ pipelineLibrary:%@ error:%@]
[%@ setScissorRects:%@ count:%@]
[%@ barrier]
MTLTextureUsagePixelFormatView
kDYFEMTLAccelerationStructureCommandEncoder_sampleCountersInBuffer_atSampleIndex_withBarrier
kDYFEMTLAccelerationStructureCommandEncoder_writeGeometrySizeOfAccelerationStructure_toBuffer_sizeBufferOffset
kDYFEMTLIOCommandQueue_barrier
MTLPixelFormatDepth32Float
kDYFEMTLRenderCommandEncoder_setColorStoreActionOptions_atIndex
kDYFEMTLResidencySet_containsAllocation
[%@ endEncoding]
```
