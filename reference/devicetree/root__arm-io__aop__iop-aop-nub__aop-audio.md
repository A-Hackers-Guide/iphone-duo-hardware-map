# `/arm-io/aop/iop-aop-nub/aop-audio`

- Name: `aop-audio`
- Parent: [`/arm-io/aop/iop-aop-nub`](root__arm-io__aop__iop-aop-nub.md)
- phandle: `97`
- compatible: `iop-audio,aop-service`
- device_type: `aop-audio`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AOPAudioService` | `AppleSPUAppInterface` | [`com.apple.driver.AOPAudio2`](../kexts/com.apple.driver.AOPAudio2.md) | `iop-audio,aop-service` |
| `AOPAudioService` | `AppleSPUAppInterface` | [`com.apple.driver.AOPAudio2`](../kexts/com.apple.driver.AOPAudio2.md) | `aop-audio` |
| `AppleAOPAudioController` | `AppleSPUAppInterface` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) | `aop-audio` |

## Firmware with a matching name [FW]

- [`Firmware/AOP/aopfw-v68aop.RELEASE.im4p`](../firmware/Firmware__AOP__aopfw-v68aop.RELEASE.im4p.md) (5,546,009 B) Tag: IM4P  Type: aopf  Version: 1
- [`Firmware/AOP2/aop2fw-v68aop2.RELEASE.im4p`](../firmware/Firmware__AOP2__aop2fw-v68aop2.RELEASE.im4p.md) (9,650,201 B) Tag: IM4P  Type: aop2  Version: 1

## All properties (4) [DT]

- **`AAPL,phandle`**: `97` (`0x61`) → phandle of [`/arm-io/aop/iop-aop-nub/aop-audio`](root__arm-io__aop__iop-aop-nub__aop-audio.md)
- **`compatible`**: `iop-audio,aop-service`
- **`device_type`**: `aop-audio`
- **`name`**: `aop-audio`
