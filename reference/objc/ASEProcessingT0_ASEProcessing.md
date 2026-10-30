# `ASEProcessingT0`

- Image: [`/System/Library/PrivateFrameworks/ASEProcessing.framework/ASEProcessing`](../userland/System__Library__PrivateFrameworks__ASEProcessing.framework__ASEProcessing.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 19 instance variables, 0 properties, 25 instance methods, 0 class methods

## Instance variables

```
Q _numberOfRequestedFrames;
Q _numberOfScheduledFrames;
Q _numberOfProcessedFrames;
I _asePlatform;
i _aseProcessingVersion;
I _aseProcessingType;
I _inputWidth;
I _inputHeight;
@"NSObject<OS_dispatch_queue>" _scheduleQueue;
@"NSObject<OS_dispatch_queue>" _completionQueue;
@"NSObject<OS_dispatch_semaphore>" _scheduleSemaphone;
{?="step_size"I"FD_state"I"FG_count"I"NFG_count"I"prev_H1_7"I"prev_V1_7"I"prev_ratio_2D_1D"I} _dc_state;
I _productType;
f _enhancementStrength;
I _destinationWidth;
I _destinationHeight;
B _inputType;
{?="FG_value"i"FG_level_count"[5i]} _prev_temporal_context;
^{aseConfigurationUnitsV2_t={MSRHcuHeader_t=II}{MSRHcuEntryHeader_t=II}{?={?=(?={?=iIB(?={?=BI{?=III}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIIII}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIII}{?={?=II}{?=III}}})})}}{MSRHcuEntryHeader_t=II}{?=I}{MSRHcuEntryHeader_t=II}{?={?=fffff}}{MSRHcuEntryHeader_t=II}{?={?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}}{MSRHcuEntryHeader_t=II}{?={?=IIIII}{?=IIIII}{?=IIIII}}{MSRHcuEntryHeader_t=II}{?=[4{?=b11b11b10}][4{?=b12b12b8}][4{?=b11b11b10}]}} _aseControlUnit;
```

## Instance methods

```
-[ASEProcessingT0 dealloc];
-[ASEProcessingT0 setInputType:];
-[ASEProcessingT0 processFrameWithInput:Measurement:outputData:];
-[ASEProcessingT0 setDestinationHeight:];
-[ASEProcessingT0 setDestinationWidth:];
-[ASEProcessingT0 setEnhancementStrength:];
-[ASEProcessingT0 DumpOutputHcus:];
-[ASEProcessingT0 configControlHeader_V1:];
-[ASEProcessingT0 configControlHeader_V2:];
-[ASEProcessingT0 digitalZoomSelectControl_V1:];
-[ASEProcessingT0 digitalZoomSelectControl_V2:];
-[ASEProcessingT0 getDestinationHeight];
-[ASEProcessingT0 getDestinationWidth];
-[ASEProcessingT0 getEnhancementStrength];
-[ASEProcessingT0 initWithConfig:aseProcessing:productType:];
-[ASEProcessingT0 printAseMeasurementOutput:];
-[ASEProcessingT0 processFrameWithInput:Measurement:Output:];
-[ASEProcessingT0 processFrameWithInput:Measurement:callback:];
-[ASEProcessingT0 processPixelWithInput:Measurement:controlUnit:];
-[ASEProcessingT0 processPixelWithInput_V1:Measurement:Output:];
-[ASEProcessingT0 processPixelWithInput_V2:Measurement:Output:];
-[ASEProcessingT0 processPixelWithMeasurement_V1:Measurement:pixelControl:];
-[ASEProcessingT0 processPixelWithMeasurement_V2:Measurement:Output:];
-[ASEProcessingT0 processPixelWithPixelControl_V1:Output:];
-[ASEProcessingT0 processPixelWithPixelControl_V2:Output:];
```
