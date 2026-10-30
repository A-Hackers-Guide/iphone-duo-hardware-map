# `AppleEventLogHandler`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleEventLogHandler`](../kexts/com.apple.driver.AppleEventLogHandler.md)
- Object size: `0x4f0` (1,264 bytes)
- Metaclass: `0xfffffe000b944e78`; metaclass vtable `0xfffffe000809b848`; class vtable `0xfffffe000809b2f0`
- Registration (init): `0xfffffe0008ca63dc`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleEventLogHandler` in [`com.apple.driver.AppleEventLogHandler`](../kexts/com.apple.driver.AppleEventLogHandler.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `event-log-handler,t8101`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) on `event-log-handler,t8101`

## Strings in its kext that name it (12)

- `\"AppleEventLogHandler: %s:%u REQUIRE failed: %s\" @%s:%d`
- `AppleEventLogHandler.cpp`
- `UInt32 AppleEventLogHandler::_readEventLogReg(EventLogID, UInt32)`
- `AppleEventLogHandler: Register is locked down! AccessType=%s Address=0x%llx IntrID=%x RegMapID=%x Deferred=%s\n`
- `void AppleEventLogHandler::_writeEventLogReg(EventLogID, UInt32, UInt32)`
- `\"AppleEventLogHandler: No event log entry found for interrupt %d\" @%s:%d`
- `site.AppleEventLogHandler`
- `virtual bool AppleEventLogHandler::start(IOService *)`
- `\"AppleEventLogHandler: Register is locked down! AccessType=%s Address=0x%llx IntrID=%x RegMapID=%x Deferred=%s\" @%s:%d`
- `\"AppleEventLogHandler: Received %u unique EventLog entries less than %u ms apart\" @%s:%d`
- `void AppleEventLogHandler::_handleEventLogInterrupt(EventLogID, bool)`
- `AppleEventLogHandler`
