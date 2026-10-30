# `AWBProcessor`

- Image: [`/System/Library/PrivateFrameworks/CameraColorProcessing.framework/CameraColorProcessing`](../userland/System__Library__PrivateFrameworks__CameraColorProcessing.framework__CameraColorProcessing.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AWBImageBufferProcessor`
- 11 instance variables, 10 properties, 18 instance methods, 5 class methods

## Instance variables

```
@"FigMetalContext" _metalContext;
@"NSMutableDictionary" _stats;
@"AWBStatistics" _awbStats;
@"AWBAlgorithm" _awbAlgo;
B _configured;
B _allocatorSetupComplete;
@"NSDictionary" _tuningParameters;
@"<MTLCommandQueue>" _metalCommandQueue;
@"<AWBIBPParams>" _awbParams;
@"CMIExternalMemoryResource" _externalMemoryResource;
@"NSDictionary" cameraInfoByPortType;
```

## Properties

```
@property (T@"<AWBIBPParams>",R,N,V_awbParams) awbParams;
@property (T@"<MTLCommandQueue>",&,N,V_metalCommandQueue) metalCommandQueue;
@property (TB,?,R,N) supportsExternalMemoryResource;
@property (T@"CMIExternalMemoryResource",?,&,N,V_externalMemoryResource) externalMemoryResource;
@property (T@"NSDictionary",&,N,V_tuningParameters) tuningParameters;
@property (T@"NSDictionary",&,N,VcameraInfoByPortType) cameraInfoByPortType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[AWBProcessor calculateSTRBKeyFromWideCamera:moduleConfig:secondaryModuleConfig:];
+[AWBProcessor calculateSTRBKeyFromWideCameraLatticeModel:moduleConfig:absoluteColorCalibrations:secondaryModuleConfig:secondaryAbsoluteColorCalibrations:];
+[AWBProcessor getColorCalibrationsUsingIdealColorCalbrations:absoluteColorCalibrations:colorCalibrationsOut:awbConfig:];
+[AWBProcessor getInternalAWBMetadataForMIWB:cameraInfo:metadata:validRect:secondaryModuleConfig:secondaryCameraInfo:];
+[AWBProcessor getTileStatsRegionWithMetadata:cropRectLTMInCoords:ltmInDownsamplingRatio:tileStatsRegionLTMInCoordsDictOut:];
```

## Instance methods

```
-[AWBProcessor resetState];
-[AWBProcessor tuningParameters];
-[AWBProcessor finishProcessing];
-[AWBProcessor externalMemoryResource];
-[AWBProcessor purgeResources];
-[AWBProcessor setMetalCommandQueue:];
-[AWBProcessor setCameraInfoByPortType:];
-[AWBProcessor setExternalMemoryResource:];
-[AWBProcessor prewarm];
-[AWBProcessor prepareToProcess:];
-[AWBProcessor setup];
-[AWBProcessor metalCommandQueue];
-[AWBProcessor cameraInfoByPortType];
-[AWBProcessor setTuningParameters:];
-[AWBProcessor process];
-[AWBProcessor dealloc];
-[AWBProcessor awbParams];
-[AWBProcessor internalSetupWithFWPlatformID:];
```
