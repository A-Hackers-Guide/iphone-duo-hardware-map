# `IOThunderboltXDomainPath`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOThunderboltFamily`](../kexts/com.apple.iokit.IOThunderboltFamily.md)
- Object size: `0x1a8` (424 bytes)
- Metaclass: `0xfffffe000ba1d1a8`; metaclass vtable `0xfffffe0008419b68`; class vtable `0xfffffe0008419738`
- Registration (init): `0xfffffe000a56c874`
- Superclasses: [`IOThunderboltAbstractPath`](IOThunderboltAbstractPath.md)

## Direct subclasses (2; 2 in total)

- [`IOThunderboltXDomainReceivePath`](IOThunderboltXDomainReceivePath.md) — `com.apple.iokit.IOThunderboltFamily`
- [`IOThunderboltXDomainTransmitPath`](IOThunderboltXDomainTransmitPath.md) — `com.apple.iokit.IOThunderboltFamily`

## Strings in its kext that name it (60)

- `%lldus IOThunderboltXDomainPath<%p>::startRemotePathActivation - Path ID %u - deactivation requested, abort\n`
- `%lldus IOThunderboltXDomainPath<%p>::resubmitXDomainPathCapabilitiesRequest - fFinalizeWaiting = %u\n`
- `%lldus IOThunderboltXDomainPath<%p>::activateSynchronous - Path ID %u\n`
- `%lldus IOThunderboltXDomainPath<%p>::resubmitXDomainPathSetupCompleteCommand - Path ID %u - deactivation requested, abort\n`
- `%lldus IOThunderboltXDomainPath<%p>::startCompleteActivation - Path ID %u - we're done with a remote-initiated activation, submitting path setup complete notification.\n`
- `%lldus IOThunderboltXDomainPath<%p>::startRemotePathActivation - Path ID %u - fDeactivationRequested = %u\n`
- `%lldus IOThunderboltXDomainPath<%p>::startRemotePathDeactivation - Path ID %u\n`
- `%lldus IOThunderboltXDomainPath<%p>::deactivateSynchronous - Path ID %u\n`
- `%lldus IOThunderboltXDomainPath<%p>::processRemoteDeactivateComplete - Path ID %u - incoming status = 0x%x, command = %p, clearing fRemotePathUUID\n`
- `%lldus IOThunderboltXDomainPath<%p>::processRemoteActivateComplete - done, status = 0x%08x\n`
- `%lldus IOThunderboltXDomainPath<%p>::resubmitXDomainPathSetupRequestCommand - fDeactivationRequested = %u\n`
- `%lldus IOThunderboltXDomainPath<%p>::processRemoteActivateComplete - remote Path ID %u, remote Allocated Hop ID = %u, remote Allocated XDomain Hop ID = %u\n`
- `%lldus IOThunderboltXDomainPath<%p>::processLocalActivateComplete - Path ID %u - WARNING: got an error, calling cleanUpOnActivationError(), status = 0x%08x\n`
- `%lldus IOThunderboltXDomainPath<%p>::processPathSetupCompleteResponse - Path ID %u - incoming status = 0x%08x, fXDPathSetupCompleteCommand = %p, command = %p, fDeactivationRequested = %u\n`
- `%lldus IOThunderboltLocalNode<%p>::listenerCallback - kIOThunderboltXDomainPathCapabilitiesRequest = %d\n`
- `%lldus IOThunderboltXDomainPath<%p>::activateSynchronous - already activated\n`
- `%lldus IOThunderboltXDomainPath<%p>::processPathCapabilitiesRequestComplete - path capabilities request unsuccessful, status = 0x%08x\n`
- `%lldus IOThunderboltXDomainPath<%p>::processPathSetupRequestResponse - Path ID %u - incoming status = 0x%08x, fXDPathSetupRequestCommand = %p, command = %p, fDeactivationRequested = %u\n`
- `%lldus IOThunderboltXDomainPath<%p>::setSourceServiceUUID - Path ID %u - uuid = %s, status = 0x%08x\n`
- `%lldus IOThunderboltXDomainPath<%p>::processLocalDeactivateComplete - Path ID %u, incoming status = 0x%x, path = %p\n`
- `%lldus IOThunderboltXDomainPath<%p>::processRemoteActivateComplete - Path ID %u - incoming status = 0x%08x, rx_command = %p, fDeactivationRequested = %u\n`
- `%lldus IOThunderboltXDomainPath<%p>::startDeactivation - Path ID %u - path setup complete command is in progress, sleep on fXDPathSetupCompleteCommand = %p\n`
- `%lldus IOThunderboltXDomainPath<%p>::startRemotePathActivation - Path ID %u - remote path is already activated. Call processRemoteActivateCompleteSuccess().\n`
- `%lldus IOThunderboltXDomainPath<%p>::startCompleteActivation - Path ID %u - we're done with a local-initiated activation. Calling finishCompleteActivation().\n`
- `%lldus IOThunderboltXDomainPath<%p>::resubmitXDomainPathCapabilitiesRequest - fFinalizeWaiting = true, stop sending capabilities requests\n`
- `%lldus IOThunderboltXDomainPath<%p>::startLocalPathActivation - Path ID %u - deactivation requested, abort\n`
- `%lldus IOThunderboltLocalNode<%p>::listenerCallback - kIOThunderboltXDomainPathSetupRequest = %d\n`
- `%lldus IOThunderboltXDomainPath<%p>::processPathSetupCompleteResponse - Path ID %u - deactivation requested, abort\n`
- `%lldus IOThunderboltXDomainPath<%p>::startDeactivation - Path ID %u - path setup request command is in progress, sleep on fXDPathSetupRequestCommand = %p\n`
- `%lldus IOThunderboltXDomainPath<%p>::initWithXDomainLink - done, success = %u\n`
- `%lldus IOThunderboltXDomainPath<%p>::sendActivationCompletion - Path ID %u - status = 0x%08x\n`
- `%lldus IOThunderboltXDomainPath<%p>::dispatchResubmitXDomainPathSetupCompleteCommand - dispatching resubmitXDomainPathSetupCompleteCommand()\n`
- `%lldus IOThunderboltLocalNode<%p>::listenerCallback - kIOThunderboltXDomainPathSetupCompleteRequest = %d\n`
- `%lldus IOThunderboltXDomainPath<%p>::startLocalPathActivation - Path ID %u - activating local path, src (%u:0x%08llx:%u) src hop [%u-%u] dst (%u:0x%08llx:%u) dst hop [%u-%u]\n`
- `%lldus IOThunderboltXDomainPath<%p>::%s - Path ID %u - [LUUID=%s RUUID=%s] (XDS=%u LHID=%u XDHID=%u RHID=%u S=0x%08x)\n`
- `%lldus IOThunderboltXDomainPath<%p>::setRemotePathUUID - Path ID %u - uuid = %s, status = 0x%08x\n`
- `%lldus IOThunderboltXDomainPath<%p>::cleanUpOnActivationError - Path ID %u - done, deactivate_status = 0x%08x\n`
- `%lldus IOThunderboltXDomainPath<%p>::completeDeactivation - Path ID %u - fXDState = %u, fDeactivationRequested = %u, status = 0x%08x\n`
- `%lldus IOThunderboltXDomainPath<%p>::processPathSetupRequestResponse - Path ID %u - deactivation requested, abort\n`
- `%lldus IOThunderboltXDomainPath<%p>::startLocalPathActivation - Path ID %u - local path is already activated. Call processLocalActivateCompleteSuccess().\n`
- `%lldus IOThunderboltXDomainPath<%p>::startRemotePathActivation - Path ID %u - remote path is not activated. Submit fXDPathSetupRequestCommand.\n`
- `%lldus IOThunderboltXDomainPath<%p>::setDestinationServiceUUID - uuid = %s, status = 0x%08x\n`
- `%lldus IOThunderboltXDomainPath<%p>::dispatchResubmitXDomainPathSetupRequestCommand - dispatching resubmitXDomainPathSetupRequestCommand()\n`
- `%lldus IOThunderboltXDomainPath<%p>::startLocalPathDeactivation - Path ID %u\n`
- `%lldus IOThunderboltXDomainPath<%p>::processLocalActivateComplete - Path ID %u - incoming status = 0x%x, path = %p, fDeactivationRequested = %u\n`
- `%lldus IOThunderboltXDomainPath<%p>::resubmitXDomainPathSetupRequestCommand - Path ID %u - deactivation requested, abort\n`
- `%lldus IOThunderboltXDomainPath<%p>::setDestinationUUID - uuid = %s, status = 0x%08x\n`
- `%lldus IOThunderboltXDomainPath<%p>::processPathSetupCompleteResponseSuccess - Path ID %u - path setup complete notification suceeded, we're done with a remote-initiated activation. Calling finishCompleteActivation().\n`
- `%lldus IOThunderboltXDomainPath<%p>::initWithXDomainLink\n`
- `%lldus IOThunderboltXDomainPath<%p>::resubmitXDomainPathSetupCompleteCommand - fDeactivationRequested = %u\n`
- `%lldus IOThunderboltXDomainPath<%p>::processLocalDeactivateComplete - Path ID %u, done, deactivate_complete_status = 0x%08x\n`
- `%lldus IOThunderboltXDomainPath<%p>::startLocalPathActivation - Path ID %u - fDeactivationRequested = %u\n`
- `%lldus IOThunderboltXDomainPath<%p>::free - Path ID %u\n`
- `%lldus IOThunderboltXDomainPath<%p>::destroyResources - stopping fSerialDispatchQueue\n`
- `%lldus IOThunderboltXDomainPath<%p>::processPathSetupRequestResponse - Path ID %u - done, wake up fXDPathSetupRequestCommand = %p\n`
- `%lldus IOThunderboltXDomainPath<%p>::deactivateSynchronous - already deactivated\n`
- `%lldus IOThunderboltXDomainPath<%p>::startLocalPathDeactivation - Path ID %u - done, status = 0x%08x\n`
- `%lldus IOThunderboltXDomainPath<%p>::destroyResources - waiting on fSerialDispatchQueue\n`
- `%lldus IOThunderboltXDomainPath<%p>::cleanUpOnActivationError - Path ID %u - status = 0x%08x\n`
- `%lldus IOThunderboltXDomainPath<%p>::createResources - ERROR: fSerialDispatchQueue = NULL\n`
