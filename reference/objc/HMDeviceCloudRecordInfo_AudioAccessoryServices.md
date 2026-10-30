# `HMDeviceCloudRecordInfo`

- Image: [`/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`](../userland/System__Library__PrivateFrameworks__AudioAccessoryServices.framework__AudioAccessoryServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 28 instance variables, 28 properties, 60 instance methods, 1 class methods

## Instance variables

```
C _haRegionStatus;
C _haRegionStatusV2;
C _hpPPERegionStatus;
C _hpRegionStatus;
c _mediaAssistEnabled;
c _pmeMediaEnabled;
c _pmeVoiceEnabled;
c _swipeGainEnabled;
@"NSString" _bluetoothAddress;
@"NSNumber" _bottomMicFaultCountLeft;
@"NSNumber" _bottomMicFaultCountRight;
@"NSNumber" _diagnosticMeasurementsCount;
@"NSNumber" _freqAccuracyFaultCountLeft;
@"NSNumber" _freqAccuracyFaultCountRight;
@"NSNumber" _frontVentFaultCountLeft;
@"NSNumber" _frontVentFaultCountRight;
@"NSNumber" _innerMicFaultCountLeft;
@"NSNumber" _innerMicFaultCountRight;
@"NSDate" _latestDiagnosticTimestampLeft;
@"NSDate" _latestDiagnosticTimestampRight;
@"NSNumber" _rearVentFaultCountLeft;
@"NSNumber" _rearVentFaultCountRight;
@"NSNumber" _speakerFaultCountLeft;
@"NSNumber" _speakerFaultCountRight;
@"NSNumber" _topMicFaultCountLeft;
@"NSNumber" _topMicFaultCountRight;
@"NSNumber" _totalHarmonicDistortionFaultCountLeft;
@"NSNumber" _totalHarmonicDistortionFaultCountRight;
```

## Properties

```
@property (T@"NSString",R,N,V_bluetoothAddress) bluetoothAddress;
@property (TC,V_haRegionStatus) haRegionStatus;
@property (TC,V_haRegionStatusV2) haRegionStatusV2;
@property (TC,V_hpPPERegionStatus) hpPPERegionStatus;
@property (TC,V_hpRegionStatus) hpRegionStatus;
@property (Tc,V_mediaAssistEnabled) mediaAssistEnabled;
@property (Tc,V_pmeMediaEnabled) pmeMediaEnabled;
@property (Tc,V_pmeVoiceEnabled) pmeVoiceEnabled;
@property (Tc,V_swipeGainEnabled) swipeGainEnabled;
@property (T@"NSNumber",&,N,V_bottomMicFaultCountLeft) bottomMicFaultCountLeft;
@property (T@"NSNumber",&,N,V_bottomMicFaultCountRight) bottomMicFaultCountRight;
@property (T@"NSNumber",&,N,V_diagnosticMeasurementsCount) diagnosticMeasurementsCount;
@property (T@"NSNumber",&,N,V_freqAccuracyFaultCountLeft) freqAccuracyFaultCountLeft;
@property (T@"NSNumber",&,N,V_freqAccuracyFaultCountRight) freqAccuracyFaultCountRight;
@property (T@"NSNumber",&,N,V_frontVentFaultCountLeft) frontVentFaultCountLeft;
@property (T@"NSNumber",&,N,V_frontVentFaultCountRight) frontVentFaultCountRight;
@property (T@"NSNumber",&,N,V_innerMicFaultCountLeft) innerMicFaultCountLeft;
@property (T@"NSNumber",&,N,V_innerMicFaultCountRight) innerMicFaultCountRight;
@property (T@"NSDate",&,N,V_latestDiagnosticTimestampLeft) latestDiagnosticTimestampLeft;
@property (T@"NSDate",&,N,V_latestDiagnosticTimestampRight) latestDiagnosticTimestampRight;
@property (T@"NSNumber",&,N,V_rearVentFaultCountLeft) rearVentFaultCountLeft;
@property (T@"NSNumber",&,N,V_rearVentFaultCountRight) rearVentFaultCountRight;
@property (T@"NSNumber",&,N,V_speakerFaultCountLeft) speakerFaultCountLeft;
@property (T@"NSNumber",&,N,V_speakerFaultCountRight) speakerFaultCountRight;
@property (T@"NSNumber",&,N,V_topMicFaultCountLeft) topMicFaultCountLeft;
@property (T@"NSNumber",&,N,V_topMicFaultCountRight) topMicFaultCountRight;
@property (T@"NSNumber",&,N,V_totalHarmonicDistortionFaultCountLeft) totalHarmonicDistortionFaultCountLeft;
@property (T@"NSNumber",&,N,V_totalHarmonicDistortionFaultCountRight) totalHarmonicDistortionFaultCountRight;
```

## Class methods

```
+[HMDeviceCloudRecordInfo supportsSecureCoding];
```

## Instance methods

```
-[HMDeviceCloudRecordInfo descriptionWithLevel:];
-[HMDeviceCloudRecordInfo bluetoothAddress];
-[HMDeviceCloudRecordInfo encodeWithCoder:];
-[HMDeviceCloudRecordInfo description];
-[HMDeviceCloudRecordInfo initWithCoder:];
-[HMDeviceCloudRecordInfo pmeVoiceEnabled];
-[HMDeviceCloudRecordInfo pmeMediaEnabled];
-[HMDeviceCloudRecordInfo mediaAssistEnabled];
-[HMDeviceCloudRecordInfo setMediaAssistEnabled:];
-[HMDeviceCloudRecordInfo setPmeMediaEnabled:];
-[HMDeviceCloudRecordInfo setPmeVoiceEnabled:];
-[HMDeviceCloudRecordInfo setSwipeGainEnabled:];
-[HMDeviceCloudRecordInfo swipeGainEnabled];
-[HMDeviceCloudRecordInfo setDiagnosticMeasurementsCount:];
-[HMDeviceCloudRecordInfo setFreqAccuracyFaultCountRight:];
-[HMDeviceCloudRecordInfo bottomMicFaultCountLeft];
-[HMDeviceCloudRecordInfo bottomMicFaultCountRight];
-[HMDeviceCloudRecordInfo diagnosticMeasurementsCount];
-[HMDeviceCloudRecordInfo freqAccuracyFaultCountLeft];
-[HMDeviceCloudRecordInfo freqAccuracyFaultCountRight];
-[HMDeviceCloudRecordInfo frontVentFaultCountLeft];
-[HMDeviceCloudRecordInfo frontVentFaultCountRight];
-[HMDeviceCloudRecordInfo haRegionStatus];
-[HMDeviceCloudRecordInfo haRegionStatusV2];
-[HMDeviceCloudRecordInfo hpPPERegionStatus];
-[HMDeviceCloudRecordInfo hpRegionStatus];
-[HMDeviceCloudRecordInfo initWithBluetoothAddress:];
-[HMDeviceCloudRecordInfo innerMicFaultCountLeft];
-[HMDeviceCloudRecordInfo innerMicFaultCountRight];
-[HMDeviceCloudRecordInfo latestDiagnosticTimestampLeft];
-[HMDeviceCloudRecordInfo latestDiagnosticTimestampRight];
-[HMDeviceCloudRecordInfo rearVentFaultCountLeft];
-[HMDeviceCloudRecordInfo rearVentFaultCountRight];
-[HMDeviceCloudRecordInfo setBottomMicFaultCountLeft:];
-[HMDeviceCloudRecordInfo setBottomMicFaultCountRight:];
-[HMDeviceCloudRecordInfo setFreqAccuracyFaultCountLeft:];
-[HMDeviceCloudRecordInfo setFrontVentFaultCountLeft:];
-[HMDeviceCloudRecordInfo setFrontVentFaultCountRight:];
-[HMDeviceCloudRecordInfo setHaRegionStatus:];
-[HMDeviceCloudRecordInfo setHaRegionStatusV2:];
-[HMDeviceCloudRecordInfo setHpPPERegionStatus:];
-[HMDeviceCloudRecordInfo setHpRegionStatus:];
-[HMDeviceCloudRecordInfo setInnerMicFaultCountLeft:];
-[HMDeviceCloudRecordInfo setInnerMicFaultCountRight:];
-[HMDeviceCloudRecordInfo setLatestDiagnosticTimestampLeft:];
-[HMDeviceCloudRecordInfo setLatestDiagnosticTimestampRight:];
-[HMDeviceCloudRecordInfo setRearVentFaultCountLeft:];
-[HMDeviceCloudRecordInfo setRearVentFaultCountRight:];
-[HMDeviceCloudRecordInfo setSpeakerFaultCountLeft:];
-[HMDeviceCloudRecordInfo setSpeakerFaultCountRight:];
-[HMDeviceCloudRecordInfo setTopMicFaultCountLeft:];
-[HMDeviceCloudRecordInfo setTopMicFaultCountRight:];
-[HMDeviceCloudRecordInfo setTotalHarmonicDistortionFaultCountLeft:];
-[HMDeviceCloudRecordInfo setTotalHarmonicDistortionFaultCountRight:];
-[HMDeviceCloudRecordInfo speakerFaultCountLeft];
-[HMDeviceCloudRecordInfo speakerFaultCountRight];
-[HMDeviceCloudRecordInfo topMicFaultCountLeft];
-[HMDeviceCloudRecordInfo topMicFaultCountRight];
-[HMDeviceCloudRecordInfo totalHarmonicDistortionFaultCountLeft];
-[HMDeviceCloudRecordInfo totalHarmonicDistortionFaultCountRight];
```
