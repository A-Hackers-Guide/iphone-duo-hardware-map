# `/arm-io/isp-exclave-proxy`

- Name: `isp-exclave-proxy`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `307`
- compatible: `isp,isp-exclave-proxy`
- device_type: `isp`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleExclaveCameraProxy` | `AppleARMIODevice` | [`com.apple.driver.AppleCamera`](../kexts/com.apple.driver.AppleCamera.md) | `isp,isp-exclave-proxy` |

## Firmware with a matching name [FW]

- [`Firmware/isp_bni/adc-boreas-v68.im4p`](../firmware/Firmware__isp_bni__adc-boreas-v68.im4p.md) (29,851,675 B) Tag: IM4P  Type: ispf  Version: 1

## All properties (7) [DT]

- **`AAPL,phandle`**: `307` (`0x133`) → phandle of [`/arm-io/isp-exclave-proxy`](root__arm-io__isp-exclave-proxy.md)
- **`compatible`**: `isp,isp-exclave-proxy`
- **`device_type`**: `isp`
- **`exclave-assigned`**: (present, empty)
- **`exclave-edk-service`**: `com.apple.service.ISPEngine_EDK`
- **`exclave-service`**: `com.apple.service.ISPEngine`
- **`name`**: `isp-exclave-proxy`
