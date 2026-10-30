# `/arm-io/aop/iop-aop-nub/compass`

- Name: `compass`
- Parent: [`/arm-io/aop/iop-aop-nub`](root__arm-io__aop__iop-aop-nub.md)
- phandle: `91`
- device_type: `compass`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## All properties (40) [DT]

- **`AAPL,phandle`**: `91` (`0x5b`) → phandle of [`/arm-io/aop/iop-aop-nub/compass`](root__arm-io__aop__iop-aop-nub__compass.md)
- **`charger-compensation-vers`**: `2` (`0x2`)
- **`coex0-driver-name`**: `IOPAudioSpeaker`
- **`coex0-notif-off`**: `3825172744` (`0xe3ff8108`)
- **`coex0-notif-on`**: `3825172743` (`0xe3ff8107`)
- **`coex0-payload-off`**: `0` (`0x0`)
- **`coex0-payload-on`**: `1` (`0x1`)
- **`coex0-prop`**: `89` (`0x59`)
- **`coex1-driver-name`**: `IOPHaptics`
- **`coex1-notif-off`**: `3825172750` (`0xe3ff810e`)
- **`coex1-notif-on`**: `3825172749` (`0xe3ff810d`)
- **`coex1-payload-off`**: `0` (`0x0`)
- **`coex1-payload-on`**: `1` (`0x1`)
- **`coex1-prop`**: `89` (`0x59`)
- **`coex2-driver-name`**: `AppleSARService`
- **`coex2-notif-off`**: `3825172498` (`0xe3ff8012`)
- **`coex2-notif-on`**: `3825172497` (`0xe3ff8011`)
- **`coex2-payload-off`**: `0` (`0x0`)
- **`coex2-payload-on`**: `1` (`0x1`)
- **`coex2-prop`**: `89` (`0x59`)
- **`compass-apl-compensation-boe`**: `syscfg/MDCC` *(placeholder, filled in by iBoot at boot)*
- **`compass-apl-compensation-sdc`**: `syscfg/MDCC` *(placeholder, filled in by iBoot at boot)*
- **`compass-calibration`**: `syscfg/CPAS` *(placeholder, filled in by iBoot at boot)*
- **`compass-hilo-compensation`**: `syscfg/CDCC` *(placeholder, filled in by iBoot at boot)*
- **`compass-mode-offset-comp`**: `syscfg/CMOC` *(placeholder, filled in by iBoot at boot)*
- **`compass-orientation`**: `syscfg/CRot,hex/010001010000000028000000030000000000000000000100000000000000FFFF0000000000000000000000000000000000000100CAB71340` *(placeholder, filled in by iBoot at boot)*
- **`compass-orientation-p2`**: `syscfg/CRot,hex/01000101000000002800000003000000000000000000FFFF000000000000010000000000000000000000000000000000000001004C0D02E7` *(placeholder, filled in by iBoot at boot)*
- **`compass-sens-angle-table`**: `hex/01000000060000000000000099FB0000D8000000ECFFFFFF5A050000170701004800000056EFFFFF9C040000C500010000000A006F020100A4FFFFFF83000000B0020000C30301008A00000087F7FFFFD70200009EFF000000001400610401009EFFFFFF3B010000EC010000610201004800000002FCFFFF19020000D9FF000000001E00A9040100D2FFFFFFE501000096010000900101006F00000091FDFFFFCB0100002E00010000003C00F8030100210000001903000083010000900001009D000000B2FEFFFF4E010000B8000100000078001A01010097000000F80200009000000027000100E5000000D9FEFFFF8300000000000100` *(placeholder, filled in by iBoot at boot)*
- **`compass-sens-calibration`**: `syscfg/CSCM` *(placeholder, filled in by iBoot at boot)*
- **`compass-sens-calibration-closed`**: `syscfg/CSCa` *(placeholder, filled in by iBoot at boot)*
- **`compass-temp-calibration`**: 32 bytes
  - u32: `0x3 0x1866 0xffff861e 0x5ccd 0x0 0x0 0x0 0x190000`
  ```
  000000  03 00 00 00 66 18 00 00 1e 86 ff ff cd 5c 00 00  ....f........\..
  000010  00 00 00 00 00 00 00 00 00 00 00 00 00 00 19 00  ................
  ```
- **`compass-vbus-compensation`**: `syscfg/CVCC` *(placeholder, filled in by iBoot at boot)*
- **`device-usage`**: `10` (`0xa`)
- **`device-usage-page`**: `65280` (`0xff00`)
- **`device_type`**: `compass`
- **`enable-coex0`**: (present, empty)
- **`enable-coex1`**: (present, empty)
- **`enable-coex2`**: (present, empty)
- **`name`**: `compass`
- **`sysconfig-location-id-override`**: `0` (`0x0`)
