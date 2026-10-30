# `/product`

- Name: `product`
- Parent: [`/`](root.md)
- phandle: `469`
- Children (8): [`/product/display0`](root__product__display0.md), [`/product/display1`](root__product__display1.md), [`/product/iopm`](root__product__iopm.md), [`/product/camera`](root__product__camera.md), [`/product/facetime`](root__product__facetime.md), [`/product/maps`](root__product__maps.md), [`/product/haptics`](root__product__haptics.md), [`/product/audio`](root__product__audio.md)

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## All properties (104) [DT]

- **`AAPL,phandle`**: `469` (`0x1d5`) → phandle of [`/product`](root__product.md)
- **`RF-exposure-separation-distance`**: `5` (`0x5`)
- **`activation-protocol-version`**: `2` (`0x2`)
- **`alisha`**: `1` (`0x1`)
- **`allow-32bit-apps`**: `1` (`0x1`)
- **`app-macho-architecture`**: `arm64e.x1`
- **`artwork-device-idiom`**: `phone`
- **`artwork-device-subtype`**: `2034` (`0x7f2`)
- **`artwork-display-gamut`**: `P3`
- **`artwork-dynamic-displaymode`**: `0`
- **`artwork-scale-factor`**: `3` (`0x3`)
- **`assistant`**: `1` (`0x1`)
- **`baseband-chipset`**: `int2`
- **`bluetooth-le`**: `1` (`0x1`)
- **`bluetooth-lea2`**: `1` (`0x1`)
- **`bmu-board-id`**: `33171` (`0x8193`)
- **`bmu-chip-id`**: `58629` (`0xe505`)
- **`bmu-num-enabled`**: `2` (`0x2`)
- **`bmu-num-supported`**: `3` (`0x3`)
- **`bmu2-board-id`**: `33171` (`0x8193`)
- **`bmu2-chip-id`**: `58629` (`0xe505`)
- **`builtin-mics`**: `4` (`0x4`)
- **`camera-button-location`**: 24 bytes
  - u32: `0xbc674 0x1121d2 0xb4069 0x29bd0 0x2710 0x1`
  ```
  000000  74 c6 0b 00 d2 21 11 00 69 40 0b 00 d0 9b 02 00  t....!..i@......
  000010  10 27 00 00 01 00 00 00                          .'......
  ```
- **`car-integration`**: `1` (`0x1`)
- **`carplay-2`**: `1` (`0x1`)
- **`chrome-identifier`**: `com.apple.dt.devicekit.chrome.phone15`
- **`collision-sos`**: (present, empty)
- **`compatible-app-variant`**: `0`
- **`compatible-device-fallback`**: `iPhone18,3`
- **`device-color-policy`**: `0` (`0x0`)
- **`device-perf-memory-class`**: `12` (`0xc`)
- **`dictation`**: `1` (`0x1`)
- **`display-backlight-compensation`**: `syscfg/DBCl` *(placeholder, filled in by iBoot at boot)*
- **`display-corner-radius`**: `0x10000003b` (u64; as two u32: `0x3b`, `0x1`)
- **`display-mirroring`**: `1` (`0x1`)
- **`display-temp-compensation`**: `syscfg/DTCl` *(placeholder, filled in by iBoot at boot)*
- **`display-workgroup-interval`**: `1` (`0x1`)
- **`ephemeral-data-mode`**: `0` (`0x0`)
- **`exclaves-enabled`**: `1` (`0x1`)
- **`external-hdr`**: (present, empty)
- **`fdr-product-type`**: `iPhone19,4`
- **`find-my`**: `1` (`0x1`)
- **`framebuffer-identifier`**: `1C896A2B-F0D7-405C-8D0F-66E4B80AD044`
- **`front-cam-offset-from-center`**: 20 bytes
  - u32: `0x105c5 0x1cad 0x1575 0x3e8 0x0`
  ```
  000000  c5 05 01 00 ad 1c 00 00 75 15 00 00 e8 03 00 00  ........u.......
  000010  00 00 00 00                                      ....
  ```
- **`front-cam-rotation-isp`**: `180` (`0xb4`)
- **`gps-capable`**: `1` (`0x1`)
- **`graphics-featureset-class`**: `APPLE11`
- **`graphics-featureset-fallbacks`**: `APPLE10:APPLE9:APPLE8:APPLE7:APPLE6:APPLE5:APPLE4:APPLE3:APPLE3v1:APPLE2:APPLE1:GLES2,0`
- **`has-applelpm`**: `1` (`0x1`)
- **`has-boot-chime`**: `1` (`0x1`)
- **`has-exclaves`**: `1` (`0x1`)
- **`hearingaid-audio-equalization`**: `1` (`0x1`)
- **`hearingaid-low-energy-audio`**: `1` (`0x1`)
- **`hid-workgroup-interval`**: `1` (`0x1`)
- **`high-bandwidth-radio`**: `1` (`0x1`)
- **`hme-in-arkit`**: `1` (`0x1`)
- **`hme-refresh-rate`**: `85` (`0x55`)
- **`iap2-protocol-supported`**: `1` (`0x1`)
- **`island-notch-location`**: `144` (`0x90`)
- **`itunes-min-ver`**: `721408` (`0xb0200`)
- **`large-format-phone`**: `1` (`0x1`)
- **`location-reminders`**: `1` (`0x1`)
- **`lockdown-certtype`**: `1` (`0x1`)
- **`low-power-express`**: `1` (`0x1`)
- **`low-power-wallet-mode`**: `1` (`0x1`)
- **`mobiledevice-min-ver`**: `1853`
- **`name`**: `product`
- **`nfc-express`**: `1` (`0x1`)
- **`offline-dictation`**: `1` (`0x1`)
- **`oled-display`**: `1` (`0x1`)
- **`partition-style`**: `iOS`
- **`personal-hotspot`**: `1` (`0x1`)
- **`primary-calibration-matrix`**: `syscfg/DPCl` *(placeholder, filled in by iBoot at boot)*
- **`product-description`**: `iPhone Duo`
- **`product-id`**: 20 bytes
  - u32: `0x6cb9bab 0x24fb3d82 0x418bf4f5 0x1cc4a7b5 0xb562f10e`
  ```
  000000  ab 9b cb 06 82 3d fb 24 f5 f4 8b 41 b5 a7 c4 1c  .....=.$...A....
  000010  0e f1 62 b5                                      ..b.
  ```
- **`product-name`**: `iPhone Duo`
- **`ptp-large-files`**: `1` (`0x1`)
- **`public-key-accelerator`**: `1` (`0x1`)
- **`rear-cam-offset-from-center`**: 20 bytes
  - u32: `0xa1b7 0x5436 0xb5b 0x3e8 0x0`
  ```
  000000  b7 a1 00 00 36 54 00 00 5b 0b 00 00 e8 03 00 00  ....6T..[.......
  000010  00 00 00 00                                      ....
  ```
- **`sandman-support`**: `1` (`0x1`)
- **`side-button-location`**: 24 bytes
  - u32: `0xbc674 0x1121d2 0x4b51e 0x2d956 0x2710 0x1`
  ```
  000000  74 c6 0b 00 d2 21 11 00 1e b5 04 00 56 d9 02 00  t....!......V...
  000010  10 27 00 00 01 00 00 00                          .'......
  ```
- **`single-stage-boot`**: `1` (`0x1`)
- **`siri-gesture`**: `1` (`0x1`)
- **`sub-product-type`**: `iPhone19,4`
- **`supports-apple-pencil`**: `1` (`0x1`)
- **`supports-avatars`**: (present, empty)
- **`supports-burnin-mitigation`**: `1` (`0x1`)
- **`supports-camera-button`**: `1` (`0x1`)
- **`supports-gray-dimming`**: (present, empty)
- **`supports-lotx`**: `1` (`0x1`)
- **`supports-maps-optical-heading`**: (present, empty)
- **`supports-personal-translator`**: `1` (`0x1`)
- **`supports-recoveryos`**: `1` (`0x1`)
- **`thin-bezel`**: `1` (`0x1`)
- **`udid-version`**: `2` (`0x2`)
- **`ui-background-quality`**: `100` (`0x64`)
- **`ui-pip`**: `1` (`0x1`)
- **`ui-weather-quality`**: `100` (`0x64`)
- **`unique-model`**: `V68AP`
- **`usb-c-smc-pwr`**: (present, empty)
- **`volume-down-button-location`**: 24 bytes
  - u32: `0xbc674 0x1121d2 0x4cee6 0x1a900 0x2710 0x0`
  ```
  000000  74 c6 0b 00 d2 21 11 00 e6 ce 04 00 00 a9 01 00  t....!..........
  000010  10 27 00 00 00 00 00 00                          .'......
  ```
- **`volume-up-button-location`**: 24 bytes
  - u32: `0xbc674 0x1121d2 0x2c43e 0x1a900 0x2710 0x0`
  ```
  000000  74 c6 0b 00 d2 21 11 00 3e c4 02 00 00 a9 01 00  t....!..>.......
  000010  10 27 00 00 00 00 00 00                          .'......
  ```
- **`watch-companion`**: `1` (`0x1`)
- **`wifi-chipset`**: `proxima`
