# `IODARTMapper`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.IODARTFamily`](../kexts/com.apple.driver.IODARTFamily.md)
- Object size: `0xa78` (2,680 bytes)
- Metaclass: `0xfffffe000b9f3630`; metaclass vtable `0xfffffe000835cfb0`; class vtable `0xfffffe000835ca28`
- Registration (init): `0xfffffe000a0994f4`
- Superclasses: [`IOMapper`](IOMapper.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `IODARTMapper` in [`com.apple.driver.IODARTFamily`](../kexts/com.apple.driver.IODARTFamily.md): `IOProviderClass` = `IODARTMapperNub`, `IONameMatch` = `iommu-mapper`

## Device-tree nodes it binds (76) [DT]

- [`/arm-io/dart-sep/mapper-sep`](../devicetree/root__arm-io__dart-sep__mapper-sep.md) on `iommu-mapper`
- [`/arm-io/dart-sep/mapper-sep-exclave`](../devicetree/root__arm-io__dart-sep__mapper-sep-exclave.md) on `iommu-mapper`
- [`/arm-io/dart-sio/mapper-sio`](../devicetree/root__arm-io__dart-sio__mapper-sio.md) on `iommu-mapper`
- [`/arm-io/dart-sio/mapper-aes`](../devicetree/root__arm-io__dart-sio__mapper-aes.md) on `iommu-mapper`
- [`/arm-io/dart-sbr/mapper-aop`](../devicetree/root__arm-io__dart-sbr__mapper-aop.md) on `iommu-mapper`
- [`/arm-io/dart-sbr/mapper-aop2`](../devicetree/root__arm-io__dart-sbr__mapper-aop2.md) on `iommu-mapper`
- [`/arm-io/dart-sbr/mapper-exclave-aop`](../devicetree/root__arm-io__dart-sbr__mapper-exclave-aop.md) on `iommu-mapper`
- [`/arm-io/dart-sbr/mapper-exclave-aop2`](../devicetree/root__arm-io__dart-sbr__mapper-exclave-aop2.md) on `iommu-mapper`
- [`/arm-io/dart-sbr/mapper-mtp`](../devicetree/root__arm-io__dart-sbr__mapper-mtp.md) on `iommu-mapper`
- [`/arm-io/dart-sbr/mapper-pmp`](../devicetree/root__arm-io__dart-sbr__mapper-pmp.md) on `iommu-mapper`
- [`/arm-io/dart-sbr/mapper-admac-leap-ns`](../devicetree/root__arm-io__dart-sbr__mapper-admac-leap-ns.md) on `iommu-mapper`
- [`/arm-io/dart-sbr/mapper-admac-base-ns`](../devicetree/root__arm-io__dart-sbr__mapper-admac-base-ns.md) on `iommu-mapper`
- [`/arm-io/dart-sbr/mapper-admac-leap-s`](../devicetree/root__arm-io__dart-sbr__mapper-admac-leap-s.md) on `iommu-mapper`
- [`/arm-io/dart-sbr/mapper-admac-base-s`](../devicetree/root__arm-io__dart-sbr__mapper-admac-base-s.md) on `iommu-mapper`
- [`/arm-io/dart-sbr/mapper-scm`](../devicetree/root__arm-io__dart-sbr__mapper-scm.md) on `iommu-mapper`
- [`/arm-io/dart-sbr/mapper-rsm`](../devicetree/root__arm-io__dart-sbr__mapper-rsm.md) on `iommu-mapper`
- [`/arm-io/dart-usb0/mapper-usb`](../devicetree/root__arm-io__dart-usb0__mapper-usb.md) on `iommu-mapper`
- [`/arm-io/dart-dcp/mapper-dcp`](../devicetree/root__arm-io__dart-dcp__mapper-dcp.md) on `iommu-mapper`
- [`/arm-io/dart-dcp/mapper-dcp-exclave`](../devicetree/root__arm-io__dart-dcp__mapper-dcp-exclave.md) on `iommu-mapper`
- [`/arm-io/dart-disp0/mapper-disp0`](../devicetree/root__arm-io__dart-disp0__mapper-disp0.md) on `iommu-mapper`
- [`/arm-io/dart-disp0/mapper-disp0-piodma`](../devicetree/root__arm-io__dart-disp0__mapper-disp0-piodma.md) on `iommu-mapper`
- [`/arm-io/dart-disp0/mapper-disp0-scl`](../devicetree/root__arm-io__dart-disp0__mapper-disp0-scl.md) on `iommu-mapper`
- [`/arm-io/dart-disp0/mapper-disp0-sca`](../devicetree/root__arm-io__dart-disp0__mapper-disp0-sca.md) on `iommu-mapper`
- [`/arm-io/dart-dispgrt/mapper-dispgrt`](../devicetree/root__arm-io__dart-dispgrt__mapper-dispgrt.md) on `iommu-mapper`
- [`/arm-io/dart-disp0-isoc/mapper-disp0-dpa`](../devicetree/root__arm-io__dart-disp0-isoc__mapper-disp0-dpa.md) on `iommu-mapper`
- [`/arm-io/dart-dcpsec/mapper-dcpsec`](../devicetree/root__arm-io__dart-dcpsec__mapper-dcpsec.md) on `iommu-mapper`
- [`/arm-io/dart-dcpsec/mapper-dcpsec-exclave`](../devicetree/root__arm-io__dart-dcpsec__mapper-dcpsec-exclave.md) on `iommu-mapper`
- [`/arm-io/dart-dispsec/mapper-dispsec`](../devicetree/root__arm-io__dart-dispsec__mapper-dispsec.md) on `iommu-mapper`
- [`/arm-io/dart-dispsec/mapper-dispsec-piodma`](../devicetree/root__arm-io__dart-dispsec__mapper-dispsec-piodma.md) on `iommu-mapper`
- [`/arm-io/dart-dispsec/mapper-dispsec-scl`](../devicetree/root__arm-io__dart-dispsec__mapper-dispsec-scl.md) on `iommu-mapper`
- [`/arm-io/dart-dispsec/mapper-dispsec-sca`](../devicetree/root__arm-io__dart-dispsec__mapper-dispsec-sca.md) on `iommu-mapper`
- [`/arm-io/dart-dispsecgrt/mapper-dispsecgrt`](../devicetree/root__arm-io__dart-dispsecgrt__mapper-dispsecgrt.md) on `iommu-mapper`
- [`/arm-io/dart-dcpext0/mapper-dcpext0`](../devicetree/root__arm-io__dart-dcpext0__mapper-dcpext0.md) on `iommu-mapper`
- [`/arm-io/dart-dcpext0/mapper-dcpext0-exclave`](../devicetree/root__arm-io__dart-dcpext0__mapper-dcpext0-exclave.md) on `iommu-mapper`
- [`/arm-io/dart-dispext0/mapper-dispext0`](../devicetree/root__arm-io__dart-dispext0__mapper-dispext0.md) on `iommu-mapper`
- [`/arm-io/dart-dispext0/mapper-dispext0-piodma`](../devicetree/root__arm-io__dart-dispext0__mapper-dispext0-piodma.md) on `iommu-mapper`
- [`/arm-io/dart-dispext0-isoc/mapper-dispext0-dpa`](../devicetree/root__arm-io__dart-dispext0-isoc__mapper-dispext0-dpa.md) on `iommu-mapper`
- [`/arm-io/dart-scaler/mapper-scaler`](../devicetree/root__arm-io__dart-scaler__mapper-scaler.md) on `iommu-mapper`
- [`/arm-io/dart-scaler/mapper-scaler-piodma`](../devicetree/root__arm-io__dart-scaler__mapper-scaler-piodma.md) on `iommu-mapper`
- [`/arm-io/dart-jpeg/mapper-jpeg`](../devicetree/root__arm-io__dart-jpeg__mapper-jpeg.md) on `iommu-mapper`
- [`/arm-io/dart-isp/mapper-isp`](../devicetree/root__arm-io__dart-isp__mapper-isp.md) on `iommu-mapper`
- [`/arm-io/dart-isp/mapper-isp-mpm`](../devicetree/root__arm-io__dart-isp__mapper-isp-mpm.md) on `iommu-mapper`
- [`/arm-io/dart-isp/mapper-isp-epipe0-exclave`](../devicetree/root__arm-io__dart-isp__mapper-isp-epipe0-exclave.md) on `iommu-mapper`
- [`/arm-io/dart-isp/mapper-isp-epipe1-exclave`](../devicetree/root__arm-io__dart-isp__mapper-isp-epipe1-exclave.md) on `iommu-mapper`
- [`/arm-io/dart-isp/mapper-isp-piodma1-exclave`](../devicetree/root__arm-io__dart-isp__mapper-isp-piodma1-exclave.md) on `iommu-mapper`
- [`/arm-io/dart-isp/mapper-isp-exclave-secure1`](../devicetree/root__arm-io__dart-isp__mapper-isp-exclave-secure1.md) on `iommu-mapper`
- [`/arm-io/dart-ave/mapper-ave`](../devicetree/root__arm-io__dart-ave__mapper-ave.md) on `iommu-mapper`
- [`/arm-io/dart-avd/mapper-avd`](../devicetree/root__arm-io__dart-avd__mapper-avd.md) on `iommu-mapper`
- [`/arm-io/dart-avd/mapper-avd-piodma`](../devicetree/root__arm-io__dart-avd__mapper-avd-piodma.md) on `iommu-mapper`
- [`/arm-io/dart-avd/mapper-avd-adsbuf`](../devicetree/root__arm-io__dart-avd__mapper-avd-adsbuf.md) on `iommu-mapper`
- [`/arm-io/dart-ane0/mapper-ane0`](../devicetree/root__arm-io__dart-ane0__mapper-ane0.md) on `iommu-mapper`
- [`/arm-io/dart-ane0/mapper-ane0-iso1`](../devicetree/root__arm-io__dart-ane0__mapper-ane0-iso1.md) on `iommu-mapper`
- [`/arm-io/dart-ane0/mapper-ane0-iso2`](../devicetree/root__arm-io__dart-ane0__mapper-ane0-iso2.md) on `iommu-mapper`
- [`/arm-io/dart-ane0/mapper-ane0-iso3`](../devicetree/root__arm-io__dart-ane0__mapper-ane0-iso3.md) on `iommu-mapper`
- [`/arm-io/dart-ane0/mapper-ane0-iso4`](../devicetree/root__arm-io__dart-ane0__mapper-ane0-iso4.md) on `iommu-mapper`
- [`/arm-io/dart-ane0/mapper-ane0-iso5`](../devicetree/root__arm-io__dart-ane0__mapper-ane0-iso5.md) on `iommu-mapper`
- [`/arm-io/dart-ane0/mapper-ane0-iso6`](../devicetree/root__arm-io__dart-ane0__mapper-ane0-iso6.md) on `iommu-mapper`
- [`/arm-io/dart-ane0/mapper-ane0-iso7`](../devicetree/root__arm-io__dart-ane0__mapper-ane0-iso7.md) on `iommu-mapper`
- [`/arm-io/dart-ane0/mapper-ane0-mpm`](../devicetree/root__arm-io__dart-ane0__mapper-ane0-mpm.md) on `iommu-mapper`
- [`/arm-io/dart-ane1/mapper-ane1`](../devicetree/root__arm-io__dart-ane1__mapper-ane1.md) on `iommu-mapper`
- [`/arm-io/dart-ane1/mapper-ane1-iso1`](../devicetree/root__arm-io__dart-ane1__mapper-ane1-iso1.md) on `iommu-mapper`
- [`/arm-io/dart-ane1/mapper-ane1-iso2`](../devicetree/root__arm-io__dart-ane1__mapper-ane1-iso2.md) on `iommu-mapper`
- [`/arm-io/dart-ane1/mapper-ane1-iso3`](../devicetree/root__arm-io__dart-ane1__mapper-ane1-iso3.md) on `iommu-mapper`
- [`/arm-io/dart-ane1/mapper-ane1-iso4`](../devicetree/root__arm-io__dart-ane1__mapper-ane1-iso4.md) on `iommu-mapper`
- [`/arm-io/dart-ane1/mapper-ane1-iso5`](../devicetree/root__arm-io__dart-ane1__mapper-ane1-iso5.md) on `iommu-mapper`
- [`/arm-io/dart-ane1/mapper-ane1-iso6`](../devicetree/root__arm-io__dart-ane1__mapper-ane1-iso6.md) on `iommu-mapper`
- [`/arm-io/dart-ane1/mapper-ane1-iso7`](../devicetree/root__arm-io__dart-ane1__mapper-ane1-iso7.md) on `iommu-mapper`
- [`/arm-io/dart-ane1/mapper-ane1-mpm`](../devicetree/root__arm-io__dart-ane1__mapper-ane1-mpm.md) on `iommu-mapper`
- [`/arm-io/dart-apcie0/mapper-apcie0-control`](../devicetree/root__arm-io__dart-apcie0__mapper-apcie0-control.md) on `iommu-mapper`
- [`/arm-io/dart-apcie0/mapper-apcie0-alpha`](../devicetree/root__arm-io__dart-apcie0__mapper-apcie0-alpha.md) on `iommu-mapper`
- [`/arm-io/dart-apcie0/mapper-apcie0-beta`](../devicetree/root__arm-io__dart-apcie0__mapper-apcie0-beta.md) on `iommu-mapper`
- [`/arm-io/dart-apcie0/mapper-apcie0-piodma`](../devicetree/root__arm-io__dart-apcie0__mapper-apcie0-piodma.md) on `iommu-mapper`
- [`/arm-io/dart-apcie0/mapper-apcie0-plce`](../devicetree/root__arm-io__dart-apcie0__mapper-apcie0-plce.md) on `iommu-mapper`
- [`/arm-io/dart-apcie1/mapper-apcie1`](../devicetree/root__arm-io__dart-apcie1__mapper-apcie1.md) on `iommu-mapper`
- [`/arm-io/dart-apcie1/mapper-apcie1-piodma`](../devicetree/root__arm-io__dart-apcie1__mapper-apcie1-piodma.md) on `iommu-mapper`
- [`/arm-io/dart-apcie1/mapper-apcie1-plce`](../devicetree/root__arm-io__dart-apcie1__mapper-apcie1-plce.md) on `iommu-mapper`

## Strings in its kext that name it (11)

- `IODARTMapper`
- `/IODARTMapper.cpp`
- `site.IODARTMapper`
- `site.IODARTMapper::pioRange_t`
- `IODARTMapperClient`
- `/IODARTMapperClient.cpp`
- `site.IODARTMapperNub`
- `IODARTMapper.cpp`
- `site.IODARTMapperClient`
- `IODARTMapperNub`
- `NewIODARTMapper`
