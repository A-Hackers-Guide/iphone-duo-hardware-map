# `CTRadioFrequencyFrontEndScanData`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 19 instance variables, 19 properties, 43 instance methods, 1 class methods

## Instance variables

```
B _rfcInitPass;
B _rffeScanPass;
Q _version;
Q _hwPrdId;
Q _hwSku;
Q _hwRev;
Q _hwHousing;
Q _rfcHwid;
Q _rfcRev;
Q _rfcMmwHwid;
Q _rfcMmwRev;
Q _fr2TrxRev;
Q _numExpectedDevices;
Q _numDetectedDevices;
Q _numMissingDevices;
@"NSMutableArray" _rffeScanInfo;
@"NSMutableArray" _missingRffeDevices;
@"NSMutableArray" _missingAtDevices;
@"NSMutableArray" _missingMmwDevices;
```

## Properties

```
@property (TQ,N,V_version) version;
@property (TQ,N,V_hwPrdId) hwPrdId;
@property (TQ,N,V_hwSku) hwSku;
@property (TQ,N,V_hwRev) hwRev;
@property (TQ,N,V_hwHousing) hwHousing;
@property (TB,N,V_rfcInitPass) rfcInitPass;
@property (TQ,N,V_rfcHwid) rfcHwid;
@property (TQ,N,V_rfcRev) rfcRev;
@property (TQ,N,V_rfcMmwHwid) rfcMmwHwid;
@property (TQ,N,V_rfcMmwRev) rfcMmwRev;
@property (TQ,N,V_fr2TrxRev) fr2TrxRev;
@property (TB,N,V_rffeScanPass) rffeScanPass;
@property (TQ,N,V_numExpectedDevices) numExpectedDevices;
@property (TQ,N,V_numDetectedDevices) numDetectedDevices;
@property (TQ,N,V_numMissingDevices) numMissingDevices;
@property (T@"NSMutableArray",&,N,V_rffeScanInfo) rffeScanInfo;
@property (T@"NSMutableArray",&,N,V_missingRffeDevices) missingRffeDevices;
@property (T@"NSMutableArray",&,N,V_missingAtDevices) missingAtDevices;
@property (T@"NSMutableArray",&,N,V_missingMmwDevices) missingMmwDevices;
```

## Class methods

```
+[CTRadioFrequencyFrontEndScanData supportsSecureCoding];
```

## Instance methods

```
-[CTRadioFrequencyFrontEndScanData init];
-[CTRadioFrequencyFrontEndScanData version];
-[CTRadioFrequencyFrontEndScanData encodeWithCoder:];
-[CTRadioFrequencyFrontEndScanData description];
-[CTRadioFrequencyFrontEndScanData initWithCoder:];
-[CTRadioFrequencyFrontEndScanData setVersion:];
-[CTRadioFrequencyFrontEndScanData copyWithZone:];
-[CTRadioFrequencyFrontEndScanData setRfcInitPass:];
-[CTRadioFrequencyFrontEndScanData hwPrdId];
-[CTRadioFrequencyFrontEndScanData rfcHwid];
-[CTRadioFrequencyFrontEndScanData fr2TrxRev];
-[CTRadioFrequencyFrontEndScanData hwHousing];
-[CTRadioFrequencyFrontEndScanData hwRev];
-[CTRadioFrequencyFrontEndScanData hwSku];
-[CTRadioFrequencyFrontEndScanData missingAtDevices];
-[CTRadioFrequencyFrontEndScanData missingMmwDevices];
-[CTRadioFrequencyFrontEndScanData missingRffeDevices];
-[CTRadioFrequencyFrontEndScanData numDetectedDevices];
-[CTRadioFrequencyFrontEndScanData numExpectedDevices];
-[CTRadioFrequencyFrontEndScanData numMissingDevices];
-[CTRadioFrequencyFrontEndScanData rfcInitPass];
-[CTRadioFrequencyFrontEndScanData rfcMmwHwid];
-[CTRadioFrequencyFrontEndScanData rfcMmwRev];
-[CTRadioFrequencyFrontEndScanData rfcRev];
-[CTRadioFrequencyFrontEndScanData rffeScanInfo];
-[CTRadioFrequencyFrontEndScanData rffeScanPass];
-[CTRadioFrequencyFrontEndScanData setFr2TrxRev:];
-[CTRadioFrequencyFrontEndScanData setHwHousing:];
-[CTRadioFrequencyFrontEndScanData setHwPrdId:];
-[CTRadioFrequencyFrontEndScanData setHwRev:];
-[CTRadioFrequencyFrontEndScanData setHwSku:];
-[CTRadioFrequencyFrontEndScanData setMissingAtDevices:];
-[CTRadioFrequencyFrontEndScanData setMissingMmwDevices:];
-[CTRadioFrequencyFrontEndScanData setMissingRffeDevices:];
-[CTRadioFrequencyFrontEndScanData setNumDetectedDevices:];
-[CTRadioFrequencyFrontEndScanData setNumExpectedDevices:];
-[CTRadioFrequencyFrontEndScanData setNumMissingDevices:];
-[CTRadioFrequencyFrontEndScanData setRfcHwid:];
-[CTRadioFrequencyFrontEndScanData setRfcMmwHwid:];
-[CTRadioFrequencyFrontEndScanData setRfcMmwRev:];
-[CTRadioFrequencyFrontEndScanData setRfcRev:];
-[CTRadioFrequencyFrontEndScanData setRffeScanInfo:];
-[CTRadioFrequencyFrontEndScanData setRffeScanPass:];
```
