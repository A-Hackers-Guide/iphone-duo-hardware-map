# `NFHardwareManagerAccessoryInterface` (protocol)

- Image: [`/System/Library/PrivateFrameworks/NearFieldAccessory.framework/NearFieldAccessory`](../userland/System__Library__PrivateFrameworks__NearFieldAccessory.framework__NearFieldAccessory.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 15 instance methods, 0 class methods

## Instance methods

```
-[NFHardwareManagerAccessoryInterface setClientName:];
-[NFHardwareManagerAccessoryInterface getInfo:];
-[NFHardwareManagerAccessoryInterface getPowerCounters:];
-[NFHardwareManagerAccessoryInterface getMultiTagState:];
-[NFHardwareManagerAccessoryInterface clearMultiTagState:];
-[NFHardwareManagerAccessoryInterface enableLPCD:callback:];
-[NFHardwareManagerAccessoryInterface enableMultiTag:callback:];
-[NFHardwareManagerAccessoryInterface getDieId:];
-[NFHardwareManagerAccessoryInterface getLastDetectedTags:];
-[NFHardwareManagerAccessoryInterface getRfSettings:];
-[NFHardwareManagerAccessoryInterface isHWSupported:];
-[NFHardwareManagerAccessoryInterface pushSignedRF:callback:];
-[NFHardwareManagerAccessoryInterface queueReaderSession:callback:];
-[NFHardwareManagerAccessoryInterface restartMultiTag:];
-[NFHardwareManagerAccessoryInterface triggerDelayedWake:callback:];
```
