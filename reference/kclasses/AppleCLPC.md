# `AppleCLPC`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleT8160CLPC`](../kexts/com.apple.driver.AppleT8160CLPC.md)
- Object size: `0xb0` (176 bytes)
- Metaclass: `0xfffffe000b9bda00`; metaclass vtable `0xfffffe000825e668`; class vtable `0xfffffe000825e110`
- Registration (init): `0xfffffe000983e204`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleT8160CLPC` in [`com.apple.driver.AppleT8160CLPC`](../kexts/com.apple.driver.AppleT8160CLPC.md): `IOProviderClass` = `ApplePMGRNub`, `IONameMatch` = `clpc,t8160`, `IOPropertyMatch` = `{'clpc-match-version': 3}`, `IOMatchCategory` = `IODefaultMatchCategory`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) on `clpc,t8160`

## Strings in its kext that name it (34)

- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/memory_dvf_manager.cpp`
- `AppleCLPCWorkLoop`
- `AppleCLPCUserClient`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/fabric_dvfm_table.cpp`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/ane_perf_sampler_impl.hpp`
- `site.AppleCLPC`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/cpu_cluster_perf_sampler.cpp`
- `AppleCLPCv3 start\n`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/clpc.cpp`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/perf_map_impl.hpp`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/ptd_interface_impl.hpp`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/apple_clpc.cpp`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/cpu_topology.cpp`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/cpu_temperature_sampler.cpp`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/cpu_sched_interface.cpp`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/cpu_cluster_perf_sampler_impl.hpp`
- `site.AppleCLPCWorkLoop`
- `AppleCLPC`
- `site.AppleCLPCUserClient`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/clpc.hpp`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/ane_topology.cpp`
- `AppleCLPC start failed\n`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/dashboard_manager_impl.hpp`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/ane_job_tracking_impl.hpp`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/cpu_timer.cpp`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/cpu_core_perf_sampler_impl.hpp`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/pmc_voter_interface.cpp`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/cpu_core_memstall_sampler.cpp`
- `AppleCLPC-1794.40.23.0.1`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/direct_access_energy_sampler_impl.hpp`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/gpu_dvfm_table.cpp`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/power_map.cpp`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/cpu_uncore_perf_sampler.cpp`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/cpu_dvfm_table_impl.hpp`
