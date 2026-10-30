# `JasperDepthProvider`

- Image: [`/System/Library/MediaCapture/H16ISP.mediacapture`](../userland/System__Library__MediaCapture__H16ISP.mediacapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PDDepthProcessorDelegate`
- 8 instance variables, 5 properties, 9 instance methods, 0 class methods

## Instance variables

```
B _wakupDone;
^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^{H16ISPDeviceController}I^{__CFDictionary}I^{H16ISPMotionManager}^{H16ISPDeviceImpactManager}^{H16ISPServicesRemote}^{H16ISPExclaveDebugService}^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}BBII^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{os_unfair_lock_s=I}^?^v{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}} _pDevice;
^{H16ISPServicesRemote=@@^?^v*} _pRemote;
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
