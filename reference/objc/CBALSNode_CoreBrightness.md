# `CBALSNode`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBHIDService`
- Protocols: `CBALSNodeProtocol`
- 18 instance variables, 27 properties, 37 instance methods, 2 class methods

## Instance variables

```
B _occlusionDrivesGrimaldi;
B _useProxForOcclusion;
B _supportsFloatLux;
B _colorSupport;
B _colorMitigation;
B _angleDependent;
I _orientation;
I _placement;
i _slowIntegrationTime;
i _fastIntegrationTime;
i _superFastIntegrationTime;
i _sensorType;
i _ceModel;
f _ceThreshold;
Q _digitizerLocationID;
Q _location;
@"CBALSHotspotLocation" _overrideHotspot;
q _digitizerFilterWindow;
```

## Properties

```
@property (TI,R,N,V_orientation) orientation;
@property (TI,R,N,V_placement) placement;
@property (TQ,R,N,V_location) location;
@property (T@"CBALSHotspotLocation",R,N,V_overrideHotspot) overrideHotspot;
@property (Tq,R,N,V_digitizerFilterWindow) digitizerFilterWindow;
@property (TB,R,N,V_useProxForOcclusion) useProxForOcclusion;
@property (TB,R,N,V_supportsFloatLux) supportsFloatLux;
@property (Ti,R,N,V_slowIntegrationTime) slowIntegrationTime;
@property (Ti,R,N,V_fastIntegrationTime) fastIntegrationTime;
@property (Ti,R,N,V_superFastIntegrationTime) superFastIntegrationTime;
@property (TB,R,N) useCopyEventOnDisplayWake;
@property (Ti,R,N,V_sensorType) sensorType;
@property (TB,R,N,V_colorSupport) colorSupport;
@property (TB,R,N,V_colorMitigation) colorMitigation;
@property (TB,R,N,V_angleDependent) angleDependent;
@property (Ti,R,N,V_ceModel) ceModel;
@property (Tf,R,N,V_ceThreshold) ceThreshold;
@property (TB,R,N) builtIn;
@property (T^{__IOHIDServiceClient=},R,N) service;
@property (TI,R,N) ioService;
@property (TQ,R,N) serviceID;
@property (TQ,R,N,V_digitizerLocationID) digitizerLocationID;
@property (TB,R,N,V_occlusionDrivesGrimaldi) occlusionDrivesGrimaldi;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CBALSNode nodeForService:];
+[CBALSNode matchingCriteria];
```

## Instance methods

```
-[CBALSNode getSupportsFloatLuxValue];
-[CBALSNode angleDependent];
-[CBALSNode setReportInterval:];
-[CBALSNode supportsFloatLux];
-[CBALSNode sensorType];
-[CBALSNode placement];
-[CBALSNode fastIntegrationTime];
-[CBALSNode location];
-[CBALSNode colorSupport];
-[CBALSNode orientation];
-[CBALSNode dealloc];
-[CBALSNode getOcclusionDrivesGrimaldi];
-[CBALSNode isEqualToCBALSNode:];
-[CBALSNode getDigitizerFilterWindow];
-[CBALSNode superFastIntegrationTime];
-[CBALSNode initALSProperties];
-[CBALSNode getUseProxForOcclusion];
-[CBALSNode getAngleDependent];
-[CBALSNode useCopyEventOnDisplayWake];
-[CBALSNode initWithALSServiceClient:];
-[CBALSNode digitizerFilterWindow];
-[CBALSNode copyEvent];
-[CBALSNode copyALSEvent];
-[CBALSNode description];
-[CBALSNode getDigitizerLocationID];
-[CBALSNode getReportInterval];
-[CBALSNode copyHotspotLocation];
-[CBALSNode occlusionDrivesGrimaldi];
-[CBALSNode ceModel];
-[CBALSNode digitizerLocationID];
-[CBALSNode colorMitigation];
-[CBALSNode slowIntegrationTime];
-[CBALSNode isColorSupported];
-[CBALSNode overrideHotspot];
-[CBALSNode copyALSEventWithinTimeout:];
-[CBALSNode useProxForOcclusion];
-[CBALSNode ceThreshold];
```
