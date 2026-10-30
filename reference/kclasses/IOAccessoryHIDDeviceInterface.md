# `IOAccessoryHIDDeviceInterface`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOAccessoryManager`](../kexts/com.apple.iokit.IOAccessoryManager.md)
- Object size: `0x108` (264 bytes)
- Metaclass: `0xfffffe000b9f1a10`; metaclass vtable `0xfffffe000832f5a8`; class vtable `0xfffffe000832eff0`
- Registration (init): `0xfffffe0009fc0ae0`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (2; 2 in total)

- [`AppleC26HID`](AppleC26HID.md) — `com.apple.driver.AppleC26Charger`
- [`AppleC26HIDWatch`](AppleC26HIDWatch.md) — `com.apple.driver.AppleC26Charger`

## Strings in its kext that name it (49)

- `IOAccessoryHIDDeviceInterface::%s [%d / %d], isInactive=%d, in commandGate, retrieve endpoint descriptor \n`
- `%s:IOAccessoryHIDDeviceInterface::%s %llu bytes, isInactive %d \n`
- `%s:IOAccessoryHIDDeviceInterface::%s - END ret %x, isInactive() %d \n`
- `%s:IOAccessoryHIDDeviceInterface::%s [ep %u/%u] \n`
- `%s:IOAccessoryHIDDeviceInterface::%s RetHIDReport, commandID %x, bytes %llu >= %llu \n`
- `site.IOAccessoryHIDDeviceInterface`
- `%s:IOAccessoryHIDDeviceInterface::%s commandID:%02X payloadLength:%02llX sizeof(cmdID)=%lu \n`
- `%s:IOAccessoryHIDDeviceInterface::%s ep %u, isInactive()=%d \n`
- `%s:IOAccessoryHIDDeviceInterface::%s [ep %u/%u] call attach\n`
- `%s:IOAccessoryHIDDeviceInterface::%s [ep %u/%u] setProperty DescriptorKey \n`
- `%s:IOAccessoryHIDDeviceInterface::%s _hidInfoReceived=%d \n`
- `%s:IOAccessoryHIDDeviceInterface::%s commandID %x, data(%llu bytes):%s \n`
- `%s:IOAccessoryHIDDeviceInterface::%s RetHIDResponse: [ep %u], errCode %x, respID %u, len %llu \n`
- `%s:IOAccessoryHIDDeviceInterface::%s END success=%d \n`
- `%s:IOAccessoryHIDDeviceInterface::%s ver %u, ep_count %u \n`
- `%s:IOAccessoryHIDDeviceInterface::%s [ep %u/%u] END ret 0x%x \n`
- `IOAccessoryHIDDeviceInterface`
- `IOAccessoryHIDDeviceInterface::%s [%d / %d], isInactive=%d, in commandGate, create endpoint \n`
- `%s:IOAccessoryHIDDeviceInterface::%s [ep %u/%u] add to _endpoints \n`
- `%s:IOAccessoryHIDDeviceInterface::%s ENTER \n`
- `%s:IOAccessoryHIDDeviceInterface::%s Enter \n`
- `%s:IOAccessoryHIDDeviceInterface::%s ep %u, isInactive=%d \n`
- `%s:IOAccessoryHIDDeviceInterface::%s [ep %u/%u] call start \n`
- `%s:IOAccessoryHIDDeviceInterface::%s RetHIDInfo: ver %u, ep_count %u, vid %02x%02x, pid %02x%02x, country %u \n`
- `%s:IOAccessoryHIDDeviceInterface::%s END \n`
- `%s:IOAccessoryHIDDeviceInterface::%s _commandGate(%d), _commandGateOnEventSource=%d \n`
- `%s:IOAccessoryHIDDeviceInterface::%s commandID %x, %llu bytes, isInactive %d, status %x \n`
- `IOAccessoryHIDDeviceInterface::%s ENTER\n`
- `IOAccessoryHIDDeviceInterface::%s END, status %x \n`
- `%s:IOAccessoryHIDDeviceInterface::%s _handleStartThreadCall(%d) \n`
- `%s:IOAccessoryHIDDeviceInterface::%s RetHIDReportMulti, commandID %x, bytes %llu >= %llu \n`
- `%s:IOAccessoryHIDDeviceInterface::%s [ep %u/%u] setProperty EndpointIDKey \n`
- `[ERROR] IOAccessoryHIDDeviceInterface::%s failed to setup endpoints! ret %x \n`
- `%s:IOAccessoryHIDDeviceInterface::%s RetHIDResponse: [ep %u] \n`
- `%s:IOAccessoryHIDDeviceInterface::%s [ep %u], RetHIDReportMulti len %llu \n`
- `[ERROR] %s:IOAccessoryHIDDeviceInterface::%s ep %u / %u, failed to attach! endpoints(%d) \n`
- `%s:IOAccessoryHIDDeviceInterface::%s %llu bytes, isInactive %d \n`
- `%s:IOAccessoryHIDDeviceInterface::%s wakeUp _hidInfo \n`
- `%s:IOAccessoryHIDDeviceInterface::%s \n`
- `[ERROR] IOAccessoryHIDDeviceInterface::%s failed startup! status %x \n`
- `[ERROR] %s:IOAccessoryHIDDeviceInterface::%s ep %u / %u, failed to create! endpoints(%d) \n`
- `%s:IOAccessoryHIDDeviceInterface::%s RetHIDResponse: [ep %u], call _receiveDataMsg, commandID %d, len %llu, status %d \n`
- `[ERROR] %s:IOAccessoryHIDDeviceInterface::%s could not create start thread call \n`
- `%s:IOAccessoryHIDDeviceInterface::%s handleStartThreadCall was already scheduled \n`
- `%s:IOAccessoryHIDDeviceInterface::%s thread_call_cancel returned false \n`
- `[ERROR] %s:IOAccessoryHIDDeviceInterface::%s %llu bytes, isInactive %d, ret 0x%x \n`
- `%s:IOAccessoryHIDDeviceInterface::%s thread_call_cancel returned true \n`
- `[ERROR] %s:IOAccessoryHIDDeviceInterface::%s %llu bytes > UINT32_MAX! \n`
- `%s:IOAccessoryHIDDeviceInterface::%s [ep %u], reportID %u, len %llu \n`
