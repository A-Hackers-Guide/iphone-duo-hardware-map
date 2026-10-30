# `LTMStatsCompute`

- Image: [`/System/Library/PrivateFrameworks/CameraColorProcessing.framework/CameraColorProcessing`](../userland/System__Library__PrivateFrameworks__CameraColorProcessing.framework__CameraColorProcessing.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LTMAlgorithmBase`
- 11 instance variables, 4 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"FigMetalContext" _metalContext;
@"<MTLComputePipelineState>" _calcLTMStatisticsPipelineState;
@"<MTLComputePipelineState>" _calcLocalHistogramShift;
@"<MTLComputePipelineState>" _localHistAndThumKernelPipelineState;
@"<MTLComputePipelineState>" _localHistHiResAndThumKernelPipelineState;
@"<MTLComputePipelineState>" _globalHistKernelPipelineState;
@"<MTLComputePipelineState>" _globalFaceHistKernelPipelineState;
@"<MTLComputePipelineState>" _collectLocalHistKernelPipelineState;
@"<MTLComputePipelineState>" _collectLocalHistHiResKernelPipelineState;
@"<MTLCommandBuffer>" _cmdBuf;
{?="width"Q"height"Q"depth"Q} _threadgroupSize;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[LTMStatsCompute rewriteAntiAliasingCoefficients:];
```

## Instance methods

```
-[LTMStatsCompute purgeResources];
-[LTMStatsCompute waitUntilCompleted];
-[LTMStatsCompute createShaders:];
-[LTMStatsCompute allocateResources];
-[LTMStatsCompute initWithMetalContext:];
-[LTMStatsCompute prewarmShaders];
-[LTMStatsCompute calcExposureRatio:];
-[LTMStatsCompute computeInputParametersForImageWidth:calcGlobalHistOnROI:enableAntiAliasing:with:to:];
-[LTMStatsCompute encodeLTMStatisticsCalculationOptimized:params:globalHistogram:globalFaceHistogram:localHistogram:thumbnail:];
-[LTMStatsCompute encodeLTMStatisticsCalculationPrecise:paramsGlobalHist:globalHistogram:localHistogram:thumbnail:];
```
