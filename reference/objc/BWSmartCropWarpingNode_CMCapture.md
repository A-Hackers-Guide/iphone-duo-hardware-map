# `BWSmartCropWarpingNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- Protocols: `BWDynamicAspectRatioChangeSource`
- 5 instance variables, 5 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"<BWSmartCropHomographyProvider>" _homographyProvider;
@"<RTSCProcessor>" _rtscProcessor;
i _activeAspectRatio;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _bufferServicingLock;
{?="width"i"height"i} _activeFormatDimensions;
```

## Properties

```
@property (Ti,V_activeAspectRatio) activeAspectRatio;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWSmartCropWarpingNode initialize];
```

## Instance methods

```
-[BWSmartCropWarpingNode prepareForCurrentConfigurationToBecomeLive];
-[BWSmartCropWarpingNode renderSampleBuffer:forInput:];
-[BWSmartCropWarpingNode _updateOutputRequirements];
-[BWSmartCropWarpingNode dealloc];
-[BWSmartCropWarpingNode _updateDetectedObjectsInfo:];
-[BWSmartCropWarpingNode activeAspectRatio];
-[BWSmartCropWarpingNode didSelectFormat:forInput:forAttachedMediaKey:];
-[BWSmartCropWarpingNode setActiveAspectRatio:];
-[BWSmartCropWarpingNode _initRTSCProcessorWithOutputDimensions:];
```
