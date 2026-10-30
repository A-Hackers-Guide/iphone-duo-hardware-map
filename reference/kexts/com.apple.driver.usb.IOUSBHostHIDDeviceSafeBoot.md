# `com.apple.driver.usb.IOUSBHostHIDDeviceSafeBoot`

- Name: I/O Kit Driver for USB HID Devices
- Version: `1.2`
- Depends on: [`com.apple.driver.usb.AppleUSBCommon`](com.apple.driver.usb.AppleUSBCommon.md) 1.0, [`com.apple.driver.usb.IOUSBHostHIDDevice`](com.apple.driver.usb.IOUSBHostHIDDevice.md) 1.2

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (3) [KC]

### IOUSBHostHIDDevice0
- `CFBundleIdentifier`: `com.apple.driver.usb.IOUSBHostHIDDevice`
- `HIDDefaultBehavior`: ``
- `IOClass`: `IOUSBHostHIDDevice`
- `IOMatchDefer`: `True`
- `IOPersonalityPublisher`: `com.apple.driver.usb.IOUSBHostHIDDeviceSafeBoot`
- `IOProviderClass`: `IOUSBHostInterface`
- `bInterfaceClass`: `3`
- `bInterfaceSubClass`: `0`

### IOUSBHostHIDDevice1
- `CFBundleIdentifier`: `com.apple.driver.usb.IOUSBHostHIDDevice`
- `HIDDefaultBehavior`: ``
- `IOClass`: `IOUSBHostHIDDevice`
- `IOMatchDefer`: `True`
- `IOPersonalityPublisher`: `com.apple.driver.usb.IOUSBHostHIDDeviceSafeBoot`
- `IOProviderClass`: `IOUSBHostInterface`
- `bInterfaceClass`: `3`
- `bInterfaceSubClass`: `1`

### SaitekP2500
- `CFBundleIdentifier`: `com.apple.driver.usb.IOUSBHostHIDDevice`
- `HIDDefaultBehavior`: ``
- `IOClass`: `IOUSBHostHIDDevice`
- `IOPersonalityPublisher`: `com.apple.driver.usb.IOUSBHostHIDDeviceSafeBoot`
- `IOProviderClass`: `IOUSBHostInterface`
- `bConfigurationValue`: `1`
- `bInterfaceNumber`: `0`
- `idProduct`: `65292`
- `idVendor`: `1699`


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
- `CFBundleIdentifier`: `com.apple.driver.usb.IOUSBHostHIDDeviceSafeBoot`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `I/O Kit Driver for USB HID Devices`
- `CFBundleNumericVersion`: `18907136`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.2`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.2`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2000-2025 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.2`
- `OSBundleRequired`: `Safe Boot`
- `OSBundleTeamIdentifier`: `Apple`
- `UIDeviceFamily`:
  - `1`
- `_CodelessKextBundlePath`: `/AppleInternal/Library/BuildRoots/4~CbSsugDd6Vzrmw5PxM2UX4EQEXBKHmg55wGjQvA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/System/Library/Extensions/IOUSBHostFamily.kext/PlugIns/IOUSBHostHIDDeviceSafeBoot.kext`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOUSBHostFamily.kext/PlugIns/IOUSBHostHIDDeviceSafeBoot.kext`
- `_PrelinkExecutableLoadAddr`: `9223372036854775807`
- `_PrelinkExecutableSourceAddr`: `9223372036854775807`
- `kOSBundleDextUniqueIdentifier`: `<data 52 chars>`

## Strings (0) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.
