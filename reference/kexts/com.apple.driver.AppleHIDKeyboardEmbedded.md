# `com.apple.driver.AppleHIDKeyboardEmbedded`

- Name: AppleHIDKeyboardEmbedded
- Version: `1.2.0a3`
- Depends on: [`com.apple.iokit.IOHIDFamily`](com.apple.iokit.IOHIDFamily.md) 1.4, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 10.0.0d2, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 10.0.0d2

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (3) [KC]

### iAP B62 ANSI Map
- `CFBundleIdentifier`: `com.apple.iokit.IOHIDFamily`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `6`
    - `DeviceUsagePage`: `1`
  -
    - `DeviceUsage`: `7`
    - `DeviceUsagePage`: `1`
- `FnFunctionUsageMap`: `0x00070029,0x000c0040,0x0007003a,0x000C0221,0x0007003b,0xff010021,0x0007003c,0xff010020,0x0007003d,0x000c01b1,0x0007003e,0x000c01ae,0x00070040,0x000C00B4,0x00070041,0x000C00CD,0x00070042,0x000C00B3,0x00070043,0x000C00E2,0x00070044,0x000C00EA,0x00070045,0x000C00E9,0x00070068,0x000C0030`
- `FnModifierUsage`: `3`
- `FnModifierUsagePage`: `255`
- `HIDDefaultBehavior`: `Keyboard`
- `IOClass`: `AppleEmbeddedKeyboard`
- `IOPersonalityPublisher`: `com.apple.driver.AppleHIDKeyboardEmbedded`
- `IOProviderClass`: `IOHIDInterface`
- `ProductID`: `572`
- `StandardType`: `0`
- `VendorID`: `1452`

### iAP B62 ISO Map
- `CFBundleIdentifier`: `com.apple.iokit.IOHIDFamily`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `6`
    - `DeviceUsagePage`: `1`
  -
    - `DeviceUsage`: `7`
    - `DeviceUsagePage`: `1`
- `FnFunctionUsageMap`: `0x00070029,0x000c0040,0x0007003a,0x000C0221,0x0007003b,0xff010021,0x0007003c,0xff010020,0x0007003d,0x000c01b1,0x0007003e,0x000c01ae,0x00070040,0x000C00B4,0x00070041,0x000C00CD,0x00070042,0x000C00B3,0x00070043,0x000C00E2,0x00070044,0x000C00EA,0x00070045,0x000C00E9,0x00070068,0x000C0030`
- `FnModifierUsage`: `3`
- `FnModifierUsagePage`: `255`
- `HIDDefaultBehavior`: `Keyboard`
- `IOClass`: `AppleEmbeddedKeyboard`
- `IOPersonalityPublisher`: `com.apple.driver.AppleHIDKeyboardEmbedded`
- `IOProviderClass`: `IOHIDInterface`
- `ProductID`: `573`
- `StandardType`: `1`
- `VendorID`: `1452`

### iAP B62 JIS Map
- `CFBundleIdentifier`: `com.apple.iokit.IOHIDFamily`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `6`
    - `DeviceUsagePage`: `1`
  -
    - `DeviceUsage`: `7`
    - `DeviceUsagePage`: `1`
- `FnFunctionUsageMap`: `0x00070029,0x000c0040,0x0007003a,0x000C0221,0x0007003b,0xff010021,0x0007003c,0xff010020,0x0007003d,0x000c01b1,0x0007003e,0x000c01ae,0x00070040,0x000C00B4,0x00070041,0x000C00CD,0x00070042,0x000C00B3,0x00070043,0x000C00E2,0x00070044,0x000C00EA,0x00070045,0x000C00E9,0x00070068,0x000C0030`
- `FnModifierUsage`: `3`
- `FnModifierUsagePage`: `255`
- `HIDDefaultBehavior`: `Keyboard`
- `IOClass`: `AppleEmbeddedKeyboard`
- `IOPersonalityPublisher`: `com.apple.driver.AppleHIDKeyboardEmbedded`
- `IOProviderClass`: `IOHIDInterface`
- `KeyboardUsageMap`:
  - `0x00ff0003`: `458982`
  - `0xff010003`: `458982`
- `ProductID`: `574`
- `StandardType`: `2`
- `VendorID`: `1452`


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
- `CFBundleGetInfoString`: `1.2.0a3`
- `CFBundleIdentifier`: `com.apple.driver.AppleHIDKeyboardEmbedded`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleHIDKeyboardEmbedded`
- `CFBundleNumericVersion`: `18890755`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.2.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.2.0a3`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2009 Apple Inc.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleRequired`: `Console`
- `OSBundleTeamIdentifier`: `None`
- `UIDeviceFamily`:
  - `1`
- `_CodelessKextBundlePath`: `/AppleInternal/Library/BuildRoots/4~CbSsugDd6Vzrmw5PxM2UX4EQEXBKHmg55wGjQvA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/System/Library/Extensions/AppleHIDKeyboardEmbedded.kext`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleHIDKeyboardEmbedded.kext`
- `_PrelinkExecutableLoadAddr`: `9223372036854775807`
- `_PrelinkExecutableSourceAddr`: `9223372036854775807`
- `kOSBundleDextUniqueIdentifier`: `<data 52 chars>`

## Strings (0) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.
