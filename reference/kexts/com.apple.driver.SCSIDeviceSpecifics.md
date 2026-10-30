# `com.apple.driver.SCSIDeviceSpecifics`

- Name: SCSIDeviceSpecifics
- Version: `564`
- Depends on: [`com.apple.iokit.IOSCSIBlockCommandsDevice`](com.apple.iokit.IOSCSIBlockCommandsDevice.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 9.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 9.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 9.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 9.0.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (18) [KC]

### ASM236XSeries
- `CFBundleIdentifier`: `com.apple.iokit.IOSCSIBlockCommandsDevice`
- `IOClass`: `IOSCSIPeripheralDeviceType00`
- `IOPersonalityPublisher`: `com.apple.driver.SCSIDeviceSpecifics`
- `IOProviderClass`: `IOSCSIPeripheralDeviceNub`
- `IOStorageFeatures`:
  - `UnmapCapable`: `True`
- `Peripheral Device Type`: `0`
- `Product Identification`: `ASM236X NVME`
- `Vendor Identification`: `ASMT`

### CalDigitTuffNano
- `CFBundleIdentifier`: `com.apple.iokit.IOSCSIBlockCommandsDevice`
- `IOClass`: `IOSCSIPeripheralDeviceType00`
- `IOPersonalityPublisher`: `com.apple.driver.SCSIDeviceSpecifics`
- `IOProviderClass`: `IOSCSIPeripheralDeviceNub`
- `IOStorageFeatures`:
  - `UnmapCapable`: `False`
- `Peripheral Device Type`: `0`
- `Product Identification`: `Tuff nano`
- `Vendor Identification`: `CalDigit`

### CrucialX6
- `CFBundleIdentifier`: `com.apple.iokit.IOSCSIBlockCommandsDevice`
- `IOClass`: `IOSCSIPeripheralDeviceType00`
- `IOPersonalityPublisher`: `com.apple.driver.SCSIDeviceSpecifics`
- `IOProviderClass`: `IOSCSIPeripheralDeviceNub`
- `IOStorageFeatures`:
  - `UnmapCapable`: `False`
- `Peripheral Device Type`: `0`
- `Product Identification`: `Crucial X6 SSD`
- `Vendor Identification`: `Micron`

### G-DRIVE-Mobile-USBC
- `CFBundleIdentifier`: `com.apple.iokit.IOSCSIBlockCommandsDevice`
- `IOClass`: `IOSCSIPeripheralDeviceType00`
- `IOPersonalityPublisher`: `com.apple.driver.SCSIDeviceSpecifics`
- `IOProviderClass`: `IOSCSIPeripheralDeviceNub`
- `IOStorageFeatures`:
  - `UnmapCapable`: `False`
- `Peripheral Device Type`: `0`
- `Product Identification`: `mobile USB-C`
- `Vendor Identification`: `G-DRIVE`

### G-DRIVE-SES_Device
- `CFBundleIdentifier`: `com.apple.iokit.IOSCSIBlockCommandsDevice`
- `IOClass`: `IOSCSIPeripheralDeviceType00`
- `IOPersonalityPublisher`: `com.apple.driver.SCSIDeviceSpecifics`
- `IOProviderClass`: `IOSCSIPeripheralDeviceNub`
- `IOStorageFeatures`:
  - `UnmapCapable`: `False`
- `Peripheral Device Type`: `0`
- `Product Identification`: `SES Device`
- `Vendor Identification`: `G-DRIVE`

### LaCieMobileSSD
- `CFBundleIdentifier`: `com.apple.iokit.IOSCSIBlockCommandsDevice`
- `IOClass`: `IOSCSIPeripheralDeviceType00`
- `IOPersonalityPublisher`: `com.apple.driver.SCSIDeviceSpecifics`
- `IOProviderClass`: `IOSCSIPeripheralDeviceNub`
- `IOStorageFeatures`:
  - `UnmapCapable`: `False`
- `Peripheral Device Type`: `0`
- `Product Identification`: `Mobile SSD`
- `Vendor Identification`: `LaCie`

### Minipro
- `CFBundleIdentifier`: `com.apple.iokit.IOSCSIBlockCommandsDevice`
- `IOClass`: `IOSCSIPeripheralDeviceType00`
- `IOPersonalityPublisher`: `com.apple.driver.SCSIDeviceSpecifics`
- `IOProviderClass`: `IOSCSIPeripheralDeviceNub`
- `IOStorageFeatures`:
  - `UnmapCapable`: `True`
- `Peripheral Device Type`: `0`
- `Product Identification`: `Minipro USB-C`
- `Vendor Identification`: `Oyen`

### OWCEnvoyProUSBC
- `CFBundleIdentifier`: `com.apple.iokit.IOSCSIBlockCommandsDevice`
- `IOClass`: `IOSCSIPeripheralDeviceType00`
- `IOPersonalityPublisher`: `com.apple.driver.SCSIDeviceSpecifics`
- `IOProviderClass`: `IOSCSIPeripheralDeviceNub`
- `IOStorageFeatures`:
  - `UnmapCapable`: `False`
- `Peripheral Device Type`: `0`
- `Product Identification`: `Envoy Pro USB-C`
- `Vendor Identification`: `OWC`

### PromisePegasus2UnmapSupport_M4
- `CFBundleIdentifier`: `com.apple.iokit.IOSCSIBlockCommandsDevice`
- `IOClass`: `IOSCSIPeripheralDeviceType00`
- `IOPersonalityPublisher`: `com.apple.driver.SCSIDeviceSpecifics`
- `IOProviderClass`: `IOSCSIPeripheralDeviceNub`
- `IOStorageFeatures`:
  - `UnmapCapable`: `True`
- `Peripheral Device Type`: `0`
- `Product Identification`: `Pegasus2 M4`
- `Vendor Identification`: `Promise`

### PromisePegasus2UnmapSupport_R4
- `CFBundleIdentifier`: `com.apple.iokit.IOSCSIBlockCommandsDevice`
- `IOClass`: `IOSCSIPeripheralDeviceType00`
- `IOPersonalityPublisher`: `com.apple.driver.SCSIDeviceSpecifics`
- `IOProviderClass`: `IOSCSIPeripheralDeviceNub`
- `IOStorageFeatures`:
  - `UnmapCapable`: `True`
- `Peripheral Device Type`: `0`
- `Product Identification`: `Pegasus2 R4`
- `Vendor Identification`: `Promise`

### PromisePegasus2UnmapSupport_R6
- `CFBundleIdentifier`: `com.apple.iokit.IOSCSIBlockCommandsDevice`
- `IOClass`: `IOSCSIPeripheralDeviceType00`
- `IOPersonalityPublisher`: `com.apple.driver.SCSIDeviceSpecifics`
- `IOProviderClass`: `IOSCSIPeripheralDeviceNub`
- `IOStorageFeatures`:
  - `UnmapCapable`: `True`
- `Peripheral Device Type`: `0`
- `Product Identification`: `Pegasus2 R6`
- `Vendor Identification`: `Promise`

### PromisePegasus2UnmapSupport_R8
- `CFBundleIdentifier`: `com.apple.iokit.IOSCSIBlockCommandsDevice`
- `IOClass`: `IOSCSIPeripheralDeviceType00`
- `IOPersonalityPublisher`: `com.apple.driver.SCSIDeviceSpecifics`
- `IOProviderClass`: `IOSCSIPeripheralDeviceNub`
- `IOStorageFeatures`:
  - `UnmapCapable`: `True`
- `Peripheral Device Type`: `0`
- `Product Identification`: `Pegasus2 R8`
- `Vendor Identification`: `Promise`

### PromisePegasus3UnmapSupport_R4
- `CFBundleIdentifier`: `com.apple.iokit.IOSCSIBlockCommandsDevice`
- `IOClass`: `IOSCSIPeripheralDeviceType00`
- `IOPersonalityPublisher`: `com.apple.driver.SCSIDeviceSpecifics`
- `IOProviderClass`: `IOSCSIPeripheralDeviceNub`
- `IOStorageFeatures`:
  - `UnmapCapable`: `True`
- `Peripheral Device Type`: `0`
- `Product Identification`: `Pegasus3 R4`
- `Vendor Identification`: `Promise`

### PromisePegasus3UnmapSupport_R6
- `CFBundleIdentifier`: `com.apple.iokit.IOSCSIBlockCommandsDevice`
- `IOClass`: `IOSCSIPeripheralDeviceType00`
- `IOPersonalityPublisher`: `com.apple.driver.SCSIDeviceSpecifics`
- `IOProviderClass`: `IOSCSIPeripheralDeviceNub`
- `IOStorageFeatures`:
  - `UnmapCapable`: `True`
- `Peripheral Device Type`: `0`
- `Product Identification`: `Pegasus3 R6`
- `Vendor Identification`: `Promise`

### PromisePegasus3UnmapSupport_R8
- `CFBundleIdentifier`: `com.apple.iokit.IOSCSIBlockCommandsDevice`
- `IOClass`: `IOSCSIPeripheralDeviceType00`
- `IOPersonalityPublisher`: `com.apple.driver.SCSIDeviceSpecifics`
- `IOProviderClass`: `IOSCSIPeripheralDeviceNub`
- `IOStorageFeatures`:
  - `UnmapCapable`: `True`
- `Peripheral Device Type`: `0`
- `Product Identification`: `Pegasus3 R8`
- `Vendor Identification`: `Promise`

### SamsungT5
- `CFBundleIdentifier`: `com.apple.iokit.IOSCSIBlockCommandsDevice`
- `IOClass`: `IOSCSIPeripheralDeviceType00`
- `IOPersonalityPublisher`: `com.apple.driver.SCSIDeviceSpecifics`
- `IOProviderClass`: `IOSCSIPeripheralDeviceNub`
- `IOStorageFeatures`:
  - `UnmapCapable`: `False`
- `Peripheral Device Type`: `0`
- `Product Identification`: `Portable SSD T5`
- `Vendor Identification`: `Samsung`

### SamsungT7
- `CFBundleIdentifier`: `com.apple.iokit.IOSCSIBlockCommandsDevice`
- `IOClass`: `IOSCSIPeripheralDeviceType00`
- `IOPersonalityPublisher`: `com.apple.driver.SCSIDeviceSpecifics`
- `IOProviderClass`: `IOSCSIPeripheralDeviceNub`
- `IOStorageFeatures`:
  - `UnmapCapable`: `False`
- `Peripheral Device Type`: `0`
- `Product Identification`: `PSSD T7`
- `Vendor Identification`: `Samsung`

### SeagateFireCudaSSD
- `CFBundleIdentifier`: `com.apple.iokit.IOSCSIBlockCommandsDevice`
- `IOClass`: `IOSCSIPeripheralDeviceType00`
- `IOPersonalityPublisher`: `com.apple.driver.SCSIDeviceSpecifics`
- `IOProviderClass`: `IOSCSIPeripheralDeviceNub`
- `IOStorageFeatures`:
  - `UnmapCapable`: `False`
- `Peripheral Device Type`: `0`
- `Product Identification`: `FireCuda SSD`
- `Vendor Identification`: `Seagate`


## C++ classes (0) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|

## Mach-O layout [KC]

```
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleGetInfoString`: `564, Copyright Apple Inc. 2002-2016`
- `CFBundleIdentifier`: `com.apple.driver.SCSIDeviceSpecifics`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `SCSIDeviceSpecifics`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `564`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `564`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `OSBundleRequired`: `Local-Root`
- `OSBundleTeamIdentifier`: `Apple`
- `UIDeviceFamily`:
  - `1`
- `_CodelessKextBundlePath`: `/AppleInternal/Library/BuildRoots/4~CbSsugDd6Vzrmw5PxM2UX4EQEXBKHmg55wGjQvA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/System/Library/Extensions/AppleStorageDrivers.kext/PlugIns/SCSIDeviceSpecifics.kext`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleStorageDrivers.kext/PlugIns/SCSIDeviceSpecifics.kext`
- `_PrelinkExecutableLoadAddr`: `9223372036854775807`
- `_PrelinkExecutableSourceAddr`: `9223372036854775807`
- `kOSBundleDextUniqueIdentifier`: `<data 52 chars>`

## Strings (0) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.
