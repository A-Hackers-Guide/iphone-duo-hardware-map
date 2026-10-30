# `IOThunderboltControllerGenericACIO`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOThunderboltFamily`](../kexts/com.apple.iokit.IOThunderboltFamily.md)
- Object size: `0x1e0` (480 bytes)
- Metaclass: `0xfffffe000ba1c7c8`; metaclass vtable `0xfffffe000840a200`; class vtable `0xfffffe0008409850`
- Registration (init): `0xfffffe000a467730`
- Superclasses: [`IOThunderboltController`](IOThunderboltController.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (2; 2 in total)

- [`IOThunderboltControllerType5`](IOThunderboltControllerType5.md) — `com.apple.iokit.IOThunderboltFamily`
- [`IOThunderboltControllerType7`](IOThunderboltControllerType7.md) — `com.apple.iokit.IOThunderboltFamily`

## Strings in its kext that name it (51)

- `%lldus IOThunderboltControllerGenericACIO(%d)::getRootSwitchStaticDataForKey - status = 0x%08x\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::earlyWake - terminatedAllClients\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::createResources\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::checkPathsDisabledByPortType - protocol_flags = 0x%08x\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::loadPortMap - fPortMap = %p fPortMapEntryCount = %d status = 0x%08x\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::earlyWake - ERROR: cable_state is NULL.\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::createTunnelInterfaceManager - attach status = 0x%08x\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::loadPortDefaults - simulate hidden dp out port - fPortDefaults last entry = %08x status = 0x%08x\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::earlyWake - call super\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::getRootSwitchStaticDataForKey - hardware_service = %p status = 0x%08x\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::createTunnelInterfaceManager\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::createTunnelInterfaceManager - hardware_service = %p status = 0x%08x\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::earlyWake - terminatedAllClients returned\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::wake - fIsAsleep = %d power_on_allowed = %d\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::checkPathsDisabledByPortType - paths_disabled = %d\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::createTunnelInterfaceManager - fTunnelInterfaceManager = %p status = 0x%08x\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::earlyWake - returnfIsAsleep = %d\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::processPlugEvent - invalidateAllClients\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::destroyResources\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::setupStaticData - Found path disable boot-args = 0x%08x\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::loadPortMap - port_map_buffer = %p status = 0x%08x\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::setupStaticData - Found path disable flags in EDT = 0x%08x\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::createSwitchForDeviceHeader - Unknown VID 0x%04x DID 0x%04x\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::checkPathsDisabledByPortType - fPathDisableBootArgs = 0x%08x, fPathDisableByATCBootArgs = 0x%016llx, fPathDisableStaticFlags = 0x%08x, path_disable_flags = 0x%08x\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::processPlugEvent - plugged = %d\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::processPlugEvent - invalidateAllClients returned\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::getRootSwitchStaticDataForKey - compatibility mode - key = %s out_value = 0x%08x status = 0x%08x\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::createTunnelInterfaceManager - status = 0x%08x\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::earlyWake - fIsAsleep = %d\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::loadPortMap - hardware_service = %p status = 0x%08x\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::wake - call super\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::loadPortMap - simulate hidden dp out port - fPortDefaults last entry = %08x status = 0x%08x\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::loadPortDefaults - fPortDefaults = %p fPortDefaultsEntryCount = %d status = 0x%08x\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::setupStaticData - Found path disable by ATC boot-args = 0x%016llx\n`
- `%lldus IOThunderboltControllerGenericACIO<%p>::shutdown\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::earlyWake - connected = %d\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::loadPortDefaults - hardware_service = %p status = 0x%08x\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::loadPortDefaults - port_defaults_buffer = %p status = 0x%08x\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::destroyTunnelInterfaceManager\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::loadPortDefaults - compatibility mode - fPortDefaults = 0x%08x %08x %08x %08x %08x %08x %08x status = 0x%08x\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::checkPathsDisabledByPortType - Checking paths disabled for port type = 0x%08x\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::getRootSwitchStaticDataForKey - found key = %s out_value = 0x%08x status = 0x%08x\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::setupStaticData - Found path disable flags in EDT = 0x%08x\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::createSwitchForDeviceHeader - Unknown VID 0x%04x DID 0x%04x\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::loadPortDefaults - hardware_service = %p status = 0x%08x\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::loadPortMap - port_map_buffer = %p status = 0x%08x\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::checkPathsDisabledByPortType - paths_disabled = %d\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::createTunnelInterfaceManager - attach status = 0x%08x\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::checkPathsDisabledByPortType - protocol_flags = 0x%08x\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::loadPortMap - hardware_service = %p status = 0x%08x\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::checkPathsDisabledByPortType - Checking paths disabled for port type = 0x%08x\n`
