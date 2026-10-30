# `CBALSNodeProtocol` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `CBEventServiceProtocol`
- 0 instance variables, 18 properties, 24 instance methods, 0 class methods

## Properties

```
@property (TI,R,N) orientation;
@property (TI,R,N) placement;
@property (TQ,R,N) location;
@property (TB,R,N) builtIn;
@property (T^{__IOHIDServiceClient=},R,N) service;
@property (TI,R,N) ioService;
@property (TQ,R,N) serviceID;
@property (T@"CBALSHotspotLocation",R,N) overrideHotspot;
@property (Tq,R,N) digitizerFilterWindow;
@property (TQ,R,N) digitizerLocationID;
@property (TB,R,N) useProxForOcclusion;
@property (TB,R,N) supportsFloatLux;
@property (Ti,R,N) slowIntegrationTime;
@property (Ti,R,N) fastIntegrationTime;
@property (Ti,R,N) superFastIntegrationTime;
@property (TB,R,N) colorSupport;
@property (TB,R,N) useCopyEventOnDisplayWake;
@property (TB,R,N) occlusionDrivesGrimaldi;
```

## Instance methods

```
-[CBALSNodeProtocol setReportInterval:];
-[CBALSNodeProtocol supportsFloatLux];
-[CBALSNodeProtocol placement];
-[CBALSNodeProtocol serviceID];
-[CBALSNodeProtocol fastIntegrationTime];
-[CBALSNodeProtocol location];
-[CBALSNodeProtocol colorSupport];
-[CBALSNodeProtocol orientation];
-[CBALSNodeProtocol isEqualToCBALSNode:];
-[CBALSNodeProtocol superFastIntegrationTime];
-[CBALSNodeProtocol useCopyEventOnDisplayWake];
-[CBALSNodeProtocol digitizerFilterWindow];
-[CBALSNodeProtocol service];
-[CBALSNodeProtocol copyALSEvent];
-[CBALSNodeProtocol builtIn];
-[CBALSNodeProtocol getReportInterval];
-[CBALSNodeProtocol occlusionDrivesGrimaldi];
-[CBALSNodeProtocol digitizerLocationID];
-[CBALSNodeProtocol slowIntegrationTime];
-[CBALSNodeProtocol overrideHotspot];
-[CBALSNodeProtocol copyALSEventWithinTimeout:];
-[CBALSNodeProtocol useProxForOcclusion];
-[CBALSNodeProtocol conformsToHIDService:];
-[CBALSNodeProtocol ioService];
```
