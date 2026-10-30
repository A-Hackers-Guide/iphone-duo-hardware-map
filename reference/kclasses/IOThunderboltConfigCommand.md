# `IOThunderboltConfigCommand`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOThunderboltFamily`](../kexts/com.apple.iokit.IOThunderboltFamily.md)
- Object size: `0x98` (152 bytes)
- Metaclass: `0xfffffe000ba1c9f8`; metaclass vtable `0xfffffe000840cd48`; class vtable `0xfffffe000840cc08`
- Registration (init): `0xfffffe000a497f38`
- Superclasses: [`IOThunderboltCommand`](IOThunderboltCommand.md) → [`IOCommand`](IOCommand.md)

## Direct subclasses (15; 29 in total)

- [`IOThunderboltConfigCMOverrideCommand`](IOThunderboltConfigCMOverrideCommand.md) — `com.apple.iokit.IOThunderboltFamily`
- [`IOThunderboltConfigCompareSwapCommand`](IOThunderboltConfigCompareSwapCommand.md) — `com.apple.iokit.IOThunderboltFamily`
- [`IOThunderboltConfigErrorCommand`](IOThunderboltConfigErrorCommand.md) — `com.apple.iokit.IOThunderboltFamily`
- [`IOThunderboltConfigModifyQuadletCommand`](IOThunderboltConfigModifyQuadletCommand.md) — `com.apple.iokit.IOThunderboltFamily`
- [`IOThunderboltConfigNotifyAckCommand`](IOThunderboltConfigNotifyAckCommand.md) — `com.apple.iokit.IOThunderboltFamily`
- [`IOThunderboltConfigPollQuadletCommand`](IOThunderboltConfigPollQuadletCommand.md) — `com.apple.iokit.IOThunderboltFamily`
- [`IOThunderboltConfigPrepareToSleepCommand`](IOThunderboltConfigPrepareToSleepCommand.md) — `com.apple.iokit.IOThunderboltFamily`
- [`IOThunderboltConfigReadCommand`](IOThunderboltConfigReadCommand.md) — `com.apple.iokit.IOThunderboltFamily`
- [`IOThunderboltConfigReadQuadletCommand`](IOThunderboltConfigReadQuadletCommand.md) — `com.apple.iokit.IOThunderboltFamily`
- [`IOThunderboltConfigResetCommand`](IOThunderboltConfigResetCommand.md) — `com.apple.iokit.IOThunderboltFamily`
- [`IOThunderboltConfigWriteCommand`](IOThunderboltConfigWriteCommand.md) — `com.apple.iokit.IOThunderboltFamily`
- [`IOThunderboltConfigWriteQuadletCommand`](IOThunderboltConfigWriteQuadletCommand.md) — `com.apple.iokit.IOThunderboltFamily`
- [`IOThunderboltConfigXDomainCommand`](IOThunderboltConfigXDomainCommand.md) — `com.apple.iokit.IOThunderboltFamily`
- [`IOThunderboltConfigXDomainLinkChangeRequestCommand`](IOThunderboltConfigXDomainLinkChangeRequestCommand.md) — `com.apple.iokit.IOThunderboltFamily`
- [`IOThunderboltConfigXDomainLinkStatusRequestCommand`](IOThunderboltConfigXDomainLinkStatusRequestCommand.md) — `com.apple.iokit.IOThunderboltFamily`

## Strings in its kext that name it (17)

- `%lldus IOThunderboltConfigCommand - error_port = 0x%x\n`
- `%lldus IOThunderboltConfigCommand - end of route\n`
- `%lldus IOThunderboltConfigCommand - kConfigCommandNotClaimedInvalid - exact route mismatch\n`
- `%lldus IOThunderboltConfigCommand<%p>::processResponse - CRC error! crc = 0x%08x, calc_crc = 0x%08x\n`
- `%lldus IOThunderboltConfigCommand<%p>::complete - target = %p, action = %p\n`
- `%lldus IOThunderboltConfigCommand - kConfigCommandNotClaimedInvalid - error port in route mismatch\n`
- `%lldus IOThunderboltConfigCommand<%p>::free\n`
- `%lldus IOThunderboltConfigCommand - kConfigCommandNotClaimedInvalid - not exact route mismatch\n`
- `%lldus IOThunderboltConfigCommand - error_route_port = 0x%x command_route_port = 0x%x\n`
- `%lldus IOThunderboltConfigCommand - kConfigCommandNotClaimedInvalid - route mismatch\n`
- `%lldus IOThunderboltConfigCommand<%p>::complete\n`
- `%lldus IOThunderboltConfigCommand<%p>::processRequestComplete - PktVerify - Request has mismatched route 0x%llx vs 0x%llx\n`
- `%lldus IOThunderboltConfigCommand<%p>::processResponse - PktVerify - Response has mismatched route 0x%llx vs 0x%llx\n`
- `%lldus IOThunderboltConfigCommand<%p>::initWithController\n`
- `%lldus IOThunderboltConfigCommand - error_code = %d exact_match = %d not_exact_match = %d error_port_in_route = %d command_status = %d\n`
- `%lldus IOThunderboltConfigCommand - fRouteString = 0x%llx error_route = 0x%llx error_port = 0x%x details = 0x%08x\n`
- `%lldus IOThunderboltConfigCommand - kConfigCommandNotClaimedInvalid - error port in route mismatch\n`
