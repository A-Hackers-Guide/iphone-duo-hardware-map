# Unbound nodes

Device-tree nodes with a `compatible` string that no kernel personality names. Each is bound some other way (by its parent driver, a property or provider-class match, a DriverKit extension, an exclave or a co-processor) or not at all. The chapters column links every chapter that names the node; that is where the explanation is. **[DT][KC]**
37 nodes.

| Node | compatible | Referenced by | Chapters that discuss it |
|---|---|---|---|
| [`/cpus/cpu0`](../devicetree/root__cpus__cpu0.md) | `apple,sawtooth, ARM,v8` |  | [01](../../docs/01-soc-cpu-memory-storage.md), [02](../../docs/02-boot-and-security.md) |
| [`/cpus/cpu1`](../devicetree/root__cpus__cpu1.md) | `apple,sawtooth, ARM,v8` |  | [02](../../docs/02-boot-and-security.md) |
| [`/cpus/cpu2`](../devicetree/root__cpus__cpu2.md) | `apple,sawtooth, ARM,v8` |  | — |
| [`/cpus/cpu3`](../devicetree/root__cpus__cpu3.md) | `apple,sawtooth, ARM,v8` |  | [02](../../docs/02-boot-and-security.md) |
| [`/cpus/cpu4`](../devicetree/root__cpus__cpu4.md) | `apple,everest, ARM,v8` |  | [01](../../docs/01-soc-cpu-memory-storage.md), [02](../../docs/02-boot-and-security.md) |
| [`/cpus/cpu5`](../devicetree/root__cpus__cpu5.md) | `apple,everest, ARM,v8` |  | [01](../../docs/01-soc-cpu-memory-storage.md), [02](../../docs/02-boot-and-security.md) |
| [`/arm-io/pmgr/pmgrtools`](../devicetree/root__arm-io__pmgr__pmgrtools.md) | `pmgrtools` |  | [01](../../docs/01-soc-cpu-memory-storage.md) |
| [`/arm-io/sio/iop-sio-nub/sio-dma`](../devicetree/root__arm-io__sio__iop-sio-nub__sio-dma.md) | `sio-dma-controller` |  | [01](../../docs/01-soc-cpu-memory-storage.md), [02](../../docs/02-boot-and-security.md) |
| [`/arm-io/rsm`](../devicetree/root__arm-io__rsm.md) | `rsm,t8101` |  | [01](../../docs/01-soc-cpu-memory-storage.md) |
| [`/arm-io/mtp-aop-mux`](../devicetree/root__arm-io__mtp-aop-mux.md) | `hid-transport,mux` |  | [01](../../docs/01-soc-cpu-memory-storage.md), [05](../../docs/05-sensors-touch-audio-haptics.md) |
| [`/arm-io/atc0-dpphy`](../devicetree/root__arm-io__atc0-dpphy.md) | `atc-dpphy,t8160` |  | [03](../../docs/03-gpu-and-displays.md), [07](../../docs/07-networking-and-connectivity.md) |
| [`/arm-io/iop-audio-controller/audio-hp/audio-codec`](../devicetree/root__arm-io__iop-audio-controller__audio-hp__audio-codec.md) | `audio-data,cs42l79` |  | [01](../../docs/01-soc-cpu-memory-storage.md) |
| [`/arm-io/iop-audio-controller/audio-speaker-mca/audio-speaker`](../devicetree/root__arm-io__iop-audio-controller__audio-speaker-mca__audio-speaker.md) | `audio-data,cs35l28` |  | [05](../../docs/05-sensors-touch-audio-haptics.md) |
| [`/arm-io/iop-audio-controller/audio-haptic-transport/audio-haptic`](../devicetree/root__arm-io__iop-audio-controller__audio-haptic-transport__audio-haptic.md) | `audio-data,audio-iop-haptics` |  | [05](../../docs/05-sensors-touch-audio-haptics.md) |
| [`/arm-io/iop-audio-controller/audio-hpdbg-transport/audio-hpdbg`](../devicetree/root__arm-io__iop-audio-controller__audio-hpdbg-transport__audio-hpdbg.md) | `audio-data,audio-iop-hpdbg` |  | [05](../../docs/05-sensors-touch-audio-haptics.md) |
| [`/arm-io/admac-base-ns/base-ns-adma-rx-2`](../devicetree/root__arm-io__admac-base-ns__base-ns-adma-rx-2.md) | `audio-dma-channel,v4p0` |  | — |
| [`/arm-io/admac-base-ns/base-ns-adma-rx-3`](../devicetree/root__arm-io__admac-base-ns__base-ns-adma-rx-3.md) | `audio-dma-channel,v4p0` |  | — |
| [`/arm-io/admac-base-ns/base-ns-adma-rx-4`](../devicetree/root__arm-io__admac-base-ns__base-ns-adma-rx-4.md) | `audio-dma-channel,v4p0` |  | — |
| [`/arm-io/admac-base-ns/base-ns-adma-rx-5`](../devicetree/root__arm-io__admac-base-ns__base-ns-adma-rx-5.md) | `audio-dma-channel,v4p0` |  | — |
| [`/arm-io/admac-base-ns/base-ns-adma-tx-7`](../devicetree/root__arm-io__admac-base-ns__base-ns-adma-tx-7.md) | `audio-dma-channel,v4p0` |  | — |
| [`/arm-io/admac-base-ns/base-ns-adma-tx-8`](../devicetree/root__arm-io__admac-base-ns__base-ns-adma-tx-8.md) | `audio-dma-channel,v4p0` |  | — |
| [`/arm-io/admac-base-ns/base-ns-adma-rx-8`](../devicetree/root__arm-io__admac-base-ns__base-ns-adma-rx-8.md) | `audio-dma-channel,v4p0` |  | — |
| [`/arm-io/admac-leap-ns/leap-ns-adma-tx-1`](../devicetree/root__arm-io__admac-leap-ns__leap-ns-adma-tx-1.md) | `audio-dma-channel,v4p0` |  | — |
| [`/arm-io/admac-leap-ns/leap-ns-adma-rx-1`](../devicetree/root__arm-io__admac-leap-ns__leap-ns-adma-rx-1.md) | `audio-dma-channel,v4p0` |  | — |
| [`/arm-io/admac-leap-ns/leap-ns-adma-tx-2`](../devicetree/root__arm-io__admac-leap-ns__leap-ns-adma-tx-2.md) | `audio-dma-channel,v4p0` |  | — |
| [`/arm-io/admac-leap-ns/leap-ns-adma-tx-3`](../devicetree/root__arm-io__admac-leap-ns__leap-ns-adma-tx-3.md) | `audio-dma-channel,v4p0` |  | — |
| [`/arm-io/admac-leap-ns/leap-ns-adma-rx-3`](../devicetree/root__arm-io__admac-leap-ns__leap-ns-adma-rx-3.md) | `audio-dma-channel,v4p0` |  | — |
| [`/arm-io/admac-base-s/base-s-adma-tx-2`](../devicetree/root__arm-io__admac-base-s__base-s-adma-tx-2.md) | `audio-dma-channel,v4p0` |  | — |
| [`/arm-io/admac-base-s/base-s-adma-tx-3`](../devicetree/root__arm-io__admac-base-s__base-s-adma-tx-3.md) | `audio-dma-channel,v4p0` |  | — |
| [`/arm-io/admac-base-s/base-s-adma-rx-4`](../devicetree/root__arm-io__admac-base-s__base-s-adma-rx-4.md) | `audio-dma-channel,v4p0` |  | — |
| [`/arm-io/admac-leap-s/leap-s-adma-rx-2`](../devicetree/root__arm-io__admac-leap-s__leap-s-adma-rx-2.md) | `audio-dma-channel,v4p0` |  | — |
| [`/arm-io/dbgCPU`](../devicetree/root__arm-io__dbgCPU.md) | `AppleDebugCPU` |  | [01](../../docs/01-soc-cpu-memory-storage.md) |
| [`/arm-io/aod2`](../devicetree/root__arm-io__aod2.md) | `aod,t8101, aod,s5l8960x` |  | [01](../../docs/01-soc-cpu-memory-storage.md), [06](../../docs/06-power-battery-thermal.md) |
| [`/arm-io/aod3`](../devicetree/root__arm-io__aod3.md) | `aod,t8101, aod,s5l8960x` |  | — |
| [`/arm-io/aod4`](../devicetree/root__arm-io__aod4.md) | `aod,t8101, aod,s5l8960x` |  | — |
| [`/port-usb-c-1`](../devicetree/root__port-usb-c-1.md) | `dock,usb-c` | `/arm-io/atc-phy0`, `/arm-io/nub-spmi2/spmi-hpm0`, `/arm-io/smc/iop-smc-nub/smc-charger`, `/arm-io/smc/iop-smc-nub/smc-ext-charger`, `/arm-io/usb-drd0` | [06](../../docs/06-power-battery-thermal.md), [07](../../docs/07-networking-and-connectivity.md) |
| [`/fillmore`](../devicetree/root__fillmore.md) | `fillmore,bt` |  | [07](../../docs/07-networking-and-connectivity.md), [11](../../docs/11-userland-radios-power-sensors.md), [13](../../docs/13-lifecycle.md) |
