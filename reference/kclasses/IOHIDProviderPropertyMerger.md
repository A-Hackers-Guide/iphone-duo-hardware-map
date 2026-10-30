# `IOHIDProviderPropertyMerger`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOHIDFamily`](../kexts/com.apple.iokit.IOHIDFamily.md)
- Object size: `0x90` (144 bytes)
- Metaclass: `0xfffffe000b9f6d98`; metaclass vtable `0xfffffe0008399bf0`; class vtable `0xfffffe0008399688`
- Registration (init): `0xfffffe000a1cd04c`
- Superclasses: [`IOProviderPropertyMerger`](IOProviderPropertyMerger.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (22)

- `GC User Driver Service` in [`com.apple.driver.AppleGameControllerPersonality`](../kexts/com.apple.driver.AppleGameControllerPersonality.md): `IOProviderClass` = `AppleGCHIDUserEventDriver`, `IOProbeScore` = `10`
- `Apple Pencil DM Property Merger (Pencil 1 wired)` in [`com.apple.driver.ApplePencilDriver`](../kexts/com.apple.driver.ApplePencilDriver.md): `IOProviderClass` = `IOHIDDevice`, `IOPropertyMatch` = `{'PrimaryUsage': 11, 'PrimaryUsagePage': 65280, 'ProductID': 786, 'VendorID': 14`, `IOProbeScore` = `1000`
- `Apple Pencil DM Property Merger (Pencil 1 wireless)` in [`com.apple.driver.ApplePencilDriver`](../kexts/com.apple.driver.ApplePencilDriver.md): `IOProviderClass` = `IOHIDDevice`, `IOPropertyMatch` = `{'PrimaryUsage': 11, 'PrimaryUsagePage': 65280, 'ProductID': 546, 'VendorID': 76`, `IOProbeScore` = `1000`
- `Apple Pencil DM Property Merger (Pencil 2 wireless)` in [`com.apple.driver.ApplePencilDriver`](../kexts/com.apple.driver.ApplePencilDriver.md): `IOProviderClass` = `IOHIDDevice`, `IOPropertyMatch` = `{'PrimaryUsage': 11, 'PrimaryUsagePage': 65280, 'ProductID': 332, 'VendorID': 76`, `IOProbeScore` = `1000`
- `Apple Pencil DM Property Merger (Pencil 2.5 wired)` in [`com.apple.driver.ApplePencilDriver`](../kexts/com.apple.driver.ApplePencilDriver.md): `IOProviderClass` = `IOHIDDevice`, `IOPropertyMatch` = `{'PrimaryUsage': 11, 'PrimaryUsagePage': 65280, 'ProductID': 1057, 'VendorID': 1`, `IOProbeScore` = `1000`
- `Apple Pencil DM Property Merger (Pencil 2.5 wireless)` in [`com.apple.driver.ApplePencilDriver`](../kexts/com.apple.driver.ApplePencilDriver.md): `IOProviderClass` = `IOHIDDevice`, `IOPropertyMatch` = `{'PrimaryUsage': 11, 'PrimaryUsagePage': 65280, 'ProductID': 482, 'VendorID': 76`, `IOProbeScore` = `1000`
- `Apple Pencil DM Property Merger (Pencil 3 wireless)` in [`com.apple.driver.ApplePencilDriver`](../kexts/com.apple.driver.ApplePencilDriver.md): `IOProviderClass` = `IOHIDDevice`, `IOPropertyMatch` = `{'PrimaryUsage': 11, 'PrimaryUsagePage': 65280, 'ProductID': 1106, 'VendorID': 7`, `IOProbeScore` = `1000`
- `Apple Pencil Haptics Property Merger` in [`com.apple.driver.ApplePencilDriver`](../kexts/com.apple.driver.ApplePencilDriver.md): `IOProviderClass` = `IOHIDDevice`, `IOPropertyMatch` = `{'PrimaryUsage': 4101, 'PrimaryUsagePage': 65376, 'ProductID': 1106, 'VendorID':`, `IOProbeScore` = `1000`
- `Apple Pencil Haptics Property Merger (old usage)` in [`com.apple.driver.ApplePencilDriver`](../kexts/com.apple.driver.ApplePencilDriver.md): `IOProviderClass` = `IOHIDDevice`, `IOPropertyMatch` = `{'PrimaryUsage': 1, 'PrimaryUsagePage': 65326, 'ProductID': 1106, 'VendorID': 76`, `IOProbeScore` = `1000`
- `Apple Pencil Motion Property Merger (Pencil 3)` in [`com.apple.driver.ApplePencilDriver`](../kexts/com.apple.driver.ApplePencilDriver.md): `IOProviderClass` = `IOHIDDevice`, `IOPropertyMatch` = `{'PrimaryUsage': 51, 'PrimaryUsagePage': 65280, 'ProductID': 1106, 'VendorID': 7`, `IOProbeScore` = `1000`
- `KeyboardA Property Merge` in [`com.apple.iokit.IOAccessoryManager`](../kexts/com.apple.iokit.IOAccessoryManager.md): `IOProviderClass` = `IOHIDDevice`, `IOPropertyMatch` = `{'ProductID': 53521, 'VendorID': 1133}`
- `KeyboardB Property Merge` in [`com.apple.iokit.IOAccessoryManager`](../kexts/com.apple.iokit.IOAccessoryManager.md): `IOProviderClass` = `IOHIDDevice`, `IOPropertyMatch` = `{'ProductID': 53520, 'VendorID': 1133}`
- `PSVR2SenseDevice User Client` in [`com.apple.iokit.IOGameControllerFamily`](../kexts/com.apple.iokit.IOGameControllerFamily.md): `IOProviderClass` = `PSVR2SenseDevice`, `IOProbeScore` = `1000`
- `IOFastPath Support Merger` in [`com.apple.iokit.IOHIDFamily`](../kexts/com.apple.iokit.IOHIDFamily.md): `IOProviderClass` = `IOHIDDevice`
- `IOHIDEventServiceUserClient` in [`com.apple.iokit.IOHIDFamily`](../kexts/com.apple.iokit.IOHIDFamily.md): `IOProviderClass` = `IOHIDEventService`
- `IOHIDLibUserClient` in [`com.apple.iokit.IOHIDFamily`](../kexts/com.apple.iokit.IOHIDFamily.md): `IOProviderClass` = `IOHIDDevice`
- `R1 Merge` in [`com.apple.iokit.IOHIDFamily`](../kexts/com.apple.iokit.IOHIDFamily.md): `IOProviderClass` = `IOHIDDevice`, `IOPropertyMatch` = `{'PrimaryUsage': 27, 'PrimaryUsagePage': 65280}`
- `Keyboard Touch ID Remap iOS/tvOS - TopCase - 666` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `AppleHIDKeyboardEventDriverV2`, `IOPropertyMatch` = `{'ProductID': 666}`
- `Keyboard Touch ID Remap iOS/tvOS - TopCase - 671` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `AppleHIDKeyboardEventDriverV2`, `IOPropertyMatch` = `{'ProductID': 671}`
- `Keyboard Touch ID Remap iOS/tvOS - TopCase - 801` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `AppleHIDKeyboardEventDriverV2`, `IOPropertyMatch` = `{'ProductID': 801}`
- `Keyboard Touch ID Remap iOS/tvOS - TopCase - 802` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `AppleHIDKeyboardEventDriverV2`, `IOPropertyMatch` = `{'ProductID': 802}`
- `iPad Magic Keyboard - ACL - TopCase - 1104` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDDevice`

## Strings in its kext that name it (2)

- `IOHIDProviderPropertyMerger`
- `site.IOHIDProviderPropertyMerger`
