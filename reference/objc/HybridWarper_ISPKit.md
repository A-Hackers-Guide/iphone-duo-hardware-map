# `HybridWarper`

- Image: [`/System/Library/PrivateFrameworks/ISPKit.framework/ISPKit`](../userland/System__Library__PrivateFrameworks__ISPKit.framework__ISPKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 11 properties, 27 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_os_log>" _logger;
@"NSMapTable" _bilateralGrids;
B _computeFrameStatsUsingGPU;
@"<MTLCommandQueue>" _commandQueue;
@"<MTLDevice>" _device;
^{__CVMetalTextureCache=} _textureCache;
@"YUV6ChSplitterEncoder" _yuvSplitterEncoder;
@"YUV6ChJoinerEncoder" _yuvJoinerEncoder;
@"GenerateSparseBlendingMapEncoder" _generateSparseBlendingMapEncoder;
@"WarpFrameWithBlendingWeightEncoder" _warpFrameWithBlendingWeightEncoder;
@"ApplyPersonMaskModulationEncoder" _applyPersonMaskModulationEncoder;
@"FlowMaskSumReduceEncoder" _flowMaskSumReduceEncoder;
@"HybridWarperBufferManager" _bufferManager;
```

## Properties

```
@property (T@"<MTLCommandQueue>",&,N,V_commandQueue) commandQueue;
@property (T@"<MTLDevice>",&,N,V_device) device;
@property (T^{__CVMetalTextureCache=},N,V_textureCache) textureCache;
@property (TB,N,V_computeFrameStatsUsingGPU) computeFrameStatsUsingGPU;
@property (T@"YUV6ChSplitterEncoder",&,N,V_yuvSplitterEncoder) yuvSplitterEncoder;
@property (T@"YUV6ChJoinerEncoder",&,N,V_yuvJoinerEncoder) yuvJoinerEncoder;
@property (T@"GenerateSparseBlendingMapEncoder",&,N,V_generateSparseBlendingMapEncoder) generateSparseBlendingMapEncoder;
@property (T@"WarpFrameWithBlendingWeightEncoder",&,N,V_warpFrameWithBlendingWeightEncoder) warpFrameWithBlendingWeightEncoder;
@property (T@"ApplyPersonMaskModulationEncoder",&,N,V_applyPersonMaskModulationEncoder) applyPersonMaskModulationEncoder;
@property (T@"FlowMaskSumReduceEncoder",&,N,V_flowMaskSumReduceEncoder) flowMaskSumReduceEncoder;
@property (T@"HybridWarperBufferManager",&,N,V_bufferManager) bufferManager;
```

## Instance methods

```
-[HybridWarper setCommandQueue:];
-[HybridWarper setDevice:];
-[HybridWarper device];
-[HybridWarper dealloc];
-[HybridWarper textureCache];
-[HybridWarper commandQueue];
-[HybridWarper setTextureCache:];
-[HybridWarper applyPersonMaskModulationEncoder];
-[HybridWarper bufferManager];
-[HybridWarper computeFlowStatsCPU:personMask:inputValidRect:personMaskValueThreshold:homography:outFlowBackgroundMean:outFlowMean:];
-[HybridWarper computeFrameStatsUsingGPU];
-[HybridWarper computePersonMaskSumCPU:inputValidRect:];
-[HybridWarper encodeToCommandBuffer:tuningGroup:homography:currentY_mipmap:historyY_mipmap:history_YUV:anstRawMask:opticalFlow:warped_YUV:totalGain:flowThresholdScaler:inputValidRect:isHomographyReliable:isTripodDetected:];
-[HybridWarper flowMaskSumReduceEncoder];
-[HybridWarper generateSparseBlendingMapEncoder];
-[HybridWarper initWithCommandQueue:textureCache:band0Size:band1Size:opticalFlowSize:blendingMapSize:];
-[HybridWarper setApplyPersonMaskModulationEncoder:];
-[HybridWarper setBufferManager:];
-[HybridWarper setComputeFrameStatsUsingGPU:];
-[HybridWarper setFlowMaskSumReduceEncoder:];
-[HybridWarper setGenerateSparseBlendingMapEncoder:];
-[HybridWarper setWarpFrameWithBlendingWeightEncoder:];
-[HybridWarper setYuvJoinerEncoder:];
-[HybridWarper setYuvSplitterEncoder:];
-[HybridWarper warpFrameWithBlendingWeightEncoder];
-[HybridWarper yuvJoinerEncoder];
-[HybridWarper yuvSplitterEncoder];
```
