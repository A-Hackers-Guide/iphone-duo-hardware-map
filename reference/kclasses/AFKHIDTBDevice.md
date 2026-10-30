# `AFKHIDTBDevice`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AFKHIDTBDevice`](../kexts/com.apple.driver.AFKHIDTBDevice.md)
- Object size: `0x128` (296 bytes)
- Metaclass: `0xfffffe000b928350`; metaclass vtable `0xfffffe0007f6cd08`; class vtable `0xfffffe0007f6c678`
- Registration (init): `0xfffffe000851e5f8`
- Superclasses: [`IOHIDDevice`](IOHIDDevice.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AFKHIDTBDevice` in [`com.apple.driver.AFKHIDTBDevice`](../kexts/com.apple.driver.AFKHIDTBDevice.md): `IOProviderClass` = `AFKTightbeamEndpoint`, `IOPropertyMatch` = `{'KEXTTBInterface': 'AFKHIDDevice'}`, `IOMatchCategory` = `AFKHIDTBDevice`, `IOProbeScore` = `1000`

## Strings in its kext that name it (12)

- `\"TB_ASSERT: \" \"(afkhidtbdevice_reporttype__decode(msg, &reportType) == TB_ERROR_SUCCESS) && \\\"failed to decode type: AFKHIDTBDevice.ReportType\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `AFKHIDTBDevice_c.c`
- `/Library/Caches/com.apple.xbs/2E36C77F-9AB7-49A3-AAD4-083D32455892/TemporaryDirectory.cxrco6/Sources/AppleHIDRT/AFKHIDTBDevice/AFKHIDTBDevice/kext/AFKHIDTBDevice.cpp`
- `failed to decode type: AFKHIDTBDevice.ReportType`
- `failed to encode type: AFKHIDTBDevice.Report`
- `failed to encode type: AFKHIDTBDevice.ReportType`
- `failed to decode type: AFKHIDTBDevice.Report`
- `site.AFKHIDTBDevice`
- `\"TB_ASSERT: \" \"(afkhidtbdevice_report__decode(msg, &report) == TB_ERROR_SUCCESS) && \\\"failed to decode type: AFKHIDTBDevice.Report\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `AFKHIDTBDevice`
- `\"TB_ASSERT: \" \"(afkhidtbdevice_reporttype__raw_encode(&msg, reportType) == TB_ERROR_SUCCESS) && \\\"failed to encode type: AFKHIDTBDevice.ReportType\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"TB_ASSERT: \" \"(afkhidtbdevice_report__raw_encode(&msg, report) == TB_ERROR_SUCCESS) && \\\"failed to encode type: AFKHIDTBDevice.Report\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
