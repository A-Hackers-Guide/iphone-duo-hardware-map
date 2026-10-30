# `/arm-io/iop-audio-controller/audio-hpdbg`

- Name: `audio-hpdbg`
- Parent: [`/arm-io/iop-audio-controller`](root__arm-io__iop-audio-controller.md)
- phandle: `377`
- compatible: `audio-control,audio-iop-haptic-debug`
- device_type: `iop-audio-ns`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `IOPHapticDebug` | `IOPAudioNode` | [`com.apple.driver.IOPHaptics`](../kexts/com.apple.driver.IOPHaptics.md) | `audio-control,audio-iop-haptic-debug` |

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `hall_ctrl` | [`/arm-io/i2c2/audio-codec`](root__arm-io__i2c2__audio-codec.md) | `hall` | `` |
| `input-data-selectors` | [`/arm-io/haptics-support-interface`](root__arm-io__haptics-support-interface.md) | `hdis` | `` |

## All properties (15) [DT]

- **`AAPL,phandle`**: `377` (`0x179`) → phandle of [`/arm-io/iop-audio-controller/audio-hpdbg`](root__arm-io__iop-audio-controller__audio-hpdbg.md)
- **`compatible`**: `audio-control,audio-iop-haptic-debug`
- **`default-input-data-sources`**: 32 bytes
  - u32: `0x61706163 0x636f6163 0x63706f73 0x73657162 0x61725630 0x61724930 0x68616c78 0x68616c79`
  - text inside: `capacaocsopcbqes0Vra0Iraxlahylah`
  ```
  000000  63 61 70 61 63 61 6f 63 73 6f 70 63 62 71 65 73  capacaocsopcbqes
  000010  30 56 72 61 30 49 72 61 78 6c 61 68 79 6c 61 68  0Vra0Iraxlahylah
  ```
- **`device_type`**: `iop-audio-ns`
- **`function-hall_ctrl`**: `0x68616c6c000000b5` (u64; as two u32: `0xb5`, `0x68616c6c`)
- **`function-input-data-selectors`**: `0x68646973000001b9` (u64; as two u32: `0x1b9`, `0x68646973`)
- **`identifier`**: `1634231395` (`0x61686463`) (four-char code `ahdc`)
- **`input-data-source-selectors`**: 456 bytes
  - u32: `0x0 0x61706163 0x616f6163 0x63706f73 0x61724930 0x61725630 0x636f6163 0x666c7473 0x68706331 0x68636d64 0x68616c78 0x636f7574 0x68617872 0x63746d70 0x73746d70 0x73705630 0x73704930 0x6d786175 0x6d74726a 0x6d78656e 0x68706332 0x68706333 0x68706334 0x736d7073 0x73657162 0x6d70656e 0x616f7065 0x6170656e 0x6964636f 0x69646469 0x766c696d 0x616f6175 0x61706175 0x68616c79 0x68617972 0x63656666 0x76636d64 0x72657378 0x72657379 0x73726d70 0x70726d70 0x63726d70 0x67636d64 0x70615630 0x63706761 0x736d6374 0x736c6374 0x74636470 0x7463706f 0x74636363 0x74636c67 0x74637632 0x7463756d 0x74746761 0x78746d70 0x79746d70 0x736c7767 0x666c7467 0x74726d70 0x736f6666 0x746f656e 0x63706f73 0x73706f77 0x61706367 0x78657374 0x76657374 0x62657374 0x62696e74 0x62687066 0x74737430 0x74737431 0x74737432 0x74737433 0x68697271 0x61697271 0x7376656e 0x696e7431 0x696e7432 0x76626174 0x76627374 0x6d706231 0x6d706232 0x72666c78 0x66666378 0x66666c78 0x73666378 0x72667374 0x61707363 0x616f7363 0x696c7666 0x61326769 0x61326763 0x73637469 0x73637463 0x70727469 0x70727463 0x70617669 0x70617663 0x70613235 0x706d7869 0x70616369 0x70633235 0x73707769 0x73707763 0x63707769 0x63707763 0x72637469 0x72637463 0x316b6374 0x72666c79 0x66666379 0x66666c79 0x73666379 0x61326774`
  - text inside: `capacaoasopc0Ira0Vracaocstlf1cphdmchxlahtuocrxahpmtcpmts0Vps0Ipsuaxmjrtmnexm2cph3cph4cphspmsbqesnepmepoanepaocdiiddimilvuaoauapaylahryahffecdmcvxseryserpmrspmrppmrcdmcg0Vapagpctcmstclspdctopctccctglct2vctmuctagttpmtxpmtygwlsgtlfpmrtffosneotsopcwopsgcpatsextsevtsebtnibfphb0tst1tst2tst3tstqrihqrianevs1tni2tnitabvtsbv1bpm2bpmxlfrxcffxlffxcfstsfrcspacsoafvliig2acg2aitcsctcsitrpctrpivapcvap52apixmpicap52cpiwpscwpsiwpccwpcitcrctcrtck1ylfrycffylffycfstg2a`
  ```
  000000  00 00 00 00 63 61 70 61 63 61 6f 61 73 6f 70 63  ....capacaoasopc
  000010  30 49 72 61 30 56 72 61 63 61 6f 63 73 74 6c 66  0Ira0Vracaocstlf
  000020  31 63 70 68 64 6d 63 68 78 6c 61 68 74 75 6f 63  1cphdmchxlahtuoc
  000030  72 78 61 68 70 6d 74 63 70 6d 74 73 30 56 70 73  rxahpmtcpmts0Vps
  000040  30 49 70 73 75 61 78 6d 6a 72 74 6d 6e 65 78 6d  0Ipsuaxmjrtmnexm
  000050  32 63 70 68 33 63 70 68 34 63 70 68 73 70 6d 73  2cph3cph4cphspms
  000060  62 71 65 73 6e 65 70 6d 65 70 6f 61 6e 65 70 61  bqesnepmepoanepa
  000070  6f 63 64 69 69 64 64 69 6d 69 6c 76 75 61 6f 61  ocdiiddimilvuaoa
  000080  75 61 70 61 79 6c 61 68 72 79 61 68 66 66 65 63  uapaylahryahffec
  000090  64 6d 63 76 78 73 65 72 79 73 65 72 70 6d 72 73  dmcvxseryserpmrs
  0000a0  70 6d 72 70 70 6d 72 63 64 6d 63 67 30 56 61 70  pmrppmrcdmcg0Vap
  0000b0  61 67 70 63 74 63 6d 73 74 63 6c 73 70 64 63 74  agpctcmstclspdct
  0000c0  6f 70 63 74 63 63 63 74 67 6c 63 74 32 76 63 74  opctccctglct2vct
  0000d0  6d 75 63 74 61 67 74 74 70 6d 74 78 70 6d 74 79  muctagttpmtxpmty
  0000e0  67 77 6c 73 67 74 6c 66 70 6d 72 74 66 66 6f 73  gwlsgtlfpmrtffos
  0000f0  6e 65 6f 74 73 6f 70 63 77 6f 70 73 67 63 70 61  neotsopcwopsgcpa
  000100  74 73 65 78 74 73 65 76 74 73 65 62 74 6e 69 62  tsextsevtsebtnib
  000110  66 70 68 62 30 74 73 74 31 74 73 74 32 74 73 74  fphb0tst1tst2tst
  000120  33 74 73 74 71 72 69 68 71 72 69 61 6e 65 76 73  3tstqrihqrianevs
  000130  31 74 6e 69 32 74 6e 69 74 61 62 76 74 73 62 76  1tni2tnitabvtsbv
  000140  31 62 70 6d 32 62 70 6d 78 6c 66 72 78 63 66 66  1bpm2bpmxlfrxcff
  000150  78 6c 66 66 78 63 66 73 74 73 66 72 63 73 70 61  xlffxcfstsfrcspa
  000160  63 73 6f 61 66 76 6c 69 69 67 32 61 63 67 32 61  csoafvliig2acg2a
  000170  69 74 63 73 63 74 63 73 69 74 72 70 63 74 72 70  itcsctcsitrpctrp
  000180  69 76 61 70 63 76 61 70 35 32 61 70 69 78 6d 70  ivapcvap52apixmp
  000190  69 63 61 70 35 32 63 70 69 77 70 73 63 77 70 73  icap52cpiwpscwps
  0001a0  69 77 70 63 63 77 70 63 69 74 63 72 63 74 63 72  iwpccwpcitcrctcr
  0001b0  74 63 6b 31 79 6c 66 72 79 63 66 66 79 6c 66 66  tck1ylfrycffylff
  0001c0  79 63 66 73 74 67 32 61                          ycfstg2a
  ```
- **`input-latency`**: `5` (`0x5`)
- **`model-name`**: `IOPHapticDebug`
- **`name`**: `audio-hpdbg`
- **`output-latency`**: `5` (`0x5`)
- **`powered-on-state`**: `1886876260` (`0x70777264`) (four-char code `pwrd`)
- **`uid`**: `Haptic Debug`
- **`zerofill-buffer-size-ms`**: `5` (`0x5`)
