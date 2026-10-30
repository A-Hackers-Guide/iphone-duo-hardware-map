# `_UIStatusBarData`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 38 instance variables, 40 properties, 90 instance methods, 3 class methods

## Instance variables

```
@"_UIStatusBarDataStringEntry" _timeEntry;
@"_UIStatusBarDataStringEntry" _shortTimeEntry;
@"_UIStatusBarDataStringEntry" _dateEntry;
@"_UIStatusBarDataStringEntry" _personNameEntry;
@"_UIStatusBarDataStringEntry" _deviceNameEntry;
@"_UIStatusBarDataCellularEntry" _cellularEntry;
@"_UIStatusBarDataCellularEntry" _secondaryCellularEntry;
@"_UIStatusBarDataWifiEntry" _wifiEntry;
@"_UIStatusBarDataBatteryEntry" _mainBatteryEntry;
@"_UIStatusBarDataBluetoothEntry" _bluetoothEntry;
@"_UIStatusBarDataThermalEntry" _thermalEntry;
@"_UIStatusBarDataActivityEntry" _activityEntry;
@"_UIStatusBarDataTetheringEntry" _tetheringEntry;
@"_UIStatusBarDataLocationEntry" _locationEntry;
@"_UIStatusBarDataLockEntry" _lockEntry;
@"_UIStatusBarDataQuietModeEntry" _quietModeEntry;
@"_UIStatusBarDataBoolEntry" _electronicTollCollectionEntry;
@"_UIStatusBarDataBoolEntry" _radarEntry;
@"_UIStatusBarDataEntry" _rotationLockEntry;
@"_UIStatusBarDataEntry" _airplaneModeEntry;
@"_UIStatusBarDataEntry" _ttyEntry;
@"_UIStatusBarDataEntry" _nikeEntry;
@"_UIStatusBarDataEntry" _assistantEntry;
@"_UIStatusBarDataEntry" _studentEntry;
@"_UIStatusBarDataEntry" _vpnEntry;
@"_UIStatusBarDataEntry" _liquidDetectionEntry;
@"_UIStatusBarDataEntry" _displayWarningEntry;
@"_UIStatusBarDataVoiceControlEntry" _voiceControlEntry;
@"_UIStatusBarDataEntry" _airPlayEntry;
@"_UIStatusBarDataEntry" _carPlayEntry;
@"_UIStatusBarDataEntry" _alarmEntry;
@"_UIStatusBarDataEntry" _satelliteEntry;
@"_UIStatusBarDataEntry" _sensorActivityEntry;
@"_UIStatusBarDataBoolEntry" _announceNotificationsEntry;
@"_UIStatusBarDataIntegerEntry" _volumeEntry;
@"_UIStatusBarDataBackgroundActivityEntry" _backgroundActivityEntry;
@"_UIStatusBarDataStringEntry" _backNavigationEntry;
@"_UIStatusBarDataStringEntry" _forwardNavigationEntry;
```

## Properties

```
@property (TB,R,N,GisEmpty) empty;
@property (T@"NSSet",R,N) existingEntryKeys;
@property (T@"_UIStatusBarDataStringEntry",C,N,V_timeEntry) timeEntry;
@property (T@"_UIStatusBarDataStringEntry",C,N,V_shortTimeEntry) shortTimeEntry;
@property (T@"_UIStatusBarDataStringEntry",C,N,V_dateEntry) dateEntry;
@property (T@"_UIStatusBarDataStringEntry",C,N,V_personNameEntry) personNameEntry;
@property (T@"_UIStatusBarDataStringEntry",C,N,V_deviceNameEntry) deviceNameEntry;
@property (T@"_UIStatusBarDataCellularEntry",C,N,V_cellularEntry) cellularEntry;
@property (T@"_UIStatusBarDataCellularEntry",C,N,V_secondaryCellularEntry) secondaryCellularEntry;
@property (T@"_UIStatusBarDataWifiEntry",C,N,V_wifiEntry) wifiEntry;
@property (T@"_UIStatusBarDataBatteryEntry",C,N,V_mainBatteryEntry) mainBatteryEntry;
@property (T@"_UIStatusBarDataBluetoothEntry",C,N,V_bluetoothEntry) bluetoothEntry;
@property (T@"_UIStatusBarDataThermalEntry",C,N,V_thermalEntry) thermalEntry;
@property (T@"_UIStatusBarDataActivityEntry",C,N,V_activityEntry) activityEntry;
@property (T@"_UIStatusBarDataTetheringEntry",C,N,V_tetheringEntry) tetheringEntry;
@property (T@"_UIStatusBarDataLocationEntry",C,N,V_locationEntry) locationEntry;
@property (T@"_UIStatusBarDataLockEntry",C,N,V_lockEntry) lockEntry;
@property (T@"_UIStatusBarDataQuietModeEntry",C,N,V_quietModeEntry) quietModeEntry;
@property (T@"_UIStatusBarDataBoolEntry",C,N,V_electronicTollCollectionEntry) electronicTollCollectionEntry;
@property (T@"_UIStatusBarDataBoolEntry",C,N,V_radarEntry) radarEntry;
@property (T@"_UIStatusBarDataEntry",C,N,V_rotationLockEntry) rotationLockEntry;
@property (T@"_UIStatusBarDataEntry",C,N,V_airplaneModeEntry) airplaneModeEntry;
@property (T@"_UIStatusBarDataEntry",C,N,V_ttyEntry) ttyEntry;
@property (T@"_UIStatusBarDataEntry",C,N,V_nikeEntry) nikeEntry;
@property (T@"_UIStatusBarDataEntry",C,N,V_assistantEntry) assistantEntry;
@property (T@"_UIStatusBarDataEntry",C,N,V_studentEntry) studentEntry;
@property (T@"_UIStatusBarDataEntry",C,N,V_vpnEntry) vpnEntry;
@property (T@"_UIStatusBarDataEntry",C,N,V_liquidDetectionEntry) liquidDetectionEntry;
@property (T@"_UIStatusBarDataEntry",C,N,V_displayWarningEntry) displayWarningEntry;
@property (T@"_UIStatusBarDataVoiceControlEntry",C,N,V_voiceControlEntry) voiceControlEntry;
@property (T@"_UIStatusBarDataEntry",C,N,V_airPlayEntry) airPlayEntry;
@property (T@"_UIStatusBarDataEntry",C,N,V_carPlayEntry) carPlayEntry;
@property (T@"_UIStatusBarDataEntry",C,N,V_alarmEntry) alarmEntry;
@property (T@"_UIStatusBarDataEntry",C,N,V_satelliteEntry) satelliteEntry;
@property (T@"_UIStatusBarDataEntry",C,N,V_sensorActivityEntry) sensorActivityEntry;
@property (T@"_UIStatusBarDataBoolEntry",C,N,V_announceNotificationsEntry) announceNotificationsEntry;
@property (T@"_UIStatusBarDataIntegerEntry",C,N,V_volumeEntry) volumeEntry;
@property (T@"_UIStatusBarDataBackgroundActivityEntry",C,N,V_backgroundActivityEntry) backgroundActivityEntry;
@property (T@"_UIStatusBarDataStringEntry",C,N,V_backNavigationEntry) backNavigationEntry;
@property (T@"_UIStatusBarDataStringEntry",C,N,V_forwardNavigationEntry) forwardNavigationEntry;
```

## Class methods

```
+[_UIStatusBarData supportsSecureCoding];
+[_UIStatusBarData entryKeys];
+[_UIStatusBarData staticDisplayData];
```

## Instance methods

```
-[_UIStatusBarData isEmpty];
-[_UIStatusBarData encodeWithCoder:];
-[_UIStatusBarData activityEntry];
-[_UIStatusBarData hash];
-[_UIStatusBarData description];
-[_UIStatusBarData initWithCoder:];
-[_UIStatusBarData copyWithZone:];
-[_UIStatusBarData setActivityEntry:];
-[_UIStatusBarData isEqual:];
-[_UIStatusBarData applyUpdate:];
-[_UIStatusBarData personNameEntry];
-[_UIStatusBarData updateFromData:];
-[_UIStatusBarData deviceNameEntry];
-[_UIStatusBarData setVolumeEntry:];
-[_UIStatusBarData _applyUpdate:keys:];
-[_UIStatusBarData airPlayEntry];
-[_UIStatusBarData airplaneModeEntry];
-[_UIStatusBarData alarmEntry];
-[_UIStatusBarData announceNotificationsEntry];
-[_UIStatusBarData assistantEntry];
-[_UIStatusBarData backNavigationEntry];
-[_UIStatusBarData backgroundActivityEntry];
-[_UIStatusBarData bluetoothEntry];
-[_UIStatusBarData carPlayEntry];
-[_UIStatusBarData cellularEntry];
-[_UIStatusBarData dataByApplyingOverlay:];
-[_UIStatusBarData dataByApplyingUpdate:keys:];
-[_UIStatusBarData dateEntry];
-[_UIStatusBarData displayWarningEntry];
-[_UIStatusBarData electronicTollCollectionEntry];
-[_UIStatusBarData existingEntryKeys];
-[_UIStatusBarData forwardNavigationEntry];
-[_UIStatusBarData liquidDetectionEntry];
-[_UIStatusBarData locationEntry];
-[_UIStatusBarData lockEntry];
-[_UIStatusBarData mainBatteryEntry];
-[_UIStatusBarData makeUpdateFromData:];
-[_UIStatusBarData nikeEntry];
-[_UIStatusBarData quietModeEntry];
-[_UIStatusBarData radarEntry];
-[_UIStatusBarData rotationLockEntry];
-[_UIStatusBarData satelliteEntry];
-[_UIStatusBarData secondaryCellularEntry];
-[_UIStatusBarData sensorActivityEntry];
-[_UIStatusBarData setAirPlayEntry:];
-[_UIStatusBarData setAirplaneModeEntry:];
-[_UIStatusBarData setAlarmEntry:];
-[_UIStatusBarData setAnnounceNotificationsEntry:];
-[_UIStatusBarData setAssistantEntry:];
-[_UIStatusBarData setBackNavigationEntry:];
-[_UIStatusBarData setBackgroundActivityEntry:];
-[_UIStatusBarData setBluetoothEntry:];
-[_UIStatusBarData setCarPlayEntry:];
-[_UIStatusBarData setCellularEntry:];
-[_UIStatusBarData setDateEntry:];
-[_UIStatusBarData setDeviceNameEntry:];
-[_UIStatusBarData setDisplayWarningEntry:];
-[_UIStatusBarData setElectronicTollCollectionEntry:];
-[_UIStatusBarData setForwardNavigationEntry:];
-[_UIStatusBarData setLiquidDetectionEntry:];
-[_UIStatusBarData setLocationEntry:];
-[_UIStatusBarData setLockEntry:];
-[_UIStatusBarData setMainBatteryEntry:];
-[_UIStatusBarData setNikeEntry:];
-[_UIStatusBarData setPersonNameEntry:];
-[_UIStatusBarData setQuietModeEntry:];
-[_UIStatusBarData setRadarEntry:];
-[_UIStatusBarData setRotationLockEntry:];
-[_UIStatusBarData setSatelliteEntry:];
-[_UIStatusBarData setSecondaryCellularEntry:];
-[_UIStatusBarData setSensorActivityEntry:];
-[_UIStatusBarData setShortTimeEntry:];
-[_UIStatusBarData setStudentEntry:];
-[_UIStatusBarData setTetheringEntry:];
-[_UIStatusBarData setThermalEntry:];
-[_UIStatusBarData setTimeEntry:];
-[_UIStatusBarData setTtyEntry:];
-[_UIStatusBarData setVoiceControlEntry:];
-[_UIStatusBarData setVpnEntry:];
-[_UIStatusBarData setWifiEntry:];
-[_UIStatusBarData shortTimeEntry];
-[_UIStatusBarData studentEntry];
-[_UIStatusBarData tetheringEntry];
-[_UIStatusBarData thermalEntry];
-[_UIStatusBarData timeEntry];
-[_UIStatusBarData ttyEntry];
-[_UIStatusBarData voiceControlEntry];
-[_UIStatusBarData volumeEntry];
-[_UIStatusBarData vpnEntry];
-[_UIStatusBarData wifiEntry];
```
