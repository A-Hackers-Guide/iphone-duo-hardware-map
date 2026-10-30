# `CBALSEventProtocol` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `CBEventProtocol`
- 0 instance variables, 15 properties, 28 instance methods, 0 class methods

## Properties

```
@property (Td,R,N) timestamp;
@property (Td) illuminance;
@property (T{CFXColorSample=[3f]{?=ff}f{?=i[6f]if}}) colorSample;
@property (TB) obstructed;
@property (T{ColorSensorVendorEventData=ICCSIIiff[6f]f[6s]fIiSB[6I]B[3f][3f]fB}) vendorData;
@property (T{CBChannelAveragedColorVendorData=I[5f][3f]S}) channelAveragedColorVendorData;
@property (Tf) integrationTime;
@property (TB) firstALSSample;
@property (TB) colorMitigationTriggered;
@property (T{ALSXTalkEstimatesVendorData=I[5f][5f]BB}) xtalkEstimates;
@property (TB) supportColor;
@property (Ti) orientation;
@property (T@"<CBALSNodeProtocol>",R) node;
@property (Tf) confidence;
@property (Tf) strength;
```

## Instance methods

```
-[CBALSEventProtocol setOrientation:];
-[CBALSEventProtocol obstructed];
-[CBALSEventProtocol setIntegrationTime:];
-[CBALSEventProtocol setSupportColor:];
-[CBALSEventProtocol strength];
-[CBALSEventProtocol channelAveragedColorVendorData];
-[CBALSEventProtocol setStrength:];
-[CBALSEventProtocol orientation];
-[CBALSEventProtocol timestamp];
-[CBALSEventProtocol illuminance];
-[CBALSEventProtocol setVendorData:];
-[CBALSEventProtocol setIlluminance:];
-[CBALSEventProtocol setColorMitigationTriggered:];
-[CBALSEventProtocol node];
-[CBALSEventProtocol colorMitigationTriggered];
-[CBALSEventProtocol setConfidence:];
-[CBALSEventProtocol setChannelAveragedColorVendorData:];
-[CBALSEventProtocol vendorData];
-[CBALSEventProtocol colorSample];
-[CBALSEventProtocol integrationTime];
-[CBALSEventProtocol supportColor];
-[CBALSEventProtocol xtalkEstimates];
-[CBALSEventProtocol setObstructed:];
-[CBALSEventProtocol setFirstALSSample:];
-[CBALSEventProtocol setColorSample:];
-[CBALSEventProtocol setXtalkEstimates:];
-[CBALSEventProtocol firstALSSample];
-[CBALSEventProtocol confidence];
```
