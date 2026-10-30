# `com.apple.iokit.IOHIDEventDriverSafeBoot`

- Name: I/O Kit HID Event Driver Safe Boot
- Version: `2.0.0`
- Depends on: [`com.apple.iokit.IOHIDFamily`](com.apple.iokit.IOHIDFamily.md) 1.5, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0.0b2, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0.0b2, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0.0b2, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0.0b2, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0.0b2

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (10) [KC]

### HID Built-In Orientation Driver
- `CFBundleIdentifier`: `com.apple.iokit.IOHIDFamily`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `138`
    - `DeviceUsagePage`: `32`
- `HIDDefaultBehavior`: ``
- `IOClass`: `IOHIDEventDriver`
- `IOPersonalityPublisher`: `com.apple.iokit.IOHIDEventDriverSafeBoot`
- `IOProbeScore`: `2`
- `IOPropertyMatch`:
  - `Built-In`: `True`
- `IOProviderClass`: `IOHIDInterface`

### HID Pointing Shim Driver
- `CFBundleIdentifier`: `com.apple.iokit.IOHIDFamily`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `2`
    - `DeviceUsagePage`: `1`
  -
    - `DeviceUsage`: `6`
    - `DeviceUsagePage`: `1`
  -
    - `DeviceUsage`: `7`
    - `DeviceUsagePage`: `1`
- `HIDCompatibilityInterface`: `True`
- `HIDDefaultBehavior`: ``
- `IOClass`: `IOHIDEventDriver`
- `IOPersonalityPublisher`: `com.apple.iokit.IOHIDEventDriverSafeBoot`
- `IOProviderClass`: `IOHIDInterface`

### HID Pointing/Consumer/System Control Driver
- `CFBundleIdentifier`: `com.apple.iokit.IOHIDFamily`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `2`
    - `DeviceUsagePage`: `1`
  -
    - `DeviceUsage`: `8`
    - `DeviceUsagePage`: `1`
  -
    - `DeviceUsage`: `128`
    - `DeviceUsagePage`: `1`
  -
    - `DeviceUsagePage`: `11`
  -
    - `DeviceUsagePage`: `12`
  -
    - `DeviceUsagePage`: `13`
  -
    - `DeviceUsagePage`: `16`
  -
    - `DeviceUsagePage`: `144`
- `HIDAccelCurves`:
  -
    - `HIDAccelGainLinear`: `65536`
    - `HIDAccelIndex`: `0`
    - `HIDAccelTangentSpeedLinear`: `524288`
  -
    - `HIDAccelGainCubic`: `5243`
    - `HIDAccelGainLinear`: `60293`
    - `HIDAccelGainParabolic`: `26214`
    - `HIDAccelIndex`: `8192`
    - `HIDAccelTangentSpeedLinear`: `537395`
    - `HIDAccelTangentSpeedParabolicRoot`: `1245184`
  -
    - `HIDAccelGainCubic`: `6554`
    - `HIDAccelGainLinear`: `60948`
    - `HIDAccelGainParabolic`: `36045`
    - `HIDAccelIndex`: `32768`
    - `HIDAccelTangentSpeedLinear`: `543949`
    - `HIDAccelTangentSpeedParabolicRoot`: `1179648`
  -
    - `HIDAccelGainCubic`: `7864`
    - `HIDAccelGainLinear`: `61604`
    - `HIDAccelGainParabolic`: `46531`
    - `HIDAccelIndex`: `45056`
    - `HIDAccelTangentSpeedLinear`: `550502`
    - `HIDAccelTangentSpeedParabolicRoot`: `1114112`
  -
    - `HIDAccelGainCubic`: `9830`
    - `HIDAccelGainLinear`: `62259`
    - `HIDAccelGainParabolic`: `57672`
    - `HIDAccelIndex`: `57344`
    - `HIDAccelTangentSpeedLinear`: `557056`
    - `HIDAccelTangentSpeedParabolicRoot`: `1048576`
  -
    - `HIDAccelGainCubic`: `11796`
    - `HIDAccelGainLinear`: `62915`
    - `HIDAccelGainParabolic`: `69468`
    - `HIDAccelIndex`: `65536`
    - `HIDAccelTangentSpeedLinear`: `563610`
    - `HIDAccelTangentSpeedParabolicRoot`: `983040`
  -
    - `HIDAccelGainCubic`: `14418`
    - `HIDAccelGainLinear`: `63570`
    - `HIDAccelGainParabolic`: `81920`
    - `HIDAccelIndex`: `98304`
    - `HIDAccelTangentSpeedLinear`: `570163`
    - `HIDAccelTangentSpeedParabolicRoot`: `917504`
  -
    - `HIDAccelGainCubic`: `17695`
    - `HIDAccelGainLinear`: `64225`
    - `HIDAccelGainParabolic`: `95027`
    - `HIDAccelIndex`: `131072`
    - `HIDAccelTangentSpeedLinear`: `576717`
    - `HIDAccelTangentSpeedParabolicRoot`: `851968`
  -
    - `HIDAccelGainCubic`: `21627`
    - `HIDAccelGainLinear`: `64881`
    - `HIDAccelGainParabolic`: `108790`
    - `HIDAccelIndex`: `163840`
    - `HIDAccelTangentSpeedLinear`: `583270`
    - `HIDAccelTangentSpeedParabolicRoot`: `786432`
  -
    - `HIDAccelGainCubic`: `26214`
    - `HIDAccelGainLinear`: `65536`
    - `HIDAccelGainParabolic`: `123208`
    - `HIDAccelIndex`: `196608`
    - `HIDAccelTangentSpeedLinear`: `589824`
    - `HIDAccelTangentSpeedParabolicRoot`: `786432`
- `HIDDefaultBehavior`: ``
- `IOClass`: `IOHIDEventDriver`
- `IOMatchDefer`: `True`
- `IOPersonalityPublisher`: `com.apple.iokit.IOHIDEventDriverSafeBoot`
- `IOProviderClass`: `IOHIDInterface`

### HID Repair Event Driver
- `CFBundleIdentifier`: `com.apple.iokit.IOHIDFamily`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `2`
    - `DeviceUsagePage`: `1`
- `HIDAccelCurves`:
  -
    - `HIDAccelGainLinear`: `65536`
    - `HIDAccelIndex`: `0`
    - `HIDAccelTangentSpeedLinear`: `524288`
  -
    - `HIDAccelGainCubic`: `5243`
    - `HIDAccelGainLinear`: `60293`
    - `HIDAccelGainParabolic`: `26214`
    - `HIDAccelIndex`: `8192`
    - `HIDAccelTangentSpeedLinear`: `537395`
    - `HIDAccelTangentSpeedParabolicRoot`: `1245184`
  -
    - `HIDAccelGainCubic`: `6554`
    - `HIDAccelGainLinear`: `60948`
    - `HIDAccelGainParabolic`: `36045`
    - `HIDAccelIndex`: `32768`
    - `HIDAccelTangentSpeedLinear`: `543949`
    - `HIDAccelTangentSpeedParabolicRoot`: `1179648`
  -
    - `HIDAccelGainCubic`: `7864`
    - `HIDAccelGainLinear`: `61604`
    - `HIDAccelGainParabolic`: `46531`
    - `HIDAccelIndex`: `45056`
    - `HIDAccelTangentSpeedLinear`: `550502`
    - `HIDAccelTangentSpeedParabolicRoot`: `1114112`
  -
    - `HIDAccelGainCubic`: `9830`
    - `HIDAccelGainLinear`: `62259`
    - `HIDAccelGainParabolic`: `57672`
    - `HIDAccelIndex`: `57344`
    - `HIDAccelTangentSpeedLinear`: `557056`
    - `HIDAccelTangentSpeedParabolicRoot`: `1048576`
  -
    - `HIDAccelGainCubic`: `11796`
    - `HIDAccelGainLinear`: `62915`
    - `HIDAccelGainParabolic`: `69468`
    - `HIDAccelIndex`: `65536`
    - `HIDAccelTangentSpeedLinear`: `563610`
    - `HIDAccelTangentSpeedParabolicRoot`: `983040`
  -
    - `HIDAccelGainCubic`: `14418`
    - `HIDAccelGainLinear`: `63570`
    - `HIDAccelGainParabolic`: `81920`
    - `HIDAccelIndex`: `98304`
    - `HIDAccelTangentSpeedLinear`: `570163`
    - `HIDAccelTangentSpeedParabolicRoot`: `917504`
  -
    - `HIDAccelGainCubic`: `17695`
    - `HIDAccelGainLinear`: `64225`
    - `HIDAccelGainParabolic`: `95027`
    - `HIDAccelIndex`: `131072`
    - `HIDAccelTangentSpeedLinear`: `576717`
    - `HIDAccelTangentSpeedParabolicRoot`: `851968`
  -
    - `HIDAccelGainCubic`: `21627`
    - `HIDAccelGainLinear`: `64881`
    - `HIDAccelGainParabolic`: `108790`
    - `HIDAccelIndex`: `163840`
    - `HIDAccelTangentSpeedLinear`: `583270`
    - `HIDAccelTangentSpeedParabolicRoot`: `786432`
  -
    - `HIDAccelGainCubic`: `26214`
    - `HIDAccelGainLinear`: `65536`
    - `HIDAccelGainParabolic`: `123208`
    - `HIDAccelIndex`: `196608`
    - `HIDAccelTangentSpeedLinear`: `589824`
    - `HIDAccelTangentSpeedParabolicRoot`: `786432`
- `HIDDefaultBehavior`: ``
- `IOClass`: `IOHIDEventRepairDriver`
- `IOPersonalityPublisher`: `com.apple.iokit.IOHIDEventDriverSafeBoot`
- `IOProviderClass`: `IOHIDInterface`
- `ProductID`: `8194`
- `Transport`: `Bluetooth`
- `VendorID`: `2652`

### HID SensorEvent Driver
- `CFBundleIdentifier`: `com.apple.iokit.IOHIDFamily`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `17`
    - `DeviceUsagePage`: `32`
  -
    - `DeviceUsage`: `18`
    - `DeviceUsagePage`: `32`
  -
    - `DeviceUsage`: `115`
    - `DeviceUsagePage`: `32`
  -
    - `DeviceUsage`: `122`
    - `DeviceUsagePage`: `32`
  -
    - `DeviceUsage`: `139`
    - `DeviceUsagePage`: `32`
  -
    - `DeviceUsage`: `138`
    - `DeviceUsagePage`: `32`
  -
    - `DeviceUsage`: `51`
    - `DeviceUsagePage`: `32`
  -
    - `DeviceUsage`: `22`
    - `DeviceUsagePage`: `32`
- `HIDDefaultBehavior`: ``
- `IOClass`: `IOHIDEventDriver`
- `IOMatchDefer`: `True`
- `IOPersonalityPublisher`: `com.apple.iokit.IOHIDEventDriverSafeBoot`
- `IOProviderClass`: `IOHIDInterface`
- `PrimaryVendorEvents`:
  - `4279500801`
  - `4279500802`
  - `4279500803`
  - `4278976525`

### HID SensorEvent Driver - Apple Crane Driver
- `CFBundleIdentifier`: `com.apple.iokit.IOHIDFamily`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `28`
    - `DeviceUsagePage`: `65292`
- `HIDDefaultBehavior`: ``
- `IOClass`: `IOHIDEventDriver`
- `IOMatchDefer`: `True`
- `IOPersonalityPublisher`: `com.apple.iokit.IOHIDEventDriverSafeBoot`
- `IOProbeScore`: `2`
- `IOPropertyMatch`:
  - `Built-In`: `True`
- `IOProviderClass`: `IOHIDInterface`
- `PrimaryVendorEvents`:
  - `4278976540`
  - `4278190115`

### HID SensorEvent Driver - Heart Rate
- `CFBundleIdentifier`: `com.apple.iokit.IOHIDFamily`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `22`
    - `DeviceUsagePage`: `32`
- `HIDDefaultBehavior`: ``
- `IOClass`: `IOHIDEventDriver`
- `IOMatchDefer`: `True`
- `IOPersonalityPublisher`: `com.apple.iokit.IOHIDEventDriverSafeBoot`
- `IOProbeScore`: `2`
- `IOProviderClass`: `IOHIDInterface`
- `PrimaryVendorEvents`:
  - `4279500801`
  - `4279500802`
  - `4279500803`
  - `4278976525`
- `Transport`: `BT-AACP`

### HID SensorEvent Driver - Hinge Angle
- `CFBundleIdentifier`: `com.apple.iokit.IOHIDFamily`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `228`
    - `DeviceUsagePage`: `32`
- `HIDDefaultBehavior`: ``
- `IOClass`: `IOHIDEventDriver`
- `IOMatchDefer`: `True`
- `IOPersonalityPublisher`: `com.apple.iokit.IOHIDEventDriverSafeBoot`
- `IOProbeScore`: `2`
- `IOPropertyMatch`:
  - `Built-In`: `True`
- `IOProviderClass`: `IOHIDInterface`

### HID VendorEvent Driver
- `CFBundleIdentifier`: `com.apple.iokit.IOHIDFamily`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `35`
    - `DeviceUsagePage`: `65280`
- `HIDDefaultBehavior`: ``
- `IOClass`: `IOHIDEventDriver`
- `IOMatchDefer`: `True`
- `IOPersonalityPublisher`: `com.apple.iokit.IOHIDEventDriverSafeBoot`
- `IOProviderClass`: `IOHIDInterface`
- `PrimaryVendorEvents`:
  - `4279500801`
  - `4279500802`
  - `4279500803`
  - `4278976525`

### VMWare Legacy Work-around
- `AbsoluteAxisBoundsRemovalPercentage`: `15`
- `CFBundleIdentifier`: `com.apple.iokit.IOHIDFamily`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `2`
    - `DeviceUsagePage`: `1`
  -
    - `DeviceUsage`: `8`
    - `DeviceUsagePage`: `1`
  -
    - `DeviceUsage`: `128`
    - `DeviceUsagePage`: `1`
  -
    - `DeviceUsagePage`: `11`
  -
    - `DeviceUsagePage`: `12`
  -
    - `DeviceUsagePage`: `13`
  -
    - `DeviceUsagePage`: `16`
- `HIDAccelCurves`:
  -
    - `HIDAccelGainLinear`: `65536`
    - `HIDAccelIndex`: `0`
    - `HIDAccelTangentSpeedLinear`: `524288`
  -
    - `HIDAccelGainCubic`: `5243`
    - `HIDAccelGainLinear`: `60293`
    - `HIDAccelGainParabolic`: `26214`
    - `HIDAccelIndex`: `8192`
    - `HIDAccelTangentSpeedLinear`: `537395`
    - `HIDAccelTangentSpeedParabolicRoot`: `1245184`
  -
    - `HIDAccelGainCubic`: `6554`
    - `HIDAccelGainLinear`: `60948`
    - `HIDAccelGainParabolic`: `36045`
    - `HIDAccelIndex`: `32768`
    - `HIDAccelTangentSpeedLinear`: `543949`
    - `HIDAccelTangentSpeedParabolicRoot`: `1179648`
  -
    - `HIDAccelGainCubic`: `7864`
    - `HIDAccelGainLinear`: `61604`
    - `HIDAccelGainParabolic`: `46531`
    - `HIDAccelIndex`: `45056`
    - `HIDAccelTangentSpeedLinear`: `550502`
    - `HIDAccelTangentSpeedParabolicRoot`: `1114112`
  -
    - `HIDAccelGainCubic`: `9830`
    - `HIDAccelGainLinear`: `62259`
    - `HIDAccelGainParabolic`: `57672`
    - `HIDAccelIndex`: `57344`
    - `HIDAccelTangentSpeedLinear`: `557056`
    - `HIDAccelTangentSpeedParabolicRoot`: `1048576`
  -
    - `HIDAccelGainCubic`: `11796`
    - `HIDAccelGainLinear`: `62915`
    - `HIDAccelGainParabolic`: `69468`
    - `HIDAccelIndex`: `65536`
    - `HIDAccelTangentSpeedLinear`: `563610`
    - `HIDAccelTangentSpeedParabolicRoot`: `983040`
  -
    - `HIDAccelGainCubic`: `14418`
    - `HIDAccelGainLinear`: `63570`
    - `HIDAccelGainParabolic`: `81920`
    - `HIDAccelIndex`: `98304`
    - `HIDAccelTangentSpeedLinear`: `570163`
    - `HIDAccelTangentSpeedParabolicRoot`: `917504`
  -
    - `HIDAccelGainCubic`: `17695`
    - `HIDAccelGainLinear`: `64225`
    - `HIDAccelGainParabolic`: `95027`
    - `HIDAccelIndex`: `131072`
    - `HIDAccelTangentSpeedLinear`: `576717`
    - `HIDAccelTangentSpeedParabolicRoot`: `851968`
  -
    - `HIDAccelGainCubic`: `21627`
    - `HIDAccelGainLinear`: `64881`
    - `HIDAccelGainParabolic`: `108790`
    - `HIDAccelIndex`: `163840`
    - `HIDAccelTangentSpeedLinear`: `583270`
    - `HIDAccelTangentSpeedParabolicRoot`: `786432`
  -
    - `HIDAccelGainCubic`: `26214`
    - `HIDAccelGainLinear`: `65536`
    - `HIDAccelGainParabolic`: `123208`
    - `HIDAccelIndex`: `196608`
    - `HIDAccelTangentSpeedLinear`: `589824`
    - `HIDAccelTangentSpeedParabolicRoot`: `786432`
- `HIDDefaultBehavior`: ``
- `IOClass`: `IOHIDEventDriver`
- `IOPersonalityPublisher`: `com.apple.iokit.IOHIDEventDriverSafeBoot`
- `IOProviderClass`: `IOHIDInterface`
- `ProductID`: `3`
- `VendorID`: `3599`


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
- `CFBundleIdentifier`: `com.apple.iokit.IOHIDEventDriverSafeBoot`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `I/O Kit HID Event Driver Safe Boot`
- `CFBundleNumericVersion`: `33587200`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `2.0.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `2.0.0`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `"Copyright © 2000-2018 Apple Inc. All rights reserved. [IOHIDFamily-2360.40.13.0.1]"`
- `OSBundleRequired`: `Safe Boot`
- `OSBundleTeamIdentifier`: `Apple`
- `UIDeviceFamily`:
  - `1`
- `_CodelessKextBundlePath`: `/AppleInternal/Library/BuildRoots/4~CbSsugDd6Vzrmw5PxM2UX4EQEXBKHmg55wGjQvA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/System/Library/Extensions/IOHIDFamily.kext/PlugIns/IOHIDEventDriverSafeBoot.kext`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOHIDFamily.kext/PlugIns/IOHIDEventDriverSafeBoot.kext`
- `_PrelinkExecutableLoadAddr`: `9223372036854775807`
- `_PrelinkExecutableSourceAddr`: `9223372036854775807`
- `kOSBundleDextUniqueIdentifier`: `<data 52 chars>`

## Strings (0) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.
