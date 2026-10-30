# `JasperDepthProvider`

- Image: [`/System/Library/MediaCapture/ISP.mediacapture`](../userland/System__Library__MediaCapture__ISP.mediacapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PDDepthProcessorDelegate`
- 8 instance variables, 5 properties, 9 instance methods, 0 class methods

## Instance variables

```
B _wakupDone;
^{ISPDevice={ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{ISPDeviceCachedConfigChannel}^{ISPModuleParams}}^{ISPDeviceController}I^{__CFDictionary}I^{ISPMotionManager}^{ISPDeviceImpactManager}^{ISPServicesRemote}^{ISPExclaveDebugService}^{SystemStatus}I[4096c]{?=[8I]}^{ISPFirmwareWorkProcessor}BBII^{ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[7{ISPNotification=*Bi}][7{ISPNotification=*Bi}]{ISPNotification=*Bi}{ISPNotification=*Bi}{ISPNotification=*Bi}II{os_unfair_lock_s=I}^?^v^{__CFDictionary}[7B]{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}} _pDevice;
^{ISPServicesRemote=@@^?^v*} _pRemote;
I _channel;
f _minFrameRate;
f _maxFrameRate;
B _frameRateChanged;
i _gmoFlowBitmask;
```

## Properties

```
@property (Ti,V_gmoFlowBitmask) gmoFlowBitmask;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[JasperDepthProvider isValid];
-[JasperDepthProvider gmoFlowBitmask];
-[JasperDepthProvider initWithDevice:andChannel:andRemote:];
-[JasperDepthProvider isSameDevice:];
-[JasperDepthProvider onlineConfig:];
-[JasperDepthProvider savePeridotCalib:];
-[JasperDepthProvider setGmoFlowBitmask:];
-[JasperDepthProvider setJasperFrameRateMax:];
-[JasperDepthProvider setJasperFrameRateMin:];
```
