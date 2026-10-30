# `ASEProcessingT1`

- Image: [`/System/Library/PrivateFrameworks/ASEProcessing.framework/ASEProcessing`](../userland/System__Library__PrivateFrameworks__ASEProcessing.framework__ASEProcessing.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ASEProcessingT0`
- 3 instance variables, 0 properties, 21 instance methods, 0 class methods

## Instance variables

```
I _enabledHcus;
^{aseConfigurationUnitsV3_t={MSRHcuHeader_t=II}{MSRHcuEntryHeader_t=II}{?=IIIIII}{MSRHcuEntryHeader_t=II}{?=[4[32f]]}{MSRHcuEntryHeader_t=II}{?=I{?=[32{?=fff}]}{?=[32{?=fff}]}{?=[32{?=fff}]}{?=IIIII}[2i][3i][4i][5i][6i][7i]}{MSRHcuEntryHeader_t=II}{?=[5{?=[32{?=fff}]}]{?=III}[13{?=II}][6{?=III}]}{MSRHcuEntryHeader_t=II}{?=[4{?=[32{?=fff}]}]{?=IIII}}{MSRHcuEntryHeader_t=II}{?=II}{MSRHcuEntryHeader_t=II}{?={?={?=II}{?=III}}}} _aseControlUnitV3;
^{?={?=I^{_ASEHcuCacheNodeCommon}^{_ASEHcuCacheNodeCommon}{?=QQQ}}{?=I^{_ASEHcuCacheNodeCommon}^{_ASEHcuCacheNodeCommon}{?=QQQ}}{?=I^{_ASEHcuCacheNodeCommon}^{_ASEHcuCacheNodeCommon}{?=QQQ}}} _aseControlUnitV3Cache;
```

## Instance methods

```
-[ASEProcessingT1 dealloc];
-[ASEProcessingT1 processFrameWithInput:Measurement:outputData:];
-[ASEProcessingT1 DumpOutputHcus:];
-[ASEProcessingT1 DumpAnnotatedOutputHcus:Hcu:Size:];
-[ASEProcessingT1 DumpFloatArray:array:count:numberPerRow:];
-[ASEProcessingT1 parseHcuDataIntoArray:Hcu:Size:];
-[ASEProcessingT1 DumpOutputHcuHeaders:];
-[ASEProcessingT1 DumpArray:type:array:count:numberPerRow:];
-[ASEProcessingT1 DumpIntArray:array:count:numberPerRow:];
-[ASEProcessingT1 DumpPiecewiseLinearCurveV3:curve:];
-[ASEProcessingT1 DumpRawOutputHcus:Hcu:Size:];
-[ASEProcessingT1 DumpUintArray:array:count:numberPerRow:];
-[ASEProcessingT1 configControlHeader_V3:];
-[ASEProcessingT1 initWithConfig:aseProcessing:productType:];
-[ASEProcessingT1 populateOutputHcus:];
-[ASEProcessingT1 printAseMeasurementOutput:];
-[ASEProcessingT1 processFrameWithInput:Measurement:callback:];
-[ASEProcessingT1 processPixelWithInput:Measurement:controlUnitV3:];
-[ASEProcessingT1 processPixelWithInput_V3:Measurement:Output:];
-[ASEProcessingT1 processPixelWithMeasurement_V3:Measurement:Output:];
-[ASEProcessingT1 processPixelWithPixelControl_V3:Output:];
```
