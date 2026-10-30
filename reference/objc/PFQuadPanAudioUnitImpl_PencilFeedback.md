# `PFQuadPanAudioUnitImpl`

- Image: [`/System/Library/PrivateFrameworks/PencilFeedback.framework/PencilFeedback`](../userland/System__Library__PrivateFrameworks__PencilFeedback.framework__PencilFeedback.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AUAudioUnit`
- 8 instance variables, 3 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"AUAudioUnitBusArray" _inputBusArray;
@"AUAudioUnitBusArray" _outputBusArray;
@"AUParameterTree" _parameterTree;
{vector<float, std::allocator<float>>="__begin_"^f"__end_"^f""{?="__cap_"^f}} _previousGains;
{vector<float, std::allocator<float>>="__begin_"^f"__end_"^f""{?="__cap_"^f}} _currentGains;
f _horizontalPan;
f _verticalPan;
q _algorithm;
```

## Properties

```
@property (Tf,N,V_horizontalPan) horizontalPan;
@property (Tf,N,V_verticalPan) verticalPan;
@property (Tq,N,V_algorithm) algorithm;
```

## Instance methods

```
-[PFQuadPanAudioUnitImpl initWithComponentDescription:options:error:];
-[PFQuadPanAudioUnitImpl algorithm];
-[PFQuadPanAudioUnitImpl setAlgorithm:];
-[PFQuadPanAudioUnitImpl deallocateRenderResources];
-[PFQuadPanAudioUnitImpl allocateRenderResourcesAndReturnError:];
-[PFQuadPanAudioUnitImpl channelCapabilities];
-[PFQuadPanAudioUnitImpl inputBusses];
-[PFQuadPanAudioUnitImpl internalRenderBlock];
-[PFQuadPanAudioUnitImpl outputBusses];
-[PFQuadPanAudioUnitImpl parameterTree];
-[PFQuadPanAudioUnitImpl shouldChangeToFormat:forBus:];
-[PFQuadPanAudioUnitImpl setVerticalPan:];
-[PFQuadPanAudioUnitImpl horizontalPan];
-[PFQuadPanAudioUnitImpl setHorizontalPan:];
-[PFQuadPanAudioUnitImpl setupParameterTree];
-[PFQuadPanAudioUnitImpl verticalPan];
```
