# `SBExternalDisplaySettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 5 instance variables, 5 properties, 11 instance methods, 1 class methods

## Instance variables

```
B _fakeStorageForWirelessDisplaySupport;
B _fakeStorageForUnderpoweredDeviceSupport;
q _extendedDisplayHardwareRequirementMask;
@"PTOutlet" _killSpringBoardOutlet;
d _fakeStorageForContentsScale;
```

## Properties

```
@property (Td,N,V_fakeStorageForContentsScale) fakeStorageForContentsScale;
@property (TB,N,V_fakeStorageForWirelessDisplaySupport) fakeStorageForWirelessDisplaySupport;
@property (TB,N,V_fakeStorageForUnderpoweredDeviceSupport) fakeStorageForUnderpoweredDeviceSupport;
@property (Tq,N,V_extendedDisplayHardwareRequirementMask) extendedDisplayHardwareRequirementMask;
@property (T@"PTOutlet",&,N,V_killSpringBoardOutlet) killSpringBoardOutlet;
```

## Class methods

```
+[SBExternalDisplaySettings settingsControllerModule];
```

## Instance methods

```
-[SBExternalDisplaySettings setKillSpringBoardOutlet:];
-[SBExternalDisplaySettings killSpringBoardOutlet];
-[SBExternalDisplaySettings setDefaultValues];
-[SBExternalDisplaySettings setFakeStorageForContentsScale:];
-[SBExternalDisplaySettings extendedDisplayHardwareRequirementMask];
-[SBExternalDisplaySettings fakeStorageForContentsScale];
-[SBExternalDisplaySettings fakeStorageForUnderpoweredDeviceSupport];
-[SBExternalDisplaySettings fakeStorageForWirelessDisplaySupport];
-[SBExternalDisplaySettings setExtendedDisplayHardwareRequirementMask:];
-[SBExternalDisplaySettings setFakeStorageForUnderpoweredDeviceSupport:];
-[SBExternalDisplaySettings setFakeStorageForWirelessDisplaySupport:];
```
