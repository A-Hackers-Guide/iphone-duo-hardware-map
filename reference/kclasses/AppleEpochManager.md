# `AppleEpochManager`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleEpochManager`](../kexts/com.apple.driver.AppleEpochManager.md)
- Object size: `0xb8` (184 bytes)
- Metaclass: `0xfffffe000b944d78`; metaclass vtable `0xfffffe000809b088`; class vtable `0xfffffe000809ab30`
- Registration (init): `0xfffffe0008ca4cb8`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleEpochManager` in [`com.apple.driver.AppleEpochManager`](../kexts/com.apple.driver.AppleEpochManager.md): `IOProviderClass` = `IOResources`, `IOResourceMatch` = `SEP`, `IOMatchCategory` = `AppleEpochManager`

## Strings in its kext that name it (17)

- `void AppleEpochManager::processEpochProposalsGated()`
- `bool AppleEpochManager::setBuddyDone(bool)`
- `site.AppleEpochManager`
- `AppleEpochManagerUserClient.cpp`
- `/Library/Caches/com.apple.xbs/0896B3D0-4755-4106-AE97-16B9AF5EF03F/TemporaryDirectory.H9Znna/Sources/AppleEpochManager/AppleEpochManager.cpp`
- `AppleEpochManager.cpp`
- `static IOReturn AppleEpochManagerUserClient::DispatchUserClientBuddyComplete(AppleEpochManagerUserClient *, void *, IOExternalMethodArguments *)`
- `IOReturn AppleEpochManager::signalBuddyDoneGated()`
- `AppleEpochManagerUserClient`
- `AppleEpochManager`
- `virtual bool AppleEpochManager::start(IOService *)`
- `virtual bool AppleEpochManagerUserClient::initWithTask(task_t, void *, UInt32)`
- `bool AppleEpochManager::_updateEpochCommits(SEPEpoch::Epoch *, SEPEpoch::EpochIndex, uint8_t)`
- `site.AppleEpochManagerUserClient`
- `/Library/Caches/com.apple.xbs/0896B3D0-4755-4106-AE97-16B9AF5EF03F/TemporaryDirectory.H9Znna/Sources/AppleEpochManager/AppleEpochManagerUserClient.cpp`
- `virtual bool AppleEpochManagerUserClient::start(IOService *)`
- `bool AppleEpochManager::_getSandcatOption(DTEntry, const char *)`
