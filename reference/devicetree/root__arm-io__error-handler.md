# `/arm-io/error-handler`

- Name: `error-handler`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `55`
- compatible: `error-handler,t8160`
- device_type: `error-handler`
- Children (16): [`/arm-io/error-handler/amcc-error-handler`](root__arm-io__error-handler__amcc-error-handler.md), [`/arm-io/error-handler/dcs-error-handler`](root__arm-io__error-handler__dcs-error-handler.md), [`/arm-io/error-handler/pmgr-error-handler`](root__arm-io__error-handler__pmgr-error-handler.md), [`/arm-io/error-handler/cllt-error-handler`](root__arm-io__error-handler__cllt-error-handler.md), [`/arm-io/error-handler/sep-error-handler`](root__arm-io__error-handler__sep-error-handler.md), [`/arm-io/error-handler/ni0-error-handler`](root__arm-io__error-handler__ni0-error-handler.md), [`/arm-io/error-handler/ni1-error-handler`](root__arm-io__error-handler__ni1-error-handler.md), [`/arm-io/error-handler/ni2-error-handler`](root__arm-io__error-handler__ni2-error-handler.md), [`/arm-io/error-handler/ni3-error-handler`](root__arm-io__error-handler__ni3-error-handler.md), [`/arm-io/error-handler/ni4-error-handler`](root__arm-io__error-handler__ni4-error-handler.md), [`/arm-io/error-handler/nsi-error-handler`](root__arm-io__error-handler__nsi-error-handler.md), [`/arm-io/error-handler/pio-error-handler`](root__arm-io__error-handler__pio-error-handler.md), [`/arm-io/error-handler/psd-error-handler`](root__arm-io__error-handler__psd-error-handler.md), [`/arm-io/error-handler/gpce-error-handler`](root__arm-io__error-handler__gpce-error-handler.md), [`/arm-io/error-handler/ipce-error-handler`](root__arm-io__error-handler__ipce-error-handler.md), [`/arm-io/error-handler/sac-error-handler`](root__arm-io__error-handler__sac-error-handler.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleSoCErrorHandler` | `AppleARMIODevice` | [`com.apple.driver.AppleT8160`](../kexts/com.apple.driver.AppleT8160.md) | `error-handler,t8160` |

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `amcc-sram-eventhandler` | [`/arm-io/mcc`](root__arm-io__mcc.md) | `M$DS` | `` |

## All properties (6) [DT]

- **`AAPL,phandle`**: `55` (`0x37`) → phandle of [`/arm-io/error-handler`](root__arm-io__error-handler.md)
- **`compatible`**: `error-handler,t8160`
- **`device_type`**: `error-handler`
- **`function-amcc-sram-eventhandler`**: `0x4d24445300000036` (u64; as two u32: `0x36`, `0x4d244453`)
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`name`**: `error-handler`
