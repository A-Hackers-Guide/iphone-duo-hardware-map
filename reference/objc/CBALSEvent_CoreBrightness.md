# `CBALSEvent`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBHIDEvent`
- Protocols: `CBALSEventProtocol`
- 16 instance variables, 22 properties, 37 instance methods, 1 class methods

## Instance variables

```
^{__IOHIDEvent=} _event;
@"NSObject<OS_os_log>" _logHandle;
B _obstructed;
B _supportColor;
B _firstALSSample;
B _colorMitigationTriggered;
f _confidence;
f _integrationTime;
i _orientation;
f _strength;
d _illuminance;
@"<CBALSNodeProtocol>" _node;
{CBChannelAveragedColorVendorData="type"I"channels"[5f]"XYZ"[3f]"history_used"S} _channelAveragedColorVendorData;
{ALSXTalkEstimatesVendorData="type"I"xdxtEstimate"[5f]"bextEstimate"[5f]"xdxtEstimateSet"B"bextEstimateSet"B} _xtalkEstimates;
{CFXColorSample="XYZ"[3f]"xy"{?="x"f"y"f}"CCT1"f"extra"{?="orientation"i"rawChannels"[6f]"nChannels"i"brightness"f}} _colorSample;
{ColorSensorVendorEventData="status"I"nChannels"C"orientation"C"brightness"S"integrationTime"I"reportInterval"I"gain"i"lux"f"rawLux"f"channelData"[6f]"CCT"f"AZOffsets"[6s]"temperature"f"sensorTimestamp"I"sensorType"i"validNSamples"S"asyncMode"B"xtalkEstimate"[6I]"colorCalcOnAOP"B"XYZAP"[3f]"XYZAOP"[3f]"filteredLux"f"filteredLuxSet"B} _vendorData;
```

## Properties

```
@property (Td,R,N) timestamp;
@property (Td,V_illuminance) illuminance;
@property (T{CFXColorSample=[3f]{?=ff}f{?=i[6f]if}},V_colorSample) colorSample;
@property (TB,V_obstructed) obstructed;
@property (T{ColorSensorVendorEventData=ICCSIIiff[6f]f[6s]fIiSB[6I]B[3f][3f]fB},V_vendorData) vendorData;
@property (T{CBChannelAveragedColorVendorData=I[5f][3f]S},V_channelAveragedColorVendorData) channelAveragedColorVendorData;
@property (Tf,V_integrationTime) integrationTime;
@property (TB,V_firstALSSample) firstALSSample;
@property (TB,V_colorMitigationTriggered) colorMitigationTriggered;
@property (T{ALSXTalkEstimatesVendorData=I[5f][5f]BB},V_xtalkEstimates) xtalkEstimates;
@property (TB,V_supportColor) supportColor;
@property (Ti,V_orientation) orientation;
@property (T@"<CBALSNodeProtocol>",R,V_node) node;
@property (Tf,V_confidence) confidence;
@property (Tf,V_strength) strength;
@property (T^{__IOHIDEvent=},R,N) event;
@property (T^{__IOHIDServiceClient=},R,N) service;
@property (TI,R,N) eventType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CBALSEvent replaceLuxWithFilteredLux:];
```

## Instance methods

```
-[CBALSEvent setOrientation:];
-[CBALSEvent obstructed];
-[CBALSEvent setIntegrationTime:];
-[CBALSEvent setSupportColor:];
-[CBALSEvent strength];
-[CBALSEvent initWithHIDEvent:andService:];
-[CBALSEvent channelAveragedColorVendorData];
-[CBALSEvent compare:];
-[CBALSEvent setStrength:];
-[CBALSEvent orientation];
-[CBALSEvent dealloc];
-[CBALSEvent illuminance];
-[CBALSEvent copyVendorDataFromEvent:];
-[CBALSEvent setVendorData:];
-[CBALSEvent setIlluminance:];
-[CBALSEvent setColorMitigationTriggered:];
-[CBALSEvent node];
-[CBALSEvent colorMitigationTriggered];
-[CBALSEvent conformsToEvent:];
-[CBALSEvent setConfidence:];
-[CBALSEvent copyXTalkDataFromEvent:];
-[CBALSEvent setChannelAveragedColorVendorData:];
-[CBALSEvent vendorData];
-[CBALSEvent colorSample];
-[CBALSEvent integrationTime];
-[CBALSEvent getServiceOrientation:];
-[CBALSEvent supportColor];
-[CBALSEvent initWithHIDEvent:andNode:];
-[CBALSEvent xtalkEstimates];
-[CBALSEvent description];
-[CBALSEvent setObstructed:];
-[CBALSEvent setFirstALSSample:];
-[CBALSEvent setColorSample:];
-[CBALSEvent setXtalkEstimates:];
-[CBALSEvent firstALSSample];
-[CBALSEvent confidence];
-[CBALSEvent copyChannelAveragedColorDataFromEvent:];
```
