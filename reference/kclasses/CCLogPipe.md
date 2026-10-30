# `CCLogPipe`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.corecapture`](../kexts/com.apple.driver.corecapture.md)
- Object size: `0x98` (152 bytes)
- Metaclass: `0xfffffe000ba3b760`; metaclass vtable `0xfffffe00084bb460`; class vtable `0xfffffe00084bacb8`
- Registration (init): `0xfffffe000ab23580`
- Superclasses: [`CCPipe`](CCPipe.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Strings in its kext that name it (31)

- `CCLogPipe::setStreamLogLevel - Unknown Stream %s\n`
- `CCLogPipe::setStreamConsoleLogFlags - Unknown Stream %s\n`
- `CCLogPipe::updateStreamLogFlags - Unknown Stream %s\n`
- `CCLogPipe::setStreamConsoleLogFlags stream:%s flags: 0x%llx\n`
- `CCLogPipe::capture pipe not ready for capture owner: %s pipe %s\n`
- `CCLogPipe::setStreamLogFlags Flags: 0x%llx\n`
- `CCLogPipe::log - Required size (%zu) is greater than max (%zu)\n`
- `CCLogPipe::capture Failed notify user client for owner: %s pipe: %s\n`
- `CCLogPipe::withOwnerNameCapacity: Invalid pipe type(%d)\n`
- `CCLogPipe::updateLogFlags: Unknown flag action\n`
- `CCLogPipe::setStreamLogLevel stream:%s Level: 0x%x\n`
- `CCLogPipe::notifyUserSpace capture notification dropped - no user client for owner: %s pipe: %s\n`
- `CCLogPipe::setStreamConsoleLogLevel - Unknown Stream %s\n`
- `CCLogPipeUserClient::setPipeStreamLogFlags stream: %s, flags: 0x%llx\n`
- `CCLogPipe::updateStreamLogFlags stream:%s flags: 0x%s\n`
- `CCLogPipe::setStreamConsoleLogLevel: stream:%s level:%u\n`
- `CCLogPipe::getMemoryDescriptor mapPipe(0) failed rv:0x%x map:%p owner:%s pipe:%s`
- `CCLogPipe::updateStreamConsoleLogFlags stream:%s flags: 0x%s\n`
- `CCLogPipe::updateStreamConsoleLogFlags - Unknown Stream %s\n`
- `CCLogPipe::capture No privilege, not capturing owner: %s pipe %s\n`
- `CCLogPipe::log -- Attempting to write outside ring buffer\n`
- `Failed opening CCLogPipeUserClient Owner:%s Pipe:%s\n`
- `CCLogPipe::getMemoryDescriptor mapPipe(1) failed rv:0x%x map:%p owner:%s pipe:%s`
- `CCLogPipe::capture Failed to add capture event for owner: %s pipe: %s\n`
- `Created CCLogPipe (Owner: %s - Name: %s)\n`
- `CCLogPipeUserClient`
- `site.CCLogPipeUserClient`
- `CCLogPipe.cpp`
- `CCLogPipe`
- `site.CCLogPipe`
- `site.CCLogPipe_IVars`
