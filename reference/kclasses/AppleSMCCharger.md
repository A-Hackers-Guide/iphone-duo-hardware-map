# `AppleSMCCharger`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSMC`](../kexts/com.apple.driver.AppleSMC.md)
- Object size: `0xe8` (232 bytes)
- Metaclass: `0xfffffe000b99b570`; metaclass vtable `0xfffffe0008201788`; class vtable `0xfffffe0008201228`
- Registration (init): `0xfffffe0009684aac`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSMCCharger` in [`com.apple.driver.AppleSMC`](../kexts/com.apple.driver.AppleSMC.md): `IOProviderClass` = `AppleSMCInterface`, `IONameMatch` = `['smc-charger', 'smc-orion-charger']`, `IOProbeScore` = `1000`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/smc/iop-smc-nub/smc-charger`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-charger.md) on `smc-charger`

## Strings in its kext that name it (60)

- `(AppleSMCChargerUtil): (port:%d) setWinningPowerSourceOption Type:%d V:%d I:%d\n\n`
- `(AppleSMCChargerUtil): %s:%d %s() Auth Status Change notification received\n\n`
- `(AppleSMCChargerUtil): POWER_STATE_NOTIFY\n\n`
- `(AppleSMCChargerUtil): IOPort returned null\n`
- `(AppleSMCChargerUtil): AppleSMCChargerUtil service registered!\n\n`
- `(AppleSMCChargerUtil): Failed to create optionsArr!\n\n`
- `(AppleSMCChargerUtil): _smcNotifArgArrLock not allocated!\n\n`
- `(AppleSMCChargerUtil): matching failed\n\n`
- `AppleSMCChargerFunction`
- `(AppleSMCChargerUtil): Failed to obtain workloop!\n\n`
- `(AppleSMCChargerUtil): %s() port:%d evt_subtype:%d\n\n`
- `AppleSMCCharger::start() ignoring hvc keys\n`
- `(AppleSMCChargerUtil): Read ATP%d key failed ret:%s!\n\n`
- `(AppleSMCChargerUtil): Read D%dST key failed! ret:%s\n\n`
- `(AppleSMCChargerUtil): %s() port:%d winnerType:%d winnerIdx:%d \n\n`
- `(AppleSMCChargerUtil): %s() mtype:%d payload0:%d payload1:%d\n`
- `(AppleSMCChargerUtil): Read ANWP key failed! ret:%s\n\n`
- `(AppleSMCChargerUtil): OverCurrent event sent to IOPort:%d\n\n`
- `(AppleSMCChargerUtil): Read D%dPt key failed dock:%d! ret:%s\n\n`
- `(AppleSMCChargerUtil): Read AC-W key failed! ret:%s\n\n`
- `(AppleSMCChargerUtil): AppleSMCAdapterSourceOptionType__PD (port:%d) V:%d I:%d\n\n`
- `AppleSMCChargerPS`
- `(AppleSMCChargerUtil): %s()\n\n`
- `(AppleSMCChargerUtil): Read D%dPt key failed dock:%d! ret1:%s\n\n`
- `(AppleSMCChargerUtil): Dock-num property not found!\n\n`
- `(AppleSMCChargerUtil): dockNum %d, magSafeAuth %d, reportPortEvents %d\n\n`
- `(AppleSMCChargerUtil): Kext Init!\n\n`
- `/Library/Caches/com.apple.xbs/54E255AF-DD90-4507-9BE8-379A89574EFC/TemporaryDirectory.eUdRVs/Sources/AppleSMC/AppleSMCEmbeddedCharger/AppleSMCChargerUtil.cpp`
- `(AppleSMCChargerUtil): Bad smcIf!\n\n`
- `(AppleSMCChargerUtil): %s() NULL PowerInFeature port:%d dock:%d _pwrKeysSupported:%d \n\n`
- `/Library/Caches/com.apple.xbs/54E255AF-DD90-4507-9BE8-379A89574EFC/TemporaryDirectory.eUdRVs/Sources/AppleSMC/AppleSMCEmbeddedCharger/AppleSMCCharger.cpp`
- `(AppleSMCChargerUtil): Failed start provider!\n\n`
- `(AppleSMCChargerUtil): SMCIF notification registration failed (ret:%s)!\n\n`
- `(AppleSMCChargerUtil): %s:%d %s() matching notification unsuccessful\n\n`
- `(AppleSMCChargerUtil): Read D%dRp key failed! ret:%s\n\n`
- `(AppleSMCChargerUtil): %s:%d %s() matching notification unsuccessful!\n\n`
- `site.AppleSMCCharger`
- `(AppleSMCChargerUtil): D%dST is 0! dock:%d!\n\n`
- `(AppleSMCChargerUtil): Kext Start!\n\n`
- `(AppleSMCChargerUtil): Failed to create powersource!\n\n`
- `(AppleSMCChargerUtil): No valid power params!\n\n`
- `(AppleSMCChargerUtil): %s:%d %s() registered for Auth Notifications\n\n`
- `(AppleSMCChargerUtil): _argArray not allocated!\n\n`
- `(AppleSMCChargerUtil): SMC key write %d unsuccessful (ret:%s)\n\n`
- `AppleSMCChargerUtil`
- `site.AppleSMCChargerPS`
- `(AppleSMCChargerUtil): AppleSMCAdapterSourceOptionType__TypeC (port:%d) V:%d I:%d\n\n`
- `(AppleSMCChargerUtil): %d key write status %d, AuthStatus %d\n\n`
- `(AppleSMCChargerUtil): Failed to create threadCall!\n\n`
- `site.AppleSMCChargerUtil`
- `(AppleSMCChargerUtil): SYSTEM_STATE_NOTIFY\n\n`
- `(AppleSMCChargerUtil): AppleSMCAdapterSourceOptionType__BrickID (port:%d) V:%d I:%d\n\n`
- `site.AppleSMCChargerFunction`
- `(AppleSMCChargerUtil): Read D%dBI key failed ret:(%s)!\n\n`
- `(AppleSMCChargerUtil): %s() port:%d\n\n`
- `(AppleSMCChargerUtil): SMC key for Auth is unavailable, not proceeding\n\n`
- `AppleSMCCharger`
- `(AppleSMCChargerUtil): %s() port:%d dock:%d \n\n`
- `(AppleSMCChargerUtil): D%dST is 0! dock:%d!\n\n`
- `(AppleSMCChargerUtil): Failed to create powersource!\n\n`
