# `CBControllerLowPowerModeParams`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CUXPCCodable`
- 29 instance variables, 29 properties, 61 instance methods, 0 class methods

## Instance variables

```
C _actionType;
c _rssiThresholdValue;
C _packetLength;
C _deviceIDAdvScanCount;
C _deviceIDLength;
C _deviceIDTimestampEffectiveBits;
C _deviceIDTimestampFrequency;
C _deviceIDTimestampLsbsTruncated;
C _deviceIDDiagLength;
C _diagnosticTxAdvBackoff;
C _diagnosticTxAdvDuration;
C _macKeyDiagLength;
S _configFlags;
S _scanDelayStart;
S _scanWindow;
S _scanInterval;
S _scanDuration;
S _nextScanDelay;
S _numberOfDelayIterations;
S _gpioAssertionTime;
S _diagnosticTxAdvInterval;
I _maxClockDriftSeconds;
@"NSData" _dataBlob;
@"NSData" _dataMask;
@"NSData" _deviceIDInfo;
@"NSData" _deviceIDInputKeyMaterial;
@"NSData" _deviceIDSalt;
@"NSData" _deviceIDDiagInfo;
@"NSData" _macKeyDiagInfo;
```

## Properties

```
@property (TC,N,V_actionType) actionType;
@property (T@"NSData",C,N,V_dataBlob) dataBlob;
@property (T@"NSData",C,N,V_dataMask) dataMask;
@property (TS,N,V_configFlags) configFlags;
@property (TS,N,V_scanDelayStart) scanDelayStart;
@property (TS,N,V_scanWindow) scanWindow;
@property (TS,N,V_scanInterval) scanInterval;
@property (TS,N,V_scanDuration) scanDuration;
@property (TS,N,V_nextScanDelay) nextScanDelay;
@property (TS,N,V_numberOfDelayIterations) numberOfDelayIterations;
@property (Tc,N,V_rssiThresholdValue) rssiThresholdValue;
@property (TC,N,V_packetLength) packetLength;
@property (TC,N,V_deviceIDAdvScanCount) deviceIDAdvScanCount;
@property (TC,N,V_deviceIDLength) deviceIDLength;
@property (T@"NSData",C,N,V_deviceIDInfo) deviceIDInfo;
@property (T@"NSData",C,N,V_deviceIDInputKeyMaterial) deviceIDInputKeyMaterial;
@property (T@"NSData",C,N,V_deviceIDSalt) deviceIDSalt;
@property (TC,N,V_deviceIDTimestampEffectiveBits) deviceIDTimestampEffectiveBits;
@property (TC,N,V_deviceIDTimestampFrequency) deviceIDTimestampFrequency;
@property (TC,N,V_deviceIDTimestampLsbsTruncated) deviceIDTimestampLsbsTruncated;
@property (TS,N,V_gpioAssertionTime) gpioAssertionTime;
@property (T@"NSData",C,N,V_deviceIDDiagInfo) deviceIDDiagInfo;
@property (TC,N,V_deviceIDDiagLength) deviceIDDiagLength;
@property (TC,N,V_diagnosticTxAdvBackoff) diagnosticTxAdvBackoff;
@property (TC,N,V_diagnosticTxAdvDuration) diagnosticTxAdvDuration;
@property (TS,N,V_diagnosticTxAdvInterval) diagnosticTxAdvInterval;
@property (T@"NSData",C,N,V_macKeyDiagInfo) macKeyDiagInfo;
@property (TC,N,V_macKeyDiagLength) macKeyDiagLength;
@property (TI,N,V_maxClockDriftSeconds) maxClockDriftSeconds;
```

## Instance methods

```
-[CBControllerLowPowerModeParams encodeWithXPCObject:];
-[CBControllerLowPowerModeParams setActionType:];
-[CBControllerLowPowerModeParams initWithXPCObject:error:];
-[CBControllerLowPowerModeParams scanInterval];
-[CBControllerLowPowerModeParams scanWindow];
-[CBControllerLowPowerModeParams setScanWindow:];
-[CBControllerLowPowerModeParams setScanDuration:];
-[CBControllerLowPowerModeParams scanDuration];
-[CBControllerLowPowerModeParams actionType];
-[CBControllerLowPowerModeParams description];
-[CBControllerLowPowerModeParams setScanInterval:];
-[CBControllerLowPowerModeParams dataBlob];
-[CBControllerLowPowerModeParams setDataBlob:];
-[CBControllerLowPowerModeParams setConfigFlags:];
-[CBControllerLowPowerModeParams configFlags];
-[CBControllerLowPowerModeParams dataMask];
-[CBControllerLowPowerModeParams deviceIDAdvScanCount];
-[CBControllerLowPowerModeParams deviceIDDiagInfo];
-[CBControllerLowPowerModeParams deviceIDDiagLength];
-[CBControllerLowPowerModeParams deviceIDInfo];
-[CBControllerLowPowerModeParams deviceIDInputKeyMaterial];
-[CBControllerLowPowerModeParams deviceIDLength];
-[CBControllerLowPowerModeParams deviceIDSalt];
-[CBControllerLowPowerModeParams deviceIDTimestampEffectiveBits];
-[CBControllerLowPowerModeParams deviceIDTimestampFrequency];
-[CBControllerLowPowerModeParams deviceIDTimestampLsbsTruncated];
-[CBControllerLowPowerModeParams diagnosticTxAdvBackoff];
-[CBControllerLowPowerModeParams diagnosticTxAdvDuration];
-[CBControllerLowPowerModeParams diagnosticTxAdvInterval];
-[CBControllerLowPowerModeParams gpioAssertionTime];
-[CBControllerLowPowerModeParams macKeyDiagInfo];
-[CBControllerLowPowerModeParams macKeyDiagLength];
-[CBControllerLowPowerModeParams maxClockDriftSeconds];
-[CBControllerLowPowerModeParams nextScanDelay];
-[CBControllerLowPowerModeParams numberOfDelayIterations];
-[CBControllerLowPowerModeParams packetLength];
-[CBControllerLowPowerModeParams rssiThresholdValue];
-[CBControllerLowPowerModeParams scanDelayStart];
-[CBControllerLowPowerModeParams setDataMask:];
-[CBControllerLowPowerModeParams setDeviceIDAdvScanCount:];
-[CBControllerLowPowerModeParams setDeviceIDDiagInfo:];
-[CBControllerLowPowerModeParams setDeviceIDDiagLength:];
-[CBControllerLowPowerModeParams setDeviceIDInfo:];
-[CBControllerLowPowerModeParams setDeviceIDInputKeyMaterial:];
-[CBControllerLowPowerModeParams setDeviceIDLength:];
-[CBControllerLowPowerModeParams setDeviceIDSalt:];
-[CBControllerLowPowerModeParams setDeviceIDTimestampEffectiveBits:];
-[CBControllerLowPowerModeParams setDeviceIDTimestampFrequency:];
-[CBControllerLowPowerModeParams setDeviceIDTimestampLsbsTruncated:];
-[CBControllerLowPowerModeParams setDiagnosticTxAdvBackoff:];
-[CBControllerLowPowerModeParams setDiagnosticTxAdvDuration:];
-[CBControllerLowPowerModeParams setDiagnosticTxAdvInterval:];
-[CBControllerLowPowerModeParams setGpioAssertionTime:];
-[CBControllerLowPowerModeParams setMacKeyDiagInfo:];
-[CBControllerLowPowerModeParams setMacKeyDiagLength:];
-[CBControllerLowPowerModeParams setMaxClockDriftSeconds:];
-[CBControllerLowPowerModeParams setNextScanDelay:];
-[CBControllerLowPowerModeParams setNumberOfDelayIterations:];
-[CBControllerLowPowerModeParams setPacketLength:];
-[CBControllerLowPowerModeParams setRssiThresholdValue:];
-[CBControllerLowPowerModeParams setScanDelayStart:];
```
