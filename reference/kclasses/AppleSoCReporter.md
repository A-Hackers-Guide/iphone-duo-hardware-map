# `AppleSoCReporter`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleT8160`](../kexts/com.apple.driver.AppleT8160.md)
- Object size: `0xf0` (240 bytes)
- Metaclass: `0xfffffe000b9a67f0`; metaclass vtable `0xfffffe0008240158`; class vtable `0xfffffe000823fc00`
- Registration (init): `0xfffffe0009800a68`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSoCReporter` in [`com.apple.driver.AppleT8160`](../kexts/com.apple.driver.AppleT8160.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `soc-reporter,t8160`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/soc-reporter`](../devicetree/root__arm-io__soc-reporter.md) on `soc-reporter,t8160`

## Strings in its kext that name it (14)

- `AppleSoCReporter:: reporter %u not started \n`
- `AppleSoCReporter::start: super::start failed\n`
- `site.AppleSoCReporter`
- `AppleSoCReporter:: %s reporter started successfully\n`
- `void AppleSoCReporter::_registerReporterFactory(ReporterFactory *)`
- `AppleSoCReporter`
- `bool AppleSoCReporter::_createReporters()`
- `ReporterBase::ReporterBase(AppleSoCReporter *, const char *)`
- `\"AppleSoCReporter:: failed registerIOReporter \\n\" @%s:%d`
- `AppleSoCReporter:: AppleSoCFunctionPerfCycleCount is called but PerfCounterReporter is not enabled \n`
- `void AppleSoCReporter::_configureReporters()`
- `AppleSoCReporter: Failed to register function parent\n`
- `AppleSoCReporter::start: started successfully \n`
- `AppleSoCReporter.cpp`
