# Device-tree property dictionary

2,197 distinct property names across 552 nodes. Shapes are inferred from length and content (string, u32, u64, empty or N bytes). **[DT]**

| Property | Nodes | Shapes | Examples |
|---|---|---|---|
| `#address-cells` | 49 | u32×49 | [`/`](../devicetree/root.md) = `0x2`<br>[`/chosen`](../devicetree/root__chosen.md) = `0x2`<br>[`/cpus`](../devicetree/root__cpus.md) = `0x1`<br>[`/arm-io`](../devicetree/root__arm-io.md) = `0x2`<br>[`/arm-io/aic`](../devicetree/root__arm-io__aic.md) = `0x0` |
| `#address-cels` | 3 | u32×3 | [`/arm-io/i2c2`](../devicetree/root__arm-io__i2c2.md) = `0x1`<br>[`/arm-io/i2c3`](../devicetree/root__arm-io__i2c3.md) = `0x1`<br>[`/arm-io/i2c4`](../devicetree/root__arm-io__i2c4.md) = `0x1` |
| `#dma-channels-rx` | 7 | u64×6, 32 B | [`/arm-io/admac-dispint0-ced-ssw`](../devicetree/root__arm-io__admac-dispint0-ced-ssw.md) = `0x0`<br>[`/arm-io/admac-dispext0-ced-ssw`](../devicetree/root__arm-io__admac-dispext0-ced-ssw.md) = `0x0`<br>[`/arm-io/admac-aop-ced-ssw`](../devicetree/root__arm-io__admac-aop-ced-ssw.md) = `0e000000000000000d00000000000000…`<br>[`/arm-io/admac-base-ns`](../devicetree/root__arm-io__admac-base-ns.md) = `0xd`<br>[`/arm-io/admac-leap-ns`](../devicetree/root__arm-io__admac-leap-ns.md) = `0x9` |
| `#dma-channels-tx` | 9 | u64×8, 32 B | [`/arm-io/admac-dispint0`](../devicetree/root__arm-io__admac-dispint0.md) = `0x1`<br>[`/arm-io/admac-dispint0-ced-ssw`](../devicetree/root__arm-io__admac-dispint0-ced-ssw.md) = `0x1`<br>[`/arm-io/admac-dispext0`](../devicetree/root__arm-io__admac-dispext0.md) = `0x1`<br>[`/arm-io/admac-dispext0-ced-ssw`](../devicetree/root__arm-io__admac-dispext0-ced-ssw.md) = `0x1`<br>[`/arm-io/admac-aop-ced-ssw`](../devicetree/root__arm-io__admac-aop-ced-ssw.md) = `05000000000000000d00000000000000…` |
| `#dma-controllers` | 3 | u32×3 | [`/arm-io/admac-dispint0-ced-ssw`](../devicetree/root__arm-io__admac-dispint0-ced-ssw.md) = `0x1`<br>[`/arm-io/admac-dispext0-ced-ssw`](../devicetree/root__arm-io__admac-dispext0-ced-ssw.md) = `0x1`<br>[`/arm-io/admac-aop-ced-ssw`](../devicetree/root__arm-io__admac-aop-ced-ssw.md) = `0x4` |
| `#gpio-int-groups` | 6 | u32×6 | [`/arm-io/gpio0`](../devicetree/root__arm-io__gpio0.md) = `0x7`<br>[`/arm-io/aop-gpio`](../devicetree/root__arm-io__aop-gpio.md) = `0x7`<br>[`/arm-io/nub-gpio`](../devicetree/root__arm-io__nub-gpio.md) = `0x7`<br>[`/arm-io/smc-gpio`](../devicetree/root__arm-io__smc-gpio.md) = `0x7`<br>[`/arm-io/mtp-gpio`](../devicetree/root__arm-io__mtp-gpio.md) = `0x7` |
| `#gpio-pins` | 6 | u32×6 | [`/arm-io/gpio0`](../devicetree/root__arm-io__gpio0.md) = `0xd6`<br>[`/arm-io/aop-gpio`](../devicetree/root__arm-io__aop-gpio.md) = `0x5f`<br>[`/arm-io/nub-gpio`](../devicetree/root__arm-io__nub-gpio.md) = `0x20`<br>[`/arm-io/smc-gpio`](../devicetree/root__arm-io__smc-gpio.md) = `0x6`<br>[`/arm-io/mtp-gpio`](../devicetree/root__arm-io__mtp-gpio.md) = `0x12` |
| `#interrupt-cells` | 14 | u32×14 | [`/arm-io/aic`](../devicetree/root__arm-io__aic.md) = `0x1`<br>[`/arm-io/gpio0`](../devicetree/root__arm-io__gpio0.md) = `0x2`<br>[`/arm-io/aop-gpio`](../devicetree/root__arm-io__aop-gpio.md) = `0x2`<br>[`/arm-io/nub-gpio`](../devicetree/root__arm-io__nub-gpio.md) = `0x2`<br>[`/arm-io/smc-gpio`](../devicetree/root__arm-io__smc-gpio.md) = `0x2` |
| `#main-cpus` | 1 | u32 | [`/arm-io/aic`](../devicetree/root__arm-io__aic.md) = `0x6` |
| `#msi-vectors` | 3 | u32×3 | [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) = `0x40`<br>[`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) = `0x20`<br>[`/arm-io/apcie/pci-bridge1`](../devicetree/root__arm-io__apcie__pci-bridge1.md) = `0x20` |
| `#num-spmi-interrupts` | 5 | u32×5 | [`/arm-io/aop-spmi0/baseband-heb`](../devicetree/root__arm-io__aop-spmi0__baseband-heb.md) = `0x7`<br>[`/arm-io/aop-spmi0/stockholm-spmi`](../devicetree/root__arm-io__aop-spmi0__stockholm-spmi.md) = `0x7`<br>[`/arm-io/aop-spmi0/hammerfest-spmi`](../devicetree/root__arm-io__aop-spmi0__hammerfest-spmi.md) = `0x7`<br>[`/arm-io/aop-spmi1/wlan-idc`](../devicetree/root__arm-io__aop-spmi1__wlan-idc.md) = `0x4`<br>[`/arm-io/aop-spmi1/baseband-idc`](../devicetree/root__arm-io__aop-spmi1__baseband-idc.md) = `0xd` |
| `#ports` | 1 | u32 | [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) = `0x2` |
| `#shared-timestamps` | 1 | u32 | [`/arm-io/aic`](../devicetree/root__arm-io__aic.md) = `0x10` |
| `#size-cells` | 37 | u32×37 | [`/`](../devicetree/root.md) = `0x2`<br>[`/cpus`](../devicetree/root__cpus.md) = `0x0`<br>[`/arm-io`](../devicetree/root__arm-io.md) = `0x2`<br>[`/arm-io/error-handler/amcc-error-handler`](../devicetree/root__arm-io__error-handler__amcc-error-handler.md) = `0x2`<br>[`/arm-io/error-handler/dcs-error-handler`](../devicetree/root__arm-io__error-handler__dcs-error-handler.md) = `0x2` |
| `#ssw-register-count` | 3 | u32×3 | [`/arm-io/admac-dispint0-ced-ssw`](../devicetree/root__arm-io__admac-dispint0-ced-ssw.md) = `0x4`<br>[`/arm-io/admac-dispext0-ced-ssw`](../devicetree/root__arm-io__admac-dispext0-ced-ssw.md) = `0x4`<br>[`/arm-io/admac-aop-ced-ssw`](../devicetree/root__arm-io__admac-aop-ced-ssw.md) = `0x87` |
| `3d-imagery` | 1 | u32 | [`/product/maps`](../devicetree/root__product__maps.md) = `0x0` |
| `3d-maps` | 1 | u32 | [`/product/maps`](../devicetree/root__product__maps.md) = `0x0` |
| `aab-cap-e` | 3 | 16 B×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `000000000000f04100007a4400409c45`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `000000000000f04100007a4400409c45`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `000000000000f04100007a4400409c45` |
| `aab-cap-l` | 3 | 16 B×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `000048420000964300800944000080bf`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `000048420000964300800944000080bf`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `000048420000964300800944000080bf` |
| `aab-constraint-e2` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x258`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x258`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x258` |
| `aab-constraint-emax` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x1388`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x1388`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x1388` |
| `aab-constraint-l0b` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x87`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x87`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x87` |
| `aab-constraint-l2` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0xdc`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0xdc`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0xdc` |
| `aab-constraint-lmax` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x424`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x424`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x424` |
| `AAPL,phandle` | 552 | u32×552 | [`/`](../devicetree/root.md) = `0x1`<br>[`/machine-timeouts`](../devicetree/root__machine-timeouts.md) = `0x2`<br>[`/chosen`](../devicetree/root__chosen.md) = `0x3`<br>[`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `0x4`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `0x5` |
| `AAPL,unit-string` | 6 | string×6 | [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) = `00000000`<br>[`/arm-io/apcie/pci-bridge0/centauri-control`](../devicetree/root__arm-io__apcie__pci-bridge0__centauri-control.md) = `00000000`<br>[`/arm-io/apcie/pci-bridge0/centauri-alpha`](../devicetree/root__arm-io__apcie__pci-bridge0__centauri-alpha.md) = `00000001`<br>[`/arm-io/apcie/pci-bridge0/centauri-beta`](../devicetree/root__arm-io__apcie__pci-bridge0__centauri-beta.md) = `00000002`<br>[`/arm-io/apcie/pci-bridge1`](../devicetree/root__arm-io__apcie__pci-bridge1.md) = `00010000` |
| `aarch64` | 1 | empty | [`/arm-io/sep`](../devicetree/root__arm-io__sep.md) = `` |
| `acc-clusters` | 1 | 56 B | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `02000000000000000000000045414343…` |
| `acc-harvesting` | 1 | u32 | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0x0` |
| `acc-impl` | 1 | 32 B | [`/arm-io`](../devicetree/root__arm-io.md) = `0000f010020000000020000000000000…` |
| `acc-impl-reg` | 6 | 16 B×6 | [`/cpus/cpu0`](../devicetree/root__cpus__cpu0.md) = `0000f010020000008800040000000000`<br>[`/cpus/cpu1`](../devicetree/root__cpus__cpu1.md) = `0000f010020000008800040000000000`<br>[`/cpus/cpu2`](../devicetree/root__cpus__cpu2.md) = `0000f010020000008800040000000000`<br>[`/cpus/cpu3`](../devicetree/root__cpus__cpu3.md) = `0000f010020000008800040000000000`<br>[`/cpus/cpu4`](../devicetree/root__cpus__cpu4.md) = `0000f011020000008800040000000000` |
| `acc-slew-rate-chip-partition` | 1 | 40 B | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `00000000454143430000000000000000…` |
| `acc-slew-rate-monitor` | 1 | u32 | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0x11` |
| `accel-interrupt-calibration` | 2 | string×2 | [`/arm-io/aop/iop-aop-nub/accel_1`](../devicetree/root__arm-io__aop__iop-aop-nub__accel_1.md) = `syscfg/A2CL`<br>[`/arm-io/aop/iop-aop-nub/accel`](../devicetree/root__arm-io__aop__iop-aop-nub__accel.md) = `syscfg/AICl` |
| `accel-nominal-extr-cal` | 4 | string×4 | [`/arm-io/aop/iop-aop-nub/accel_1`](../devicetree/root__arm-io__aop__iop-aop-nub__accel_1.md) = `syscfg/ARXN,hex/02000201464D30692800000001000000000000000000`<br>[`/arm-io/aop/iop-aop-nub/hgaccel_1`](../devicetree/root__arm-io__aop__iop-aop-nub__hgaccel_1.md) = `syscfg/AhXN,hex/02000201464D30692800000001000000000000000000`<br>[`/arm-io/aop/iop-aop-nub/accel`](../devicetree/root__arm-io__aop__iop-aop-nub__accel.md) = `syscfg/ARXN,hex/02000201464D30692800000001000000000000000000`<br>[`/arm-io/aop/iop-aop-nub/hgaccel`](../devicetree/root__arm-io__aop__iop-aop-nub__hgaccel.md) = `syscfg/AhXN,hex/02000201464D30692800000001000000000000000000` |
| `accel-offset-cal` | 2 | string×2 | [`/arm-io/aop/iop-aop-nub/accel_1`](../devicetree/root__arm-io__aop__iop-aop-nub__accel_1.md) = `syscfg/A2oC`<br>[`/arm-io/aop/iop-aop-nub/accel`](../devicetree/root__arm-io__aop__iop-aop-nub__accel.md) = `syscfg/AROC` |
| `accel-orientation` | 2 | string×2 | [`/arm-io/aop/iop-aop-nub/accel_1`](../devicetree/root__arm-io__aop__iop-aop-nub__accel_1.md) = `syscfg/ARot`<br>[`/arm-io/aop/iop-aop-nub/accel`](../devicetree/root__arm-io__aop__iop-aop-nub__accel.md) = `syscfg/ARot` |
| `accel-range-extr-cal` | 2 | string×2 | [`/arm-io/aop/iop-aop-nub/accel_1`](../devicetree/root__arm-io__aop__iop-aop-nub__accel_1.md) = `syscfg/A2XC`<br>[`/arm-io/aop/iop-aop-nub/accel`](../devicetree/root__arm-io__aop__iop-aop-nub__accel.md) = `syscfg/ARXC` |
| `accel-range-intr-cal` | 4 | string×2, 60 B×2 | [`/arm-io/aop/iop-aop-nub/accel_1`](../devicetree/root__arm-io__aop__iop-aop-nub__accel_1.md) = `syscfg/A2NC,hex/03000101464D30692C00000002000000200000000000`<br>[`/arm-io/aop/iop-aop-nub/hgaccel_1`](../devicetree/root__arm-io__aop__iop-aop-nub__hgaccel_1.md) = `02000101000000002c00000001000000…`<br>[`/arm-io/aop/iop-aop-nub/accel`](../devicetree/root__arm-io__aop__iop-aop-nub__accel.md) = `syscfg/ARNC,hex/03000101524D30692C00000002000000200000000000`<br>[`/arm-io/aop/iop-aop-nub/hgaccel`](../devicetree/root__arm-io__aop__iop-aop-nub__hgaccel.md) = `02000101000000002c00000001000000…` |
| `accel-range-sensitivity-cal` | 2 | string×2 | [`/arm-io/aop/iop-aop-nub/accel_1`](../devicetree/root__arm-io__aop__iop-aop-nub__accel_1.md) = `syscfg/ARSC`<br>[`/arm-io/aop/iop-aop-nub/accel`](../devicetree/root__arm-io__aop__iop-aop-nub__accel.md) = `syscfg/ARSC` |
| `accel-sensitivity-calibration` | 2 | string×2 | [`/arm-io/aop/iop-aop-nub/accel_1`](../devicetree/root__arm-io__aop__iop-aop-nub__accel_1.md) = `syscfg/ASCl`<br>[`/arm-io/aop/iop-aop-nub/accel`](../devicetree/root__arm-io__aop__iop-aop-nub__accel.md) = `syscfg/ASCl` |
| `acoustic-id` | 1 | u32 | [`/product/audio`](../devicetree/root__product__audio.md) = `0x1f5d` |
| `acsk-subtarget` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x6` |
| `activation-protocol-version` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x2` |
| `actuator-cpms-bgd_100ms` | 1 | u64 | [`/product/audio`](../devicetree/root__product__audio.md) = `0xeef000001f4` |
| `actuator-cpms-bgd_inst` | 1 | u64 | [`/product/audio`](../devicetree/root__product__audio.md) = `0x1db0000006d6` |
| `adaptive-ui` | 1 | empty | [`/product/maps`](../devicetree/root__product__maps.md) = `` |
| `adc-gains` | 1 | 12 B | [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) = `060606068383068686860000` |
| `address-width` | 1 | u32 | [`/arm-io/aes`](../devicetree/root__arm-io__aes.md) = `0x2a` |
| `admac-evolution` | 4 | u32×4 | [`/arm-io/admac-base-ns`](../devicetree/root__arm-io__admac-base-ns.md) = `0x1`<br>[`/arm-io/admac-leap-ns`](../devicetree/root__arm-io__admac-leap-ns.md) = `0x1`<br>[`/arm-io/admac-base-s`](../devicetree/root__arm-io__admac-base-s.md) = `0x1`<br>[`/arm-io/admac-leap-s`](../devicetree/root__arm-io__admac-leap-s.md) = `0x1` |
| `ads-present` | 1 | u32 | [`/arm-io/avd`](../devicetree/root__arm-io__avd.md) = `0x1` |
| `aes-service-publish-timeout` | 1 | u32 | [`/defaults`](../devicetree/root__defaults.md) = `0x78` |
| `aes-version` | 1 | u32 | [`/arm-io/aes`](../devicetree/root__arm-io__aes.md) = `0x6` |
| `afi-ns-names` | 1 | u64 | [`/arm-io/error-handler/nsi-error-handler`](../devicetree/root__arm-io__error-handler__nsi-error-handler.md) = `0x4e5331204e533020` |
| `afi-top-bw-enable` | 1 | u32 | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0x0` |
| `afi-top-bw-threshold` | 1 | 64 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `c2f53000000000000000000000000000…` |
| `aft-control-list` | 1 | u64 | [`/arm-io/cpu-debug-interface`](../devicetree/root__arm-io__cpu-debug-interface.md) = `0x25d010000` |
| `aft-instance-list` | 1 | 72 B | [`/arm-io/cpu-debug-interface`](../devicetree/root__arm-io__cpu-debug-interface.md) = `0000005d020000004146490000000000…` |
| `aft-params` | 1 | 208 B | [`/arm-io/cpu-debug-interface`](../devicetree/root__arm-io__cpu-debug-interface.md) = `60087080020000001000015d02000000…` |
| `aggregate-cam-photo-zoom` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x7d0` |
| `aggregate-cam-video-zoom` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x4b0` |
| `aggregate-camera` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x1` |
| `agm-primary` | 1 | string | [`/arm-io/mtp/iop-mtp-nub`](../devicetree/root__arm-io__mtp__iop-mtp-nub.md) = `AppleHIDTransportDeviceMailbox` |
| `agm-secondary` | 1 | string | [`/arm-io/mtp/iop-mtp-nub`](../devicetree/root__arm-io__mtp__iop-mtp-nub.md) = `AppleHIDTransportDeviceMailbox` |
| `agx-address-space-mgmt-mode` | 1 | u32 | [`/arm-io/sgx`](../devicetree/root__arm-io__sgx.md) = `0x1` |
| `agx-af-rd-bw-constraint` | 1 | 192 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `00000000000000000300000000000000…` |
| `agx-af-rd-bw-dvfs-filter` | 1 | u32 | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0xffffffff` |
| `agx-af-rd-bw-enable` | 1 | u32 | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0x1` |
| `agx-af-rd-bw-threshold` | 1 | 1024 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `00000000000000000000000000000000…` |
| `agx-af-wr-bw-constraint` | 1 | 192 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `00000000000000000300000000000000…` |
| `agx-af-wr-bw-dvfs-filter` | 1 | u32 | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0xffffffff` |
| `agx-af-wr-bw-enable` | 1 | u32 | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0x1` |
| `agx-af-wr-bw-threshold` | 1 | 1024 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `00000000000000000000000000000000…` |
| `agx-dcs-bw-constraint-a` | 1 | 192 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `00000000000000000800000000000000…` |
| `agx-dcs-bw-constraint-b` | 1 | 192 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `00000000000000000700000000000000…` |
| `agx-dcs-bw-constraint-c` | 1 | 192 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `00000000000000000800000000000000…` |
| `agx-dcs-bw-dvfs-filter` | 1 | u32 | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0xffffffff` |
| `agx-dcs-bw-enable` | 1 | u32 | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0x1` |
| `agx-dcs-bw-threshold-a` | 1 | 2304 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `00000000000000000000000000000000…` |
| `agx-dcs-bw-threshold-b` | 1 | 2048 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `00000000000000000000000000000000…` |
| `agx-dcs-bw-threshold-c` | 1 | 2304 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `00000000000000000000000000000000…` |
| `aicglbcfg-offset` | 1 | u32 | [`/arm-io/aic`](../devicetree/root__arm-io__aic.md) = `0x14` |
| `alisha` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `allow-32bit-apps` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `allow-ap-nonce-retrieval` | 1 | empty | [`/chosen`](../devicetree/root__chosen.md) = `` |
| `allow-apf-sid-remap` | 1 | empty | [`/arm-io/dart-isp`](../devicetree/root__arm-io__dart-isp.md) = `` |
| `allow-subpage-mapping` | 7 | empty×7 | [`/arm-io/dart-sio/mapper-sio`](../devicetree/root__arm-io__dart-sio__mapper-sio.md) = ``<br>[`/arm-io/dart-sio/mapper-aes`](../devicetree/root__arm-io__dart-sio__mapper-aes.md) = ``<br>[`/arm-io/dart-sbr/mapper-admac-leap-ns`](../devicetree/root__arm-io__dart-sbr__mapper-admac-leap-ns.md) = ``<br>[`/arm-io/dart-sbr/mapper-admac-base-ns`](../devicetree/root__arm-io__dart-sbr__mapper-admac-base-ns.md) = ``<br>[`/arm-io/dart-usb0/mapper-usb`](../devicetree/root__arm-io__dart-usb0__mapper-usb.md) = `` |
| `allow-vm-reserve-mapping` | 1 | empty | [`/arm-io/dart-sep`](../devicetree/root__arm-io__dart-sep.md) = `` |
| `als-new-calibration-path` | 1 | u32 | [`/exbright`](../devicetree/root__exbright.md) = `0x1` |
| `als-types` | 1 | 12 B | [`/exbright`](../devicetree/root__exbright.md) = `090000000900000009000000` |
| `always-on` | 1 | empty | [`/arm-io/dart-sbr`](../devicetree/root__arm-io__dart-sbr.md) = `` |
| `always-on-time` | 2 | u32×2 | [`/arm-io/disp0`](../devicetree/root__arm-io__disp0.md) = `0x1`<br>[`/arm-io/dispsec`](../devicetree/root__arm-io__dispsec.md) = `0x1` |
| `amcc-count` | 1 | u32 | [`/arm-io/mcc`](../devicetree/root__arm-io__mcc.md) = `0x1` |
| `amcc-plane-enable-mask` | 1 | u32 | [`/arm-io/mcc`](../devicetree/root__arm-io__mcc.md) = `0x7` |
| `amcc-reg-idx` | 1 | u32 | [`/arm-io/mcc`](../devicetree/root__arm-io__mcc.md) = `0x1` |
| `amfi-allows-trust-cache-load` | 1 | u32 | [`/chosen`](../devicetree/root__chosen.md) = `0x0` |
| `amfi-only-platform-code` | 1 | u32 | [`/chosen`](../devicetree/root__chosen.md) = `0x0` |
| `aml-lux-activation-threshold` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x459c4000`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x459c4000`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x43960000` |
| `aml-lux-table` | 3 | 48 B×2, 72 B | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `00409c4500401c4600606a460050c346…`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `00409c4500401c4600606a460050c346…`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0000c842000096430000164400004844…` |
| `aml-nits-activation-threshold` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x42c80000`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x42c80000`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x42c80000` |
| `aml-nits-table` | 3 | 60 B×2, 44 B | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0000c842000096430000fa4300002f44…`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0000c842000096430000fa4300002f44…`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0000c842000096430000fa4300002f44…` |
| `aml-ramp-aod-duration` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x40000000`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x40000000`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x40000000` |
| `aml-ramp-bezier-anchors` | 3 | 12 B×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `9a99993e6666663f9a99593f`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `9a99993e6666663f9a99593f`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `9a99993e6666663f9a99593f` |
| `aml-ramp-down-duration` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x40a00000`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x40a00000`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x40a00000` |
| `aml-ramp-down-lux-threshold` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x457a0000`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x457a0000`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x43160000` |
| `aml-ramp-up-duration` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x40a00000`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x40a00000`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x40a00000` |
| `aml-ramp-up-lux-threshold` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x457a0000`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x457a0000`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x43160000` |
| `aml-ramp-update-rate` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x42700000`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x42700000`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x42700000` |
| `aml-strength-table` | 3 | 720 B, 528 B, 1080 B | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `00000000000000000000000000000000…`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `00000000000000000000000000000000…`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `00000000000000000000000000000000…` |
| `aml-supported` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x1`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x1`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x1` |
| `ane-dcs-bw-constraint-a` | 1 | 192 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `00000000000000000300000000000000…` |
| `ane-dcs-bw-constraint-b` | 1 | 192 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `00000000000000000300000000000000…` |
| `ane-dcs-bw-constraint-c` | 1 | 192 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `00000000000000000300000000000000…` |
| `ane-dcs-bw-dvfs-filter` | 1 | u32 | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0xffffffff` |
| `ane-dcs-bw-enable` | 1 | u32 | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0x1` |
| `ane-dcs-bw-threshold-a` | 1 | 2304 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `00000c00010000000000000000000000…` |
| `ane-dcs-bw-threshold-b` | 1 | 2048 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `00000c00010000000000000000000000…` |
| `ane-dcs-bw-threshold-c` | 1 | 2304 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `00000600010000000000000000000000…` |
| `ane-dpe` | 1 | u32 | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0x0` |
| `ane-id` | 2 | u32×2 | [`/arm-io/ane0`](../devicetree/root__arm-io__ane0.md) = `0x0`<br>[`/arm-io/ane1`](../devicetree/root__arm-io__ane1.md) = `0x1` |
| `ane-subtype` | 2 | u32×2 | [`/arm-io/ane0`](../devicetree/root__arm-io__ane0.md) = `0x0`<br>[`/arm-io/ane1`](../devicetree/root__arm-io__ane1.md) = `0x1` |
| `ane-type` | 2 | u32×2 | [`/arm-io/ane0`](../devicetree/root__arm-io__ane0.md) = `0x400`<br>[`/arm-io/ane1`](../devicetree/root__arm-io__ane1.md) = `0x400` |
| `ane-utility-max-freq` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x57c` |
| `ane-utilization-ki-down` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x8000` |
| `ane-utilization-ki-up` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x25999` |
| `ane-utilization-kp-down` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x0` |
| `ane-utilization-kp-up` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x0` |
| `ane-utilization-target` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0xcccc` |
| `ane0-af-bw-constraint` | 1 | 192 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `00000000000000000100000000000000…` |
| `ane0-af-bw-dvfs-filter` | 1 | u32 | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0xffffff00` |
| `ane0-af-bw-enable` | 1 | u32 | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0x1` |
| `ane0-af-bw-threshold` | 1 | 1024 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `00001800000000000000000000000000…` |
| `ane0-dcs-bw-constraint-a` | 1 | 192 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `00000000000000000300000000000000…` |
| `ane0-dcs-bw-constraint-b` | 1 | 192 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `00000000000000000300000000000000…` |
| `ane0-dcs-bw-constraint-c` | 1 | 192 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `00000000000000000300000000000000…` |
| `ane0-dcs-bw-dvfs-filter` | 1 | u32 | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0xffffffff` |
| `ane0-dcs-bw-enable` | 1 | u32 | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0x0` |
| `ane0-dcs-bw-threshold-a` | 1 | 2304 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `00000c00010000000000000000000000…` |
| `ane0-dcs-bw-threshold-b` | 1 | 2048 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `00000c00010000000000000000000000…` |
| `ane0-dcs-bw-threshold-c` | 1 | 2304 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `00000600010000000000000000000000…` |
| `ane0-link0-af-bw-constraint` | 1 | 192 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `00000000000000000100000000000000…` |
| `ane0-link0-af-bw-dvfs-filter` | 1 | u32 | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0xff` |
| `ane0-link0-af-bw-enable` | 1 | u32 | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0x1` |
| `ane0-link0-af-bw-threshold` | 1 | 1024 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `00001800000000000000000000000000…` |
| `ane0-link1-af-bw-constraint` | 1 | 192 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `00000000000000000100000000000000…` |
| `ane0-link1-af-bw-dvfs-filter` | 1 | u32 | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0xff` |
| `ane0-link1-af-bw-enable` | 1 | u32 | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0x1` |
| `ane0-link1-af-bw-threshold` | 1 | 1024 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `00001800000000000000000000000000…` |
| `ane1-af-bw-constraint` | 1 | 192 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `00000000000000000100000000000000…` |
| `ane1-af-bw-dvfs-filter` | 1 | u32 | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0xffffff00` |
| `ane1-af-bw-enable` | 1 | u32 | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0x1` |
| `ane1-af-bw-threshold` | 1 | 1024 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `00001800000000000000000000000000…` |
| `ane1-dcs-bw-constraint-a` | 1 | 192 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `00000000000000000300000000000000…` |
| `ane1-dcs-bw-constraint-b` | 1 | 192 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `00000000000000000300000000000000…` |
| `ane1-dcs-bw-constraint-c` | 1 | 192 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `00000000000000000300000000000000…` |
| `ane1-dcs-bw-dvfs-filter` | 1 | u32 | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0xffffffff` |
| `ane1-dcs-bw-enable` | 1 | u32 | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0x0` |
| `ane1-dcs-bw-threshold-a` | 1 | 2304 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `00000c00010000000000000000000000…` |
| `ane1-dcs-bw-threshold-b` | 1 | 2048 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `00000c00010000000000000000000000…` |
| `ane1-dcs-bw-threshold-c` | 1 | 2304 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `00000600010000000000000000000000…` |
| `ane1-link0-af-bw-constraint` | 1 | 192 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `00000000000000000100000000000000…` |
| `ane1-link0-af-bw-dvfs-filter` | 1 | u32 | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0xff` |
| `ane1-link0-af-bw-enable` | 1 | u32 | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0x1` |
| `ane1-link0-af-bw-threshold` | 1 | 1024 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `00001800000000000000000000000000…` |
| `ane1-link1-af-bw-constraint` | 1 | 192 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `00000000000000000100000000000000…` |
| `ane1-link1-af-bw-dvfs-filter` | 1 | u32 | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0xff` |
| `ane1-link1-af-bw-enable` | 1 | u32 | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0x1` |
| `ane1-link1-af-bw-threshold` | 1 | 1024 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `00001800000000000000000000000000…` |
| `angle-dependent` | 2 | u32×2 | [`/arm-io/aop/iop-aop-nub/als2a`](../devicetree/root__arm-io__aop__iop-aop-nub__als2a.md) = `0x1`<br>[`/arm-io/aop/iop-aop-nub/als2b`](../devicetree/root__arm-io__aop__iop-aop-nub__als2b.md) = `0x1` |
| `aod` | 1 | u32 | [`/arm-io/nub-spmi2/spmi-hpm0`](../devicetree/root__arm-io__nub-spmi2__spmi-hpm0.md) = `0x1b6` |
| `aod-high-luminance-supported` | 1 | u32 | [`/core-brightness`](../devicetree/root__core-brightness.md) = `0x1` |
| `aod-max-mem` | 1 | u32 | [`/defaults`](../devicetree/root__defaults.md) = `0x12c` |
| `aon-ptd-int-imm` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x52434430` |
| `aon-ptd-supported` | 1 | empty | [`/arm-io/pmgr/pmgrtools`](../devicetree/root__arm-io__pmgr__pmgrtools.md) = `` |
| `aop-fr-timebase` | 1 | u32 | [`/arm-io/aop/iop-aop-nub`](../devicetree/root__arm-io__aop__iop-aop-nub.md) = `0x1` |
| `aop-isp-v2protocol` | 1 | empty | [`/arm-io/aop/iop-aop-nub`](../devicetree/root__arm-io__aop__iop-aop-nub.md) = `` |
| `aop-target` | 1 | u32 | [`/arm-io/aop/iop-aop-nub`](../devicetree/root__arm-io__aop__iop-aop-nub.md) = `0x1` |
| `aop-timesync-reg-index` | 1 | u32 | [`/arm-io/aop`](../devicetree/root__arm-io__aop.md) = `0x5` |
| `aop_audio_ced_die0` | 2 | u32×2 | [`/ced-ssw/ced_tunable_mask`](../devicetree/root__ced-ssw__ced_tunable_mask.md) = `0x4`<br>[`/ced-ssw/ced_disable_mask`](../devicetree/root__ced-ssw__ced_disable_mask.md) = `0x2` |
| `aop_audio_ced_die1` | 2 | u32×2 | [`/ced-ssw/ced_tunable_mask`](../devicetree/root__ced-ssw__ced_tunable_mask.md) = `0x20`<br>[`/ced-ssw/ced_disable_mask`](../devicetree/root__ced-ssw__ced_disable_mask.md) = `0x10` |
| `aot-linger-time-ms` | 1 | u32 | [`/product/iopm`](../devicetree/root__product__iopm.md) = `0x0` |
| `aot-mode` | 1 | u32 | [`/product/iopm`](../devicetree/root__product__iopm.md) = `0xd` |
| `aot-power` | 3 | u32×2, u64 | [`/arm-io/smc`](../devicetree/root__arm-io__smc.md) = `0x1`<br>[`/arm-io/ane0`](../devicetree/root__arm-io__ane0.md) = `0x1`<br>[`/buttons`](../devicetree/root__buttons.md) = `0x100000001` |
| `ap-controls-metadata` | 1 | 12 B | [`/arm-io/soc-misc`](../devicetree/root__arm-io__soc-misc.md) = `746370610000000001000000` |
| `ap-recoverable-panics` | 3 | empty×3 | [`/arm-io/ispRtb/iop-isp-nub`](../devicetree/root__arm-io__ispRtb__iop-isp-nub.md) = ``<br>[`/arm-io/ane0/iop-ane0-nub`](../devicetree/root__arm-io__ane0__iop-ane0-nub.md) = ``<br>[`/arm-io/ane1/iop-ane1-nub`](../devicetree/root__arm-io__ane1__iop-ane1-nub.md) = `` |
| `ap-time-mark-with-boot-arg` | 1 | empty | [`/arm-io/aop/iop-aop-nub/gnss`](../devicetree/root__arm-io__aop__iop-aop-nub__gnss.md) = `` |
| `ap-voter-agent-idx` | 1 | u32 | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0x3` |
| `ap-wake-sources` | 1 | 600 B | [`/arm-io/soc-misc`](../devicetree/root__arm-io__soc-misc.md) = `00000000010000004149432e57616b65…` |
| `apcie-path` | 2 | string×2 | [`/arm-io/apcie0-plce`](../devicetree/root__arm-io__apcie0-plce.md) = `/arm-io/apcie`<br>[`/arm-io/apcie1-plce`](../devicetree/root__arm-io__apcie1-plce.md) = `/arm-io/apcie` |
| `apcie-piodma` | 2 | u32×2 | [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) = `0x1ab`<br>[`/arm-io/apcie/pci-bridge1`](../devicetree/root__arm-io__apcie__pci-bridge1.md) = `0x1b1` |
| `apcie-piodma-sid` | 2 | u32×2 | [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) = `0x11`<br>[`/arm-io/apcie/pci-bridge1`](../devicetree/root__arm-io__apcie__pci-bridge1.md) = `0x11` |
| `apcie-plce` | 2 | u32×2 | [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) = `0x1ac`<br>[`/arm-io/apcie/pci-bridge1`](../devicetree/root__arm-io__apcie__pci-bridge1.md) = `0x1b2` |
| `apcie-plce-sid` | 2 | u32×2 | [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) = `0x13`<br>[`/arm-io/apcie/pci-bridge1`](../devicetree/root__arm-io__apcie__pci-bridge1.md) = `0x13` |
| `apcie-port` | 2 | u32×2 | [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) = `0x0`<br>[`/arm-io/apcie/pci-bridge1`](../devicetree/root__arm-io__apcie__pci-bridge1.md) = `0x1` |
| `apf` | 1 | 192 B | [`/arm-io/sapt`](../devicetree/root__arm-io__sapt.md) = `1101000000400c2002000000ffbf0d20…` |
| `app-macho-architecture` | 1 | string | [`/product`](../devicetree/root__product.md) = `arm64e.x1` |
| `arbuffer-addr-rx` | 1 | u32 | [`/arm-io/aop-spmi1/baseband-idc`](../devicetree/root__arm-io__aop-spmi1__baseband-idc.md) = `0x80` |
| `arch-type` | 1 | string | [`/fillmore`](../devicetree/root__fillmore.md) = `bt1` |
| `artwork-device-idiom` | 1 | string | [`/product`](../devicetree/root__product.md) = `phone` |
| `artwork-device-subtype` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x7f2` |
| `artwork-display-gamut` | 1 | string | [`/product`](../devicetree/root__product.md) = `P3` |
| `artwork-dynamic-displaymode` | 1 | string | [`/product`](../devicetree/root__product.md) = `0` |
| `artwork-scale-factor` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x3` |
| `ASP1` | 1 | u64 | [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) = `0x600303034818` |
| `ASP2` | 1 | u64 | [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) = `0x10300004818` |
| `ASP3` | 1 | u64 | [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) = `0x707074810` |
| `ASP4` | 1 | u64 | [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) = `0x4818` |
| `assistant` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `atc-phy` | 1 | u32 | [`/arm-io/atc0-dpphy`](../devicetree/root__arm-io__atc0-dpphy.md) = `0xde` |
| `atc-phy-parent` | 1 | u32 | [`/arm-io/usb-drd0`](../devicetree/root__arm-io__usb-drd0.md) = `0xde` |
| `audio` | 1 | u32 | [`/arm-io/dcpext0`](../devicetree/root__arm-io__dcpext0.md) = `0x121` |
| `audio-driver` | 1 | string | [`/arm-io/smc/iop-smc-nub/smc-ext-charger`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-ext-charger.md) = `AppleCS42L79Audio` |
| `audio-enable-warmup-ms` | 1 | u32 | [`/arm-io/iop-audio-controller/audio-haptic`](../devicetree/root__arm-io__iop-audio-controller__audio-haptic.md) = `0x3` |
| `audio-stream-formatter` | 4 | u32×4 | [`/arm-io/iop-audio-controller/audio-leap-internal-loopback/audio-leap-internal-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-leap-internal-loopback__audio-leap-internal-loopback.md) = `0x6c656170`<br>[`/arm-io/iop-audio-controller/audio-s-leap-internal-loopback/audio-s-leap-internal-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-s-leap-internal-loopback__audio-s-leap-internal-loopback.md) = `0x6c656170`<br>[`/arm-io/iop-audio-controller/audio-haptic-transport/audio-haptic`](../devicetree/root__arm-io__iop-audio-controller__audio-haptic-transport__audio-haptic.md) = `0x6c656170`<br>[`/arm-io/iop-audio-controller/audio-hpdbg-transport/audio-hpdbg`](../devicetree/root__arm-io__iop-audio-controller__audio-hpdbg-transport__audio-hpdbg.md) = `0x6c656170` |
| `aurora-cltm-enter-multiplier` | 1 | u32 | [`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x3fa66666` |
| `aurora-cltm-threshold` | 1 | u32 | [`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x431b0000` |
| `aurora-enter-lux` | 1 | 12 B | [`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `00c8b04500c8b04500c8b045` |
| `aurora-exit-lux` | 1 | 12 B | [`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0088a0450088a0450088a045` |
| `aurora-ramp-down-tap-points` | 3 | u64×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x3ecccccd3e4ccccd`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x3ecccccd3e4ccccd`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x3ecccccd3e4ccccd` |
| `aurora-ramp-up-speed` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x40000000`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x40000000`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x40000000` |
| `aurora-ramp-up-tap-points` | 3 | u64×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x3eb333333e3851ec`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x3eb333333e3851ec`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x3eb333333e3851ec` |
| `aurora-saturation-lux` | 3 | 12 B×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0080bb460080bb460080bb46`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0080bb460080bb460080bb46`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `00ce824600ce824600ce8246` |
| `aurora-session-limit` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x43960000`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x43960000`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x43960000` |
| `aurora-supported` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x1`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x1`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x1` |
| `aurora-upo-enter-multiplier` | 1 | u32 | [`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x3fa95810` |
| `aurora-upo-threshold` | 1 | u32 | [`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x44960000` |
| `auth-required` | 2 | empty×2 | [`/arm-io/mtp/iop-mtp-nub/multi-touch2`](../devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch2.md) = ``<br>[`/arm-io/mtp/iop-mtp-nub/multi-touch`](../devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch.md) = `` |
| `auth-source-index` | 2 | u32×2 | [`/arm-io/mtp/iop-mtp-nub/multi-touch2`](../devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch2.md) = `0x2`<br>[`/arm-io/mtp/iop-mtp-nub/multi-touch`](../devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch.md) = `0x1` |
| `auth-supported` | 1 | empty | [`/arm-io/mtp/iop-mtp-nub`](../devicetree/root__arm-io__mtp__iop-mtp-nub.md) = `` |
| `auto-focus` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x1` |
| `auto-low-light-video` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x1` |
| `auto-rate-change` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x1` |
| `automatic-rail-gating-enabled` | 3 | u32×3 | [`/arm-io/dcp/iop-dcp-nub`](../devicetree/root__arm-io__dcp__iop-dcp-nub.md) = `0x1`<br>[`/arm-io/dcpsec/iop-dcpsec-nub`](../devicetree/root__arm-io__dcpsec__iop-dcpsec-nub.md) = `0x1`<br>[`/arm-io/dcpext0/iop-dcpext0-nub`](../devicetree/root__arm-io__dcpext0__iop-dcpext0-nub.md) = `0x1` |
| `avd-ads-keytype-version` | 1 | u32 | [`/arm-io/avd`](../devicetree/root__arm-io__avd.md) = `0x3` |
| `avd-version` | 1 | u32 | [`/arm-io/avd`](../devicetree/root__arm-io__avd.md) = `0x4` |
| `awl-scratch-supported` | 1 | u32 | [`/arm-io/wdt`](../devicetree/root__arm-io__wdt.md) = `0x1` |
| `back-camera-autofocus-recal` | 2 | string×2 | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) = `syscfg/BCAR`<br>[`/arm-io/isp`](../devicetree/root__arm-io__isp.md) = `syscfg/BCAR` |
| `backing-color` | 1 | string | [`/chosen`](../devicetree/root__chosen.md) = `syscfg/CLBG` |
| `backing-glass-material` | 1 | string | [`/chosen`](../devicetree/root__chosen.md) = `syscfg/BGMt` |
| `backlight-detection` | 1 | u32 | [`/arm-io/smc/iop-smc-nub/smc-ext-charger`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-ext-charger.md) = `0x0` |
| `baseband-chipset` | 1 | string | [`/product`](../devicetree/root__product.md) = `int2` |
| `baseband-heb` | 1 | u32 | [`/baseband`](../devicetree/root__baseband.md) = `0xd1` |
| `baseband-idc` | 1 | u32 | [`/baseband`](../devicetree/root__baseband.md) = `0xda` |
| `battery-data-clients` | 1 | u32 | [`/arm-io/nub-spmi0/btm`](../devicetree/root__arm-io__nub-spmi0__btm.md) = `0x1` |
| `battery-data-collection` | 1 | u32 | [`/arm-io/nub-spmi0/btm`](../devicetree/root__arm-io__nub-spmi0__btm.md) = `0x1` |
| `battery-data-input-source` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x0` |
| `battery-id` | 1 | 32 B | [`/arm-io/smc/iop-smc-nub/smc-charger`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-charger.md) = `00000000000000000000000000000000…` |
| `bdm-nits1` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x44548000`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x44548000`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x44548000` |
| `bdm-nits2` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x44c80000`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x44c80000`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x44c80000` |
| `bdm-supported` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x1`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x1`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x1` |
| `bics-hw-partition-size` | 1 | u32 | [`/defaults`](../devicetree/root__defaults.md) = `0x64` |
| `bics-sec-hw-partition-size` | 1 | u32 | [`/defaults`](../devicetree/root__defaults.md) = `0x64` |
| `billboard-addr-rx-antcluster` | 1 | u32 | [`/arm-io/aop-spmi1/wlan-idc`](../devicetree/root__arm-io__aop-spmi1__wlan-idc.md) = `0x80` |
| `billboard-addr-rx-e85mitigation` | 1 | u32 | [`/arm-io/aop-spmi1/baseband-idc`](../devicetree/root__arm-io__aop-spmi1__baseband-idc.md) = `0xa8` |
| `billboard-addr-rx-mpe-report` | 1 | u32 | [`/arm-io/aop-spmi1/baseband-idc`](../devicetree/root__arm-io__aop-spmi1__baseband-idc.md) = `0x60` |
| `billboard-addr-rx-regulatory` | 2 | u32×2 | [`/arm-io/aop-spmi1/wlan-idc`](../devicetree/root__arm-io__aop-spmi1__wlan-idc.md) = `0x60`<br>[`/arm-io/aop-spmi1/baseband-idc`](../devicetree/root__arm-io__aop-spmi1__baseband-idc.md) = `0x70` |
| `billboard-addr-rx-rev` | 2 | u32×2 | [`/arm-io/aop-spmi1/wlan-idc`](../devicetree/root__arm-io__aop-spmi1__wlan-idc.md) = `0x20`<br>[`/arm-io/aop-spmi1/baseband-idc`](../devicetree/root__arm-io__aop-spmi1__baseband-idc.md) = `0x20` |
| `billboard-addr-rx-sar-report` | 2 | u32×2 | [`/arm-io/aop-spmi1/wlan-idc`](../devicetree/root__arm-io__aop-spmi1__wlan-idc.md) = `0x48`<br>[`/arm-io/aop-spmi1/baseband-idc`](../devicetree/root__arm-io__aop-spmi1__baseband-idc.md) = `0x48` |
| `billboard-addr-rx-vswr-report` | 1 | u32 | [`/arm-io/aop-spmi1/baseband-idc`](../devicetree/root__arm-io__aop-spmi1__baseband-idc.md) = `0x9c` |
| `billboard-addr-tx-accessory` | 2 | u32×2 | [`/arm-io/aop-spmi1/wlan-idc`](../devicetree/root__arm-io__aop-spmi1__wlan-idc.md) = `0xa0`<br>[`/arm-io/aop-spmi1/baseband-idc`](../devicetree/root__arm-io__aop-spmi1__baseband-idc.md) = `0x40` |
| `billboard-addr-tx-config-vswr` | 1 | u32 | [`/arm-io/aop-spmi1/baseband-idc`](../devicetree/root__arm-io__aop-spmi1__baseband-idc.md) = `0x94` |
| `billboard-addr-tx-deviceupdate` | 1 | u32 | [`/arm-io/aop-spmi1/baseband-idc`](../devicetree/root__arm-io__aop-spmi1__baseband-idc.md) = `0xb0` |
| `billboard-addr-tx-e85mitigation` | 1 | u32 | [`/arm-io/aop-spmi1/baseband-idc`](../devicetree/root__arm-io__aop-spmi1__baseband-idc.md) = `0xa0` |
| `billboard-addr-tx-sar-budget` | 2 | u32×2 | [`/arm-io/aop-spmi1/wlan-idc`](../devicetree/root__arm-io__aop-spmi1__wlan-idc.md) = `0x28`<br>[`/arm-io/aop-spmi1/baseband-idc`](../devicetree/root__arm-io__aop-spmi1__baseband-idc.md) = `0x30` |
| `billboard-addr-tx-wait-time` | 1 | u32 | [`/arm-io/aop-spmi1/baseband-idc`](../devicetree/root__arm-io__aop-spmi1__baseband-idc.md) = `0x78` |
| `bitrate-2g` | 1 | u32 | [`/product/facetime`](../devicetree/root__product__facetime.md) = `0x64` |
| `bitrate-3g` | 1 | u32 | [`/product/facetime`](../devicetree/root__product__facetime.md) = `0xe4` |
| `bitrate-lte` | 1 | u32 | [`/product/facetime`](../devicetree/root__product__facetime.md) = `0xe4` |
| `bitrate-wifi` | 1 | u32 | [`/product/facetime`](../devicetree/root__product__facetime.md) = `0x7d0` |
| `blr-cct-warning` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0xa8c`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0xa8c`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0xa8c` |
| `bluetooth-le` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `bluetooth-lea2` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `bmu-board-id` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x8193` |
| `bmu-chip-id` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0xe505` |
| `bmu-num-enabled` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x2` |
| `bmu-num-supported` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x3` |
| `bmu2-board-id` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x8193` |
| `bmu2-chip-id` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0xe505` |
| `board-id` | 1 | u32 | [`/chosen`](../devicetree/root__chosen.md) = `0x0` |
| `boost-agent` | 1 | 336 B | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `000000010000000044495350494e545f…` |
| `boost-enabled` | 1 | u32 | [`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x1` |
| `boot-adapter-id` | 1 | u32 | [`/arm-io/smc/iop-smc-nub/smc-charger`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-charger.md) = `0x0` |
| `boot-console` | 1 | empty | [`/arm-io/uart0`](../devicetree/root__arm-io__uart0.md) = `` |
| `boot-manifest-hash` | 1 | 48 B | [`/chosen`](../devicetree/root__chosen.md) = `00000000000000000000000000000000…` |
| `boot-nonce` | 1 | u64 | [`/chosen`](../devicetree/root__chosen.md) = `0x0` |
| `boot-type` | 1 | string | [`/chosen`](../devicetree/root__chosen.md) = `local` |
| `boot-voltage` | 1 | u32 | [`/arm-io/smc/iop-smc-nub/smc-charger`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-charger.md) = `0x0` |
| `bootloader-type` | 3 | string×3 | [`/arm-io/mtp/iop-mtp-nub/multi-touch2`](../devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch2.md) = `CBOR`<br>[`/arm-io/mtp/iop-mtp-nub/multi-touch`](../devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch.md) = `CBOR`<br>[`/arm-io/mtp/iop-mtp-nub/nova`](../devicetree/root__arm-io__mtp__iop-mtp-nub__nova.md) = `FlatPack` |
| `bootp-response` | 1 | 300 B | [`/chosen`](../devicetree/root__chosen.md) = `00000000000000000000000000000000…` |
| `bridge-offset` | 1 | u32 | [`/arm-io/nub-spmi0/pmu-main/sgpio-bridge-pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main__sgpio-bridge-pmu-main.md) = `0xdd10` |
| `btm-enabled` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x1` |
| `btm-pmu-type` | 1 | u32 | [`/arm-io/nub-spmi0/btm`](../devicetree/root__arm-io__nub-spmi0__btm.md) = `0xf` |
| `built-in` | 5 | empty×5 | [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) = ``<br>[`/arm-io/apcie/pci-bridge0/centauri-control`](../devicetree/root__arm-io__apcie__pci-bridge0__centauri-control.md) = ``<br>[`/arm-io/apcie/pci-bridge0/centauri-alpha`](../devicetree/root__arm-io__apcie__pci-bridge0__centauri-alpha.md) = ``<br>[`/arm-io/apcie/pci-bridge0/centauri-beta`](../devicetree/root__arm-io__apcie__pci-bridge0__centauri-beta.md) = ``<br>[`/arm-io/apcie/pci-bridge1`](../devicetree/root__arm-io__apcie__pci-bridge1.md) = `` |
| `builtin-mics` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x4` |
| `bus-number` | 1 | u32 | [`/arm-io/usb-drd0`](../devicetree/root__arm-io__usb-drd0.md) = `0x0` |
| `bus-range` | 1 | u64 | [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) = `0x800000000` |
| `button-delay_hold` | 1 | u32 | [`/buttons`](../devicetree/root__buttons.md) = `0x124f8` |
| `button-delay_voldown` | 1 | u32 | [`/buttons`](../devicetree/root__buttons.md) = `0x124f8` |
| `button-delay_volup` | 1 | u32 | [`/buttons`](../devicetree/root__buttons.md) = `0x124f8` |
| `button-names` | 1 | string | [`/buttons`](../devicetree/root__buttons.md) = `volup, voldown, hold` |
| `button-priority_hold` | 1 | u32 | [`/buttons`](../devicetree/root__buttons.md) = `0x1` |
| `button-priority_voldown` | 1 | u32 | [`/buttons`](../devicetree/root__buttons.md) = `0x2` |
| `button-priority_volup` | 1 | u32 | [`/buttons`](../devicetree/root__buttons.md) = `0x2` |
| `bwr-agent` | 1 | 192 B | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0100000122000000444953505f494e54…` |
| `bwr-catch-up-factor` | 1 | u32 | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0x10000` |
| `bypass-10` | 2 | empty×2 | [`/arm-io/dart-ane0`](../devicetree/root__arm-io__dart-ane0.md) = ``<br>[`/arm-io/dart-ane1`](../devicetree/root__arm-io__dart-ane1.md) = `` |
| `bypass-13` | 2 | empty×2 | [`/arm-io/dart-ane0`](../devicetree/root__arm-io__dart-ane0.md) = ``<br>[`/arm-io/dart-ane1`](../devicetree/root__arm-io__dart-ane1.md) = `` |
| `bypass-15` | 3 | empty×3 | [`/arm-io/dart-isp`](../devicetree/root__arm-io__dart-isp.md) = ``<br>[`/arm-io/dart-ane0`](../devicetree/root__arm-io__dart-ane0.md) = ``<br>[`/arm-io/dart-ane1`](../devicetree/root__arm-io__dart-ane1.md) = `` |
| `bypass-16` | 2 | empty×2 | [`/arm-io/dart-apcie0`](../devicetree/root__arm-io__dart-apcie0.md) = ``<br>[`/arm-io/dart-apcie1`](../devicetree/root__arm-io__dart-apcie1.md) = `` |
| `bypass-18` | 2 | empty×2 | [`/arm-io/dart-apcie0`](../devicetree/root__arm-io__dart-apcie0.md) = ``<br>[`/arm-io/dart-apcie1`](../devicetree/root__arm-io__dart-apcie1.md) = `` |
| `ca-client-cpu-work-dev-w-down` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x10a3d7` |
| `ca-client-cpu-work-high-dev` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x80000` |
| `ca-client-cpu-work-high-floor` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x1999` |
| `ca-client-cpu-work-typical-dev` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x10000` |
| `ca-client-cpu-work-window` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x15c28f` |
| `calibration-source` | 1 | u32 | [`/exbright`](../devicetree/root__exbright.md) = `0x1` |
| `camera-button-location` | 3 | 24 B×3 | [`/product`](../devicetree/root__product.md) = `74c60b00d221110069400b00d09b0200…`<br>[`/product/display0`](../devicetree/root__product__display0.md) = `74c60b00d221110069400b00d09b0200…`<br>[`/product/display1`](../devicetree/root__product__display1.md) = `8409180034e810008c220b00d09b0200…` |
| `camera-driver` | 1 | string | [`/arm-io/smc/iop-smc-nub/smc-ext-charger`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-ext-charger.md) = `AppleCamera` |
| `camera-front` | 2 | u32×2 | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) = `0x1`<br>[`/arm-io/isp`](../devicetree/root__arm-io__isp.md) = `0x1` |
| `camera-hdr-version` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x3` |
| `camera-rear` | 2 | u32×2 | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) = `0x1`<br>[`/arm-io/isp`](../devicetree/root__arm-io__isp.md) = `0x1` |
| `camera-strobe-color-cal` | 2 | string×2 | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) = `syscfg/STRB`<br>[`/arm-io/isp`](../devicetree/root__arm-io__isp.md) = `syscfg/STRB` |
| `camera-ui-version` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x2` |
| `canvas-height` | 1 | u32 | [`/arm-io/dispsec`](../devicetree/root__arm-io__dispsec.md) = `0xb25` |
| `canvas-width` | 1 | u32 | [`/arm-io/dispsec`](../devicetree/root__arm-io__dispsec.md) = `0x7d7` |
| `cap0-offset` | 1 | u32 | [`/arm-io/aic`](../devicetree/root__arm-io__aic.md) = `0x4` |
| `cap0_max_interrupt_umask` | 1 | u32 | [`/arm-io/aic`](../devicetree/root__arm-io__aic.md) = `0xffff` |
| `car-integration` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `carplay-2` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `carplay-power-limit` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x18000` |
| `ce-model` | 3 | u32×3 | [`/arm-io/aop/iop-aop-nub/als2a`](../devicetree/root__arm-io__aop__iop-aop-nub__als2a.md) = `0x5`<br>[`/arm-io/aop/iop-aop-nub/als2b`](../devicetree/root__arm-io__aop__iop-aop-nub__als2b.md) = `0x0`<br>[`/arm-io/aop/iop-aop-nub/als`](../devicetree/root__arm-io__aop__iop-aop-nub__als.md) = `0x4` |
| `ce-threshold` | 2 | u32×2 | [`/arm-io/aop/iop-aop-nub/als2a`](../devicetree/root__arm-io__aop__iop-aop-nub__als2a.md) = `0x1eb8`<br>[`/arm-io/aop/iop-aop-nub/als`](../devicetree/root__arm-io__aop__iop-aop-nub__als.md) = `0x6666` |
| `ced-ssw-service` | 6 | string×6 | [`/arm-io/admac-dispint0`](../devicetree/root__arm-io__admac-dispint0.md) = `AudioDMACLLTEscalationDetectorDISP-I-ISOC`<br>[`/arm-io/admac-dispext0`](../devicetree/root__arm-io__admac-dispext0.md) = `AudioDMACLLTEscalationDetectorDISP-E0-ISOC`<br>[`/arm-io/admac-base-ns`](../devicetree/root__arm-io__admac-base-ns.md) = `AudioDMACLLTEscalationDetectorADMAC-A`<br>[`/arm-io/admac-leap-ns`](../devicetree/root__arm-io__admac-leap-ns.md) = `AudioDMACLLTEscalationDetectorADMAC-A`<br>[`/arm-io/admac-base-s`](../devicetree/root__arm-io__admac-base-s.md) = `AudioDMACLLTEscalationDetectorADMAC-A` |
| `centauri-builtin` | 1 | empty | [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) = `` |
| `certificate-production-status` | 1 | u32 | [`/chosen`](../devicetree/root__chosen.md) = `0x0` |
| `certificate-security-mode` | 1 | u32 | [`/chosen`](../devicetree/root__chosen.md) = `0x0` |
| `cg-reflectance` | 2 | u32×2 | [`/exbright/contrast-indicator-0`](../devicetree/root__exbright__contrast-indicator-0.md) = `0x4ccc`<br>[`/exbright/contrast-indicator-1`](../devicetree/root__exbright__contrast-indicator-1.md) = `0x4` |
| `channel-buffer-alloc-base-rx` | 6 | u32×6 | [`/arm-io/admac-dispint0`](../devicetree/root__arm-io__admac-dispint0.md) = `0x0`<br>[`/arm-io/admac-dispext0`](../devicetree/root__arm-io__admac-dispext0.md) = `0x0`<br>[`/arm-io/admac-base-ns`](../devicetree/root__arm-io__admac-base-ns.md) = `0x0`<br>[`/arm-io/admac-leap-ns`](../devicetree/root__arm-io__admac-leap-ns.md) = `0x0`<br>[`/arm-io/admac-base-s`](../devicetree/root__arm-io__admac-base-s.md) = `0x0` |
| `channel-buffer-alloc-base-tx` | 6 | u32×6 | [`/arm-io/admac-dispint0`](../devicetree/root__arm-io__admac-dispint0.md) = `0x0`<br>[`/arm-io/admac-dispext0`](../devicetree/root__arm-io__admac-dispext0.md) = `0x0`<br>[`/arm-io/admac-base-ns`](../devicetree/root__arm-io__admac-base-ns.md) = `0x0`<br>[`/arm-io/admac-leap-ns`](../devicetree/root__arm-io__admac-leap-ns.md) = `0x0`<br>[`/arm-io/admac-base-s`](../devicetree/root__arm-io__admac-base-s.md) = `0x0` |
| `channel-buffer-allocation` | 6 | 16 B×4, u64×2 | [`/arm-io/admac-dispint0`](../devicetree/root__arm-io__admac-dispint0.md) = `0x1900`<br>[`/arm-io/admac-dispext0`](../devicetree/root__arm-io__admac-dispext0.md) = `0x1900`<br>[`/arm-io/admac-base-ns`](../devicetree/root__arm-io__admac-base-ns.md) = `001e000000000000001e000000000000`<br>[`/arm-io/admac-leap-ns`](../devicetree/root__arm-io__admac-leap-ns.md) = `000e0000000000000011000000000000`<br>[`/arm-io/admac-base-s`](../devicetree/root__arm-io__admac-base-s.md) = `80010000000000000040000000000000` |
| `channel-buffer-size` | 16 | empty×16 | [`/arm-io/admac-base-ns/base-ns-adma-rx-2`](../devicetree/root__arm-io__admac-base-ns__base-ns-adma-rx-2.md) = ``<br>[`/arm-io/admac-base-ns/base-ns-adma-rx-3`](../devicetree/root__arm-io__admac-base-ns__base-ns-adma-rx-3.md) = ``<br>[`/arm-io/admac-base-ns/base-ns-adma-rx-4`](../devicetree/root__arm-io__admac-base-ns__base-ns-adma-rx-4.md) = ``<br>[`/arm-io/admac-base-ns/base-ns-adma-rx-5`](../devicetree/root__arm-io__admac-base-ns__base-ns-adma-rx-5.md) = ``<br>[`/arm-io/admac-base-ns/base-ns-adma-tx-7`](../devicetree/root__arm-io__admac-base-ns__base-ns-adma-tx-7.md) = `` |
| `channel-is-development-only` | 1 | empty | [`/arm-io/admac-leap-s/leap-s-adma-rx-2`](../devicetree/root__arm-io__admac-leap-s__leap-s-adma-rx-2.md) = `` |
| `channels-offset` | 6 | u32×6 | [`/arm-io/admac-dispint0`](../devicetree/root__arm-io__admac-dispint0.md) = `0x0`<br>[`/arm-io/admac-dispext0`](../devicetree/root__arm-io__admac-dispext0.md) = `0x0`<br>[`/arm-io/admac-base-ns`](../devicetree/root__arm-io__admac-base-ns.md) = `0x0`<br>[`/arm-io/admac-leap-ns`](../devicetree/root__arm-io__admac-leap-ns.md) = `0x0`<br>[`/arm-io/admac-base-s`](../devicetree/root__arm-io__admac-base-s.md) = `0x0` |
| `charger-compensation-vers` | 1 | u32 | [`/arm-io/aop/iop-aop-nub/compass`](../devicetree/root__arm-io__aop__iop-aop-nub__compass.md) = `0x2` |
| `chip-id` | 1 | u32 | [`/chosen`](../devicetree/root__chosen.md) = `0x0` |
| `chip-revision` | 1 | u32 | [`/arm-io`](../devicetree/root__arm-io.md) = `0x0` |
| `chiplet-count` | 1 | u32 | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) = `0x1` |
| `chromatic-visibility-f` | 2 | u32×2 | [`/exbright/contrast-indicator-0`](../devicetree/root__exbright__contrast-indicator-0.md) = `0x2145a`<br>[`/exbright/contrast-indicator-1`](../devicetree/root__exbright__contrast-indicator-1.md) = `0x2145a` |
| `chrome-identifier` | 3 | string×3 | [`/product`](../devicetree/root__product.md) = `com.apple.dt.devicekit.chrome.phone15`<br>[`/product/display0`](../devicetree/root__product__display0.md) = `com.apple.dt.devicekit.chrome.phone15`<br>[`/product/display1`](../devicetree/root__product__display1.md) = `com.apple.dt.devicekit.chrome.phone14` |
| `ci-constant-hdr` | 2 | u32×2 | [`/exbright/contrast-indicator-0`](../devicetree/root__exbright__contrast-indicator-0.md) = `0x26666`<br>[`/exbright/contrast-indicator-1`](../devicetree/root__exbright__contrast-indicator-1.md) = `0x24ccc` |
| `ci-constant-sdr` | 2 | u32×2 | [`/exbright/contrast-indicator-0`](../devicetree/root__exbright__contrast-indicator-0.md) = `0xcccc`<br>[`/exbright/contrast-indicator-1`](../devicetree/root__exbright__contrast-indicator-1.md) = `0xb333` |
| `ci-lux-factor-hdr` | 2 | u32×2 | [`/exbright/contrast-indicator-0`](../devicetree/root__exbright__contrast-indicator-0.md) = `0xc4`<br>[`/exbright/contrast-indicator-1`](../devicetree/root__exbright__contrast-indicator-1.md) = `0x560` |
| `ci-lux-factor-sdr` | 2 | u32×2 | [`/exbright/contrast-indicator-0`](../devicetree/root__exbright__contrast-indicator-0.md) = `0x41`<br>[`/exbright/contrast-indicator-1`](../devicetree/root__exbright__contrast-indicator-1.md) = `0x1f2` |
| `ci-nits-factor-hdr` | 2 | u32×2 | [`/exbright/contrast-indicator-0`](../devicetree/root__exbright__contrast-indicator-0.md) = `0x209fb`<br>[`/exbright/contrast-indicator-1`](../devicetree/root__exbright__contrast-indicator-1.md) = `0x22666` |
| `ci-nits-factor-sdr` | 2 | u32×2 | [`/exbright/contrast-indicator-0`](../devicetree/root__exbright__contrast-indicator-0.md) = `0x12212`<br>[`/exbright/contrast-indicator-1`](../devicetree/root__exbright__contrast-indicator-1.md) = `0x1428f` |
| `cil` | 1 | u32 | [`/arm-io/eic`](../devicetree/root__arm-io__eic.md) = `0x1` |
| `cl4-entropy` | 1 | 192 B | [`/chosen`](../devicetree/root__chosen.md) = `00000000000000000000000000000000…` |
| `claim-wake` | 4 | empty×4 | [`/arm-io/aop/iop-aop-nub`](../devicetree/root__arm-io__aop__iop-aop-nub.md) = ``<br>[`/arm-io/aop-exclave-mailbox`](../devicetree/root__arm-io__aop-exclave-mailbox.md) = ``<br>[`/arm-io/aop2/iop-aop2-nub`](../devicetree/root__arm-io__aop2__iop-aop2-nub.md) = ``<br>[`/arm-io/aop2-exclave-mailbox`](../devicetree/root__arm-io__aop2-exclave-mailbox.md) = `` |
| `claim-wake-endpoint-flags` | 1 | 16 B | [`/arm-io/aop2-exclave-mailbox`](../devicetree/root__arm-io__aop2-exclave-mailbox.md) = `30000000040000003100000004000000` |
| `class` | 1 | u32 | [`/baseband`](../devicetree/root__baseband.md) = `0x3` |
| `clcdclk_frequency` | 1 | 12 B | [`/arm-io/dispext0`](../devicetree/root__arm-io__dispext0.md) = `300000004342475201000000` |
| `clcl-cal` | 1 | string | [`/arm-io/haptics-support-interface`](../devicetree/root__arm-io__haptics-support-interface.md) = `syscfg/CLCL` |
| `clcl-cal-mi` | 1 | string | [`/arm-io/haptics-support-interface`](../devicetree/root__arm-io__haptics-support-interface.md) = `syscfg-mismatch/CLCL` |
| `client_budgets_extra` | 1 | 68 B | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0000000d00000100c3d300007aba0000…` |
| `client_powers_extra` | 1 | 68 B | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0000000d35420000c43600003a300000…` |
| `clients_extra` | 1 | 24 B | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0103030d000000007374726f62650000…` |
| `clock-domain` | 11 | u32×11 | [`/arm-io/iop-audio-controller/audio-hp`](../devicetree/root__arm-io__iop-audio-controller__audio-hp.md) = `0x6d61696e`<br>[`/arm-io/iop-audio-controller/audio-leap-internal-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-leap-internal-loopback.md) = `0x6d61696e`<br>[`/arm-io/iop-audio-controller/audio-mca-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-mca-loopback.md) = `0x6d61696e`<br>[`/arm-io/iop-audio-controller/audio-receiver`](../devicetree/root__arm-io__iop-audio-controller__audio-receiver.md) = `0x6d61696e`<br>[`/arm-io/iop-audio-controller/audio-flicker`](../devicetree/root__arm-io__iop-audio-controller__audio-flicker.md) = `0x6d61696e` |
| `clock-frequencies` | 1 | 384 B | [`/arm-io`](../devicetree/root__arm-io.md) = `00000000000000000000000000000000…` |
| `clock-frequency` | 1 | u32 | [`/`](../devicetree/root.md) = `0x0` |
| `clock-gates` | 28 | u32×14, empty×7, u64×4 | [`/arm-io/aes`](../devicetree/root__arm-io__aes.md) = `0x19`<br>[`/arm-io/aop`](../devicetree/root__arm-io__aop.md) = ``<br>[`/arm-io/aop2`](../devicetree/root__arm-io__aop2.md) = ``<br>[`/arm-io/pmp`](../devicetree/root__arm-io__pmp.md) = `0x9800000097`<br>[`/arm-io/sep`](../devicetree/root__arm-io__sep.md) = `` |
| `clock-ids` | 31 | u32×12, empty×8, u64×7 | [`/arm-io/wdt`](../devicetree/root__arm-io__wdt.md) = `0x4`<br>[`/arm-io/spi1`](../devicetree/root__arm-io__spi1.md) = `0x194`<br>[`/arm-io/aop`](../devicetree/root__arm-io__aop.md) = ``<br>[`/arm-io/aop2`](../devicetree/root__arm-io__aop2.md) = ``<br>[`/arm-io/pmp`](../devicetree/root__arm-io__pmp.md) = `` |
| `closed-loop` | 1 | u32 | [`/product/haptics`](../devicetree/root__product__haptics.md) = `0x1` |
| `clpc` | 1 | u32 | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) = `0x3` |
| `clpc-dev-intrs-timeout` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x7a120` |
| `clpc-voter-agent-idx` | 1 | u32 | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0x1` |
| `cluster-ctl-offset` | 1 | u32 | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0x80000` |
| `cluster-dvfs-devices` | 1 | 32 B | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `00000000030000000100000004000000…` |
| `cluster-id` | 6 | u32×6 | [`/cpus/cpu0`](../devicetree/root__cpus__cpu0.md) = `0x0`<br>[`/cpus/cpu1`](../devicetree/root__cpus__cpu1.md) = `0x0`<br>[`/cpus/cpu2`](../devicetree/root__cpus__cpu2.md) = `0x0`<br>[`/cpus/cpu3`](../devicetree/root__cpus__cpu3.md) = `0x0`<br>[`/cpus/cpu4`](../devicetree/root__cpus__cpu4.md) = `0x1` |
| `cluster-type` | 6 | string×6 | [`/cpus/cpu0`](../devicetree/root__cpus__cpu0.md) = `E`<br>[`/cpus/cpu1`](../devicetree/root__cpus__cpu1.md) = `E`<br>[`/cpus/cpu2`](../devicetree/root__cpus__cpu2.md) = `E`<br>[`/cpus/cpu3`](../devicetree/root__cpus__cpu3.md) = `E`<br>[`/cpus/cpu4`](../devicetree/root__cpus__cpu4.md) = `P` |
| `clusters` | 1 | u64 | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0x200000004` |
| `coex0-driver-name` | 2 | string×2 | [`/arm-io/aop/iop-aop-nub/compass`](../devicetree/root__arm-io__aop__iop-aop-nub__compass.md) = `IOPAudioSpeaker`<br>[`/arm-io/aop/iop-aop-nub/cma`](../devicetree/root__arm-io__aop__iop-aop-nub__cma.md) = `IOPHaptics` |
| `coex0-notif-off` | 2 | u32×2 | [`/arm-io/aop/iop-aop-nub/compass`](../devicetree/root__arm-io__aop__iop-aop-nub__compass.md) = `0xe3ff8108`<br>[`/arm-io/aop/iop-aop-nub/cma`](../devicetree/root__arm-io__aop__iop-aop-nub__cma.md) = `0xe3ff810e` |
| `coex0-notif-on` | 2 | u32×2 | [`/arm-io/aop/iop-aop-nub/compass`](../devicetree/root__arm-io__aop__iop-aop-nub__compass.md) = `0xe3ff8107`<br>[`/arm-io/aop/iop-aop-nub/cma`](../devicetree/root__arm-io__aop__iop-aop-nub__cma.md) = `0xe3ff810d` |
| `coex0-payload-off` | 2 | u32×2 | [`/arm-io/aop/iop-aop-nub/compass`](../devicetree/root__arm-io__aop__iop-aop-nub__compass.md) = `0x0`<br>[`/arm-io/aop/iop-aop-nub/cma`](../devicetree/root__arm-io__aop__iop-aop-nub__cma.md) = `0x0` |
| `coex0-payload-on` | 2 | u32×2 | [`/arm-io/aop/iop-aop-nub/compass`](../devicetree/root__arm-io__aop__iop-aop-nub__compass.md) = `0x1`<br>[`/arm-io/aop/iop-aop-nub/cma`](../devicetree/root__arm-io__aop__iop-aop-nub__cma.md) = `0x1` |
| `coex0-prop` | 2 | u32×2 | [`/arm-io/aop/iop-aop-nub/compass`](../devicetree/root__arm-io__aop__iop-aop-nub__compass.md) = `0x59`<br>[`/arm-io/aop/iop-aop-nub/cma`](../devicetree/root__arm-io__aop__iop-aop-nub__cma.md) = `0xdb` |
| `coex1-driver-name` | 1 | string | [`/arm-io/aop/iop-aop-nub/compass`](../devicetree/root__arm-io__aop__iop-aop-nub__compass.md) = `IOPHaptics` |
| `coex1-notif-off` | 1 | u32 | [`/arm-io/aop/iop-aop-nub/compass`](../devicetree/root__arm-io__aop__iop-aop-nub__compass.md) = `0xe3ff810e` |
| `coex1-notif-on` | 1 | u32 | [`/arm-io/aop/iop-aop-nub/compass`](../devicetree/root__arm-io__aop__iop-aop-nub__compass.md) = `0xe3ff810d` |
| `coex1-payload-off` | 1 | u32 | [`/arm-io/aop/iop-aop-nub/compass`](../devicetree/root__arm-io__aop__iop-aop-nub__compass.md) = `0x0` |
| `coex1-payload-on` | 1 | u32 | [`/arm-io/aop/iop-aop-nub/compass`](../devicetree/root__arm-io__aop__iop-aop-nub__compass.md) = `0x1` |
| `coex1-prop` | 1 | u32 | [`/arm-io/aop/iop-aop-nub/compass`](../devicetree/root__arm-io__aop__iop-aop-nub__compass.md) = `0x59` |
| `coex2-driver-name` | 1 | string | [`/arm-io/aop/iop-aop-nub/compass`](../devicetree/root__arm-io__aop__iop-aop-nub__compass.md) = `AppleSARService` |
| `coex2-notif-off` | 1 | u32 | [`/arm-io/aop/iop-aop-nub/compass`](../devicetree/root__arm-io__aop__iop-aop-nub__compass.md) = `0xe3ff8012` |
| `coex2-notif-on` | 1 | u32 | [`/arm-io/aop/iop-aop-nub/compass`](../devicetree/root__arm-io__aop__iop-aop-nub__compass.md) = `0xe3ff8011` |
| `coex2-payload-off` | 1 | u32 | [`/arm-io/aop/iop-aop-nub/compass`](../devicetree/root__arm-io__aop__iop-aop-nub__compass.md) = `0x0` |
| `coex2-payload-on` | 1 | u32 | [`/arm-io/aop/iop-aop-nub/compass`](../devicetree/root__arm-io__aop__iop-aop-nub__compass.md) = `0x1` |
| `coex2-prop` | 1 | u32 | [`/arm-io/aop/iop-aop-nub/compass`](../devicetree/root__arm-io__aop__iop-aop-nub__compass.md) = `0x59` |
| `cold-boot-after-hibernate` | 5 | empty×5 | [`/arm-io/ans/iop-ans-nub`](../devicetree/root__arm-io__ans__iop-ans-nub.md) = ``<br>[`/arm-io/smc/iop-smc-nub`](../devicetree/root__arm-io__smc__iop-smc-nub.md) = ``<br>[`/arm-io/mtp/iop-mtp-nub`](../devicetree/root__arm-io__mtp__iop-mtp-nub.md) = ``<br>[`/arm-io/dcpsec/iop-dcpsec-nub`](../devicetree/root__arm-io__dcpsec__iop-dcpsec-nub.md) = ``<br>[`/arm-io/dcpext0/iop-dcpext0-nub`](../devicetree/root__arm-io__dcpext0__iop-dcpext0-nub.md) = `` |
| `collision-sos` | 1 | empty | [`/product`](../devicetree/root__product.md) = `` |
| `color-space` | 2 | u32×2 | [`/exbright/contrast-indicator-0`](../devicetree/root__exbright__contrast-indicator-0.md) = `0x0`<br>[`/exbright/contrast-indicator-1`](../devicetree/root__exbright__contrast-indicator-1.md) = `0x0` |
| `compass-apl-compensation-boe` | 1 | string | [`/arm-io/aop/iop-aop-nub/compass`](../devicetree/root__arm-io__aop__iop-aop-nub__compass.md) = `syscfg/MDCC` |
| `compass-apl-compensation-sdc` | 1 | string | [`/arm-io/aop/iop-aop-nub/compass`](../devicetree/root__arm-io__aop__iop-aop-nub__compass.md) = `syscfg/MDCC` |
| `compass-calibration` | 2 | string×2 | [`/arm-io/aop/iop-aop-nub/compass`](../devicetree/root__arm-io__aop__iop-aop-nub__compass.md) = `syscfg/CPAS`<br>[`/arm-io/aop/iop-aop-nub/compass_1`](../devicetree/root__arm-io__aop__iop-aop-nub__compass_1.md) = `syscfg/CPAS` |
| `compass-hilo-compensation` | 1 | string | [`/arm-io/aop/iop-aop-nub/compass`](../devicetree/root__arm-io__aop__iop-aop-nub__compass.md) = `syscfg/CDCC` |
| `compass-mode-offset-comp` | 1 | string | [`/arm-io/aop/iop-aop-nub/compass`](../devicetree/root__arm-io__aop__iop-aop-nub__compass.md) = `syscfg/CMOC` |
| `compass-orientation` | 2 | string×2 | [`/arm-io/aop/iop-aop-nub/compass`](../devicetree/root__arm-io__aop__iop-aop-nub__compass.md) = `syscfg/CRot,hex/01000101000000002800000003000000000000000000`<br>[`/arm-io/aop/iop-aop-nub/compass_1`](../devicetree/root__arm-io__aop__iop-aop-nub__compass_1.md) = `syscfg/JRot,hex/01000101010000002800000003000000000001000000` |
| `compass-orientation-p2` | 1 | string | [`/arm-io/aop/iop-aop-nub/compass`](../devicetree/root__arm-io__aop__iop-aop-nub__compass.md) = `syscfg/CRot,hex/01000101000000002800000003000000000000000000` |
| `compass-sens-angle-table` | 1 | string | [`/arm-io/aop/iop-aop-nub/compass`](../devicetree/root__arm-io__aop__iop-aop-nub__compass.md) = `hex/01000000060000000000000099FB0000D8000000ECFFFFFF5A050000` |
| `compass-sens-calibration` | 1 | string | [`/arm-io/aop/iop-aop-nub/compass`](../devicetree/root__arm-io__aop__iop-aop-nub__compass.md) = `syscfg/CSCM` |
| `compass-sens-calibration-closed` | 1 | string | [`/arm-io/aop/iop-aop-nub/compass`](../devicetree/root__arm-io__aop__iop-aop-nub__compass.md) = `syscfg/CSCa` |
| `compass-temp-calibration` | 1 | 32 B | [`/arm-io/aop/iop-aop-nub/compass`](../devicetree/root__arm-io__aop__iop-aop-nub__compass.md) = `03000000661800001e86ffffcd5c0000…` |
| `compass-vbus-compensation` | 1 | string | [`/arm-io/aop/iop-aop-nub/compass`](../devicetree/root__arm-io__aop__iop-aop-nub__compass.md) = `syscfg/CVCC` |
| `compatible` | 332 | string×332 | [`/`](../devicetree/root.md) = `V68AP, iPhone19,4, AppleARM`<br>[`/cpus/cpu0`](../devicetree/root__cpus__cpu0.md) = `apple,sawtooth, ARM,v8`<br>[`/cpus/cpu1`](../devicetree/root__cpus__cpu1.md) = `apple,sawtooth, ARM,v8`<br>[`/cpus/cpu2`](../devicetree/root__cpus__cpu2.md) = `apple,sawtooth, ARM,v8`<br>[`/cpus/cpu3`](../devicetree/root__cpus__cpu3.md) = `apple,sawtooth, ARM,v8` |
| `compatible-app-variant` | 1 | string | [`/product`](../devicetree/root__product.md) = `0` |
| `compatible-device-fallback` | 1 | string | [`/product`](../devicetree/root__product.md) = `iPhone18,3` |
| `component-index` | 2 | u32×2 | [`/arm-io/i2c3/mogul-display`](../devicetree/root__arm-io__i2c3__mogul-display.md) = `0x1`<br>[`/arm-io/i2c3/mogul-display2`](../devicetree/root__arm-io__i2c3__mogul-display2.md) = `0x2` |
| `config` | 2 | u32, 40 B | [`/arm-io/sep/iop-sep-nub/InvalidateHmac`](../devicetree/root__arm-io__sep__iop-sep-nub__InvalidateHmac.md) = `0x1`<br>[`/baseband`](../devicetree/root__baseband.md) = `fa000000f401000000000000e8030000…` |
| `config-auto-rate-change-flag` | 1 | u32 | [`/arm-io/nub-spmi0/btm`](../devicetree/root__arm-io__nub-spmi0__btm.md) = `0x1` |
| `config-duty-cycle-data-read` | 1 | u32 | [`/arm-io/nub-spmi0/btm`](../devicetree/root__arm-io__nub-spmi0__btm.md) = `0x1` |
| `config-number` | 1 | string | [`/`](../devicetree/root.md) = `syscfg/CFG#/0x40,zeroes/0x40` |
| `config-vddmain-data-read` | 1 | u32 | [`/arm-io/nub-spmi0/btm`](../devicetree/root__arm-io__nub-spmi0__btm.md) = `0x1` |
| `configuration-string` | 2 | string×2 | [`/arm-io/rsm`](../devicetree/root__arm-io__rsm.md) = `muxNcm`<br>[`/arm-io/usb-drd0`](../devicetree/root__arm-io__usb-drd0.md) = `stdMuxPTPEthValIDA` |
| `consistent-debug-root` | 1 | u64 | [`/chosen`](../devicetree/root__chosen.md) = `0x0` |
| `content-protect` | 1 | empty | [`/defaults`](../devicetree/root__defaults.md) = `` |
| `continuous-NAND-client` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x1` |
| `continuous-time` | 2 | empty×2 | [`/arm-io/ans/iop-ans-nub`](../devicetree/root__arm-io__ans__iop-ans-nub.md) = ``<br>[`/arm-io/smc/iop-smc-nub`](../devicetree/root__arm-io__smc__iop-smc-nub.md) = `` |
| `controller` | 1 | 1144 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `010000001f0000004300000000000000…` |
| `controller-coeff-cal` | 1 | string | [`/product/haptics`](../devicetree/root__product__haptics.md) = `syscfg/CLCL` |
| `coprovider-group` | 2 | string×2 | [`/arm-io/scaler0`](../devicetree/root__arm-io__scaler0.md) = `scaler`<br>[`/arm-io/jpeg`](../devicetree/root__arm-io__jpeg.md) = `jpeg` |
| `coredump-active-only` | 1 | empty | [`/arm-io/smc/iop-smc-nub`](../devicetree/root__arm-io__smc__iop-smc-nub.md) = `` |
| `coredump-copy-buffer` | 2 | u32×2 | [`/arm-io/gfx-asc/iop-gfx-nub`](../devicetree/root__arm-io__gfx-asc__iop-gfx-nub.md) = `0x8000`<br>[`/arm-io/gfx1-asc/iop-gfx1-nub`](../devicetree/root__arm-io__gfx1-asc__iop-gfx1-nub.md) = `0x8000` |
| `coredump-enable` | 13 | u32×13 | [`/arm-io/aop/iop-aop-nub`](../devicetree/root__arm-io__aop__iop-aop-nub.md) = `0x40`<br>[`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0x40`<br>[`/arm-io/sio/iop-sio-nub`](../devicetree/root__arm-io__sio__iop-sio-nub.md) = `0x40`<br>[`/arm-io/smc/iop-smc-nub`](../devicetree/root__arm-io__smc__iop-smc-nub.md) = `0x40`<br>[`/arm-io/mtp/iop-mtp-nub`](../devicetree/root__arm-io__mtp__iop-mtp-nub.md) = `0x40` |
| `coredump-rel-privacy-approved` | 3 | empty×3 | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = ``<br>[`/arm-io/gfx-asc/iop-gfx-nub`](../devicetree/root__arm-io__gfx-asc__iop-gfx-nub.md) = ``<br>[`/arm-io/gfx1-asc/iop-gfx1-nub`](../devicetree/root__arm-io__gfx1-asc__iop-gfx1-nub.md) = `` |
| `coresight-reg` | 6 | 16 B×6 | [`/cpus/cpu0`](../devicetree/root__cpus__cpu0.md) = `0000011002000000c800030000000000`<br>[`/cpus/cpu1`](../devicetree/root__cpus__cpu1.md) = `0000111002000000c800030000000000`<br>[`/cpus/cpu2`](../devicetree/root__cpus__cpu2.md) = `0000211002000000c800030000000000`<br>[`/cpus/cpu3`](../devicetree/root__cpus__cpu3.md) = `0000311002000000c800030000000000`<br>[`/cpus/cpu4`](../devicetree/root__cpus__cpu4.md) = `0000011102000000c800030000000000` |
| `corr-err-period-us` | 2 | u32×2 | [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) = `0x0`<br>[`/arm-io/apcie/pci-bridge1`](../devicetree/root__arm-io__apcie__pci-bridge1.md) = `0x0` |
| `country-of-origin` | 1 | string | [`/`](../devicetree/root.md) = `syscfg/Coor` |
| `cover-glass-material` | 1 | string | [`/chosen`](../devicetree/root__chosen.md) = `syscfg/CGMt` |
| `coverglass-color` | 1 | string | [`/chosen`](../devicetree/root__chosen.md) = `syscfg/CLCG` |
| `cpm-impl` | 1 | 32 B | [`/arm-io`](../devicetree/root__arm-io.md) = `0000e410020000000080000000000000…` |
| `cpm-impl-reg` | 6 | 16 B×6 | [`/cpus/cpu0`](../devicetree/root__cpus__cpu0.md) = `0000e4100200000028c0000000000000`<br>[`/cpus/cpu1`](../devicetree/root__cpus__cpu1.md) = `0000e4100200000028c0000000000000`<br>[`/cpus/cpu2`](../devicetree/root__cpus__cpu2.md) = `0000e4100200000028c0000000000000`<br>[`/cpus/cpu3`](../devicetree/root__cpus__cpu3.md) = `0000e4100200000028c0000000000000`<br>[`/cpus/cpu4`](../devicetree/root__cpus__cpu4.md) = `0000e4110200000028c0000000000000` |
| `cpms-batt-model-100ms-fallback` | 1 | 880 B | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `d0070000d0070000da070000e4070000…` |
| `cpms-batt-model-1ms-fallback` | 1 | 880 B | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `409c0000409c0000409c0000409c0000…` |
| `cpms-batt-model-1s-fallback` | 1 | 880 B | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `d0070000d0070000da070000e4070000…` |
| `cpms-fallback-power-low` | 1 | 12 B | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `3cc4ffff3cc4ffff3cc4ffff` |
| `cpms-full-mode-load-frac-hyst` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x1999` |
| `cpms-full-mode-load-fraction` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0xc000` |
| `cpms-input-current-rate-thr` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x1999` |
| `cpms-input-decay-weight-pmu` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0xab9a` |
| `cpms-input-decay-weight-pmu-red` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x4b0` |
| `cpms-input-enable-pmu-VF` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x1` |
| `cpms-input-ki-gain-down` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x51e` |
| `cpms-input-ki-gain-up` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x51e` |
| `cpms-input-pp-max-fusion` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x1` |
| `cpms-input-Ps-cutoff-voltage` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x34000` |
| `cpms-input-ps-max-fusion` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x1` |
| `cpms-input-Pu-cutoff-voltage` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x34000` |
| `cpms-input-ratio-up-pp` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0xcccc` |
| `cpms-input-ratio-up-ps` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0xcccc` |
| `cpms-input-use-filter-pp` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x1` |
| `cpms-input-use-filter-ps` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x1` |
| `cpms-input-voltage-thr` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x7ae` |
| `cpms-input-weight-factor-pp` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x10000` |
| `cpms-input-weight-factor-ps` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x10000` |
| `cpms-pmax-computed-rdc` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x1` |
| `cpms-pmax-enable-neg-sys-ld` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x1` |
| `cpms-pmax-too-low-thresholds` | 1 | 12 B | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `3cc4ffff3cc4ffff3cc4ffff` |
| `cpms-policy-type` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x2` |
| `cpms-syscap-filter-constants` | 1 | 24 B | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `00000000000000000080020000800000…` |
| `cpms-use-centralized-data` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x1` |
| `cpms-use-lpem-data` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x1` |
| `cpu-amx-mem-llc-ld-e-ki-dn` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x20000` |
| `cpu-amx-mem-llc-ld-e-ki-up` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x140000` |
| `cpu-amx-mem-llc-ld-e-target` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x147b` |
| `cpu-amx-mem-llc-ld-max-rate-e` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0xb70` |
| `cpu-avg-limiter-input-tc` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0xf8` |
| `cpu-avg-limiter-ki` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x6b7b` |
| `cpu-avg-limiter-kp` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0xdd2f2` |
| `cpu-avg-limiter-target-tc` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x0` |
| `cpu-bg-limiter-enable` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x1` |
| `cpu-bg-limiter-target` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x6666` |
| `cpu-core-mask-raise-holdoff` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0xa` |
| `cpu-ctrl-filtered` | 1 | empty | [`/arm-io/sep`](../devicetree/root__arm-io__sep.md) = `` |
| `cpu-dither-res-e-ki-dn` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x38e2` |
| `cpu-dither-res-e-ki-up` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0xaaac` |
| `cpu-dither-res-e-target` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x1999` |
| `cpu-dither-res-p-ki-dn` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x38e2` |
| `cpu-dither-res-p-ki-up` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0xaaac` |
| `cpu-dither-res-p-target` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x1999` |
| `cpu-dynamic-control` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x1` |
| `cpu-dynamic-core-rotation-mode` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x2` |
| `cpu-e-step-down-delay-us` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x1f4` |
| `cpu-efficiency-ki-down` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x3333` |
| `cpu-efficiency-ki-up` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x1999` |
| `cpu-efficiency-kp-down` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x0` |
| `cpu-efficiency-kp-up` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x0` |
| `cpu-high-e-threshold-high-e` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x20000` |
| `cpu-high-e-threshold-high-p` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0xb0000` |
| `cpu-high-e-threshold-low-e` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x8000` |
| `cpu-high-e-threshold-low-p` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x50000` |
| `cpu-high-epi-threshold-low-e` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0xf5c` |
| `cpu-iblm-mode` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x3` |
| `cpu-id` | 6 | u32×6 | [`/cpus/cpu0`](../devicetree/root__cpus__cpu0.md) = `0x0`<br>[`/cpus/cpu1`](../devicetree/root__cpus__cpu1.md) = `0x1`<br>[`/cpus/cpu2`](../devicetree/root__cpus__cpu2.md) = `0x2`<br>[`/cpus/cpu3`](../devicetree/root__cpus__cpu3.md) = `0x3`<br>[`/cpus/cpu4`](../devicetree/root__cpus__cpu4.md) = `0x4` |
| `cpu-idle-time-grace-period` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x64` |
| `cpu-impl-reg` | 6 | 16 B×6 | [`/cpus/cpu0`](../devicetree/root__cpus__cpu0.md) = `00000510020000001090000000000000`<br>[`/cpus/cpu1`](../devicetree/root__cpus__cpu1.md) = `00001510020000001090000000000000`<br>[`/cpus/cpu2`](../devicetree/root__cpus__cpu2.md) = `00002510020000001090000000000000`<br>[`/cpus/cpu3`](../devicetree/root__cpus__cpu3.md) = `00003510020000001090000000000000`<br>[`/cpus/cpu4`](../devicetree/root__cpus__cpu4.md) = `00000511020000001090000000000000` |
| `cpu-io-lim-min-freq` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x1194` |
| `cpu-low-power-frequency-max` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x96c` |
| `cpu-lowpeak-limiter-input-tc` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x10` |
| `cpu-lowpeak-limiter-ki` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x71de7` |
| `cpu-lowpeak-limiter-kp` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x1cac1` |
| `cpu-lowpeak-limiter-target-tc` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x0` |
| `cpu-migr-delta-clear-threshold` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x0` |
| `cpu-migr-delta-set-threshold` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x1` |
| `cpu-migr-mask-update-interval` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x4` |
| `cpu-migr-pref-eligible-mask` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x3` |
| `cpu-perf-cnt-filter-tc-down` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0xa` |
| `cpu-perf-cnt-filter-tc-up` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0xa` |
| `cpu-perf-state0-index` | 1 | u32 | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0x2` |
| `cpu-power-gate-latency-ns` | 1 | u32 | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0xc350` |
| `cpu-power-zone-filter-tc-0` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x1d4c0` |
| `cpu-power-zone-target-0` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x190000` |
| `cpu-power-zone-target-offset-0` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x199a` |
| `cpu-pref-mask-update-interval` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x4` |
| `cpu-rot-pwr-disengage-thresh` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x18000` |
| `cpu-rot-pwr-engage-thresh` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x28000` |
| `cpu-sched-lat-nonui-ki-down` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0xe14` |
| `cpu-sched-lat-nonui-ki-up` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x1999` |
| `cpu-sched-lat-nonui-kp-down` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x0` |
| `cpu-sched-lat-nonui-kp-up` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0xae1` |
| `cpu-sched-lat-nonui-target` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0xfa0` |
| `cpu-sched-lat-ui-ki-down` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x3851` |
| `cpu-sched-lat-ui-ki-up` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x6666` |
| `cpu-sched-lat-ui-kp-down` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x0` |
| `cpu-sched-lat-ui-kp-up` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x28f5` |
| `cpu-sched-lat-ui-target` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x3e8` |
| `cpu-upo-frequency-min-e` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x45c` |
| `cpu-util-sfi-min-on-percent` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x4000` |
| `cpu-utility-limiter-enable` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x1` |
| `cpu-utilization-control-mode` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x3` |
| `cpu-utilization-ki-down` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0xccc` |
| `cpu-utilization-ki-up` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0xa0000` |
| `cpu-utilization-kp-down` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x0` |
| `cpu-utilization-kp-up` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x0` |
| `cpu-utilization-spl-ki-down-c0` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0xf5c` |
| `cpu-utilization-spl-ki-down-c1` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0xf5c` |
| `cpu-utilization-spl-ki-down-c2` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0xe14` |
| `cpu-utilization-spl-ki-down-c3` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0xe14` |
| `cpu-utilization-spl-ki-down-c4` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x3333` |
| `cpu-utilization-spl-ki-down-t1` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x3645` |
| `cpu-utilization-spl-ki-down-t2` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x472b` |
| `cpu-utilization-spl-ki-down-t3` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0xcccc` |
| `cpu-utilization-spl-ki-up-c0` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x150000` |
| `cpu-utilization-spl-ki-up-c1` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0xfd70` |
| `cpu-utilization-spl-ki-up-c2` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x122831` |
| `cpu-utilization-spl-ki-up-c3` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x32ed9` |
| `cpu-utilization-spl-ki-up-c4` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x1999` |
| `cpu-utilization-spl-ki-up-t1` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x2fdf` |
| `cpu-utilization-spl-ki-up-t2` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x4000` |
| `cpu-utilization-spl-ki-up-t3` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0xcccc` |
| `cpu-utilization-target` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0xfd70` |
| `cpu-utilization-tier-mode` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x2` |
| `cpu-uttdbg-reg` | 6 | 16 B×6 | [`/cpus/cpu0`](../devicetree/root__cpus__cpu0.md) = `0000041002000000c800000000000000`<br>[`/cpus/cpu1`](../devicetree/root__cpus__cpu1.md) = `0000141002000000c800000000000000`<br>[`/cpus/cpu2`](../devicetree/root__cpus__cpu2.md) = `0000241002000000c800000000000000`<br>[`/cpus/cpu3`](../devicetree/root__cpus__cpu3.md) = `0000341002000000c800000000000000`<br>[`/cpus/cpu4`](../devicetree/root__cpus__cpu4.md) = `0000041102000000c800000000000000` |
| `cpx-encryption-mode` | 1 | u32 | [`/defaults`](../devicetree/root__defaults.md) = `0x2` |
| `crashlog-non-fatal` | 1 | empty | [`/arm-io/ans/iop-ans-nub`](../devicetree/root__arm-io__ans__iop-ans-nub.md) = `` |
| `cryptex1-certificate-format` | 1 | string | [`/chosen`](../devicetree/root__chosen.md) = `x509` |
| `cryptex1-key-scheme` | 1 | string | [`/chosen`](../devicetree/root__chosen.md) = `rsa4096` |
| `crypto-hash-method` | 1 | string | [`/chosen`](../devicetree/root__chosen.md) = `sha2-384` |
| `cs-system-policy` | 1 | string | [`/chosen`](../devicetree/root__chosen.md) = `default` |
| `current-limit-threshold` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x5a3d7` |
| `current-limit-window-size` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x1e` |
| `current-observation-window-size` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x0` |
| `current-prediction-window-size` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x1e` |
| `dapf-instance-0` | 3 | 156 B×2, 624 B | [`/arm-io/dart-isp`](../devicetree/root__arm-io__dart-isp.md) = `00407080020000002341708002000000…`<br>[`/arm-io/dart-ane0`](../devicetree/root__arm-io__dart-ane0.md) = `00806181030000000380618103000000…`<br>[`/arm-io/dart-ane1`](../devicetree/root__arm-io__dart-ane1.md) = `00806181030000000380618103000000…` |
| `dart-options` | 23 | u32×23 | [`/arm-io/dart-sep`](../devicetree/root__arm-io__dart-sep.md) = `0x25`<br>[`/arm-io/dart-sio`](../devicetree/root__arm-io__dart-sio.md) = `0x25`<br>[`/arm-io/dart-sbr`](../devicetree/root__arm-io__dart-sbr.md) = `0xe5`<br>[`/arm-io/dart-usb0`](../devicetree/root__arm-io__dart-usb0.md) = `0x27`<br>[`/arm-io/dart-dcp`](../devicetree/root__arm-io__dart-dcp.md) = `0x65` |
| `darwinos-security-environment` | 1 | u32 | [`/chosen`](../devicetree/root__chosen.md) = `0x0` |
| `darwinos-userspace-reboot` | 1 | u32 | [`/chosen`](../devicetree/root__chosen.md) = `0x0` |
| `data-isolation` | 2 | u32×2 | [`/arm-io/gfx-asc/iop-gfx-nub`](../devicetree/root__arm-io__gfx-asc__iop-gfx-nub.md) = `0x1`<br>[`/arm-io/gfx1-asc/iop-gfx1-nub`](../devicetree/root__arm-io__gfx1-asc__iop-gfx1-nub.md) = `0x1` |
| `data-journaling` | 1 | empty | [`/defaults`](../devicetree/root__defaults.md) = `` |
| `data-sources` | 8 | 27 B, 48 B, 43 B | [`/arm-io/iop-audio-controller/audio-hp/audio-codec`](../devicetree/root__arm-io__iop-audio-controller__audio-hp__audio-codec.md) = `61327061080001000100010000000000…`<br>[`/arm-io/iop-audio-controller/audio-leap-internal-loopback/audio-leap-internal-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-leap-internal-loopback__audio-leap-internal-loopback.md) = `61327061020204000200010000000000…`<br>[`/arm-io/iop-audio-controller/audio-mca-loopback/audio-mca-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-mca-loopback__audio-mca-loopback.md) = `63327061020200000000010000000000…`<br>[`/arm-io/iop-audio-controller/audio-receiver/audio-receiver`](../devicetree/root__arm-io__iop-audio-controller__audio-receiver__audio-receiver.md) = `72327061000100000000010000000000…`<br>[`/arm-io/iop-audio-controller/audio-flicker/audio-flicker`](../devicetree/root__arm-io__iop-audio-controller__audio-flicker__audio-flicker.md) = `66327061020004000200010000000000…` |
| `DBVMax` | 1 | u32 | [`/exbright`](../devicetree/root__exbright.md) = `0x7ff` |
| `DBVMin` | 1 | u32 | [`/exbright`](../devicetree/root__exbright.md) = `0x75` |
| `dcp-brightness-node` | 3 | string×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `DCP`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `DCPSEC`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `DCPSEC` |
| `dcp-types` | 1 | u64 | [`/exbright`](../devicetree/root__exbright.md) = `0x100000000` |
| `dcs-bw-enable` | 1 | u32 | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0x1` |
| `dcs-bw-threshold-a` | 1 | 144 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `703d0c00010000000000000000000000…` |
| `dcs-bw-threshold-b` | 1 | 128 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `703d0c00010000000000000000000000…` |
| `dcs-bw-threshold-c` | 1 | 144 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `b81e0600010000000000000000000000…` |
| `dcs-channel-enable-mask` | 1 | u32 | [`/arm-io/mcc`](../devicetree/root__arm-io__mcc.md) = `0x3f` |
| `dcs-count-per-amcc` | 1 | u32 | [`/arm-io/mcc`](../devicetree/root__arm-io__mcc.md) = `0x6` |
| `dcs-reg-idx` | 1 | u32 | [`/arm-io/mcc`](../devicetree/root__arm-io__mcc.md) = `0x8` |
| `dcs-wr-bw-enable` | 1 | u32 | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0x1` |
| `dcs-wr-bw-threshold` | 1 | 64 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `14ee2c00000000000000000000000000…` |
| `dcs-wr-bw-threshold-c` | 1 | 64 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `c2751600000000000000000000000000…` |
| `dead-mappings` | 2 | 16 B×2 | [`/arm-io/dart-ane0`](../devicetree/root__arm-io__dart-ane0.md) = `00f0ffffff0300000010000000000000`<br>[`/arm-io/dart-ane1`](../devicetree/root__arm-io__dart-ane1.md) = `00f0ffffff0300000010000000000000` |
| `debug-enabled` | 1 | u32 | [`/chosen`](../devicetree/root__chosen.md) = `0x0` |
| `debug-wait-start` | 1 | u32 | [`/chosen/iBoot`](../devicetree/root__chosen__iBoot.md) = `0x0` |
| `decode-samples-per-second` | 1 | u32 | [`/arm-io/avd`](../devicetree/root__arm-io__avd.md) = `0x6dc0` |
| `decoding` | 1 | 48 B | [`/product/facetime`](../devicetree/root__product__facetime.md) = `400100000f00f000400100001e00f000…` |
| `default-apcie-options` | 2 | u32×2 | [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) = `0x72f40000`<br>[`/arm-io/apcie/pci-bridge1`](../devicetree/root__arm-io__apcie__pci-bridge1.md) = `0x72f40000` |
| `default-boot-ok` | 1 | u32 | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0x1` |
| `default-input-data-sources` | 1 | 32 B | [`/arm-io/iop-audio-controller/audio-hpdbg`](../devicetree/root__arm-io__iop-audio-controller__audio-hpdbg.md) = `6361706163616f63736f706362716573…` |
| `default-options` | 1 | u32 | [`/baseband`](../devicetree/root__baseband.md) = `0x4` |
| `default-tck` | 3 | u32×3 | [`/arm-io/aod2`](../devicetree/root__arm-io__aod2.md) = `0x1388`<br>[`/arm-io/aod3`](../devicetree/root__arm-io__aod3.md) = `0x64`<br>[`/arm-io/aod4`](../devicetree/root__arm-io__aod4.md) = `0x64` |
| `deferred-processing` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x1` |
| `delta-voltage-target-Pmax` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x4b` |
| `delta-voltage-target-Vdroop` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x19` |
| `dev-range` | 1 | u64 | [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) = `0xff00000000` |
| `development-cert` | 1 | u32 | [`/chosen`](../devicetree/root__chosen.md) = `0x0` |
| `device-color-policy` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x0` |
| `device-curr-used-timeout-ms` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x1388` |
| `device-imei` | 1 | 32 B | [`/baseband`](../devicetree/root__baseband.md) = `00000000000000000000000000000000…` |
| `device-mac-address` | 1 | string | [`/arm-io/usb-drd0`](../devicetree/root__arm-io__usb-drd0.md) = `macaddr/ethaddr,syscfg/EMac/6,zeroes/6` |
| `device-name` | 8 | string×8 | [`/arm-io/iop-audio-controller/audio-hp/audio-codec`](../devicetree/root__arm-io__iop-audio-controller__audio-hp__audio-codec.md) = `HPMic`<br>[`/arm-io/iop-audio-controller/audio-leap-internal-loopback/audio-leap-internal-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-leap-internal-loopback__audio-leap-internal-loopback.md) = `NonSecure MCA LEAP Loopback`<br>[`/arm-io/iop-audio-controller/audio-mca-loopback/audio-mca-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-mca-loopback__audio-mca-loopback.md) = `NonSecure MCA Loopback`<br>[`/arm-io/iop-audio-controller/audio-receiver/audio-receiver`](../devicetree/root__arm-io__iop-audio-controller__audio-receiver__audio-receiver.md) = `Receiver`<br>[`/arm-io/iop-audio-controller/audio-flicker/audio-flicker`](../devicetree/root__arm-io__iop-audio-controller__audio-flicker__audio-flicker.md) = `Flicker` |
| `device-perf-memory-class` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0xc` |
| `device-tree-tag` | 1 | string | [`/`](../devicetree/root.md) = `EmbeddedDeviceTrees-12661.52.3` |
| `device-type` | 1 | 24 B | [`/arm-io/sio`](../devicetree/root__arm-io__sio.md) = `49505364040000000000000052415564…` |
| `device-uid` | 8 | string×8 | [`/arm-io/iop-audio-controller/audio-hp/audio-codec`](../devicetree/root__arm-io__iop-audio-controller__audio-hp__audio-codec.md) = `HPMic`<br>[`/arm-io/iop-audio-controller/audio-leap-internal-loopback/audio-leap-internal-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-leap-internal-loopback__audio-leap-internal-loopback.md) = `NonSecure MCA LEAP Loopback`<br>[`/arm-io/iop-audio-controller/audio-mca-loopback/audio-mca-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-mca-loopback__audio-mca-loopback.md) = `NonSecure MCA Loopback`<br>[`/arm-io/iop-audio-controller/audio-receiver/audio-receiver`](../devicetree/root__arm-io__iop-audio-controller__audio-receiver__audio-receiver.md) = `Receiver`<br>[`/arm-io/iop-audio-controller/audio-flicker/audio-flicker`](../devicetree/root__arm-io__iop-audio-controller__audio-flicker__audio-flicker.md) = `Flicker` |
| `device-usage` | 10 | u32×10 | [`/arm-io/aop/iop-aop-nub/accel_1`](../devicetree/root__arm-io__aop__iop-aop-nub__accel_1.md) = `0x3`<br>[`/arm-io/aop/iop-aop-nub/gyro_1`](../devicetree/root__arm-io__aop__iop-aop-nub__gyro_1.md) = `0x9`<br>[`/arm-io/aop/iop-aop-nub/hgaccel_1`](../devicetree/root__arm-io__aop__iop-aop-nub__hgaccel_1.md) = `0x1e`<br>[`/arm-io/aop/iop-aop-nub/accel`](../devicetree/root__arm-io__aop__iop-aop-nub__accel.md) = `0x3`<br>[`/arm-io/aop/iop-aop-nub/hgaccel`](../devicetree/root__arm-io__aop__iop-aop-nub__hgaccel.md) = `0x1e` |
| `device-usage-page` | 10 | u32×10 | [`/arm-io/aop/iop-aop-nub/accel_1`](../devicetree/root__arm-io__aop__iop-aop-nub__accel_1.md) = `0xff00`<br>[`/arm-io/aop/iop-aop-nub/gyro_1`](../devicetree/root__arm-io__aop__iop-aop-nub__gyro_1.md) = `0xff00`<br>[`/arm-io/aop/iop-aop-nub/hgaccel_1`](../devicetree/root__arm-io__aop__iop-aop-nub__hgaccel_1.md) = `0xff00`<br>[`/arm-io/aop/iop-aop-nub/accel`](../devicetree/root__arm-io__aop__iop-aop-nub__accel.md) = `0xff00`<br>[`/arm-io/aop/iop-aop-nub/hgaccel`](../devicetree/root__arm-io__aop__iop-aop-nub__hgaccel.md) = `0xff00` |
| `device_type` | 354 | string×354 | [`/`](../devicetree/root.md) = `bootrom`<br>[`/cpus/cpu0`](../devicetree/root__cpus__cpu0.md) = `cpu`<br>[`/cpus/cpu1`](../devicetree/root__cpus__cpu1.md) = `cpu`<br>[`/cpus/cpu2`](../devicetree/root__cpus__cpu2.md) = `cpu`<br>[`/cpus/cpu3`](../devicetree/root__cpus__cpu3.md) = `cpu` |
| `devices` | 1 | 624 B | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `08000000000000000000000000000000…` |
| `dfp-endpoints` | 1 | string | [`/arm-io/display-crossbar0`](../devicetree/root__arm-io__display-crossbar0.md) = `atc0, lpdptx` |
| `diagnostic-data-partial-region` | 4 | u32×4 | [`/arm-io/i2c3/display-eeprom/display-eeprom-data`](../devicetree/root__arm-io__i2c3__display-eeprom__display-eeprom-data.md) = `0x0`<br>[`/arm-io/i2c3/display-eeprom-hi/display-eeprom-data-hi`](../devicetree/root__arm-io__i2c3__display-eeprom-hi__display-eeprom-data-hi.md) = `0x1`<br>[`/arm-io/i2c3/display-eeprom-2/display-eeprom-data-2`](../devicetree/root__arm-io__i2c3__display-eeprom-2__display-eeprom-data-2.md) = `0x0`<br>[`/arm-io/i2c3/display-eeprom-2-hi/display-eeprom-data-2-hi`](../devicetree/root__arm-io__i2c3__display-eeprom-2-hi__display-eeprom-data-2-hi.md) = `0x1` |
| `diagnostic-data-regions` | 4 | u32×4 | [`/arm-io/i2c3/display-eeprom/display-eeprom-data`](../devicetree/root__arm-io__i2c3__display-eeprom__display-eeprom-data.md) = `0x2`<br>[`/arm-io/i2c3/display-eeprom-hi/display-eeprom-data-hi`](../devicetree/root__arm-io__i2c3__display-eeprom-hi__display-eeprom-data-hi.md) = `0x2`<br>[`/arm-io/i2c3/display-eeprom-2/display-eeprom-data-2`](../devicetree/root__arm-io__i2c3__display-eeprom-2__display-eeprom-data-2.md) = `0x3`<br>[`/arm-io/i2c3/display-eeprom-2-hi/display-eeprom-data-2-hi`](../devicetree/root__arm-io__i2c3__display-eeprom-2-hi__display-eeprom-data-2-hi.md) = `0x3` |
| `diagnostic-mask-all` | 1 | string | [`/buttons`](../devicetree/root__buttons.md) = `voldown, volup, hold` |
| `dictation` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `die-ane-id` | 2 | u32×2 | [`/arm-io/ane0`](../devicetree/root__arm-io__ane0.md) = `0x0`<br>[`/arm-io/ane1`](../devicetree/root__arm-io__ane1.md) = `0x1` |
| `die-id` | 3 | u32×2, u64 | [`/chosen`](../devicetree/root__chosen.md) = `0x0`<br>[`/arm-io/ane0`](../devicetree/root__arm-io__ane0.md) = `0x0`<br>[`/arm-io/ane1`](../devicetree/root__arm-io__ane1.md) = `0x0` |
| `digitizer-location-id` | 3 | u32×3 | [`/arm-io/aop/iop-aop-nub/als2a`](../devicetree/root__arm-io__aop__iop-aop-nub__als2a.md) = `0x221`<br>[`/arm-io/aop/iop-aop-nub/als2b`](../devicetree/root__arm-io__aop__iop-aop-nub__als2b.md) = `0x221`<br>[`/arm-io/aop/iop-aop-nub/als`](../devicetree/root__arm-io__aop__iop-aop-nub__als.md) = `0x220` |
| `direction` | 16 | empty×16 | [`/arm-io/admac-base-ns/base-ns-adma-rx-2`](../devicetree/root__arm-io__admac-base-ns__base-ns-adma-rx-2.md) = ``<br>[`/arm-io/admac-base-ns/base-ns-adma-rx-3`](../devicetree/root__arm-io__admac-base-ns__base-ns-adma-rx-3.md) = ``<br>[`/arm-io/admac-base-ns/base-ns-adma-rx-4`](../devicetree/root__arm-io__admac-base-ns__base-ns-adma-rx-4.md) = ``<br>[`/arm-io/admac-base-ns/base-ns-adma-rx-5`](../devicetree/root__arm-io__admac-base-ns__base-ns-adma-rx-5.md) = ``<br>[`/arm-io/admac-base-ns/base-ns-adma-tx-7`](../devicetree/root__arm-io__admac-base-ns__base-ns-adma-tx-7.md) = `` |
| `disable-accessory-firmware` | 1 | u32 | [`/chosen`](../devicetree/root__chosen.md) = `0x0` |
| `disable-av-content-protection` | 1 | u32 | [`/chosen`](../devicetree/root__chosen.md) = `0x0` |
| `disable-transport-rm` | 1 | u32 | [`/chosen`](../devicetree/root__chosen.md) = `0x0` |
| `disp0_audio_ced_die0` | 2 | u32×2 | [`/ced-ssw/ced_tunable_mask`](../devicetree/root__ced-ssw__ced_tunable_mask.md) = `0x8`<br>[`/ced-ssw/ced_disable_mask`](../devicetree/root__ced-ssw__ced_disable_mask.md) = `0x4` |
| `disp0_audio_ced_die1` | 2 | u32×2 | [`/ced-ssw/ced_tunable_mask`](../devicetree/root__ced-ssw__ced_tunable_mask.md) = `0x24`<br>[`/ced-ssw/ced_disable_mask`](../devicetree/root__ced-ssw__ced_disable_mask.md) = `0x12` |
| `disp0_ced_die0` | 2 | u32×2 | [`/ced-ssw/ced_tunable_mask`](../devicetree/root__ced-ssw__ced_tunable_mask.md) = `0x12`<br>[`/ced-ssw/ced_disable_mask`](../devicetree/root__ced-ssw__ced_disable_mask.md) = `0x9` |
| `disp0_ced_die1` | 2 | u32×2 | [`/ced-ssw/ced_tunable_mask`](../devicetree/root__ced-ssw__ced_tunable_mask.md) = `0x2e`<br>[`/ced-ssw/ced_disable_mask`](../devicetree/root__ced-ssw__ced_disable_mask.md) = `0x17` |
| `dispext0_audio_ced_die0` | 2 | u32×2 | [`/ced-ssw/ced_tunable_mask`](../devicetree/root__ced-ssw__ced_tunable_mask.md) = `0xa`<br>[`/ced-ssw/ced_disable_mask`](../devicetree/root__ced-ssw__ced_disable_mask.md) = `0x5` |
| `dispext0_audio_ced_die1` | 2 | u32×2 | [`/ced-ssw/ced_tunable_mask`](../devicetree/root__ced-ssw__ced_tunable_mask.md) = `0x26`<br>[`/ced-ssw/ced_disable_mask`](../devicetree/root__ced-ssw__ced_disable_mask.md) = `0x13` |
| `dispext0_ced_die0` | 2 | u32×2 | [`/ced-ssw/ced_tunable_mask`](../devicetree/root__ced-ssw__ced_tunable_mask.md) = `0x14`<br>[`/ced-ssw/ced_disable_mask`](../devicetree/root__ced-ssw__ced_disable_mask.md) = `0xa` |
| `dispext0_ced_die1` | 2 | u32×2 | [`/ced-ssw/ced_tunable_mask`](../devicetree/root__ced-ssw__ced_tunable_mask.md) = `0x30`<br>[`/ced-ssw/ced_disable_mask`](../devicetree/root__ced-ssw__ced_disable_mask.md) = `0x18` |
| `dispext1_audio_ced_die0` | 2 | u32×2 | [`/ced-ssw/ced_tunable_mask`](../devicetree/root__ced-ssw__ced_tunable_mask.md) = `0xc`<br>[`/ced-ssw/ced_disable_mask`](../devicetree/root__ced-ssw__ced_disable_mask.md) = `0x6` |
| `dispext1_audio_ced_die1` | 2 | u32×2 | [`/ced-ssw/ced_tunable_mask`](../devicetree/root__ced-ssw__ced_tunable_mask.md) = `0x28`<br>[`/ced-ssw/ced_disable_mask`](../devicetree/root__ced-ssw__ced_disable_mask.md) = `0x14` |
| `dispext1_ced_die0` | 2 | u32×2 | [`/ced-ssw/ced_tunable_mask`](../devicetree/root__ced-ssw__ced_tunable_mask.md) = `0x16`<br>[`/ced-ssw/ced_disable_mask`](../devicetree/root__ced-ssw__ced_disable_mask.md) = `0xb` |
| `dispext1_ced_die1` | 2 | u32×2 | [`/ced-ssw/ced_tunable_mask`](../devicetree/root__ced-ssw__ced_tunable_mask.md) = `0x32`<br>[`/ced-ssw/ced_disable_mask`](../devicetree/root__ced-ssw__ced_disable_mask.md) = `0x19` |
| `dispext2_audio_ced_die0` | 2 | u32×2 | [`/ced-ssw/ced_tunable_mask`](../devicetree/root__ced-ssw__ced_tunable_mask.md) = `0xe`<br>[`/ced-ssw/ced_disable_mask`](../devicetree/root__ced-ssw__ced_disable_mask.md) = `0x7` |
| `dispext2_audio_ced_die1` | 2 | u32×2 | [`/ced-ssw/ced_tunable_mask`](../devicetree/root__ced-ssw__ced_tunable_mask.md) = `0x2a`<br>[`/ced-ssw/ced_disable_mask`](../devicetree/root__ced-ssw__ced_disable_mask.md) = `0x15` |
| `dispext2_ced_die0` | 2 | u32×2 | [`/ced-ssw/ced_tunable_mask`](../devicetree/root__ced-ssw__ced_tunable_mask.md) = `0x18`<br>[`/ced-ssw/ced_disable_mask`](../devicetree/root__ced-ssw__ced_disable_mask.md) = `0xc` |
| `dispext2_ced_die1` | 2 | u32×2 | [`/ced-ssw/ced_tunable_mask`](../devicetree/root__ced-ssw__ced_tunable_mask.md) = `0x34`<br>[`/ced-ssw/ced_disable_mask`](../devicetree/root__ced-ssw__ced_disable_mask.md) = `0x1a` |
| `dispext3_audio_ced_die0` | 2 | u32×2 | [`/ced-ssw/ced_tunable_mask`](../devicetree/root__ced-ssw__ced_tunable_mask.md) = `0x10`<br>[`/ced-ssw/ced_disable_mask`](../devicetree/root__ced-ssw__ced_disable_mask.md) = `0x8` |
| `dispext3_audio_ced_die1` | 2 | u32×2 | [`/ced-ssw/ced_tunable_mask`](../devicetree/root__ced-ssw__ced_tunable_mask.md) = `0x2c`<br>[`/ced-ssw/ced_disable_mask`](../devicetree/root__ced-ssw__ced_disable_mask.md) = `0x16` |
| `dispext3_ced_die0` | 2 | u32×2 | [`/ced-ssw/ced_tunable_mask`](../devicetree/root__ced-ssw__ced_tunable_mask.md) = `0x1a`<br>[`/ced-ssw/ced_disable_mask`](../devicetree/root__ced-ssw__ced_disable_mask.md) = `0xd` |
| `dispext3_ced_die1` | 2 | u32×2 | [`/ced-ssw/ced_tunable_mask`](../devicetree/root__ced-ssw__ced_tunable_mask.md) = `0x36`<br>[`/ced-ssw/ced_disable_mask`](../devicetree/root__ced-ssw__ced_disable_mask.md) = `0x1b` |
| `display-backlight-compensation` | 1 | string | [`/product`](../devicetree/root__product.md) = `syscfg/DBCl` |
| `display-boot-rotation` | 1 | u32 | [`/chosen`](../devicetree/root__chosen.md) = `0x0` |
| `display-corner-radius` | 4 | 16 B×2, u32, u64 | [`/chosen`](../devicetree/root__chosen.md) = `0x0`<br>[`/product`](../devicetree/root__product.md) = `0x10000003b`<br>[`/product/display0`](../devicetree/root__product__display0.md) = `000000410000004100006c4200006c42`<br>[`/product/display1`](../devicetree/root__product__display1.md) = `00005c4200005c4200005c4200005c42` |
| `display-default-color` | 3 | u32×3 | [`/arm-io/disp0`](../devicetree/root__arm-io__disp0.md) = `0x0`<br>[`/arm-io/dispsec`](../devicetree/root__arm-io__dispsec.md) = `0x0`<br>[`/arm-io/dispext0`](../devicetree/root__arm-io__dispext0.md) = `0x0` |
| `display-id` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x0`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x1`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x1` |
| `display-index` | 6 | u32×6 | [`/arm-io/i2c3/display-eeprom/display-eeprom-generic-data`](../devicetree/root__arm-io__i2c3__display-eeprom__display-eeprom-generic-data.md) = `0x0`<br>[`/arm-io/i2c3/display-eeprom-2/display-eeprom-generic-data-2`](../devicetree/root__arm-io__i2c3__display-eeprom-2__display-eeprom-generic-data-2.md) = `0x1`<br>[`/arm-io/exdisplaypipe`](../devicetree/root__arm-io__exdisplaypipe.md) = `0x0`<br>[`/arm-io/exdisplaypipe1`](../devicetree/root__arm-io__exdisplaypipe1.md) = `0x1`<br>[`/product/display0`](../devicetree/root__product__display0.md) = `0x0` |
| `display-mirroring` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `display-rotation` | 3 | u32×3 | [`/chosen`](../devicetree/root__chosen.md) = `0x0`<br>[`/product/display0`](../devicetree/root__product__display0.md) = `0x0`<br>[`/product/display1`](../devicetree/root__product__display1.md) = `0x10e` |
| `display-scale` | 3 | u32×3 | [`/chosen`](../devicetree/root__chosen.md) = `0x0`<br>[`/product/display0`](../devicetree/root__product__display0.md) = `0x3`<br>[`/product/display1`](../devicetree/root__product__display1.md) = `0x3` |
| `display-temp-compensation` | 1 | string | [`/product`](../devicetree/root__product.md) = `syscfg/DTCl` |
| `display-timing-info` | 1 | 32 B | [`/arm-io/dispext0`](../devicetree/root__arm-io__dispext0.md) = `00040000320000003300000032000000…` |
| `display-workgroup-interval` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `dma-channel` | 4 | u32×4 | [`/arm-io/admac-hp-mic-ec-proxy`](../devicetree/root__arm-io__admac-hp-mic-ec-proxy.md) = `0x4`<br>[`/arm-io/admac-speaker-tx-ec-proxy`](../devicetree/root__arm-io__admac-speaker-tx-ec-proxy.md) = `0x2`<br>[`/arm-io/admac-receiver-tx-ec-proxy`](../devicetree/root__arm-io__admac-receiver-tx-ec-proxy.md) = `0x3`<br>[`/arm-io/admac-sllb-ec-proxy`](../devicetree/root__arm-io__admac-sllb-ec-proxy.md) = `0x2` |
| `dma-channels` | 3 | 32 B×2, 64 B | [`/arm-io/spi1`](../devicetree/root__arm-io__spi1.md) = `16000000000000000000000080000000…`<br>[`/arm-io/dp-audio0`](../devicetree/root__arm-io__dp-audio0.md) = `00000000020000000000000000100000…`<br>[`/arm-io/dp-audio1`](../devicetree/root__arm-io__dp-audio1.md) = `00000000020000000000000000100000…` |
| `dma-controllers` | 3 | u32×2, 16 B | [`/arm-io/admac-dispint0-ced-ssw`](../devicetree/root__arm-io__admac-dispint0-ced-ssw.md) = `0x44414930`<br>[`/arm-io/admac-dispext0-ced-ssw`](../devicetree/root__arm-io__admac-dispext0-ced-ssw.md) = `0x44415830`<br>[`/arm-io/admac-aop-ced-ssw`](../devicetree/root__arm-io__admac-aop-ced-ssw.md) = `53534142534e41425353454c534e454c` |
| `dma-parent` | 3 | u32×3 | [`/arm-io/spi1`](../devicetree/root__arm-io__spi1.md) = `0x89`<br>[`/arm-io/dp-audio0`](../devicetree/root__arm-io__dp-audio0.md) = `0xf7`<br>[`/arm-io/dp-audio1`](../devicetree/root__arm-io__dp-audio1.md) = `0x11f` |
| `dma-provider-rx` | 8 | string×8 | [`/arm-io/iop-audio-controller/audio-hp`](../devicetree/root__arm-io__iop-audio-controller__audio-hp.md) = `base-s-adma-rx-4`<br>[`/arm-io/iop-audio-controller/audio-leap-internal-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-leap-internal-loopback.md) = `leap-ns-adma-rx-3`<br>[`/arm-io/iop-audio-controller/audio-mca-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-mca-loopback.md) = `base-ns-adma-rx-8`<br>[`/arm-io/iop-audio-controller/audio-flicker`](../devicetree/root__arm-io__iop-audio-controller__audio-flicker.md) = `base-ns-adma-rx-5`<br>[`/arm-io/iop-audio-controller/audio-s-leap-internal-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-s-leap-internal-loopback.md) = `leap-s-adma-rx-2` |
| `dma-provider-tx` | 7 | string×7 | [`/arm-io/iop-audio-controller/audio-leap-internal-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-leap-internal-loopback.md) = `leap-ns-adma-tx-3`<br>[`/arm-io/iop-audio-controller/audio-mca-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-mca-loopback.md) = `base-ns-adma-tx-8`<br>[`/arm-io/iop-audio-controller/audio-receiver`](../devicetree/root__arm-io__iop-audio-controller__audio-receiver.md) = `base-s-adma-tx-3`<br>[`/arm-io/iop-audio-controller/audio-s-leap-internal-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-s-leap-internal-loopback.md) = `leap-ns-adma-tx-2`<br>[`/arm-io/iop-audio-controller/lp-mic-injection-device`](../devicetree/root__arm-io__iop-audio-controller__lp-mic-injection-device.md) = `base-ns-adma-tx-7` |
| `dma-stream-type` | 16 | u32×16 | [`/arm-io/admac-base-ns/base-ns-adma-rx-2`](../devicetree/root__arm-io__admac-base-ns__base-ns-adma-rx-2.md) = `0x49534f43`<br>[`/arm-io/admac-base-ns/base-ns-adma-rx-3`](../devicetree/root__arm-io__admac-base-ns__base-ns-adma-rx-3.md) = `0x49534f43`<br>[`/arm-io/admac-base-ns/base-ns-adma-rx-4`](../devicetree/root__arm-io__admac-base-ns__base-ns-adma-rx-4.md) = `0x49534f43`<br>[`/arm-io/admac-base-ns/base-ns-adma-rx-5`](../devicetree/root__arm-io__admac-base-ns__base-ns-adma-rx-5.md) = `0x49534f43`<br>[`/arm-io/admac-base-ns/base-ns-adma-tx-7`](../devicetree/root__arm-io__admac-base-ns__base-ns-adma-tx-7.md) = `0x49534f43` |
| `dmashim` | 1 | 72 B | [`/arm-io/sio`](../devicetree/root__arm-io__sio.md) = `49505353000010a50200000000001000…` |
| `dock` | 1 | u32 | [`/arm-io/nub-spmi2/spmi-hpm0`](../devicetree/root__arm-io__nub-spmi2__spmi-hpm0.md) = `0x1c5` |
| `dock-connect-sleep-duration-ms` | 1 | u32 | [`/arm-io/rsm`](../devicetree/root__arm-io__rsm.md) = `0x0` |
| `dock-num` | 2 | u32×2 | [`/arm-io/smc/iop-smc-nub/smc-charger`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-charger.md) = `0x1`<br>[`/arm-io/smc/iop-smc-nub/smc-charger-util`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-charger-util.md) = `0x1` |
| `dock-remote-wake` | 1 | empty | [`/arm-io/usb-drd0/usb-drd0-port-hs`](../devicetree/root__arm-io__usb-drd0__usb-drd0-port-hs.md) = `` |
| `dock-wstat-mask` | 1 | u32 | [`/arm-io/dockchannel-uart`](../devicetree/root__arm-io__dockchannel-uart.md) = `0xfff` |
| `domain-id` | 1 | u32 | [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) = `0x0` |
| `dont-power-on` | 2 | empty×2 | [`/arm-io/ane0/iop-ane0-nub`](../devicetree/root__arm-io__ane0__iop-ane0-nub.md) = ``<br>[`/arm-io/ane1/iop-ane1-nub`](../devicetree/root__arm-io__ane1__iop-ane1-nub.md) = `` |
| `dot-pitch-float` | 2 | u32×2 | [`/arm-io/disp0`](../devicetree/root__arm-io__disp0.md) = `0x43e60000`<br>[`/arm-io/dispsec`](../devicetree/root__arm-io__dispsec.md) = `0x43d70000` |
| `dp-switch-dfp-endpoint` | 1 | u32 | [`/arm-io/atc0-dpphy`](../devicetree/root__arm-io__atc0-dpphy.md) = `0x0` |
| `dp-switch-dfp-port` | 1 | u32 | [`/arm-io/atc0-dpphy`](../devicetree/root__arm-io__atc0-dpphy.md) = `0x0` |
| `dp-switch-parent` | 2 | u32×2 | [`/arm-io/atc0-dpphy`](../devicetree/root__arm-io__atc0-dpphy.md) = `0xdb`<br>[`/arm-io/dcpext0`](../devicetree/root__arm-io__dcpext0.md) = `0xdb` |
| `dp-switch-ufp-endpoint` | 1 | u32 | [`/arm-io/dcpext0`](../devicetree/root__arm-io__dcpext0.md) = `0x1` |
| `dp-switch-ufp-port` | 1 | u32 | [`/arm-io/dcpext0`](../devicetree/root__arm-io__dcpext0.md) = `0x0` |
| `dp-training-table` | 1 | empty | [`/arm-io/atc-phy0`](../devicetree/root__arm-io__atc-phy0.md) = `` |
| `dp-training-table-hbr` | 1 | 64 B | [`/arm-io/atc-phy0`](../devicetree/root__arm-io__atc-phy0.md) = `24000000130400000b07000004090000…` |
| `dp-training-table-rbr` | 1 | 64 B | [`/arm-io/atc-phy0`](../devicetree/root__arm-io__atc-phy0.md) = `24000000130400000b07000004090000…` |
| `dpxbar-parent` | 1 | u32 | [`/arm-io/atc0-dpphy`](../devicetree/root__arm-io__atc0-dpphy.md) = `0xdc` |
| `dram-power-limit-spl-cpu-c0` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x10000` |
| `dram-power-limit-spl-cpu-c1` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x9999` |
| `dram-power-limit-spl-cpu-c2` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x4ccc` |
| `dram-power-limit-spl-cpu-c3` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x3333` |
| `dram-power-limit-spl-cpu-t1` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x4ccc` |
| `dram-power-limit-spl-cpu-t2` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0xcccc` |
| `dram-power-limit-spl-gpu-c0` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x10000` |
| `dram-power-limit-spl-gpu-c1` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x9999` |
| `dram-power-limit-spl-gpu-c2` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x4ccc` |
| `dram-power-limit-spl-gpu-c3` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x3333` |
| `dram-power-limit-spl-gpu-t1` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x4ccc` |
| `dram-power-limit-spl-gpu-t2` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0xcccc` |
| `dram-power-limit-spl-t0` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x0` |
| `dram-power-limit-spl-t3` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x10000` |
| `dram-saca-freqs` | 1 | 36 B | [`/arm-io/error-handler/sac-error-handler`](../devicetree/root__arm-io__error-handler__sac-error-handler.md) = `00000000000000000000000000000000…` |
| `dram-vendor` | 1 | 16 B | [`/chosen`](../devicetree/root__chosen.md) = `00000000000000000000000000000000` |
| `dram-vendor-id` | 1 | u32 | [`/chosen`](../devicetree/root__chosen.md) = `0x0` |
| `dramcfg-data` | 1 | u64 | [`/arm-io/mcc`](../devicetree/root__arm-io__mcc.md) = `0x5555534000000133` |
| `droop-Ps-threshold-factor` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x0` |
| `droop-Pu-threshold-factor` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x0` |
| `ds-max-factor-aab-off` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x3f4d4fdf`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x3f4d4fdf`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x3f4d4fdf` |
| `ds-max-factors` | 3 | 24 B×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `8fc2753eb81e053fb81e053fb81e053f…`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `8fc2753eb81e053fb81e053fb81e053f…`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `8fc2753eb81e053fb81e053fb81e053f…` |
| `ds-max-fall-time` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x41200000`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x41200000`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x41200000` |
| `ds-max-pivot` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x41f00000`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x41f00000`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x41f00000` |
| `ds-max-rise-time` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x40a00000`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x40a00000`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x40a00000` |
| `ds-max-rise-time-fast` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x40400000`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x40400000`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x40400000` |
| `ds-max-rise-time-fast-thr` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x3f7ae148`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x3f7ae148`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x3f7ae148` |
| `ds-max-thresholds` | 3 | 24 B×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0000803f0000f0410000164400007a44…`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0000803f0000f0410000164400007a44…`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0000803f0000f0410000164400007a44…` |
| `ds-min-factors` | 3 | 24 B×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0000803f000000400000c0400000c040…`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0000803f000000400000c0400000c040…`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0000803f000000400000c0400000c040…` |
| `ds-min-fall-time` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x41200000`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x41200000`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x41200000` |
| `ds-min-pivot` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x42e60000`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x42e60000`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x42e60000` |
| `ds-min-rise-time` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x40a00000`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x40a00000`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x40a00000` |
| `ds-min-thresholds` | 3 | 24 B×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0000a0400000f0410000c8420000fa43…`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0000a0400000f0410000c8420000fa43…`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0000a0400000f0410000c8420000fa43…` |
| `dsid_mgmt` | 1 | u32 | [`/arm-io/mcc`](../devicetree/root__arm-io__mcc.md) = `0x1` |
| `dvc-done-err-bits` | 1 | u32 | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0x9` |
| `dvfs-domain` | 1 | 112 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `01000000090000000000000044435300…` |
| `dvmr-agent` | 1 | 24 B | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0000000180020000494e56414c494400…` |
| `dynamic-Pmax-Vcut-enabled` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x1` |
| `dynamic-PMU-Vthr-enabled` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x1` |
| `e-apfs` | 1 | u32 | [`/filesystems`](../devicetree/root__filesystems.md) = `0x1` |
| `ean-storage-present` | 1 | empty | [`/defaults`](../devicetree/root__defaults.md) = `` |
| `edr-exit-seconds-per-stop` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x3f400000`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x3f400000`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x3f400000` |
| `edr-max-nits` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x44c80000`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x44c80000`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x44c80000` |
| `edr-potential-headroom` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x41000000`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x41000000`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x41000000` |
| `edr-reference-headroom` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x41400000`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x41400000`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x41400000` |
| `edr-seconds-per-stop` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x3dcccccd`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x3dcccccd`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x3dcccccd` |
| `edt-property-ver` | 1 | u32 | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0x2` |
| `eeprom-read-property` | 2 | string×2 | [`/arm-io/mtp/iop-mtp-nub/multi-touch2`](../devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch2.md) = `AppleDiagnosticDataDisplay`<br>[`/arm-io/mtp/iop-mtp-nub/multi-touch`](../devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch.md) = `AppleDiagnosticDataDisplay` |
| `effective-production-status-ap` | 1 | u32 | [`/chosen`](../devicetree/root__chosen.md) = `0x0` |
| `effective-production-status-sep` | 1 | u32 | [`/chosen`](../devicetree/root__chosen.md) = `0x0` |
| `effective-security-mode-ap` | 1 | u32 | [`/chosen`](../devicetree/root__chosen.md) = `0x0` |
| `effective-security-mode-sep` | 1 | u32 | [`/chosen`](../devicetree/root__chosen.md) = `0x0` |
| `en-peak-power-envelope` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x1` |
| `enable-actual-Ps-Calc` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x1` |
| `enable-aging-model` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x1` |
| `enable-coex0` | 2 | empty×2 | [`/arm-io/aop/iop-aop-nub/compass`](../devicetree/root__arm-io__aop__iop-aop-nub__compass.md) = ``<br>[`/arm-io/aop/iop-aop-nub/cma`](../devicetree/root__arm-io__aop__iop-aop-nub__cma.md) = `` |
| `enable-coex1` | 1 | empty | [`/arm-io/aop/iop-aop-nub/compass`](../devicetree/root__arm-io__aop__iop-aop-nub__compass.md) = `` |
| `enable-coex2` | 1 | empty | [`/arm-io/aop/iop-aop-nub/compass`](../devicetree/root__arm-io__aop__iop-aop-nub__compass.md) = `` |
| `enable-IR-compensation` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x1` |
| `enable-ptm` | 2 | empty, u32 | [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) = ``<br>[`/arm-io/apcie/pci-bridge1`](../devicetree/root__arm-io__apcie__pci-bridge1.md) = `0x1` |
| `enable-sw-drain` | 1 | u32 | [`/arm-io/dockchannel-uart`](../devicetree/root__arm-io__dockchannel-uart.md) = `0x1` |
| `enable_stop_clocks` | 1 | 288 B | [`/arm-io/cpu-debug-interface`](../devicetree/root__arm-io__cpu-debug-interface.md) = `0000288800000000ffff000000000000…` |
| `enabledChannels` | 1 | u32 | [`/product/audio`](../devicetree/root__product__audio.md) = `0xf` |
| `enclosure-material` | 1 | string | [`/chosen`](../devicetree/root__chosen.md) = `syscfg/EnMt` |
| `encoding` | 1 | 56 B | [`/product/facetime`](../devicetree/root__product__facetime.md) = `400100000f00f000400100001e00f000…` |
| `energy-adder` | 2 | u32×2 | [`/arm-io/disp0`](../devicetree/root__arm-io__disp0.md) = `0x13851`<br>[`/arm-io/dispsec`](../devicetree/root__arm-io__dispsec.md) = `0x287ae` |
| `energy-consumption-target` | 1 | 12 B | [`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `001b3749001b374900ba5b49` |
| `entangle-nonce` | 1 | empty | [`/defaults`](../devicetree/root__defaults.md) = `` |
| `eos-halley-config` | 1 | u32 | [`/arm-io/aop-spmi0/stockholm-spmi/stockholm`](../devicetree/root__arm-io__aop-spmi0__stockholm-spmi__stockholm.md) = `0x1` |
| `ephemeral-data-mode` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x0` |
| `ephemeral-storage` | 1 | u32 | [`/chosen`](../devicetree/root__chosen.md) = `0x0` |
| `epoch-bumps` | 1 | empty | [`/arm-io/sep/iop-sep-nub/Sandcat`](../devicetree/root__arm-io__sep__iop-sep-nub__Sandcat.md) = `` |
| `eps-dir-bitmap` | 1 | u32 | [`/arm-io/usb-drd0`](../devicetree/root__arm-io__usb-drd0.md) = `0x264` |
| `error-interrupts` | 5 | 60 B×5 | [`/arm-io/nub-spmi0`](../devicetree/root__arm-io__nub-spmi0.md) = `04010000050100000801000009010000…`<br>[`/arm-io/nub-spmi1`](../devicetree/root__arm-io__nub-spmi1.md) = `04010000050100000801000009010000…`<br>[`/arm-io/nub-spmi2`](../devicetree/root__arm-io__nub-spmi2.md) = `04010000050100000801000009010000…`<br>[`/arm-io/aop-spmi0`](../devicetree/root__arm-io__aop-spmi0.md) = `04010000050100000801000009010000…`<br>[`/arm-io/aop-spmi1`](../devicetree/root__arm-io__aop-spmi1.md) = `04010000050100000801000009010000…` |
| `error-reflector` | 23 | u64×23 | [`/arm-io/dart-sep`](../devicetree/root__arm-io__dart-sep.md) = `0x27f000000`<br>[`/arm-io/dart-sio`](../devicetree/root__arm-io__dart-sio.md) = `0x27f000000`<br>[`/arm-io/dart-sbr`](../devicetree/root__arm-io__dart-sbr.md) = `0x27f000000`<br>[`/arm-io/dart-usb0`](../devicetree/root__arm-io__dart-usb0.md) = `0x27f000000`<br>[`/arm-io/dart-dcp`](../devicetree/root__arm-io__dart-dcp.md) = `0x27f000000` |
| `event-logs` | 1 | 792 B | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) = `02000000010000002c04000002000000…` |
| `event-trigger-supported` | 1 | u32 | [`/arm-io/msg`](../devicetree/root__arm-io__msg.md) = `0x1` |
| `event_name-btn1` | 1 | string | [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) = `hold` |
| `event_name-btn3` | 1 | string | [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) = `action` |
| `event_name-btn4` | 1 | string | [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) = `capture` |
| `event_name-gpio11` | 1 | string | [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) = `charger` |
| `event_name-gpio16` | 1 | string | [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) = `wifibt` |
| `event_name-gpio6` | 1 | string | [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) = `baseband` |
| `event_name-mask15` | 1 | string | [`/arm-io/nub-gpio`](../devicetree/root__arm-io__nub-gpio.md) = `dock` |
| `event_name-mask16` | 1 | string | [`/arm-io/aop-gpio`](../devicetree/root__arm-io__aop-gpio.md) = `baseband` |
| `exclave-assigned` | 32 | empty×32 | [`/arm-io/aop-exclave-mailbox`](../devicetree/root__arm-io__aop-exclave-mailbox.md) = ``<br>[`/arm-io/aop-exclave-ioreporting`](../devicetree/root__arm-io__aop-exclave-ioreporting.md) = ``<br>[`/arm-io/aop2-exclave-mailbox`](../devicetree/root__arm-io__aop2-exclave-mailbox.md) = ``<br>[`/arm-io/esm`](../devicetree/root__arm-io__esm.md) = ``<br>[`/arm-io/dcp-exclave-mailbox`](../devicetree/root__arm-io__dcp-exclave-mailbox.md) = `` |
| `exclave-edk-service` | 25 | string×25 | [`/arm-io/aop-exclave-mailbox`](../devicetree/root__arm-io__aop-exclave-mailbox.md) = `com.apple.service.SecureRTBuddyAOP_EDK`<br>[`/arm-io/aop2-exclave-mailbox`](../devicetree/root__arm-io__aop2-exclave-mailbox.md) = `com.apple.service.SecureRTBuddyAOP2_EDK`<br>[`/arm-io/esm`](../devicetree/root__arm-io__esm.md) = `com.apple.service.ExclaveSEPManager_EDK`<br>[`/arm-io/dcp-exclave-mailbox`](../devicetree/root__arm-io__dcp-exclave-mailbox.md) = `com.apple.service.SecureRTBuddyDCP_EDK`<br>[`/arm-io/exdisplaypipe`](../devicetree/root__arm-io__exdisplaypipe.md) = `com.apple.service.EXDisplayPipeDriver_EDK_xnuproxy` |
| `exclave-endpoint` | 3 | u32×3 | [`/arm-io/aop-exclave-ioreporting`](../devicetree/root__arm-io__aop-exclave-ioreporting.md) = `0x4d`<br>[`/arm-io/dcp-exclave-ioreporting`](../devicetree/root__arm-io__dcp-exclave-ioreporting.md) = `0x4e`<br>[`/arm-io/dcpsec-exclave-ioreporting`](../devicetree/root__arm-io__dcpsec-exclave-ioreporting.md) = `0x99` |
| `exclave-io-ranges` | 1 | 112 B | [`/defaults`](../devicetree/root__defaults.md) = `000003d6020000000040000000000000…` |
| `exclave-proxy-parent` | 2 | u32×2 | [`/arm-io/ane0`](../devicetree/root__arm-io__ane0.md) = `0x156`<br>[`/arm-io/ane1`](../devicetree/root__arm-io__ane1.md) = `0x157` |
| `exclave-reg` | 2 | 16 B×2 | [`/arm-io/ane-exclave-proxy`](../devicetree/root__arm-io__ane-exclave-proxy.md) = `0000404f040000000080080000000000`<br>[`/arm-io/ane1-exclave-proxy`](../devicetree/root__arm-io__ane1-exclave-proxy.md) = `00004053040000000080080000000000` |
| `exclave-service` | 25 | string×25 | [`/arm-io/aop-exclave-mailbox`](../devicetree/root__arm-io__aop-exclave-mailbox.md) = `com.apple.service.SecureRTBuddyAOP`<br>[`/arm-io/aop2-exclave-mailbox`](../devicetree/root__arm-io__aop2-exclave-mailbox.md) = `com.apple.service.SecureRTBuddyAOP2`<br>[`/arm-io/esm`](../devicetree/root__arm-io__esm.md) = `com.apple.service.ExclaveSEPManager`<br>[`/arm-io/dcp-exclave-mailbox`](../devicetree/root__arm-io__dcp-exclave-mailbox.md) = `com.apple.service.SecureRTBuddyDCP`<br>[`/arm-io/exdisplaypipe`](../devicetree/root__arm-io__exdisplaypipe.md) = `com.apple.service.EXDisplayPipeDriver_xnuproxy` |
| `exclave-sid` | 10 | u32×4, 16 B×2, u64×2 | [`/arm-io/dart-sep`](../devicetree/root__arm-io__dart-sep.md) = `0x2`<br>[`/arm-io/dart-sbr`](../devicetree/root__arm-io__dart-sbr.md) = `01000000030000002b0000002d000000`<br>[`/arm-io/dart-dcp`](../devicetree/root__arm-io__dart-dcp.md) = `0x4`<br>[`/arm-io/dart-disp0`](../devicetree/root__arm-io__dart-disp0.md) = `0xf0000000e`<br>[`/arm-io/dart-dcpsec`](../devicetree/root__arm-io__dart-dcpsec.md) = `0x4` |
| `exclaves-enabled` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `ext-irq-reg-index` | 2 | u32×2 | [`/arm-io/aop`](../devicetree/root__arm-io__aop.md) = `0x4`<br>[`/arm-io/aop2`](../devicetree/root__arm-io__aop2.md) = `0x3` |
| `extended-otp-cal` | 1 | u32 | [`/arm-io/smc/iop-smc-nub/smc-ext-charger`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-ext-charger.md) = `0x1` |
| `external` | 1 | u32 | [`/arm-io/dispext0`](../devicetree/root__arm-io__dispext0.md) = `0x1` |
| `external-hdr` | 1 | empty | [`/product`](../devicetree/root__product.md) = `` |
| `external-index` | 1 | u32 | [`/arm-io/dcpext0/iop-dcpext0-nub`](../devicetree/root__arm-io__dcpext0__iop-dcpext0-nub.md) = `0x1` |
| `external-named-power-provider` | 3 | string×3 | [`/arm-io/iop-audio-controller/lp-mic-device`](../devicetree/root__arm-io__iop-audio-controller__lp-mic-device.md) = `AppleCS42L79Audio`<br>[`/arm-io/iop-audio-controller/lp-mic-io-buffer-device`](../devicetree/root__arm-io__iop-audio-controller__lp-mic-io-buffer-device.md) = `SharedDARTMapperProxy`<br>[`/arm-io/iop-audio-controller/siri-listening-device`](../devicetree/root__arm-io__iop-audio-controller__siri-listening-device.md) = `AppleCS42L79Audio` |
| `extint-baseaddress` | 1 | u32 | [`/arm-io/aic`](../devicetree/root__arm-io__aic.md) = `0x10000` |
| `extintrcfg-stride` | 1 | u32 | [`/arm-io/aic`](../devicetree/root__arm-io__aic.md) = `0x4a00` |
| `fab-compute-power-ratio-high` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x60000` |
| `fab-compute-power-ratio-low` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x40000` |
| `fab-compute-power-target-high` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x1999` |
| `fab-compute-power-target-low` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0xccc` |
| `fabric-mem-separation-max` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x3` |
| `fabric-perf-state-follows-accp` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x0` |
| `fabric-slice-fmt-ver` | 1 | u32 | [`/arm-io/aop/iop-aop-nub/aop-gapf-filters`](../devicetree/root__arm-io__aop__iop-aop-nub__aop-gapf-filters.md) = `0x1` |
| `fabric-slices` | 1 | 320 B | [`/arm-io/aop/iop-aop-nub/aop-gapf-filters`](../devicetree/root__arm-io__aop__iop-aop-nub__aop-gapf-filters.md) = `1f000000000000000000809302000000…` |
| `face-detection-support` | 2 | u32×2 | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) = `0x1`<br>[`/arm-io/isp`](../devicetree/root__arm-io__isp.md) = `0x1` |
| `factory_key_disable` | 1 | empty | [`/arm-io/sep/iop-sep-nub/Sandcat`](../devicetree/root__arm-io__sep__iop-sep-nub__Sandcat.md) = `` |
| `failsafe-category-0` | 2 | string×2 | [`/arm-io/dcp0-expert`](../devicetree/root__arm-io__dcp0-expert.md) = `displayInternalFailures`<br>[`/arm-io/dcpsec-expert`](../devicetree/root__arm-io__dcpsec-expert.md) = `displayInternalFailures` |
| `failsafe-category-1` | 2 | string×2 | [`/arm-io/dcp0-expert`](../devicetree/root__arm-io__dcp0-expert.md) = `sysClkInputFailures`<br>[`/arm-io/dcpsec-expert`](../devicetree/root__arm-io__dcpsec-expert.md) = `sysClkInputFailures` |
| `failsafe-category-2` | 2 | string×2 | [`/arm-io/dcp0-expert`](../devicetree/root__arm-io__dcp0-expert.md) = `alpdpMainLinkTrainingFailures`<br>[`/arm-io/dcpsec-expert`](../devicetree/root__arm-io__dcpsec-expert.md) = `alpdpMainLinkTrainingFailures` |
| `failsafe-category-3` | 2 | string×2 | [`/arm-io/dcp0-expert`](../devicetree/root__arm-io__dcp0-expert.md) = `alpdpAuxFailures`<br>[`/arm-io/dcpsec-expert`](../devicetree/root__arm-io__dcpsec-expert.md) = `alpdpAuxFailures` |
| `failsafe-category-4` | 2 | string×2 | [`/arm-io/dcp0-expert`](../devicetree/root__arm-io__dcp0-expert.md) = `alpdpMainLinkPayloadFailures`<br>[`/arm-io/dcpsec-expert`](../devicetree/root__arm-io__dcpsec-expert.md) = `alpdpMainLinkPayloadFailures` |
| `failsafe-category-5` | 2 | string×2 | [`/arm-io/dcp0-expert`](../devicetree/root__arm-io__dcp0-expert.md) = `alpdpMainLinkTimingFailures`<br>[`/arm-io/dcpsec-expert`](../devicetree/root__arm-io__dcpsec-expert.md) = `alpdpMainLinkTimingFailures` |
| `failsafe-category-6` | 2 | string×2 | [`/arm-io/dcp0-expert`](../devicetree/root__arm-io__dcp0-expert.md) = `mainLinkXsyncMismatchFailures`<br>[`/arm-io/dcpsec-expert`](../devicetree/root__arm-io__dcpsec-expert.md) = `mainLinkXsyncMismatchFailures` |
| `failsafe-category-7` | 2 | string×2 | [`/arm-io/dcp0-expert`](../devicetree/root__arm-io__dcp0-expert.md) = `noActionFailures`<br>[`/arm-io/dcpsec-expert`](../devicetree/root__arm-io__dcpsec-expert.md) = `noActionFailures` |
| `failsafe-telemetry-event` | 2 | string×2 | [`/arm-io/dcp0-expert`](../devicetree/root__arm-io__dcp0-expert.md) = `com.apple.display.HealthMonitor.DisplayFailsafeCategorizatio`<br>[`/arm-io/dcpsec-expert`](../devicetree/root__arm-io__dcpsec-expert.md) = `com.apple.display.HealthMonitor.DisplayFailsafeCategorizatio` |
| `fallback-table-high-temp` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x27` |
| `fallback-table-low-temp` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0xfffffff1` |
| `fallback-table-row-count` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0xb` |
| `fallback-table-timescales` | 1 | 12 B | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `000000000100000002000000` |
| `fast-die-ctrl-ce-map` | 2 | 88 B×2 | [`/arm-io/pmp/iop-pmp-nub/:borneo_h19a_0`](../devicetree/root__arm-io__pmp__iop-pmp-nub___borneo_h19a_0.md) = `01000000000000000000000001000000…`<br>[`/arm-io/pmp/iop-pmp-nub/:borneo_h19p_0`](../devicetree/root__arm-io__pmp__iop-pmp-nub___borneo_h19p_0.md) = `01000000000000000000000001000000…` |
| `fast-die-ctrl-ts` | 1 | u32 | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0x50000` |
| `fast-die-ctrl-ts-avg-temp` | 1 | u32 | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0x640000` |
| `fatal-interrupts` | 5 | u32×5 | [`/arm-io/nub-spmi0`](../devicetree/root__arm-io__nub-spmi0.md) = `0x119`<br>[`/arm-io/nub-spmi1`](../devicetree/root__arm-io__nub-spmi1.md) = `0x119`<br>[`/arm-io/nub-spmi2`](../devicetree/root__arm-io__nub-spmi2.md) = `0x119`<br>[`/arm-io/aop-spmi0`](../devicetree/root__arm-io__aop-spmi0.md) = `0x119`<br>[`/arm-io/aop-spmi1`](../devicetree/root__arm-io__aop-spmi1.md) = `0x119` |
| `fdr-class` | 1 | u32 | [`/exbright`](../devicetree/root__exbright.md) = `0x1` |
| `fdr-classes` | 3 | string×3 | [`/arm-io/mtp/iop-mtp-nub`](../devicetree/root__arm-io__mtp__iop-mtp-nub.md) = `TBCl/MdTh, nova-touch-cal, TBCl/NvFc, nova-force-cal`<br>[`/arm-io/mtp/iop-mtp-nub/multi-touch2`](../devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch2.md) = `DspB/ADTN, adtn-calibration, DspB/CDTN, cdtn-calibration, Ds`<br>[`/arm-io/mtp/iop-mtp-nub/multi-touch`](../devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch.md) = `DspB/ADTN, adtn-calibration, DspB/CDTN, cdtn-calibration, Ds` |
| `fdr-data-identifier` | 2 | string×2 | [`/arm-io/mtp/iop-mtp-nub/multi-touch2`](../devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch2.md) = `DspB/ADTN, ZG:CoverGlassSerialNumberSecondary, DspB/CDTN, ZG`<br>[`/arm-io/mtp/iop-mtp-nub/multi-touch`](../devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch.md) = `DspB/ADTN, OWi11Urd09rDmPVy1z5dOQ, DspB/CDTN, OWi11Urd09rDmP` |
| `fdr-product-type` | 1 | string | [`/product`](../devicetree/root__product.md) = `iPhone19,4` |
| `feature-ldcm-arch-version` | 1 | u32 | [`/arm-io/nub-spmi2/spmi-hpm0`](../devicetree/root__arm-io__nub-spmi2__spmi-hpm0.md) = `0x5` |
| `feature-ldcm-hw-version` | 1 | u32 | [`/arm-io/nub-spmi2/spmi-hpm0`](../devicetree/root__arm-io__nub-spmi2__spmi-hpm0.md) = `0x4` |
| `features-supported` | 2 | 12 B, u32 | [`/arm-io/nub-spmi2/spmi-hpm0`](../devicetree/root__arm-io__nub-spmi2__spmi-hpm0.md) = `010000000200000005000000`<br>[`/port-magsafe-1`](../devicetree/root__port-magsafe-1.md) = `0x1` |
| `find-my` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `firmware-name` | 5 | string×5 | [`/arm-io/aop/iop-aop-nub`](../devicetree/root__arm-io__aop__iop-aop-nub.md) = `v68aop`<br>[`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `t8160pmp`<br>[`/arm-io/smc/iop-smc-nub`](../devicetree/root__arm-io__smc__iop-smc-nub.md) = `t8160smc`<br>[`/arm-io/gfx-asc/iop-gfx-nub`](../devicetree/root__arm-io__gfx-asc__iop-gfx-nub.md) = `GFX`<br>[`/arm-io/gfx1-asc/iop-gfx1-nub`](../devicetree/root__arm-io__gfx1-asc__iop-gfx1-nub.md) = `GFX1` |
| `firmware-version` | 1 | 256 B | [`/chosen`](../devicetree/root__chosen.md) = `00000000000000000000000000000000…` |
| `first-bypass-sid` | 1 | u32 | [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) = `0x10` |
| `first-frame-response-threshold` | 2 | 20 B×2 | [`/arm-io/disp0`](../devicetree/root__arm-io__disp0.md) = `295c0f00d7a3100085eb110033331300…`<br>[`/arm-io/dispsec`](../devicetree/root__arm-io__dispsec.md) = `295c0f00d7a3100085eb110033331300…` |
| `flag-pmax-ilim` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x1` |
| `flags` | 15 | u32×15 | [`/arm-io/error-handler/amcc-error-handler`](../devicetree/root__arm-io__error-handler__amcc-error-handler.md) = `0x0`<br>[`/arm-io/error-handler/dcs-error-handler`](../devicetree/root__arm-io__error-handler__dcs-error-handler.md) = `0x0`<br>[`/arm-io/error-handler/pmgr-error-handler`](../devicetree/root__arm-io__error-handler__pmgr-error-handler.md) = `0x0`<br>[`/arm-io/error-handler/cllt-error-handler`](../devicetree/root__arm-io__error-handler__cllt-error-handler.md) = `0x0`<br>[`/arm-io/error-handler/sep-error-handler`](../devicetree/root__arm-io__error-handler__sep-error-handler.md) = `0x0` |
| `flash` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x1` |
| `Flicker` | 1 | u64 | [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) = `0x2000102` |
| `flicker-config` | 1 | u32 | [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) = `0x3` |
| `flush-by-dva` | 23 | u32×23 | [`/arm-io/dart-sep`](../devicetree/root__arm-io__dart-sep.md) = `0x1`<br>[`/arm-io/dart-sio`](../devicetree/root__arm-io__dart-sio.md) = `0x1`<br>[`/arm-io/dart-sbr`](../devicetree/root__arm-io__dart-sbr.md) = `0x1`<br>[`/arm-io/dart-usb0`](../devicetree/root__arm-io__dart-usb0.md) = `0x1`<br>[`/arm-io/dart-dcp`](../devicetree/root__arm-io__dart-dcp.md) = `0x1` |
| `flush-cache-on-panic` | 1 | u32 | [`/arm-io/mcc`](../devicetree/root__arm-io__mcc.md) = `0x0` |
| `fmic-mic` | 1 | u64 | [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) = `0x309020903` |
| `formula-max-nits` | 1 | u32 | [`/exbright`](../devicetree/root__exbright.md) = `0xcb20000` |
| `fp-identity-scrambler-version` | 1 | u32 | [`/defaults`](../devicetree/root__defaults.md) = `0x3` |
| `framebuffer-height` | 1 | u32 | [`/arm-io/dispext0`](../devicetree/root__arm-io__dispext0.md) = `0x870` |
| `framebuffer-identifier` | 3 | string×3 | [`/product`](../devicetree/root__product.md) = `1C896A2B-F0D7-405C-8D0F-66E4B80AD044`<br>[`/product/display0`](../devicetree/root__product__display0.md) = `1C896A2B-F0D7-405C-8D0F-66E4B80AD044`<br>[`/product/display1`](../devicetree/root__product__display1.md) = `BF0DC480-5EE2-4EC1-B02B-C75E94759832` |
| `framebuffer-width` | 1 | u32 | [`/arm-io/dispext0`](../devicetree/root__arm-io__dispext0.md) = `0x1000` |
| `free-running-counter` | 1 | 32 B | [`/arm-io/soc-reporter`](../devicetree/root__arm-io__soc-reporter.md) = `01000206040000001f000000a0090000…` |
| `front-auto-focus` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x1` |
| `front-auto-hdr` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x1` |
| `front-burst` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x1` |
| `front-burst-image-duration` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x64` |
| `front-cam-offset-from-center` | 3 | 20 B×3 | [`/product`](../devicetree/root__product.md) = `c5050100ad1c000075150000e8030000…`<br>[`/product/display0`](../devicetree/root__product__display0.md) = `66bc000010770000560e0000e8030000…`<br>[`/product/display1`](../devicetree/root__product__display1.md) = `a617010066bc0000560e0000e8030000…` |
| `front-cam-rotation-isp` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0xb4` |
| `front-cam-superwide-capability` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x1` |
| `front-flash-capability` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x1` |
| `front-hdr` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x1` |
| `front-hdr-on` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x1` |
| `front-low-light-photo` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x1` |
| `front-max-burst-length` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x258` |
| `front-max-slomo-video-fps-1080p` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x78` |
| `front-max-slomo-video-fps-720p` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x78` |
| `front-max-video-fps-1080p` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x3c` |
| `front-max-video-fps-4k` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x3c` |
| `front-max-video-fps-720p` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x3c` |
| `front-max-video-zoom` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x1` |
| `front-slowmo` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x1` |
| `front-stage-light-portrait` | 1 | empty | [`/product/camera`](../devicetree/root__product__camera.md) = `` |
| `front-variable-frame-rate` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x1` |
| `function-amcc-sram-eventhandler` | 1 | u64 | [`/arm-io/error-handler`](../devicetree/root__arm-io__error-handler.md) = `0x4d24445300000036` |
| `function-ane0_power_func` | 1 | u64 | [`/arm-io/spi1/mesa`](../devicetree/root__arm-io__spi1__mesa.md) = `0x414e50570000013e` |
| `function-ane1_data_param_get` | 2 | u64×2 | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) = `0x644765740000014a`<br>[`/arm-io/isp`](../devicetree/root__arm-io__isp.md) = `0x644765740000014a` |
| `function-ane1_data_param_set` | 2 | u64×2 | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) = `0x645365740000014a`<br>[`/arm-io/isp`](../devicetree/root__arm-io__isp.md) = `0x645365740000014a` |
| `function-ane1_ep_control` | 2 | u64×2 | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) = `0x6543746c0000014a`<br>[`/arm-io/isp`](../devicetree/root__arm-io__isp.md) = `0x6543746c0000014a` |
| `function-ane1_power_func` | 3 | u64×3 | [`/arm-io/spi1/mesa`](../devicetree/root__arm-io__spi1__mesa.md) = `0x414e50570000014a`<br>[`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) = `0x414e50570000014a`<br>[`/arm-io/isp`](../devicetree/root__arm-io__isp.md) = `0x414e50570000014a` |
| `function-ane_data_param_get` | 2 | u64×2 | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) = `0x644765740000013e`<br>[`/arm-io/isp`](../devicetree/root__arm-io__isp.md) = `0x644765740000013e` |
| `function-ane_data_param_set` | 2 | u64×2 | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) = `0x645365740000013e`<br>[`/arm-io/isp`](../devicetree/root__arm-io__isp.md) = `0x645365740000013e` |
| `function-ane_ep_control` | 2 | u64×2 | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) = `0x6543746c0000013e`<br>[`/arm-io/isp`](../devicetree/root__arm-io__isp.md) = `0x6543746c0000013e` |
| `function-ane_perf_ctr` | 1 | u64 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x414e43520000013e` |
| `function-ane_perf_ctr1` | 1 | u64 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x414e43520000014a` |
| `function-ane_power_func` | 3 | u64×3 | [`/arm-io/spi1/mesa`](../devicetree/root__arm-io__spi1__mesa.md) = `0x414e50570000013e`<br>[`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) = `0x414e50570000013e`<br>[`/arm-io/isp`](../devicetree/root__arm-io__isp.md) = `0x414e50570000013e` |
| `function-aod_swclk` | 3 | 16 B×3 | [`/arm-io/aod2`](../devicetree/root__arm-io__aod2.md) = `350000004f4950476800000001010000`<br>[`/arm-io/aod3`](../devicetree/root__arm-io__aod3.md) = `730000004f4950470500000000010000`<br>[`/arm-io/aod4`](../devicetree/root__arm-io__aod4.md) = `350000004f4950476800000001010000` |
| `function-aod_swdio` | 3 | 16 B×3 | [`/arm-io/aod2`](../devicetree/root__arm-io__aod2.md) = `350000004f4950476200000000010000`<br>[`/arm-io/aod3`](../devicetree/root__arm-io__aod3.md) = `730000004f4950470800000001010000`<br>[`/arm-io/aod4`](../devicetree/root__arm-io__aod4.md) = `350000004f4950476200000000010000` |
| `function-avoid_perf_state` | 1 | u64 | [`/arm-io/error-handler/sac-error-handler`](../devicetree/root__arm-io__error-handler__sac-error-handler.md) = `0x4150524600000030` |
| `function-bb_on` | 1 | 20 B | [`/baseband`](../devicetree/root__baseband.md) = `9f00000038574b704f49637000008000…` |
| `function-bb_warm_reset` | 1 | 16 B | [`/baseband`](../devicetree/root__baseband.md) = `9f00000034574b70696c706200000000` |
| `function-boot_measurements` | 2 | 16 B×2 | [`/arm-io/aop-spmi0/stockholm-spmi/stockholm`](../devicetree/root__arm-io__aop-spmi0__stockholm-spmi__stockholm.md) = `350000004f4950476900000001010000`<br>[`/arm-io/aop-spmi0/hammerfest-spmi/hammerfest`](../devicetree/root__arm-io__aop-spmi0__hammerfest-spmi__hammerfest.md) = `350000004f4950478300000001010000` |
| `function-btm-config` | 1 | u64 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x424d434f000000c9` |
| `function-btm-config-battfw` | 1 | u64 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x424d4331000000c9` |
| `function-btm-start` | 1 | u64 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x424d5354000000c9` |
| `function-btm-stop` | 1 | u64 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x424d5350000000c9` |
| `function-btm-vthr` | 1 | u64 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x424d5654000000c9` |
| `function-button_hold` | 1 | 12 B | [`/buttons`](../devicetree/root__buttons.md) = `9f000000526e7462444c4862` |
| `function-button_voldown` | 1 | 12 B | [`/buttons`](../devicetree/root__buttons.md) = `9f000000526e74624e445662` |
| `function-button_volup` | 1 | 12 B | [`/buttons`](../devicetree/root__buttons.md) = `9f000000526e746250555662` |
| `function-clock_enable` | 2 | 20 B×2 | [`/arm-io/mtp/iop-mtp-nub/multi-touch2`](../devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch2.md) = `9f00000038574b704f49637000000008…`<br>[`/arm-io/mtp/iop-mtp-nub/multi-touch`](../devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch.md) = `9f00000038574b704f49637000000008…` |
| `function-clock_gate` | 1 | u64 | [`/arm-io`](../devicetree/root__arm-io.md) = `0x636c6b4700000030` |
| `function-clock_req_interrupt` | 1 | 20 B | [`/arm-io/ave`](../devicetree/root__arm-io__ave.md) = `30000000515249437300000023000000…` |
| `function-clpc_clvr_peek_0` | 1 | 16 B | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `a6000000506474705254307001000000` |
| `function-clpc_clvr_read_0` | 1 | 16 B | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `a6000000526474705254307001000080` |
| `function-cm_power_change_notify` | 2 | u64×2 | [`/arm-io/iop-audio-controller/lp-mic-device`](../devicetree/root__arm-io__iop-audio-controller__lp-mic-device.md) = `0x6c70736d000000b5`<br>[`/arm-io/iop-audio-controller/siri-listening-device`](../devicetree/root__arm-io__iop-audio-controller__siri-listening-device.md) = `0x6c706c73000000b5` |
| `function-conf_isp_ref0_clk_freq` | 1 | 20 B | [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) = `3000000043505349000000009e1ac155…` |
| `function-conf_isp_ref1_clk_freq` | 1 | 20 B | [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) = `3000000043505349010000009e1ac155…` |
| `function-conf_isp_ref2_clk_freq` | 1 | 20 B | [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) = `3000000043505349020000009e1ac155…` |
| `function-cpu_idle` | 6 | u64×6 | [`/cpus/cpu0`](../devicetree/root__cpus__cpu0.md) = `0x6370754900000030`<br>[`/cpus/cpu1`](../devicetree/root__cpus__cpu1.md) = `0x6370754900000030`<br>[`/cpus/cpu2`](../devicetree/root__cpus__cpu2.md) = `0x6370754900000030`<br>[`/cpus/cpu3`](../devicetree/root__cpus__cpu3.md) = `0x6370754900000030`<br>[`/cpus/cpu4`](../devicetree/root__cpus__cpu4.md) = `0x6370754900000030` |
| `function-current-read` | 1 | 20 B | [`/arm-io/mtp/iop-mtp-nub/nova`](../devicetree/root__arm-io__mtp__iop-mtp-nub__nova.md) = `9f00000038524b705348637000000022…` |
| `function-dart_force_active` | 2 | u64×2 | [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) = `0x46616374000001a5`<br>[`/arm-io/apcie/pci-bridge1`](../devicetree/root__arm-io__apcie__pci-bridge1.md) = `0x46616374000001ad` |
| `function-dart_release_sid` | 2 | u64×2 | [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) = `0x5352656c000001a5`<br>[`/arm-io/apcie/pci-bridge1`](../devicetree/root__arm-io__apcie__pci-bridge1.md) = `0x5352656c000001ad` |
| `function-dart_request_sid` | 2 | u64×2 | [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) = `0x53526571000001a5`<br>[`/arm-io/apcie/pci-bridge1`](../devicetree/root__arm-io__apcie__pci-bridge1.md) = `0x53526571000001ad` |
| `function-dart_self` | 2 | u64×2 | [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) = `0x53656c66000001a5`<br>[`/arm-io/apcie/pci-bridge1`](../devicetree/root__arm-io__apcie__pci-bridge1.md) = `0x53656c66000001ad` |
| `function-debug_gpio` | 1 | 16 B | [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) = `350000004f4950474000000001010000` |
| `function-device_reset` | 1 | 12 B | [`/arm-io/scaler0`](../devicetree/root__arm-io__scaler0.md) = `300000005453524111000000` |
| `function-dock_parent` | 4 | u64×4 | [`/arm-io/smc/iop-smc-nub/smc-charger`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-charger.md) = `0x61636350000001c5`<br>[`/arm-io/smc/iop-smc-nub/smc-ext-charger`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-ext-charger.md) = `0x61636350000001c6`<br>[`/arm-io/atc-phy0`](../devicetree/root__arm-io__atc-phy0.md) = `0x61636350000001c5`<br>[`/arm-io/usb-drd0`](../devicetree/root__arm-io__usb-drd0.md) = `0x61636350000001c5` |
| `function-dock_wired` | 1 | u64 | [`/arm-io/smc/iop-smc-nub/smc-ext-charger`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-ext-charger.md) = `0x61636350000001c5` |
| `function-enable` | 2 | 20 B, 16 B | [`/arm-io/aop-spmi0/stockholm-spmi/stockholm`](../devicetree/root__arm-io__aop-spmi0__stockholm-spmi__stockholm.md) = `9f00000038574b704f49637000008000…`<br>[`/arm-io/aop-spmi0/hammerfest-spmi/hammerfest`](../devicetree/root__arm-io__aop-spmi0__hammerfest-spmi__hammerfest.md) = `720000004f4950470600000001010000` |
| `function-enable_core` | 6 | 12 B×5, string | [`/cpus/cpu0`](../devicetree/root__cpus__cpu0.md) = `3000000065726f4301000000`<br>[`/cpus/cpu1`](../devicetree/root__cpus__cpu1.md) = `3000000065726f4302000000`<br>[`/cpus/cpu2`](../devicetree/root__cpus__cpu2.md) = `3000000065726f4304000000`<br>[`/cpus/cpu3`](../devicetree/root__cpus__cpu3.md) = `3000000065726f4308000000`<br>[`/cpus/cpu4`](../devicetree/root__cpus__cpu4.md) = `0, eroC@` |
| `function-error_detect` | 1 | 16 B | [`/centauri`](../devicetree/root__centauri.md) = `730000004f4950471600000000010000` |
| `function-error_handler` | 6 | 12 B×5, string | [`/cpus/cpu0`](../devicetree/root__cpus__cpu0.md) = `,, HrrE`<br>[`/cpus/cpu1`](../devicetree/root__cpus__cpu1.md) = `2c0000004872724501000000`<br>[`/cpus/cpu2`](../devicetree/root__cpus__cpu2.md) = `2c0000004872724502000000`<br>[`/cpus/cpu3`](../devicetree/root__cpus__cpu3.md) = `2c0000004872724503000000`<br>[`/cpus/cpu4`](../devicetree/root__cpus__cpu4.md) = `2c0000004872724506000000` |
| `function-external_standby` | 1 | 12 B | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `9f0000005779656b4553424d` |
| `function-flicker_bias` | 1 | u64 | [`/arm-io/aop/iop-aop-nub/grimaldi-control`](../devicetree/root__arm-io__aop__iop-aop-nub__grimaldi-control.md) = `0x666c6273000000b5` |
| `function-Flicker_master` | 1 | 12 B | [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) = `680100003144554166327061` |
| `function-get_pdod` | 1 | 12 B | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `9f0000005279656b31444442` |
| `function-get_valid_perf_states` | 4 | 16 B×4 | [`/arm-io/scaler0`](../devicetree/root__arm-io__scaler0.md) = `30000000474652502d00000002000000`<br>[`/arm-io/jpeg`](../devicetree/root__arm-io__jpeg.md) = `30000000474652502c00000002000000`<br>[`/arm-io/ave`](../devicetree/root__arm-io__ave.md) = `30000000474652502f00000002010000`<br>[`/arm-io/avd`](../devicetree/root__arm-io__avd.md) = `30000000474652502e00000002000000` |
| `function-get_vbus_detect` | 1 | 12 B | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `9f0000005279656b53554256` |
| `function-gnss-time-mark` | 1 | 16 B | [`/arm-io/aop/iop-aop-nub/gnss`](../devicetree/root__arm-io__aop__iop-aop-nub__gnss.md) = `720000004f4950470000000001010000` |
| `function-grimaldi-device-id` | 1 | u64 | [`/arm-io/grimaldi`](../devicetree/root__arm-io__grimaldi.md) = `0x646576490000006a` |
| `function-grimaldi-gain` | 1 | u64 | [`/arm-io/grimaldi`](../devicetree/root__arm-io__grimaldi.md) = `0x6761696e0000006a` |
| `function-grimaldi-power-get` | 1 | u64 | [`/arm-io/grimaldi`](../devicetree/root__arm-io__grimaldi.md) = `0x707772470000006a` |
| `function-grimaldi-power-set` | 1 | u64 | [`/arm-io/grimaldi`](../devicetree/root__arm-io__grimaldi.md) = `0x707772530000006a` |
| `function-hall_ctrl` | 2 | u64×2 | [`/arm-io/iop-audio-controller/audio-haptic`](../devicetree/root__arm-io__iop-audio-controller__audio-haptic.md) = `0x68616c6c000000b5`<br>[`/arm-io/iop-audio-controller/audio-hpdbg`](../devicetree/root__arm-io__iop-audio-controller__audio-hpdbg.md) = `0x68616c6c000000b5` |
| `function-haptics_session` | 1 | u64 | [`/arm-io/iop-audio-controller/audio-haptic`](../devicetree/root__arm-io__iop-audio-controller__audio-haptic.md) = `0x68707363000001b9` |
| `function-hid_event_dispatch` | 1 | u64 | [`/arm-io/spi1/mesa`](../devicetree/root__arm-io__spi1__mesa.md) = `0x42757444000001c4` |
| `function-ignore_vbus_drop` | 1 | u64 | [`/arm-io/nub-spmi2/spmi-hpm0`](../devicetree/root__arm-io__nub-spmi2__spmi-hpm0.md) = `0x69677662000001c5` |
| `function-input-data-selectors` | 1 | u64 | [`/arm-io/iop-audio-controller/audio-hpdbg`](../devicetree/root__arm-io__iop-audio-controller__audio-hpdbg.md) = `0x68646973000001b9` |
| `function-iommu_handler` | 4 | u64×4 | [`/arm-io/admac-hp-mic-ec-proxy`](../devicetree/root__arm-io__admac-hp-mic-ec-proxy.md) = `0x736470720000019d`<br>[`/arm-io/admac-speaker-tx-ec-proxy`](../devicetree/root__arm-io__admac-speaker-tx-ec-proxy.md) = `0x736470720000019d`<br>[`/arm-io/admac-receiver-tx-ec-proxy`](../devicetree/root__arm-io__admac-receiver-tx-ec-proxy.md) = `0x736470720000019d`<br>[`/arm-io/admac-sllb-ec-proxy`](../devicetree/root__arm-io__admac-sllb-ec-proxy.md) = `0x736470720000019d` |
| `function-jasper-sac` | 1 | 12 B | [`/baseband`](../devicetree/root__baseband.md) = `d301000043434153476d6163` |
| `function-link-data_enable` | 1 | u64 | [`/arm-io/smc/iop-smc-nub/smc-aop`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-aop.md) = `0x656e626c00000063` |
| `function-link-data_param_get` | 1 | u64 | [`/arm-io/smc/iop-smc-nub/smc-aop`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-aop.md) = `0x6461744700000063` |
| `function-link-data_param_set` | 1 | u64 | [`/arm-io/smc/iop-smc-nub/smc-aop`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-aop.md) = `0x6461745300000063` |
| `function-lostperf_report_write` | 1 | 16 B | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `a600000057647470504c534f02000000` |
| `function-mcc_dataset` | 8 | u64×8 | [`/arm-io/disp0`](../devicetree/root__arm-io__disp0.md) = `0x4d24445300000036`<br>[`/arm-io/dispsec`](../devicetree/root__arm-io__dispsec.md) = `0x4d24445300000036`<br>[`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) = `0x4d24445300000036`<br>[`/arm-io/ave`](../devicetree/root__arm-io__ave.md) = `0x4d24445300000036`<br>[`/arm-io/avd`](../devicetree/root__arm-io__avd.md) = `0x4d24445300000036` |
| `function-mesa_pwr` | 1 | 20 B | [`/arm-io/spi1/mesa`](../devicetree/root__arm-io__spi1__mesa.md) = `9f00000038574b70444c637000000000…` |
| `function-monitor-current-3v0` | 1 | 20 B | [`/arm-io/spi1/mesa`](../devicetree/root__arm-io__spi1__mesa.md) = `9f00000038524b70524344616c645049…` |
| `function-motion_data_enable` | 2 | u64×2 | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) = `0x656e626c0000005e`<br>[`/arm-io/isp`](../devicetree/root__arm-io__isp.md) = `0x656e626c0000005e` |
| `function-motion_data_param_get` | 2 | u64×2 | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) = `0x646174470000005e`<br>[`/arm-io/isp`](../devicetree/root__arm-io__isp.md) = `0x646174470000005e` |
| `function-motion_data_param_set` | 2 | u64×2 | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) = `0x646174530000005e`<br>[`/arm-io/isp`](../devicetree/root__arm-io__isp.md) = `0x646174530000005e` |
| `function-motion_state_set` | 2 | u64×2 | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) = `0x6d7374530000005e`<br>[`/arm-io/isp`](../devicetree/root__arm-io__isp.md) = `0x6d7374530000005e` |
| `function-over-current-detection` | 1 | 12 B | [`/arm-io/spi1/mesa`](../devicetree/root__arm-io__spi1__mesa.md) = `9f0000005279656b434f6d70` |
| `function-over-current-read` | 1 | 12 B | [`/arm-io/mtp/iop-mtp-nub/nova`](../devicetree/root__arm-io__mtp__iop-mtp-nub__nova.md) = `9f0000005279656b534d6d70` |
| `function-over-current-write` | 1 | 12 B | [`/arm-io/mtp/iop-mtp-nub/nova`](../devicetree/root__arm-io__mtp__iop-mtp-nub__nova.md) = `9f0000005779656b534d6d70` |
| `function-panic_notify` | 1 | 16 B | [`/arm-io/wdt`](../devicetree/root__arm-io__wdt.md) = `350000004f4950474000000000010000` |
| `function-parrot_srst` | 1 | u64 | [`/arm-io/usb-drd0`](../devicetree/root__arm-io__usb-drd0.md) = `0x70727374000001c5` |
| `function-pcie_port_control` | 2 | 12 B×2 | [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) = `9e010000437472509f010000`<br>[`/baseband`](../devicetree/root__baseband.md) = `9e01000043747250a3010000` |
| `function-pdm_rx_control` | 1 | u64 | [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) = `0x50444d6900000174` |
| `function-perst` | 2 | string×2 | [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) = `r, OIPGB`<br>[`/arm-io/apcie/pci-bridge1`](../devicetree/root__arm-io__apcie__pci-bridge1.md) = `r, OIPG@` |
| `function-pmp_control` | 1 | u64 | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0x504d504300000077` |
| `function-pmu_button` | 1 | u64 | [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) = `0x42757444000001c4` |
| `function-pmu_exton` | 1 | 20 B | [`/baseband`](../devicetree/root__baseband.md) = `9f00000038524b704f49637000000002…` |
| `function-pmu_exton_config` | 1 | 20 B | [`/baseband`](../devicetree/root__baseband.md) = `9f00000038574b704f49637000008007…` |
| `function-pmuaccess_L1DY` | 1 | u64 | [`/arm-io/pmgr/pmgrtools`](../devicetree/root__arm-io__pmgr__pmgrtools.md) = `0x706d7552000000c6` |
| `function-power` | 1 | 20 B | [`/arm-io/mtp/iop-mtp-nub/nova`](../devicetree/root__arm-io__mtp__iop-mtp-nub__nova.md) = `9f00000038574b70444c637000000000…` |
| `function-power_1v2_core` | 2 | 20 B×2 | [`/arm-io/mtp/iop-mtp-nub/multi-touch2`](../devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch2.md) = `9f00000038574b70444c637000000000…`<br>[`/arm-io/mtp/iop-mtp-nub/multi-touch`](../devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch.md) = `9f00000038574b70444c637000000000…` |
| `function-power_gate` | 1 | u64 | [`/arm-io`](../devicetree/root__arm-io.md) = `0x7077724700000030` |
| `function-power_peak_budget` | 1 | u64 | [`/arm-io/iop-audio-controller/audio-haptic`](../devicetree/root__arm-io__iop-audio-controller__audio-haptic.md) = `0x706b7077000001b9` |
| `function-ptd_lookup_mult` | 2 | u64×2 | [`/arm-io/mtp/iop-mtp-nub/mtp`](../devicetree/root__arm-io__mtp__iop-mtp-nub__mtp.md) = `0x70744d4c000000a6`<br>[`/arm-io/baseband-ptd`](../devicetree/root__arm-io__baseband-ptd.md) = `0x70744d4c000000a6` |
| `function-ptd_peek_mult` | 1 | u64 | [`/arm-io/baseband-ptd`](../devicetree/root__arm-io__baseband-ptd.md) = `0x70744d50000000a6` |
| `function-ptd_read_mult` | 2 | u64×2 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x70744d52000000a6`<br>[`/arm-io/baseband-ptd`](../devicetree/root__arm-io__baseband-ptd.md) = `0x70744d52000000a6` |
| `function-rd_rose_pwr` | 1 | 20 B | [`/arm-io/aop/iop-aop-nub/rose`](../devicetree/root__arm-io__aop__iop-aop-nub__rose.md) = `9f00000038524b70444c637000000000…` |
| `function-Receiver_master` | 1 | 12 B | [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) = `660100003144554172327061` |
| `function-reset` | 4 | 20 B×3, 16 B | [`/arm-io/mtp/iop-mtp-nub/multi-touch2`](../devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch2.md) = `9f00000038574b704f49637000000000…`<br>[`/arm-io/mtp/iop-mtp-nub/multi-touch`](../devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch.md) = `9f00000038574b704f49637000000000…`<br>[`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) = `720000004f4950475700000001000100`<br>[`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) = `9f00000038574b704f49637000008000…` |
| `function-reset_det` | 1 | 16 B | [`/baseband`](../devicetree/root__baseband.md) = `720000004f4950471000000000000000` |
| `function-rose_coredump` | 1 | 16 B | [`/arm-io/aop/iop-aop-nub/rose`](../devicetree/root__arm-io__aop__iop-aop-nub__rose.md) = `720000004f4950470c00000001010000` |
| `function-rose_pwr` | 1 | 20 B | [`/arm-io/aop/iop-aop-nub/rose`](../devicetree/root__arm-io__aop__iop-aop-nub__rose.md) = `9f00000038574b70444c637000000000…` |
| `function-rose_reset` | 1 | 20 B | [`/arm-io/aop/iop-aop-nub/rose`](../devicetree/root__arm-io__aop__iop-aop-nub__rose.md) = `9f00000038574b704f49637000008000…` |
| `function-rx` | 1 | 16 B | [`/arm-io/uart0`](../devicetree/root__arm-io__uart0.md) = `350000004f4950474300000002010000` |
| `function-sac` | 2 | 92 B, 12 B | [`/baseband`](../devicetree/root__baseband.md) = `d2010000434341533064636c3164636c…`<br>[`/centauri`](../devicetree/root__centauri.md) = `d2010000434341536d617264` |
| `function-saca` | 1 | 12 B | [`/arm-io/aop/iop-aop-nub/prox`](../devicetree/root__arm-io__aop__iop-aop-nub__prox.md) = `d201000041434153786f7270` |
| `function-saca0` | 2 | 12 B×2 | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) = `d201000041434153306d6163`<br>[`/arm-io/isp`](../devicetree/root__arm-io__isp.md) = `d201000041434153306d6163` |
| `function-saca0b` | 2 | 12 B×2 | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) = `d201000041434153326d6163`<br>[`/arm-io/isp`](../devicetree/root__arm-io__isp.md) = `d201000041434153326d6163` |
| `function-saca0c` | 2 | 12 B×2 | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) = `d201000041434153346d6163`<br>[`/arm-io/isp`](../devicetree/root__arm-io__isp.md) = `d201000041434153346d6163` |
| `function-saca0d` | 2 | 12 B×2 | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) = `d201000041434153416d6163`<br>[`/arm-io/isp`](../devicetree/root__arm-io__isp.md) = `d201000041434153416d6163` |
| `function-saca1` | 2 | 12 B×2 | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) = `d201000041434153316d6163`<br>[`/arm-io/isp`](../devicetree/root__arm-io__isp.md) = `d201000041434153316d6163` |
| `function-saca1b` | 2 | 12 B×2 | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) = `d201000041434153336d6163`<br>[`/arm-io/isp`](../devicetree/root__arm-io__isp.md) = `d201000041434153336d6163` |
| `function-saca1c` | 2 | 12 B×2 | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) = `d201000041434153356d6163`<br>[`/arm-io/isp`](../devicetree/root__arm-io__isp.md) = `d201000041434153356d6163` |
| `function-saca2` | 2 | 12 B×2 | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) = `d201000041434153366d6163`<br>[`/arm-io/isp`](../devicetree/root__arm-io__isp.md) = `d201000041434153366d6163` |
| `function-saca2b` | 2 | 12 B×2 | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) = `d201000041434153376d6163`<br>[`/arm-io/isp`](../devicetree/root__arm-io__isp.md) = `d201000041434153376d6163` |
| `function-saca2c` | 2 | 12 B×2 | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) = `d201000041434153386d6163`<br>[`/arm-io/isp`](../devicetree/root__arm-io__isp.md) = `d201000041434153386d6163` |
| `function-saca2d` | 2 | 12 B×2 | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) = `d201000041434153396d6163`<br>[`/arm-io/isp`](../devicetree/root__arm-io__isp.md) = `d201000041434153396d6163` |
| `function-saca3` | 2 | 12 B×2 | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) = `d201000041434153426d6163`<br>[`/arm-io/isp`](../devicetree/root__arm-io__isp.md) = `d201000041434153426d6163` |
| `function-saca3b` | 2 | 12 B×2 | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) = `d201000041434153436d6163`<br>[`/arm-io/isp`](../devicetree/root__arm-io__isp.md) = `d201000041434153436d6163` |
| `function-saca4` | 2 | 12 B×2 | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) = `d201000041434153446d6163`<br>[`/arm-io/isp`](../devicetree/root__arm-io__isp.md) = `d201000041434153446d6163` |
| `function-saca4b` | 2 | 12 B×2 | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) = `d201000041434153456d6163`<br>[`/arm-io/isp`](../devicetree/root__arm-io__isp.md) = `d201000041434153456d6163` |
| `function-saca4c` | 2 | 12 B×2 | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) = `d201000041434153466d6163`<br>[`/arm-io/isp`](../devicetree/root__arm-io__isp.md) = `d201000041434153466d6163` |
| `function-saca5` | 2 | 12 B×2 | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) = `d301000041434153476d6163`<br>[`/arm-io/isp`](../devicetree/root__arm-io__isp.md) = `d301000041434153476d6163` |
| `function-saca_dram` | 1 | 12 B | [`/arm-io/error-handler/sac-error-handler`](../devicetree/root__arm-io__error-handler__sac-error-handler.md) = `d2010000414341536d617264` |
| `function-saca_lcd0` | 2 | 12 B×2 | [`/arm-io/dcp-sac-controller`](../devicetree/root__arm-io__dcp-sac-controller.md) = `d2010000414341533064636c`<br>[`/arm-io/dcpsec-sac-controller`](../devicetree/root__arm-io__dcpsec-sac-controller.md) = `d2010000414341533264636c` |
| `function-saca_lcd1` | 2 | 12 B×2 | [`/arm-io/dcp-sac-controller`](../devicetree/root__arm-io__dcp-sac-controller.md) = `d2010000414341533164636c`<br>[`/arm-io/dcpsec-sac-controller`](../devicetree/root__arm-io__dcpsec-sac-controller.md) = `d2010000414341533364636c` |
| `function-se_boot_measurements` | 1 | 16 B | [`/arm-io/aop-spmi0/stockholm-spmi/stockholm`](../devicetree/root__arm-io__aop-spmi0__stockholm-spmi__stockholm.md) = `350000004f4950478000000001010000` |
| `function-send_disp_clock` | 1 | u64 | [`/arm-io/dispext0`](../devicetree/root__arm-io__dispext0.md) = `0x55507073000000e9` |
| `function-service_gate` | 1 | u64 | [`/arm-io`](../devicetree/root__arm-io.md) = `0x5345525600000030` |
| `function-service_reset` | 1 | u64 | [`/arm-io`](../devicetree/root__arm-io.md) = `0x5352535400000030` |
| `function-service_state` | 1 | u64 | [`/arm-io`](../devicetree/root__arm-io.md) = `0x5345524700000030` |
| `function-set_perf_state_floor` | 4 | 16 B×4 | [`/arm-io/scaler0`](../devicetree/root__arm-io__scaler0.md) = `30000000534652502d00000002000000`<br>[`/arm-io/jpeg`](../devicetree/root__arm-io__jpeg.md) = `30000000534652502c00000002000000`<br>[`/arm-io/ave`](../devicetree/root__arm-io__ave.md) = `30000000534652502f00000002010000`<br>[`/arm-io/avd`](../devicetree/root__arm-io__avd.md) = `30000000534652502e00000002000000` |
| `function-spi0_mosi_config` | 1 | 16 B | [`/arm-io/ans`](../devicetree/root__arm-io__ans.md) = `350000004f4950471500000001000100` |
| `function-spi0_sclk_config` | 1 | 16 B | [`/arm-io/ans`](../devicetree/root__arm-io__ans.md) = `350000004f4950471600000001000100` |
| `function-spi_cs0` | 1 | u64 | [`/arm-io/spi1`](../devicetree/root__arm-io__spi1.md) = `0x6e756c6c00000001` |
| `function-thermal_budget` | 1 | u64 | [`/arm-io/iop-audio-controller/audio-haptic`](../devicetree/root__arm-io__iop-audio-controller__audio-haptic.md) = `0x74686572000001b9` |
| `function-timestamp_sync` | 1 | 16 B | [`/arm-io/mt-bt-timestamp-sync`](../devicetree/root__arm-io__mt-bt-timestamp-sync.md) = `720000004f4950470900000002000002` |
| `function-tx` | 1 | 16 B | [`/arm-io/uart0`](../devicetree/root__arm-io__uart0.md) = `350000004f4950474200000002010000` |
| `function-vote_force_wakeup_dram` | 1 | string | [`/arm-io/usb-drd0`](../devicetree/root__arm-io__usb-drd0.md) = `H, DWFV` |
| `function-wait_for_power_gate` | 1 | 20 B | [`/arm-io/sep/iop-sep-nub`](../devicetree/root__arm-io__sep__iop-sep-nub.md) = `30000000746961570d00000000000000…` |
| `function-warm_reset` | 1 | 16 B | [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) = `9f00000034574b70696c706200000001` |
| `function_ptd_read_mult` | 1 | u64 | [`/arm-io/nub-spmi0/btm`](../devicetree/root__arm-io__nub-spmi0__btm.md) = `0x70744d52000000a6` |
| `fw-host-irq-address` | 2 | u32×2 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x2b08`<br>[`/arm-io/nub-spmi0/pmu-main/sgpio-bridge-pmu-main/pmu-secondary`](../devicetree/root__arm-io__nub-spmi0__pmu-main__sgpio-bridge-pmu-main__pmu-secondary.md) = `0x2b08` |
| `fw-mcom-address` | 2 | u32×2 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x2b60`<br>[`/arm-io/nub-spmi0/pmu-main/sgpio-bridge-pmu-main/pmu-secondary`](../devicetree/root__arm-io__nub-spmi0__pmu-main__sgpio-bridge-pmu-main__pmu-secondary.md) = `0x2b60` |
| `fw-mcom-int-index` | 2 | u32×2 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x1`<br>[`/arm-io/nub-spmi0/pmu-main/sgpio-bridge-pmu-main/pmu-secondary`](../devicetree/root__arm-io__nub-spmi0__pmu-main__sgpio-bridge-pmu-main__pmu-secondary.md) = `0x0` |
| `gapf-count` | 3 | u32×3 | [`/arm-io/dcp0-expert`](../devicetree/root__arm-io__dcp0-expert.md) = `0xf`<br>[`/arm-io/dcpsec-expert`](../devicetree/root__arm-io__dcpsec-expert.md) = `0xf`<br>[`/arm-io/dcpext0-expert`](../devicetree/root__arm-io__dcpext0-expert.md) = `0x2` |
| `gapf-reg-first-index` | 3 | u32×3 | [`/arm-io/dcp0-expert`](../devicetree/root__arm-io__dcp0-expert.md) = `0x1`<br>[`/arm-io/dcpsec-expert`](../devicetree/root__arm-io__dcpsec-expert.md) = `0x1`<br>[`/arm-io/dcpext0-expert`](../devicetree/root__arm-io__dcpext0-expert.md) = `0x1` |
| `gcp-supported` | 4 | u32×4 | [`/backlight`](../devicetree/root__backlight.md) = `0x1`<br>[`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x1`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x1`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x1` |
| `gen` | 5 | u32×5 | [`/arm-io/nub-spmi0`](../devicetree/root__arm-io__nub-spmi0.md) = `0x4`<br>[`/arm-io/nub-spmi1`](../devicetree/root__arm-io__nub-spmi1.md) = `0x4`<br>[`/arm-io/nub-spmi2`](../devicetree/root__arm-io__nub-spmi2.md) = `0x4`<br>[`/arm-io/aop-spmi0`](../devicetree/root__arm-io__aop-spmi0.md) = `0x4`<br>[`/arm-io/aop-spmi1`](../devicetree/root__arm-io__aop-spmi1.md) = `0x4` |
| `general-config` | 1 | u64 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x4000000c800` |
| `gfx-qos` | 1 | u64 | [`/arm-io/sgx`](../devicetree/root__arm-io__sgx.md) = `0x100000001` |
| `gfx-voter-agent-idx` | 1 | u32 | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0x2` |
| `gid-aes-key` | 1 | u32 | [`/chosen`](../devicetree/root__chosen.md) = `0x0` |
| `glb-time-source` | 1 | 12 B | [`/arm-io/soc-misc`](../devicetree/root__arm-io__soc-misc.md) = `000000000400000005000000` |
| `glitchless` | 6 | u32×6 | [`/arm-io/gpio0`](../devicetree/root__arm-io__gpio0.md) = `0x1`<br>[`/arm-io/aop-gpio`](../devicetree/root__arm-io__aop-gpio.md) = `0x1`<br>[`/arm-io/nub-gpio`](../devicetree/root__arm-io__nub-gpio.md) = `0x1`<br>[`/arm-io/smc-gpio`](../devicetree/root__arm-io__smc-gpio.md) = `0x1`<br>[`/arm-io/mtp-gpio`](../devicetree/root__arm-io__mtp-gpio.md) = `0x1` |
| `gnss-comms-interface` | 1 | u32 | [`/baseband`](../devicetree/root__baseband.md) = `0x2` |
| `gpio-iic_scl` | 3 | 12 B×3 | [`/arm-io/i2c2`](../devicetree/root__arm-io__i2c2.md) = `ca0000000201010041500000`<br>[`/arm-io/i2c3`](../devicetree/root__arm-io__i2c3.md) = `c80000000201010041500000`<br>[`/arm-io/i2c4`](../devicetree/root__arm-io__i2c4.md) = `d20000000201010041500000` |
| `gpio-iic_sda` | 3 | 12 B×3 | [`/arm-io/i2c2`](../devicetree/root__arm-io__i2c2.md) = `cb0000000201010041500000`<br>[`/arm-io/i2c3`](../devicetree/root__arm-io__i2c3.md) = `c90000000201010041500000`<br>[`/arm-io/i2c4`](../devicetree/root__arm-io__i2c4.md) = `d30000000201010041500000` |
| `gpio-repair_en` | 1 | 12 B | [`/arm-io/secure-repair`](../devicetree/root__arm-io__secure-repair.md) = `5a00000001010000414f5000` |
| `gps-capable` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `gpu-device-max-power` | 1 | u32 | [`/arm-io/sgx`](../devicetree/root__arm-io__sgx.md) = `0x1428` |
| `gpu-num-perf-states` | 1 | u32 | [`/arm-io/sgx`](../devicetree/root__arm-io__sgx.md) = `0x2` |
| `gpu-power-sample-period` | 1 | u32 | [`/arm-io/sgx`](../devicetree/root__arm-io__sgx.md) = `0x8` |
| `gpu-pwr-sample-period-aic-clks` | 1 | u32 | [`/arm-io/sgx`](../devicetree/root__arm-io__sgx.md) = `0x30d40` |
| `gpu-unified-budget-interface` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x1` |
| `graphics-featureset-class` | 1 | string | [`/product`](../devicetree/root__product.md) = `APPLE11` |
| `graphics-featureset-fallbacks` | 1 | string | [`/product`](../devicetree/root__product.md) = `APPLE10:APPLE9:APPLE8:APPLE7:APPLE6:APPLE5:APPLE4:APPLE3:APP` |
| `grimaldi-sampling-strategy` | 4 | u32×4 | [`/core-brightness`](../devicetree/root__core-brightness.md) = `0x1`<br>[`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x1`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x1`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x1` |
| `gs-b-min` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x3f666666`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x3f666666`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x3f666666` |
| `gs-i-nominal` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x3ea147ae`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x3f28f5c3`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x3f28f5c3` |
| `gs-i-threshold` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x3f83d70a`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x3f83d70a`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x3f83d70a` |
| `gs-pab-index` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x115`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x117`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x117` |
| `gs-slope` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x3f000000`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x3f000000`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x3f000000` |
| `gyro-interrupt-calibration` | 2 | string×2 | [`/arm-io/aop/iop-aop-nub/gyro_1`](../devicetree/root__arm-io__aop__iop-aop-nub__gyro_1.md) = `syscfg/G2CL`<br>[`/arm-io/aop/iop-aop-nub/gyro`](../devicetree/root__arm-io__aop__iop-aop-nub__gyro.md) = `syscfg/GICl` |
| `gyro-nominal-extr-cal` | 2 | string×2 | [`/arm-io/aop/iop-aop-nub/gyro_1`](../devicetree/root__arm-io__aop__iop-aop-nub__gyro_1.md) = `syscfg/GRXN,hex/02000201464D30692800000001000000000000000000`<br>[`/arm-io/aop/iop-aop-nub/gyro`](../devicetree/root__arm-io__aop__iop-aop-nub__gyro.md) = `syscfg/GRXN,hex/02000201464D30692800000001000000000000000000` |
| `gyro-orientation` | 2 | string×2 | [`/arm-io/aop/iop-aop-nub/gyro_1`](../devicetree/root__arm-io__aop__iop-aop-nub__gyro_1.md) = `syscfg/GRot`<br>[`/arm-io/aop/iop-aop-nub/gyro`](../devicetree/root__arm-io__aop__iop-aop-nub__gyro.md) = `syscfg/GRot` |
| `gyro-range-extr-cal` | 2 | string×2 | [`/arm-io/aop/iop-aop-nub/gyro_1`](../devicetree/root__arm-io__aop__iop-aop-nub__gyro_1.md) = `syscfg/G2XC`<br>[`/arm-io/aop/iop-aop-nub/gyro`](../devicetree/root__arm-io__aop__iop-aop-nub__gyro.md) = `syscfg/GRXC` |
| `gyro-range-intr-cal` | 2 | string×2 | [`/arm-io/aop/iop-aop-nub/gyro_1`](../devicetree/root__arm-io__aop__iop-aop-nub__gyro_1.md) = `syscfg/G2NC,hex/03000101464D30692C00000002000000A00F00000000`<br>[`/arm-io/aop/iop-aop-nub/gyro`](../devicetree/root__arm-io__aop__iop-aop-nub__gyro.md) = `syscfg/GRNC,hex/03000101524D30692C00000002000000A00F00000000` |
| `gyro-range-sensitivity-cal` | 2 | string×2 | [`/arm-io/aop/iop-aop-nub/gyro_1`](../devicetree/root__arm-io__aop__iop-aop-nub__gyro_1.md) = `syscfg/GRSC`<br>[`/arm-io/aop/iop-aop-nub/gyro`](../devicetree/root__arm-io__aop__iop-aop-nub__gyro.md) = `syscfg/GRSC` |
| `gyro-sensitivity-calibration` | 2 | string×2 | [`/arm-io/aop/iop-aop-nub/gyro_1`](../devicetree/root__arm-io__aop__iop-aop-nub__gyro_1.md) = `syscfg/GSCl`<br>[`/arm-io/aop/iop-aop-nub/gyro`](../devicetree/root__arm-io__aop__iop-aop-nub__gyro.md) = `syscfg/GSCl` |
| `gyro-temp-table` | 2 | string×2 | [`/arm-io/aop/iop-aop-nub/gyro_1`](../devicetree/root__arm-io__aop__iop-aop-nub__gyro_1.md) = `syscfg/G2TT`<br>[`/arm-io/aop/iop-aop-nub/gyro`](../devicetree/root__arm-io__aop__iop-aop-nub__gyro.md) = `syscfg/GYTT` |
| `h264-playback-level` | 1 | u32 | [`/arm-io/avd`](../devicetree/root__arm-io__avd.md) = `0x2a` |
| `Hall` | 1 | u64 | [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) = `0x2020102` |
| `halle-calibration` | 1 | string | [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) = `syscfg/PSCl,syscfg-mismatch/PSCl` |
| `hardware-version` | 1 | u32 | [`/arm-io/scaler0`](../devicetree/root__arm-io__scaler0.md) = `0x1b` |
| `has-applelpm` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `has-baseband` | 1 | empty | [`/arm-io/aop/iop-aop-nub`](../devicetree/root__arm-io__aop__iop-aop-nub.md) = `` |
| `has-boot-chime` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `has-espresso` | 1 | u32 | [`/arm-io/smc/iop-smc-nub/smc-ext-charger`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-ext-charger.md) = `0x1` |
| `has-exclaves` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `has-fw` | 2 | u32×2 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x1`<br>[`/arm-io/nub-spmi0/pmu-main/sgpio-bridge-pmu-main/pmu-secondary`](../devicetree/root__arm-io__nub-spmi0__pmu-main__sgpio-bridge-pmu-main__pmu-secondary.md) = `0x1` |
| `has-ironbull-camera-cloak` | 1 | u32 | [`/arm-io/smc/iop-smc-nub/smc-ext-charger`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-ext-charger.md) = `0x1` |
| `has-ironman-camera-cloak` | 1 | u32 | [`/arm-io/smc/iop-smc-nub/smc-ext-charger`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-ext-charger.md) = `0x1` |
| `has-ironman-charging` | 1 | u32 | [`/arm-io/smc/iop-smc-nub/smc-ext-charger`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-ext-charger.md) = `0x1` |
| `has-kf` | 1 | u32 | [`/arm-io/sgx`](../devicetree/root__arm-io__sgx.md) = `0x1` |
| `has-lpem-fw-scc` | 1 | u32 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x1` |
| `has-peripheral-logs` | 1 | u32 | [`/arm-io/smc/iop-smc-nub/smc-ext-charger`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-ext-charger.md) = `0x4` |
| `has-prox` | 2 | u32×2 | [`/product/display0`](../devicetree/root__product__display0.md) = `0x1`<br>[`/product/display1`](../devicetree/root__product__display1.md) = `0x0` |
| `has-sphere` | 2 | u32×2 | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) = `0x1`<br>[`/arm-io/isp`](../devicetree/root__arm-io__isp.md) = `0x1` |
| `hd-mic-coex` | 1 | u32 | [`/arm-io/smc/iop-smc-nub/smc-ext-charger`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-ext-charger.md) = `0x1` |
| `hdcp-channels` | 3 | u32×3 | [`/arm-io/dcp`](../devicetree/root__arm-io__dcp.md) = `0x5`<br>[`/arm-io/dcpsec`](../devicetree/root__arm-io__dcpsec.md) = `0x6`<br>[`/arm-io/dcpext0`](../devicetree/root__arm-io__dcpext0.md) = `0x7` |
| `hdcp-parent` | 3 | u32×3 | [`/arm-io/dcp`](../devicetree/root__arm-io__dcp.md) = `0x7e`<br>[`/arm-io/dcpsec`](../devicetree/root__arm-io__dcpsec.md) = `0x7e`<br>[`/arm-io/dcpext0`](../devicetree/root__arm-io__dcpext0.md) = `0x7e` |
| `hearingaid-audio-equalization` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `hearingaid-low-energy-audio` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `hid-merge-personality` | 4 | string×4 | [`/arm-io/mtp/iop-mtp-nub`](../devicetree/root__arm-io__mtp__iop-mtp-nub.md) = `MTP_SYS`<br>[`/arm-io/mtp/iop-mtp-nub/multi-touch2`](../devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch2.md) = `V68SS1`<br>[`/arm-io/mtp/iop-mtp-nub/multi-touch`](../devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch.md) = `V68PS1`<br>[`/arm-io/mtp/iop-mtp-nub/nova`](../devicetree/root__arm-io__mtp__iop-mtp-nub__nova.md) = `M1` |
| `hid-workgroup-interval` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `hidrm-enabled` | 1 | u32 | [`/defaults`](../devicetree/root__defaults.md) = `0x1` |
| `high-bandwidth-radio` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `historyChannels` | 1 | u32 | [`/product/audio`](../devicetree/root__product__audio.md) = `0xf` |
| `hme-in-arkit` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `hme-refresh-rate` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x55` |
| `home-button-type` | 1 | u32 | [`/buttons`](../devicetree/root__buttons.md) = `0x2` |
| `host` | 1 | string | [`/arm-io/grimaldi`](../devicetree/root__arm-io__grimaldi.md) = `AOP` |
| `host-mac-address` | 1 | string | [`/arm-io/usb-drd0`](../devicetree/root__arm-io__usb-drd0.md) = `macaddr/wifiaddr,syscfg/WMac/6,zeroes/6` |
| `host-os-information` | 1 | 128 B | [`/chosen`](../devicetree/root__chosen.md) = `00000000000000000000000000000000…` |
| `hotspot-center-x` | 3 | u32×3 | [`/arm-io/aop/iop-aop-nub/als2a`](../devicetree/root__arm-io__aop__iop-aop-nub__als2a.md) = `0x2c50000`<br>[`/arm-io/aop/iop-aop-nub/als2b`](../devicetree/root__arm-io__aop__iop-aop-nub__als2b.md) = `0x27f20000`<br>[`/arm-io/aop/iop-aop-nub/als`](../devicetree/root__arm-io__aop__iop-aop-nub__als.md) = `0x17370000` |
| `hotspot-center-y` | 3 | u32×3 | [`/arm-io/aop/iop-aop-nub/als2a`](../devicetree/root__arm-io__aop__iop-aop-nub__als2a.md) = `0x14c70000`<br>[`/arm-io/aop/iop-aop-nub/als2b`](../devicetree/root__arm-io__aop__iop-aop-nub__als2b.md) = `0x27430000`<br>[`/arm-io/aop/iop-aop-nub/als`](../devicetree/root__arm-io__aop__iop-aop-nub__als.md) = `0x2bd0000` |
| `housing-color` | 1 | string | [`/chosen`](../devicetree/root__chosen.md) = `syscfg/CLHS` |
| `hpm-class-type` | 1 | u32 | [`/arm-io/nub-spmi2/spmi-hpm0`](../devicetree/root__arm-io__nub-spmi2__spmi-hpm0.md) = `0xf` |
| `HPMic` | 1 | u64 | [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) = `0x4000100` |
| `hw-dpe-reg` | 1 | 440 B | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `09000000110100008001000000000000…` |
| `hw-name` | 2 | string×2 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `becketts`<br>[`/arm-io/nub-spmi0/pmu-main/sgpio-bridge-pmu-main/pmu-secondary`](../devicetree/root__arm-io__nub-spmi0__pmu-main__sgpio-bridge-pmu-main__pmu-secondary.md) = `fairmont` |
| `hw-type` | 1 | string | [`/arm-io/jpeg`](../devicetree/root__arm-io__jpeg.md) = `130000` |
| `hwintmon-stride` | 1 | u32 | [`/arm-io/aic`](../devicetree/root__arm-io__aic.md) = `0x4a00` |
| `iap2-protocol-supported` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `iboot-audio-volume` | 1 | u32 | [`/arm-io/iop-audio-controller/audio-speaker`](../devicetree/root__arm-io__iop-audio-controller__audio-speaker.md) = `0x7fff` |
| `iboot-auth` | 2 | empty×2 | [`/arm-io/i2c3/mogul-display`](../devicetree/root__arm-io__i2c3__mogul-display.md) = ``<br>[`/arm-io/i2c3/mogul-display2`](../devicetree/root__arm-io__i2c3__mogul-display2.md) = `` |
| `ic-auth-type` | 3 | u32×3 | [`/arm-io/i2c3/mogul-display`](../devicetree/root__arm-io__i2c3__mogul-display.md) = `0x30000`<br>[`/arm-io/i2c3/mogul-display2`](../devicetree/root__arm-io__i2c3__mogul-display2.md) = `0x30000`<br>[`/arm-io/i2c4/mogul-mlb`](../devicetree/root__arm-io__i2c4__mogul-mlb.md) = `0x40000` |
| `identifier` | 25 | u32×25 | [`/arm-io/iop-audio-controller/audio-hp`](../devicetree/root__arm-io__iop-audio-controller__audio-hp.md) = `0x68706169`<br>[`/arm-io/iop-audio-controller/audio-leap-internal-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-leap-internal-loopback.md) = `0x6c696c62`<br>[`/arm-io/iop-audio-controller/audio-mca-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-mca-loopback.md) = `0x6c70626b`<br>[`/arm-io/iop-audio-controller/audio-receiver`](../devicetree/root__arm-io__iop-audio-controller__audio-receiver.md) = `0x72656376`<br>[`/arm-io/iop-audio-controller/audio-flicker`](../devicetree/root__arm-io__iop-audio-controller__audio-flicker.md) = `0x666c636b` |
| `identity` | 3 | string×3 | [`/arm-io/admac-dispint0-ced-ssw`](../devicetree/root__arm-io__admac-dispint0-ced-ssw.md) = `DISP-I-ISOC`<br>[`/arm-io/admac-dispext0-ced-ssw`](../devicetree/root__arm-io__admac-dispext0-ced-ssw.md) = `DISP-E0-ISOC`<br>[`/arm-io/admac-aop-ced-ssw`](../devicetree/root__arm-io__admac-aop-ced-ssw.md) = `ADMAC-A` |
| `idle-ctrl-check` | 4 | empty×4 | [`/arm-io/aop2`](../devicetree/root__arm-io__aop2.md) = ``<br>[`/arm-io/dcp`](../devicetree/root__arm-io__dcp.md) = ``<br>[`/arm-io/dcpsec`](../devicetree/root__arm-io__dcpsec.md) = ``<br>[`/arm-io/dcpext0`](../devicetree/root__arm-io__dcpext0.md) = `` |
| `ie-fix` | 6 | u32×6 | [`/arm-io/gpio0`](../devicetree/root__arm-io__gpio0.md) = `0x1`<br>[`/arm-io/aop-gpio`](../devicetree/root__arm-io__aop-gpio.md) = `0x1`<br>[`/arm-io/nub-gpio`](../devicetree/root__arm-io__nub-gpio.md) = `0x1`<br>[`/arm-io/smc-gpio`](../devicetree/root__arm-io__smc-gpio.md) = `0x1`<br>[`/arm-io/mtp-gpio`](../devicetree/root__arm-io__mtp-gpio.md) = `0x1` |
| `ignore-gating` | 1 | empty | [`/arm-io/ans`](../devicetree/root__arm-io__ans.md) = `` |
| `ignore-link-speed-mismatch` | 1 | u32 | [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) = `0x1` |
| `ignore-secondary` | 2 | empty×2 | [`/arm-io/dart-isp`](../devicetree/root__arm-io__dart-isp.md) = ``<br>[`/arm-io/dart-avd`](../devicetree/root__arm-io__dart-avd.md) = `` |
| `ignore-sid-count-mismatch` | 1 | empty | [`/arm-io/dart-isp`](../devicetree/root__arm-io__dart-isp.md) = `` |
| `image-tag` | 4 | u32×4 | [`/arm-io/mtp/iop-mtp-nub`](../devicetree/root__arm-io__mtp__iop-mtp-nub.md) = `0x6d747066`<br>[`/arm-io/mtp/iop-mtp-nub/multi-touch2`](../devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch2.md) = `0x6d746677`<br>[`/arm-io/mtp/iop-mtp-nub/multi-touch`](../devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch.md) = `0x6d746677`<br>[`/arm-io/mtp/iop-mtp-nub/nova`](../devicetree/root__arm-io__mtp__iop-mtp-nub__nova.md) = `0x6d6e646f` |
| `image4-cert-type` | 1 | u32 | [`/chosen`](../devicetree/root__chosen.md) = `0x1` |
| `image4-supported` | 1 | empty | [`/chosen`](../devicetree/root__chosen.md) = `` |
| `imeisv` | 1 | u32 | [`/baseband`](../devicetree/root__baseband.md) = `0x4` |
| `imic-mic` | 1 | u64 | [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) = `0x307020701` |
| `index` | 16 | empty×16 | [`/arm-io/admac-base-ns/base-ns-adma-rx-2`](../devicetree/root__arm-io__admac-base-ns__base-ns-adma-rx-2.md) = ``<br>[`/arm-io/admac-base-ns/base-ns-adma-rx-3`](../devicetree/root__arm-io__admac-base-ns__base-ns-adma-rx-3.md) = ``<br>[`/arm-io/admac-base-ns/base-ns-adma-rx-4`](../devicetree/root__arm-io__admac-base-ns__base-ns-adma-rx-4.md) = ``<br>[`/arm-io/admac-base-ns/base-ns-adma-rx-5`](../devicetree/root__arm-io__admac-base-ns__base-ns-adma-rx-5.md) = ``<br>[`/arm-io/admac-base-ns/base-ns-adma-tx-7`](../devicetree/root__arm-io__admac-base-ns__base-ns-adma-tx-7.md) = `` |
| `info-clock_offset` | 1 | u64 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x600002100` |
| `info-fault_log` | 1 | u64 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x900001000` |
| `info-fault_name-10` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `ot,overtemp` |
| `info-fault_name-11` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `ov,vddmain_ovlo` |
| `info-fault_name-16` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `btn_rst,two_finger_rst` |
| `info-fault_name-17` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `crash,crash0_in` |
| `info-fault_name-18` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `btn_rst,btn_seq_reset` |
| `info-fault_name-19` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `btn_rst,sec_btn_seq` |
| `info-fault_name-20` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `wdog,reset_in_1` |
| `info-fault_name-21` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `dbg_rst,reset_in_2` |
| `info-fault_name-22` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `sochot,reset_in_3` |
| `info-fault_name-23` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `rst_in,reset_in_1_deassert` |
| `info-fault_name-24` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `spmi,spmi_fault` |
| `info-fault_name-25` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `ntc_shdn` |
| `info-fault_name-26` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `timeout,dblclick_timeout` |
| `info-fault_name-28` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `timeout,watchdog_timeout` |
| `info-fault_name-29` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `sstate,button_dfu_recover` |
| `info-fault_name-3` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `uv,vddmain_uvlo` |
| `info-fault_name-30` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `crash,crash1_in` |
| `info-fault_name-31` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `sstate,dfu_btn_seq_reset` |
| `info-fault_name-32` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `temp_abs_buck0` |
| `info-fault_name-33` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `temp_abs_buck1` |
| `info-fault_name-35` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `otp_crc` |
| `info-fault_name-36` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `sgpio` |
| `info-fault_name-37` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `btn_shdn` |
| `info-fault_name-38` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `xtal_wdog_expiry` |
| `info-fault_name-39` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `mfsm_sgpio` |
| `info-fault_name-40` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `crash,metis_fw_crash` |
| `info-fault_name-41` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `crash,metis_hw_crash` |
| `info-fault_name-42` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `timeout,target_st_wdog_timeout` |
| `info-fault_name-43` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `timeout,wdog_fw_timeout` |
| `info-fault_name-44` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `emerg_shdn` |
| `info-fault_name-5` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `uv,vdd_boost_uvlo` |
| `info-fault_name-50` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `target_off_restart` |
| `info-fault_name-51` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `target_off_shutdown` |
| `info-fault_name-52` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `target_off_conflict` |
| `info-fault_name-56` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `ot,tdie_overtemp_idx0` |
| `info-fault_name-57` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `ot,tdie_overtemp_idx1` |
| `info-fault_name-58` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `ot,tdie_overtemp_idx2` |
| `info-fault_name-59` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `ot,tdie_overtemp_idx3` |
| `info-fault_name-6` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `ov,vdd_boost_ovlo` |
| `info-fault_name-60` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `ot,tdie_overtemp_idx4` |
| `info-fault_name-61` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `ot,tdie_overtemp` |
| `info-fault_name-62` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `ov,ldo_ana_ovp` |
| `info-fault_name-63` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `ov,ldo_dig_ovp` |
| `info-fault_name-64` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `uv,cp_uvlo` |
| `info-fault_name-65` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `ov,cp_ovlo` |
| `info-fault_name-66` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `cp_wdog_expiry` |
| `info-fault_name-67` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `uv,ldo9_uv` |
| `info-fault_name-68` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `ov,ldo9_ov` |
| `info-fault_name-69` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `uv,ldo9b_uv` |
| `info-fault_name-70` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `ov,ldo9b_ov` |
| `info-fault_name-71` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `ov,cpneg_dvc` |
| `info-fault_name-8` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `por` |
| `info-fault_name-9` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `rst` |
| `info-has_phra` | 1 | u32 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x1` |
| `info-id` | 1 | u64 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0xa00000000` |
| `info-leg_scrpad` | 2 | u32×2 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0xf800`<br>[`/arm-io/nub-spmi0/pmu-main/sgpio-bridge-pmu-main/pmu-secondary`](../devicetree/root__arm-io__nub-spmi0__pmu-main__sgpio-bridge-pmu-main__pmu-secondary.md) = `0xf800` |
| `info-o2ws_name-0` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `fw_nonsec_off_wakeup_csr` |
| `info-o2ws_name-1` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `gcb_off_wakeup` |
| `info-o2ws_name-10` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `target_state_wdog_timeout` |
| `info-o2ws_name-11` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `pgood_wdog_to_error_wakeup` |
| `info-o2ws_name-12` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `wake2lf_negedge` |
| `info-o2ws_name-13` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `fw_nonsec_off_wakeup_wdog` |
| `info-o2ws_name-14` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `fw_req_auto_wakeup` |
| `info-o2ws_name-2` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `gcb_wakeup` |
| `info-o2ws_name-3` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `rtc_alarm_wakeup` |
| `info-o2ws_name-4` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `auto_wakeup` |
| `info-o2ws_name-5` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `gcb_crash_wakeup` |
| `info-o2ws_name-6` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `hw_wdog_wakeup` |
| `info-o2ws_name-7` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `fw_wdog_wakeup` |
| `info-o2ws_name-8` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `dft_ctrl2_wakeup` |
| `info-o2ws_name-9` | 1 | string | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `pgood_wdog_to_off_wakeup` |
| `info-off2wake_source` | 1 | u64 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x20000281b` |
| `info-rtc` | 1 | u32 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x2002` |
| `info-rtc_alarm_ctrl` | 1 | u32 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x2000` |
| `info-rtc_alarm_ctrl_en_mask` | 1 | u32 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x40` |
| `info-rtc_alarm_event` | 1 | u32 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x2000` |
| `info-rtc_alarm_event_mask` | 1 | u32 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x2` |
| `info-rtc_alarm_mask` | 1 | u32 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x1` |
| `info-rtc_alarm_monitor_mask` | 1 | u32 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x1` |
| `info-rtc_alarm_offset` | 1 | u32 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x2008` |
| `info-rtc_irq_mask_offset` | 1 | u32 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x200e` |
| `info-rtc_scrpad` | 1 | u32 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x2100` |
| `info-scrpad` | 1 | u64 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x280000008000` |
| `info-scrpad_lpm_ctrl` | 1 | u32 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0xa7dc` |
| `info-scrpad_lpm_log` | 1 | u32 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0xa780` |
| `info-scrpad_socd` | 1 | u64 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x80000008b00` |
| `initial-trigger-bytes` | 2 | u32×2 | [`/arm-io/admac-base-s/base-s-adma-tx-2`](../devicetree/root__arm-io__admac-base-s__base-s-adma-tx-2.md) = `0x60`<br>[`/arm-io/admac-base-s/base-s-adma-tx-3`](../devicetree/root__arm-io__admac-base-s__base-s-adma-tx-3.md) = `0x60` |
| `inner-camera` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x1` |
| `inner-max-video-fps-1080p` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x1e` |
| `input-data-source-selectors` | 2 | 48 B, 456 B | [`/arm-io/iop-audio-controller/audio-speaker`](../devicetree/root__arm-io__iop-audio-controller__audio-speaker.md) = `30567073304970733032767330726573…`<br>[`/arm-io/iop-audio-controller/audio-hpdbg`](../devicetree/root__arm-io__iop-audio-controller__audio-hpdbg.md) = `000000006361706163616f61736f7063…` |
| `input-latency` | 2 | u32×2 | [`/arm-io/iop-audio-controller/audio-haptic`](../devicetree/root__arm-io__iop-audio-controller__audio-haptic.md) = `0x8`<br>[`/arm-io/iop-audio-controller/audio-hpdbg`](../devicetree/root__arm-io__iop-audio-controller__audio-hpdbg.md) = `0x5` |
| `inst` | 1 | u32 | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0x0` |
| `instance` | 24 | string×18, 32 B×2, 80 B×2 | [`/arm-io/dart-sep`](../devicetree/root__arm-io__dart-sep.md) = `TRAD, DART`<br>[`/arm-io/dart-sio`](../devicetree/root__arm-io__dart-sio.md) = `TRAD, DART`<br>[`/arm-io/dart-sbr`](../devicetree/root__arm-io__dart-sbr.md) = `TRAD, DART`<br>[`/arm-io/atc-phy0`](../devicetree/root__arm-io__atc-phy0.md) = `0x0`<br>[`/arm-io/dart-usb0`](../devicetree/root__arm-io__dart-usb0.md) = `5452414400000000444152544c4c5400…` |
| `int-id` | 1 | u64 | [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) = `0x8080404040404` |
| `int-offset` | 1 | u64 | [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) = `0x1000d0b090200` |
| `internal-index` | 2 | u32×2 | [`/arm-io/dcp/iop-dcp-nub`](../devicetree/root__arm-io__dcp__iop-dcp-nub.md) = `0x0`<br>[`/arm-io/dcpsec/iop-dcpsec-nub`](../devicetree/root__arm-io__dcpsec__iop-dcpsec-nub.md) = `0x1` |
| `interrupt-base` | 1 | u32 | [`/arm-io/msg`](../devicetree/root__arm-io__msg.md) = `0x5c` |
| `interrupt-config` | 1 | 120 B | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `000000014456464d5f434f5000000000…` |
| `interrupt-controller` | 14 | empty×13, string | [`/arm-io/aic`](../devicetree/root__arm-io__aic.md) = `master`<br>[`/arm-io/gpio0`](../devicetree/root__arm-io__gpio0.md) = ``<br>[`/arm-io/aop-gpio`](../devicetree/root__arm-io__aop-gpio.md) = ``<br>[`/arm-io/nub-gpio`](../devicetree/root__arm-io__nub-gpio.md) = ``<br>[`/arm-io/smc-gpio`](../devicetree/root__arm-io__smc-gpio.md) = `` |
| `interrupt-parent` | 143 | u32×136, 12 B×5, 36 B | [`/cpus/cpu0`](../devicetree/root__cpus__cpu0.md) = `0x2d`<br>[`/cpus/cpu1`](../devicetree/root__cpus__cpu1.md) = `0x2d`<br>[`/cpus/cpu2`](../devicetree/root__cpus__cpu2.md) = `0x2d`<br>[`/cpus/cpu3`](../devicetree/root__cpus__cpu3.md) = `0x2d`<br>[`/cpus/cpu4`](../devicetree/root__cpus__cpu4.md) = `0x2d` |
| `interrupt-type` | 1 | 12 B | [`/arm-io/nub-spmi2/spmi-hpm0`](../devicetree/root__arm-io__nub-spmi2__spmi-hpm0.md) = `000000000200000003000000` |
| `interrupts` | 136 | u32×64, u64×18, 12 B×18 | [`/cpus/cpu0`](../devicetree/root__cpus__cpu0.md) = `0x32`<br>[`/cpus/cpu1`](../devicetree/root__cpus__cpu1.md) = `0x35`<br>[`/cpus/cpu2`](../devicetree/root__cpus__cpu2.md) = `0x38`<br>[`/cpus/cpu3`](../devicetree/root__cpus__cpu3.md) = `0x3b`<br>[`/cpus/cpu4`](../devicetree/root__cpus__cpu4.md) = `0x46` |
| `interrupts-valid` | 1 | u32 | [`/arm-io/sgx`](../devicetree/root__arm-io__sgx.md) = `0xdf` |
| `intmaskclear-stride` | 1 | u32 | [`/arm-io/aic`](../devicetree/root__arm-io__aic.md) = `0x4a00` |
| `intmaskset-stride` | 1 | u32 | [`/arm-io/aic`](../devicetree/root__arm-io__aic.md) = `0x4a00` |
| `invert-menu-key` | 1 | u32 | [`/arm-io/spi1/mesa`](../devicetree/root__arm-io__spi1__mesa.md) = `0x1` |
| `iomd-cache-size` | 24 | u32×24 | [`/arm-io/dart-disp0/mapper-disp0`](../devicetree/root__arm-io__dart-disp0__mapper-disp0.md) = `0x40`<br>[`/arm-io/dart-disp0/mapper-disp0-piodma`](../devicetree/root__arm-io__dart-disp0__mapper-disp0-piodma.md) = `0x40`<br>[`/arm-io/dart-dispgrt/mapper-dispgrt`](../devicetree/root__arm-io__dart-dispgrt__mapper-dispgrt.md) = `0x40`<br>[`/arm-io/dart-dispsec/mapper-dispsec`](../devicetree/root__arm-io__dart-dispsec__mapper-dispsec.md) = `0x40`<br>[`/arm-io/dart-dispsec/mapper-dispsec-piodma`](../devicetree/root__arm-io__dart-dispsec__mapper-dispsec-piodma.md) = `0x40` |
| `iomd-cache-ttl` | 24 | u32×24 | [`/arm-io/dart-disp0/mapper-disp0`](../devicetree/root__arm-io__dart-disp0__mapper-disp0.md) = `0x7d0`<br>[`/arm-io/dart-disp0/mapper-disp0-piodma`](../devicetree/root__arm-io__dart-disp0__mapper-disp0-piodma.md) = `0x7d0`<br>[`/arm-io/dart-dispgrt/mapper-dispgrt`](../devicetree/root__arm-io__dart-dispgrt__mapper-dispgrt.md) = `0x7d0`<br>[`/arm-io/dart-dispsec/mapper-dispsec`](../devicetree/root__arm-io__dart-dispsec__mapper-dispsec.md) = `0x7d0`<br>[`/arm-io/dart-dispsec/mapper-dispsec-piodma`](../devicetree/root__arm-io__dart-dispsec__mapper-dispsec-piodma.md) = `0x7d0` |
| `iommu-parent` | 49 | u32×35, u64×9, 24 B×2 | [`/arm-io/aes`](../devicetree/root__arm-io__aes.md) = `0x8c`<br>[`/arm-io/aop`](../devicetree/root__arm-io__aop.md) = `0x8e`<br>[`/arm-io/aop/iop-aop-nub/rose`](../devicetree/root__arm-io__aop__iop-aop-nub__rose.md) = `0x98`<br>[`/arm-io/aop-exclave-mailbox`](../devicetree/root__arm-io__aop-exclave-mailbox.md) = `0x90`<br>[`/arm-io/aop2`](../devicetree/root__arm-io__aop2.md) = `0x8f` |
| `iommu-present` | 1 | empty | [`/arm-io`](../devicetree/root__arm-io.md) = `` |
| `iop-audio-service-name` | 2 | string×2 | [`/arm-io/iop-audio-controller`](../devicetree/root__arm-io__iop-audio-controller.md) = `AOPAudioService`<br>[`/arm-io/iop-voicetrigger-controller`](../devicetree/root__arm-io__iop-voicetrigger-controller.md) = `AOPVoiceTriggerService` |
| `iop-version` | 16 | u32×16 | [`/arm-io/aop`](../devicetree/root__arm-io__aop.md) = `0x1`<br>[`/arm-io/aop2`](../devicetree/root__arm-io__aop2.md) = `0x1`<br>[`/arm-io/pmp`](../devicetree/root__arm-io__pmp.md) = `0x1`<br>[`/arm-io/sep`](../devicetree/root__arm-io__sep.md) = `0x1`<br>[`/arm-io/sio`](../devicetree/root__arm-io__sio.md) = `0x1` |
| `ioport-client` | 1 | u32 | [`/arm-io/smc/iop-smc-nub/smc-power-out`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-power-out.md) = `0x1` |
| `ipce-hw-retention` | 10 | empty×10 | [`/arm-io/dart-dcp`](../devicetree/root__arm-io__dart-dcp.md) = ``<br>[`/arm-io/dart-disp0`](../devicetree/root__arm-io__dart-disp0.md) = ``<br>[`/arm-io/dart-dispgrt`](../devicetree/root__arm-io__dart-dispgrt.md) = ``<br>[`/arm-io/dart-dcpsec`](../devicetree/root__arm-io__dart-dcpsec.md) = ``<br>[`/arm-io/dart-dispsec`](../devicetree/root__arm-io__dart-dispsec.md) = `` |
| `irq-destination-index` | 6 | u32×6 | [`/arm-io/admac-dispint0`](../devicetree/root__arm-io__admac-dispint0.md) = `0x0`<br>[`/arm-io/admac-dispext0`](../devicetree/root__arm-io__admac-dispext0.md) = `0x0`<br>[`/arm-io/admac-base-ns`](../devicetree/root__arm-io__admac-base-ns.md) = `0x0`<br>[`/arm-io/admac-leap-ns`](../devicetree/root__arm-io__admac-leap-ns.md) = `0x0`<br>[`/arm-io/admac-base-s`](../devicetree/root__arm-io__admac-base-s.md) = `0x0` |
| `irq-destinations` | 6 | 16 B×6 | [`/arm-io/admac-dispint0`](../devicetree/root__arm-io__admac-dispint0.md) = `2043494155504341204e544744534e55`<br>[`/arm-io/admac-dispext0`](../devicetree/root__arm-io__admac-dispext0.md) = `2043494155504341204e544744534e55`<br>[`/arm-io/admac-base-ns`](../devicetree/root__arm-io__admac-base-ns.md) = `2043494155504341204e544744534e55`<br>[`/arm-io/admac-leap-ns`](../devicetree/root__arm-io__admac-leap-ns.md) = `2043494155504341204e544744534e55`<br>[`/arm-io/admac-base-s`](../devicetree/root__arm-io__admac-base-s.md) = `2043494155504341204e544744534e55` |
| `irq-tx-offset-accessory` | 2 | u32×2 | [`/arm-io/aop-spmi1/wlan-idc`](../devicetree/root__arm-io__aop-spmi1__wlan-idc.md) = `0x3c`<br>[`/arm-io/aop-spmi1/baseband-idc`](../devicetree/root__arm-io__aop-spmi1__baseband-idc.md) = `0x39` |
| `irq-tx-offset-billboard-send0` | 2 | u32×2 | [`/arm-io/aop-spmi0/baseband-heb`](../devicetree/root__arm-io__aop-spmi0__baseband-heb.md) = `0x12`<br>[`/arm-io/aop-spmi1/baseband-idc`](../devicetree/root__arm-io__aop-spmi1__baseband-idc.md) = `0x12` |
| `irq-tx-offset-billboard-send1` | 2 | u32×2 | [`/arm-io/aop-spmi0/baseband-heb`](../devicetree/root__arm-io__aop-spmi0__baseband-heb.md) = `0x13`<br>[`/arm-io/aop-spmi1/baseband-idc`](../devicetree/root__arm-io__aop-spmi1__baseband-idc.md) = `0x13` |
| `irq-tx-offset-billboard-send2` | 2 | u32×2 | [`/arm-io/aop-spmi0/baseband-heb`](../devicetree/root__arm-io__aop-spmi0__baseband-heb.md) = `0x1f`<br>[`/arm-io/aop-spmi1/baseband-idc`](../devicetree/root__arm-io__aop-spmi1__baseband-idc.md) = `0x1f` |
| `irq-tx-offset-config-vswr` | 1 | u32 | [`/arm-io/aop-spmi1/baseband-idc`](../devicetree/root__arm-io__aop-spmi1__baseband-idc.md) = `0x3b` |
| `irq-tx-offset-deviceupdate` | 1 | u32 | [`/arm-io/aop-spmi1/baseband-idc`](../devicetree/root__arm-io__aop-spmi1__baseband-idc.md) = `0x43` |
| `irq-tx-offset-e85mitigation` | 1 | u32 | [`/arm-io/aop-spmi1/baseband-idc`](../devicetree/root__arm-io__aop-spmi1__baseband-idc.md) = `0x1a` |
| `irq-tx-offset-ocp-read-complete` | 2 | u32×2 | [`/arm-io/aop-spmi0/baseband-heb`](../devicetree/root__arm-io__aop-spmi0__baseband-heb.md) = `0x1b`<br>[`/arm-io/aop-spmi1/baseband-idc`](../devicetree/root__arm-io__aop-spmi1__baseband-idc.md) = `0x1b` |
| `irq-tx-offset-ocp-send` | 2 | u32×2 | [`/arm-io/aop-spmi0/baseband-heb`](../devicetree/root__arm-io__aop-spmi0__baseband-heb.md) = `0xc`<br>[`/arm-io/aop-spmi1/baseband-idc`](../devicetree/root__arm-io__aop-spmi1__baseband-idc.md) = `0xd` |
| `irq-tx-offset-sar-budget` | 2 | u32×2 | [`/arm-io/aop-spmi1/wlan-idc`](../devicetree/root__arm-io__aop-spmi1__wlan-idc.md) = `0x3d`<br>[`/arm-io/aop-spmi1/baseband-idc`](../devicetree/root__arm-io__aop-spmi1__baseband-idc.md) = `0x38` |
| `irq-tx-offset-wait-time` | 1 | u32 | [`/arm-io/aop-spmi1/baseband-idc`](../devicetree/root__arm-io__aop-spmi1__baseband-idc.md) = `0x41` |
| `is-development-only` | 1 | empty | [`/arm-io/iop-audio-controller/audio-s-leap-internal-loopback/audio-s-leap-internal-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-s-leap-internal-loopback__audio-s-leap-internal-loopback.md) = `` |
| `is-primary` | 1 | u32 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x1` |
| `island-notch-location` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x90` |
| `isolated-audio-service-input` | 2 | u32×2 | [`/arm-io/iop-audio-controller/audio-hp/audio-codec`](../devicetree/root__arm-io__iop-audio-controller__audio-hp__audio-codec.md) = `0x19c`<br>[`/arm-io/iop-audio-controller/audio-s-leap-internal-loopback/audio-s-leap-internal-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-s-leap-internal-loopback__audio-s-leap-internal-loopback.md) = `0x199` |
| `isolated-audio-service-output` | 2 | u32×2 | [`/arm-io/iop-audio-controller/audio-receiver/audio-receiver`](../devicetree/root__arm-io__iop-audio-controller__audio-receiver__audio-receiver.md) = `0x197`<br>[`/arm-io/iop-audio-controller/audio-speaker-mca/audio-speaker`](../devicetree/root__arm-io__iop-audio-controller__audio-speaker-mca__audio-speaker.md) = `0x196` |
| `isp-alss-lum-weight` | 2 | 16 B×2 | [`/arm-io/disp0`](../devicetree/root__arm-io__disp0.md) = `000000006c36000017b700007b120000`<br>[`/arm-io/dispsec`](../devicetree/root__arm-io__dispsec.md) = `000000006c36000017b700007b120000` |
| `isp-alss-zone-count` | 2 | u32×2 | [`/arm-io/disp0`](../devicetree/root__arm-io__disp0.md) = `0xb`<br>[`/arm-io/dispsec`](../devicetree/root__arm-io__dispsec.md) = `0xb` |
| `isp-alss-zone-height` | 2 | 44 B×2 | [`/arm-io/disp0`](../devicetree/root__arm-io__disp0.md) = `b00000003800000038000000b0000000…`<br>[`/arm-io/dispsec`](../devicetree/root__arm-io__dispsec.md) = `4a0000004a0000004a0000004a000000…` |
| `isp-alss-zone-weight` | 2 | 44 B×2 | [`/arm-io/disp0`](../devicetree/root__arm-io__disp0.md) = `c2b500001e0500001e0500005c0f0000…`<br>[`/arm-io/dispsec`](../devicetree/root__arm-io__dispsec.md) = `23090000fb0a000023090000fb0a0000…` |
| `isp-alss-zone-width` | 2 | 44 B×2 | [`/arm-io/disp0`](../devicetree/root__arm-io__disp0.md) = `b0000000b0000000b0000000b0000000…`<br>[`/arm-io/dispsec`](../devicetree/root__arm-io__dispsec.md) = `510000004a0000004a00000051000000…` |
| `isp-alss-zone-x` | 2 | 44 B×2 | [`/arm-io/disp0`](../devicetree/root__arm-io__disp0.md) = `8f040000df0300008f040000df030000…`<br>[`/arm-io/dispsec`](../devicetree/root__arm-io__dispsec.md) = `00000000510000009b00000000000000…` |
| `isp-alss-zone-y` | 2 | 44 B×2 | [`/arm-io/disp0`](../devicetree/root__arm-io__disp0.md) = `38000000000000000000000038000000…`<br>[`/arm-io/dispsec`](../devicetree/root__arm-io__dispsec.md) = `8e0200008e0200008e020000d8020000…` |
| `isp-aop-control-config` | 1 | 16 B | [`/arm-io/aop/iop-aop-nub/spherecontrol`](../devicetree/root__arm-io__aop__iop-aop-nub__spherecontrol.md) = `0000619002000000000000203d000000` |
| `isp-aop-motion_1-config` | 1 | 16 B | [`/arm-io/aop/iop-aop-nub/spherecontrol`](../devicetree/root__arm-io__aop__iop-aop-nub__spherecontrol.md) = `0000619002000000000000403e000000` |
| `isp-aop-motion_full_rate-config` | 1 | 16 B | [`/arm-io/aop/iop-aop-nub/spherecontrol`](../devicetree/root__arm-io__aop__iop-aop-nub__spherecontrol.md) = `0000619002000000000000083b000000` |
| `isp-aop-pearl-config` | 1 | 16 B | [`/arm-io/aop/iop-aop-nub/spherecontrol`](../devicetree/root__arm-io__aop__iop-aop-nub__spherecontrol.md) = `0000619002000000000000103c000000` |
| `isp-horizon` | 1 | u32 | [`/chosen`](../devicetree/root__chosen.md) = `0x0` |
| `isp_ced_die0` | 2 | u32×2 | [`/ced-ssw/ced_tunable_mask`](../devicetree/root__ced-ssw__ced_tunable_mask.md) = `0x2`<br>[`/ced-ssw/ced_disable_mask`](../devicetree/root__ced-ssw__ced_disable_mask.md) = `0x1` |
| `isp_ced_die1` | 2 | u32×2 | [`/ced-ssw/ced_tunable_mask`](../devicetree/root__ced-ssw__ced_tunable_mask.md) = `0x1e`<br>[`/ced-ssw/ced_disable_mask`](../devicetree/root__ced-ssw__ced_disable_mask.md) = `0xf` |
| `itunes-min-ver` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0xb0200` |
| `join-power-plane` | 3 | u32×3 | [`/arm-io/dcp0-expert`](../devicetree/root__arm-io__dcp0-expert.md) = `0x1`<br>[`/arm-io/dcpsec-expert`](../devicetree/root__arm-io__dcpsec-expert.md) = `0x1`<br>[`/arm-io/dcpext0-expert`](../devicetree/root__arm-io__dcpext0-expert.md) = `0x1` |
| `k2-int-opendrain` | 1 | empty | [`/arm-io/aop/iop-aop-nub`](../devicetree/root__arm-io__aop__iop-aop-nub.md) = `` |
| `k2-pkg-id` | 1 | empty | [`/arm-io/aop/iop-aop-nub`](../devicetree/root__arm-io__aop__iop-aop-nub.md) = `` |
| `kci-name` | 3 | string×3 | [`/arm-io/iop-audio-controller/audio-hw-pcm-audiomgr`](../devicetree/root__arm-io__iop-audio-controller__audio-hw-pcm-audiomgr.md) = `AOPAudioHWPCMAssetManagerInterface`<br>[`/arm-io/iop-audio-controller/audio-haptic-leap`](../devicetree/root__arm-io__iop-audio-controller__audio-haptic-leap.md) = `AppleHapticsAudioInterface`<br>[`/arm-io/audio-resource-manager`](../devicetree/root__arm-io__audio-resource-manager.md) = `AudioResourceManagerInterface` |
| `keep-root-port-on` | 1 | empty | [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) = `` |
| `kern.entitled_dev_max_task_pmem` | 1 | u32 | [`/defaults`](../devicetree/root__defaults.md) = `0x1a00` |
| `kern.entitled_max_task_pmem` | 1 | u32 | [`/defaults`](../devicetree/root__defaults.md) = `0x1800` |
| `kern.gpu_pmem_selector` | 1 | u32 | [`/defaults`](../devicetree/root__defaults.md) = `0x1` |
| `kern.io_throttle_period_tier3` | 1 | u32 | [`/defaults`](../devicetree/root__defaults.md) = `0x14` |
| `kern.io_throttle_window_tier3` | 1 | u32 | [`/defaults`](../devicetree/root__defaults.md) = `0x64` |
| `kern.max_task_pmem` | 1 | u32 | [`/defaults`](../devicetree/root__defaults.md) = `0xd30` |
| `kern.maxkfsevents` | 1 | u32 | [`/defaults`](../devicetree/root__defaults.md) = `0x400` |
| `kern.maxvnodes` | 1 | u32 | [`/defaults`](../devicetree/root__defaults.md) = `0x4650` |
| `kern.memstat_reaper_mb` | 1 | u32 | [`/defaults`](../devicetree/root__defaults.md) = `0x96a` |
| `kern.swap_all_apps` | 1 | u32 | [`/defaults`](../devicetree/root__defaults.md) = `0x1` |
| `kern.thread_group_extra_bytes` | 1 | u32 | [`/defaults`](../devicetree/root__defaults.md) = `0x40` |
| `kern.vm_compressor` | 1 | u32 | [`/defaults`](../devicetree/root__defaults.md) = `0x20` |
| `kern.vm_reclaim_max_threshold` | 1 | string | [`/defaults`](../devicetree/root__defaults.md) = ` ` |
| `kernel-only` | 1 | string | [`/chosen/memory-map`](../devicetree/root__chosen__memory-map.md) = `true` |
| `l2-cache-id` | 6 | u32×6 | [`/cpus/cpu0`](../devicetree/root__cpus__cpu0.md) = `0x0`<br>[`/cpus/cpu1`](../devicetree/root__cpus__cpu1.md) = `0x0`<br>[`/cpus/cpu2`](../devicetree/root__cpus__cpu2.md) = `0x0`<br>[`/cpus/cpu3`](../devicetree/root__cpus__cpu3.md) = `0x0`<br>[`/cpus/cpu4`](../devicetree/root__cpus__cpu4.md) = `0x0` |
| `l2-cache-size` | 12 | u32×12 | [`/cpus/cpu0/:borneo_h19a_3`](../devicetree/root__cpus__cpu0___borneo_h19a_3.md) = `0x400000`<br>[`/cpus/cpu0/:borneo_h19p_3`](../devicetree/root__cpus__cpu0___borneo_h19p_3.md) = `0x800000`<br>[`/cpus/cpu1/:borneo_h19a_3`](../devicetree/root__cpus__cpu1___borneo_h19a_3.md) = `0x400000`<br>[`/cpus/cpu1/:borneo_h19p_3`](../devicetree/root__cpus__cpu1___borneo_h19p_3.md) = `0x800000`<br>[`/cpus/cpu2/:borneo_h19a_3`](../devicetree/root__cpus__cpu2___borneo_h19a_3.md) = `0x400000` |
| `l2-ecc-correctable-panic` | 1 | u32 | [`/defaults`](../devicetree/root__defaults.md) = `0x1` |
| `lane-cfg` | 1 | u32 | [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) = `0x0` |
| `large-format-phone` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `link-state-power` | 1 | 16 B | [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) = `00000000000000000000000000000000` |
| `link-tx_config` | 1 | 20 B | [`/arm-io/smc/iop-smc-nub/smc-aop`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-aop.md) = `0000640c03000000200000002d000000…` |
| `listening-mic-mask` | 1 | u32 | [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) = `0x5` |
| `live-effects` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x1` |
| `live-photo-auto` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x1` |
| `live-photo-capture` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x1` |
| `LmaxProduct` | 1 | u32 | [`/exbright`](../devicetree/root__exbright.md) = `0xbb80000` |
| `lmic-mic` | 1 | u64 | [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) = `0x30a020a04` |
| `LminProduct` | 1 | u32 | [`/exbright`](../devicetree/root__exbright.md) = `0xa0000` |
| `load-kernel-start` | 1 | u32 | [`/chosen/iBoot`](../devicetree/root__chosen__iBoot.md) = `0x0` |
| `local-mac-address` | 3 | string×3 | [`/arm-io/apcie/pci-bridge0/centauri-alpha`](../devicetree/root__arm-io__apcie__pci-bridge0__centauri-alpha.md) = `macaddr/wifiaddr,syscfg/WMac/6,zeroes/6`<br>[`/arm-io/bluetooth`](../devicetree/root__arm-io__bluetooth.md) = `macaddr/btaddr,syscfg/BMac/6,zeroes/6`<br>[`/fillmore`](../devicetree/root__fillmore.md) = `macaddr/otaddr,syscfg/TMac/8,zeroes/8` |
| `location-reminders` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `lockdown-certtype` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `low-power-enable` | 1 | empty | [`/arm-io/sep`](../devicetree/root__arm-io__sep.md) = `` |
| `low-power-express` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `low-power-wallet-mode` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `low-temp-accel-offset` | 2 | string×2 | [`/arm-io/aop/iop-aop-nub/accel_1`](../devicetree/root__arm-io__aop__iop-aop-nub__accel_1.md) = `syscfg/LTAO`<br>[`/arm-io/aop/iop-aop-nub/accel`](../devicetree/root__arm-io__aop__iop-aop-nub__accel.md) = `syscfg/LTAO` |
| `LPMic` | 1 | u64 | [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) = `0x8004060100` |
| `lts-config` | 1 | 80 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `010000000c020000db6d220000000000…` |
| `lts-ctrl-loop` | 1 | 224 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `01000000000000000000000001000000…` |
| `lts-ctrl-ts` | 1 | u32 | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0x50000` |
| `lts-voltage` | 1 | 48 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `01000000030000000400000002000000…` |
| `ma-channel-thr` | 3 | 20 B×3 | [`/arm-io/aop/iop-aop-nub/als2a`](../devicetree/root__arm-io__aop__iop-aop-nub__als2a.md) = `00002442000088410000c8410000c841…`<br>[`/arm-io/aop/iop-aop-nub/als2b`](../devicetree/root__arm-io__aop__iop-aop-nub__als2b.md) = `00002442000088410000c8410000c841…`<br>[`/arm-io/aop/iop-aop-nub/als`](../devicetree/root__arm-io__aop__iop-aop-nub__als.md) = `00002442000088410000c8410000c841…` |
| `mac-address-bluetooth0` | 1 | string | [`/chosen`](../devicetree/root__chosen.md) = `macaddr/btaddr,syscfg/BMac/6` |
| `mac-address-ethernet0` | 1 | string | [`/chosen`](../devicetree/root__chosen.md) = `macaddr/ethaddr,syscfg/EMac/6` |
| `mac-address-ethernet1` | 1 | string | [`/chosen`](../devicetree/root__chosen.md) = `macaddr/ethaddr1,syscfg/EMc2/6` |
| `mac-address-wifi0` | 1 | string | [`/chosen`](../devicetree/root__chosen.md) = `macaddr/wifiaddr,syscfg/WMac/6` |
| `magnitude-cal` | 1 | u32 | [`/arm-io/aop/iop-aop-nub/jarvis`](../devicetree/root__arm-io__aop__iop-aop-nub__jarvis.md) = `0xfa00000` |
| `manual-availability` | 14 | u32×14 | [`/arm-io/dart-sbr`](../devicetree/root__arm-io__dart-sbr.md) = `0x1`<br>[`/arm-io/dart-usb0`](../devicetree/root__arm-io__dart-usb0.md) = `0x1`<br>[`/arm-io/dart-disp0`](../devicetree/root__arm-io__dart-disp0.md) = `0x1`<br>[`/arm-io/dart-dispgrt`](../devicetree/root__arm-io__dart-dispgrt.md) = `0x1`<br>[`/arm-io/dart-dcpsec`](../devicetree/root__arm-io__dart-dcpsec.md) = `0x1` |
| `manual-enable` | 2 | empty×2 | [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) = ``<br>[`/arm-io/apcie/pci-bridge1`](../devicetree/root__arm-io__apcie__pci-bridge1.md) = `` |
| `manual-enable-defer-scan` | 2 | empty×2 | [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) = ``<br>[`/arm-io/apcie/pci-bridge1`](../devicetree/root__arm-io__apcie__pci-bridge1.md) = `` |
| `manual-enable-s2r` | 1 | empty | [`/arm-io/apcie/pci-bridge1`](../devicetree/root__arm-io__apcie__pci-bridge1.md) = `` |
| `manufacturer` | 1 | string | [`/`](../devicetree/root.md) = `Apple Inc.` |
| `map-range` | 1 | 20 B | [`/arm-io/sio`](../devicetree/root__arm-io__sio.md) = `4353494d000000a50200000000400000…` |
| `mapping-enforcement-mode` | 1 | u32 | [`/arm-io`](../devicetree/root__arm-io.md) = `0x2` |
| `marketing-hardware-behavior` | 1 | string | [`/chosen`](../devicetree/root__chosen.md) = `syscfg/MkBH` |
| `marketing-software-behavior` | 1 | string | [`/chosen`](../devicetree/root__chosen.md) = `syscfg/MkBS` |
| `max-aop-clk` | 1 | u32 | [`/arm-io/dockchannel-uart`](../devicetree/root__arm-io__dockchannel-uart.md) = `0x112a8800` |
| `max-aurora-gain` | 1 | 12 B | [`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `00002040b81e3540b81e3540` |
| `max-avg-bpp` | 2 | u32×2 | [`/arm-io/disp0`](../devicetree/root__arm-io__disp0.md) = `0xd999a`<br>[`/arm-io/dispsec`](../devicetree/root__arm-io__dispsec.md) = `0xd999a` |
| `max-bit-depth-bits` | 16 | u32×16 | [`/arm-io/admac-base-ns/base-ns-adma-rx-2`](../devicetree/root__arm-io__admac-base-ns__base-ns-adma-rx-2.md) = `0x10`<br>[`/arm-io/admac-base-ns/base-ns-adma-rx-3`](../devicetree/root__arm-io__admac-base-ns__base-ns-adma-rx-3.md) = `0x10`<br>[`/arm-io/admac-base-ns/base-ns-adma-rx-4`](../devicetree/root__arm-io__admac-base-ns__base-ns-adma-rx-4.md) = `0x20`<br>[`/arm-io/admac-base-ns/base-ns-adma-rx-5`](../devicetree/root__arm-io__admac-base-ns__base-ns-adma-rx-5.md) = `0x10`<br>[`/arm-io/admac-base-ns/base-ns-adma-tx-7`](../devicetree/root__arm-io__admac-base-ns__base-ns-adma-tx-7.md) = `0x10` |
| `max-channel-count` | 16 | u32×16 | [`/arm-io/admac-base-ns/base-ns-adma-rx-2`](../devicetree/root__arm-io__admac-base-ns__base-ns-adma-rx-2.md) = `0xc`<br>[`/arm-io/admac-base-ns/base-ns-adma-rx-3`](../devicetree/root__arm-io__admac-base-ns__base-ns-adma-rx-3.md) = `0x2`<br>[`/arm-io/admac-base-ns/base-ns-adma-rx-4`](../devicetree/root__arm-io__admac-base-ns__base-ns-adma-rx-4.md) = `0x4`<br>[`/arm-io/admac-base-ns/base-ns-adma-rx-5`](../devicetree/root__arm-io__admac-base-ns__base-ns-adma-rx-5.md) = `0x9`<br>[`/arm-io/admac-base-ns/base-ns-adma-tx-7`](../devicetree/root__arm-io__admac-base-ns__base-ns-adma-tx-7.md) = `0x4` |
| `max-env-partition` | 1 | u32 | [`/chosen`](../devicetree/root__chosen.md) = `0x0` |
| `max-env-var-data-size` | 1 | u32 | [`/chosen`](../devicetree/root__chosen.md) = `0x0` |
| `max-env-var-name-size` | 1 | u32 | [`/chosen`](../devicetree/root__chosen.md) = `0x0` |
| `max-fifo-depth-bytes` | 2 | u32×2 | [`/arm-io/admac-base-s/base-s-adma-tx-2`](../devicetree/root__arm-io__admac-base-s__base-s-adma-tx-2.md) = `0xa0`<br>[`/arm-io/admac-base-s/base-s-adma-tx-3`](../devicetree/root__arm-io__admac-base-s__base-s-adma-tx-3.md) = `0xa0` |
| `max-peak-bpp` | 2 | u32×2 | [`/arm-io/disp0`](../devicetree/root__arm-io__disp0.md) = `0xd999a`<br>[`/arm-io/dispsec`](../devicetree/root__arm-io__dispsec.md) = `0xd999a` |
| `max-sample-rate-hz` | 16 | u32×16 | [`/arm-io/admac-base-ns/base-ns-adma-rx-2`](../devicetree/root__arm-io__admac-base-ns__base-ns-adma-rx-2.md) = `0xbb80`<br>[`/arm-io/admac-base-ns/base-ns-adma-rx-3`](../devicetree/root__arm-io__admac-base-ns__base-ns-adma-rx-3.md) = `0xbb80`<br>[`/arm-io/admac-base-ns/base-ns-adma-rx-4`](../devicetree/root__arm-io__admac-base-ns__base-ns-adma-rx-4.md) = `0xbb80`<br>[`/arm-io/admac-base-ns/base-ns-adma-rx-5`](../devicetree/root__arm-io__admac-base-ns__base-ns-adma-rx-5.md) = `0xbb80`<br>[`/arm-io/admac-base-ns/base-ns-adma-tx-7`](../devicetree/root__arm-io__admac-base-ns__base-ns-adma-tx-7.md) = `0x3e80` |
| `max-scaling-ratio` | 2 | u32×2 | [`/arm-io/disp0`](../devicetree/root__arm-io__disp0.md) = `0x20000`<br>[`/arm-io/dispsec`](../devicetree/root__arm-io__dispsec.md) = `0x20000` |
| `max-scan-time` | 1 | u32 | [`/arm-io/spi1/mesa`](../devicetree/root__arm-io__spi1__mesa.md) = `0x13333` |
| `max-sids-in-mismatch` | 1 | u32 | [`/arm-io/dart-isp`](../devicetree/root__arm-io__dart-isp.md) = `0x12` |
| `max_fs_entries` | 4 | u32×4 | [`/filesystems/fstab`](../devicetree/root__filesystems__fstab.md) = `0x7`<br>[`/filesystems/fstab-ephemeral-recovery-data`](../devicetree/root__filesystems__fstab-ephemeral-recovery-data.md) = `0x3`<br>[`/filesystems/fstab-ephemeral-diag-data`](../devicetree/root__filesystems__fstab-ephemeral-diag-data.md) = `0x7`<br>[`/filesystems/fstab-ephemeral-devrecov-data`](../devicetree/root__filesystems__fstab-ephemeral-devrecov-data.md) = `0x4` |
| `max_irq_interrupt_umask` | 1 | u32 | [`/arm-io/aic`](../devicetree/root__arm-io__aic.md) = `0xffff` |
| `maximum-link-speed` | 1 | u32 | [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) = `0x3` |
| `maxnumirq-offset` | 1 | u32 | [`/arm-io/aic`](../devicetree/root__arm-io__aic.md) = `0xc` |
| `mc-cue-quota-cfg` | 1 | 120 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `00000000200100002001000008000000…` |
| `mc-cue-win-count` | 1 | u32 | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0x50` |
| `mc-dsid-ptd-config` | 1 | 24 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `00000000000000000800000000000000…` |
| `mc-quota-policy` | 1 | u32 | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0x2` |
| `mc_cmd_ack_ptd_count` | 1 | u32 | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0x1` |
| `mc_cmd_ptd_count` | 1 | u32 | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0x2` |
| `mc_quota_req_ptd_count` | 1 | u32 | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0x8` |
| `mc_quota_rsp_ptd_count` | 1 | u32 | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0x8` |
| `mcache-stream` | 1 | 2352 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0e00000004000000010000000d000000…` |
| `mem-compute-power-ratio-high` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x60000` |
| `mem-compute-power-ratio-low` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x40000` |
| `mem-compute-power-target-high` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x3999` |
| `mem-compute-power-target-low` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x2000` |
| `mem-cpu-stall-amx-thresh-p` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0xea60` |
| `mem-cpu-stall-min-effort-c1-p` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x10000` |
| `mem-cpu-stall-min-effort-t1-p` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x1999` |
| `mem-cpu-stall-r-ki-down-c1-p` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x20000` |
| `mem-cpu-stall-r-ki-up-c0-e` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x320000` |
| `mem-cpu-stall-r-ki-up-c1-e` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x8000` |
| `mem-cpu-stall-r-ki-up-c1-p` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x4ccc` |
| `mem-cpu-stall-r-t1-e` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x3333` |
| `mem-cpu-stall-r-t1-p` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0xa666` |
| `mem-cpu-stall-r-target-e` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x7ae` |
| `mem-cpu-stall-r-target2-e` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x4ccc` |
| `mem-cpu-stall-r-target2-p` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0xccc` |
| `mem-io-timeout` | 1 | 12 B | [`/arm-io/apcie/pci-bridge0/centauri-control`](../devicetree/root__arm-io__apcie__pci-bridge0__centauri-control.md) = `0000000000000002204e0004` |
| `mem-perf-state-follows-accp` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x0` |
| `MemoryMapReserved-0` | 1 | 16 B | [`/chosen/memory-map`](../devicetree/root__chosen__memory-map.md) = `00000000000000000000000000000000` |
| `MemoryMapReserved-1` | 1 | 16 B | [`/chosen/memory-map`](../devicetree/root__chosen__memory-map.md) = `00000000000000000000000000000000` |
| `MemoryMapReserved-10` | 1 | 16 B | [`/chosen/memory-map`](../devicetree/root__chosen__memory-map.md) = `00000000000000000000000000000000` |
| `MemoryMapReserved-11` | 1 | 16 B | [`/chosen/memory-map`](../devicetree/root__chosen__memory-map.md) = `00000000000000000000000000000000` |
| `MemoryMapReserved-12` | 1 | 16 B | [`/chosen/memory-map`](../devicetree/root__chosen__memory-map.md) = `00000000000000000000000000000000` |
| `MemoryMapReserved-13` | 1 | 16 B | [`/chosen/memory-map`](../devicetree/root__chosen__memory-map.md) = `00000000000000000000000000000000` |
| `MemoryMapReserved-14` | 1 | 16 B | [`/chosen/memory-map`](../devicetree/root__chosen__memory-map.md) = `00000000000000000000000000000000` |
| `MemoryMapReserved-15` | 1 | 16 B | [`/chosen/memory-map`](../devicetree/root__chosen__memory-map.md) = `00000000000000000000000000000000` |
| `MemoryMapReserved-2` | 1 | 16 B | [`/chosen/memory-map`](../devicetree/root__chosen__memory-map.md) = `00000000000000000000000000000000` |
| `MemoryMapReserved-3` | 1 | 16 B | [`/chosen/memory-map`](../devicetree/root__chosen__memory-map.md) = `00000000000000000000000000000000` |
| `MemoryMapReserved-4` | 1 | 16 B | [`/chosen/memory-map`](../devicetree/root__chosen__memory-map.md) = `00000000000000000000000000000000` |
| `MemoryMapReserved-5` | 1 | 16 B | [`/chosen/memory-map`](../devicetree/root__chosen__memory-map.md) = `00000000000000000000000000000000` |
| `MemoryMapReserved-6` | 1 | 16 B | [`/chosen/memory-map`](../devicetree/root__chosen__memory-map.md) = `00000000000000000000000000000000` |
| `MemoryMapReserved-7` | 1 | 16 B | [`/chosen/memory-map`](../devicetree/root__chosen__memory-map.md) = `00000000000000000000000000000000` |
| `MemoryMapReserved-8` | 1 | 16 B | [`/chosen/memory-map`](../devicetree/root__chosen__memory-map.md) = `00000000000000000000000000000000` |
| `MemoryMapReserved-9` | 1 | 16 B | [`/chosen/memory-map`](../devicetree/root__chosen__memory-map.md) = `00000000000000000000000000000000` |
| `mesaType` | 1 | u32 | [`/arm-io/spi1/mesa`](../devicetree/root__arm-io__spi1__mesa.md) = `0x2` |
| `meta-sw-interrupt` | 1 | 20 B | [`/arm-io/sgx`](../devicetree/root__arm-io__sgx.md) = `48400181020000004842018102000000…` |
| `metal-standard` | 1 | u32 | [`/arm-io/sgx`](../devicetree/root__arm-io__sgx.md) = `0x100` |
| `mib-curve-lux` | 1 | 124 B | [`/exbright`](../devicetree/root__exbright.md) = `00000000010000000200000005000000…` |
| `mib-curve-lux-1` | 1 | 124 B | [`/exbright`](../devicetree/root__exbright.md) = `00000000010000000200000005000000…` |
| `mib-curve-nits` | 1 | 124 B | [`/exbright`](../devicetree/root__exbright.md) = `1e8502001e85020066260300b89e0400…` |
| `mib-curve-nits-1` | 1 | 124 B | [`/exbright`](../devicetree/root__exbright.md) = `66a6020066a60200eb510300b8de0400…` |
| `mib-nits-scaling-factor` | 1 | u32 | [`/exbright`](../devicetree/root__exbright.md) = `0x6b85` |
| `mib-nits-scaling-factor-1` | 1 | u32 | [`/exbright`](../devicetree/root__exbright.md) = `0x6b85` |
| `mic-trim-gains-0` | 1 | string | [`/product/audio`](../devicetree/root__product__audio.md) = `syscfg/MiGH` |
| `mic-trim-gains-1` | 1 | string | [`/product/audio`](../devicetree/root__product__audio.md) = `syscfg/MiGT` |
| `mic-trim-gains-key-cnt` | 1 | u32 | [`/product/audio`](../devicetree/root__product__audio.md) = `0x2` |
| `mil` | 1 | u32 | [`/arm-io/eic`](../devicetree/root__arm-io__eic.md) = `0x1` |
| `misc-acg-offset` | 1 | u32 | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0x38000` |
| `misc-cores-offset` | 1 | u32 | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0x34000` |
| `mix-n-match-prevention-status` | 1 | u32 | [`/chosen`](../devicetree/root__chosen.md) = `0x0` |
| `mlb-serial-number` | 1 | string | [`/`](../devicetree/root.md) = `syscfg/MLB#/0x20,zeroes/0x20` |
| `mmio-fpwm` | 1 | 16 B | [`/arm-io/eic`](../devicetree/root__arm-io__eic.md) = `000004e50200000000c0000000000000` |
| `mmio-gltb` | 1 | 16 B | [`/arm-io/eic`](../devicetree/root__arm-io__eic.md) = `00802ac8020000000040000000000000` |
| `mmio-gpio` | 1 | 16 B | [`/arm-io/eic`](../devicetree/root__arm-io__eic.md) = `000000da020000000040000000000000` |
| `mmio-ps` | 1 | 16 B | [`/arm-io/eic`](../devicetree/root__arm-io__eic.md) = `000070c00200000000c0010000000000` |
| `mmio-wd-e` | 1 | 16 B | [`/arm-io/eic`](../devicetree/root__arm-io__eic.md) = `00002bc8020000000040000000000000` |
| `mmio-wd-isp` | 1 | 16 B | [`/arm-io/eic`](../devicetree/root__arm-io__eic.md) = `0000b1c3030000000080000000000000` |
| `mobiledevice-min-ver` | 1 | string | [`/product`](../devicetree/root__product.md) = `1853` |
| `model` | 1 | string | [`/`](../devicetree/root.md) = `iPhone19,4` |
| `model-config` | 1 | string | [`/`](../devicetree/root.md) = `syscfg/MdlC` |
| `model-name` | 2 | string×2 | [`/arm-io/iop-audio-controller/audio-haptic`](../devicetree/root__arm-io__iop-audio-controller__audio-haptic.md) = `leap`<br>[`/arm-io/iop-audio-controller/audio-hpdbg`](../devicetree/root__arm-io__iop-audio-controller__audio-hpdbg.md) = `IOPHapticDebug` |
| `model-number` | 1 | string | [`/`](../devicetree/root.md) = `syscfg/Mod#/0x20,zeroes/0x20` |
| `model-param-max-Qmax` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x6270` |
| `model-param-max-resistance` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x64` |
| `model-param-min-RCFreq4` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x1b5` |
| `model-param-temp-coeff-thresh` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0xffff63c0` |
| `mogul-auth-key` | 2 | string×2 | [`/arm-io/dcp0-expert`](../devicetree/root__arm-io__dcp0-expert.md) = `auth-passed`<br>[`/arm-io/dcpsec-expert`](../devicetree/root__arm-io__dcpsec-expert.md) = `auth-passed` |
| `mogul-auth-provider` | 2 | u32×2 | [`/arm-io/dcp0-expert`](../devicetree/root__arm-io__dcp0-expert.md) = `0xc1`<br>[`/arm-io/dcpsec-expert`](../devicetree/root__arm-io__dcpsec-expert.md) = `0xc2` |
| `moment-capture` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x1` |
| `monitor-current-3v0-count` | 1 | u32 | [`/arm-io/spi1/mesa`](../devicetree/root__arm-io__spi1__mesa.md) = `0x3` |
| `monitor-current-3v0-threshold` | 1 | u32 | [`/arm-io/spi1/mesa`](../devicetree/root__arm-io__spi1__mesa.md) = `0x82` |
| `monitor-current-avg-count` | 1 | u32 | [`/arm-io/spi1/mesa`](../devicetree/root__arm-io__spi1__mesa.md) = `0x1` |
| `monitor-enable-power-down` | 1 | u32 | [`/arm-io/spi1/mesa`](../devicetree/root__arm-io__spi1__mesa.md) = `0x0` |
| `monitor-power-avg-count` | 1 | u32 | [`/arm-io/spi1/mesa`](../devicetree/root__arm-io__spi1__mesa.md) = `0x14` |
| `monitor-power-interval` | 1 | u32 | [`/arm-io/spi1/mesa`](../devicetree/root__arm-io__spi1__mesa.md) = `0x3e8` |
| `monitor-power-threshold` | 1 | u32 | [`/arm-io/spi1/mesa`](../devicetree/root__arm-io__spi1__mesa.md) = `0xbe` |
| `msg-buffer-address-rx-ocp` | 2 | u32×2 | [`/arm-io/aop-spmi0/baseband-heb`](../devicetree/root__arm-io__aop-spmi0__baseband-heb.md) = `0xa0`<br>[`/arm-io/aop-spmi1/baseband-idc`](../devicetree/root__arm-io__aop-spmi1__baseband-idc.md) = `0xa0` |
| `msg-buffer-address-tx-billboard` | 2 | u32×2 | [`/arm-io/aop-spmi0/baseband-heb`](../devicetree/root__arm-io__aop-spmi0__baseband-heb.md) = `0x20`<br>[`/arm-io/aop-spmi1/baseband-idc`](../devicetree/root__arm-io__aop-spmi1__baseband-idc.md) = `0x20` |
| `msg-buffer-address-tx-ocp` | 2 | u32×2 | [`/arm-io/aop-spmi0/baseband-heb`](../devicetree/root__arm-io__aop-spmi0__baseband-heb.md) = `0x1080`<br>[`/arm-io/aop-spmi1/baseband-idc`](../devicetree/root__arm-io__aop-spmi1__baseband-idc.md) = `0x1080` |
| `msgbox-mailbox-connection` | 1 | u32 | [`/arm-io/avd`](../devicetree/root__arm-io__avd.md) = `0xd` |
| `msgbox-mailbox-num` | 20 | u32×20 | [`/arm-io/aop`](../devicetree/root__arm-io__aop.md) = `0x0`<br>[`/arm-io/aop-exclave-mailbox`](../devicetree/root__arm-io__aop-exclave-mailbox.md) = `0x13`<br>[`/arm-io/aop2`](../devicetree/root__arm-io__aop2.md) = `0x1`<br>[`/arm-io/aop2-exclave-mailbox`](../devicetree/root__arm-io__aop2-exclave-mailbox.md) = `0x14`<br>[`/arm-io/pmp`](../devicetree/root__arm-io__pmp.md) = `0x4` |
| `msgbox-using-alias` | 16 | string×14, u32×2 | [`/arm-io/aop`](../devicetree/root__arm-io__aop.md) = `true`<br>[`/arm-io/aop-exclave-mailbox`](../devicetree/root__arm-io__aop-exclave-mailbox.md) = `true`<br>[`/arm-io/aop2`](../devicetree/root__arm-io__aop2.md) = `true`<br>[`/arm-io/aop2-exclave-mailbox`](../devicetree/root__arm-io__aop2-exclave-mailbox.md) = `true`<br>[`/arm-io/pmp`](../devicetree/root__arm-io__pmp.md) = `0x1` |
| `msgbox-using-postoffice` | 21 | string×18, u32×3 | [`/arm-io/aop`](../devicetree/root__arm-io__aop.md) = `true`<br>[`/arm-io/aop-exclave-mailbox`](../devicetree/root__arm-io__aop-exclave-mailbox.md) = `true`<br>[`/arm-io/aop2`](../devicetree/root__arm-io__aop2.md) = `true`<br>[`/arm-io/aop2-exclave-mailbox`](../devicetree/root__arm-io__aop2-exclave-mailbox.md) = `true`<br>[`/arm-io/pmp`](../devicetree/root__arm-io__pmp.md) = `0x1` |
| `msi-address` | 1 | u64 | [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) = `0xfffff000` |
| `msi-parent-controller` | 1 | u32 | [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) = `0x2d` |
| `msi-vector-base` | 2 | u32×2 | [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) = `0x0`<br>[`/arm-io/apcie/pci-bridge1`](../devicetree/root__arm-io__apcie__pci-bridge1.md) = `0x20` |
| `msi-vector-offset` | 1 | u32 | [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) = `0x5ed` |
| `msp-bfh-params` | 1 | 60 B | [`/arm-io/ans`](../devicetree/root__arm-io__ans.md) = `01000200efbeadde0200000018000000…` |
| `msp-phy-fw-path` | 1 | string | [`/arm-io/ans`](../devicetree/root__arm-io__ans.md) = `t303.aus5` |
| `mtr-cluster` | 1 | 32 B | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `00000300e001100001000401e1011000…` |
| `mtr-sensor` | 1 | 220 B | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `00050000546530303030356900000000…` |
| `name` | 552 | string×552 | [`/`](../devicetree/root.md) = `device-tree`<br>[`/machine-timeouts`](../devicetree/root__machine-timeouts.md) = `machine-timeouts`<br>[`/chosen`](../devicetree/root__chosen.md) = `chosen`<br>[`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `manifest-properties`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `manifest-object-properties` |
| `name-override` | 1 | string | [`/arm-io/aop/iop-aop-nub/aop-voicetrigger`](../devicetree/root__arm-io__aop__iop-aop-nub__aop-voicetrigger.md) = `AOPVoiceTriggerService` |
| `namespaces` | 1 | 96 B | [`/arm-io/ans`](../devicetree/root__arm-io__ans.md) = `01000000010000000000000002000000…` |
| `nametag` | 15 | u32×15 | [`/arm-io/error-handler/amcc-error-handler`](../devicetree/root__arm-io__error-handler__amcc-error-handler.md) = `0x616d6363`<br>[`/arm-io/error-handler/dcs-error-handler`](../devicetree/root__arm-io__error-handler__dcs-error-handler.md) = `0x64637320`<br>[`/arm-io/error-handler/pmgr-error-handler`](../devicetree/root__arm-io__error-handler__pmgr-error-handler.md) = `0x706d6772`<br>[`/arm-io/error-handler/cllt-error-handler`](../devicetree/root__arm-io__error-handler__cllt-error-handler.md) = `0x636c6c74`<br>[`/arm-io/error-handler/sep-error-handler`](../devicetree/root__arm-io__error-handler__sep-error-handler.md) = `0x73657020` |
| `nand-debug` | 1 | u64 | [`/arm-io/ans`](../devicetree/root__arm-io__ans.md) = `0x1` |
| `navigation` | 1 | u32 | [`/product/maps`](../devicetree/root__product__maps.md) = `0x0` |
| `ncm-control-ecid-mac` | 1 | u32 | [`/arm-io/rsm`](../devicetree/root__arm-io__rsm.md) = `0x1` |
| `network-interface-unit-en` | 1 | u32 | [`/arm-io/apcie/pci-bridge0/centauri-alpha`](../devicetree/root__arm-io__apcie__pci-bridge0__centauri-alpha.md) = `0x0` |
| `nfc-express` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `nfccModel` | 2 | u32×2 | [`/arm-io/aop-spmi0/stockholm-spmi`](../devicetree/root__arm-io__aop-spmi0__stockholm-spmi.md) = `0xdf`<br>[`/arm-io/aop-spmi0/hammerfest-spmi`](../devicetree/root__arm-io__aop-spmi0__hammerfest-spmi.md) = `0xbd` |
| `nfccModel-A0` | 1 | u32 | [`/arm-io/aop-spmi0/stockholm-spmi`](../devicetree/root__arm-io__aop-spmi0__stockholm-spmi.md) = `0xda` |
| `nfccModel_A0` | 1 | u32 | [`/arm-io/aop-spmi0/hammerfest-spmi`](../devicetree/root__arm-io__aop-spmi0__hammerfest-spmi.md) = `0xbc` |
| `nfcWithRadio` | 2 | u32×2 | [`/arm-io/aop-spmi0/stockholm-spmi/stockholm`](../devicetree/root__arm-io__aop-spmi0__stockholm-spmi__stockholm.md) = `0x1`<br>[`/arm-io/aop-spmi0/hammerfest-spmi/hammerfest`](../devicetree/root__arm-io__aop-spmi0__hammerfest-spmi__hammerfest.md) = `0x1` |
| `no-aic-ipi-required` | 6 | empty×6 | [`/cpus/cpu0`](../devicetree/root__cpus__cpu0.md) = ``<br>[`/cpus/cpu1`](../devicetree/root__cpus__cpu1.md) = ``<br>[`/cpus/cpu2`](../devicetree/root__cpus__cpu2.md) = ``<br>[`/cpus/cpu3`](../devicetree/root__cpus__cpu3.md) = ``<br>[`/cpus/cpu4`](../devicetree/root__cpus__cpu4.md) = `` |
| `no-effaceable-storage` | 1 | empty | [`/defaults`](../devicetree/root__defaults.md) = `` |
| `no-firmware-service` | 12 | empty×12 | [`/arm-io/aop2/iop-aop2-nub`](../devicetree/root__arm-io__aop2__iop-aop2-nub.md) = ``<br>[`/arm-io/sio/iop-sio-nub`](../devicetree/root__arm-io__sio__iop-sio-nub.md) = ``<br>[`/arm-io/mtp/iop-mtp-nub`](../devicetree/root__arm-io__mtp__iop-mtp-nub.md) = ``<br>[`/arm-io/dcp/iop-dcp-nub`](../devicetree/root__arm-io__dcp__iop-dcp-nub.md) = ``<br>[`/arm-io/dcpsec/iop-dcpsec-nub`](../devicetree/root__arm-io__dcpsec__iop-dcpsec-nub.md) = `` |
| `no-flow-control` | 1 | empty | [`/arm-io/uart0`](../devicetree/root__arm-io__uart0.md) = `` |
| `no-hibernate-sleep` | 4 | empty×4 | [`/arm-io/ans/iop-ans-nub`](../devicetree/root__arm-io__ans__iop-ans-nub.md) = ``<br>[`/arm-io/smc/iop-smc-nub`](../devicetree/root__arm-io__smc__iop-smc-nub.md) = ``<br>[`/arm-io/dcpsec/iop-dcpsec-nub`](../devicetree/root__arm-io__dcpsec__iop-dcpsec-nub.md) = ``<br>[`/arm-io/dcpext0/iop-dcpext0-nub`](../devicetree/root__arm-io__dcpext0__iop-dcpext0-nub.md) = `` |
| `no-resume-restore` | 5 | u32×5 | [`/arm-io/aop-gpio`](../devicetree/root__arm-io__aop-gpio.md) = `0x1`<br>[`/arm-io/nub-gpio`](../devicetree/root__arm-io__nub-gpio.md) = `0x1`<br>[`/arm-io/smc-gpio`](../devicetree/root__arm-io__smc-gpio.md) = `0x1`<br>[`/arm-io/mtp-gpio`](../devicetree/root__arm-io__mtp-gpio.md) = `0x1`<br>[`/arm-io/secure-repair`](../devicetree/root__arm-io__secure-repair.md) = `0x1` |
| `no-shutdown` | 4 | u32×4 | [`/arm-io/aop/iop-aop-nub`](../devicetree/root__arm-io__aop__iop-aop-nub.md) = `0x1`<br>[`/arm-io/aop2/iop-aop2-nub`](../devicetree/root__arm-io__aop2__iop-aop2-nub.md) = `0x1`<br>[`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0x1`<br>[`/arm-io/smc/iop-smc-nub`](../devicetree/root__arm-io__smc__iop-smc-nub.md) = `0x1` |
| `node` | 4 | string×4 | [`/osenvironments/recovery-environment/ephemeral-recovery-data-volume`](../devicetree/root__osenvironments__recovery-environment__ephemeral-recovery-data-volume.md) = `fstab`<br>[`/osenvironments/diagnostics-environment/ephemeral-diag-data-volume`](../devicetree/root__osenvironments__diagnostics-environment__ephemeral-diag-data-volume.md) = `fstab`<br>[`/osenvironments/darwinos-ramdisk-environment/ephemeral-recovery-data-volume`](../devicetree/root__osenvironments__darwinos-ramdisk-environment__ephemeral-recovery-data-volume.md) = `fstab`<br>[`/osenvironments/device-recovery-environment/ephemeral-devrecov-data-volume`](../devicetree/root__osenvironments__device-recovery-environment__ephemeral-devrecov-data-volume.md) = `fstab` |
| `node_path` | 27 | string×27 | [`/osenvironments/recovery-environment/ephemeral-storage`](../devicetree/root__osenvironments__recovery-environment__ephemeral-storage.md) = `chosen`<br>[`/osenvironments/recovery-environment/no-sepfw-load-at-boot`](../devicetree/root__osenvironments__recovery-environment__no-sepfw-load-at-boot.md) = `chosen`<br>[`/osenvironments/recovery-environment/no-protected-data-access`](../devicetree/root__osenvironments__recovery-environment__no-protected-data-access.md) = `chosen`<br>[`/osenvironments/recovery-environment/amfi-allows-trust-cache-load`](../devicetree/root__osenvironments__recovery-environment__amfi-allows-trust-cache-load.md) = `chosen`<br>[`/osenvironments/recovery-environment/disable-av-content-protection`](../devicetree/root__osenvironments__recovery-environment__disable-av-content-protection.md) = `chosen` |
| `non-auth-personality` | 2 | string×2 | [`/arm-io/mtp/iop-mtp-nub/multi-touch2`](../devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch2.md) = `non-auth`<br>[`/arm-io/mtp/iop-mtp-nub/multi-touch`](../devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch.md) = `non-auth` |
| `nova-force-cal` | 1 | string | [`/arm-io/mtp/iop-mtp-nub/nova`](../devicetree/root__arm-io__mtp__iop-mtp-nub__nova.md) = `syscfg/NvFc` |
| `nova-touch-cal` | 1 | string | [`/arm-io/mtp/iop-mtp-nub/nova`](../devicetree/root__arm-io__mtp__iop-mtp-nub__nova.md) = `syscfg/NvTh` |
| `nub-aic-irq-aggr-cfg` | 1 | 12 B | [`/arm-io/soc-misc`](../devicetree/root__arm-io__soc-misc.md) = `000000000000000001000000` |
| `nub-fr-global-metadata` | 1 | 12 B | [`/arm-io/soc-misc`](../devicetree/root__arm-io__soc-misc.md) = `7266626e0300000001000000` |
| `number-of-batteries` | 1 | u32 | [`/arm-io/nub-spmi0/btm`](../devicetree/root__arm-io__nub-spmi0__btm.md) = `0x2` |
| `number-of-battery-packs` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x2` |
| `number-of-ca-flipbooks` | 1 | u32 | [`/backlight`](../devicetree/root__backlight.md) = `0x1` |
| `number-of-PMUs` | 1 | u32 | [`/arm-io/nub-spmi0/btm`](../devicetree/root__arm-io__nub-spmi0__btm.md) = `0x2` |
| `nvme-ans-ppm-budget` | 1 | u32 | [`/arm-io/ans`](../devicetree/root__arm-io__ans.md) = `0xbb8` |
| `nvme-ans-selected-hash-type` | 1 | string | [`/arm-io/ans`](../devicetree/root__arm-io__ans.md) = `SHA3-256-4K` |
| `nvme-ans-sha-present` | 1 | empty | [`/arm-io/ans`](../devicetree/root__arm-io__ans.md) = `` |
| `nvme-ans-supported-hash-types` | 1 | string | [`/arm-io/ans`](../devicetree/root__arm-io__ans.md) = `SHA3-256-4K:SHA3-384-4K:SHA3-512-4K` |
| `nvme-iboot-sptm-security` | 1 | empty | [`/defaults`](../devicetree/root__defaults.md) = `` |
| `nvme-interrupt-idx` | 1 | u32 | [`/arm-io/ans`](../devicetree/root__arm-io__ans.md) = `0x3` |
| `nvme-linear-sq` | 1 | empty | [`/arm-io/ans`](../devicetree/root__arm-io__ans.md) = `` |
| `nvme-queue-entries` | 1 | u32 | [`/arm-io/ans`](../devicetree/root__arm-io__ans.md) = `0x40` |
| `nvme-secure-reg-layout` | 1 | empty | [`/arm-io/ans`](../devicetree/root__arm-io__ans.md) = `` |
| `nvram-bank-count` | 1 | u32 | [`/chosen`](../devicetree/root__chosen.md) = `0x0` |
| `nvram-bank-size` | 1 | u32 | [`/chosen`](../devicetree/root__chosen.md) = `0x0` |
| `nvram-current-bank` | 1 | u32 | [`/chosen`](../devicetree/root__chosen.md) = `0x0` |
| `nvram-proxy-data` | 1 | 8192 B | [`/chosen`](../devicetree/root__chosen.md) = `00000000000000000000000000000000…` |
| `occlusion-drives-grimaldi` | 1 | u32 | [`/arm-io/aop/iop-aop-nub/als`](../devicetree/root__arm-io__aop__iop-aop-nub__als.md) = `0x1` |
| `offline-dictation` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `oled-display` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `opengl-standard` | 1 | u32 | [`/arm-io/sgx`](../devicetree/root__arm-io__sgx.md) = `0x300` |
| `option` | 1 | string | [`/:borneo`](../devicetree/root___borneo.md) = `h19p, h19a` |
| `os_env_type` | 4 | u32×4 | [`/filesystems/fstab`](../devicetree/root__filesystems__fstab.md) = `0x1`<br>[`/filesystems/fstab-ephemeral-recovery-data`](../devicetree/root__filesystems__fstab-ephemeral-recovery-data.md) = `0x2`<br>[`/filesystems/fstab-ephemeral-diag-data`](../devicetree/root__filesystems__fstab-ephemeral-diag-data.md) = `0x3`<br>[`/filesystems/fstab-ephemeral-devrecov-data`](../devicetree/root__filesystems__fstab-ephemeral-devrecov-data.md) = `0x9` |
| `osenvironment` | 1 | 32 B | [`/chosen`](../devicetree/root__chosen.md) = `00000000000000000000000000000000…` |
| `other-interrupts` | 5 | 12 B×5 | [`/arm-io/nub-spmi0`](../devicetree/root__arm-io__nub-spmi0.md) = `06010000070100000b010000`<br>[`/arm-io/nub-spmi1`](../devicetree/root__arm-io__nub-spmi1.md) = `06010000070100000b010000`<br>[`/arm-io/nub-spmi2`](../devicetree/root__arm-io__nub-spmi2.md) = `06010000070100000b010000`<br>[`/arm-io/aop-spmi0`](../devicetree/root__arm-io__aop-spmi0.md) = `06010000070100000b010000`<br>[`/arm-io/aop-spmi1`](../devicetree/root__arm-io__aop-spmi1.md) = `06010000070100000b010000` |
| `output-data-source-selectors` | 1 | u64 | [`/arm-io/iop-audio-controller/audio-speaker`](../devicetree/root__arm-io__iop-audio-controller__audio-speaker.md) = `0x546f7053426f7453` |
| `output-latency` | 2 | u32×2 | [`/arm-io/iop-audio-controller/audio-haptic`](../devicetree/root__arm-io__iop-audio-controller__audio-haptic.md) = `0x8`<br>[`/arm-io/iop-audio-controller/audio-hpdbg`](../devicetree/root__arm-io__iop-audio-controller__audio-hpdbg.md) = `0x5` |
| `p3-color-space-video-recording` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x1` |
| `paa-sdr-lut` | 1 | 12 B | [`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0080544400007a4400808444` |
| `pack-format-enabled` | 1 | u32 | [`/arm-io/nub-spmi0/btm`](../devicetree/root__arm-io__nub-spmi0__btm.md) = `0x1` |
| `page-size` | 27 | u32×27 | [`/arm-io/dart-sep`](../devicetree/root__arm-io__dart-sep.md) = `0x4000`<br>[`/arm-io/dart-sio`](../devicetree/root__arm-io__dart-sio.md) = `0x4000`<br>[`/arm-io/dart-sbr`](../devicetree/root__arm-io__dart-sbr.md) = `0x4000`<br>[`/arm-io/i2c3/display-eeprom`](../devicetree/root__arm-io__i2c3__display-eeprom.md) = `0x20`<br>[`/arm-io/i2c3/display-eeprom-hi`](../devicetree/root__arm-io__i2c3__display-eeprom-hi.md) = `0x20` |
| `panel-gamma` | 1 | u32 | [`/exbright`](../devicetree/root__exbright.md) = `0x898` |
| `panel-typical-freq` | 1 | u32 | [`/exbright`](../devicetree/root__exbright.md) = `0x78` |
| `panic-on-event-log-intr` | 1 | u32 | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) = `0x1` |
| `panic-on-missing-event-log` | 1 | u32 | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) = `0x1` |
| `panic-reset-type` | 1 | u32 | [`/defaults`](../devicetree/root__defaults.md) = `0x2` |
| `panic-save-flag-bit` | 1 | u32 | [`/arm-io/wdt`](../devicetree/root__arm-io__wdt.md) = `0x0` |
| `panic-save-reg-idx` | 1 | u32 | [`/arm-io/mcc`](../devicetree/root__arm-io__mcc.md) = `0x0` |
| `panic-trace-mode` | 1 | u32 | [`/arm-io/cpu-debug-interface`](../devicetree/root__arm-io__cpu-debug-interface.md) = `0x24` |
| `panorama` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x1` |
| `parent` | 4 | string×4 | [`/osenvironments/recovery-environment/ephemeral-recovery-data-volume`](../devicetree/root__osenvironments__recovery-environment__ephemeral-recovery-data-volume.md) = `/filesystems`<br>[`/osenvironments/diagnostics-environment/ephemeral-diag-data-volume`](../devicetree/root__osenvironments__diagnostics-environment__ephemeral-diag-data-volume.md) = `/filesystems`<br>[`/osenvironments/darwinos-ramdisk-environment/ephemeral-recovery-data-volume`](../devicetree/root__osenvironments__darwinos-ramdisk-environment__ephemeral-recovery-data-volume.md) = `/filesystems`<br>[`/osenvironments/device-recovery-environment/ephemeral-devrecov-data-volume`](../devicetree/root__osenvironments__device-recovery-environment__ephemeral-devrecov-data-volume.md) = `/filesystems` |
| `parking-node-id` | 1 | u32 | [`/arm-io/iop-audio-controller/audio-haptic-leap`](../devicetree/root__arm-io__iop-audio-controller__audio-haptic-leap.md) = `0x70726b4e` |
| `parrot-port-number` | 1 | u32 | [`/arm-io/usb-drd0`](../devicetree/root__arm-io__usb-drd0.md) = `0xff` |
| `partition-style` | 1 | string | [`/product`](../devicetree/root__product.md) = `iOS` |
| `pcc-table` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x3`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x3`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x3` |
| `pci-aer-correctable` | 1 | u32 | [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) = `0x0` |
| `pci-aer-uncorrectable` | 1 | u32 | [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) = `0x1` |
| `pci-aspm-default` | 5 | u32×5 | [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) = `0x2`<br>[`/arm-io/apcie/pci-bridge0/centauri-control`](../devicetree/root__arm-io__apcie__pci-bridge0__centauri-control.md) = `0x2`<br>[`/arm-io/apcie/pci-bridge0/centauri-alpha`](../devicetree/root__arm-io__apcie__pci-bridge0__centauri-alpha.md) = `0x2`<br>[`/arm-io/apcie/pci-bridge0/centauri-beta`](../devicetree/root__arm-io__apcie__pci-bridge0__centauri-beta.md) = `0x2`<br>[`/arm-io/apcie/pci-bridge1/baseband-pcie-leda`](../devicetree/root__arm-io__apcie__pci-bridge1__baseband-pcie-leda.md) = `0x2` |
| `pci-bridge-handle` | 1 | string | [`/centauri`](../devicetree/root__centauri.md) = `/arm-io/apcie/pci-bridge0` |
| `pci-l1ss-enable` | 4 | u32×4 | [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) = `0x4055000f`<br>[`/arm-io/apcie/pci-bridge0/centauri-control`](../devicetree/root__arm-io__apcie__pci-bridge0__centauri-control.md) = `0x4055000f`<br>[`/arm-io/apcie/pci-bridge1`](../devicetree/root__arm-io__apcie__pci-bridge1.md) = `0x4055000f`<br>[`/arm-io/apcie/pci-bridge1/baseband-pcie-leda`](../devicetree/root__arm-io__apcie__pci-bridge1__baseband-pcie-leda.md) = `0x4055000f` |
| `pci-max-latency` | 5 | u32×5 | [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) = `0x10081008`<br>[`/arm-io/apcie/pci-bridge0/centauri-control`](../devicetree/root__arm-io__apcie__pci-bridge0__centauri-control.md) = `0x10081008`<br>[`/arm-io/apcie/pci-bridge0/centauri-alpha`](../devicetree/root__arm-io__apcie__pci-bridge0__centauri-alpha.md) = `0x10081008`<br>[`/arm-io/apcie/pci-bridge0/centauri-beta`](../devicetree/root__arm-io__apcie__pci-bridge0__centauri-beta.md) = `0x10081008`<br>[`/arm-io/apcie/pci-bridge1/baseband-pcie-leda`](../devicetree/root__arm-io__apcie__pci-bridge1__baseband-pcie-leda.md) = `0x10081008` |
| `pci-max-payload-size` | 1 | u32 | [`/arm-io/apcie/pci-bridge1`](../devicetree/root__arm-io__apcie__pci-bridge1.md) = `0x1` |
| `pci-msi-flags` | 1 | u32 | [`/arm-io/apcie/pci-bridge1/baseband-pcie-leda`](../devicetree/root__arm-io__apcie__pci-bridge1__baseband-pcie-leda.md) = `0x1` |
| `pci-msi-limit` | 1 | u32 | [`/arm-io/apcie/pci-bridge1/baseband-pcie-leda`](../devicetree/root__arm-io__apcie__pci-bridge1__baseband-pcie-leda.md) = `0x8` |
| `pci-skip-rematch-reset` | 3 | empty×3 | [`/arm-io/apcie/pci-bridge0/centauri-control`](../devicetree/root__arm-io__apcie__pci-bridge0__centauri-control.md) = ``<br>[`/arm-io/apcie/pci-bridge0/centauri-alpha`](../devicetree/root__arm-io__apcie__pci-bridge0__centauri-alpha.md) = ``<br>[`/arm-io/apcie/pci-bridge0/centauri-beta`](../devicetree/root__arm-io__apcie__pci-bridge0__centauri-beta.md) = `` |
| `pcie-nand-boot-supported` | 1 | empty | [`/defaults`](../devicetree/root__defaults.md) = `` |
| `peak-power-range` | 1 | 12 B | [`/arm-io/iop-audio-controller/audio-haptic`](../devicetree/root__arm-io__iop-audio-controller__audio-haptic.md) = `441600003405000044160000` |
| `pearl-calibration-data` | 2 | string×2 | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) = `syscfg/PrCL`<br>[`/arm-io/isp`](../devicetree/root__arm-io__isp.md) = `syscfg/PrCL` |
| `perf-counters` | 2 | 1984 B, 30272 B | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `03008503000000000004000000050000…`<br>[`/arm-io/soc-reporter`](../devicetree/root__arm-io__soc-reporter.md) = `04000100010000000001000000000000…` |
| `perf-domains` | 1 | 196 B | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `000000010000000000000000534f4300…` |
| `perf-groups` | 2 | 252 B×2 | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0200000000c003000100000010000000…`<br>[`/arm-io/soc-reporter`](../devicetree/root__arm-io__soc-reporter.md) = `0200000000c003000100000010000000…` |
| `perf-state-boost-route` | 1 | 112 B | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `80020000000003008002000001000300…` |
| `perf-state-count` | 1 | u32 | [`/arm-io/sgx`](../devicetree/root__arm-io__sgx.md) = `0x0` |
| `perf-states` | 1 | 128 B | [`/arm-io/sgx`](../devicetree/root__arm-io__sgx.md) = `00000000000000000000000000000000…` |
| `personal-hotspot` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `perst-to-config` | 2 | u32×2 | [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) = `0x1`<br>[`/arm-io/apcie/pci-bridge1`](../devicetree/root__arm-io__apcie__pci-bridge1.md) = `0x1` |
| `phi-attach-high-cal` | 1 | u32 | [`/arm-io/aop/iop-aop-nub/jarvis`](../devicetree/root__arm-io__aop__iop-aop-nub__jarvis.md) = `0x323d7` |
| `phi-attach-low-cal` | 1 | u32 | [`/arm-io/aop/iop-aop-nub/jarvis`](../devicetree/root__arm-io__aop__iop-aop-nub__jarvis.md) = `0xfffcdc29` |
| `phi-detach-high-cal` | 1 | u32 | [`/arm-io/aop/iop-aop-nub/jarvis`](../devicetree/root__arm-io__aop__iop-aop-nub__jarvis.md) = `0x647ae` |
| `phi-detach-low-cal` | 1 | u32 | [`/arm-io/aop/iop-aop-nub/jarvis`](../devicetree/root__arm-io__aop__iop-aop-nub__jarvis.md) = `0xfff9b852` |
| `phi-ignore-high-cal` | 1 | u32 | [`/arm-io/aop/iop-aop-nub/jarvis`](../devicetree/root__arm-io__aop__iop-aop-nub__jarvis.md) = `0x323d7` |
| `phi-ignore-low-cal` | 1 | u32 | [`/arm-io/aop/iop-aop-nub/jarvis`](../devicetree/root__arm-io__aop__iop-aop-nub__jarvis.md) = `0x0` |
| `photo-capture-on-touch-down` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x1` |
| `photon-detector-cal-data` | 2 | string×2 | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) = `syscfg/RACa`<br>[`/arm-io/isp`](../devicetree/root__arm-io__isp.md) = `syscfg/RACa` |
| `photon-detector-cal-data-offset` | 2 | string×2 | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) = `syscfg/RACm`<br>[`/arm-io/isp`](../devicetree/root__arm-io__isp.md) = `syscfg/RACm` |
| `photos-live-video-rendering` | 1 | empty | [`/product/camera`](../devicetree/root__product__camera.md) = `` |
| `physical-descriptions` | 5 | 24 B×5 | [`/arm-io/iop-audio-controller/lp-mic-io-buffer-device`](../devicetree/root__arm-io__iop-audio-controller__lp-mic-io-buffer-device.md) = `00fa0000803e00006d63706c0c000000…`<br>[`/arm-io/audio-speaker-tx-stream-proxy`](../devicetree/root__arm-io__audio-speaker-tx-stream-proxy.md) = `e03d000080bb00006d63706c0c000000…`<br>[`/arm-io/audio-receiver-tx-stream-proxy`](../devicetree/root__arm-io__audio-receiver-tx-stream-proxy.md) = `e03d000080bb00006d63706c04000000…`<br>[`/arm-io/audio-sllb-proxy`](../devicetree/root__arm-io__audio-sllb-proxy.md) = `e03d000080bb00006d63706c09000000…`<br>[`/arm-io/audio-hp-proxy`](../devicetree/root__arm-io__audio-hp-proxy.md) = `e03d000080bb00006d63706c04000000…` |
| `pio-dst-filt-fr-global` | 1 | u32 | [`/arm-io/aop/iop-aop-nub/aop-pio-filters`](../devicetree/root__arm-io__aop__iop-aop-nub__aop-pio-filters.md) = `0x3a` |
| `pio-dst-filt-global` | 1 | u32 | [`/arm-io/aop/iop-aop-nub/aop-pio-filters`](../devicetree/root__arm-io__aop__iop-aop-nub__aop-pio-filters.md) = `0x0` |
| `pio-src-filt-global` | 1 | u32 | [`/arm-io/aop/iop-aop-nub/aop-pio-filters`](../devicetree/root__arm-io__aop__iop-aop-nub__aop-pio-filters.md) = `0xa` |
| `pio-vm-base` | 1 | u64 | [`/arm-io/pmp`](../devicetree/root__arm-io__pmp.md) = `0xc0000000` |
| `pio-vm-size` | 1 | string | [`/arm-io/pmp`](../devicetree/root__arm-io__pmp.md) = `@` |
| `piodma-base-address` | 2 | 24 B×2 | [`/arm-io/apcie0-piodma`](../devicetree/root__arm-io__apcie0-piodma.md) = `000000b01c000000000000c00b000000…`<br>[`/arm-io/apcie1-piodma`](../devicetree/root__arm-io__apcie1-piodma.md) = `000000b01c000000000000c00b000000…` |
| `piodma-byte-alignment` | 2 | u32×2 | [`/arm-io/apcie0-piodma`](../devicetree/root__arm-io__apcie0-piodma.md) = `0x10`<br>[`/arm-io/apcie1-piodma`](../devicetree/root__arm-io__apcie1-piodma.md) = `0x10` |
| `piodma-fifo-size` | 2 | u32×2 | [`/arm-io/apcie0-piodma`](../devicetree/root__arm-io__apcie0-piodma.md) = `0x10`<br>[`/arm-io/apcie1-piodma`](../devicetree/root__arm-io__apcie1-piodma.md) = `0x10` |
| `piodma-id` | 2 | u32×2 | [`/arm-io/apcie0-piodma`](../devicetree/root__arm-io__apcie0-piodma.md) = `0x0`<br>[`/arm-io/apcie1-piodma`](../devicetree/root__arm-io__apcie1-piodma.md) = `0x1` |
| `piodma-max-segment-size` | 2 | u32×2 | [`/arm-io/apcie0-piodma`](../devicetree/root__arm-io__apcie0-piodma.md) = `0x0`<br>[`/arm-io/apcie1-piodma`](../devicetree/root__arm-io__apcie1-piodma.md) = `0x0` |
| `piodma-max-transfer-size` | 2 | u32×2 | [`/arm-io/apcie0-piodma`](../devicetree/root__arm-io__apcie0-piodma.md) = `0x80`<br>[`/arm-io/apcie1-piodma`](../devicetree/root__arm-io__apcie1-piodma.md) = `0x80` |
| `piodma-num-address-bits` | 2 | u32×2 | [`/arm-io/apcie0-piodma`](../devicetree/root__arm-io__apcie0-piodma.md) = `0x2a`<br>[`/arm-io/apcie1-piodma`](../devicetree/root__arm-io__apcie1-piodma.md) = `0x2a` |
| `pipelined-stillimage-capability` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x1` |
| `pkg-1s-spl-dcs-c0` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x0` |
| `pkg-1s-spl-dcs-c1` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x4000` |
| `pkg-1s-spl-dcs-c2` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0xb333` |
| `pkg-1s-spl-dcs-c3` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x10000` |
| `pkg-avg-limiter-input-tc` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x384` |
| `pkg-avg-limiter-ki` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0xd1b` |
| `pkg-avg-limiter-kp` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x28f5c` |
| `pkg-avg-limiter-target-tc` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x0` |
| `pkg-avg-max-power` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x38d9db` |
| `pkg-avg-therm-power-target-tc` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0xfa` |
| `pkg-dynamic-split-mode` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x2` |
| `pkg-dynamic-split-seed-on` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x1` |
| `pkg-low-power-target-tc` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x64` |
| `pkg-lowpeak-limiter-input-tc` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x3c` |
| `pkg-lowpeak-limiter-ki` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x96bc` |
| `pkg-lowpeak-limiter-kp` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x1d14e` |
| `pkg-lowpeak-limiter-target-tc` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x0` |
| `pkg-lowpeak-max-power` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x38d9db` |
| `pkg-lpm-power-target` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x2000000` |
| `pkg-lpm-power-target-B` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x2000000` |
| `pkg-peak-power-target-tc` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0xa` |
| `pkg-power-limit-is-effort` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x1` |
| `pkg-power-limit-spl-cpu-c0` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x0` |
| `pkg-power-limit-spl-cpu-t1` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x175c29` |
| `pkg-power-limit-spl-cpu-t2` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x175c29` |
| `pkg-power-limit-spl-gpu-c0` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x0` |
| `pkg-power-limit-spl-gpu-t1` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x175c29` |
| `pkg-power-limit-spl-gpu-t2` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x175c29` |
| `pkg-power-limit-spl-t0` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x31eb8` |
| `pkg-power-limit-spl-t3` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x175c29` |
| `pkg-power-zone-filter-tc-0` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0xea60` |
| `pkg-power-zone-target-0` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0xff0000` |
| `pkg-power-zone-target-offset-0` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x199a` |
| `pkg-sustainable-power-target` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x36666` |
| `pkg-sustainable-power-target-B` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x4b333` |
| `platform-name` | 1 | 32 B | [`/`](../devicetree/root.md) = `00000000000000000000000000000000…` |
| `plce-link-init0-script` | 2 | u32×2 | [`/arm-io/apcie0-plce`](../devicetree/root__arm-io__apcie0-plce.md) = `0x0`<br>[`/arm-io/apcie1-plce`](../devicetree/root__arm-io__apcie1-plce.md) = `0x0` |
| `plce-link-init1-script` | 2 | u32×2 | [`/arm-io/apcie0-plce`](../devicetree/root__arm-io__apcie0-plce.md) = `0x1`<br>[`/arm-io/apcie1-plce`](../devicetree/root__arm-io__apcie1-plce.md) = `0x1` |
| `plce-link-restore-script` | 2 | u32×2 | [`/arm-io/apcie0-plce`](../devicetree/root__arm-io__apcie0-plce.md) = `0x2`<br>[`/arm-io/apcie1-plce`](../devicetree/root__arm-io__apcie1-plce.md) = `0x2` |
| `plce-link-shutdown-script` | 2 | u32×2 | [`/arm-io/apcie0-plce`](../devicetree/root__arm-io__apcie0-plce.md) = `0x5f`<br>[`/arm-io/apcie1-plce`](../devicetree/root__arm-io__apcie1-plce.md) = `0x5f` |
| `plce-link-teardown-script` | 2 | u32×2 | [`/arm-io/apcie0-plce`](../devicetree/root__arm-io__apcie0-plce.md) = `0x5e`<br>[`/arm-io/apcie1-plce`](../devicetree/root__arm-io__apcie1-plce.md) = `0x5e` |
| `plce-num-scripts` | 2 | u32×2 | [`/arm-io/apcie0-plce`](../devicetree/root__arm-io__apcie0-plce.md) = `0x60`<br>[`/arm-io/apcie1-plce`](../devicetree/root__arm-io__apcie1-plce.md) = `0x60` |
| `plt-logic-version` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x1`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x2`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x2` |
| `pm-ptd-ranges` | 1 | 64 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `01000000020000000300000004000000…` |
| `pmap-io-filters` | 1 | 144 B | [`/defaults`](../devicetree/root__defaults.md) = `50434d412c08040050434d41680b0400…` |
| `pmap-io-ranges` | 1 | 2544 B | [`/defaults`](../devicetree/root__defaults.md) = `000000c00b0000000000002000000000…` |
| `pmc` | 2 | u32×2 | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0x1`<br>[`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) = `0x1` |
| `pmc-ltr-ka` | 2 | u32×2 | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0x1`<br>[`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) = `0x1` |
| `pmc-pmgr` | 2 | u32×2 | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0x1f`<br>[`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) = `0x1f` |
| `pmc-sac-dcs-offset` | 1 | u32 | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0x1c5c28` |
| `pmgr-aon-cps-metadata` | 1 | 12 B | [`/arm-io/soc-misc`](../devicetree/root__arm-io__soc-misc.md) = `207370630200000001000000` |
| `pmgr-aon-security-metadata` | 1 | 12 B | [`/arm-io/soc-misc`](../devicetree/root__arm-io__soc-misc.md) = `207361700100000001000000` |
| `pmgr-ver` | 1 | u32 | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) = `0x2` |
| `pmgr_ced_die0` | 2 | u32×2 | [`/ced-ssw/ced_tunable_mask`](../devicetree/root__ced-ssw__ced_tunable_mask.md) = `0x0`<br>[`/ced-ssw/ced_disable_mask`](../devicetree/root__ced-ssw__ced_disable_mask.md) = `0x0` |
| `pmgr_ced_die1` | 2 | u32×2 | [`/ced-ssw/ced_tunable_mask`](../devicetree/root__ced-ssw__ced_tunable_mask.md) = `0x1c`<br>[`/ced-ssw/ced_disable_mask`](../devicetree/root__ced-ssw__ced_disable_mask.md) = `0xe` |
| `pmgrtools-version` | 1 | u32 | [`/arm-io/pmgr/pmgrtools`](../devicetree/root__arm-io__pmgr__pmgrtools.md) = `0x1` |
| `pmp` | 1 | u32 | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) = `0x2` |
| `pmp-voter-agent-idx` | 1 | u32 | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0x0` |
| `pmp_ptd_db_reg_idx` | 1 | u32 | [`/arm-io/mcc`](../devicetree/root__arm-io__mcc.md) = `0x6` |
| `pmp_ptd_update_reg_idx` | 1 | u32 | [`/arm-io/mcc`](../devicetree/root__arm-io__mcc.md) = `0x7` |
| `PMU-pmax-sampling-enabled` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x1` |
| `pmu_mcom_offset_L1DY` | 1 | u32 | [`/arm-io/pmgr/pmgrtools`](../devicetree/root__arm-io__pmgr__pmgrtools.md) = `0x2b60` |
| `policy` | 1 | u32 | [`/arm-io/sapt`](../devicetree/root__arm-io__sapt.md) = `0x2` |
| `policy-allow-accessory` | 1 | u32 | [`/arm-io/eic`](../devicetree/root__arm-io__eic.md) = `0x1` |
| `policy-allow-prox-suppression` | 1 | u32 | [`/arm-io/eic`](../devicetree/root__arm-io__eic.md) = `0x1` |
| `policy-alt-indicator` | 1 | u32 | [`/arm-io/eic`](../devicetree/root__arm-io__eic.md) = `0x1` |
| `policy-override-chill-pill` | 1 | u32 | [`/arm-io/eic`](../devicetree/root__arm-io__eic.md) = `0x3e8` |
| `policy-sensor-control` | 1 | u32 | [`/arm-io/eic`](../devicetree/root__arm-io__eic.md) = `0x0` |
| `populate-registry-time` | 1 | u32 | [`/chosen/iBoot`](../devicetree/root__chosen__iBoot.md) = `0x0` |
| `port-id` | 2 | u32×2 | [`/arm-io/apcie0-plce`](../devicetree/root__arm-io__apcie0-plce.md) = `0x0`<br>[`/arm-io/apcie1-plce`](../devicetree/root__arm-io__apcie1-plce.md) = `0x1` |
| `port-number` | 13 | u32×13 | [`/arm-io/smc/iop-smc-nub/smc-charger`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-charger.md) = `0x1`<br>[`/arm-io/smc/iop-smc-nub/smc-ext-charger`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-ext-charger.md) = `0x1`<br>[`/arm-io/smc/iop-smc-nub/smc-charger-util`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-charger-util.md) = `0x1`<br>[`/arm-io/rsm`](../devicetree/root__arm-io__rsm.md) = `0x1`<br>[`/arm-io/nub-spmi2/spmi-hpm0`](../devicetree/root__arm-io__nub-spmi2__spmi-hpm0.md) = `0x1` |
| `port-type` | 13 | u32×13 | [`/arm-io/smc/iop-smc-nub/smc-charger`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-charger.md) = `0x2`<br>[`/arm-io/smc/iop-smc-nub/smc-ext-charger`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-ext-charger.md) = `0x9`<br>[`/arm-io/smc/iop-smc-nub/smc-charger-util`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-charger-util.md) = `0x2`<br>[`/arm-io/rsm`](../devicetree/root__arm-io__rsm.md) = `0x2`<br>[`/arm-io/nub-spmi2/spmi-hpm0`](../devicetree/root__arm-io__nub-spmi2__spmi-hpm0.md) = `0x2` |
| `portrait-lighting-strength` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x1` |
| `post-effects` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x1` |
| `power-canary-offset` | 1 | u32 | [`/arm-io/sart-ans`](../devicetree/root__arm-io__sart-ans.md) = `0x0` |
| `power-control-features` | 1 | u32 | [`/product/haptics`](../devicetree/root__product__haptics.md) = `0x2` |
| `power-gates` | 23 | u32×12, empty×6, u64×3 | [`/arm-io/aop`](../devicetree/root__arm-io__aop.md) = ``<br>[`/arm-io/aop2`](../devicetree/root__arm-io__aop2.md) = ``<br>[`/arm-io/pmp`](../devicetree/root__arm-io__pmp.md) = `0x9800000097`<br>[`/arm-io/sep`](../devicetree/root__arm-io__sep.md) = ``<br>[`/arm-io/sio`](../devicetree/root__arm-io__sio.md) = `0x18` |
| `power-lut-data-lut` | 2 | 2352 B×2 | [`/arm-io/disp0`](../devicetree/root__arm-io__disp0.md) = `2e0000002e0000002e0000002e000000…`<br>[`/arm-io/dispsec`](../devicetree/root__arm-io__dispsec.md) = `6a0000006a0000006a0000006a000000…` |
| `power-lut-data-x` | 2 | u32×2 | [`/arm-io/disp0`](../devicetree/root__arm-io__disp0.md) = `0x1c`<br>[`/arm-io/dispsec`](../devicetree/root__arm-io__dispsec.md) = `0x1c` |
| `power-lut-data-xindex` | 2 | 112 B×2 | [`/arm-io/disp0`](../devicetree/root__arm-io__disp0.md) = `04000000080000000f00000017000000…`<br>[`/arm-io/dispsec`](../devicetree/root__arm-io__dispsec.md) = `04000000080000000f00000017000000…` |
| `power-lut-data-y` | 2 | u32×2 | [`/arm-io/disp0`](../devicetree/root__arm-io__disp0.md) = `0x15`<br>[`/arm-io/dispsec`](../devicetree/root__arm-io__dispsec.md) = `0x15` |
| `power-lut-data-yindex` | 2 | 84 B×2 | [`/arm-io/disp0`](../devicetree/root__arm-io__disp0.md) = `00000000050000000a0000000f000000…`<br>[`/arm-io/dispsec`](../devicetree/root__arm-io__dispsec.md) = `00000000050000000a0000000f000000…` |
| `power-lut-vbatt-cur-nominal` | 2 | u32×2 | [`/arm-io/disp0`](../devicetree/root__arm-io__disp0.md) = `0x13b`<br>[`/arm-io/dispsec`](../devicetree/root__arm-io__dispsec.md) = `0x294` |
| `power-managed` | 2 | u32, string | [`/arm-io/ans/iop-ans-nub`](../devicetree/root__arm-io__ans__iop-ans-nub.md) = `0x1`<br>[`/arm-io/gfx1-asc/iop-gfx1-nub`](../devicetree/root__arm-io__gfx1-asc__iop-gfx1-nub.md) = `true` |
| `power-off-delay` | 1 | u32 | [`/arm-io/spi1/mesa`](../devicetree/root__arm-io__spi1__mesa.md) = `0xa` |
| `power-on-delay` | 1 | u32 | [`/arm-io/spi1/mesa`](../devicetree/root__arm-io__spi1__mesa.md) = `0x7` |
| `powered-on-state` | 2 | u32×2 | [`/arm-io/iop-audio-controller/audio-haptic`](../devicetree/root__arm-io__iop-audio-controller__audio-haptic.md) = `0x70777264`<br>[`/arm-io/iop-audio-controller/audio-hpdbg`](../devicetree/root__arm-io__iop-audio-controller__audio-hpdbg.md) = `0x70777264` |
| `ppm-idle-budget` | 1 | u32 | [`/baseband`](../devicetree/root__baseband.md) = `0xa` |
| `ppm-low-budget` | 1 | u32 | [`/baseband`](../devicetree/root__baseband.md) = `0x1` |
| `ppm-max-budget` | 1 | u32 | [`/baseband`](../devicetree/root__baseband.md) = `0x2710` |
| `pre-loaded` | 1 | u32 | [`/arm-io/smc/iop-smc-nub`](../devicetree/root__arm-io__smc__iop-smc-nub.md) = `0x0` |
| `predictive-horizon-pmax` | 1 | 384 B | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `050000007a010000220b000020000000…` |
| `pref-decoding` | 1 | u64 | [`/product/facetime`](../devicetree/root__product__facetime.md) = `0x300001e00000400` |
| `pressure-global-offset-cal` | 1 | u32 | [`/arm-io/aop/iop-aop-nub/pressure`](../devicetree/root__arm-io__aop__iop-aop-nub__pressure.md) = `0x1f00` |
| `pressure-heater-resistance` | 1 | u32 | [`/arm-io/aop/iop-aop-nub/pressure`](../devicetree/root__arm-io__aop__iop-aop-nub__pressure.md) = `0x153d8` |
| `pressure-offset-calibration` | 1 | string | [`/arm-io/aop/iop-aop-nub/pressure`](../devicetree/root__arm-io__aop__iop-aop-nub__pressure.md) = `syscfg/SPPO` |
| `prewarm-on-state` | 1 | u32 | [`/arm-io/iop-audio-controller/audio-haptic`](../devicetree/root__arm-io__iop-audio-controller__audio-haptic.md) = `0x70773120` |
| `primary` | 2 | u32×2 | [`/arm-io/disp0`](../devicetree/root__arm-io__disp0.md) = `0x0`<br>[`/arm-io/dispsec`](../devicetree/root__arm-io__dispsec.md) = `0x1` |
| `primary-calibration-matrix` | 1 | string | [`/product`](../devicetree/root__product.md) = `syscfg/DPCl` |
| `primary-port-id` | 2 | u32×2 | [`/port-usb-c-1`](../devicetree/root__port-usb-c-1.md) = `0x2`<br>[`/port-magsafe-1`](../devicetree/root__port-magsafe-1.md) = `0x200` |
| `private` | 4 | string×4 | [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) = `1`<br>[`/arm-io/iop-audio-controller/audio-receiver/audio-receiver`](../devicetree/root__arm-io__iop-audio-controller__audio-receiver__audio-receiver.md) = `1`<br>[`/arm-io/iop-audio-controller/audio-s-leap-internal-loopback/audio-s-leap-internal-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-s-leap-internal-loopback__audio-s-leap-internal-loopback.md) = `1`<br>[`/arm-io/iop-audio-controller/audio-speaker`](../devicetree/root__arm-io__iop-audio-controller__audio-speaker.md) = `1` |
| `probe-port` | 3 | u32×3 | [`/arm-io/aod2`](../devicetree/root__arm-io__aod2.md) = `0x1eca`<br>[`/arm-io/aod3`](../devicetree/root__arm-io__aod3.md) = `0x1ecb`<br>[`/arm-io/aod4`](../devicetree/root__arm-io__aod4.md) = `0x1ecc` |
| `procedural-antialiasing` | 1 | empty | [`/arm-io/sgx`](../devicetree/root__arm-io__sgx.md) = `` |
| `product-description` | 1 | string | [`/product`](../devicetree/root__product.md) = `iPhone Duo` |
| `product-id` | 1 | 20 B | [`/product`](../devicetree/root__product.md) = `ab9bcb06823dfb24f5f48b41b5a7c41c…` |
| `product-name` | 1 | string | [`/product`](../devicetree/root__product.md) = `iPhone Duo` |
| `production-cert` | 1 | u32 | [`/chosen`](../devicetree/root__chosen.md) = `0x0` |
| `property_name` | 27 | string×27 | [`/osenvironments/recovery-environment/ephemeral-storage`](../devicetree/root__osenvironments__recovery-environment__ephemeral-storage.md) = `ephemeral-storage`<br>[`/osenvironments/recovery-environment/no-sepfw-load-at-boot`](../devicetree/root__osenvironments__recovery-environment__no-sepfw-load-at-boot.md) = `sepfw-load-at-boot`<br>[`/osenvironments/recovery-environment/no-protected-data-access`](../devicetree/root__osenvironments__recovery-environment__no-protected-data-access.md) = `protected-data-access`<br>[`/osenvironments/recovery-environment/amfi-allows-trust-cache-load`](../devicetree/root__osenvironments__recovery-environment__amfi-allows-trust-cache-load.md) = `amfi-allows-trust-cache-load`<br>[`/osenvironments/recovery-environment/disable-av-content-protection`](../devicetree/root__osenvironments__recovery-environment__disable-av-content-protection.md) = `disable-av-content-protection` |
| `protected-data-access` | 1 | u32 | [`/chosen`](../devicetree/root__chosen.md) = `0x1` |
| `protection-granularity` | 3 | u32×3 | [`/arm-io/dart-usb0`](../devicetree/root__arm-io__dart-usb0.md) = `0x10`<br>[`/arm-io/dart-apcie0`](../devicetree/root__arm-io__dart-apcie0.md) = `0x80`<br>[`/arm-io/dart-apcie1`](../devicetree/root__arm-io__dart-apcie1.md) = `0x80` |
| `prox-calibration` | 1 | string | [`/arm-io/aop/iop-aop-nub/prox`](../devicetree/root__arm-io__aop__iop-aop-nub__prox.md) = `syscfg/PxCl` |
| `proxy-is-development-only` | 1 | empty | [`/arm-io/admac-sllb-ec-proxy`](../devicetree/root__arm-io__admac-sllb-ec-proxy.md) = `` |
| `ps-groups` | 1 | 36 B | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `00000000000000000000000001000000…` |
| `pscl-cal` | 1 | string | [`/arm-io/haptics-support-interface`](../devicetree/root__arm-io__haptics-support-interface.md) = `syscfg/PSCl` |
| `pscl-cal-mi` | 1 | string | [`/arm-io/haptics-support-interface`](../devicetree/root__arm-io__haptics-support-interface.md) = `syscfg-mismatch/PSCl` |
| `psd` | 1 | u32 | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0x1` |
| `psd-mailbox-offset` | 1 | u32 | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0x10000` |
| `psd-panic-data` | 1 | 528 B | [`/arm-io/error-handler/psd-error-handler`](../devicetree/root__arm-io__error-handler__psd-error-handler.md) = `0000000000000000010000005053442e…` |
| `psd-timeout-ms` | 1 | u32 | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0x44c` |
| `ptd-dvfs-ceil-range` | 1 | u32 | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0x14` |
| `ptd-entities-offset` | 1 | u64 | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0x0` |
| `ptd-feature-enabled` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x1` |
| `ptd-hw-irq-vectors` | 1 | u32 | [`/arm-io/aon-ptd`](../devicetree/root__arm-io__aon-ptd.md) = `0x20` |
| `ptd-int-en-offset` | 1 | u64 | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0x18100` |
| `ptd-int-enable-clr-offset` | 1 | u64 | [`/arm-io/aon-ptd`](../devicetree/root__arm-io__aon-ptd.md) = `0x300` |
| `ptd-int-enable-offset` | 1 | u64 | [`/arm-io/aon-ptd`](../devicetree/root__arm-io__aon-ptd.md) = `0x100` |
| `ptd-int-enable-set-offset` | 1 | u64 | [`/arm-io/aon-ptd`](../devicetree/root__arm-io__aon-ptd.md) = `0x200` |
| `ptd-int-enclr-offset` | 1 | u64 | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0x18300` |
| `ptd-int-enset-offset` | 1 | u64 | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0x18200` |
| `ptd-int-status-offset` | 2 | u64×2 | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0x18000`<br>[`/arm-io/aon-ptd`](../devicetree/root__arm-io__aon-ptd.md) = `0x0` |
| `ptd-range` | 1 | 928 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `01000000000000000100000000000000…` |
| `ptd-range-ctrl2drv` | 1 | u32 | [`/arm-io/mcc`](../devicetree/root__arm-io__mcc.md) = `0x1e` |
| `ptd-range-drv2ctrl` | 1 | u32 | [`/arm-io/mcc`](../devicetree/root__arm-io__mcc.md) = `0xe` |
| `ptd-ranges` | 3 | 24 B, u64, string | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0a0000000b0000000c0000000d000000…`<br>[`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x410000001f`<br>[`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = ` , @` |
| `ptd-update-reg-index` | 1 | u32 | [`/arm-io/pmp`](../devicetree/root__arm-io__pmp.md) = `0x4` |
| `ptd-update-space-offset` | 1 | u64 | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0x10000` |
| `ptd-vecsel-ctrl-diff` | 1 | u64 | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0x200` |
| `ptd-vecsel-ctrl-offset` | 1 | u64 | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0x18400` |
| `ptmu-region-0-data` | 1 | u64 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x400000c000` |
| `ptmu-region-1-data` | 1 | u64 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x400000c040` |
| `ptmu-region-10-data` | 1 | u64 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x800000c300` |
| `ptmu-region-11-data` | 1 | u64 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x800000c380` |
| `ptmu-region-12-data` | 1 | u64 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x2000000c400` |
| `ptmu-region-13-data` | 1 | u64 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x2000000c600` |
| `ptmu-region-14-data` | 1 | u64 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x4000000c800` |
| `ptmu-region-15-data` | 1 | u64 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x4000000cc00` |
| `ptmu-region-2-data` | 1 | u64 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x400000c080` |
| `ptmu-region-3-data` | 1 | u64 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x400000c0c0` |
| `ptmu-region-4-data` | 1 | u64 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x400000c100` |
| `ptmu-region-5-data` | 1 | u64 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x400000c140` |
| `ptmu-region-6-data` | 1 | u64 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x400000c180` |
| `ptmu-region-7-data` | 1 | u64 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x400000c1c0` |
| `ptmu-region-8-data` | 1 | u64 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x800000c200` |
| `ptmu-region-9-data` | 1 | u64 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x800000c280` |
| `ptmu-secure-region-0-data` | 1 | u64 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x4000000b000` |
| `ptmu-secure-region-1-data` | 1 | u64 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x4000000b400` |
| `ptmu-secure-region-2-data` | 1 | u64 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x4000000b800` |
| `ptmu-secure-region-3-data` | 1 | u64 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x2000000bc00` |
| `ptmu-secure-region-4-data` | 1 | u64 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x2000000be00` |
| `ptp-large-files` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `public-key-accelerator` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `publish-user-client` | 1 | empty | [`/arm-io/iop-audio-controller/siri-listening-device`](../devicetree/root__arm-io__iop-audio-controller__siri-listening-device.md) = `` |
| `pubstampcfg0-offset` | 1 | u32 | [`/arm-io/aic`](../devicetree/root__arm-io__aic.md) = `0x1000` |
| `pubstampcfg0inttype-mask` | 1 | u32 | [`/arm-io/aic`](../devicetree/root__arm-io__aic.md) = `0x3` |
| `pubstampdcfg0en-mask` | 1 | u32 | [`/arm-io/aic`](../devicetree/root__arm-io__aic.md) = `0x80000000` |
| `pubstampdhi-offset` | 1 | u32 | [`/arm-io/aic`](../devicetree/root__arm-io__aic.md) = `0x100c` |
| `pubstamplo0-offset` | 1 | u32 | [`/arm-io/aic`](../devicetree/root__arm-io__aic.md) = `0x1008` |
| `pubstampstride-mask` | 1 | u32 | [`/arm-io/aic`](../devicetree/root__arm-io__aic.md) = `0x10` |
| `queue-depth` | 5 | u64×5 | [`/arm-io/nub-spmi0`](../devicetree/root__arm-io__nub-spmi0.md) = `0x10000000100`<br>[`/arm-io/nub-spmi1`](../devicetree/root__arm-io__nub-spmi1.md) = `0x10000000100`<br>[`/arm-io/nub-spmi2`](../devicetree/root__arm-io__nub-spmi2.md) = `0x10000000100`<br>[`/arm-io/aop-spmi0`](../devicetree/root__arm-io__aop-spmi0.md) = `0x10000000100`<br>[`/arm-io/aop-spmi1`](../devicetree/root__arm-io__aop-spmi1.md) = `0x10000000100` |
| `quiesced` | 5 | empty×5 | [`/arm-io/ans/iop-ans-nub`](../devicetree/root__arm-io__ans__iop-ans-nub.md) = ``<br>[`/arm-io/smc/iop-smc-nub`](../devicetree/root__arm-io__smc__iop-smc-nub.md) = ``<br>[`/arm-io/dcp/iop-dcp-nub`](../devicetree/root__arm-io__dcp__iop-dcp-nub.md) = ``<br>[`/arm-io/dcpsec/iop-dcpsec-nub`](../devicetree/root__arm-io__dcpsec__iop-dcpsec-nub.md) = ``<br>[`/arm-io/dcpext0/iop-dcpext0-nub`](../devicetree/root__arm-io__dcpext0__iop-dcpext0-nub.md) = `` |
| `ramp-down-max-tap-point` | 1 | 12 B | [`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `cdcccc3ecdcccc3ecdcccc3e` |
| `ramp-down-min-tap-point` | 1 | 12 B | [`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `cdcc4c3ecdcc4c3ecdcc4c3e` |
| `ramp-up-max-tap-point` | 1 | 12 B | [`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `3333b33e3333b33e3333b33e` |
| `ramp-up-min-tap-point` | 1 | 12 B | [`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `ec51383eec51383eec51383e` |
| `random-seed` | 1 | 256 B | [`/chosen`](../devicetree/root__chosen.md) = `00000000000000000000000000000000…` |
| `ranges` | 2 | 240 B, 56 B | [`/arm-io`](../devicetree/root__arm-io.md) = `00000000000000000000000002000000…`<br>[`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) = `00000043000000c00b000000000000c0…` |
| `rdc-cap-enabled` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x1` |
| `real-time` | 6 | empty×6 | [`/arm-io/dart-disp0`](../devicetree/root__arm-io__dart-disp0.md) = ``<br>[`/arm-io/dart-dispgrt`](../devicetree/root__arm-io__dart-dispgrt.md) = ``<br>[`/arm-io/dart-dispsec`](../devicetree/root__arm-io__dart-dispsec.md) = ``<br>[`/arm-io/dart-dispsecgrt`](../devicetree/root__arm-io__dart-dispsecgrt.md) = ``<br>[`/arm-io/dart-dispext0`](../devicetree/root__arm-io__dart-dispext0.md) = `` |
| `rear-auto-hdr` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x1` |
| `rear-burst` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x1` |
| `rear-burst-image-duration` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x64` |
| `rear-cam-offset-from-center` | 3 | 20 B×3 | [`/product`](../devicetree/root__product.md) = `b7a10000365400005b0b0000e8030000…`<br>[`/product/display0`](../devicetree/root__product__display0.md) = `51aa0000c41f0000821e0000e8030000…`<br>[`/product/display1`](../devicetree/root__product__display1.md) = `58c0000051aa0000da070000e8030000…` |
| `rear-cam-sup-wide-af-capability` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x1` |
| `rear-cam-superwide-capability` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x1` |
| `rear-hdr` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x1` |
| `rear-hdr-on` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x1` |
| `rear-low-light-photo` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x1` |
| `rear-max-burst-length` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x258` |
| `rear-max-slomo-video-fps-1080p` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0xf0` |
| `rear-max-slomo-video-fps-720p` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0xf0` |
| `rear-max-video-fps-1080p` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x78` |
| `rear-max-video-fps-4k` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x78` |
| `rear-max-video-fps-720p` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x3c` |
| `rear-max-video-frame_rate` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x3c` |
| `rear-max-video-zoom` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x3` |
| `rear-slowmo` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x1` |
| `rear-stage-light-portrait` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x1` |
| `rear-variable-frame-rate` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x1` |
| `reboot-firmware` | 1 | empty | [`/arm-io/ispRtb/iop-isp-nub`](../devicetree/root__arm-io__ispRtb__iop-isp-nub.md) = `` |
| `Receiver` | 1 | u64 | [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) = `0x1000000` |
| `reconfig-firmware` | 2 | empty×2 | [`/arm-io/ane0/iop-ane0-nub`](../devicetree/root__arm-io__ane0__iop-ane0-nub.md) = ``<br>[`/arm-io/ane1/iop-ane1-nub`](../devicetree/root__arm-io__ane1__iop-ane1-nub.md) = `` |
| `reg` | 273 | u32×82, 16 B×56, 64 B×27 | [`/cpus/cpu0`](../devicetree/root__cpus__cpu0.md) = `0x0`<br>[`/cpus/cpu1`](../devicetree/root__cpus__cpu1.md) = `0x1`<br>[`/cpus/cpu2`](../devicetree/root__cpus__cpu2.md) = `0x2`<br>[`/cpus/cpu3`](../devicetree/root__cpus__cpu3.md) = `0x3`<br>[`/cpus/cpu4`](../devicetree/root__cpus__cpu4.md) = `0x100` |
| `reg-block` | 1 | 16 B | [`/arm-io/sep/iop-sep-nub/InvalidateHmac`](../devicetree/root__arm-io__sep__iop-sep-nub__InvalidateHmac.md) = `00c02d88020000000080010000000000` |
| `reg-groups` | 1 | 48 B | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `01000000000008000700000000400300…` |
| `reg-maps` | 2 | 216 B, 16 B | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `00000000010001000200000103000201…`<br>[`/arm-io/soc-reporter`](../devicetree/root__arm-io__soc-reporter.md) = `00000000010001000200020003000300` |
| `reg-private` | 6 | u64×6 | [`/cpus/cpu0`](../devicetree/root__cpus__cpu0.md) = `0x210010000`<br>[`/cpus/cpu1`](../devicetree/root__cpus__cpu1.md) = `0x210110000`<br>[`/cpus/cpu2`](../devicetree/root__cpus__cpu2.md) = `0x210210000`<br>[`/cpus/cpu3`](../devicetree/root__cpus__cpu3.md) = `0x210310000`<br>[`/cpus/cpu4`](../devicetree/root__cpus__cpu4.md) = `0x211010000` |
| `reg-val-update` | 1 | 16 B | [`/arm-io/msg`](../devicetree/root__arm-io__msg.md) = `0c030000000000008c00000001000000` |
| `region-base` | 4 | u64×4 | [`/arm-io/aop/iop-aop-nub`](../devicetree/root__arm-io__aop__iop-aop-nub.md) = `0x290c00000`<br>[`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0x280500000`<br>[`/arm-io/ans/iop-ans-nub`](../devicetree/root__arm-io__ans__iop-ans-nub.md) = `0x0`<br>[`/arm-io/smc/iop-smc-nub`](../devicetree/root__arm-io__smc__iop-smc-nub.md) = `0x28de00000` |
| `region-info` | 1 | string | [`/`](../devicetree/root.md) = `syscfg/Regn/0x20,zeroes/0x20` |
| `region-size` | 4 | u64×3, string | [`/arm-io/aop/iop-aop-nub`](../devicetree/root__arm-io__aop__iop-aop-nub.md) = `:`<br>[`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0xb0000`<br>[`/arm-io/ans/iop-ans-nub`](../devicetree/root__arm-io__ans__iop-ans-nub.md) = `0x0`<br>[`/arm-io/smc/iop-smc-nub`](../devicetree/root__arm-io__smc__iop-smc-nub.md) = `0x140000` |
| `region-sku` | 1 | string | [`/baseband`](../devicetree/root__baseband.md) = `syscfg/RSKU/0x40,zeroes/0x40` |
| `registerWithPrimary` | 2 | empty×2 | [`/arm-io/iop-audio-controller/audio-receiver/audio-receiver`](../devicetree/root__arm-io__iop-audio-controller__audio-receiver__audio-receiver.md) = ``<br>[`/arm-io/iop-audio-controller/audio-flicker/audio-flicker`](../devicetree/root__arm-io__iop-audio-controller__audio-flicker__audio-flicker.md) = `` |
| `regulatory-model-number` | 1 | string | [`/`](../devicetree/root.md) = `syscfg/RMd#/0x20` |
| `release-arbiter-shared-mem` | 1 | empty | [`/arm-io/audio-sllb-proxy`](../devicetree/root__arm-io__audio-sllb-proxy.md) = `` |
| `remap` | 12 | u32×4, 12 B×3, 28 B×3 | [`/arm-io/dart-sbr`](../devicetree/root__arm-io__dart-sbr.md) = `1a0400001b0400001c0400001d040000…`<br>[`/arm-io/dart-usb0`](../devicetree/root__arm-io__dart-usb0.md) = `0x100`<br>[`/arm-io/dart-dcp`](../devicetree/root__arm-io__dart-dcp.md) = `050300000603000008030000`<br>[`/arm-io/dart-disp0`](../devicetree/root__arm-io__dart-disp0.md) = `0c0b0000120b0000010b0000020b0000…`<br>[`/arm-io/dart-dispgrt`](../devicetree/root__arm-io__dart-dispgrt.md) = `0x102` |
| `remap-usages` | 1 | u64 | [`/buttons`](../devicetree/root__buttons.md) = `0xb002d000b002e` |
| `remote-node-interface` | 1 | u32 | [`/arm-io/iop-audio-controller/audio-haptic-leap`](../devicetree/root__arm-io__iop-audio-controller__audio-haptic-leap.md) = `0x17d` |
| `remote-only` | 3 | empty×3 | [`/arm-io/dcp/iop-dcp-nub`](../devicetree/root__arm-io__dcp__iop-dcp-nub.md) = ``<br>[`/arm-io/dcpsec/iop-dcpsec-nub`](../devicetree/root__arm-io__dcpsec__iop-dcpsec-nub.md) = ``<br>[`/arm-io/dcpext0/iop-dcpext0-nub`](../devicetree/root__arm-io__dcpext0__iop-dcpext0-nub.md) = `` |
| `remote-power-state` | 2 | u32×2 | [`/arm-io/dcp0-expert`](../devicetree/root__arm-io__dcp0-expert.md) = `0x1`<br>[`/arm-io/dcpsec-expert`](../devicetree/root__arm-io__dcpsec-expert.md) = `0x1` |
| `repair-environment` | 1 | u32 | [`/chosen`](../devicetree/root__chosen.md) = `0x0` |
| `repair-history` | 1 | string | [`/chosen`](../devicetree/root__chosen.md) = `syscfg/RCHL` |
| `repair-status` | 1 | string | [`/chosen`](../devicetree/root__chosen.md) = `syscfg/rpcp` |
| `replacement` | 4 | string×4 | [`/osenvironments/recovery-environment/ephemeral-recovery-data-volume`](../devicetree/root__osenvironments__recovery-environment__ephemeral-recovery-data-volume.md) = `fstab-ephemeral-recovery-data`<br>[`/osenvironments/diagnostics-environment/ephemeral-diag-data-volume`](../devicetree/root__osenvironments__diagnostics-environment__ephemeral-diag-data-volume.md) = `fstab-ephemeral-diag-data`<br>[`/osenvironments/darwinos-ramdisk-environment/ephemeral-recovery-data-volume`](../devicetree/root__osenvironments__darwinos-ramdisk-environment__ephemeral-recovery-data-volume.md) = `fstab-ephemeral-recovery-data`<br>[`/osenvironments/device-recovery-environment/ephemeral-devrecov-data-volume`](../devicetree/root__osenvironments__device-recovery-environment__ephemeral-devrecov-data-volume.md) = `fstab-ephemeral-devrecov-data` |
| `report-port-event` | 1 | u32 | [`/arm-io/smc/iop-smc-nub/smc-charger-util`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-charger-util.md) = `0x1` |
| `reporter-enable-mask` | 1 | u32 | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0xa` |
| `reporter-mask` | 1 | u32 | [`/arm-io/soc-reporter`](../devicetree/root__arm-io__soc-reporter.md) = `0x5` |
| `required-functions` | 2 | string×2 | [`/arm-io/aop-spmi0/stockholm-spmi`](../devicetree/root__arm-io__aop-spmi0__stockholm-spmi.md) = `support_host_wake_spmi, support_data_over_spmi`<br>[`/arm-io/aop-spmi0/hammerfest-spmi`](../devicetree/root__arm-io__aop-spmi0__hammerfest-spmi.md) = `support_host_wake_spmi, support_data_over_spmi` |
| `required-gpios` | 2 | string×2 | [`/arm-io/aop-spmi0/stockholm-spmi/stockholm`](../devicetree/root__arm-io__aop-spmi0__stockholm-spmi__stockholm.md) = `support_venable, support_virtual_gpio, support_boot_measurem`<br>[`/arm-io/aop-spmi0/hammerfest-spmi/hammerfest`](../devicetree/root__arm-io__aop-spmi0__hammerfest-spmi__hammerfest.md) = `support_venable, support_virtual_gpio, support_boot_measurem` |
| `resource-gid-mapping` | 1 | 43 B | [`/arm-io/audio-resource-manager`](../devicetree/root__arm-io__audio-resource-manager.md) = `00000100204d4350414f50417564696f…` |
| `retention` | 12 | empty×12 | [`/arm-io/dart-sep`](../devicetree/root__arm-io__dart-sep.md) = ``<br>[`/arm-io/dart-sbr`](../devicetree/root__arm-io__dart-sbr.md) = ``<br>[`/arm-io/dart-dcp`](../devicetree/root__arm-io__dart-dcp.md) = ``<br>[`/arm-io/dart-disp0`](../devicetree/root__arm-io__dart-disp0.md) = ``<br>[`/arm-io/dart-dispgrt`](../devicetree/root__arm-io__dart-dispgrt.md) = `` |
| `rev-offset` | 1 | u32 | [`/arm-io/aic`](../devicetree/root__arm-io__aic.md) = `0x0` |
| `rf-antenna-name` | 2 | string×2 | [`/arm-io/aop-spmi0/stockholm-spmi/stockholm`](../devicetree/root__arm-io__aop-spmi0__stockholm-spmi__stockholm.md) = `RTM8_8`<br>[`/arm-io/aop-spmi0/hammerfest-spmi/hammerfest`](../devicetree/root__arm-io__aop-spmi0__hammerfest-spmi__hammerfest.md) = `RTM8_8S` |
| `RF-exposure-separation-distance` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x5` |
| `rid` | 1 | u32 | [`/arm-io/nub-spmi2/spmi-hpm0`](../devicetree/root__arm-io__nub-spmi2__spmi-hpm0.md) = `0x0` |
| `ring-light-supported` | 2 | u32×2 | [`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x1`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x1` |
| `role` | 56 | string×34, u32×22 | [`/arm-io/gpio0`](../devicetree/root__arm-io__gpio0.md) = `AP`<br>[`/arm-io/aop`](../devicetree/root__arm-io__aop.md) = `AOP`<br>[`/arm-io/aop-exclave-mailbox`](../devicetree/root__arm-io__aop-exclave-mailbox.md) = `AOP-EXCLAVE`<br>[`/arm-io/aop-exclave-ioreporting`](../devicetree/root__arm-io__aop-exclave-ioreporting.md) = `AOP-EXCLAVE`<br>[`/arm-io/aop2`](../devicetree/root__arm-io__aop2.md) = `AOP2` |
| `rom-panic-bytes` | 1 | u32 | [`/arm-io/sep/iop-sep-nub`](../devicetree/root__arm-io__sep__iop-sep-nub.md) = `0x1d8` |
| `root-matching` | 1 | 256 B | [`/chosen`](../devicetree/root__chosen.md) = `00000000000000000000000000000000…` |
| `rosaline-calibration-current` | 2 | string×2 | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) = `syscfg/RxCL`<br>[`/arm-io/isp`](../devicetree/root__arm-io__isp.md) = `syscfg/RxCL` |
| `routes` | 4 | u32×4 | [`/arm-io/aop/iop-aop-nub`](../devicetree/root__arm-io__aop__iop-aop-nub.md) = `0x6c`<br>[`/arm-io/aop2/iop-aop2-nub`](../devicetree/root__arm-io__aop2__iop-aop2-nub.md) = `0x70`<br>[`/arm-io/dcp/iop-dcp-nub`](../devicetree/root__arm-io__dcp__iop-dcp-nub.md) = `0xfb`<br>[`/arm-io/dcpsec/iop-dcpsec-nub`](../devicetree/root__arm-io__dcpsec__iop-dcpsec-nub.md) = `0x10f` |
| `rsm-channel-max-ver` | 1 | u32 | [`/arm-io/rsm`](../devicetree/root__arm-io__rsm.md) = `0x2` |
| `rsm-channel-min-ver` | 1 | u32 | [`/arm-io/rsm`](../devicetree/root__arm-io__rsm.md) = `0x1` |
| `rtplc-apce-table` | 3 | 16 B×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `000000009a99193f6666663f0000803f`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `000000009a99193f6666663f0000803f`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `000000009a99193f6666663f0000803f` |
| `rtplc-nits-table` | 3 | 16 B×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0000c8440000c8440000964400009644`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0000c8440000c8440000964400009644`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0000c8440000c8440000964400009644` |
| `rtplc-supported` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x1`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x1`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x1` |
| `sac-index-count` | 2 | u32×2 | [`/arm-io/dcp-sac-controller`](../devicetree/root__arm-io__dcp-sac-controller.md) = `0x2`<br>[`/arm-io/dcpsec-sac-controller`](../devicetree/root__arm-io__dcpsec-sac-controller.md) = `0x2` |
| `samplerate-default` | 1 | u64 | [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) = `0xbb8000000000` |
| `samplerate-subset` | 1 | 16 B | [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) = `0000000080bb00000000000000000000` |
| `sampling-interval-ms` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x4` |
| `sandman-support` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `sar-mpe-ant-cluster-config` | 1 | u32 | [`/arm-io/aop-spmi1/baseband-idc`](../devicetree/root__arm-io__aop-spmi1__baseband-idc.md) = `0x28` |
| `sart-power-managed` | 1 | empty | [`/arm-io/sart-ans`](../devicetree/root__arm-io__sart-ans.md) = `` |
| `sart-power-reg-offset` | 1 | u32 | [`/arm-io/sart-ans`](../devicetree/root__arm-io__sart-ans.md) = `0x13e8` |
| `sart-version` | 1 | u32 | [`/arm-io/sart-ans`](../devicetree/root__arm-io__sart-ans.md) = `0x4` |
| `sbd` | 1 | 396 B | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `00000000ffffffff0000000000000000…` |
| `scan-timer-reset-time` | 1 | u32 | [`/arm-io/spi1/mesa`](../devicetree/root__arm-io__spi1__mesa.md) = `0x9999` |
| `scodec_ced_die0` | 2 | u32×2 | [`/ced-ssw/ced_tunable_mask`](../devicetree/root__ced-ssw__ced_tunable_mask.md) = `0x6`<br>[`/ced-ssw/ced_disable_mask`](../devicetree/root__ced-ssw__ced_disable_mask.md) = `0x3` |
| `scodec_ced_die1` | 2 | u32×2 | [`/ced-ssw/ced_tunable_mask`](../devicetree/root__ced-ssw__ced_tunable_mask.md) = `0x22`<br>[`/ced-ssw/ced_disable_mask`](../devicetree/root__ced-ssw__ced_disable_mask.md) = `0x11` |
| `sdd-vers` | 1 | u32 | [`/baseband`](../devicetree/root__baseband.md) = `0x30203` |
| `secure-boot` | 1 | u32 | [`/chosen`](../devicetree/root__chosen.md) = `0x0` |
| `secure-root-prefix` | 1 | string | [`/`](../devicetree/root.md) = `md` |
| `secureboot-certificate-format` | 1 | string | [`/chosen`](../devicetree/root__chosen.md) = `im4c` |
| `secureboot-key-scheme` | 1 | string | [`/chosen`](../devicetree/root__chosen.md) = `rsa4096` |
| `security-reg-index` | 3 | u32×3 | [`/arm-io/dcp0-expert`](../devicetree/root__arm-io__dcp0-expert.md) = `0x0`<br>[`/arm-io/dcpsec-expert`](../devicetree/root__arm-io__dcpsec-expert.md) = `0x0`<br>[`/arm-io/dcpext0-expert`](../devicetree/root__arm-io__dcpext0-expert.md) = `0x0` |
| `self-actuated` | 2 | empty×2 | [`/arm-io/admac-dispint0`](../devicetree/root__arm-io__admac-dispint0.md) = ``<br>[`/arm-io/admac-dispext0`](../devicetree/root__arm-io__admac-dispext0.md) = `` |
| `self-power-gate` | 1 | empty | [`/arm-io/sep`](../devicetree/root__arm-io__sep.md) = `` |
| `sensor` | 1 | 12 B | [`/arm-io/smctempsensor0`](../devicetree/root__arm-io__smctempsensor0.md) = `6d54504c6d544c4c6d455457` |
| `sensor-id` | 1 | u32 | [`/arm-io/spi1/mesa`](../devicetree/root__arm-io__spi1__mesa.md) = `0x3358` |
| `sensor-type` | 2 | u32×2 | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) = `0x83`<br>[`/arm-io/isp`](../devicetree/root__arm-io__isp.md) = `0x83` |
| `separate-thermal-budget-adds` | 1 | 16 B | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0100000007000000090000000a000000` |
| `sepfw-load-at-boot` | 1 | u32 | [`/chosen`](../devicetree/root__chosen.md) = `0x1` |
| `SEPHiddenKeySupport` | 1 | empty | [`/arm-io/sep`](../devicetree/root__arm-io__sep.md) = `` |
| `sequence-power_off` | 1 | 46 B | [`/arm-io/aop/iop-aop-nub/rose`](../devicetree/root__arm-io__aop__iop-aop-nub__rose.md) = `66756e6374696f6e2d726f73655f7265…` |
| `sequence-power_on` | 1 | 22 B | [`/arm-io/aop/iop-aop-nub/rose`](../devicetree/root__arm-io__aop__iop-aop-nub__rose.md) = `66756e6374696f6e2d726f73655f7077…` |
| `sequence-reset` | 1 | 48 B | [`/arm-io/aop/iop-aop-nub/rose`](../devicetree/root__arm-io__aop__iop-aop-nub__rose.md) = `66756e6374696f6e2d726f73655f7265…` |
| `sequence-trigger_coredump` | 1 | 54 B | [`/arm-io/aop/iop-aop-nub/rose`](../devicetree/root__arm-io__aop__iop-aop-nub__rose.md) = `66756e6374696f6e2d726f73655f636f…` |
| `serial-device` | 1 | u32 | [`/defaults`](../devicetree/root__defaults.md) = `0xa8` |
| `serial-number` | 1 | string | [`/`](../devicetree/root.md) = `syscfg/SrNm/0x20,zeroes/0x20` |
| `service` | 1 | 108 B | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `01000000010000000800ffffffffffff…` |
| `service-display` | 2 | u32×2 | [`/arm-io/mtp/iop-mtp-nub/multi-touch2`](../devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch2.md) = `0x102`<br>[`/arm-io/mtp/iop-mtp-nub/multi-touch`](../devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch.md) = `0xe9` |
| `service-exclave_proxy` | 4 | string×4 | [`/arm-io/admac-base-s/base-s-adma-tx-2`](../devicetree/root__arm-io__admac-base-s__base-s-adma-tx-2.md) = `DMAChannelProxy@admac-speaker-tx-ec-proxy`<br>[`/arm-io/admac-base-s/base-s-adma-tx-3`](../devicetree/root__arm-io__admac-base-s__base-s-adma-tx-3.md) = `DMAChannelProxy@admac-receiver-tx-ec-proxy`<br>[`/arm-io/admac-base-s/base-s-adma-rx-4`](../devicetree/root__arm-io__admac-base-s__base-s-adma-rx-4.md) = `DMAChannelProxy@admac-hp-mic-ec-proxy`<br>[`/arm-io/admac-leap-s/leap-s-adma-rx-2`](../devicetree/root__arm-io__admac-leap-s__leap-s-adma-rx-2.md) = `DMAChannelProxy@admac-sllb-ec-proxy` |
| `service-gates` | 26 | u32×19, u64×3, string×2 | [`/arm-io/spi1`](../devicetree/root__arm-io__spi1.md) = `0x12`<br>[`/arm-io/aes`](../devicetree/root__arm-io__aes.md) = `0x19`<br>[`/arm-io/pmp`](../devicetree/root__arm-io__pmp.md) = `0x9800000097`<br>[`/arm-io/sio`](../devicetree/root__arm-io__sio.md) = `0x18`<br>[`/arm-io/uart0`](../devicetree/root__arm-io__uart0.md) = `0x5` |
| `service-reset` | 15 | u32×15 | [`/arm-io/sio`](../devicetree/root__arm-io__sio.md) = `0x14`<br>[`/arm-io/i2c2`](../devicetree/root__arm-io__i2c2.md) = `0x22`<br>[`/arm-io/i2c3`](../devicetree/root__arm-io__i2c3.md) = `0x23`<br>[`/arm-io/i2c4`](../devicetree/root__arm-io__i2c4.md) = `0x24`<br>[`/arm-io/dcp`](../devicetree/root__arm-io__dcp.md) = `0xd` |
| `sgpio-bus-id` | 1 | u32 | [`/arm-io/nub-spmi0/pmu-main/sgpio-bridge-pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main__sgpio-bridge-pmu-main.md) = `0x0` |
| `shutdown-sleep` | 6 | empty×6 | [`/arm-io/ans/iop-ans-nub`](../devicetree/root__arm-io__ans__iop-ans-nub.md) = ``<br>[`/arm-io/dcp/iop-dcp-nub`](../devicetree/root__arm-io__dcp__iop-dcp-nub.md) = ``<br>[`/arm-io/dcpsec/iop-dcpsec-nub`](../devicetree/root__arm-io__dcpsec__iop-dcpsec-nub.md) = ``<br>[`/arm-io/dcpext0/iop-dcpext0-nub`](../devicetree/root__arm-io__dcpext0__iop-dcpext0-nub.md) = ``<br>[`/arm-io/gfx-asc/iop-gfx-nub`](../devicetree/root__arm-io__gfx-asc__iop-gfx-nub.md) = `` |
| `sid` | 23 | u32×9, u64×7, 12 B×2 | [`/arm-io/dart-sep`](../devicetree/root__arm-io__dart-sep.md) = `0x100000000`<br>[`/arm-io/dart-sio`](../devicetree/root__arm-io__dart-sio.md) = `0x100000000`<br>[`/arm-io/dart-sbr`](../devicetree/root__arm-io__dart-sbr.md) = `00000000020000000400000006000000…`<br>[`/arm-io/dart-usb0`](../devicetree/root__arm-io__dart-usb0.md) = `0xe00000001`<br>[`/arm-io/dart-dcp`](../devicetree/root__arm-io__dart-dcp.md) = `0x3` |
| `sid-count` | 23 | u32×23 | [`/arm-io/dart-sep`](../devicetree/root__arm-io__dart-sep.md) = `0x3`<br>[`/arm-io/dart-sio`](../devicetree/root__arm-io__dart-sio.md) = `0x2`<br>[`/arm-io/dart-sbr`](../devicetree/root__arm-io__dart-sbr.md) = `0x39`<br>[`/arm-io/dart-usb0`](../devicetree/root__arm-io__dart-usb0.md) = `0x10`<br>[`/arm-io/dart-dcp`](../devicetree/root__arm-io__dart-dcp.md) = `0xf` |
| `sid-lft` | 1 | string | [`/arm-io/dart-sbr`](../devicetree/root__arm-io__dart-sbr.md) = `&, ', 2, 3` |
| `sid-mcw` | 3 | u32×2, string | [`/arm-io/dart-sbr`](../devicetree/root__arm-io__dart-sbr.md) = `#, $`<br>[`/arm-io/dart-dcp`](../devicetree/root__arm-io__dart-dcp.md) = `0xa`<br>[`/arm-io/dart-dcpsec`](../devicetree/root__arm-io__dart-dcpsec.md) = `0xa` |
| `sid-ocla` | 1 | string | [`/arm-io/dart-sbr`](../devicetree/root__arm-io__dart-sbr.md) = `%, 4` |
| `sid-trace` | 4 | u32×3, 20 B | [`/arm-io/dart-sbr`](../devicetree/root__arm-io__dart-sbr.md) = `0a0000000a0000000b0000000c000000…`<br>[`/arm-io/dart-dcp`](../devicetree/root__arm-io__dart-dcp.md) = `0x9`<br>[`/arm-io/dart-dcpsec`](../devicetree/root__arm-io__dart-dcpsec.md) = `0x9`<br>[`/arm-io/dart-dcpext0`](../devicetree/root__arm-io__dart-dcpext0.md) = `0x9` |
| `side-button-location` | 3 | 24 B×3 | [`/product`](../devicetree/root__product.md) = `74c60b00d22111001eb5040056d90200…`<br>[`/product/display0`](../devicetree/root__product__display0.md) = `74c60b00d22111001eb5040056d90200…`<br>[`/product/display1`](../devicetree/root__product__display1.md) = `8409180034e810004197040056d90200…` |
| `sidp-rom-manifest-hash` | 1 | 48 B | [`/chosen`](../devicetree/root__chosen.md) = `00000000000000000000000000000000…` |
| `sika-support` | 1 | u32 | [`/arm-io/sep`](../devicetree/root__arm-io__sep.md) = `0x1` |
| `sil-enabled` | 1 | u32 | [`/core-brightness`](../devicetree/root__core-brightness.md) = `0x1` |
| `simple-reconfig-wdog-icc-time` | 1 | u32 | [`/arm-io/wdt`](../devicetree/root__arm-io__wdt.md) = `0x5` |
| `simple-reconfig-wdog-support` | 1 | empty | [`/arm-io/wdt`](../devicetree/root__arm-io__wdt.md) = `` |
| `single-stage-boot` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `sio-hmac1-disable-mask` | 1 | u64 | [`/arm-io/sep/iop-sep-nub/InvalidateHmac`](../devicetree/root__arm-io__sep__iop-sep-nub__InvalidateHmac.md) = `0x1` |
| `sio-hmac1-offset` | 1 | string | [`/arm-io/sep/iop-sep-nub/InvalidateHmac`](../devicetree/root__arm-io__sep__iop-sep-nub__InvalidateHmac.md) = `T` |
| `sioaesdisable-offset` | 1 | u32 | [`/arm-io/aes`](../devicetree/root__arm-io__aes.md) = `0x0` |
| `sioaesdisablegid0-offset` | 1 | u32 | [`/arm-io/aes`](../devicetree/root__arm-io__aes.md) = `0x8` |
| `sioaesdisablegid1-offset` | 1 | u32 | [`/arm-io/aes`](../devicetree/root__arm-io__aes.md) = `0xc` |
| `sioaesdisableuid1-offset` | 1 | u32 | [`/arm-io/aes`](../devicetree/root__arm-io__aes.md) = `0x4` |
| `siri-gesture` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `size` | 2 | 16 B×2 | [`/arm-io/i2c3/display-eeprom/display-eeprom-generic-data`](../devicetree/root__arm-io__i2c3__display-eeprom__display-eeprom-generic-data.md) = `320000003200000002000000c0000000`<br>[`/arm-io/i2c3/display-eeprom-2/display-eeprom-generic-data-2`](../devicetree/root__arm-io__i2c3__display-eeprom-2__display-eeprom-generic-data-2.md) = `320000003200000002000000c0000000` |
| `skip-mcc-off-to-s2r` | 1 | u32 | [`/arm-io/mcc`](../devicetree/root__arm-io__mcc.md) = `0x1` |
| `skip-spmi-reconfig` | 2 | empty×2 | [`/arm-io/aop-spmi0/stockholm-spmi`](../devicetree/root__arm-io__aop-spmi0__stockholm-spmi.md) = ``<br>[`/arm-io/aop-spmi0/hammerfest-spmi`](../devicetree/root__arm-io__aop-spmi0__hammerfest-spmi.md) = `` |
| `sleep-on-hibernate` | 3 | empty×3 | [`/arm-io/aop/iop-aop-nub`](../devicetree/root__arm-io__aop__iop-aop-nub.md) = ``<br>[`/arm-io/aop2/iop-aop2-nub`](../devicetree/root__arm-io__aop2__iop-aop2-nub.md) = ``<br>[`/arm-io/mtp/iop-mtp-nub`](../devicetree/root__arm-io__mtp__iop-mtp-nub.md) = `` |
| `slider-mapping` | 3 | 404 B×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0000803f713d8a3f8fc2953fae47a13f…`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0000803f713d8a3f8fc2953fae47a13f…`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0000803f713d8a3f8fc2953fae47a13f…` |
| `smc-aop-charge-config` | 1 | 16 B | [`/arm-io/aop/iop-aop-nub/smc-control`](../devicetree/root__arm-io__aop__iop-aop-nub__smc-control.md) = `0000641003000000040000002a000000` |
| `smc-interface-comm-enabled` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x1` |
| `smc-thermal-report-version` | 1 | u32 | [`/baseband`](../devicetree/root__baseband.md) = `0x3` |
| `smic-mic` | 1 | u64 | [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) = `0x308020802` |
| `sn450WithLoadSwitch` | 1 | u32 | [`/arm-io/aop-spmi0/stockholm-spmi/stockholm`](../devicetree/root__arm-io__aop-spmi0__stockholm-spmi__stockholm.md) = `0x1` |
| `soc-device` | 1 | 3720 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `01000000454e4f4e0100000000000000…` |
| `soc-device-ps-group` | 1 | u64 | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0x3ffffc00` |
| `soc-device-ps-map` | 1 | 260 B | [`/arm-io/pmgr/pmgrtools`](../devicetree/root__arm-io__pmgr__pmgrtools.md) = `67000000414758000000000000000000…` |
| `soc-devices` | 1 | 16 B | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `03000000040000000600000007000000` |
| `soc-dpe` | 1 | u32 | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0x1` |
| `soc-generation` | 1 | string | [`/arm-io`](../devicetree/root__arm-io.md) = `H19` |
| `soc-id` | 1 | string | [`/arm-io/ave`](../devicetree/root__arm-io__ave.md) = `t8160` |
| `soc-ni0-bw-enable` | 1 | u32 | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0x0` |
| `soc-ni0-bw-threshold` | 1 | 64 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `e17a1800000000000000000000000000…` |
| `soc-ni1-bw-enable` | 1 | u32 | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0x0` |
| `soc-ni1-bw-threshold` | 1 | 64 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `e17a1800000000000000000000000000…` |
| `soc-ni2-bw-enable` | 1 | u32 | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0x0` |
| `soc-ni2-bw-threshold` | 1 | 64 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `e17a1800000000000000000000000000…` |
| `soc-ni3-bw-enable` | 1 | u32 | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0x0` |
| `soc-ni3-bw-threshold` | 1 | 64 B | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `e17a1800000000000000000000000000…` |
| `sochot-sensors` | 2 | 88 B, 112 B | [`/arm-io/pmp/iop-pmp-nub/:borneo_h19a_1`](../devicetree/root__arm-io__pmp__iop-pmp-nub___borneo_h19a_1.md) = `01000000020000000300000004000000…`<br>[`/arm-io/pmp/iop-pmp-nub/:borneo_h19p_1`](../devicetree/root__arm-io__pmp__iop-pmp-nub___borneo_h19p_1.md) = `01000000020000000300000004000000…` |
| `socni-count` | 1 | u32 | [`/arm-io/mcc`](../devicetree/root__arm-io__mcc.md) = `0x4` |
| `socni-reg-idx` | 1 | u32 | [`/arm-io/mcc`](../devicetree/root__arm-io__mcc.md) = `0x2` |
| `soft-disconnect-interval` | 1 | u32 | [`/arm-io/usb-drd0`](../devicetree/root__arm-io__usb-drd0.md) = `0xf0` |
| `software-behavior` | 1 | string | [`/chosen`](../devicetree/root__chosen.md) = `syscfg/SwBh/0x10,zeroes/0x10` |
| `software-bundle-version` | 1 | string | [`/chosen`](../devicetree/root__chosen.md) = `syscfg/SBVr/0x10,zeroes/0x10` |
| `spatial-over-capture` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x1` |
| `speaker-cpms-bgd_100ms` | 1 | u64 | [`/product/audio`](../devicetree/root__product__audio.md) = `0xffffffffffffffff` |
| `speaker-cpms-bgd_1s` | 1 | u64 | [`/product/audio`](../devicetree/root__product__audio.md) = `0x232a00000717` |
| `speaker-cpms-bgd_inst` | 1 | u64 | [`/product/audio`](../devicetree/root__product__audio.md) = `0xffffffffffffffff` |
| `speaker-thiele-small-0` | 1 | string | [`/product/audio`](../devicetree/root__product__audio.md) = `syscfg/SpPH` |
| `speaker-thiele-small-key-cnt` | 1 | u32 | [`/product/audio`](../devicetree/root__product__audio.md) = `0x1` |
| `speaker-trim-gains-0` | 1 | string | [`/product/audio`](../devicetree/root__product__audio.md) = `syscfg/SpGH` |
| `speaker-trim-gains-key-cnt` | 1 | u32 | [`/product/audio`](../devicetree/root__product__audio.md) = `0x1` |
| `special-region-0-corner-curve` | 2 | string×2 | [`/product/display0`](../devicetree/root__product__display0.md) = `circular`<br>[`/product/display1`](../devicetree/root__product__display1.md) = `circular` |
| `special-region-0-frame` | 2 | 16 B×2 | [`/product/display0`](../devicetree/root__product__display0.md) = `00e095440000b0420000de420000de42`<br>[`/product/display1`](../devicetree/root__product__display1.md) = `00007c42008031440000de420000de42` |
| `special-region-0-type` | 2 | string×2 | [`/product/display0`](../devicetree/root__product__display0.md) = `Jindo`<br>[`/product/display1`](../devicetree/root__product__display1.md) = `BlankableRR` |
| `special-region-1-frame` | 1 | 16 B | [`/product/display1`](../devicetree/root__product__display1.md) = `0000000000e0a64400c0ea4400000000` |
| `special-region-1-type` | 1 | string | [`/product/display1`](../devicetree/root__product__display1.md) = `Fold` |
| `special-regions-count` | 2 | u32×2 | [`/product/display0`](../devicetree/root__product__display0.md) = `0x1`<br>[`/product/display1`](../devicetree/root__product__display1.md) = `0x2` |
| `spi-frequency` | 1 | u32 | [`/arm-io/spi1/mesa`](../devicetree/root__arm-io__spi1__mesa.md) = `0x7a1200` |
| `spi-version` | 1 | u32 | [`/arm-io/spi1`](../devicetree/root__arm-io__spi1.md) = `0x1` |
| `spkamp-config_arc` | 1 | 16 B | [`/arm-io/aop/iop-aop-nub/SPUApp`](../devicetree/root__arm-io__aop__iop-aop-nub__SPUApp.md) = `02030a02fd0008f0e843000130010101` |
| `spkamp-config_btmspk` | 1 | 16 B | [`/arm-io/aop/iop-aop-nub/SPUApp`](../devicetree/root__arm-io__aop__iop-aop-nub__SPUApp.md) = `05060002fd0008f0e84000013a010001` |
| `spkamp-names` | 1 | string | [`/arm-io/aop/iop-aop-nub/SPUApp`](../devicetree/root__arm-io__aop__iop-aop-nub__SPUApp.md) = `arc, btmspk` |
| `spmiFollowerReset` | 1 | u32 | [`/arm-io/aop-spmi0/stockholm-spmi`](../devicetree/root__arm-io__aop-spmi0__stockholm-spmi.md) = `0x1` |
| `sptm-allow-internal-reg` | 1 | 256 B | [`/arm-io/cpu-debug-interface`](../devicetree/root__arm-io__cpu-debug-interface.md) = `000000600000000000c0000000000000…` |
| `sptm-allow-reg` | 7 | 16 B×3, 64 B×2, 48 B | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0000848c000000000000040000000000…`<br>[`/arm-io/smc/iop-smc-nub`](../devicetree/root__arm-io__smc__iop-smc-nub.md) = `0000e08d020000000000140000000000`<br>[`/arm-io/mtp`](../devicetree/root__arm-io__mtp.md) = `0000c094000000000000280000000000`<br>[`/arm-io/jpeg`](../devicetree/root__arm-io__jpeg.md) = `00000006020000000000000100000000`<br>[`/arm-io/ane0`](../devicetree/root__arm-io__ane0.md) = `000020810000000000c0000000000000…` |
| `sram-index` | 2 | u32×2 | [`/arm-io/pmp`](../devicetree/root__arm-io__pmp.md) = `0x1`<br>[`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0x1` |
| `sram-t-agents` | 1 | 40 B | [`/arm-io/aop/iop-aop-nub/aop-gapf-filters`](../devicetree/root__arm-io__aop__iop-aop-nub__aop-gapf-filters.md) = `ad530300ff0ff8ffaf530300ff0ff8ff…` |
| `sram-t-agents-count` | 1 | u32 | [`/arm-io/aop/iop-aop-nub/aop-gapf-filters`](../devicetree/root__arm-io__aop__iop-aop-nub__aop-gapf-filters.md) = `0x5` |
| `sram-ut-agents` | 1 | 24 B | [`/arm-io/aop/iop-aop-nub/aop-gapf-filters`](../devicetree/root__arm-io__aop__iop-aop-nub__aop-gapf-filters.md) = `ae530300ff0ff8ffb2530300ff0ff8ff…` |
| `sram-ut-agents-count` | 1 | u32 | [`/arm-io/aop/iop-aop-nub/aop-gapf-filters`](../devicetree/root__arm-io__aop__iop-aop-nub__aop-gapf-filters.md) = `0x3` |
| `sss-horizon-low-power-thresh` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x8000` |
| `stackshot-mask` | 1 | string | [`/buttons`](../devicetree/root__buttons.md) = `voldown, volup, hold` |
| `stage-light-portrait-preview` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x1` |
| `start-time` | 1 | u32 | [`/chosen/iBoot`](../devicetree/root__chosen__iBoot.md) = `0x0` |
| `state` | 6 | string×6 | [`/cpus/cpu0`](../devicetree/root__cpus__cpu0.md) = `waiting`<br>[`/cpus/cpu1`](../devicetree/root__cpus__cpu1.md) = `waiting`<br>[`/cpus/cpu2`](../devicetree/root__cpus__cpu2.md) = `waiting`<br>[`/cpus/cpu3`](../devicetree/root__cpus__cpu3.md) = `waiting`<br>[`/cpus/cpu4`](../devicetree/root__cpus__cpu4.md) = `waiting` |
| `std-dev-x-cal` | 1 | u32 | [`/arm-io/aop/iop-aop-nub/jarvis`](../devicetree/root__arm-io__aop__iop-aop-nub__jarvis.md) = `0x5a0000` |
| `std-dev-y-cal` | 1 | u32 | [`/arm-io/aop/iop-aop-nub/jarvis`](../devicetree/root__arm-io__aop__iop-aop-nub__jarvis.md) = `0x5a0000` |
| `std-dev-z-cal` | 1 | u32 | [`/arm-io/aop/iop-aop-nub/jarvis`](../devicetree/root__arm-io__aop__iop-aop-nub__jarvis.md) = `0x320000` |
| `stereo-sound-recording` | 1 | u32 | [`/product/audio`](../devicetree/root__product__audio.md) = `0x1` |
| `stop_clocks` | 1 | 96 B | [`/arm-io/cpu-debug-interface`](../devicetree/root__arm-io__cpu-debug-interface.md) = `00000210000000007806000000000000…` |
| `strobe-coex` | 1 | u32 | [`/arm-io/aop/iop-aop-nub/als`](../devicetree/root__arm-io__aop__iop-aop-nub__als.md) = `0x2` |
| `sub-product-type` | 1 | string | [`/product`](../devicetree/root__product.md) = `iPhone19,4` |
| `support-dptx-fifo-telemetry` | 2 | u32×2 | [`/arm-io/dcp0-expert`](../devicetree/root__arm-io__dcp0-expert.md) = `0x1`<br>[`/arm-io/dcpsec-expert`](../devicetree/root__arm-io__dcpsec-expert.md) = `0x1` |
| `support-health-telemetry` | 2 | u32×2 | [`/arm-io/dcp0-expert`](../devicetree/root__arm-io__dcp0-expert.md) = `0x1`<br>[`/arm-io/dcpsec-expert`](../devicetree/root__arm-io__dcpsec-expert.md) = `0x1` |
| `support-psd-self-vote` | 3 | u32×3 | [`/arm-io/dcp0-expert`](../devicetree/root__arm-io__dcp0-expert.md) = `0x1`<br>[`/arm-io/dcpsec-expert`](../devicetree/root__arm-io__dcpsec-expert.md) = `0x1`<br>[`/arm-io/dcpext0-expert`](../devicetree/root__arm-io__dcpext0-expert.md) = `0x1` |
| `support-standalone` | 2 | u32×2 | [`/arm-io/dcp0-expert`](../devicetree/root__arm-io__dcp0-expert.md) = `0x1`<br>[`/arm-io/dcpsec-expert`](../devicetree/root__arm-io__dcpsec-expert.md) = `0x1` |
| `supported-all-radio-version` | 1 | u32 | [`/arm-io/aop-spmi1/baseband-idc`](../devicetree/root__arm-io__aop-spmi1__baseband-idc.md) = `0x206` |
| `supported-ap-gpr0-version` | 1 | u32 | [`/arm-io/aop-spmi1/baseband-idc`](../devicetree/root__arm-io__aop-spmi1__baseband-idc.md) = `0x206` |
| `supported-ar-buffer-version` | 1 | u32 | [`/arm-io/aop-spmi1/baseband-idc`](../devicetree/root__arm-io__aop-spmi1__baseband-idc.md) = `0x206` |
| `supported-int-groups` | 5 | 16 B×2, 12 B×2, u64 | [`/arm-io/aop-gpio`](../devicetree/root__arm-io__aop-gpio.md) = `03000000040000000500000006000000`<br>[`/arm-io/nub-gpio`](../devicetree/root__arm-io__nub-gpio.md) = `040000000500000006000000`<br>[`/arm-io/smc-gpio`](../devicetree/root__arm-io__smc-gpio.md) = `0x600000005`<br>[`/arm-io/mtp-gpio`](../devicetree/root__arm-io__mtp-gpio.md) = `040000000500000006000000`<br>[`/arm-io/secure-repair`](../devicetree/root__arm-io__secure-repair.md) = `03000000040000000500000006000000` |
| `supported-non-radio-version` | 1 | u32 | [`/arm-io/aop-spmi1/baseband-idc`](../devicetree/root__arm-io__aop-spmi1__baseband-idc.md) = `0x206` |
| `supportedChannels` | 1 | u32 | [`/product/audio`](../devicetree/root__product__audio.md) = `0xf` |
| `supports-3rd-party-haptics` | 1 | u32 | [`/product/haptics`](../devicetree/root__product__haptics.md) = `0x1` |
| `supports-advanced-vp-chatflavor` | 1 | u32 | [`/product/audio`](../devicetree/root__product__audio.md) = `0x1` |
| `supports-always-listening` | 1 | u32 | [`/product/audio`](../devicetree/root__product__audio.md) = `0x1` |
| `supports-ammolite` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x1`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x1`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x1` |
| `supports-apple-pencil` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `supports-apt` | 2 | u32×2 | [`/arm-io/disp0`](../devicetree/root__arm-io__disp0.md) = `0x1`<br>[`/arm-io/dispsec`](../devicetree/root__arm-io__dispsec.md) = `0x1` |
| `supports-audio-mix` | 1 | u32 | [`/product/audio`](../devicetree/root__product__audio.md) = `0x1` |
| `supports-auto-mic-mode` | 1 | u32 | [`/product/audio`](../devicetree/root__product__audio.md) = `0x1` |
| `supports-avatars` | 1 | empty | [`/product`](../devicetree/root__product.md) = `` |
| `supports-barge-in` | 1 | u32 | [`/product/audio`](../devicetree/root__product__audio.md) = `0x1` |
| `supports-burnin-mitigation` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `supports-camera-button` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `supports-cellular-boost` | 1 | u32 | [`/arm-io/aop-spmi1/baseband-idc`](../devicetree/root__arm-io__aop-spmi1__baseband-idc.md) = `0x0` |
| `supports-cltm-aware-aurora` | 1 | u32 | [`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x1` |
| `supports-concurrent-hp-lp-mics` | 1 | u32 | [`/product/audio`](../devicetree/root__product__audio.md) = `0x1` |
| `supports-cpms-via-spmi` | 1 | u32 | [`/baseband`](../devicetree/root__baseband.md) = `0x1` |
| `supports-float-lux` | 3 | u32×3 | [`/arm-io/aop/iop-aop-nub/als2a`](../devicetree/root__arm-io__aop__iop-aop-nub__als2a.md) = `0x1`<br>[`/arm-io/aop/iop-aop-nub/als2b`](../devicetree/root__arm-io__aop__iop-aop-nub__als2b.md) = `0x1`<br>[`/arm-io/aop/iop-aop-nub/als`](../devicetree/root__arm-io__aop__iop-aop-nub__als.md) = `0x1` |
| `supports-gcp` | 1 | u32 | [`/backlight`](../devicetree/root__backlight.md) = `0x1` |
| `supports-gray-dimming` | 1 | empty | [`/product`](../devicetree/root__product.md) = `` |
| `supports-hsar-cellular` | 1 | u32 | [`/arm-io/aop-spmi1/baseband-idc`](../devicetree/root__arm-io__aop-spmi1__baseband-idc.md) = `0x1` |
| `supports-hsar-wifi-bt` | 1 | u32 | [`/arm-io/aop-spmi1/baseband-idc`](../devicetree/root__arm-io__aop-spmi1__baseband-idc.md) = `0x1` |
| `supports-lotx` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `supports-maps-optical-heading` | 1 | empty | [`/product`](../devicetree/root__product.md) = `` |
| `supports-mic-modes-telephony` | 1 | u32 | [`/product/audio`](../devicetree/root__product__audio.md) = `0x1` |
| `supports-multiple-user-clients` | 1 | empty | [`/arm-io/iop-audio-controller/siri-listening-device`](../devicetree/root__arm-io__iop-audio-controller__siri-listening-device.md) = `` |
| `supports-nfc-reader-mode` | 2 | empty×2 | [`/arm-io/aop-spmi0/stockholm-spmi/stockholm`](../devicetree/root__arm-io__aop-spmi0__stockholm-spmi__stockholm.md) = ``<br>[`/arm-io/aop-spmi0/hammerfest-spmi/hammerfest`](../devicetree/root__arm-io__aop-spmi0__hammerfest-spmi__hammerfest.md) = `` |
| `supports-personal-translator` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `supports-recoveryos` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `supports-spatial-audio-capture` | 1 | u32 | [`/product/audio`](../devicetree/root__product__audio.md) = `0x1` |
| `supports-spatial-facetime` | 1 | u32 | [`/product/audio`](../devicetree/root__product__audio.md) = `0x1` |
| `supports-twilight` | 4 | u32×4 | [`/backlight`](../devicetree/root__backlight.md) = `0x1`<br>[`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x1`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x1`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x1` |
| `surface-type` | 4 | u32×4 | [`/arm-io/disp0`](../devicetree/root__arm-io__disp0.md) = `0x1`<br>[`/arm-io/dispsec`](../devicetree/root__arm-io__dispsec.md) = `0x2`<br>[`/product/display0`](../devicetree/root__product__display0.md) = `0x1`<br>[`/product/display1`](../devicetree/root__product__display1.md) = `0x2` |
| `sw-err-rsv-bits` | 1 | u32 | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0x7` |
| `sync-display-state-control` | 1 | u32 | [`/core-brightness`](../devicetree/root__core-brightness.md) = `0x1` |
| `sync-preset` | 1 | 192 B | [`/arm-io/msg`](../devicetree/root__arm-io__msg.md) = `00000100000000000000000001000000…` |
| `sync_lookup` | 1 | 136 B | [`/arm-io/msg`](../devicetree/root__arm-io__msg.md) = `6261636b2d63616d6572612d636f6d70…` |
| `syncdbv-supported` | 1 | u32 | [`/core-brightness`](../devicetree/root__core-brightness.md) = `0x1` |
| `sysconfig-location-id-override` | 2 | u32×2 | [`/arm-io/aop/iop-aop-nub/compass`](../devicetree/root__arm-io__aop__iop-aop-nub__compass.md) = `0x0`<br>[`/arm-io/aop/iop-aop-nub/compass_1`](../devicetree/root__arm-io__aop__iop-aop-nub__compass_1.md) = `0x1` |
| `system-events-required` | 1 | u32 | [`/arm-io/apcie/pci-bridge0/centauri-control`](../devicetree/root__arm-io__apcie__pci-bridge0__centauri-control.md) = `0x0` |
| `system-load-inputs-Peff` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0xfae1` |
| `system-load-inputs-Pk` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x8000` |
| `system-load-inputs-Pt` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x10000` |
| `system-trusted` | 1 | u32 | [`/chosen`](../devicetree/root__chosen.md) = `0x0` |
| `system-utilization-gpu-in-en` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x1` |
| `system-utilization-gpu-out-en` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x1` |
| `systemloadinput-ptle-rank-pp` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x55` |
| `systemloadinput-ptle-rank-ps` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x5a` |
| `t-refclk-to-perst` | 2 | u32×2 | [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) = `0x64`<br>[`/arm-io/apcie/pci-bridge1`](../devicetree/root__arm-io__apcie__pci-bridge1.md) = `0x64` |
| `tail-padding` | 1 | u32 | [`/arm-io/dart-jpeg/mapper-jpeg`](../devicetree/root__arm-io__dart-jpeg__mapper-jpeg.md) = `0x1` |
| `target-sub-type` | 1 | string | [`/`](../devicetree/root.md) = `V68AP` |
| `target-type` | 1 | string | [`/`](../devicetree/root.md) = `V68` |
| `tcal-cal` | 1 | string | [`/arm-io/haptics-support-interface`](../devicetree/root__arm-io__haptics-support-interface.md) = `syscfg/TCal` |
| `tcal-cal-mi` | 1 | string | [`/arm-io/haptics-support-interface`](../devicetree/root__arm-io__haptics-support-interface.md) = `syscfg-mismatch/TCal` |
| `temp-compensation-table` | 1 | string | [`/arm-io/aop/iop-aop-nub/pressure`](../devicetree/root__arm-io__aop__iop-aop-nub__pressure.md) = `syscfg/PRTT` |
| `temp-sensor` | 2 | 1232 B, 1624 B | [`/arm-io/pmp/iop-pmp-nub/:borneo_h19a_2`](../devicetree/root__arm-io__pmp__iop-pmp-nub___borneo_h19a_2.md) = `01000000080000000600000000000000…`<br>[`/arm-io/pmp/iop-pmp-nub/:borneo_h19p_2`](../devicetree/root__arm-io__pmp__iop-pmp-nub___borneo_h19p_2.md) = `01000000080000000600000000000000…` |
| `terminate-missing-endpoint` | 1 | empty | [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) = `` |
| `thermal-budget-range` | 1 | 12 B | [`/arm-io/iop-audio-controller/audio-haptic`](../devicetree/root__arm-io__iop-audio-controller__audio-haptic.md) = `3f0b0000770100003f0b0000` |
| `thermal-interval-ms` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0xc` |
| `theta-attach-high-cal` | 1 | u32 | [`/arm-io/aop/iop-aop-nub/jarvis`](../devicetree/root__arm-io__aop__iop-aop-nub__jarvis.md) = `0x323d7` |
| `theta-attach-low-cal` | 1 | u32 | [`/arm-io/aop/iop-aop-nub/jarvis`](../devicetree/root__arm-io__aop__iop-aop-nub__jarvis.md) = `0x0` |
| `theta-detach-high-cal` | 1 | u32 | [`/arm-io/aop/iop-aop-nub/jarvis`](../devicetree/root__arm-io__aop__iop-aop-nub__jarvis.md) = `0x323d7` |
| `theta-detach-low-cal` | 1 | u32 | [`/arm-io/aop/iop-aop-nub/jarvis`](../devicetree/root__arm-io__aop__iop-aop-nub__jarvis.md) = `0x0` |
| `thin-bezel` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `time-between-scans` | 1 | u32 | [`/arm-io/spi1/mesa`](../devicetree/root__arm-io__spi1__mesa.md) = `0x20000` |
| `time-stamp` | 1 | string | [`/`](../devicetree/root.md) = `Tue Oct 13 23:32:31 PDT 2026` |
| `timerInterval` | 1 | u32 | [`/arm-io/smctempsensor0`](../devicetree/root__arm-io__smctempsensor0.md) = `0x3e8` |
| `timers-reg-index` | 1 | u32 | [`/arm-io/smc`](../devicetree/root__arm-io__smc.md) = `0x3` |
| `tlbi-aperture-offset` | 23 | u64×23 | [`/arm-io/dart-sep`](../devicetree/root__arm-io__dart-sep.md) = `0x700`<br>[`/arm-io/dart-sio`](../devicetree/root__arm-io__dart-sio.md) = `0x780`<br>[`/arm-io/dart-sbr`](../devicetree/root__arm-io__dart-sbr.md) = `0x680`<br>[`/arm-io/dart-usb0`](../devicetree/root__arm-io__dart-usb0.md) = `0x100`<br>[`/arm-io/dart-dcp`](../devicetree/root__arm-io__dart-dcp.md) = `0x280` |
| `tlbi-flushes-smmu` | 6 | empty×6 | [`/arm-io/dart-disp0`](../devicetree/root__arm-io__dart-disp0.md) = ``<br>[`/arm-io/dart-dispgrt`](../devicetree/root__arm-io__dart-dispgrt.md) = ``<br>[`/arm-io/dart-dcpsec`](../devicetree/root__arm-io__dart-dcpsec.md) = ``<br>[`/arm-io/dart-dispsec`](../devicetree/root__arm-io__dart-dispsec.md) = ``<br>[`/arm-io/dart-dispsecgrt`](../devicetree/root__arm-io__dart-dispsecgrt.md) = `` |
| `tnr-mode-back` | 1 | u32 | [`/product/facetime`](../devicetree/root__product__facetime.md) = `0xa` |
| `tnr-mode-front` | 1 | u32 | [`/product/facetime`](../devicetree/root__product__facetime.md) = `0xa` |
| `transport-encoding` | 1 | u32 | [`/arm-io/bluetooth`](../devicetree/root__arm-io__bluetooth.md) = `0x9` |
| `transport-tunneled` | 1 | u32 | [`/arm-io/atc0-dpphy`](../devicetree/root__arm-io__atc0-dpphy.md) = `0x0` |
| `transport-type` | 1 | u32 | [`/arm-io/atc0-dpphy`](../devicetree/root__arm-io__atc0-dpphy.md) = `0x5` |
| `transports-supported` | 2 | 16 B, u32 | [`/arm-io/nub-spmi2/spmi-hpm0`](../devicetree/root__arm-io__nub-spmi2__spmi-hpm0.md) = `01000000020000000300000005000000`<br>[`/port-magsafe-1`](../devicetree/root__port-magsafe-1.md) = `0xf` |
| `trigger-ce` | 1 | 16 B | [`/arm-io/wdt`](../devicetree/root__arm-io__wdt.md) = `68007880020000000000000001000000` |
| `trigger-config` | 1 | 96 B | [`/arm-io/wdt`](../devicetree/root__arm-io__wdt.md) = `84020210020000000f00000001000000…` |
| `trigger_lookup` | 1 | 136 B | [`/arm-io/msg`](../devicetree/root__arm-io__msg.md) = `65787465726e616c2d73796e632d7072…` |
| `trm-enabled` | 1 | u32 | [`/defaults`](../devicetree/root__defaults.md) = `0x1` |
| `trm-profile` | 1 | u32 | [`/defaults`](../devicetree/root__defaults.md) = `0x3` |
| `truetone-strength` | 3 | 24 B×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `00000000713d8a3e713d8a3ecdcc4c3e…`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `00000000713d8a3e713d8a3ecdcc4c3e…`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `00000000713d8a3e713d8a3ecdcc4c3e…` |
| `ttw-supported` | 2 | empty×2 | [`/arm-io/mtp/iop-mtp-nub/multi-touch2`](../devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch2.md) = ``<br>[`/arm-io/mtp/iop-mtp-nub/multi-touch`](../devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch.md) = `` |
| `tunable-table-bundle` | 1 | string | [`/arm-io/ans`](../devicetree/root__arm-io__ans.md) = `qwdbnujv` |
| `tunable-target` | 2 | string×2 | [`/arm-io/exdisplaypipe`](../devicetree/root__arm-io__exdisplaypipe.md) = `TDispTargetP68`<br>[`/arm-io/exdisplaypipe1`](../devicetree/root__arm-io__exdisplaypipe1.md) = `TDispTargetS68` |
| `tw-lux-activation-threshold` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x42c7fff3`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x42c7fff3`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x42c7fff3` |
| `tw-lux-table` | 3 | 36 B×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `00000000000020410000a0410000f041…`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `00000000000020410000a0410000f041…`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `00000000000020410000a0410000f041…` |
| `tw-nits-activation-threshold` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x41200000`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x41200000`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x41200000` |
| `tw-nits-table` | 3 | 40 B×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0000803f000000400000404000008040…`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0000803f000000400000404000008040…`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0000803f000000400000404000008040…` |
| `tw-ramp-aod-duration` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x40000000`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x40000000`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x40000000` |
| `tw-ramp-bezier-anchors` | 3 | 12 B×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `9a99993e6666663f9a99593f`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `9a99993e6666663f9a99593f`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `9a99993e6666663f9a99593f` |
| `tw-ramp-down-duration` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x40a00000`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x40a00000`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x40a00000` |
| `tw-ramp-down-lux-threshold` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x41900000`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x41900000`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x41900000` |
| `tw-ramp-up-duration` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x40a00000`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x40a00000`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x40a00000` |
| `tw-ramp-up-lux-threshold` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x41700000`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x41700000`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x41700000` |
| `tw-ramp-update-rate` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x42700000`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x42700000`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x42700000` |
| `tw-strength-table` | 3 | 360 B×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0000403f4ca62a3f2653153f0000003f…`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0000403f4ca62a3f2653153f0000003f…`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0000403f4ca62a3f2653153f0000003f…` |
| `tw-supported` | 4 | u32×4 | [`/backlight`](../devicetree/root__backlight.md) = `0x1`<br>[`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x1`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x1`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x1` |
| `txm-secure-channel` | 1 | u32 | [`/chosen`](../devicetree/root__chosen.md) = `0x1` |
| `txm-secure-channel-base` | 1 | u64 | [`/arm-io/dart-sep`](../devicetree/root__arm-io__dart-sep.md) = `0x10000004000` |
| `txm-secure-channel-size` | 1 | string | [`/arm-io/dart-sep`](../devicetree/root__arm-io__dart-sep.md) = `@` |
| `uart-version` | 1 | u32 | [`/arm-io/uart0`](../devicetree/root__arm-io__uart0.md) = `0x1` |
| `uat-enforce-gpu-carveout` | 1 | u32 | [`/defaults`](../devicetree/root__defaults.md) = `0x0` |
| `uat-vaddr-size` | 1 | u32 | [`/defaults`](../devicetree/root__defaults.md) = `0x2b` |
| `ucert-offset` | 1 | u32 | [`/arm-io/sep`](../devicetree/root__arm-io__sep.md) = `0x0` |
| `ucert-size` | 1 | u32 | [`/arm-io/sep`](../devicetree/root__arm-io__sep.md) = `0x24c` |
| `ucont-offset` | 1 | u32 | [`/arm-io/sep`](../devicetree/root__arm-io__sep.md) = `0x250` |
| `ucont-size` | 1 | u32 | [`/arm-io/sep`](../devicetree/root__arm-io__sep.md) = `0x52c` |
| `udid-version` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x2` |
| `ufp-count` | 1 | u32 | [`/arm-io/display-crossbar0`](../devicetree/root__arm-io__display-crossbar0.md) = `0x1` |
| `ufp-endpoints` | 1 | string | [`/arm-io/display-crossbar0`](../devicetree/root__arm-io__display-crossbar0.md) = `dispext0, dispext1` |
| `ui-background-quality` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x64` |
| `ui-pip` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `ui-present-boost-constraint-us` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0xbb8` |
| `ui-present-constraint-min-us` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x7d0` |
| `ui-present-cpu-work-high-floor` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0x1999` |
| `ui-present-util-target-l0s` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0xe666` |
| `ui-present-util-target-l1s` | 1 | u32 | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) = `0xe666` |
| `ui-weather-quality` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x64` |
| `uid` | 2 | string×2 | [`/arm-io/iop-audio-controller/audio-haptic`](../devicetree/root__arm-io__iop-audio-controller__audio-haptic.md) = `Actuator`<br>[`/arm-io/iop-audio-controller/audio-hpdbg`](../devicetree/root__arm-io__iop-audio-controller__audio-hpdbg.md) = `Haptic Debug` |
| `uid-aes-key` | 1 | u32 | [`/chosen`](../devicetree/root__chosen.md) = `0x0` |
| `unique-chip-id` | 1 | u64 | [`/chosen`](../devicetree/root__chosen.md) = `0x0` |
| `unique-device-id` | 1 | 16 B | [`/chosen`](../devicetree/root__chosen.md) = `00000000000000000000000000000000` |
| `unique-model` | 1 | string | [`/product`](../devicetree/root__product.md) = `V68AP` |
| `unrestricted-subsystem-root` | 1 | u32 | [`/chosen`](../devicetree/root__chosen.md) = `0x0` |
| `UnusedBooleanProperty0` | 2 | u32×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `0x0`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `0x0` |
| `UnusedBooleanProperty1` | 2 | u32×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `0x0`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `0x0` |
| `UnusedBooleanProperty10` | 2 | u32×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `0x0`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `0x0` |
| `UnusedBooleanProperty11` | 2 | u32×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `0x0`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `0x0` |
| `UnusedBooleanProperty12` | 2 | u32×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `0x0`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `0x0` |
| `UnusedBooleanProperty13` | 2 | u32×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `0x0`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `0x0` |
| `UnusedBooleanProperty14` | 2 | u32×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `0x0`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `0x0` |
| `UnusedBooleanProperty15` | 2 | u32×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `0x0`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `0x0` |
| `UnusedBooleanProperty16` | 2 | u32×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `0x0`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `0x0` |
| `UnusedBooleanProperty17` | 2 | u32×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `0x0`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `0x0` |
| `UnusedBooleanProperty18` | 2 | u32×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `0x0`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `0x0` |
| `UnusedBooleanProperty19` | 2 | u32×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `0x0`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `0x0` |
| `UnusedBooleanProperty2` | 2 | u32×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `0x0`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `0x0` |
| `UnusedBooleanProperty3` | 2 | u32×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `0x0`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `0x0` |
| `UnusedBooleanProperty4` | 2 | u32×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `0x0`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `0x0` |
| `UnusedBooleanProperty5` | 2 | u32×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `0x0`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `0x0` |
| `UnusedBooleanProperty6` | 2 | u32×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `0x0`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `0x0` |
| `UnusedBooleanProperty7` | 2 | u32×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `0x0`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `0x0` |
| `UnusedBooleanProperty8` | 2 | u32×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `0x0`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `0x0` |
| `UnusedBooleanProperty9` | 2 | u32×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `0x0`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `0x0` |
| `UnusedIntegerProperty0` | 2 | u64×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `0x0`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `0x0` |
| `UnusedIntegerProperty1` | 2 | u64×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `0x0`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `0x0` |
| `UnusedIntegerProperty10` | 2 | u64×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `0x0`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `0x0` |
| `UnusedIntegerProperty11` | 2 | u64×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `0x0`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `0x0` |
| `UnusedIntegerProperty12` | 2 | u64×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `0x0`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `0x0` |
| `UnusedIntegerProperty13` | 2 | u64×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `0x0`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `0x0` |
| `UnusedIntegerProperty14` | 2 | u64×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `0x0`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `0x0` |
| `UnusedIntegerProperty15` | 2 | u64×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `0x0`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `0x0` |
| `UnusedIntegerProperty16` | 2 | u64×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `0x0`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `0x0` |
| `UnusedIntegerProperty17` | 2 | u64×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `0x0`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `0x0` |
| `UnusedIntegerProperty18` | 2 | u64×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `0x0`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `0x0` |
| `UnusedIntegerProperty19` | 2 | u64×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `0x0`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `0x0` |
| `UnusedIntegerProperty2` | 2 | u64×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `0x0`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `0x0` |
| `UnusedIntegerProperty3` | 2 | u64×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `0x0`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `0x0` |
| `UnusedIntegerProperty4` | 2 | u64×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `0x0`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `0x0` |
| `UnusedIntegerProperty5` | 2 | u64×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `0x0`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `0x0` |
| `UnusedIntegerProperty6` | 2 | u64×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `0x0`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `0x0` |
| `UnusedIntegerProperty7` | 2 | u64×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `0x0`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `0x0` |
| `UnusedIntegerProperty8` | 2 | u64×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `0x0`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `0x0` |
| `UnusedIntegerProperty9` | 2 | u64×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `0x0`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `0x0` |
| `UnusedStringProperty0` | 2 | 64 B×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `00000000000000000000000000000000…`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `00000000000000000000000000000000…` |
| `UnusedStringProperty1` | 2 | 64 B×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `00000000000000000000000000000000…`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `00000000000000000000000000000000…` |
| `UnusedStringProperty2` | 2 | 64 B×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `00000000000000000000000000000000…`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `00000000000000000000000000000000…` |
| `UnusedStringProperty3` | 2 | 64 B×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `00000000000000000000000000000000…`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `00000000000000000000000000000000…` |
| `UnusedStringProperty4` | 2 | 64 B×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `00000000000000000000000000000000…`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `00000000000000000000000000000000…` |
| `UnusedStringProperty5` | 2 | 64 B×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `00000000000000000000000000000000…`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `00000000000000000000000000000000…` |
| `UnusedStringProperty6` | 2 | 64 B×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `00000000000000000000000000000000…`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `00000000000000000000000000000000…` |
| `UnusedStringProperty7` | 2 | 64 B×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `00000000000000000000000000000000…`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `00000000000000000000000000000000…` |
| `UnusedStringProperty8` | 2 | 64 B×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `00000000000000000000000000000000…`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `00000000000000000000000000000000…` |
| `UnusedStringProperty9` | 2 | 64 B×2 | [`/chosen/manifest-properties`](../devicetree/root__chosen__manifest-properties.md) = `00000000000000000000000000000000…`<br>[`/chosen/manifest-object-properties`](../devicetree/root__chosen__manifest-object-properties.md) = `00000000000000000000000000000000…` |
| `upo-shutdown-delay` | 1 | u32 | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) = `0x0` |
| `usb-c-smc-pwr` | 1 | empty | [`/product`](../devicetree/root__product.md) = `` |
| `usb-control-request-policy` | 1 | u32 | [`/arm-io/usb-drd0`](../devicetree/root__arm-io__usb-drd0.md) = `0x1` |
| `usb-max-speed-capability` | 1 | u32 | [`/arm-io/usb-drd0/:borneo_h19a_5`](../devicetree/root__arm-io__usb-drd0___borneo_h19a_5.md) = `0x2` |
| `usb-port-current-limit` | 2 | u32×2 | [`/arm-io/usb-drd0/usb-drd0-port-hs`](../devicetree/root__arm-io__usb-drd0__usb-drd0-port-hs.md) = `0x384`<br>[`/arm-io/usb-drd0/:borneo_h19p_5/usb-drd0-port-ss`](../devicetree/root__arm-io__usb-drd0___borneo_h19p_5__usb-drd0-port-ss.md) = `0x384` |
| `usb-port-number` | 2 | u32×2 | [`/arm-io/usb-drd0/usb-drd0-port-hs`](../devicetree/root__arm-io__usb-drd0__usb-drd0-port-hs.md) = `0x1`<br>[`/arm-io/usb-drd0/:borneo_h19p_5/usb-drd0-port-ss`](../devicetree/root__arm-io__usb-drd0___borneo_h19p_5__usb-drd0-port-ss.md) = `0x2` |
| `usb-repeater` | 1 | u32 | [`/arm-io/usb-drd0`](../devicetree/root__arm-io__usb-drd0.md) = `0x746e7420` |
| `usb-soft-retry-policy` | 1 | u32 | [`/arm-io/usb-drd0`](../devicetree/root__arm-io__usb-drd0.md) = `0x2` |
| `usb-storage-workaround` | 1 | u32 | [`/defaults`](../devicetree/root__defaults.md) = `0x1` |
| `usbphy-frequency` | 1 | u32 | [`/arm-io`](../devicetree/root__arm-io.md) = `0x0` |
| `use-case` | 4 | u32×4 | [`/arm-io/admac-hp-mic-ec-proxy`](../devicetree/root__arm-io__admac-hp-mic-ec-proxy.md) = `0x68706169`<br>[`/arm-io/admac-speaker-tx-ec-proxy`](../devicetree/root__arm-io__admac-speaker-tx-ec-proxy.md) = `0x73706b4f`<br>[`/arm-io/admac-receiver-tx-ec-proxy`](../devicetree/root__arm-io__admac-receiver-tx-ec-proxy.md) = `0x72656376`<br>[`/arm-io/admac-sllb-ec-proxy`](../devicetree/root__arm-io__admac-sllb-ec-proxy.md) = `0x736c6c62` |
| `use-case-client-format` | 1 | 192 B | [`/product/audio`](../devicetree/root__product__audio.md) = `61646e7380bb00000100000000040000…` |
| `use-case-dsp-in-format` | 1 | 224 B | [`/product/audio`](../devicetree/root__product__audio.md) = `646b746d80bb00000400000000040000…` |
| `use-case-struct-version` | 1 | u32 | [`/product/audio`](../devicetree/root__product__audio.md) = `0x1` |
| `use-filtered-Rss-I3-I4` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x1` |
| `use-lwvm` | 1 | empty | [`/defaults`](../devicetree/root__defaults.md) = `` |
| `use-modern-cpms` | 3 | u32×3 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x1`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x1`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x1` |
| `use-prox-for-occlusion` | 3 | u32×3 | [`/arm-io/aop/iop-aop-nub/als2a`](../devicetree/root__arm-io__aop__iop-aop-nub__als2a.md) = `0x0`<br>[`/arm-io/aop/iop-aop-nub/als2b`](../devicetree/root__arm-io__aop__iop-aop-nub__als2b.md) = `0x0`<br>[`/arm-io/aop/iop-aop-nub/als`](../devicetree/root__arm-io__aop__iop-aop-nub__als.md) = `0x1` |
| `use-recovery-securityd` | 1 | u32 | [`/chosen`](../devicetree/root__chosen.md) = `0x0` |
| `usecase-dart-map` | 1 | 24 B | [`/arm-io/audio-shared-dart-proxy`](../devicetree/root__arm-io__audio-shared-dart-proxy.md) = `69617068000000007870646100000000…` |
| `user-accessible-max-nits` | 4 | u32×4 | [`/core-brightness/brightness-primary`](../devicetree/root__core-brightness__brightness-primary.md) = `0x4240000`<br>[`/core-brightness/brightness-secondary`](../devicetree/root__core-brightness__brightness-secondary.md) = `0x4240000`<br>[`/core-brightness/brightness-secondary-doe1`](../devicetree/root__core-brightness__brightness-secondary-doe1.md) = `0x4240000`<br>[`/exbright`](../devicetree/root__exbright.md) = `0x4240000` |
| `user-power-managed` | 7 | u32×5, string×2 | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) = `0x1`<br>[`/arm-io/sio/iop-sio-nub`](../devicetree/root__arm-io__sio__iop-sio-nub.md) = `0x1`<br>[`/arm-io/smc/iop-smc-nub`](../devicetree/root__arm-io__smc__iop-smc-nub.md) = `0x1`<br>[`/arm-io/ispRtb/iop-isp-nub`](../devicetree/root__arm-io__ispRtb__iop-isp-nub.md) = `true`<br>[`/arm-io/ane0/iop-ane0-nub`](../devicetree/root__arm-io__ane0__iop-ane0-nub.md) = `0x1` |
| `value` | 27 | u32×27 | [`/osenvironments/recovery-environment/ephemeral-storage`](../devicetree/root__osenvironments__recovery-environment__ephemeral-storage.md) = `0x1`<br>[`/osenvironments/recovery-environment/no-sepfw-load-at-boot`](../devicetree/root__osenvironments__recovery-environment__no-sepfw-load-at-boot.md) = `0x0`<br>[`/osenvironments/recovery-environment/no-protected-data-access`](../devicetree/root__osenvironments__recovery-environment__no-protected-data-access.md) = `0x0`<br>[`/osenvironments/recovery-environment/amfi-allows-trust-cache-load`](../devicetree/root__osenvironments__recovery-environment__amfi-allows-trust-cache-load.md) = `0x1`<br>[`/osenvironments/recovery-environment/disable-av-content-protection`](../devicetree/root__osenvironments__recovery-environment__disable-av-content-protection.md) = `0x1` |
| `version` | 1 | u32 | [`/:version`](../devicetree/root___version.md) = `0x1` |
| `vhci-ports` | 1 | u32 | [`/arm-io/rsm`](../devicetree/root__arm-io__rsm.md) = `0x696f7320` |
| `video-cap` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x2` |
| `video-stills` | 1 | u32 | [`/product/camera`](../devicetree/root__product__camera.md) = `0x1` |
| `virt-service-start` | 1 | u32 | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0x96` |
| `vm-alignment` | 3 | 12 B×3 | [`/arm-io/dart-disp0`](../devicetree/root__arm-io__dart-disp0.md) = `010000000800000008000000`<br>[`/arm-io/dart-dispsec`](../devicetree/root__arm-io__dart-dispsec.md) = `010000000800000008000000`<br>[`/arm-io/dart-dispext0`](../devicetree/root__arm-io__dart-dispext0.md) = `010000000800000008000000` |
| `vm-base` | 23 | u64×23 | [`/arm-io/dart-sep`](../devicetree/root__arm-io__dart-sep.md) = `0x10000000000`<br>[`/arm-io/dart-sio`](../devicetree/root__arm-io__dart-sio.md) = `0x10000000000`<br>[`/arm-io/dart-sbr`](../devicetree/root__arm-io__dart-sbr.md) = `0x10040000000`<br>[`/arm-io/dart-usb0`](../devicetree/root__arm-io__dart-usb0.md) = `0x10000004000`<br>[`/arm-io/dart-dcp`](../devicetree/root__arm-io__dart-dcp.md) = `0x10000000000` |
| `vm-base-0` | 1 | u64 | [`/arm-io/dart-sep`](../devicetree/root__arm-io__dart-sep.md) = `0x10000004000` |
| `vm-base-1` | 2 | u64×2 | [`/arm-io/dart-sep`](../devicetree/root__arm-io__dart-sep.md) = `0x10000000000`<br>[`/arm-io/dart-sbr`](../devicetree/root__arm-io__dart-sbr.md) = `0x20000000000` |
| `vm-base-14` | 2 | u64×2 | [`/arm-io/dart-disp0`](../devicetree/root__arm-io__dart-disp0.md) = `0x10000000000`<br>[`/arm-io/dart-dispsec`](../devicetree/root__arm-io__dart-dispsec.md) = `0x10000000000` |
| `vm-base-15` | 2 | u64×2 | [`/arm-io/dart-disp0`](../devicetree/root__arm-io__dart-disp0.md) = `0x10000000000`<br>[`/arm-io/dart-dispsec`](../devicetree/root__arm-io__dart-dispsec.md) = `0x10000000000` |
| `vm-base-2` | 1 | u64 | [`/arm-io/dart-sep`](../devicetree/root__arm-io__dart-sep.md) = `0x20000004000` |
| `vm-base-3` | 1 | u64 | [`/arm-io/dart-sbr`](../devicetree/root__arm-io__dart-sbr.md) = `0x20000000000` |
| `vm-base-4` | 2 | u64×2 | [`/arm-io/dart-dcp`](../devicetree/root__arm-io__dart-dcp.md) = `0x20000000000`<br>[`/arm-io/dart-dcpsec`](../devicetree/root__arm-io__dart-dcpsec.md) = `0x20000000000` |
| `vm-base-43` | 1 | u64 | [`/arm-io/dart-sbr`](../devicetree/root__arm-io__dart-sbr.md) = `0x10040000000` |
| `vm-force` | 4 | u64×4 | [`/arm-io/dart-apcie0/mapper-apcie0-control`](../devicetree/root__arm-io__dart-apcie0__mapper-apcie0-control.md) = `0x10000000000`<br>[`/arm-io/dart-apcie0/mapper-apcie0-alpha`](../devicetree/root__arm-io__dart-apcie0__mapper-apcie0-alpha.md) = `0x10000000000`<br>[`/arm-io/dart-apcie0/mapper-apcie0-beta`](../devicetree/root__arm-io__dart-apcie0__mapper-apcie0-beta.md) = `0x10000000000`<br>[`/arm-io/dart-apcie1/mapper-apcie1`](../devicetree/root__arm-io__dart-apcie1__mapper-apcie1.md) = `0x10000000000` |
| `vm-offset` | 2 | 16 B×2 | [`/arm-io/dart-apcie0`](../devicetree/root__arm-io__dart-apcie0.md) = `00000000000000000000000800000000`<br>[`/arm-io/dart-apcie1`](../devicetree/root__arm-io__dart-apcie1.md) = `00000000000000000000000800000000` |
| `vm-reserve` | 1 | 16 B | [`/arm-io/dart-sep`](../devicetree/root__arm-io__dart-sep.md) = `004000000001000000c0000000010000` |
| `vm-size` | 23 | u64×23 | [`/arm-io/dart-sep`](../devicetree/root__arm-io__dart-sep.md) = `0x30000000000`<br>[`/arm-io/dart-sio`](../devicetree/root__arm-io__dart-sio.md) = `0x30000000000`<br>[`/arm-io/dart-sbr`](../devicetree/root__arm-io__dart-sbr.md) = `0x2ffc0000000`<br>[`/arm-io/dart-usb0`](../devicetree/root__arm-io__dart-usb0.md) = `0xffff0000`<br>[`/arm-io/dart-dcp`](../devicetree/root__arm-io__dart-dcp.md) = `0x30000000000` |
| `vm-size-0` | 1 | u64 | [`/arm-io/dart-sep`](../devicetree/root__arm-io__dart-sep.md) = `0xffff0000` |
| `vm-size-1` | 2 | string×2 | [`/arm-io/dart-sep`](../devicetree/root__arm-io__dart-sep.md) = `P`<br>[`/arm-io/dart-sbr`](../devicetree/root__arm-io__dart-sbr.md) = ` ` |
| `vm-size-11` | 2 | u64×2 | [`/arm-io/dart-disp0`](../devicetree/root__arm-io__dart-disp0.md) = `0x1000000000`<br>[`/arm-io/dart-dispsec`](../devicetree/root__arm-io__dart-dispsec.md) = `0x1000000000` |
| `vm-size-14` | 2 | u64×2 | [`/arm-io/dart-disp0`](../devicetree/root__arm-io__dart-disp0.md) = `0x1000000000`<br>[`/arm-io/dart-dispsec`](../devicetree/root__arm-io__dart-dispsec.md) = `0x1000000000` |
| `vm-size-15` | 2 | u64×2 | [`/arm-io/dart-disp0`](../devicetree/root__arm-io__dart-disp0.md) = `0x1000000000`<br>[`/arm-io/dart-dispsec`](../devicetree/root__arm-io__dart-dispsec.md) = `0x1000000000` |
| `vm-size-2` | 1 | u64 | [`/arm-io/dart-sep`](../devicetree/root__arm-io__dart-sep.md) = `0xffff0000` |
| `vm-size-21` | 2 | u64×2 | [`/arm-io/dart-disp0`](../devicetree/root__arm-io__dart-disp0.md) = `0x1000000000`<br>[`/arm-io/dart-dispsec`](../devicetree/root__arm-io__dart-dispsec.md) = `0x1000000000` |
| `vm-size-3` | 4 | u64×3, string | [`/arm-io/dart-sbr`](../devicetree/root__arm-io__dart-sbr.md) = ` `<br>[`/arm-io/dart-dcp`](../devicetree/root__arm-io__dart-dcp.md) = `0x1000000000`<br>[`/arm-io/dart-dcpsec`](../devicetree/root__arm-io__dart-dcpsec.md) = `0x1000000000`<br>[`/arm-io/dart-dcpext0`](../devicetree/root__arm-io__dart-dcpext0.md) = `0x1000000000` |
| `vm-size-4` | 2 | u64×2 | [`/arm-io/dart-dcp`](../devicetree/root__arm-io__dart-dcp.md) = `0x10000000000`<br>[`/arm-io/dart-dcpsec`](../devicetree/root__arm-io__dart-dcpsec.md) = `0x10000000000` |
| `vm-size-43` | 1 | u64 | [`/arm-io/dart-sbr`](../devicetree/root__arm-io__dart-sbr.md) = `0xffff0000` |
| `voiceTriggerChannels` | 1 | u32 | [`/product/audio`](../devicetree/root__product__audio.md) = `0x5` |
| `vol.fs_ephemeral` | 3 | empty×3 | [`/filesystems/fstab-ephemeral-recovery-data/ephemeral-recovery-data-vol`](../devicetree/root__filesystems__fstab-ephemeral-recovery-data__ephemeral-recovery-data-vol.md) = ``<br>[`/filesystems/fstab-ephemeral-diag-data/ephemeral-diag-data-vol`](../devicetree/root__filesystems__fstab-ephemeral-diag-data__ephemeral-diag-data-vol.md) = ``<br>[`/filesystems/fstab-ephemeral-devrecov-data/ephemeral-diag-data-vol`](../devicetree/root__filesystems__fstab-ephemeral-devrecov-data__ephemeral-diag-data-vol.md) = `` |
| `vol.fs_file` | 19 | string×19 | [`/filesystems/fstab/xart-vol`](../devicetree/root__filesystems__fstab__xart-vol.md) = `/private/xarts`<br>[`/filesystems/fstab/system-vol`](../devicetree/root__filesystems__fstab__system-vol.md) = `/`<br>[`/filesystems/fstab/preboot-vol`](../devicetree/root__filesystems__fstab__preboot-vol.md) = `/private/preboot`<br>[`/filesystems/fstab/data-vol`](../devicetree/root__filesystems__fstab__data-vol.md) = `/private/var`<br>[`/filesystems/fstab/baseband-vol`](../devicetree/root__filesystems__fstab__baseband-vol.md) = `/private/var/wireless/baseband_data` |
| `vol.fs_mntopts` | 19 | string×18, empty | [`/filesystems/fstab/xart-vol`](../devicetree/root__filesystems__fstab__xart-vol.md) = `nosuid,nodev,nobrowse`<br>[`/filesystems/fstab/system-vol`](../devicetree/root__filesystems__fstab__system-vol.md) = ``<br>[`/filesystems/fstab/preboot-vol`](../devicetree/root__filesystems__fstab__preboot-vol.md) = `nosuid,nodev,nobrowse`<br>[`/filesystems/fstab/data-vol`](../devicetree/root__filesystems__fstab__data-vol.md) = `nosuid,nodev`<br>[`/filesystems/fstab/baseband-vol`](../devicetree/root__filesystems__fstab__baseband-vol.md) = `nosuid,nodev,nobrowse` |
| `vol.fs_mntorder` | 19 | u32×19 | [`/filesystems/fstab/xart-vol`](../devicetree/root__filesystems__fstab__xart-vol.md) = `0x2`<br>[`/filesystems/fstab/system-vol`](../devicetree/root__filesystems__fstab__system-vol.md) = `0x0`<br>[`/filesystems/fstab/preboot-vol`](../devicetree/root__filesystems__fstab__preboot-vol.md) = `0x1`<br>[`/filesystems/fstab/data-vol`](../devicetree/root__filesystems__fstab__data-vol.md) = `0x3`<br>[`/filesystems/fstab/baseband-vol`](../devicetree/root__filesystems__fstab__baseband-vol.md) = `0x4` |
| `vol.fs_name` | 19 | string×19 | [`/filesystems/fstab/xart-vol`](../devicetree/root__filesystems__fstab__xart-vol.md) = `xART`<br>[`/filesystems/fstab/system-vol`](../devicetree/root__filesystems__fstab__system-vol.md) = `System`<br>[`/filesystems/fstab/preboot-vol`](../devicetree/root__filesystems__fstab__preboot-vol.md) = `Preboot`<br>[`/filesystems/fstab/data-vol`](../devicetree/root__filesystems__fstab__data-vol.md) = `Data`<br>[`/filesystems/fstab/baseband-vol`](../devicetree/root__filesystems__fstab__baseband-vol.md) = `Baseband-Data` |
| `vol.fs_passno` | 19 | u32×19 | [`/filesystems/fstab/xart-vol`](../devicetree/root__filesystems__fstab__xart-vol.md) = `0x1`<br>[`/filesystems/fstab/system-vol`](../devicetree/root__filesystems__fstab__system-vol.md) = `0x1`<br>[`/filesystems/fstab/preboot-vol`](../devicetree/root__filesystems__fstab__preboot-vol.md) = `0x1`<br>[`/filesystems/fstab/data-vol`](../devicetree/root__filesystems__fstab__data-vol.md) = `0x2`<br>[`/filesystems/fstab/baseband-vol`](../devicetree/root__filesystems__fstab__baseband-vol.md) = `0x2` |
| `vol.fs_role` | 16 | u32×16 | [`/filesystems/fstab/xart-vol`](../devicetree/root__filesystems__fstab__xart-vol.md) = `0x100`<br>[`/filesystems/fstab/system-vol`](../devicetree/root__filesystems__fstab__system-vol.md) = `0x1`<br>[`/filesystems/fstab/preboot-vol`](../devicetree/root__filesystems__fstab__preboot-vol.md) = `0x10`<br>[`/filesystems/fstab/data-vol`](../devicetree/root__filesystems__fstab__data-vol.md) = `0x40`<br>[`/filesystems/fstab/baseband-vol`](../devicetree/root__filesystems__fstab__baseband-vol.md) = `0x80` |
| `vol.fs_type` | 19 | string×19 | [`/filesystems/fstab/xart-vol`](../devicetree/root__filesystems__fstab__xart-vol.md) = `rw`<br>[`/filesystems/fstab/system-vol`](../devicetree/root__filesystems__fstab__system-vol.md) = `ro`<br>[`/filesystems/fstab/preboot-vol`](../devicetree/root__filesystems__fstab__preboot-vol.md) = `ro`<br>[`/filesystems/fstab/data-vol`](../devicetree/root__filesystems__fstab__data-vol.md) = `rw`<br>[`/filesystems/fstab/baseband-vol`](../devicetree/root__filesystems__fstab__baseband-vol.md) = `rw` |
| `volman-err-check` | 1 | u32 | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0x1` |
| `volman-status-offset` | 1 | u32 | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0x4c` |
| `volman-sw-err-check` | 1 | u32 | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `0x1` |
| `volume-down-button-location` | 3 | 24 B×3 | [`/product`](../devicetree/root__product.md) = `74c60b00d2211100e6ce040000a90100…`<br>[`/product/display0`](../devicetree/root__product__display0.md) = `74c60b00d2211100e6ce040000a90100…`<br>[`/product/display1`](../devicetree/root__product__display1.md) = `8409180034e8100012b2040000a90100…` |
| `volume-up-button-location` | 3 | 24 B×3 | [`/product`](../devicetree/root__product.md) = `74c60b00d22111003ec4020000a90100…`<br>[`/product/display0`](../devicetree/root__product__display0.md) = `74c60b00d22111003ec4020000a90100…`<br>[`/product/display1`](../devicetree/root__product__display1.md) = `8409180034e810006aa7020000a90100…` |
| `voter-agent` | 1 | 96 B | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `010f000180020000504d500000000000…` |
| `voter-rail-data` | 1 | 96 B | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) = `00000100010000004443530000000000…` |
| `wake-events` | 4 | u32×2, empty×2 | [`/arm-io/aop-gpio`](../devicetree/root__arm-io__aop-gpio.md) = `0x1006`<br>[`/arm-io/nub-gpio`](../devicetree/root__arm-io__nub-gpio.md) = `0xf06`<br>[`/arm-io/smc-gpio`](../devicetree/root__arm-io__smc-gpio.md) = ``<br>[`/arm-io/mtp-gpio`](../devicetree/root__arm-io__mtp-gpio.md) = `` |
| `wake-no-interrupt-group` | 4 | u32×4 | [`/arm-io/aop-gpio`](../devicetree/root__arm-io__aop-gpio.md) = `0x4`<br>[`/arm-io/nub-gpio`](../devicetree/root__arm-io__nub-gpio.md) = `0x4`<br>[`/arm-io/mtp-gpio`](../devicetree/root__arm-io__mtp-gpio.md) = `0x4`<br>[`/arm-io/secure-repair`](../devicetree/root__arm-io__secure-repair.md) = `0x4` |
| `wake-time-counter` | 1 | 48 B | [`/arm-io/soc-misc`](../devicetree/root__arm-io__soc-misc.md) = `00100000041000000400000008100000…` |
| `wakeup-data` | 3 | 12 B×3 | [`/arm-io/i2c3/mogul-display`](../devicetree/root__arm-io__i2c3__mogul-display.md) = `0000000080f0fa02b80b0000`<br>[`/arm-io/i2c3/mogul-display2`](../devicetree/root__arm-io__i2c3__mogul-display2.md) = `0000000080f0fa02b80b0000`<br>[`/arm-io/i2c4/mogul-mlb`](../devicetree/root__arm-io__i2c4__mogul-mlb.md) = `0000000080f0fa02b80b0000` |
| `wakeup-device` | 2 | string×2 | [`/arm-io/i2c3`](../devicetree/root__arm-io__i2c3.md) = `mogul-display, mogul-display2`<br>[`/arm-io/i2c4`](../devicetree/root__arm-io__i2c4.md) = `mogul-mlb` |
| `watch-companion` | 1 | u32 | [`/product`](../devicetree/root__product.md) = `0x1` |
| `watchdog-enable` | 7 | empty×7 | [`/arm-io/aop/iop-aop-nub`](../devicetree/root__arm-io__aop__iop-aop-nub.md) = ``<br>[`/arm-io/aop2/iop-aop2-nub`](../devicetree/root__arm-io__aop2__iop-aop2-nub.md) = ``<br>[`/arm-io/smc/iop-smc-nub`](../devicetree/root__arm-io__smc__iop-smc-nub.md) = ``<br>[`/arm-io/mtp/iop-mtp-nub`](../devicetree/root__arm-io__mtp__iop-mtp-nub.md) = ``<br>[`/arm-io/dcp/iop-dcp-nub`](../devicetree/root__arm-io__dcp__iop-dcp-nub.md) = `` |
| `wdt-version` | 1 | u32 | [`/arm-io/wdt`](../devicetree/root__arm-io__wdt.md) = `0x2` |
| `weight-factor-model-Px` | 1 | u32 | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) = `0x2ac0` |
| `wifi-antenna-sku-info` | 1 | string | [`/centauri`](../devicetree/root__centauri.md) = `syscfg/WSKU` |
| `wifi-chipset` | 1 | string | [`/product`](../devicetree/root__product.md) = `proxima` |
| `wifi-rfem-info` | 1 | string | [`/centauri`](../devicetree/root__centauri.md) = `syscfg/RFEM` |
| `wireless-splitter` | 1 | u32 | [`/product/audio`](../devicetree/root__product__audio.md) = `0x1` |
| `workload-priority` | 1 | u32 | [`/arm-io/scaler0`](../devicetree/root__arm-io__scaler0.md) = `0x5` |
| `zerofill-buffer-size-ms` | 2 | u32×2 | [`/arm-io/iop-audio-controller/audio-haptic`](../devicetree/root__arm-io__iop-audio-controller__audio-haptic.md) = `0x5`<br>[`/arm-io/iop-audio-controller/audio-hpdbg`](../devicetree/root__arm-io__iop-audio-controller__audio-hpdbg.md) = `0x5` |
