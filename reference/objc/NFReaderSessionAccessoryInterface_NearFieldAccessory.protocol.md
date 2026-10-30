# `NFReaderSessionAccessoryInterface` (protocol)

- Image: [`/System/Library/PrivateFrameworks/NearFieldAccessory.framework/NearFieldAccessory`](../userland/System__Library__PrivateFrameworks__NearFieldAccessory.framework__NearFieldAccessory.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NFSessionAccessoryInterface`
- 0 instance variables, 0 properties, 13 instance methods, 0 class methods

## Instance methods

```
-[NFReaderSessionAccessoryInterface stopPolling:];
-[NFReaderSessionAccessoryInterface disconnectTag:];
-[NFReaderSessionAccessoryInterface sendMFGCommand:payload:completion:];
-[NFReaderSessionAccessoryInterface transceive:callback:];
-[NFReaderSessionAccessoryInterface readTypeIdentifier:];
-[NFReaderSessionAccessoryInterface checkNdefSupport:];
-[NFReaderSessionAccessoryInterface checkPresence:];
-[NFReaderSessionAccessoryInterface connectTag:callback:];
-[NFReaderSessionAccessoryInterface enableContinuousWave:withFrequencySweep:callback:];
-[NFReaderSessionAccessoryInterface readRawNdef:];
-[NFReaderSessionAccessoryInterface setTagDataRate:callback:];
-[NFReaderSessionAccessoryInterface startPollingForTechnology:lpcd:callback:];
-[NFReaderSessionAccessoryInterface transceiveAccessoryCommand:callback:];
```
