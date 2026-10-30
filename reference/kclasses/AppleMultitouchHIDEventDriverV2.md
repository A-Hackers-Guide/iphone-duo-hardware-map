# `AppleMultitouchHIDEventDriverV2`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleMultitouchDriver`](../kexts/com.apple.driver.AppleMultitouchDriver.md)
- Object size: `0x148` (328 bytes)
- Metaclass: `0xfffffe000b986698`; metaclass vtable `0xfffffe00081829c8`; class vtable `0xfffffe0008182278`
- Registration (init): `0xfffffe00092dfafc`
- Superclasses: [`IOHIDEventDriver`](IOHIDEventDriver.md) → [`IOHIDEventService`](IOHIDEventService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 3 in total)

- [`AppleMultitouchInputHIDEventDriver`](AppleMultitouchInputHIDEventDriver.md) — `com.apple.driver.AppleTopCaseHIDEventDriver`

## Strings in its kext that name it (10)

- `AppleMultitouchHIDEventDriverV2`
- `AppleMultitouchHIDEventDriverV2::setMultitouchReport() reportID 0x%02x, length %d`
- `AppleMultitouchHIDEventDriverV2::simpleGetReport() for reportID 0x%02x, length %d completed`
- `AppleMultitouchHIDEventDriverV2::simpleGetReport() for reportID 0x%02x, length %d`
- `AppleMultitouchHIDEventDriverV2::getMultitouchReport() reportID 0x%02x, length %d`
- `[AppleMultitouchHIDEventDriverV2::handleInterruptReport reportID:%d (%d bytes)]`
- `AppleMultitouchHIDEventDriverV2::getMultitouchReportInfo() reportID 0x%02x`
- `AppleMultitouchHIDEventDriverV2::simpleSetReport() for reportID 0x%02x, length %d`
- `site.AppleMultitouchHIDEventDriverV2`
- `AppleMultitouchHIDEventDriverV2::enableMultitouchEvents(%s)`
