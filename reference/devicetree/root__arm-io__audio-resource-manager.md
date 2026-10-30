# `/arm-io/audio-resource-manager`

- Name: `audio-resource-manager`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `442`
- compatible: `audio,embedded-resource-manager`
- device_type: `audio-resource-manager`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleEmbeddedAudioResourceManager` | `AppleARMIODevice` | [`com.apple.driver.AppleEmbeddedAudioResourceManager`](../kexts/com.apple.driver.AppleEmbeddedAudioResourceManager.md) | `audio,embedded-resource-manager` |

## All properties (6) [DT]

- **`AAPL,phandle`**: `442` (`0x1ba`) → phandle of [`/arm-io/audio-resource-manager`](root__arm-io__audio-resource-manager.md)
- **`compatible`**: `audio,embedded-resource-manager`
- **`device_type`**: `audio-resource-manager`
- **`kci-name`**: `AudioResourceManagerInterface`
- **`name`**: `audio-resource-manager`
- **`resource-gid-mapping`**: 43 bytes
  - text inside: ` MCPAOPAudioHWPCMAssetManagerInterface`
  ```
  000000  00 00 01 00 20 4d 43 50 41 4f 50 41 75 64 69 6f  .... MCPAOPAudio
  000010  48 57 50 43 4d 41 73 73 65 74 4d 61 6e 61 67 65  HWPCMAssetManage
  000020  72 49 6e 74 65 72 66 61 63 65 00                 rInterface.
  ```
