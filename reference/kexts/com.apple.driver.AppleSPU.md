# `com.apple.driver.AppleSPU`

- Name: AppleSPU
- Version: `1`
- UUID: `CE7DAAE7-13AD-3292-BB7A-15A1D8614E7A`
- Source version: `1087.40.4.0.0`
- Depends on: [`com.apple.driver.AppleA7IOP`](com.apple.driver.AppleA7IOP.md) 1.0.0, [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleFirmwareUpdateKext`](com.apple.driver.AppleFirmwareUpdateKext.md) 1.0.0, [`com.apple.driver.IOSlaveProcessor`](com.apple.driver.IOSlaveProcessor.md) 1.0.0, [`com.apple.driver.RTBuddy`](com.apple.driver.RTBuddy.md) 1.0.0, [`com.apple.iokit.CoreAnalyticsFamily`](com.apple.iokit.CoreAnalyticsFamily.md) 1.0, [`com.apple.iokit.IOHIDFamily`](com.apple.iokit.IOHIDFamily.md) 2.0, [`com.apple.iokit.IOReportFamily`](com.apple.iokit.IOReportFamily.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 14.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 14.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 14.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 14.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 22.0

## Device-tree nodes it binds (9) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/aop/iop-aop-nub`](../devicetree/root__arm-io__aop__iop-aop-nub.md) | `AppleLVBOOST` | `iop-aop-nub` |
| [`/arm-io/aop/iop-aop-nub`](../devicetree/root__arm-io__aop__iop-aop-nub.md) | `AppleSPUTimesyncV2` | `iop-aop-nub` |
| [`/arm-io/aop/iop-aop-nub/SPUApp`](../devicetree/root__arm-io__aop__iop-aop-nub__SPUApp.md) | `AppleSPUAppDriver` | `SPUApp` |
| [`/arm-io/aop/iop-aop-nub/smc-control`](../devicetree/root__arm-io__aop__iop-aop-nub__smc-control.md) | `AppleAOPSMCDriver` | `smc-control` |
| [`/arm-io/aop/iop-aop-nub/gnss`](../devicetree/root__arm-io__aop__iop-aop-nub__gnss.md) | `AppleSPUGNSSDriver` | `gnss` |
| [`/arm-io/aop/iop-aop-nub/dcp-control`](../devicetree/root__arm-io__aop__iop-aop-nub__dcp-control.md) | `AppleSPUDCPDriver` | `dcp-control` |
| [`/arm-io/aop/iop-aop-nub/grimaldi-control`](../devicetree/root__arm-io__aop__iop-aop-nub__grimaldi-control.md) | `AppleSPUGrimaldiDriver` | `grimaldi-control` |
| [`/arm-io/aon-ptd`](../devicetree/root__arm-io__aon-ptd.md) | `AppleSPUAONPTDDriver` | `aon-ptd` |
| [`/arm-io/mtp/iop-mtp-nub/multi-touch`](../devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch.md) | `AppleSPUControl` | `multi-touch` |

## IOKit personalities (38) [KC]

###  AppleSPUFastpathDriver 
- `CFBundleIdentifier`: `com.apple.driver.AppleSPU`
- `IOCFPlugInTypes`:
  - `53EA6734-C70E-4635-9CF5-4FAF05B4F230`: `AppleSPU.kext/PlugIns/FastpathLib.plugin`
- `IOClass`: `AppleSPUFastpathDriver`
- `IOMatchCategory`: `AppleSPUFastpathDriver`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPU`
- `IOProviderClass`: `AppleSPUFastpathInterface`

### AppleAOPSMCDriver
- `CFBundleIdentifier`: `com.apple.driver.AppleSPU`
- `IOClass`: `AppleAOPSMCDriver`
- `IOKitDebug`: `65535`
- `IOMatchCategory`: `AppleAOPSMCDriver`
- `IONameMatch`:
  - `smc-control`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPU`
- `IOProviderClass`: `AppleSPUAppInterface`

### AppleLVBOOST
- `CFBundleIdentifier`: `com.apple.driver.AppleSPU`
- `IOClass`: `AppleLVBOOST`
- `IOMatchCategory`: `AppleLVBOOST`
- `IONameMatch`:
  - `iop-spu-nub`
  - `iop-aop-nub`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPU`
- `IOProviderClass`: `AppleA7IOPNub`

### AppleSPU
- `CFBundleIdentifier`: `com.apple.driver.AppleSPU`
- `IOClass`: `AppleSPU`
- `IONameMatch`:
  - `AOPEndpoint1`
  - `AOPEndpoint2`
  - `AOPEndpoint3`
  - `AOPEndpoint4`
  - `AOPEndpoint5`
  - `AOPEndpoint6`
  - `AOPEndpoint7`
  - `AOPEndpoint8`
  - `AOPEndpoint9`
  - `AOPEndpoint10`
  - `AOPEndpoint11`
  - `AOPEndpoint12`
  - `AOPEndpoint13`
  - `AOPEndpoint14`
  - `AOPEndpoint15`
  - `AOPEndpoint16`
  - `AOPEndpoint17`
  - `AOPEndpoint18`
  - `AOPEndpoint19`
  - `AOPEndpoint20`
  - `AOPEndpoint21`
  - `AOPEndpoint22`
  - `AOPEndpoint23`
  - `AOPEndpoint24`
  - `AOPEndpoint25`
  - `AOPEndpoint26`
  - `AOPEndpoint27`
  - `AOPEndpoint28`
  - `AOPEndpoint29`
  - `AOPEndpoint30`
  - `AOPEndpoint31`
  - `AOPEndpoint32`
  - `SPUEndpoint1`
  - `SPUEndpoint2`
  - `SPUEndpoint3`
  - `SPUEndpoint4`
  - `SPUEndpoint5`
  - `SPUEndpoint6`
  - `SPUEndpoint7`
  - `SPUEndpoint8`
  - `SPUEndpoint9`
  - `SPUEndpoint10`
  - `SPUEndpoint11`
  - `SPUEndpoint12`
  - `SPUEndpoint13`
  - `SPUEndpoint14`
  - `SPUEndpoint15`
  - `SPUEndpoint16`
  - `SPU2Endpoint1`
  - `SPU2Endpoint2`
  - `SPU2Endpoint3`
  - `SPU2Endpoint4`
  - `SPU2Endpoint5`
  - `SPU2Endpoint6`
  - `SPU2Endpoint7`
  - `SPU2Endpoint8`
  - `SPU2Endpoint9`
  - `SPU2Endpoint10`
  - `SPU2Endpoint11`
  - `SPU2Endpoint12`
  - `SPU2Endpoint13`
  - `SPU2Endpoint14`
  - `SPU2Endpoint15`
  - `SPU2Endpoint16`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPU`
- `IOProviderClass`: `RTBuddyEndpointService`
- `allowed-action-list`:
  - `AOP_log`:
    - `get-property`:
      - `208`: `True`
    - `perform-command`:
      - `35`: `True`
      - `36`: `True`
      - `37`: `True`
      - `38`: `True`
    - `set-property`:
      - `208`: `True`
  - `AOP_profile`:
    - `get-property`:
      - `208`: `True`
      - `209`: `True`
      - `210`: `True`
      - `211`: `True`
      - `212`: `True`
      - `213`: `True`
      - `214`: `True`
    - `perform-command`:
      - `32`: `True`
      - `33`: `True`
      - `34`: ``
      - `35`: `True`
      - `36`: `True`
      - `37`: `True`
      - `38`: `True`
    - `set-property`:
      - `210`: `True`
      - `213`: `True`
  - `SPUApp`:
    - `get-property`:
      - `20`: `True`
      - `210`: `True`
      - `213`: `True`
      - `214`: `True`
      - `215`: `True`
      - `216`: `True`
      - `218`: `True`
      - `220`: `True`
      - `223`: `True`
      - `224`: `True`
      - `225`: `True`
      - `43`: `True`
      - `69`: `True`
      - `71`: `True`
    - `perform-command`:
      - `0`: `True`
      - `10`: `True`
      - `121`: `True`
      - `32`: `True`
      - `33`: `True`
      - `34`: `True`
      - `35`: `True`
      - `36`: `True`
      - `37`: `True`
      - `38`: `True`
      - `39`: `True`
      - `4`: `True`
      - `40`: `True`
      - `41`: `True`
      - `42`: `True`
      - `44`: `True`
      - `45`: `True`
      - `46`: `True`
      - `47`: `True`
      - `48`: `True`
      - `53`: `True`
      - `54`: `True`
      - `55`: `True`
    - `set-property`:
      - `208`: `True`
      - `209`: `True`
      - `210`: `True`
      - `211`: `True`
      - `217`: `True`
      - `218`: `True`
      - `219`: `True`
      - `220`: `True`
      - `221`: `True`
      - `222`: `True`
      - `224`: `True`
      - `225`: `True`
      - `226`: `True`
      - `228`: `True`
      - `44`: `True`
      - `69`: `True`
      - `70`: `True`
      - `71`: `True`
      - `72`: `True`
  - `rose`:
    - `get-property`: `{}`
    - `perform-command`: `{}`
    - `set-property`: `{}`

### AppleSPUALSSealionAccessoryDriver
- `CFBundleIdentifier`: `com.apple.driver.AppleSPU`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `4`
    - `DeviceUsagePage`: `65280`
- `IOCFPlugInTypes`:
  - `3BC5CC87-845E-48AB-A9C2-9436001BA68A`: `AppleSPU.kext/PlugIns/AppleSPULib.plugin`
- `IOClass`: `AppleSPUALSSealionAccessoryDriver`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPU`
- `IOProviderClass`: `IOHIDInterface`
- `QueueSize`: `16384`
- `Transport`: `SPU`
- `manufacturer`: `Sealion-Accessory`

### AppleSPUALSSealionDriver
- `CFBundleIdentifier`: `com.apple.driver.AppleSPU`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `4`
    - `DeviceUsagePage`: `65280`
- `IOCFPlugInTypes`:
  - `3BC5CC87-845E-48AB-A9C2-9436001BA68A`: `AppleSPU.kext/PlugIns/AppleSPULib.plugin`
- `IOClass`: `AppleSPUALSSealionDriver`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPU`
- `IOProviderClass`: `IOHIDInterface`
- `QueueSize`: `16384`
- `Transport`: `SPU`
- `manufacturer`: `Sealion`

### AppleSPUALSSunfishDriver
- `CFBundleIdentifier`: `com.apple.driver.AppleSPU`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `4`
    - `DeviceUsagePage`: `65280`
- `IOCFPlugInTypes`:
  - `3BC5CC87-845E-48AB-A9C2-9436001BA68A`: `AppleSPU.kext/PlugIns/AppleSPULib.plugin`
- `IOClass`: `AppleSPUALSSunfishDriver`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPU`
- `IOProviderClass`: `IOHIDInterface`
- `QueueSize`: `16384`
- `Transport`: `SPU`
- `manufacturer`: `Sunfish`

### AppleSPUAONPTDDriver
- `CFBundleIdentifier`: `com.apple.driver.AppleSPU`
- `IOClass`: `AppleSPUAONPTDDriver`
- `IOMatchCategory`: `AppleSPUAONPTDDriver`
- `IONameMatch`:
  - `aon-ptd`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPU`
- `IOProviderClass`: `AppleSPUAppInterface`

### AppleSPUAppDriver
- `CFBundleIdentifier`: `com.apple.driver.AppleSPU`
- `IOClass`: `AppleSPUAppDriver`
- `IONameMatch`:
  - `SPUApp`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPU`
- `IOProviderClass`: `AppleSPUAppInterface`
- `IOUserClientClass`: `AppleSPUAppDriverUserClient`

### AppleSPUBasebandDriver
- `CFBundleIdentifier`: `com.apple.driver.AppleSPU`
- `IOClass`: `AppleSPUBasebandDriver`
- `IONameMatch`:
  - `AOP_baseband`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPU`
- `IOProviderClass`: `AppleSPUAppInterface`

### AppleSPUBattChannelDriver
- `CFBundleIdentifier`: `com.apple.driver.AppleSPU`
- `IOClass`: `AppleSPUBattChannelDriver`
- `IONameMatch`:
  - `batt-adc`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPU`
- `IOProviderClass`: `AppleSPUAppInterface`
- `IOUserClientClass`: `AppleSPUBattChannelUserClient`

### AppleSPUBoraUartDriver
- `CFBundleIdentifier`: `com.apple.driver.AppleSPU`
- `IOClass`: `AppleSPUBoraUartDriver`
- `IONameMatch`:
  - `bora-uart`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPU`
- `IOProviderClass`: `AppleSPUAppInterface`

### AppleSPUButtonDriver
- `CFBundleIdentifier`: `com.apple.driver.AppleSPU`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `1`
    - `DeviceUsagePage`: `11`
  -
    - `DeviceUsage`: `1`
    - `DeviceUsagePage`: `12`
- `IOCFPlugInTypes`:
  - `3BC5CC87-845E-48AB-A9C2-9436001BA68A`: `AppleSPU.kext/PlugIns/AppleSPULib.plugin`
- `IOClass`: `AppleSPUButtonDriver`
- `IOParentMatch`:
  - `IOParentMatch`:
    - `IONameMatch`:
      - `aop-button`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPU`
- `IOProviderClass`: `IOHIDInterface`
- `Transport`: `SPU`

### AppleSPUControl
- `CFBundleIdentifier`: `com.apple.driver.AppleSPU`
- `IOClass`: `AppleSPUControl`
- `IOMatchCategory`: `AppleSPUControl`
- `IONameMatch`:
  - `multi-touch`
  - `opal`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPU`
- `IOProviderClass`: `AppleARMIODevice`

### AppleSPUDCPDriver
- `CFBundleIdentifier`: `com.apple.driver.AppleSPU`
- `IOClass`: `AppleSPUDCPDriver`
- `IONameMatch`:
  - `dcp-control`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPU`
- `IOProviderClass`: `AppleSPUAppInterface`

### AppleSPUDispADCDriver
- `CFBundleIdentifier`: `com.apple.driver.AppleSPU`
- `IOClass`: `AppleSPUDispADCDriver`
- `IONameMatch`:
  - `disp-adc`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPU`
- `IOProviderClass`: `AppleSPUAppInterface`
- `IOUserClientClass`: `AppleSPUDispADCUserClient`

### AppleSPUFirmwareService-AOP
- `CFBundleIdentifier`: `com.apple.driver.AppleSPU`
- `IOClass`: `AppleSPUFirmwareService`
- `IOMatchCategory`: `RTBuddyFirmwareService`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPU`
- `IOPropertyMatch`:
  - `role`: `AOP`
- `IOProviderClass`: `RTBuddyService`

### AppleSPUFirmwareService-SPU
- `CFBundleIdentifier`: `com.apple.driver.AppleSPU`
- `IOClass`: `AppleSPUFirmwareService`
- `IOMatchCategory`: `RTBuddyFirmwareService`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPU`
- `IOPropertyMatch`:
  - `role`: `SPU`
- `IOProviderClass`: `RTBuddyService`

### AppleSPUFirmwareService-SPU2
- `CFBundleIdentifier`: `com.apple.driver.AppleSPU`
- `IOClass`: `AppleSPUFirmwareService`
- `IOMatchCategory`: `RTBuddyFirmwareService`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPU`
- `IOPropertyMatch`:
  - `role`: `SPU2`
- `IOProviderClass`: `RTBuddyService`

### AppleSPUGNSSDriver
- `CFBundleIdentifier`: `com.apple.driver.AppleSPU`
- `IOCFPlugInTypes`:
  - `3168B08E-E57D-4E04-92C9-C015B8B0E9AB`: `AppleSPU.kext/PlugIns/GNSSPassthroughLib.plugin`
- `IOClass`: `AppleSPUGNSSDriver`
- `IONameMatch`:
  - `gnss`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPU`
- `IOProviderClass`: `AppleSPUAppInterface`
- `IOUserClientClass`: `AppleSPUGNSSDriverUserClient`

### AppleSPUGestureDriver
- `CFBundleIdentifier`: `com.apple.driver.AppleSPU`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `3`
    - `DeviceUsagePage`: `65292`
- `IOCFPlugInTypes`:
  - `0B842ADD-C395-4352-95F6-6585EB515623`: `IOHIDFamily.kext/PlugIns/IOHIDLib.plugin`
  - `3BC5CC87-845E-48AB-A9C2-9436001BA68A`: `AppleSPU.kext/PlugIns/AppleSPULib.plugin`
- `IOClass`: `AppleSPUGestureDriver`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPU`
- `IOProviderClass`: `IOHIDInterface`
- `QueueSize`: `16384`
- `Transport`: `SPU`

### AppleSPUGpioUnplugDriver
- `CFBundleIdentifier`: `com.apple.driver.AppleSPU`
- `IOClass`: `AppleSPUGpioUnplugDriver`
- `IONameMatch`:
  - `romeo`
  - `juliet`
  - `lanai_l`
  - `lanai_r`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPU`
- `IOProviderClass`: `AppleSPUInterface`

### AppleSPUGrimaldiDriver
- `CFBundleIdentifier`: `com.apple.driver.AppleSPU`
- `IOClass`: `AppleSPUGrimaldiDriver`
- `IONameMatch`:
  - `grimaldi-control`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPU`
- `IOProviderClass`: `AppleSPUAppInterface`

### AppleSPUHIDDevice
- `CFBundleIdentifier`: `com.apple.driver.AppleSPU`
- `IOCFPlugInTypes`:
  - `7ACF5332-1A35-4893-87CB-BA64E1887FAE`: `AppleSPU.kext/PlugIns/AppleSPULib.plugin`
- `IOClass`: `AppleSPUHIDDevice`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPU`
- `IOProviderClass`: `AppleSPUHIDInterface`

### AppleSPUHIDDriver
- `CFBundleIdentifier`: `com.apple.driver.AppleSPU`
- `IOCFPlugInTypes`:
  - `0B842ADD-C395-4352-95F6-6585EB515623`: `IOHIDFamily.kext/PlugIns/IOHIDLib.plugin`
  - `3BC5CC87-845E-48AB-A9C2-9436001BA68A`: `AppleSPU.kext/PlugIns/AppleSPULib.plugin`
- `IOClass`: `AppleSPUHIDDriver`
- `IOParentMatch`:
  - `IOParentMatch`:
    - `IOPropertyMatch`:
      - `UseGenericHIDDriver`: `False`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPU`
- `IOProviderClass`: `IOHIDInterface`
- `QueueSize`: `16384`
- `Transport`: `SPU`

### AppleSPUHIDEventDriver
- `CFBundleIdentifier`: `com.apple.driver.AppleSPU`
- `IOCFPlugInTypes`:
  - `0B842ADD-C395-4352-95F6-6585EB515623`: `IOHIDFamily.kext/PlugIns/IOHIDLib.plugin`
  - `3BC5CC87-845E-48AB-A9C2-9436001BA68A`: `AppleSPU.kext/PlugIns/AppleSPULib.plugin`
- `IOClass`: `AppleSPUHIDEventDriver`
- `IOParentMatch`:
  - `IOParentMatch`:
    - `IOPropertyMatch`:
      - `UseGenericHIDDriver`: `True`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPU`
- `IOProviderClass`: `IOHIDInterface`
- `QueueSize`: `16384`
- `Transport`: `SPU`

### AppleSPUHapticsAudioDriver
- `CFBundleIdentifier`: `com.apple.driver.AppleSPU`
- `IOClass`: `AppleSPUHapticsAudioDriver`
- `IONameMatch`:
  - `aop-haptics-audio`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPU`
- `IOProviderClass`: `AppleSPUInterface`
- `IOUserClientClass`: `AppleSPUHapticsAudioUC`

### AppleSPUHapticsManagerDriver
- `CFBundleIdentifier`: `com.apple.driver.AppleSPU`
- `IOClass`: `AppleSPUHapticsManagerDriver`
- `IONameMatch`:
  - `aop-haptics-manager`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPU`
- `IOProviderClass`: `AppleSPUInterface`
- `IOUserClientClass`: `AppleSPUHapticsManagerUserClient`

### AppleSPULogDriver
- `CFBundleIdentifier`: `com.apple.driver.AppleSPU`
- `IOClass`: `AppleSPULogDriver`
- `IOMatchCategory`: `AppleSPULogDriver`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPU`
- `IOProviderClass`: `AppleSPUAppDriver`
- `IOUserClientClass`: `AppleSPULogDriverUserClient`

### AppleSPULogFirmwareDriver
- `CFBundleIdentifier`: `com.apple.driver.AppleSPU`
- `IOClass`: `AppleSPULogFirmwareDriver`
- `IOMatchCategory`: `AppleSPULogFirmwareDriver`
- `IONameMatch`:
  - `AOP_log`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPU`
- `IOProviderClass`: `AppleSPUInterface`

### AppleSPUMarconiControl
- `CFBundleIdentifier`: `com.apple.driver.AppleSPU`
- `IOClass`: `AppleSPUMarconiControl`
- `IOMatchCategory`: `AppleSPUMarconiControl`
- `IONameMatch`:
  - `aop-marconi-bt-control`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPU`
- `IOProviderClass`: `AppleSPUAppInterface`

### AppleSPUMesaDriver
- `CFBundleIdentifier`: `com.apple.driver.AppleSPU`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `19`
    - `DeviceUsagePage`: `32`
- `IOClass`: `AppleSPUMesaDriver`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPU`
- `IOProviderClass`: `IOHIDInterface`
- `Transport`: `SPU`

### AppleSPUPDMCLKDriver
- `CFBundleIdentifier`: `com.apple.driver.AppleSPU`
- `IOClass`: `AppleSPUPDMCLKDriver`
- `IONameMatch`:
  - `pdmclk`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPU`
- `IOProviderClass`: `AppleSPUInterface`

### AppleSPUProfileDriver
- `CFBundleIdentifier`: `com.apple.driver.AppleSPU`
- `IOClass`: `AppleSPUProfileDriver`
- `IOMatchCategory`: `AppleSPUProfileDriver`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPU`
- `IOProviderClass`: `AppleSPUAppDriver`
- `IOUserClientClass`: `AppleSPUProfileDriverUserClient`

### AppleSPUProfileFirmwareDriver
- `CFBundleIdentifier`: `com.apple.driver.AppleSPU`
- `IOClass`: `AppleSPUProfileFirmwareDriver`
- `IOMatchCategory`: `AppleSPUProfileFirmwareDriver`
- `IONameMatch`:
  - `AOP_profile`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPU`
- `IOProviderClass`: `AppleSPUInterface`

### AppleSPUSmartCoverDriver
- `CFBundleIdentifier`: `com.apple.driver.AppleSPU`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `41`
    - `DeviceUsagePage`: `65280`
  -
    - `DeviceUsage`: `1`
    - `DeviceUsagePage`: `11`
- `IOCFPlugInTypes`:
  - `3BC5CC87-845E-48AB-A9C2-9436001BA68A`: `AppleSPU.kext/PlugIns/AppleSPULib.plugin`
- `IOClass`: `AppleSPUSmartCoverDriver`
- `IOParentMatch`:
  - `IOParentMatch`:
    - `IONameMatch`:
      - `aop-smart-cover`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPU`
- `IOProviderClass`: `IOHIDInterface`
- `Transport`: `SPU`

### AppleSPUTimesyncV1
- `CFBundleIdentifier`: `com.apple.driver.AppleSPU`
- `IOClass`: `AppleSPUTimesyncV1`
- `IOKitDebug`: `65535`
- `IOMatchCategory`: `AppleSPUTimesync`
- `IONameMatch`: `iop-spu-nub`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPU`
- `IOProviderClass`: `AppleA7IOPNub`

### AppleSPUTimesyncV2
- `CFBundleIdentifier`: `com.apple.driver.AppleSPU`
- `IOClass`: `AppleSPUTimesyncV2`
- `IOKitDebug`: `65535`
- `IOMatchCategory`: `AppleSPUTimesync`
- `IONameMatch`:
  - `iop-aop-nub`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPU`
- `IOProviderClass`: `AppleA7IOPNub`


## C++ classes (61) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleAOPSMCDriver` | 0xf8 | IOService → IORegistryEntry |
| `AppleAOPSMCFunction` | 0x38 | AppleARMFunction |
| `AppleLVBOOST` | 0xa0 | IOService → IORegistryEntry |
| `AppleSPU` | 0x698 | IOService → IORegistryEntry |
| `AppleSPUALSDriver` | 0x278 | AppleSPUHIDDriver → AppleEmbeddedHIDEventService → IOHIDEventService → IOService → IORegistryEntry |
| `AppleSPUALSSealionAccessoryDriver` | 0x298 | AppleSPUALSDriver → AppleSPUHIDDriver → AppleEmbeddedHIDEventService → IOHIDEventService → IOService → IORegistryEntry |
| `AppleSPUALSSealionDriver` | 0x400 | AppleSPUALSDriver → AppleSPUHIDDriver → AppleEmbeddedHIDEventService → IOHIDEventService → IOService → IORegistryEntry |
| `AppleSPUALSSunfishDriver` | 0x280 | AppleSPUALSDriver → AppleSPUHIDDriver → AppleEmbeddedHIDEventService → IOHIDEventService → IOService → IORegistryEntry |
| `AppleSPUAONPTDDriver` | 0xa0 | IOService → IORegistryEntry |
| `AppleSPUAppDriver` | 0x150 | IOService → IORegistryEntry |
| `AppleSPUAppDriverUserClient` | 0x100 | IOUserClient → IOService → IORegistryEntry |
| `AppleSPUAppInterface` | 0x1a8 | AppleSPUInterface → IOService → IORegistryEntry |
| `AppleSPUBasebandDriver` | 0xc0 | IOService → IORegistryEntry |
| `AppleSPUBattChannelDriver` | 0xb0 | IOService → IORegistryEntry |
| `AppleSPUBattChannelUserClient` | 0x118 | IOUserClient → IOService → IORegistryEntry |
| `AppleSPUBoraUartDriver` | 0xa0 | IOService → IORegistryEntry |
| `AppleSPUButtonDriver` | 0x880 | AppleSPUHIDDriver → AppleEmbeddedHIDEventService → IOHIDEventService → IOService → IORegistryEntry |
| `AppleSPUCoexParams` | 0x68 |  |
| `AppleSPUControl` | 0xe0 | IOService → IORegistryEntry |
| `AppleSPUDCPDriver` | 0xc0 | IOService → IORegistryEntry |
| `AppleSPUDispADCDriver` | 0xc0 | IOService → IORegistryEntry |
| `AppleSPUDispADCUserClient` | 0x118 | IOUserClient → IOService → IORegistryEntry |
| `AppleSPUFastpathCaptureObject` | 0x120 |  |
| `AppleSPUFastpathClientObject` | 0x18 |  |
| `AppleSPUFastpathDriver` | 0xc8 | IOService → IORegistryEntry |
| `AppleSPUFastpathDriverUserClient` | 0x100 | IOUserClient2022 → IOUserClient → IOService → IORegistryEntry |
| `AppleSPUFastpathInterface` | 0xa8 | IOService → IORegistryEntry |
| `AppleSPUFirmwareService` | 0x1c0 | RTBuddyFirmwareService → IOService → IORegistryEntry |
| `AppleSPUGNSSDriver` | 0xf8 | IOService → IORegistryEntry |
| `AppleSPUGNSSDriverUserClient` | 0x108 | IOUserClient2022 → IOUserClient → IOService → IORegistryEntry |
| `AppleSPUGpioUnplugDriver` | 0xb0 | IOService → IORegistryEntry |
| `AppleSPUGrimaldiDriver` | 0xd0 | IOService → IORegistryEntry |
| `AppleSPUHIDDevice` | 0x240 | IOHIDDevice → IOService → IORegistryEntry |
| `AppleSPUHIDDeviceUserClient` | 0x128 | IOUserClient → IOService → IORegistryEntry |
| `AppleSPUHIDDriver` | 0x238 | AppleEmbeddedHIDEventService → IOHIDEventService → IOService → IORegistryEntry |
| `AppleSPUHIDDriverUserClient` | 0x110 | IOUserClient → IOService → IORegistryEntry |
| `AppleSPUHIDEventDriver` | 0x160 | IOHIDEventDriver → IOHIDEventService → IOService → IORegistryEntry |
| `AppleSPUHIDInterface` | 0x1a8 | AppleSPUInterface → IOService → IORegistryEntry |
| `AppleSPUHapticsAudioDriver` | 0x670 | IOService → IORegistryEntry |
| `AppleSPUHapticsAudioUC` | 0xf8 | IOUserClient → IOService → IORegistryEntry |
| `AppleSPUHapticsManagerDriver` | 0xa0 | IOService → IORegistryEntry |
| `AppleSPUHapticsManagerUserClient` | 0x108 | IOUserClient → IOService → IORegistryEntry |
| `AppleSPUInterface` | 0x1a8 | IOService → IORegistryEntry |
| `AppleSPUMarconiControl` | 0xa8 | IOService → IORegistryEntry |
| `AppleSPUMarconiFunction` | 0x38 | AppleARMFunction |
| `AppleSPUMesaDriver` | 0x260 | AppleSPUHIDDriver → AppleEmbeddedHIDEventService → IOHIDEventService → IOService → IORegistryEntry |
| `AppleSPUPDMCLKDriver` | 0x90 | IOService → IORegistryEntry |
| `AppleSPUProfileDriver` | 0x5f10 | IOService → IORegistryEntry |
| `AppleSPUProfileDriverUserClient` | 0x100 | IOUserClient → IOService → IORegistryEntry |
| `AppleSPUProfileFirmwareDriver` | 0x108 | IOService → IORegistryEntry |
| `AppleSPURemoteCrashdump` | 0x50 |  |
| `AppleSPUSimpleAsyncEventSource` | 0x50 | IOEventSource |
| `AppleSPUSingleShotReporter` | 0xa8 | IOService → IORegistryEntry |
| `AppleSPUSmartCoverDriver` | 0x258 | AppleSPUHIDDriver → AppleEmbeddedHIDEventService → IOHIDEventService → IOService → IORegistryEntry |
| `AppleSPUSpkAmpStateFunction` | 0x40 | AppleARMFunction |
| `AppleSPUTimesync` | 0xe0 | IOService → IORegistryEntry |
| `AppleSPUTimesyncV1` | 0xe0 | AppleSPUTimesync → IOService → IORegistryEntry |
| `AppleSPUTimesyncV2` | 0xe0 | AppleSPUTimesync → IOService → IORegistryEntry |
| `AppleSPUUserClient` | 0x108 | IOUserClient → IOService → IORegistryEntry |
| `ClientObject` | 0x48 |  |
| `SPUCommand` | 0x38 | IOCommand |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1720)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00007468 off=0x00772d10-0x0077a178 addr=0xfffffe0007776d10-0xfffffe000777e178 r--/r--   __TEXT            
	sz=0x00005dcf off=0x00773428-0x007791f7 addr=0xfffffe0007777428-0xfffffe000777d1f7               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000bee off=0x007791f7-0x00779de5 addr=0xfffffe000777d1f7-0xfffffe000777dde5               __TEXT.__os_log           
	sz=0x00000388 off=0x00779df0-0x0077a178 addr=0xfffffe000777ddf0-0xfffffe000777e178               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x000488fc off=0x026bb3d0-0x02703ccc addr=0xfffffe00096bf3d0-0xfffffe0009707ccc r-x/r-x   __TEXT_EXEC       
	sz=0x00047cfc off=0x026bb3d0-0x027030cc addr=0xfffffe00096bf3d0-0xfffffe00097070cc          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000c00 off=0x027030cc-0x02703ccc addr=0xfffffe00097070cc-0xfffffe0009707ccc          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000018c8 off=0x04998188-0x04999a50 addr=0xfffffe000b99c188-0xfffffe000b99da50 rw-/rw-   __DATA            
	sz=0x00000938 off=0x04998188-0x04998ac0 addr=0xfffffe000b99c188-0xfffffe000b99cac0               __DATA.__data             
	sz=0x000009c0 off=0x00000000-0x000009c0 addr=0xfffffe000b99cac0-0xfffffe000b99d480               __DATA.__common           (Zerofill)
	sz=0x000005d0 off=0x00000000-0x000005d0 addr=0xfffffe000b99d480-0xfffffe000b99da50               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x000191e8 off=0x01207b90-0x01220d78 addr=0xfffffe000820bb90-0xfffffe0008224d78 rw-/rw-   __DATA_CONST      
	sz=0x00000188 off=0x01207b90-0x01207d18 addr=0xfffffe000820bb90-0xfffffe000820bd18         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000188 off=0x01207d18-0x01207ea0 addr=0xfffffe000820bd18-0xfffffe000820bea0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000174a8 off=0x01207ea0-0x0121f348 addr=0xfffffe000820bea0-0xfffffe0008223348         __DATA_CONST.__const            
	sz=0x00000f40 off=0x0121f348-0x01220288 addr=0xfffffe0008223348-0xfffffe0008224288         __DATA_CONST.__kalloc_type      
	sz=0x00000320 off=0x01220288-0x012205a8 addr=0xfffffe0008224288-0xfffffe00082245a8         __DATA_CONST.__kalloc_var       
	sz=0x00000600 off=0x012205a8-0x01220ba8 addr=0xfffffe00082245a8-0xfffffe0008224ba8         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000001d0 off=0x01220ba8-0x01220d78 addr=0xfffffe0008224ba8-0xfffffe0008224d78         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 442 at 0x04ae5f90
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     CE7DAAE7-13AD-3292-BB7A-15A1D8614E7A
008: LC_SOURCE_VERSION           1087.40.4.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab1d38 size=0xb58
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleSPU`
- `CFBundleIdentifier`: `com.apple.driver.AppleSPU`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleSPU`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2013 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleSPU.kext`
- `_PrelinkExecutableLoadAddr`: `-2198897988336`
- `_PrelinkExecutableRelativePath`: `AppleSPU`
- `_PrelinkExecutableSize`: `436244`
- `_PrelinkExecutableSourceAddr`: `-2198897988336`
- `_PrelinkKmodInfo`: `-2198828629624`

## Strings (970) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `BatteryCompensationEnable`
- `compass-hilo-compensation`
- `set-config`
- `AppleSPUFastPathRingBuffer.cpp`
- `tx queue size`
- `allow-raw-i2c`
- `HumidityFactoryMode`
- `audio-mic-notify`
- `AppleSPU`
- `%s: Unrecognized command %d received for ALSS!\n`
- `aop_workout_detected`
- `function-lvboost`
- `1211111212221212111111111222222`
- `com.apple.aop.hid-driver.hid-service.pdr`
- `anymotion`
- `12111112122212121121`
- `spu_ep_%u_cmd_%02x`
- `AppleSPUGNSSDriver`
- `chip_id`
- `InterfaceType`
- `Unexpected packetType: %d`
- `site.AppleSPUHapticsAudioDriver`
- `12111112122212121111111211111112222221211211222222222221112111121111212`
- `RawTemperatureMode`
- `_ap_latency`
- `dispatchCombo`
- `AppleSPUTimesync`
- `spu_SCMHIDDebug`
- `HIDRelayManagerFirmwarePortName`
- `kernel-read`
- `com.apple.aop.adc.user-client.full-access`
- `rx queue size`
- `enable-1k6-imu`
- `UseAABPlugin`
- `std-dev-z-cal`
- `%s: received`
- `%s: Got PM Assertion ID %llx\n`
- `k2-low-priority`
- `setPropertiesGated`
- `open`
- `WaitNumFramesAfterSuccess`
- `com.apple.aop.spuapp.user-client.full-access`
- `site.AppleSPUSpkAmpStateFunction`
- `sysconfig-location-id-override`
- `coex%d-matched`
- `std-dev-y-cal`
- `AppleSPUDataQueue.cpp`
- `EventCount`
- `AppleSPUHIDDriverUserClient`
- `set-lvboost`
- `pmu-arc-reset`
- `StateGain`
- `compass-mode-offset-comp`
- `ALS reports`
- `%c`
- `ReportBufferEntrySize`
- `compass-sens-calibration`
- `site.AppleSPUFastpathInterface`
- `iop_ringbuffer.h`
- `Osmium reports`
- `CurrentNits`
- `site.AppleSPUHIDDevice`
- `121111121222121211111`
- `pressure-use-polling`
- `AppleSPUPDMCLKDriver`
- `AppleSPUMesaDriver`
- `%s: Sending kMesaCommandResetBegin command\n`
- `RTBuddyPatchBay.h`
- `GlobalForceFeel`
- `cma`
- `ReportInterval`
- `function-vsh_adc_pwr`
- `AccelerometerMotionDetectionMode`
- `site.AppleSPUHapticsManagerDriver`
- `com.apple.aop.profile.user-client`
- `spu_rtp_optical`
- `aop-fr-timebase`
- `FastPathMotionEventEntitlement`
- `AppleSPUButtonDriver`
- `StateHapticType`
- `function-grimaldi-power`
- `part`
- `aonBufferTest`
- `site.AppleSPUBattChannelUserClient`
- `AppleSPUFastpathCaptureObject`
- `hidrelay-enable`
- `k2-int-opendrain`
- `scrt`
- `__ETEXT`
- `AppleSPUSmartCoverDriver`
- `12111112122212121111`
- `121`
- `ocpErrorToKernelClientFunction`
- `%s::%s - calibrated successfully!\n`
- `1222222222222212`
- `com.apple.aop.spuapp.user-client`
- `%s: reportID: %#02x type: %#02x usage-page: %#04x usage: %#04x size: %#x\n`
- `IOHIDALSTestMode`
- `AppleSPUALSDriver::%s Setting mode %d\n`
- `\"AOT not supported on endpoints with historical buffer\" @%s:%d`
- `SensitivityCompensationClosedEnable`
- `spu_queue_overflow_ep%u`
- `ap-cont`
- `light-em-up`
- `potassium-low-priority`
- `Role`
- `AppleSPUHapticsManagerUserClient`
- `raw-stream`
- `measure`
- `lid-angle-sensor-calibration`
- `IOReportLegendPublic`
- `12111112122212121111111111111210`
- `Error AppleSPU %s: _queueStopped is true on sleep path`
- `spu_none`
- `reset`
- `all`
- `ApplePTD`
- `com.apple.aop.batt.user-client.full-access`
- `allowed-action-list`
- `watch-coex-adc`
- `spmiReadyToKernelClientFunction`
- `AppleSPUFastpathDriverUserClient`
- `accel-nominal-extr-cal`
- `spkamp-config_%s`
- `aop_flip`
- `aop-strict-entitlements`
- `BGHRProperties`
- `compass-battery-compensation`
- `role`
- `_ext`
- `IOUserClientDefaultLockingSetProperties`
- `AppleAOPSMCDriver`
- `ALSS: Sync ALS Function %p\n`
- `GyroForcePWMMode`
- `%s%s`
- `site.AppleSPUDispADCDriver`
- `ERROR: The LSCI2.4 calibration key is too small\n`
- `AppleSPUBasebandDriver`
- `use-aop-force_pwm`
- `site.AppleSPUTimesyncV2`
- `would fail`
- `turtle-temperature-cal`
- `description`
- `coex%d-payload-off`
- `Lisa reports`
- `site.AppleSPUGrimaldiDriver`
- `alsCalibration`
- `ERROR: Insufficient calibration key version - %d.%d\n`
- `AppleSPUHapticsAudioDriver::%s\n`
- `121111121222121211111111111112110`
- `ApplePDMController`
- `%s: reportID: %#02x type: %#02x %#02x usage-page: %#04x usage: %#04x size: %#x [COLLECTION]\n`
- `HIDDefaultBehavior`
- `SensorCompensationMode`
- `prox-calibration`
- `panic %02x`
- `ap`
- `get-property`
- `AppleSPUHIDDriver: set %s kIOHIDEventServiceQueueSize to %d KB\n`
- `compass-sens-angle-table`
- `AppleSPUTimesyncV1`
- `ButtonErrStatusMesa`
- `IOHIDALSRunHistorical`
- `spu_rtp_lisa`
- `calendar`
- `handleClickStateGlobalConfig`
- `AppleSPUHIDDriver: coexID:%d found for service:%s from driver:%s \n`
- `phi-attach-low-cal`
- `site.AppleAOPSMCFunction`
- `StateButtonState`
- `Built-In`
- `true`
- `function-clock`
- `multi-touch`
- `site.AppleSPUHIDDeviceUserClient`
- `function-alss`
- `com.apple.aop.user-client.full-access`
- `AppleSPUTimesyncV2`
- `AppleSPUHIDDeviceUserClient`
- `has-baseband`
- `ALSS: Display ALSS Function %p\n`
- `AppleSPURemoteCrashdump`
- `ap-batch`
- `1211222111`
- `ON`
- `phi-ignore-high-cal`
- `%s: found node %s\n`
- `coex%d-driver-name`
- `site.AppleSPUProfileDriverUserClient`
- `Tried to override key %s but failed with: 0x%x\n`
- `hilo-factor-x`
- `AppleSPUBasebandDriver BB-Uart quiescing: %s\n`
- `hilo-threshold-z`
- `accel-range-sensitivity-cal`
- `Wakes`
- `spu_queue_overflow_ep`
- `BatchInterval`
- `Address`
- `%s: unsupported size for patchbay variable 0x%x (%d)\n`
- `Sealion driver found\n`
- `AppleSPUHIDDriver:: matched AppleARMPMUCharger service %p\n`
- `phi-detach-low-cal`
- `AppleSPUHapticsAudioUC`
- `AppleSPUALSSealionDriver`
- `aop-dcp-buffer-size`
- `IOHIDPlacementType`
- `admin`
- `spu_gesture`
- `Platinum reports`
- `smc-shared-region-base`
- `d79-rev1-clp-workaround`
- `moscovium-logging`
- `CompassFactoryMode`
- `AppleSPUFirmwareService.cpp`
- `handleFrameBufferMsg`
- `ERROR: The ALS calibration key is too small\n`
- `site.AppleSPUAONPTDDriver`
- `model`
- `IOUserClientCreator`
- `com.apple.aop.hid-driver.hid-service.cma`
- `1211111212221212111111111111210`
- `function-cs`
- `%s'%s'=%u\n`
- `aop_orientation`
- `GreenCoefficient`
- `HESOnlyMode`
- `penultDuration`
- `TemperatureCompensationEnable`
- `UseMachContinuousTime`
- `spu_osmium`
- `site.AppleSPUAppDriverUserClient`
- `site.AppleSPUAppDriver`
- `%s `
- `AppleSPUHIDEventDriver`
- `firmware-type`
- `hilo-threshold-y`
- `LocationID`
- `site.ClientObject`
- `aop_cblite`
- `site.AppleSPUButtonDriver`
- `com.apple.aop.haptics-audio.user-client`
- `aop_bluetooth`
- `WalletCompensationEnable`
- `temp-offset-calibration`
- `\"%s: firmware validation failed %d\" @%s:%d`
- `reportInterval`
- `phi-attach-high-cal`
- `site.AppleSPUHapticsAudioUC`
- `AppleSPUSpkAmpStateFunction`
- `SPI reports`
- `function-als-sync`
- `osmium-revision`
- `AccelMeasurementRange`
- `AppleSPUAppDriver: Register for audio notifier\n`
- `AppleSPU(%d): Missing acquire historical`
- `RGB coeffs IOFixed %x, %x, %x\n`
- `com.apple.aop.haptics.set-mapping.access`
- `Shake`
- `spu_platinum`
- `HIDRelayUSBInterface`
- `turtle_temp_comp`
- `kTCCServiceMotionSensors`
- `coex%d-notif-off`
- `+++++\n`
- `accel-interrupt-calibration`
- `bInterfaceNumber`
- `spu_reset_slave`
- `AppleSPUFastpathDriver`
- `absolute-temp-offset-cal`
- `aop_juliet_unplug_detected`
- `Compass reports`
- `count`
- `AppleSPUDispADCDriver`
- `pdm-clk-for-display`
- `ButtonErrStatusBtmSpk`
- `ERROR: The LSCI4.x calibration key is too small\n`
- `%s usage: %x %x -> %x\n`
- `SupportAlwaysOnCompass`
- `AppleSPUHIDDriver::Unable to match AppleARMPMUCharger service\n`
- `GYRO_TEMP`
- `\"Incompatible protocol version: spu=%#08x kext=%#08x\" @%s:%d`
- `%s: too many external segments\n`
- `calibration_state`
- `pressure-offset-calibration`
- `AppleSPUAppDriver : pmu-pwm-on-msg = %x\n`
- `handleDeviceStateReport`
- `IOHIDEventService`
- `compass-apl-compensation`
- `AppleSPUBattChannelUserClient`
- `AOP endpoint %u`
- `AppleSPUHIDInterface`
- `site.AppleSPUProfileDriver`
- `limit-i2c-bus-frequency`
- `AppleSPU_ep%d`
- `AppleSPUHapticsManagerDriver`
- `FactoryMode`
- `TCCService`
- `12111112122212121111111211111112222221211211222222222221112111121111212122222212`
- `%s_ext`
- `AppleSPUHIDDevice`
- `site.AppleSPUHapticsManagerUserClient`
- `disable-aicl`
- `spu-ignore-pras-calibration`
- `AppleSPUFastpathInterface`
- `AppleSPU::_handleReadyReport, serviceName (%s) \n`
- `site.AppleSPUSimpleAsyncEventSource`
- `121111121222121211112`
- `Mux`
- `Captured errdump [%ld bytes]\n`
- `hamm-p2-risetime-fix`
- `perform-command`
- `bt-pico-cal`
- `%x`
- `1211111212221212111112222122`
- `\"%s: %d images found in fw bundle\" @%s:%d`
- `AOP ALSS Function instantiated!\n`
- `memdump`
- `humidity-offset-calibration`
- `absolute-temp-offset-bcm-cal`
- `pid %d, `
- `historical queue size`
- `ButtonErrStatusTurtle`
- `HistoricalBufferDefersQueueStart`
- `spu`
- `Total packets`
- `%s: (kv %d pc %d lp %d sc %d tx %d)\n`
- `ButtonErrStatusArc`
- `site.AppleSPUUserClient`
- `QueueSize`
- `site.AppleSPU`
- `aop_eclipse`
- `_num_events`
- `pmu-btmspk-reset`
- `RawInterval`
- `121111121222121211122`
- `1211111212221212111111121111111222222121121122222222222111211112111121211122`
- `AppleSPUUserClient`
- `site.AppleSPUBattChannelDriver`
- `function-flicker_bias`
- `aop-profiler-disable`
- `bosch-high-odr`
- `AccelerometerFactoryMode`
- `site.AppleSPUALSSunfishDriver`
- `aop_gesture1`
- `.`
- `spu_touch`
- `Resetting nub %s...\n`
- `_num_first_more1s`
- `IMMERSION_TEMP`
- `function-power`
- `1211121112`
- `read`
- `aop-audio-debug`
- `IOHIDOrientationType`
- `las`
- `1211111212221212111111121111111222222121121122222222222111211112111121212222221`
- `122122121`
- `coex%d-prop`
- `-----\n`
- `pt-led-type`
- `statistics`
- `Number of services`
- `LmaxProduct`
- `aop_impact`
- `_handleSubPacket`
- `SPU2`
- `dispatchAccel`
- `spu_sedentary_alarm`
- `Ready reports`
- `HIDRelaySupport`
- `compass-orientation`
- `spu-ignore-sppo-calibration`
- `site.AppleLVBOOST`
- `1211111212221212111111111111111112110`
- `\"%s: firmware target %s not found\" @%s:%d`
- `HIDRelayBehavior`
- `%s-b2b-unplug-detected`
- `PanicSPU`
- `AppleSPU.cpp`
- `site.AppleSPUTimesyncV1`
- `enable-doppler`
- `aop-button`
- `1222112111222`
- `aggd`
- `ALSSSupported`
- `AppleSPUHIDDriver`
- `AppleSPUBoraUartDriver`
- `minimum-request-spacing-ms`
- `aop_crane`
- `Tag`
- `ERROR: Coefficient '%s' is empty!\n`
- `AppleSPUInterface`
- `timesync`
- `first_bhfassets_ts`
- `ALSS Calling display with kIOAOPFBConfigure returned %s\n`
- `ufp:`
- `clock-count`
- `has-dapf`
- `spu-accel-historical`
- `AppleSPUHapticsAudioDriver`
- `bb-gyro-fwload-coex`
- `_last_event_timestamp`
- `spkamp-names`
- `StateMinTime`
- `AppleSPUControl`
- `PrimaryUsage`
- `absolute-temp-offset-fcm-cal`
- `%d`
- `j307-awcs-dev-intr-mapping`
- `AppleARMBacklight`
- `AppleSPUMarconiControl`
- `RTBuddyService`
- `com.apple.aop.adc.user-client`
- `%08x: `
- `rose-removal-for-doe`
- `\"%s: invalid firmware bundle format\\n\" @%s:%d`
- `default`
- `site.AppleSPUCoexParams`
- `gyro-sensitivity-calibration`
- `%s: claim system wake flags:%#x reason:'%s'\n`
- `plugin`
- `MotionEventRestricted`
- `gyro-range-sensitivity-cal`
- `AppleSPUAppDriver : pmu-pwm-off-msg = %x\n`
- `Message reports`
- `RedCoefficient`
- `121111121222121211111111111122121`
- `sensor_rates`
- `1211111212221212111222222222222`
- `aop-force-fw-loading`
- `AppleSPUGNSSDriverUserClient::clientClose[%s]`
- `ButtonErrStatusGeneral`
- `accel-offset-cal`
- `PrimaryUsagePage`
- `name`
- `AppleARMPMUCharger`
- `aop-memory-alignment`
- `disable-juliet-unplug-detect`
- `site.AppleSPUControl`
- `spherecontrol`
- `com.apple.aop.user-client`
- `site.AppleSPUPDMCLKDriver`
- `com.apple.aop.profile.user-client.full-access`
- `mesa-pm-assertion`
- `12111112122212121111111211111112222221211211222222222221112111121111212122222211121211122222222222222222222222222222222222222111`
- `StateAssertion`
- `MaxReportBufferCount`
- `12111112122212121111111111111121210`
- `_first_ts_s`
- `MotionTriggerNumFrames`
- `%s: GPIO state %x\n`
- `aop-isp-v2protocol`
- `ALSSAvailable`
- `<unknown>`
- `set-named-property`
- `succeeded`
- `com.apple.drivers.AppleSPUMarconiControl`
- `compass-wallet-compensation`
- `phi-detach-high-cal`
- `,`
- `IOUserClientDefaultLocking`
- `AppleSPUDCPDriver`
- `function-gnss-time-mark`
- `smc-aop-charge-config`
- `ALSS config has %d rects\n`
- `gnss-force-ap-timemark`
- `Placement`
- `AppleSPUProfileFirmwareDriver`
- `set-property`
- `OFF`
- `APLCompensationEnable`
- `hgal-ocal`
- `%s'%s'=%s\n`
- `spu_unknown(0x%02x)_ep%u`
- `aop_threshold_als`
- `site.AppleSPUFastpathCaptureObject`
- `aop-i2c-conf`
- `com.apple.aop.gnss.user-client.full-access`
- `button-err-state-ap-ts`
- `ThresholdX`
- `pressure-global-offset-cal`
- `spu_activity_alarm`
- `AppleCS42L79Audio`
- `/product`
- `%s::%s state change for comp %s to %#x`
- `InstantAmperage`
- `AppleAOPSMCFunction`
- `com.apple.aop.fastpath.user-client`
- `silicon`
- `SPUCommand`
- `1211111212221212111111`
- `aop-isp-v2`
- `ASSET CONFIG: state:%u speed: %u slot:%u minDelta:%llu maxDelta %llu gain:%x enable:%u\n`
- `site.AppleSPUALSSealionAccessoryDriver`
- `DroppedEventCount`
- `AppleSPU(%d): AcquireHistorical mismatch acq=%d != rel %d`
- `wake reasons`
- `reset-count`
- `service_id`
- `AppleSPUMarconiFunction`
- `get-named-property`
- `theta-detach-low-cal`
- `AppleSPUInterface(%s): %s: failed seq=%x cat=%x payloadSize=%x \n`
- `com.apple.aop.hid-device.user-client`
- `site.AppleSPUSingleShotReporter`
- `compass-temp-calibration`
- `AppleSPUSimpleAsyncEventSource`
- `site.AppleSPUFastpathDriverUserClient`
- `orb-offset-cal`
- `121111121222121211121222121211122121212111`
- `site.AppleSPUTimesync`
- `%s: ext mapping: tag:0x%x len:%d\n`
- `site.AppleSPUDCPDriver`
- `AppleSPUAONPTDDriver`
- `AppleSPU(%d): Failed to copy historical MD`
- `Packet errors`
- `GlobalConfig`
- `com.apple.aop.fastpath.user-client.full-access`
- `AppleSPU(%d): AcquireHistorical wrptr mismatch %d != %d`
- `aop_prox`
- `Received ready report for fastpath %s [%d,%d]\n`
- `12111112122212121111111112121112122122122122122122122122`
- `%.*s`
- `module-revision`
- `stats`
- `AppleSPUCoexParams`
- `aop_ttw`
- `crashdump`
- `AppleSPUDispADCUserClient`
- `hilo-log`
- `watch-moscovium`
- `watch-sage-vsh`
- `SensitivityAngleTableEnable`
- `ap-time-mark-with-boot-arg`
- `_aop_latency`
- `%s::%s state change to %d at %llu`
- `com.apple.aop.haptics-manager.user-client`
- `121111121222121211`
- `mode`
- `site.AppleSPURemoteCrashdump`
- `hilo-factor-z`
- `enable-coex%d`
- `kIOAOPALSAbortCapture recvd, stopping ALS\n`
- `accel-sensitivity-calibration`
- `Sunfish driver found\n`
- `12111112122212121121121111112221122222222222121111222`
- `%s: reportID: %#02x type: %#02x %#02x usage-page: %#04x usage: %#04x size: %#x value: %#x (%#x)\n`
- `spu_READY`
- `1211111212221212112222`
- `BCMTemperatureCompensationEnable`
- `site.AppleSPUFastpathClientObject`
- `Total signals`
- `%s: %x -> %x\n`
- `Received a reset request from SPU for nub %s\n`
- `com.apple.aop.user-client.all`
- `\"multiple historical queue owners on %s\\n\" @%s:%d`
- `IOUserClientDefaultLockingSingleThreadExternalMethod`
- `gyro-range-extr-cal`
- `site.AppleSPUHIDEventDriver`
- `hilo-factor-y`
- `121111121222121211122121`
- `site.AppleSPUALSDriver`
- `unk`
- `AppleSPUAppDriver error: pmu-pwm-off-msg not present\n`
- `historical_tester`
- `!! Unexpected SPU wake reason %d, setting to unknown !!`
- `spu_opal_reset`
- `smc-shared-region-size`
- `ocpDataReadyToKernelClientFunction`
- `on`
- `hgal-scal`
- `satin-cal`
- `aop-hardening`
- `hilo-lmax`
- `NoFactoryCalibration`
- `StateEnable`
- `calibration_complete_ts`
- `%s: forcePWM %x\n`
- `set-grape-cs`
- `sulu-historical`
- `site.IOAOPFBRect`
- `PRESSURE_TEMP`
- `phi-ignore-low-cal`
- `toggle-reset-count`
- `%llu`
- `\"%s\" @%s:%d`
- `start`
- `121111121222121211111112212211111`
- `coex%d-notif-on`
- `spu_sshb`
- `Reset reports`
- `aot`
- `\"fp_ringbuffer abort at %s:%d [ref=%p]\" @%s:%d`
- `site.AppleSPUGNSSDriverUserClient`
- `site.AppleSPUSmartCoverDriver`
- `connected`
- `IOReportLegend`
- `IOHibernateState`
- `yCurrentRegion negative!, window %d!!\n`
- `StateSpeed`
- `IOUserClientEntitlements`
- `AppleSPUALSDriver`
- `AppleSPUSingleShotReporter`
- `RawMode`
- `raw-spi`
- `__EDATA`
- `false`
- `\"out of buffer entries\" @%s:%d`
- `accel-range-extr-cal`
- `send-command`
- `%s: setting config for spk %s\n`
- `site.AppleSPUProfileFirmwareDriver`
- `site.AppleSPUHIDInterface`
- `AppleSPUInterface.cpp`
- `StateConfig`
- `ap-report`
- `12111121`
- `spu-nap`
- `hilo-always-send`
- `AppleVoltageDictionary`
- `coex%d-payload-on`
- `gyro-trim-calibration`
- `aop_ped_fence`
- `1211212`
- `_num_events_after_wake`
- `pressure-heater-resistance`
- `voice_trigger`
- `aop_wireless_chrg`
- `\"ringbuffer abort at %s:%d [%s]\" @%s:%d`
- `function-force_pwm`
- `ERROR: Failed to dequeue from iop_ringbuffer! cnt: %d\n`
- `ALSS config has %lu %lu %lu coeffs\n`
- `12111112122212121111111211111112222221211211222222222221112111121111212221111111111111222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222`
- `12111112122212121112`
- `1211111212221212111111111111212110`
- `audio`
- `spu_rtp_hr`
- `aop_romeo_unplug_detected`
- `aop_wombat`
- `UseGenericHIDDriver`
- `AOP`
- `com.apple.aop.hid-driver.user-client.full-access`
- `set-state-assertion`
- `alternate-prox-gpio`
- `hilo-threshold`
- `aop-timesync-reg-index`
- `HIDPropertiesRequiredForMatching`
- `AppleSPU(%d): Clearing historical queue for endpoint\n`
- `ERROR: The numRegions in LSCI4.x calibration data is too large.`
- `HIDRelayManagerDeviceConfig`
- `low-temp-accel-offset`
- `historical-memory`
- `\"Unexpected message from IOP (msg: %#llx)\" @%s:%d`
- `1211112`
- `sens`
- `ap-wake`
- `SupportHDRCompass`
- `AppleSPUBattChannelDriver`
- `\"Variable write size (%ld) does not match patch variable size(%d)\" @%s:%d`
- `bt-inverse-filter-cal`
- `maggie_ready_ts`
- `121111121222121211111222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222`
- `<null>`
- `gyro-range-intr-cal`
- `awcs-dev-intr-mapping`
- `121111121222121211111112`
- `GyroProperties`
- `site.AppleSPUHIDDriverUserClient`
- `pmu-pwm-off-msg`
- `%s`
- `%s\n`
- `ButtonErrStatusMux`
- `site.AppleSPUFirmwareService`
- `StateSlot`
- `dispatchGyro`
- `site.CompassCompensation`
- `AppleSPUHIDDriverUC.cpp`
- `aop_brook`
- `AppleSPUFirmwareService`
- `DetectionMode`
- `ProxFactoryMode`
- `turtle-hot-probe-cal`
- `Accel reports`
- `hidrelay-usb-interface-name`
- `log`
- `%s(%s): %#x`
- `com.apple.aop.haptics-manager.user-client.full-access`
- `AppleSPUALSSealionAccessoryDriver`
- `compass-bcm-calibration`
- `Gyro reports`
- `121111121222121211112112`
- `12111112122212121112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222`
- `AppleSPUAONPTD`
- `AppleSPUGrimaldiDriver`
- `loadCalibrationData`
- `AccelVarThreshold`
- `theta-detach-high-cal`
- `firmware-name`
- `121111121222121211211122211111212121212121212121212121212121221111112122`
- `site.AppleSPUDispADCUserClient`
- `aop-profiler-config`
- `IOPropertyMatch`
- `site.AppleSPUGNSSDriver`
- `GyroFactoryMode`
- `site.float`
- `serial_number`
- `Configuring AOP profiler (%s) -> %x\n`
- `dependency-name`
- `watch-doe-thermopile`
- `probe`
- `IOHIDALSRawMode`
- `_forcePWM`
- `AppleSPUAppDriver`
- `\"slaveMemory=%p\" @%s:%d`
- `AppleSPUProfileDriverUserClient`
- `DisplayCompensationEnable`
- `BGHREnable`
- `aop_smart_cover`
- `SerialNumber`
- `manufacturer`
- `assert`
- `cumulus`
- `spu_rtp_ctrl`
- `rose-otp-workaround`
- `opal`
- `DebugState`
- `Target`
- `AppleSPUGNSSDriverUserClient`
- `COMPASS_TEMP`
- `theta-attach-low-cal`
- `profile`
- `PanicOscar`
- `site.AppleSPUBoraUartDriver`
- `AppleSPU(%u): historical queue for endpoint has not been drained\n`
- `site.AppleSPUAppInterface`
- `site.AppleAOPSMCDriver`
- `k2-pkg-id`
- `motionRestrictedService`
- `spu_unknown`
- `%s: bad size for dt property %s (%d)\n`
- `site.AppleSPUALSSealionDriver`
- `KextTimestamp`
- `GyroExtLevelTriggerSync`
- `compass-sens-calibration-closed`
- `AppleSPUALSSunfishDriver`
- `queueSize`
- `DataCount`
- `12111112122212121111111211111112222221211211222222222221112111121111212122222211212`
- `ScheduleWake`
- `spu_aggregate_dictionary`
- `spu_als`
- `aop_bump`
- `site.SPUCommand`
- `DroppedDataCount`
- `button-err-state-masks`
- `bb-uart-quiescing`
- `play-asset`
- `RX packets`
- `AOP_`
- `user`
- `ptd-data-table`
- `AOPSupportsAggregateDictionary`
- `AppleSPUFastpathClientObject`
- `StateMaxTime`
- `prox-debug`
- `handleClickStateConfig`
- `Apple`
- `spmiErrorToKernelClientFunction`
- `1211111212221212111121221`
- `HIDServiceAccessEntitlement`
- `_num_events_before_sleep`
- `pmu-pwm-client`
- `sound_analysis`
- `maximum-ap-request-latency`
- `AppleBaseband`
- `%s set HESOnlyMode to %u\n`
- `site.AppleSPUFastpathDriver`
- `charger-compensation-vers`
- `unknown`
- `pressure-ext-trigger`
- `maximum-ap-request-latency-observed`
- `   `
- ` | `
- `function-mesa_reset`
- `function-reset`
- `AppleDAPF`
- `ALSS is not supported, ALS lux values may be incorrect!\n`
- `ERROR: '%s' is empty!\n`
- `ERROR: The LSCI4.5 calibration key is too small\n`
- `_handleTxHistoricalQueueLocal`
- `always-on-domain`
- `com.apple.aop.hid-driver.user-client`
- `ERROR: The numRegions in LSCI4.5 calibration data is too large.`
- `site.AppleSPUMarconiFunction`
- `payloadSize`
- `compass-vbus-compensation`
- `AppleSPUInterface(%s): %s: seq=%x cat=%x payloadSize=%x\n`
- `12111112122212121111111211111122111111222222`
- `site.AppleSPUBasebandDriver`
- `AppleSPUAppDriver error: pmu-pwm-on-msg not present\n`
- `spu_slave`
- `als-alternate`
- `com.apple.aop.hid-device.user-client.full-access`
- `registerKernelClientToAppleBasebandFunction`
- `ClientObject`
- `%s'%s'\n`
- `12111112122212121211`
- `ALSS COEFF r %#x, g %#x, b %#x\n`
- `site.Timesync`
- `AppleSPUProfileDriver`
- `setIntegrationMode`
- `coex%d-duration-threshold-msecs`
- `AppleSPUGNSSDriverUserClient::start[%s] -> %d [ret=%x]`
- `historical buffer defers queue start`
- `AutoRateControl`
- `com.apple.aop.haptics-audio.user-client.full-access`
- `%d stale messages for endpoint %s\n`
- `_num_first_less1s`
- `AppleSPUHIDDriver: failed to send timesync report (sz=%u)\n`
- `theta-attach-high-cal`
- `\"_handleReadyReport called more than once \\n\" @%s:%d`
- `AppleSPUAppDriverUserClient`
- `AppleSPUAppInterface`
- ` `
- `BlueCoefficient`
- `timestamp`
- `disable-gicl`
- `com.apple.aop.batt.user-client`
- `121111121222121211111112111111122222212112112222222222211121111211112121111`
- `ModeOffsetCompensationEnable`
- `audio_env_dosimetry`
- `IOMobileFramebuffer`
- `_first_ts_b`
- `12111112122212121111112112`
- `watch-doe-adc`
- `wdt`
- `ACCEL_TEMP`
- `COMBO_TEMP`
- `\"user panic\" @%s:%d`
- `aop_rose_ctrl`
- `none`
- `backlight`
- `1211111212221212111112122122`
- `Responses`
- `com.apple.aop.gnss.user-client`
- `BasebandInReset`
- `SensitivityCompensationEnable`
- `accel-range-intr-cal`
- `ALSS RECT[%d]: x %d y %d w %d h %d\n`
- `button-err-state-aop-ts`
- `%02x `
- `SPU`
- `report`
- `site.AppleSPUHIDDriver`
- `get-config`
- `pmu-pwm-on-msg`
- `ERROR: Bad profile queue ptr! rdptr=%d wrptr=%d size=%d\n`
- `site.AppleSPUMesaDriver`
- `aop-dcp-buffer-address`
- `IOHIDALSDumpCalibration`
- `SensorTestMode`
- `raw-access`
- `IOUserClientClass`
- `aop-retention`
- `%s: Request latency check failed (reqID:%d latency:%llu)\n`
- `button-err-state`
- `AppleLVBOOST`
- `aop-profile`
- `AppleSPUGpioUnplugDriver`
- `pressure-accel-sensitivity`
- `1211111212221212121111121111112221111221221121111222111122122112111122211112212211212111112112221122211222112221122211222112221122211222112221122211222112221122211222112222221111222222222222222222222222222221212`
- `GlobalNumStages`
- `magnitude-cal`
- `aop-target`
- `site.AppleSPUGpioUnplugDriver`
- `SensorPowerMode`
- `ExactMatchOnly`
- `ChargerCompensationEnable`
- `TX packets`
- `spu_mesa_reset`
- `Captured kext errdump [%ld bytes]\n`
- `srb_ringbuffer.h`
- `121111111222221221111111111222222222`
- `AppleSPUBasebandDriver BB-Gyro coex: %s\n`
- `off`
- `site.AppleSPUInterface`
- `aop-accel-alternate`
- `LastQueueTime`
- `highg`
- `HumidityRawMode`
- `slaveAlignment`
- `aop-smc-endpoint-cfg`
- `RegisterService`
- `aop-hid-driver-uc-hardening`
- `%d `
- `AppleSPUAppDriver: pdm notification message: %x, power state: %ld\n`
- `function-spu-lvboost`
- `%s: manufacturer %s\n`
- `ALSIntegrationMode`
- `baseband`
- `toggle-reset-enabled`
- `aonBuffer`
- `site.AppleSPUMarconiControl`
- `ThresholdPeriod`
- `FastPathHasEntitlement`
- `hilo-threshold-x`
- `HUMIDITY_TEMP`
- `gyro-interrupt-calibration`
- `gyro-nominal-extr-cal`
- `std-dev-x-cal`
- `Grape reports`
- `chip-role`
- `failed`
- `HID reports`

**[__TEXT.__os_log]**

- `Unable to create ARM function for Grimaldi power`
- `Aborting Grimaldi power on - system is going to sleep\n`
- `Unable to create ARM function for VSH ADC power`
- `Error running stop AOP ADC sampling: %x`
- `nullptr passed to stopMeasurement for collected samples`
- `AppleSPUMarconiControl Failed setPowerEnable %d, %d`
- `%s: entering sleep state (events this cycle: %u)`
- `Unable to power on ADC: %x`
- `Could not allocate AOP sample buffer size %d`
- `Unable to power off ADC`
- `AppleSPUMarconiFunction: _signature=%#x param1=%p param2=%p param3=%p\n`
- `Entitlement check %s for \"%s\" for operation %s:%s:%s on %s`
- `AP continuous time before rising GPIO: %llu. After rising GPIO: %llu\n`
- `Dropped gnss data report queue is full(%zu)`
- `Error setting grimaldi power state`
- `Grimaldi timed out waiting for audio codec to power on\n`
- `AppleSPUMarconiControl setPowerEnable %d time %lldus (%lld)\n`
- `AppleSPUGNSSDriver::_setEventQueueGated kIOReturnExclusiveAccess`
- `Dropped gnss event due to oversized packet: %zu`
- `  GetPingPongBufferPayloadSize -> %x`
- `AppleSPUHIDDriver - failed to register interest for coex service %p, coex index %d\n`
- `SSHB_ASSET UPDATE: state:%u speed: %u slot:%u minDelta:%llu maxDelta %llu gain:%x enable:%u -> %s [result=%x]`
- `Found ARM function for Flicker Bias Control`
- `calling _marconi_ctrl->notifyMarconiPowerEnable, en=%d\n`
- `PTDEntries update: %#x`
- `%s watchdog triggered; num_events=%u delta=%lld winterval=%d\n`
- `No memory for aon buffer \n`
- `AppleSPUHIDDriver::openForClient -> %x`
- `AppleSPUHIDDriver: %s set coex property %d %s, ret=%x, coex-idx=%x`
- `%s: waking from sleep`
- `Grimaldi was interrupted while waiting for audio codec to power on\n`
- `AppleSPUGNSSDriver::_setDataNotificationPortGated kIOReturnNotReady`
- `Dropped gnss data report due to missing data queue %zu`
- `Dropped gnss event for queue error(%zu)`
- `[hilo-compensation] report interval changed to %d`
- `%s startdog; time=%llu num_events=%u report_intvl=%u last_event=%llu delta=%llu\n`
- `  ClientOpen(%u,%u) -> %x`
- `Unable to find ARM function for Flicker Bias Control`
- `Starting display ADC sampling`
- `%s: does not support %s (usage pair - 0x%04x:0x%04x)`
- `[hilo-compensation] nits: %u apl: %u/1000 prev_offset: (%d %d %d) factor: (%d %d %d) new_offset: (%d %d %d) diff: (%d %d %d) threshold: (%d %d %d) exceed: %s sendAlways: %s`
- `[hilo-compensation] thread call already pending`
- `Stopping display ADC sampling`
- `AppleSPUMarconiControl setPowerEnable [Caching State] %d, %d time %lldus (%lld)`
- `AppleSPUGNSSDriver::_setDataQueueGated kIOReturnExclusiveAccess`
- `  GetAonBufferPayloadSize -> %x`
- `  ClientOpen(%zu,%zu) -> %x`
- `[%s] %.*s\n`
- `%s: started for %s (usage pair 0x%04x:0x%04x)`
- `Returned buffer size from AOP ADC display sampling does not match number of samples`
- `Matched ptd table, size: %d`
- `Dropped gnss event due to missing data queue %zu`
- `[hilo-compensation] sending %d %#08x,  %d %#08x,  %d %#08x`
- `SSHB_ASSET CONFIG: state:%u speed: %u slot:%u minDelta:%llu maxDelta %llu gain:%x enable:%u -> %s [result=%x]`
- `Client \"%s\" attempts to execute internal command %s:%s:%s on %s`
- `%s: first event after wake, latency %llu us`
