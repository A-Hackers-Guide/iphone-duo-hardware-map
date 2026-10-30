# `IOThunderboltSwitchOS2`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOThunderboltFamily`](../kexts/com.apple.iokit.IOThunderboltFamily.md)
- Object size: `0x2c8` (712 bytes)
- Metaclass: `0xfffffe000ba1ca20`; metaclass vtable `0xfffffe000840dc00`; class vtable `0xfffffe000840cde0`
- Registration (init): `0xfffffe000a4a2e5c`
- Superclasses: [`IOThunderboltSwitchOS`](IOThunderboltSwitchOS.md) → [`IOThunderboltSwitch`](IOThunderboltSwitch.md) → [`IOThunderboltNub`](IOThunderboltNub.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (2; 2 in total)

- [`IOThunderboltSwitchIntelJHL9580`](IOThunderboltSwitchIntelJHL9580.md) — `com.apple.iokit.IOThunderboltFamily`
- [`IOThunderboltSwitchType7`](IOThunderboltSwitchType7.md) — `com.apple.iokit.IOThunderboltFamily`

## Strings in its kext that name it (45)

- `%lldus IOThunderboltSwitchOS2<%p>::configureUpstreamAsymmetricMode - dispatchAsync( IOThunderboltSwitchOS2<%p>::configureUpstreamAsymmetricModeInternal )\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::configureUpstreamAsymmetricMode - wake sleeping threads\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::updateUpstreamLinkModeSupport - final values: ufp_asymmetric_support = 0x%08x, dfp_asymmetric_support = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS2(%x:%llx)::checkPathsDisabledByPortType - paths_disabled = %d for port type 0x%08x\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::configureRouter - data = 0x%08x should_configure = %d - status = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::updateUpstreamLinkModeSupport - done, status = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::updateUpstreamLinkModeSupport - ufp_supported_link_modes = 0x%08x, dfp_supported_link_modes = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::configureUpstreamAsymmetricMode - start waiting for in-progress asymmetric transition (if any)\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::setTMUParameters - set avg constant to %d. data = 0x%08x mask = 0x%08x status = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::checkCanEnterLinkModeForPort - port = (%x@%llx:0x%x), mode = %d, link_mode_entry_possible = %u, status = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::updateUpstreamLinkModeSupport - read UFP, ufp_asymmetric_support = 0x%08x, status = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::configureRouter - config ready - status = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::updateUpstreamLinkModeSupport - read DFP, dfp_asymmetric_support = 0x%08x, status = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::changeTMUMode\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::disableTMU\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::checkCanEnterLinkModeForPort - ufp = (%x@%llx:0x%x), dfp = (%x@%llx:0x%x)\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::configureRouter - router ready - status = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::updateUpstreamLinkModeSupport\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::configureRouter - write config = 0x%08x - status = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::getRequiredTMUMode - fTimeSyncNotSupported = true, disabling TMU\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::needsTMUModeChange tmu_mode=0x%x current_tmu_mode=0x%x needs_change=%d\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::setTMUParameters - set freq measurement window to %d. data = 0x%08x mask = 0x%08x status = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::updateUpstreamLinkModeSupport - check x3 transmitters ufp -> dfp, ufp_asymmetric_support = 0x%08x, dfp_asymmetric_support = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::updateUpstreamLinkModeSupport - dfp = (%x@%llx:0x%x), ufp = (%x@%llx:0x%x), ufp spec version = 0x%x, dfp spec version = 0x%x, ufp current link speed = 0x%x\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::configureUpstreamAsymmetricMode - done waiting for in-progress asymmetric transition\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::checkCanEnterLinkModeForPort - ufp supported link modes = 0x%08x, dfp supported link modes = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::updateUpstreamLinkModeSupport - check x3 transmitters dfp -> ufp, dfp_asymmetric_support = 0x%08x, ufp_asymmetric_support = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::enableTMU - tmu_mode = %d\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::updateUpstreamLinkModeSupport - cable asymmetric support = %u, status = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::checkCanEnterLinkModeForPort - port = (%x@%llx:0x%x), mode = %d\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::configureRouter - write config valid = 0x%08x - status = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::checkCanEnterLinkModeForPort - ufp_can_enter_x3_rx = %d, ufp_can_enter_x3_tx = %d\n`
- `%lldus IOThunderboltSwitchOS2(%d)::updateCLxModeInternal enable=0x%x\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::checkCanEnterLinkModeForPort - port = (%x@%llx:0x%x), mode = %d\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::updateUpstreamLinkModeSupport - read UFP, ufp_asymmetric_support = 0x%08x, status = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS2<%p>::configureUpstreamAsymmetricMode - dispatchAsync( IOThunderboltSwitchOS2<%p>::configureUpstreamAsymmetricModeInternal )\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::configureUpstreamAsymmetricMode - Failed to get cleared Asym in progress indication cleared).\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::configureUpstreamAsymmetricMode - sym -> asym ufp CL0 polling status=0x%08x.\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::changeTMUMode\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::configureUpstreamAsymmetricMode - asym -> sym step 5/6a status=0x%08x).\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::configureUpstreamAsymmetricMode - asym -> sym  Failed to get expected negotiated width (Expected=0x%x ufp_negotiated_width=0x%x status=0x%08x).\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::checkCanEnterLinkModeForPort - ufp = (%x@%llx:0x%x), dfp = (%x@%llx:0x%x)\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::disableTMU\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::updateUpstreamLinkModeSupport - read UFP failed, ufp_asymmetric_support = 0x%08x, status = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::configureRouter - write config valid = 0x%08x - status = 0x%08x\n`
