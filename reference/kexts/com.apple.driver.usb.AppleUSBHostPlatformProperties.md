# `com.apple.driver.usb.AppleUSBHostPlatformProperties`

- Name: com.apple.driver.usb.AppleUSBHostPlatformProperties
- Version: `1.2`
- Depends on: [`com.apple.driver.AppleUSBHostMergeProperties`](com.apple.driver.AppleUSBHostMergeProperties.md) 1.2, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 23.0.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (2) [KC]

### Mac Internal Hub Properties
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHostPlatformProperties`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `kUSBHubIdlePolicy`: `1000`
  - `kUSBHubPowerSupply`: `6400`
  - `kUSBSleepPortCurrentLimit`: `1600`
  - `kUSBWakePortCurrentLimit`: `1600`
- `idProductArray`:
  - `32777`
  - `32778`
  - `32781`
  - `32782`
- `idVendor`: `1452`

### Mac Internal Hub Properties 2
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHostPlatformProperties`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `kUSBHubIdlePolicy`: `1000`
  - `kUSBHubPowerSupply`: `4500`
  - `kUSBSleepPortCurrentLimit`: `1500`
  - `kUSBWakePortCurrentLimit`: `1500`
- `idProductArray`:
  - `32779`
  - `32780`
  - `32783`
  - `32784`
- `idVendor`: `1452`


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
- `CFBundleIdentifier`: `com.apple.driver.usb.AppleUSBHostPlatformProperties`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `com.apple.driver.usb.AppleUSBHostPlatformProperties`
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
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleRequired`: `Root`
- `OSBundleTeamIdentifier`: `Apple`
- `UIDeviceFamily`:
  - `1`
- `_CodelessKextBundlePath`: `/AppleInternal/Library/BuildRoots/4~CbSsugDd6Vzrmw5PxM2UX4EQEXBKHmg55wGjQvA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/System/Library/Extensions/IOUSBHostFamily.kext/PlugIns/AppleUSBHostPlatformProperties.kext`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOUSBHostFamily.kext/PlugIns/AppleUSBHostPlatformProperties.kext`
- `_PrelinkExecutableLoadAddr`: `9223372036854775807`
- `_PrelinkExecutableSourceAddr`: `9223372036854775807`
- `kOSBundleDextUniqueIdentifier`: `<data 52 chars>`

## Strings (0) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.
