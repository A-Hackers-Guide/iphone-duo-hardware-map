# BuildManifest

Every component Apple signs for the iPhone19,4 iOS 27.2 restore, per build identity. Personalization (the IM4M ticket from Apple's signing server) covers each component's digest; flags such as `Trusted`, `ESEC` and `EPRO` say how it is checked. **[FW]**

- ProductVersion: `27.2`, ProductBuildVersion: `24B91020`
- SupportedProductTypes: `iPhone19,4`

## Customer Erase Install (IPSW)

- `ApChipID`: `0x8160`
- `ApBoardID`: `0x0E`
- `ApSecurityDomain`: `0x01`
- `Ap,ProductType`: `iPhone19,4`
- `Ap,Target`: `V68AP`
- `Ap,TargetType`: `v68`
- `Ap,ProductMarketingVersion`: `27.2`
- `Ap,OSLongVersion`: `24.2.102.9.0,0`
- Info `Ap,Timestamp`: `0`
- Info `BuildNumber`: `24B91020`
- Info `BuildTrain`: `RavePopB`
- Info `ContentEncoding`: `aea`
- Info `Cryptex1,AppOSSize`: `16`
- Info `Cryptex1,SystemOSSize`: `5918`
- Info `DeviceClass`: `v68ap`
- Info `FDRSupport`: `True`
- Info `ImageName`: `V68RestoreIPSW`
- Info `MinimumSystemPartition`: `9791`
- Info `MobileDeviceMinVersion`: `1853`
- Info `OSDiskImageSize`: `10364`
- Info `OSVarContentSize`: `818733056`
- Info `RecoveryVariant`: `Recovery Customer Install`
- Info `RequiresNonceSlot`: `True`
- Info `RequiresUIDMode`: `True`
- Info `RestoreAttestationMode`: `8`
- Info `RestoreBehavior`: `Erase`
- Info `Variant`: `Customer Erase Install (IPSW)`

172 components.

| Component | Path | Digest (SHA-384, first 16 hex) | Flags |
|---|---|---|---|
| `ANE` | `Firmware/ane/h19_ane0_fw_perses_v6x.im4p` | `64b8d6c628bad189` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `ANS` | `Firmware/ansf.t8160.release.im4p` | `14d1f7273d1a1d75` | Trusted, IsFirmwarePayload, RestoreRequestRules |
| `AOP` | `Firmware/AOP/aopfw-v68aop.RELEASE.im4p` | `a8be918779ae2c1d` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `AOP2` | `Firmware/AOP2/aop2fw-v68aop2.RELEASE.im4p` | `abfbc6dc12c26f5c` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `AVE` | `Firmware/ave/AppleAVE2FW_H19.im4p` | `b9030e94822ebb2c` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `Ap,ANE1` | `Firmware/ane/h19_ane1_fw_perses_v6x.im4p` | `051c0dc0bb17eed9` | Trusted, IsFUDFirmware, RestoreRequestRules |
| `Ap,AVD` | `Firmware/avd/AppleAVDFW_H19P.im4p` | `a580555ba355aca0` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `Ap,ApplePMCFirmware` | `Firmware/pmc/t8160pmcfw.im4p` | `887e53baaf9f25ad` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `Ap,AppleVideoEncoder0` | `Firmware/ave/AppleAVE2FW_H19_AVE0.im4p` | `63e41e5d2bfa0328` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `Ap,AppleVideoEncoder1` | `Firmware/ave/AppleAVE2FW_H19_AVE1.im4p` | `049e3519a25033b3` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `Ap,AppleVideoEncoder2` | `Firmware/ave/AppleAVE2FW_H19_AVE2.im4p` | `19c0e781fee7cba7` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `Ap,AppleVideoEncoder3` | `Firmware/ave/AppleAVE2FW_H19_AVE3.im4p` | `5e1206584755555f` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `Ap,AppleVideoEncoder4` | `Firmware/ave/AppleAVE2FW_H19_AVE4.im4p` | `1adac89457306494` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `Ap,AppleVideoEncoder5` | `Firmware/ave/AppleAVE2FW_H19_AVE5.im4p` | `63ff7021a0e26aab` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `Ap,AppleVideoEncoder6` | `Firmware/ave/AppleAVE2FW_H19_AVE6.im4p` | `e62efe0891fc91f5` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `Ap,AppleVideoEncoder7` | `Firmware/ave/AppleAVE2FW_H19_AVE7.im4p` | `223eda99b6bace8b` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `Ap,AppleVideoEncoder8` | `Firmware/ave/AppleAVE2FW_H19_AVE8.im4p` | `05f79bc85c0600aa` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `Ap,AudioBootChime` | `Firmware/embeddedaudioresources/image4/v68-boot-chime.im4p` | `9e584ad82b3787c6` | Trusted, IsiBootNonEssentialFirmware, RestoreRequestRules |
| `Ap,ExclaveOS` | `141-27521-104.dmg.aea` | `e5068d05578a3d9e` | Trusted, RestoreRequestRules |
| `Ap,ExclaveOSIntegrityCatalog` | `Firmware/141-27521-104.dmg.aea.integrity_catalog` | `414d318f25032cf9` | Trusted, IsFUDFirmware, RestoreRequestRules |
| `Ap,ExclaveOSTrustCache` | `Firmware/141-27521-104.dmg.aea.trustcache` | `c11c6fe006449290` | Trusted, IsFUDFirmware, RestoreRequestRules |
| `Ap,ExclaveOSVolume` | `Firmware/141-27521-104.dmg.aea.root_hash` | `e7d273a37772bbb8` | Trusted, IsFUDFirmware, RestoreRequestRules |
| `Ap,GFX1Firmware` | `Firmware/agx/armfw1_g19p.im4p` | `33febef5d5a22898` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `Ap,HapticAssets` | `Firmware/V68_HapticAssets.im4p` | `9a85fd4f0a9f365e` | IsFUDFirmware, RestoreRequestRules |
| `Ap,LowPowerMode` | `Firmware/AppleLPM/AppleLPM.v68.release.im4p` | `d72c01b171d40df1` | IsiBootEANFirmware, RestoreRequestRules |
| `Ap,MSRFirmware` | `Firmware/msr/t8160.msrf.im4p` | `6c2611f3e8b5eaed` | Trusted, IsFUDFirmware, RestoreRequestRules |
| `Ap,MandoFW` | `Firmware/V68_MandoFirmware.im4p` | `44624f1ad5411cbe` | IsFUDFirmware, RestoreRequestRules |
| `Ap,RestoreANE1` | `Firmware/ane/h19_ane1_fw_perses_v6x.im4p` | `d88874b6f35f6d3f` | Trusted, IsLoadedByiBoot, RestoreRequestRules |
| `Ap,RestoreMSRFirmware` | `Firmware/msr/t8160.rmsr.im4p` | `4594142c48d515ef` | Trusted, IsLoadedByiBoot, RestoreRequestRules |
| `Ap,RestoreSecureM3Firmware` | `Firmware/M3/bin/securem3fw-v68.im4p` | `f4a3ee30ac0b966c` | Trusted, IsLoadedByiBoot, RestoreRequestRules |
| `Ap,RestoreSecurePageTableMonitor` | `Firmware/sptm.t8160.release.im4p` | `c9e66676240d53ab` | Trusted, IsLoadedByiBoot, RestoreRequestRules |
| `Ap,RestoreTrustedExecutionMonitor` | `Firmware/txm.iphoneos.release.im4p` | `75371b6d03b94162` | Trusted, IsLoadedByiBoot, RestoreRequestRules |
| `Ap,RestorecL4` | `Firmware/image4/exclavecore_bundle.v68.RELEASE.restore.im4p` | `f7846005a0bfd5a0` | Trusted, IsLoadedByiBoot, RestoreRequestRules |
| `Ap,SecureM3Firmware` | `Firmware/M3/bin/securem3fw-v68.im4p` | `9b9075693ce1ecd8` | Trusted, IsFUDFirmware, RestoreRequestRules |
| `Ap,SecurePageTableMonitor` | `Firmware/sptm.t8160.release.im4p` | `2f69cb8b9dc4932f` | Trusted, IsFUDFirmware, RestoreRequestRules |
| `Ap,SystemVolumeCanonicalMetadata` | `Firmware/141-28898-095.dmg.aea.mtree` | `5d99f6cc85a80b45` | Trusted, IsFUDFirmware, RestoreRequestRules |
| `Ap,TrustedExecutionMonitor` | `Firmware/txm.iphoneos.release.im4p` | `e9f0a0a9f060553d` | Trusted, IsFUDFirmware, RestoreRequestRules |
| `Ap,cL4` | `Firmware/image4/exclavecore_bundle.v68.RELEASE.im4p` | `c52af32219d872a0` | Trusted, IsFUDFirmware, RestoreRequestRules |
| `AppleLogo` | `Firmware/all_flash/applelogo@2d~iphone.im4p` | `72e55666b43d92ae` | Trusted, IsiBootEANFirmware, RestoreRequestRules |
| `BMU,DigestMap` | `Firmware/Volchok/BAT8193/DigestMap.der` | `a217a7c58314ae73` |  |
| `BMU,FirmwareMap` | `Firmware/Volchok/BAT8193/FirmwareMap.plist` | `b87e189151c508da` |  |
| `BMU2,DigestMap` | `Firmware/Volchok/BAT8193/DigestMap.der` | `a217a7c58314ae73` |  |
| `BMU2,FirmwareMap` | `Firmware/Volchok/BAT8193/FirmwareMap.plist` | `b87e189151c508da` |  |
| `Cellular1,CdpAscDl` | `Firmware/c4020iphone/Release/patched/ftab.bin` | `9bb48fff8021c91f` | Trusted, RestoreRequestRules |
| `Cellular1,CdpAscUl` | `Firmware/c4020iphone/Release/patched/ftab.bin` | `c0e59a3e3ffbd3b5` | Trusted, RestoreRequestRules |
| `Cellular1,CdpHost` | `Firmware/c4020iphone/Release/patched/ftab.bin` | `8d30be1ec9e53237` | Trusted, RestoreRequestRules |
| `Cellular1,L1CL1S` | `Firmware/c4020iphone/Release/patched/ftab.bin` | `46e0cdcb8acbca7a` | Trusted, RestoreRequestRules |
| `Cellular1,LLB` | `Firmware/c4020iphone/Release/patched/ftab.bin` | `162f084d64d6ba1e` | Trusted, RestoreRequestRules |
| `Cellular1,PMUFW` | `Firmware/c4020iphone/Release/patched/ftab.bin` | `33e1a57e7ba21e87` | Trusted, RestoreRequestRules |
| `Cellular1,PMUFW2` | `Firmware/c4020iphone/Release/patched/ftab.bin` | `024bbc34f73996a3` | Trusted, RestoreRequestRules |
| `Cellular1,RTKitOS` | `Firmware/c4020iphone/Release/patched/ftab.bin` | `9ccde882d2e36794` | Trusted, RestoreRequestRules |
| `Cellular1,Recipe` | `Firmware/c4020iphone/Release/patched/ftab.bin` | `e7cb1b15c3717f42` | Trusted, RestoreRequestRules |
| `Cellular1,iBootData` | `Firmware/c4020iphone/Release/patched/ftab.bin` | `45b76cdcd9e32532` | Trusted, RestoreRequestRules |
| `Cryptex1,AppOS` | `141-28395-106.dmg` | `87f1114332363108` | RestoreRequestRules |
| `Cryptex1,AppTrustCache` | `Firmware/141-28395-106.dmg.trustcache` | `7072d57c04de1ffd` | RestoreRequestRules |
| `Cryptex1,AppVolume` | `Firmware/141-28395-106.dmg.root_hash` | `e3a31ede1b5fdbb0` | RestoreRequestRules |
| `Cryptex1,SystemOS` | `141-28400-098.dmg.aea` | `597a37020cb5123a` | RestoreRequestRules |
| `Cryptex1,SystemTrustCache` | `Firmware/141-28400-098.dmg.aea.trustcache` | `fa1bbcbdaa387a71` | RestoreRequestRules |
| `Cryptex1,SystemVolume` | `Firmware/141-28400-098.dmg.aea.root_hash` | `9bfa3a33afdde331` | RestoreRequestRules |
| `DCP` | `Firmware/dcp/t8160dcp.im4p` | `aefaf09c5156cd03` | Trusted, IsiBootEANFirmware, RestoreRequestRules |
| `DeviceTree` | `Firmware/all_flash/DeviceTree.v68ap.im4p` | `a3b521b47aa0f054` | Trusted, IsFirmwarePayload, RestoreRequestRules |
| `GFX` | `Firmware/agx/armfw_g19p.im4p` | `40c7cc60cbda6878` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `ISP` | `Firmware/isp_bni/adc-boreas-v68.im4p` | `33b6bdc438ecbe1b` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `KernelCache` | `kernelcache.release.v6x-pandia` | `9f57d7cf359fc767` | Trusted, RestoreRequestRules |
| `LLB` | `Firmware/all_flash/LLB.v68.RELEASE.im4p` | `302b40b9dbf4070b` | Trusted, IsFirmwarePayload, RestoreRequestRules |
| `LeapHaptics` | `Firmware/V68_LeapHapticsFirmware.im4p` | `8afa6138a6d3be9b` | IsFUDFirmware, RestoreRequestRules |
| `Liquid` | `Firmware/all_flash/liquiddetect@2d~iphone.im4p` | `194aaed667db6ada` | Trusted, IsiBootEANFirmware, RestoreRequestRules |
| `MtpFirmware` | `Firmware/V68_MtpFirmware.im4p` | `270a440ad64cb858` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `Multitouch` | `Firmware/V68_Multitouch.im4p` | `7368509e073e8c3b` | IsFUDFirmware, RestoreRequestRules |
| `OS` | `141-28898-095.dmg.aea` | `b1d8bce0e16a7548` | Trusted, RestoreRequestRules |
| `PMP` | `Firmware/pmp/t8160pmp.im4p` | `19008a2bc4a04e1b` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `Rap,RTKitIOConfig` | `Firmware/Rose/r2p1/ftab.bin` | `6b1013023f1c7479` | Trusted, RestoreRequestRules |
| `Rap,RTKitOS` | `Firmware/Rose/r2p1/ftab.bin` | `e46b5fd033a4a736` | Trusted, RestoreRequestRules |
| `Rap,SoftwareBinaryDsp1` | `Firmware/Rose/r2p1/ftab.bin` | `7300dc26d19b540e` | Trusted, RestoreRequestRules |
| `RecoveryMode` | `Firmware/all_flash/recoverymode@2d~iphone.im4p` | `848e2e1ba471a389` | Trusted, IsiBootEANFirmware, RestoreRequestRules |
| `RestoreANS` | `Firmware/rans.t8160.release.im4p` | `c60c3b84b45ea4f0` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `RestoreDCP` | `Firmware/dcp/t8160dcp_restore.im4p` | `39063050c7616fc6` | Trusted, IsLoadedByiBoot, RestoreRequestRules |
| `RestoreDeviceTree` | `Firmware/all_flash/DeviceTree.v68ap.im4p` | `94cbc3d7c32dfcad` | Trusted, RestoreRequestRules |
| `RestoreKernelCache` | `kernelcache.release.v6x-pandia` | `14a743b0cc147a94` | Trusted, RestoreRequestRules |
| `RestoreLogo` | `Firmware/all_flash/applelogo@2d~iphone.im4p` | `0f7534a7d9c2761a` | Trusted, RestoreRequestRules |
| `RestoreRamDisk` | `141-28940-105.dmg` | `2d09674fd3181693` | Trusted, RestoreRequestRules |
| `RestoreSEP` | `Firmware/all_flash/sep-firmware.v68.RELEASE.im4p` | `6333efcf0bc6eccf` | Trusted, RestoreRequestRules |
| `RestoreTrustCache` | `Firmware/141-28940-105.dmg.trustcache` | `c0b105973b887ac4` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `SE,RapRTKitOS` | `Firmware/Rose/r2p1/ftab.bin` | `e46b5fd033a4a736` |  |
| `SE,RapSwBinDsp` | `Firmware/Rose/r2p1/ftab.bin` | `7300dc26d19b540e` |  |
| `SE,UpdatePayload` | `Firmware/SE/Stockholm91.RELEASE.sefw` | `` |  |
| `SEP` | `Firmware/all_flash/sep-firmware.v68.RELEASE.im4p` | `a4e4c8fcba2b9a78` | Trusted, RestoreRequestRules |
| `SIO` | `Firmware/SmartIOFirmware_ASCv8.im4p` | `8873ba2b293fc114` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `SepStage1` | `Firmware/all_flash/sep-patches.v68.im4p` | `58a738a8ef5bbc8b` | Trusted, RestoreRequestRules |
| `StaticTrustCache` | `Firmware/141-28898-095.dmg.aea.trustcache` | `f9fd4c9b274ca337` | Trusted, IsFUDFirmware, RestoreRequestRules |
| `SystemVolume` | `Firmware/141-28898-095.dmg.aea.root_hash` | `23684e5cf582fcdd` | Trusted, IsFUDFirmware, RestoreRequestRules |
| `WCHFirmwareUpdater` | `Firmware/WirelessPower/WirelessPower.v68.im4p` | `ee119dfcfbb36a8e` | Trusted, IsLoadedByiBoot, IsiBootEANFirmware, RestoreRequestRules |
| `Wireless1,ACIBT` | `Firmware/t2026phoneG2/Release/ftab.bin` | `51c01d433c414fa2` | Trusted, RestoreRequestRules |
| `Wireless1,ACIBTLPEM` | `Firmware/t2026phoneG2/Release/ftab.bin` | `1f9a194a2e7aaa38` | Trusted, RestoreRequestRules |
| `Wireless1,ACIBTManuf` | `Firmware/t2026phoneG2/Release/ftab.bin` | `51c01d433c414fa2` | Trusted, RestoreRequestRules |
| `Wireless1,ACIWIFI` | `Firmware/t2026phoneG2/Release/ftab.bin` | `902b5adeacd5144f` | Trusted, RestoreRequestRules |
| `Wireless1,ACIWiFiTxManuf` | `Firmware/t2026phoneG2/Release/ftab.bin` | `36423b324369661e` | Trusted, RestoreRequestRules |
| `Wireless1,BTSecondary` | `Firmware/t2026phoneG2/Release/ftab.bin` | `ebd59be4d27b01a4` | Trusted, RestoreRequestRules |
| `Wireless1,BTSecondaryManuf` | `Firmware/t2026phoneG2/Release/ftab.bin` | `ebd59be4d27b01a4` | Trusted, RestoreRequestRules |
| `Wireless1,CCPUApplicationFirmware` | `Firmware/t2026phoneG2/Release/ftab.bin` | `45f576ce687be46e` | Trusted, RestoreRequestRules |
| `Wireless1,CoexRealTimeArbiter` | `Firmware/t2026phoneG2/Release/ftab.bin` | `44749c87da9b89c1` | Trusted, RestoreRequestRules |
| `Wireless1,PhyBlueTooth` | `Firmware/t2026phoneG2/Release/ftab.bin` | `181d64d765b57b4e` | Trusted, RestoreRequestRules |
| `Wireless1,PhyBlueTooth5G` | `Firmware/t2026phoneG2/Release/ftab.bin` | `8c0742a5e9ad20e1` | Trusted, RestoreRequestRules |
| `Wireless1,PhyBlueTooth5GManuf` | `Firmware/t2026phoneG2/Release/ftab.bin` | `8c0742a5e9ad20e1` | Trusted, RestoreRequestRules |
| `Wireless1,PhyBlueToothLPM` | `Firmware/t2026phoneG2/Release/ftab.bin` | `b0b972453c81fc03` | Trusted, RestoreRequestRules |
| `Wireless1,PhyBlueToothManuf` | `Firmware/t2026phoneG2/Release/ftab.bin` | `181d64d765b57b4e` | Trusted, RestoreRequestRules |
| `Wireless1,PhyBluetooth5GTrim` | `Firmware/t2026phoneG2/Release/ftab.bin` | `94c974402ac11c71` | Trusted, RestoreRequestRules |
| `Wireless1,PhyBluetoothTrim` | `Firmware/t2026phoneG2/Release/ftab.bin` | `3820e32dc8f92bf0` | Trusted, RestoreRequestRules |
| `Wireless1,RTKitOS` | `Firmware/t2026phoneG2/Release/ftab.bin` | `8219626cc42aae17` | Trusted, RestoreRequestRules |
| `Wireless1,RTKitOSLPEM` | `Firmware/t2026phoneG2/Release/ftab.bin` | `be6863c3d47047bd` | Trusted, RestoreRequestRules |
| `Wireless1,ScanBTLPEM` | `Firmware/t2026phoneG2/Release/ftab.bin` | `3c449b8c373522b5` | Trusted, RestoreRequestRules |
| `Wireless1,ScanBTManuf` | `Firmware/t2026phoneG2/Release/ftab.bin` | `f890cbeafa0ccbeb` | Trusted, RestoreRequestRules |
| `Wireless1,ScanBluetooth` | `Firmware/t2026phoneG2/Release/ftab.bin` | `f890cbeafa0ccbeb` | Trusted, RestoreRequestRules |
| `Wireless1,ScanWifi` | `Firmware/t2026phoneG2/Release/ftab.bin` | `14f68624a65887fa` | Trusted, RestoreRequestRules |
| `Wireless1,ScanWifiManuf` | `Firmware/t2026phoneG2/Release/ftab.bin` | `611a45ae78230635` | Trusted, RestoreRequestRules |
| `Wireless1,WiFiRx` | `Firmware/t2026phoneG2/Release/ftab.bin` | `00751f9522d1e2e3` | Trusted, RestoreRequestRules |
| `Wireless1,WiFiRxManuf` | `Firmware/t2026phoneG2/Release/ftab.bin` | `43b50d30fed4c6be` | Trusted, RestoreRequestRules |
| `Wireless1,WiFiTx` | `Firmware/t2026phoneG2/Release/ftab.bin` | `b28a762c0e1d7d94` | Trusted, RestoreRequestRules |
| `Wireless1,WiFiTxManuf` | `Firmware/t2026phoneG2/Release/ftab.bin` | `da7ad47bb37867fc` | Trusted, RestoreRequestRules |
| `Wireless1,Wifi2GLMAC` | `Firmware/t2026phoneG2/Release/ftab.bin` | `2d0a90a6fcd00801` | Trusted, RestoreRequestRules |
| `Wireless1,Wifi2GLMACManuf` | `Firmware/t2026phoneG2/Release/ftab.bin` | `3e72c8dbb12e0c77` | Trusted, RestoreRequestRules |
| `Wireless1,Wifi2GLPhy` | `Firmware/t2026phoneG2/Release/ftab.bin` | `847eca454fc4f9f4` | Trusted, RestoreRequestRules |
| `Wireless1,Wifi2GLPhyManuf` | `Firmware/t2026phoneG2/Release/ftab.bin` | `847eca454fc4f9f4` | Trusted, RestoreRequestRules |
| `Wireless1,Wifi2GLPhyTrim` | `Firmware/t2026phoneG2/Release/ftab.bin` | `afc1e501998b0b55` | Trusted, RestoreRequestRules |
| `Wireless1,Wifi5GLMAC` | `Firmware/t2026phoneG2/Release/ftab.bin` | `bedce67d68535076` | Trusted, RestoreRequestRules |
| `Wireless1,Wifi5GLMACManuf` | `Firmware/t2026phoneG2/Release/ftab.bin` | `2372fd4b17cc6eef` | Trusted, RestoreRequestRules |
| `Wireless1,Wifi5GLPhy` | `Firmware/t2026phoneG2/Release/ftab.bin` | `d528706af0b66fe1` | Trusted, RestoreRequestRules |
| `Wireless1,Wifi5GLPhyManuf` | `Firmware/t2026phoneG2/Release/ftab.bin` | `d528706af0b66fe1` | Trusted, RestoreRequestRules |
| `Wireless1,Wifi5GLPhyTrim` | `Firmware/t2026phoneG2/Release/ftab.bin` | `c8dac484934f456d` | Trusted, RestoreRequestRules |
| `Wireless1,WifiRegData` | `Firmware/t2026phoneG2/Release/ftab.bin` | `03adb4c5ce95a3da` | Trusted, RestoreRequestRules |
| `YonkersIR1,SysTopPatch0` | `Firmware/Lakeville/YonkersIR1,SysTopPatch0` | `9c7c82fa00263d52` |  |
| `YonkersIR1,SysTopPatch1` | `Firmware/Lakeville/YonkersIR1,SysTopPatch1` | `052b9ec06213a1db` | EPRO |
| `YonkersIR1,SysTopPatch2` | `Firmware/Lakeville/YonkersIR1,SysTopPatch2` | `9c7c82fa00263d52` |  |
| `YonkersIR1,SysTopPatch3` | `Firmware/Lakeville/YonkersIR1,SysTopPatch3` | `052b9ec06213a1db` | EPRO |
| `YonkersIR1,SysTopPatch4` | `Firmware/Lakeville/YonkersIR1,SysTopPatch4` | `9c7c82fa00263d52` |  |
| `YonkersIR1,SysTopPatch5` | `Firmware/Lakeville/YonkersIR1,SysTopPatch5` | `052b9ec06213a1db` | EPRO |
| `YonkersIR1,SysTopPatch6` | `Firmware/Lakeville/YonkersIR1,SysTopPatch6` | `9c7c82fa00263d52` |  |
| `YonkersIR1,SysTopPatch7` | `Firmware/Lakeville/YonkersIR1,SysTopPatch7` | `052b9ec06213a1db` | EPRO |
| `YonkersIR1,SysTopPatch8` | `Firmware/Lakeville/YonkersIR1,SysTopPatch8` | `bf0b187d19186250` |  |
| `YonkersIR1,SysTopPatch9` | `Firmware/Lakeville/YonkersIR1,SysTopPatch9` | `cbb72635c6f3ab38` | EPRO |
| `YonkersIR1,SysTopPatchA` | `Firmware/Lakeville/YonkersIR1,SysTopPatchA` | `bf0b187d19186250` |  |
| `YonkersIR1,SysTopPatchB` | `Firmware/Lakeville/YonkersIR1,SysTopPatchB` | `cbb72635c6f3ab38` | EPRO |
| `YonkersIR1,SysTopPatchC` | `Firmware/Lakeville/YonkersIR1,SysTopPatchC` | `bf0b187d19186250` |  |
| `YonkersIR1,SysTopPatchD` | `Firmware/Lakeville/YonkersIR1,SysTopPatchD` | `cbb72635c6f3ab38` | EPRO |
| `YonkersIR1,SysTopPatchE` | `Firmware/Lakeville/YonkersIR1,SysTopPatchE` | `bf0b187d19186250` |  |
| `YonkersIR1,SysTopPatchF` | `Firmware/Lakeville/YonkersIR1,SysTopPatchF` | `cbb72635c6f3ab38` | EPRO |
| `YonkersIR2,SysTopPatch0` | `Firmware/Glenbrook/YonkersIR2,SysTopPatch0` | `766c1906a4df7abe` |  |
| `YonkersIR2,SysTopPatch1` | `Firmware/Glenbrook/YonkersIR2,SysTopPatch1` | `dd99f434a5980c4b` | EPRO |
| `YonkersIR2,SysTopPatch2` | `Firmware/Glenbrook/YonkersIR2,SysTopPatch2` | `766c1906a4df7abe` |  |
| `YonkersIR2,SysTopPatch3` | `Firmware/Glenbrook/YonkersIR2,SysTopPatch3` | `dd99f434a5980c4b` | EPRO |
| `YonkersIR2,SysTopPatch4` | `Firmware/Glenbrook/YonkersIR2,SysTopPatch4` | `766c1906a4df7abe` |  |
| `YonkersIR2,SysTopPatch5` | `Firmware/Glenbrook/YonkersIR2,SysTopPatch5` | `dd99f434a5980c4b` | EPRO |
| `YonkersIR2,SysTopPatch6` | `Firmware/Glenbrook/YonkersIR2,SysTopPatch6` | `766c1906a4df7abe` |  |
| `YonkersIR2,SysTopPatch7` | `Firmware/Glenbrook/YonkersIR2,SysTopPatch7` | `dd99f434a5980c4b` | EPRO |
| `YonkersIR2,SysTopPatch8` | `Firmware/Glenbrook/YonkersIR2,SysTopPatch8` | `7f2c2fa99478bc52` |  |
| `YonkersIR2,SysTopPatch9` | `Firmware/Glenbrook/YonkersIR2,SysTopPatch9` | `0305ea5727d84fe4` | EPRO |
| `YonkersIR2,SysTopPatchA` | `Firmware/Glenbrook/YonkersIR2,SysTopPatchA` | `7f2c2fa99478bc52` |  |
| `YonkersIR2,SysTopPatchB` | `Firmware/Glenbrook/YonkersIR2,SysTopPatchB` | `0305ea5727d84fe4` | EPRO |
| `YonkersIR2,SysTopPatchC` | `Firmware/Glenbrook/YonkersIR2,SysTopPatchC` | `7f2c2fa99478bc52` |  |
| `YonkersIR2,SysTopPatchD` | `Firmware/Glenbrook/YonkersIR2,SysTopPatchD` | `0305ea5727d84fe4` | EPRO |
| `YonkersIR2,SysTopPatchE` | `Firmware/Glenbrook/YonkersIR2,SysTopPatchE` | `7f2c2fa99478bc52` |  |
| `YonkersIR2,SysTopPatchF` | `Firmware/Glenbrook/YonkersIR2,SysTopPatchF` | `0305ea5727d84fe4` | EPRO |
| `eUICC,Gold` | `Firmware/vinyl_20.vnlfw` | `a9632326a052c090` |  |
| `eUICC,Main` | `Firmware/vinyl_20.vnlfw` | `ac690767d5368041` |  |
| `ftap` | `` | `` | Trusted, RestoreRequestRules |
| `ftsp` | `` | `` | Trusted, RestoreRequestRules |
| `iBEC` | `Firmware/dfu/iBEC.v68.RELEASE.im4p` | `41fa3c2a7d464186` | Trusted, RestoreRequestRules |
| `iBSS` | `Firmware/dfu/iBSS.v68.RELEASE.im4p` | `198d68bff7940560` | Trusted, RestoreRequestRules |
| `iBoot` | `Firmware/all_flash/iBoot.v68.RELEASE.im4p` | `28df03c4dfab963c` | Trusted, IsFirmwarePayload, RestoreRequestRules |
| `iBootData` | `Firmware/all_flash/iBootData.v68.RELEASE.im4p` | `09ec9d198c7d9be2` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `rfta` | `` | `` | Trusted, RestoreRequestRules |
| `rfts` | `` | `` | Trusted, RestoreRequestRules |

### Component details

#### `ANE`
- `Digest`: `64b8d6c628bad1896a23a2a0475db70ec18674967ded0d3dda576bae22c4a7b0bfa73f3d767d0f529b35f045abad7d85`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/ane/h19_ane0_fw_perses_v6x.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `ANS`
- `Digest`: `14d1f7273d1a1d75710ba2f6619d6842d0e504bf83ccf3375d30036d65420772141b6041fa23b9d7025f8bba1c64beaa`
- Info `IsFTAB`: `False`
- Info `IsFirmwarePayload`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/ansf.t8160.release.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `AOP`
- `Digest`: `a8be918779ae2c1ddb8fbbb6d1d4db0535ab13121086d13e203a7defb7c1e5a16caafdd27a592beead05ac9c116fae74`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/AOP/aopfw-v68aop.RELEASE.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `AOP2`
- `Digest`: `abfbc6dc12c26f5c1587439022847317fa3895b8101e27bfd65913817d5360c8537aae8f5709db99b76dd6f7d25fe7df`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/AOP2/aop2fw-v68aop2.RELEASE.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `AVE`
- `Digest`: `b9030e94822ebb2cbf6f221c75ff0ff8104dd40ce0261813ff9a001f165b9b24e6778b3796ba10db64e05da16b861d61`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/ave/AppleAVE2FW_H19.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,ANE1`
- `Digest`: `051c0dc0bb17eed9933ff020d30d8d8e1d7c1570c6eb091de7164ae582f2ce5b1d0c467b497a867feacfc622cf2f905d`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/ane/h19_ane1_fw_perses_v6x.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,AVD`
- `Digest`: `a580555ba355aca0584aeb5fcde3c494cd965a9ad11abb6a435fd61dee77c8b156c92282247139e17f097c4308f063df`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/avd/AppleAVDFW_H19P.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,ApplePMCFirmware`
- `Digest`: `887e53baaf9f25ad1ef1fd97b1287cd2f195a5ad72b40af70585d943da1e4ba075f02d5cabbbe824774639566caa04cb`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/pmc/t8160pmcfw.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,AppleVideoEncoder0`
- `Digest`: `63e41e5d2bfa0328dfab9db0ffd464622575062c0622fa4732de2cadf58b273c7734f697cc9d1c1e056a7d5cdb107ff7`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/ave/AppleAVE2FW_H19_AVE0.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,AppleVideoEncoder1`
- `Digest`: `049e3519a25033b3033a130df46585b0f2f05555985fd3b0a8654b332f164cd49daf6b2384328906940a7f7a201a1585`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/ave/AppleAVE2FW_H19_AVE1.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,AppleVideoEncoder2`
- `Digest`: `19c0e781fee7cba72045d9ed90dc29c2c7101116685a6168d1dba6f9585a8a8c612d6e8e6bb87f601c12929109898358`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/ave/AppleAVE2FW_H19_AVE2.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,AppleVideoEncoder3`
- `Digest`: `5e1206584755555f9b4c6e3334f4c6c0bca650be8a53f5dd1448a629ff37e60e385bf54335e8b235edc8d3a848ba7e51`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/ave/AppleAVE2FW_H19_AVE3.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,AppleVideoEncoder4`
- `Digest`: `1adac89457306494c8b20c71d04df9ce5251241dd9e34395a8fe4453da82e673024dfd7c5b79cddd2c00af877f98d3be`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/ave/AppleAVE2FW_H19_AVE4.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,AppleVideoEncoder5`
- `Digest`: `63ff7021a0e26aab0bfe4e02ea3fa4925ec892b97dabaa21e8dd549a2aca1a80b7f420e0efbedec143fbbcf3cf6fa2f8`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/ave/AppleAVE2FW_H19_AVE5.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,AppleVideoEncoder6`
- `Digest`: `e62efe0891fc91f53f25b0772008b96d61d83d425dada746baac8b25990eaaf79b92af27a1ab38e2fe8605311d3bd863`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/ave/AppleAVE2FW_H19_AVE6.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,AppleVideoEncoder7`
- `Digest`: `223eda99b6bace8b6acbedbe0bbe4e38700ce20d666597e37fe57d1ad2e30ff5ad169fa5dce78661dc8a3c36d843fc20`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/ave/AppleAVE2FW_H19_AVE7.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,AppleVideoEncoder8`
- `Digest`: `05f79bc85c0600aa2c26f9fc3d8e0496d67d618a71ff4f01d880fd2dfdd3158d10bcbd183f55fb148e0c5b6f72b3242c`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/ave/AppleAVE2FW_H19_AVE8.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,AudioBootChime`
- `Digest`: `9e584ad82b3787c6e8f16678b959c331d48ccb5983f16216999b057bdbc6def30f8ba8bf0a050b4b385264452a3cba1e`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `True`
- Info `Path`: `Firmware/embeddedaudioresources/image4/v68-boot-chime.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,ExclaveOS`
- `Digest`: `e5068d05578a3d9ee1755e0db9618cbf326b558f2a467f1276364611a902f24f97e1519d5c46a30bbb052dfa22a9fda4`
- Info `ExcludeFromiBootSystemContainer`: `True`
- Info `HashMethod`: `sha2-384`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `141-27521-104.dmg.aea`
- Info `Personalize`: `False`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `Ap,ExclaveOSIntegrityCatalog`
- `Digest`: `414d318f25032cf9b4dfd74c45adcd3850dbf56ab847f55a70555d838a5455bd16d25b60f411a32d40838c8395556160`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/141-27521-104.dmg.aea.integrity_catalog`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `Ap,ExclaveOSTrustCache`
- `Digest`: `c11c6fe006449290640ff32a684eec66ec45fa2eba567206fe107e1980b71f4d831ba16df62ed1e734746c0e7b88e9d4`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/141-27521-104.dmg.aea.trustcache`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `Ap,ExclaveOSVolume`
- `Digest`: `e7d273a37772bbb870896c3bc97d83e21f848e762f6a2846254b2309924334ea8e8c029834308e5513e548d075826468`
- Info `ExcludeFromiBootSystemContainer`: `True`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/141-27521-104.dmg.aea.root_hash`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `Ap,GFX1Firmware`
- `Digest`: `33febef5d5a228984d2603f89e1b9ef78dfaae91d0167ae0fdaeb147a20c9ff25b1a79fcbdd1620384b95f1a43bbe0ad`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/agx/armfw1_g19p.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,HapticAssets`
- `Digest`: `9a85fd4f0a9f365ea646340f7ac597c0d39979d9c2a4cbb2ccca79ff81c5cc861a62d9e7ae53a29b71f183af3513ca38`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/V68_HapticAssets.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `False`

#### `Ap,LowPowerMode`
- `Digest`: `d72c01b171d40df1890d463dfb2b5911d53ecd66901f1606a1829767014c90d5cb0ae63c53fffe00bae7c45b2c2a9942`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `True`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/AppleLPM/AppleLPM.v68.release.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `False`

#### `Ap,MSRFirmware`
- `Digest`: `6c2611f3e8b5eaed277fce91ace8673d74e8dab2f938b8c80b72e4cd1ebe091e4c953c06330499553d54ac4b3de4045c`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/msr/t8160.msrf.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,MandoFW`
- `Digest`: `44624f1ad5411cbe0b5805b174c5a05dbf77bbd4d267f8eb2bd318d5364c3e3a0d96c1359f8850dc486141e7789cdaa3`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/V68_MandoFirmware.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `False`

#### `Ap,RestoreANE1`
- `Digest`: `d88874b6f35f6d3ff66e6918060c7ff1724aa8de5126e5665a5e204fe60786c2a565f900e6f36d97731aac4d8d8152e1`
- Info `Img4PayloadType`: `ran1`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/ane/h19_ane1_fw_perses_v6x.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,RestoreMSRFirmware`
- `Digest`: `4594142c48d515ef3d986a85fdf1d8c16ff030de561b578328f58b08850ae8544c0d25b4005c734686b586474034837f`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/msr/t8160.rmsr.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,RestoreSecureM3Firmware`
- `Digest`: `f4a3ee30ac0b966c872be05e9cf85b784a8363473952bff011c4d131ffae982fce7eb3d6ffbc7206c1545baa76f6ad75`
- Info `Img4PayloadType`: `rsm3`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/M3/bin/securem3fw-v68.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `Ap,RestoreSecurePageTableMonitor`
- `Digest`: `c9e66676240d53abb09022bb1d63972ba82a49ae7edce2a118174fae514e58adf4ef8bdf5d1015047dc29c42eb974c1b`
- Info `Img4PayloadType`: `rspt`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/sptm.t8160.release.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `Ap,RestoreTrustedExecutionMonitor`
- `Digest`: `75371b6d03b94162e4e95077067ab36dc4eb92ddbc78574be819b79ebd2399e816ae4416c995e01d597376d729f5a0a1`
- Info `Img4PayloadType`: `rtrx`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/txm.iphoneos.release.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `Ap,RestorecL4`
- `Digest`: `f7846005a0bfd5a07116a05cb9084b8bcd58b56e593e95d5d6a94db71329dbcc9b64adc70b1174d100c7c75bed413baa`
- Info `Img4PayloadType`: `rxcl`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/image4/exclavecore_bundle.v68.RELEASE.restore.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `Ap,SecureM3Firmware`
- `Digest`: `9b9075693ce1ecd88a4952a1529681d9d13412933cb63079d4873bbd510813d422adf8d241617bf139651447372bfbcd`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/M3/bin/securem3fw-v68.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,SecurePageTableMonitor`
- `Digest`: `2f69cb8b9dc4932ffbb28f4bf7ce6712b46e8d3a90367255646779b94aa28895cd6220da5884f6d5dea8715e8b91f737`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/sptm.t8160.release.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,SystemVolumeCanonicalMetadata`
- `Digest`: `5d99f6cc85a80b45ee2e2269ffc9de71339b5cdd1fed01519af43c6baefd2250d44c4f21f1bb99c93002e76fb42ec0af`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/141-28898-095.dmg.aea.mtree`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `Ap,TrustedExecutionMonitor`
- `Digest`: `e9f0a0a9f060553dcba6de84e0cd4b70c381bf3a174168282843fc12cd01509d6071e6286a13022652cfab95189c3c5b`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/txm.iphoneos.release.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `Ap,cL4`
- `Digest`: `c52af32219d872a04f421d10a74e181601a049a4611a906e687807e355102e1085d61892f5e0d0a9750ce56b4ff76863`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/image4/exclavecore_bundle.v68.RELEASE.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `AppleLogo`
- `Digest`: `72e55666b43d92ae01875414c1a25d8809ccde5b720b7d42749d6d3bcda2031bd48561b7a83ebaa4da10299bc2e62634`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `True`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/all_flash/applelogo@2d~iphone.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `BMU,DigestMap`
- `Digest`: `a217a7c58314ae739da9a12c9788affb98ee223a5774f5863d49a071c11cbad6`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Volchok/BAT8193/DigestMap.der`
- Info `Personalize`: `True`

#### `BMU,FirmwareMap`
- `Digest`: `b87e189151c508daaf1029e9dd2a558bb292b9ffa98fc0b1c2a859ba139d3bd5`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Volchok/BAT8193/FirmwareMap.plist`
- Info `Personalize`: `True`

#### `BMU2,DigestMap`
- `Digest`: `a217a7c58314ae739da9a12c9788affb98ee223a5774f5863d49a071c11cbad6`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Volchok/BAT8193/DigestMap.der`
- Info `Personalize`: `True`

#### `BMU2,FirmwareMap`
- `Digest`: `b87e189151c508daaf1029e9dd2a558bb292b9ffa98fc0b1c2a859ba139d3bd5`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Volchok/BAT8193/FirmwareMap.plist`
- Info `Personalize`: `True`

#### `Cellular1,CdpAscDl`
- `Digest`: `9bb48fff8021c91f3f9ce98a38c19ef89399272bcd487c6a6b4bcc777b1dda566e59fb74d2d8089462bb843b1babb0ce`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/c4020iphone/Release/patched/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Cellular1,CdpAscUl`
- `Digest`: `c0e59a3e3ffbd3b5c75428fb36432facabc745944296ff515f737c4fef4efc64586809f7a16f56354a1eaecf2aa8d774`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/c4020iphone/Release/patched/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Cellular1,CdpHost`
- `Digest`: `8d30be1ec9e53237500b942bdabdd2477b6f3337c86a57053e3b2ed5be37baf8cb40b0c8882f5d8a6bc3cc0c38735de9`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/c4020iphone/Release/patched/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Cellular1,L1CL1S`
- `Digest`: `46e0cdcb8acbca7a0ce1ea1672227796130091b7abe75f5fa14d430f370edd93d8b434a7e7df09012657b589b43a7081`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/c4020iphone/Release/patched/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Cellular1,LLB`
- `Digest`: `162f084d64d6ba1ea7d26fd9a94362aa914ac87f0b55b27f5ef35fc6a083666319dd15a3d8748ed32d85ea54787f2d05`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/c4020iphone/Release/patched/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Cellular1,PMUFW`
- `Digest`: `33e1a57e7ba21e87c045b6f85a1fbe1732285f7151962cf6c3cd3f83dbe45745cf2ed60ed5e266851b6d0b1dc733f541`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/c4020iphone/Release/patched/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Cellular1,PMUFW2`
- `Digest`: `024bbc34f73996a33ab5b2e39ce36b158fb336f8d7cd7b7027e2c0ace73bb004c53cb948b03df45f8ef31de51041fe88`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/c4020iphone/Release/patched/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Cellular1,RTKitOS`
- `Digest`: `9ccde882d2e3679418efc6f95b12e7d77d16081ecc9432dd510519cd5f6d773cfbdffee5fc6fe0505cbc6677b1e83e54`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/c4020iphone/Release/patched/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Cellular1,Recipe`
- `Digest`: `e7cb1b15c3717f42a127a35b5506d720f2d58971e781cbe731c87cc96aac422973337922eb80e5ed6695501c35d8168d`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/c4020iphone/Release/patched/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Cellular1,iBootData`
- `Digest`: `45b76cdcd9e32532b492018443e65eb3757a404c02555e76ccb4722eaa69130d76e1d7bba88042f3cf9767e48857df7b`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/c4020iphone/Release/patched/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Cryptex1,AppOS`
- `Digest`: `87f11143323631088cb240ce81efea1106fc9d365f56fb41be851cdf28730b560680cd65b9a3e16e87a99c7604390f22`
- Info `HashMethod`: `sha2-384`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `141-28395-106.dmg`
- Info `Personalize`: `False`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`

#### `Cryptex1,AppTrustCache`
- `Digest`: `7072d57c04de1ffdcddabf6f3e65d8ce2099f2f22245369ccb56c7c3b7432359e5e108f54cd423d4358266db667110b6`
- Info `HashMethod`: `sha2-384`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/141-28395-106.dmg.trustcache`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`

#### `Cryptex1,AppVolume`
- `Digest`: `e3a31ede1b5fdbb0926a736bbf51e45869f925f57ac839fecb3192a8d5ba5c9c8194eee786baa64e8fb74e3945bc11a9`
- Info `HashMethod`: `sha2-384`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/141-28395-106.dmg.root_hash`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`

#### `Cryptex1,SystemOS`
- `Digest`: `597a37020cb5123afbcbf78f749f4b8e1a6fba94e7dc22322495728c9a2ad9070bf4a7307e7fc9a1c30a6073678758a6`
- Info `HashMethod`: `sha2-384`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `141-28400-098.dmg.aea`
- Info `Personalize`: `False`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`

#### `Cryptex1,SystemTrustCache`
- `Digest`: `fa1bbcbdaa387a71ba17cae7d6d3dbe846aa4e8835ca047e3b0cbf2e7e742bdc1bff9bae1a10e879d6eaf8374d3fd181`
- Info `HashMethod`: `sha2-384`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/141-28400-098.dmg.aea.trustcache`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`

#### `Cryptex1,SystemVolume`
- `Digest`: `9bfa3a33afdde3318fbf044538eb669b8f9a2f20b4c5bed0028249cc1b565377b8df1e6d48e027b151ebb5cfd0037d99`
- Info `HashMethod`: `sha2-384`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/141-28400-098.dmg.aea.root_hash`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`

#### `DCP`
- `Digest`: `aefaf09c5156cd037df5a0213fe1eb1e797cf3b68d1fcb7c8c300eae33eddbaf1b387379ee4a76049fe5acf9304253f4`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `True`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/dcp/t8160dcp.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `DeviceTree`
- `Digest`: `a3b521b47aa0f0540ac943eb5afab35b123789358cd16b74e394db195fdbc000bae4adb8b3e2c06b9555034e86269f76`
- Info `IsFTAB`: `False`
- Info `IsFirmwarePayload`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/all_flash/DeviceTree.v68ap.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `GFX`
- `Digest`: `40c7cc60cbda687879663afb4c02f0293531e4a372e5247a2d986276853a7ae2f5f5887e5e0dd0359bb194696c894cf1`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/agx/armfw_g19p.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `ISP`
- `Digest`: `33b6bdc438ecbe1bdfe93f88700d230813ffde3943f1df799a4d69a1ea36b6b2bea61ee51ce971cc578624668eeebc9f`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/isp_bni/adc-boreas-v68.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `KernelCache`
- `Digest`: `9f57d7cf359fc7671d295630bb82f9909ead4c9f41b80b34e8248f3519de737e29c5e1069e48d40d49772b389d176201`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `kernelcache.release.v6x-pandia`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `LLB`
- `BuildString`: `iBoot-15391~1757`
- `Digest`: `302b40b9dbf4070bb0fa4e4215b222b81ad70b1557a03e354f057e3bac40c3136d707e6734924b3456312a8e767631bf`
- Info `IsFTAB`: `False`
- Info `IsFirmwarePayload`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/all_flash/LLB.v68.RELEASE.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'DPRO': True}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductionMode': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresIm`
- `MemoryMap`: `6480728002000000040000006880728002000000040000000801051102000000080000003002e4110200000008000000f849e4110200000008000000000005110200000008000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000`
- `RawDataDigest`: `2e62b37b6485cc3814fd1cfda528062cac98afd2cb365a23fc5b5a76231ae832f73c74e64b5f17f17195d50d6591a698`
- `Trusted`: `True`

#### `LeapHaptics`
- `Digest`: `8afa6138a6d3be9b7fc121d0afefabd41330555a8a3b4915200b9c804531b6238ce070122ba5e1c9632135165738e065`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/V68_LeapHapticsFirmware.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `False`

#### `Liquid`
- `Digest`: `194aaed667db6adaa64d1c9250667a24bf0fb8b94939256a3bbf3958681d7fbd444416e5eda5617964221cc64feda25d`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `True`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/all_flash/liquiddetect@2d~iphone.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `MtpFirmware`
- `Digest`: `270a440ad64cb8582dc2cfef143d513b2a3714afa8c690b2bf2f568fdd31271276ed120cd549dd6997a2020feb3bfe77`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/V68_MtpFirmware.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Multitouch`
- `Digest`: `7368509e073e8c3bbe4f93e101879b48e0f1b3b044038976d643093f87378ccfe88ea58cc6e5afe26933ca94acf4c477`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/V68_Multitouch.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `False`

#### `OS`
- `Digest`: `b1d8bce0e16a7548ac7f3e6a243720965ef8461eda3034e0ea8eaef38b9676d6499b46e6dba99c3f109a8206133480b9`
- Info `HashMethod`: `sha2-384`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `141-28898-095.dmg.aea`
- Info `Personalize`: `False`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `PMP`
- `Digest`: `19008a2bc4a04e1b7ea69fd82e585ea96246e5e3a6ad8718ae0ad9bec05521fbf7770b62c26f1263f1b5a59cf0c4af4b`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/pmp/t8160pmp.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Rap,RTKitIOConfig`
- `Digest`: `6b1013023f1c7479108eef02f6d78f03113b687efbcff90b17d9beca0445f96b0ebac5630f6599b54d3d8e63d164f364`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Rose/r2p1/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Rap,RTKitOS`
- `Digest`: `e46b5fd033a4a73604477ece10221dc011355e265d12086c4a9bdde103094b9c0f89c516bc92f4744660bd66f2f408ef`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Rose/r2p1/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Rap,SoftwareBinaryDsp1`
- `Digest`: `7300dc26d19b540e06204e17e2c34cec3eafc3759cd12b22eac0e14e45d64fd53a38a436a009aece07836f0da32e8446`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Rose/r2p1/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `RecoveryMode`
- `Digest`: `848e2e1ba471a38985b09e96b375b4dc812e101f29b1a109887ae1f46ec41648d11da5a2493434ec091e33c72fbd93df`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `True`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/all_flash/recoverymode@2d~iphone.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `RestoreANS`
- `Digest`: `c60c3b84b45ea4f06c28cbd059377d2ba69f6afce9558d7e578483e45291ddc489b452ff3fcc8a0c98ed5b4306a7bd92`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/rans.t8160.release.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `RestoreDCP`
- `Digest`: `39063050c7616fc6ee7b1dc3b3a1d7ddf8d33f39ca3be62f1fe20638f51f07349463e777a9cdbb944d9afd3d83fbf5fe`
- Info `Img4PayloadType`: `rdcp`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/dcp/t8160dcp_restore.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `RestoreDeviceTree`
- `Digest`: `94cbc3d7c32dfcad8107dca33a68d57d63eed74e57941dde950f8685e5437107e60c664cbdceb25a22a5bbdda95e4ae3`
- Info `Img4PayloadType`: `rdtr`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/all_flash/DeviceTree.v68ap.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `RestoreKernelCache`
- `Digest`: `14a743b0cc147a9480dea7708fc3e5310fa89174656296649188e59c40ca531f44b870ed2b795522fcd6bdc51298b06f`
- Info `Img4PayloadType`: `rkrn`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `kernelcache.release.v6x-pandia`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `RestoreLogo`
- `Digest`: `0f7534a7d9c2761a6401e49ef5d826178a7254f6c052c7cde5d99bdba1cbfda71a304e5d43bea1a7b17812975e9b487e`
- Info `Img4PayloadType`: `rlgo`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/all_flash/applelogo@2d~iphone.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `RestoreRamDisk`
- `Digest`: `2d09674fd3181693644bc53f037b38fd0fd4e683c86d8f8c2cbd5bec2984cf6af5f9a3beedee505d87c50f72f19e79e0`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `141-28940-105.dmg`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `RestoreSEP`
- `Digest`: `6333efcf0bc6eccfd1b3e879911304bea043d007be0446167aa3cc666598b605e52ef185c48418fa91fa8bcca28939bf`
- Info `Img4PayloadType`: `rsep`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsSecondaryFirmwarePayload`: `True`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/all_flash/sep-firmware.v68.RELEASE.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'ESEC': False}, 'Conditions': {'ApRawSecurityMode': False}}, {'Actions': {'ESEC': True}, 'Conditions': {'ApRawSecurityMode': True}}, {'Actions': {'DSEC': True, 'ESEC': False}, 'Conditions': {'ApDemotionPolicyOverride': '', 'ApRawProductionMode': False, 'ApRawSecurityMode': True}}, {'Ac`
- `MemoryMap`: `000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000`
- `ObjectPayloadPropertyDigest`: `2b8d753529cd508e1a554eed82d7b8dafdcc64736a007453938f23006f0d51139bb0e78ea1f99a0233e4d37b891e9d16`
- `RawDataDigest`: `ce336e482b48402ee816475232d12e9a6dbc7aa138256a1efc2aef36cec5830d8b164d96bd716fb678f0f8be43765611`
- `TBMDigests`: `07acf0061948b097cb65709af43c70f06b51ebc4ac35905ad9bd52f00bb02524a58c0a8cae32e368597b52ec792fc26de436b7988ddffd36523ddb679caa2cc3538088049388d679fa143b955a5e1285afea75c9f0aa0ad9c3dc3f2922d2ad577ea975d9c01166af949d66fb105444985d79af4bb62dc566aaf1e9e7a6928981023268b752cbfb587e97b0bb865c426d95045524af0a75f4e0ee1ddaa192ddb909c91195ae0c269dca390d4d145b2afae46d3c62df4fc9a016a1b04d1ed79e69fc15c98b9e86190f354c80102ed5d06f4c1215853ae50ece2538fd90686ee25a5e7587ac428512b248c64b417306d272`
- `Trusted`: `True`

#### `RestoreTrustCache`
- `Digest`: `c0b105973b887ac4806aa2c6eae8f62ad026525842c66d188ccc38e6d34b77d008953e7222db23ad2d3cd820b33081bd`
- Info `Img4PayloadType`: `rtsc`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/141-28940-105.dmg.trustcache`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `SE,RapRTKitOS`
- `Digest`: `e46b5fd033a4a73604477ece10221dc011355e265d12086c4a9bdde103094b9c0f89c516bc92f4744660bd66f2f408ef`
- Info `Img4PayloadType`: `rkos`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Rose/r2p1/ftab.bin`
- Info `Personalize`: `False`

#### `SE,RapSwBinDsp`
- `Digest`: `7300dc26d19b540e06204e17e2c34cec3eafc3759cd12b22eac0e14e45d64fd53a38a436a009aece07836f0da32e8446`
- Info `Img4PayloadType`: `sbd1`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Rose/r2p1/ftab.bin`
- Info `Personalize`: `False`

#### `SE,UpdatePayload`
- `DevelopmentUpdatePayloadHash`: `fdb79271bb26f2f490782b97a01621656e291e612bba82a0d51c070963ee90a1`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/SE/Stockholm91.RELEASE.sefw`
- Info `Personalize`: `True`
- `ProductionUpdatePayloadHash`: `40e6ac72e7665b06e7633ee692ed9d8a838f18ea4af387e15dcde09c62bfd4b5`

#### `SEP`
- `Digest`: `a4e4c8fcba2b9a783553d195a2f3addc07d62cd1dc56896aa8f0d8f82e5c84588e40391f3a356ae595b85cd060e3c248`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsSecondaryFirmwarePayload`: `True`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/all_flash/sep-firmware.v68.RELEASE.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'ESEC': False}, 'Conditions': {'ApRawSecurityMode': False}}, {'Actions': {'ESEC': True}, 'Conditions': {'ApRawSecurityMode': True}}, {'Actions': {'DSEC': True, 'ESEC': False}, 'Conditions': {'ApDemotionPolicyOverride': '', 'ApRawProductionMode': False, 'ApRawSecurityMode': True}}, {'Ac`
- `MemoryMap`: `000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000`
- `ObjectPayloadPropertyDigest`: `2b8d753529cd508e1a554eed82d7b8dafdcc64736a007453938f23006f0d51139bb0e78ea1f99a0233e4d37b891e9d16`
- `RawDataDigest`: `ce336e482b48402ee816475232d12e9a6dbc7aa138256a1efc2aef36cec5830d8b164d96bd716fb678f0f8be43765611`
- `TBMDigests`: `4f9b357da6a251c413dfa30c0f7fb382260b1fdc311e0321c8c78d04512375e8bf46103d787a27cf8695f8843ea068e3fcd750bba68cd7b510f27de03d8636a1a727f00fac5fb9ba7d96306c1a0bdfa11f89ba3375c61b26a1d6c3e07191341558f63c8c1bc13dd68862b47353fadea69364c5b9696e14c65ee250142655fe111685e9fce6f35863eac15db5df9d2101ec14a7658b5760e7358aad4598926a9fe1634914815278410007db1b8fb5d19842c763c6cc2941413fef7c3f5a92ac1c71c3fd355821d378b011d7d0184d64e98292be2737f951ee6d48dfc229481ec53300fb6cac73324f97cf1be7697a2647`
- `Trusted`: `True`

#### `SIO`
- `Digest`: `8873ba2b293fc1144f3fbc9780492ffea17cbac9c3ab5b182ce19ec789d6b75a2b2e3c603dc135bfda6cd21ca3ee7344`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/SmartIOFirmware_ASCv8.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `SepStage1`
- `Digest`: `58a738a8ef5bbc8b36b56d9637cea87db2c6f54634de65755eb9ad4f9d7cb4dcbb80eb0d6e8fb0b15a3ec7b975feb35c`
- Info `Img4PayloadType`: `stg1`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsSecondaryFirmwarePayload`: `True`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/all_flash/sep-patches.v68.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EnableGid0ForNextStage': True}, 'Conditions': {}}, {'Actions': {'ESEC': False}, 'Conditions': {'ApRawSecurityMode': False}}, {'Actions': {'ESEC': True}, 'Conditions': {'ApRawSecurityMode': True}}, {'Actions': {'DSEC': True, 'ESEC': False}, 'Conditions': {'ApDemotionPolicyOverride': ''`
- `MemoryMap`: `000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000`
- `ObjectPayloadPropertyDigest`: `5242f6de7bceb54f81e79d072c7b12bb8d74235561af15029d720cff3fa6a719c96a9e5900b5f279ecaa39c2f16d9034`
- `RawDataDigest`: `5eee7fcf6e3c9c425834179d18c809cd4cc31a863170f350332938ac15bbb8b50e28e92f552cf3b9007bc101f4e35199`
- `Trusted`: `True`

#### `StaticTrustCache`
- `Digest`: `f9fd4c9b274ca337a1c1c0864f6b42bc62e570149d14fcd60d9a8702c1330656974d2fab9554ebf7300aa2d9ef84500f`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/141-28898-095.dmg.aea.trustcache`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `SystemVolume`
- `Digest`: `23684e5cf582fcdde50c305d64f0510f0f608b7128edd7386937636e933f399ecb35e51db91374af4c8aba3c14fe1944`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/141-28898-095.dmg.aea.root_hash`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `WCHFirmwareUpdater`
- `Digest`: `ee119dfcfbb36a8e300f3c169678af57a6dd2328bd5c1368ee4bf285208d20a452246acd87bb4dea7b55b44c4d45287b`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `True`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/WirelessPower/WirelessPower.v68.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,ACIBT`
- `Digest`: `51c01d433c414fa22f7769dad787f55f3fd2de1e308607402da015d423ef5bc0929a525f4d7038d20349509749573d50`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,ACIBTLPEM`
- `Digest`: `1f9a194a2e7aaa3825af77a23dd7f71d6e6b05a94f2aa181d653a885c6c09b3291a3adcc4d6a30ce9a455324dc88f97c`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,ACIBTManuf`
- `Digest`: `51c01d433c414fa22f7769dad787f55f3fd2de1e308607402da015d423ef5bc0929a525f4d7038d20349509749573d50`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,ACIWIFI`
- `Digest`: `902b5adeacd5144fb149f7b3d87c64b0ef7276c13cb92cf7e8e73d4f22ba743dd73f0b920f539e0bfb95ab3f4e3bcbb1`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,ACIWiFiTxManuf`
- `Digest`: `36423b324369661e34da69383f486a7f30838e99a7f7756d74254ecbdf951ca7397ce33d96e05b4dc0d2f590def4c66a`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,BTSecondary`
- `Digest`: `ebd59be4d27b01a4e1a696feb77a6aa10a75087f609efaff2e0f0ce3215113e74b0de656ee29eb9835d6a751b11ae931`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,BTSecondaryManuf`
- `Digest`: `ebd59be4d27b01a4e1a696feb77a6aa10a75087f609efaff2e0f0ce3215113e74b0de656ee29eb9835d6a751b11ae931`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,CCPUApplicationFirmware`
- `Digest`: `45f576ce687be46effa69e4d48584543abe24bb1684e137fe2ac3a307828c0e9024302bf437530d5f1c3c4dc99ab2eea`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,CoexRealTimeArbiter`
- `Digest`: `44749c87da9b89c1e09056d09de81bf1bcc7125480a78db8424e9583d5be8df4f861c9d31813a8c1806398d0c18941ec`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,PhyBlueTooth`
- `Digest`: `181d64d765b57b4e3167ce24151b847f99c713b84bd75abe67708f2abbc66be9a0b1c2ac6b97733ff0132732efa9040e`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,PhyBlueTooth5G`
- `Digest`: `8c0742a5e9ad20e1254c7355de8386dcb335305c0977edbdb3778c149f063353713f8004479930c0b81f44f49b1f3e02`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,PhyBlueTooth5GManuf`
- `Digest`: `8c0742a5e9ad20e1254c7355de8386dcb335305c0977edbdb3778c149f063353713f8004479930c0b81f44f49b1f3e02`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,PhyBlueToothLPM`
- `Digest`: `b0b972453c81fc0327ead8a21c73630cb4d516ee0f7d542181bef7493f68f956da73d4174dd40b41faa2138cda04739d`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,PhyBlueToothManuf`
- `Digest`: `181d64d765b57b4e3167ce24151b847f99c713b84bd75abe67708f2abbc66be9a0b1c2ac6b97733ff0132732efa9040e`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,PhyBluetooth5GTrim`
- `Digest`: `94c974402ac11c7180cb8b14686c18ec353565b2590ce8a709a5cd5d6c26e6b94f24950c03d623e037cecc3d9e582b50`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,PhyBluetoothTrim`
- `Digest`: `3820e32dc8f92bf00be0cc9eeda45317d7f37d600236bd0e1f54a993f1e5d87d6094b4536f56a3ac75179c33fb9505cc`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,RTKitOS`
- `Digest`: `8219626cc42aae1765e87b3c3f8034530f66a23bc1fd3bfdeb69b578c14e78590daec9c28d75c5b9f917f1aacdd68cf6`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,RTKitOSLPEM`
- `Digest`: `be6863c3d47047bde6b35529fa3f3d9eb88b4678531ef6cf7966ffb85b6fc8408b12a745b7ad07f30f8898ccd073cb4a`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,ScanBTLPEM`
- `Digest`: `3c449b8c373522b5025c3161008797cd14cb0907d29e7ccf521ac55a2085553801aebd1545557fba6700a8c7149407ae`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,ScanBTManuf`
- `Digest`: `f890cbeafa0ccbeb427962f17b48f603feff8561172a98d231ed8205e81e30146f04df9e096776d80dafd3d347a53cbd`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,ScanBluetooth`
- `Digest`: `f890cbeafa0ccbeb427962f17b48f603feff8561172a98d231ed8205e81e30146f04df9e096776d80dafd3d347a53cbd`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,ScanWifi`
- `Digest`: `14f68624a65887fa965c6ddf6d01b2b1027db493a891ddcef52454f1a8939ddcfcb7d1d668e857d9353a344de6275289`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,ScanWifiManuf`
- `Digest`: `611a45ae78230635ae909126967e6783cd39e6bda0c3e28d5e87360bc1144756308a86c1b18574652053b727c0b482c1`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,WiFiRx`
- `Digest`: `00751f9522d1e2e3a2b5684278fb36ff6925949b46e878efd797cfde49c32cdb7286856a7ead45383646538e1a487294`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,WiFiRxManuf`
- `Digest`: `43b50d30fed4c6befc3704b461841679cd339fdd85fa06d8a28fe08b83f13ade2a7a8de0c0d1957f8febcff31a0ee3c6`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,WiFiTx`
- `Digest`: `b28a762c0e1d7d947f2f728c3ea45afe5940eb0785f2f10689c17fc23c5fa40cbbec821fab3673637ae1da9f340253b4`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,WiFiTxManuf`
- `Digest`: `da7ad47bb37867fc46f85ebff1f2d02204382ad199efaed984d7f433165cf0377c83afce9477707cd7bb04a584bb238e`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,Wifi2GLMAC`
- `Digest`: `2d0a90a6fcd00801a8381b3111cc4b15ed9e9093de81c6b9dec26025466376bea66f53ebd7112161dfce217b69f01315`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,Wifi2GLMACManuf`
- `Digest`: `3e72c8dbb12e0c77dca7685815aa628373702b63d5b2155e44fd1152f0f560706d38bd019f3ad3b70ffe51a27d3e1566`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,Wifi2GLPhy`
- `Digest`: `847eca454fc4f9f4970ecec9b1fe41dc2649a1ebbfac48747a432a484089f94f300cd1381bce6e186a2802a144d0c28b`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,Wifi2GLPhyManuf`
- `Digest`: `847eca454fc4f9f4970ecec9b1fe41dc2649a1ebbfac48747a432a484089f94f300cd1381bce6e186a2802a144d0c28b`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,Wifi2GLPhyTrim`
- `Digest`: `afc1e501998b0b550ca0f2ea81ac94a37fde226bff043a61eb0f1178575f68da86197e0e667374855cc77a70cd5f78d7`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,Wifi5GLMAC`
- `Digest`: `bedce67d68535076b21cb535a67e61eec4bcfc95637a395f465a2cbafde3b987dea3cc3c9c41ccb56c2020daefd6de66`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,Wifi5GLMACManuf`
- `Digest`: `2372fd4b17cc6eef67f8281125fca7f57a75a36ab005a568763a40defc9cdaa88deb0290a3a7158a5d9e0068e134189f`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,Wifi5GLPhy`
- `Digest`: `d528706af0b66fe115912d7bba9185a176d41b4eddda8e09b107d78d652eecb98a4b38cc0c671d4a068d0ff142ea1d4c`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,Wifi5GLPhyManuf`
- `Digest`: `d528706af0b66fe115912d7bba9185a176d41b4eddda8e09b107d78d652eecb98a4b38cc0c671d4a068d0ff142ea1d4c`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,Wifi5GLPhyTrim`
- `Digest`: `c8dac484934f456d998a8d7438c0d577ea2e660e81330fff47a7497558de462c3a594557c00e652eb30a4e90ba64fa3b`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,WifiRegData`
- `Digest`: `03adb4c5ce95a3dab17572b4c73dfcdbdacef0ab31f6f98372f7356ac38eb839e65f69469fa78b685499cfadf90414f2`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `YonkersIR1,SysTopPatch0`
- `Digest`: `9c7c82fa00263d5265d6210eec68223618fa474ab5f02e2ed635e770d10a5ce3`
- `EPRO`: `False`
- `FabRevision`: `49409`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Lakeville/YonkersIR1,SysTopPatch0`
- Info `Personalize`: `True`

#### `YonkersIR1,SysTopPatch1`
- `Digest`: `052b9ec06213a1db74d7e45917d9bbf1d41b487eb647f3e14032ed1b37a2c1bf`
- `EPRO`: `True`
- `FabRevision`: `49409`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Lakeville/YonkersIR1,SysTopPatch1`
- Info `Personalize`: `True`

#### `YonkersIR1,SysTopPatch2`
- `Digest`: `9c7c82fa00263d5265d6210eec68223618fa474ab5f02e2ed635e770d10a5ce3`
- `EPRO`: `False`
- `FabRevision`: `49473`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Lakeville/YonkersIR1,SysTopPatch2`
- Info `Personalize`: `True`

#### `YonkersIR1,SysTopPatch3`
- `Digest`: `052b9ec06213a1db74d7e45917d9bbf1d41b487eb647f3e14032ed1b37a2c1bf`
- `EPRO`: `True`
- `FabRevision`: `49473`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Lakeville/YonkersIR1,SysTopPatch3`
- Info `Personalize`: `True`

#### `YonkersIR1,SysTopPatch4`
- `Digest`: `9c7c82fa00263d5265d6210eec68223618fa474ab5f02e2ed635e770d10a5ce3`
- `EPRO`: `False`
- `FabRevision`: `49729`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Lakeville/YonkersIR1,SysTopPatch4`
- Info `Personalize`: `True`

#### `YonkersIR1,SysTopPatch5`
- `Digest`: `052b9ec06213a1db74d7e45917d9bbf1d41b487eb647f3e14032ed1b37a2c1bf`
- `EPRO`: `True`
- `FabRevision`: `49729`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Lakeville/YonkersIR1,SysTopPatch5`
- Info `Personalize`: `True`

#### `YonkersIR1,SysTopPatch6`
- `Digest`: `9c7c82fa00263d5265d6210eec68223618fa474ab5f02e2ed635e770d10a5ce3`
- `EPRO`: `False`
- `FabRevision`: `43690`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Lakeville/YonkersIR1,SysTopPatch6`
- Info `Personalize`: `True`

#### `YonkersIR1,SysTopPatch7`
- `Digest`: `052b9ec06213a1db74d7e45917d9bbf1d41b487eb647f3e14032ed1b37a2c1bf`
- `EPRO`: `True`
- `FabRevision`: `43690`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Lakeville/YonkersIR1,SysTopPatch7`
- Info `Personalize`: `True`

#### `YonkersIR1,SysTopPatch8`
- `Digest`: `bf0b187d19186250b12f1bd5a3ce4def94004816a346c3c4f6df914f8c63d2a3`
- `EPRO`: `False`
- `FabRevision`: `49730`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Lakeville/YonkersIR1,SysTopPatch8`
- Info `Personalize`: `True`

#### `YonkersIR1,SysTopPatch9`
- `Digest`: `cbb72635c6f3ab38b4047515ea1471253f3cfa5fc301e7dced9f62b4065af7f7`
- `EPRO`: `True`
- `FabRevision`: `49730`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Lakeville/YonkersIR1,SysTopPatch9`
- Info `Personalize`: `True`

#### `YonkersIR1,SysTopPatchA`
- `Digest`: `bf0b187d19186250b12f1bd5a3ce4def94004816a346c3c4f6df914f8c63d2a3`
- `EPRO`: `False`
- `FabRevision`: `49986`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Lakeville/YonkersIR1,SysTopPatchA`
- Info `Personalize`: `True`

#### `YonkersIR1,SysTopPatchB`
- `Digest`: `cbb72635c6f3ab38b4047515ea1471253f3cfa5fc301e7dced9f62b4065af7f7`
- `EPRO`: `True`
- `FabRevision`: `49986`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Lakeville/YonkersIR1,SysTopPatchB`
- Info `Personalize`: `True`

#### `YonkersIR1,SysTopPatchC`
- `Digest`: `bf0b187d19186250b12f1bd5a3ce4def94004816a346c3c4f6df914f8c63d2a3`
- `EPRO`: `False`
- `FabRevision`: `52428`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Lakeville/YonkersIR1,SysTopPatchC`
- Info `Personalize`: `True`

#### `YonkersIR1,SysTopPatchD`
- `Digest`: `cbb72635c6f3ab38b4047515ea1471253f3cfa5fc301e7dced9f62b4065af7f7`
- `EPRO`: `True`
- `FabRevision`: `52428`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Lakeville/YonkersIR1,SysTopPatchD`
- Info `Personalize`: `True`

#### `YonkersIR1,SysTopPatchE`
- `Digest`: `bf0b187d19186250b12f1bd5a3ce4def94004816a346c3c4f6df914f8c63d2a3`
- `EPRO`: `False`
- `FabRevision`: `56797`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Lakeville/YonkersIR1,SysTopPatchE`
- Info `Personalize`: `True`

#### `YonkersIR1,SysTopPatchF`
- `Digest`: `cbb72635c6f3ab38b4047515ea1471253f3cfa5fc301e7dced9f62b4065af7f7`
- `EPRO`: `True`
- `FabRevision`: `56797`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Lakeville/YonkersIR1,SysTopPatchF`
- Info `Personalize`: `True`

#### `YonkersIR2,SysTopPatch0`
- `Digest`: `766c1906a4df7abea032957e6358e8f0948cd63a17b946de81e900b46e2fe30f`
- `EPRO`: `False`
- `FabRevision`: `49409`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Glenbrook/YonkersIR2,SysTopPatch0`
- Info `Personalize`: `True`

#### `YonkersIR2,SysTopPatch1`
- `Digest`: `dd99f434a5980c4b0779aee077d3d86c97f2739b6299540efabd33e740874230`
- `EPRO`: `True`
- `FabRevision`: `49409`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Glenbrook/YonkersIR2,SysTopPatch1`
- Info `Personalize`: `True`

#### `YonkersIR2,SysTopPatch2`
- `Digest`: `766c1906a4df7abea032957e6358e8f0948cd63a17b946de81e900b46e2fe30f`
- `EPRO`: `False`
- `FabRevision`: `49473`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Glenbrook/YonkersIR2,SysTopPatch2`
- Info `Personalize`: `True`

#### `YonkersIR2,SysTopPatch3`
- `Digest`: `dd99f434a5980c4b0779aee077d3d86c97f2739b6299540efabd33e740874230`
- `EPRO`: `True`
- `FabRevision`: `49473`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Glenbrook/YonkersIR2,SysTopPatch3`
- Info `Personalize`: `True`

#### `YonkersIR2,SysTopPatch4`
- `Digest`: `766c1906a4df7abea032957e6358e8f0948cd63a17b946de81e900b46e2fe30f`
- `EPRO`: `False`
- `FabRevision`: `43690`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Glenbrook/YonkersIR2,SysTopPatch4`
- Info `Personalize`: `True`

#### `YonkersIR2,SysTopPatch5`
- `Digest`: `dd99f434a5980c4b0779aee077d3d86c97f2739b6299540efabd33e740874230`
- `EPRO`: `True`
- `FabRevision`: `43690`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Glenbrook/YonkersIR2,SysTopPatch5`
- Info `Personalize`: `True`

#### `YonkersIR2,SysTopPatch6`
- `Digest`: `766c1906a4df7abea032957e6358e8f0948cd63a17b946de81e900b46e2fe30f`
- `EPRO`: `False`
- `FabRevision`: `48059`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Glenbrook/YonkersIR2,SysTopPatch6`
- Info `Personalize`: `True`

#### `YonkersIR2,SysTopPatch7`
- `Digest`: `dd99f434a5980c4b0779aee077d3d86c97f2739b6299540efabd33e740874230`
- `EPRO`: `True`
- `FabRevision`: `48059`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Glenbrook/YonkersIR2,SysTopPatch7`
- Info `Personalize`: `True`

#### `YonkersIR2,SysTopPatch8`
- `Digest`: `7f2c2fa99478bc52f047cffed36dc3fea3e617113a4788b55b18be2470f97c9c`
- `EPRO`: `False`
- `FabRevision`: `49474`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Glenbrook/YonkersIR2,SysTopPatch8`
- Info `Personalize`: `True`

#### `YonkersIR2,SysTopPatch9`
- `Digest`: `0305ea5727d84fe41c073105ed389517b947e733adcf2aa4fd7d5e1d3082baa7`
- `EPRO`: `True`
- `FabRevision`: `49474`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Glenbrook/YonkersIR2,SysTopPatch9`
- Info `Personalize`: `True`

#### `YonkersIR2,SysTopPatchA`
- `Digest`: `7f2c2fa99478bc52f047cffed36dc3fea3e617113a4788b55b18be2470f97c9c`
- `EPRO`: `False`
- `FabRevision`: `49730`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Glenbrook/YonkersIR2,SysTopPatchA`
- Info `Personalize`: `True`

#### `YonkersIR2,SysTopPatchB`
- `Digest`: `0305ea5727d84fe41c073105ed389517b947e733adcf2aa4fd7d5e1d3082baa7`
- `EPRO`: `True`
- `FabRevision`: `49730`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Glenbrook/YonkersIR2,SysTopPatchB`
- Info `Personalize`: `True`

#### `YonkersIR2,SysTopPatchC`
- `Digest`: `7f2c2fa99478bc52f047cffed36dc3fea3e617113a4788b55b18be2470f97c9c`
- `EPRO`: `False`
- `FabRevision`: `49986`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Glenbrook/YonkersIR2,SysTopPatchC`
- Info `Personalize`: `True`

#### `YonkersIR2,SysTopPatchD`
- `Digest`: `0305ea5727d84fe41c073105ed389517b947e733adcf2aa4fd7d5e1d3082baa7`
- `EPRO`: `True`
- `FabRevision`: `49986`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Glenbrook/YonkersIR2,SysTopPatchD`
- Info `Personalize`: `True`

#### `YonkersIR2,SysTopPatchE`
- `Digest`: `7f2c2fa99478bc52f047cffed36dc3fea3e617113a4788b55b18be2470f97c9c`
- `EPRO`: `False`
- `FabRevision`: `52428`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Glenbrook/YonkersIR2,SysTopPatchE`
- Info `Personalize`: `True`

#### `YonkersIR2,SysTopPatchF`
- `Digest`: `0305ea5727d84fe41c073105ed389517b947e733adcf2aa4fd7d5e1d3082baa7`
- `EPRO`: `True`
- `FabRevision`: `52428`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Glenbrook/YonkersIR2,SysTopPatchF`
- Info `Personalize`: `True`

#### `eUICC,Gold`
- `Digest`: `a9632326a052c090677482c51c4d07259478c6d941ee1d2ee46ccf0f6f9249aa`
- Info `Path`: `Firmware/vinyl_20.vnlfw`

#### `eUICC,Main`
- `Digest`: `ac690767d53680418ce22855a94fd9f1be619995fc03d66d06fae31b263ae296`
- Info `Path`: `Firmware/vinyl_20.vnlfw`

#### `ftap`
- Info `HashMethod`: `sha2-256`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Personalize`: `False`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `ftsp`
- Info `HashMethod`: `sha2-256`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Personalize`: `False`
- Info `RestoreRequestRules`: `[{'Actions': {'ESEC': False}, 'Conditions': {'ApRawSecurityMode': False}}, {'Actions': {'ESEC': True}, 'Conditions': {'ApRawSecurityMode': True}}, {'Actions': {'ESEC': False}, 'Conditions': {'ApDemotionPolicyOverride': '', 'ApRawProductionMode': False, 'ApRawSecurityMode': True}}, {'Actions': {'ESEC`
- `Trusted`: `True`

#### `iBEC`
- `BuildString`: `iBoot-15391~1757`
- `Digest`: `41fa3c2a7d464186a00f90caec97640c78ffb77af1ffb1db84a00a3b944ed29a3927347c95c939135445fc54baaefc78`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/dfu/iBEC.v68.RELEASE.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `iBSS`
- `BuildString`: `iBoot-15391~1757`
- `Digest`: `198d68bff79405608411f36aa2e2c7036a92f001f474d842c18c52c54634ea77148483530c980bcb7828e3d17f814d90`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/dfu/iBSS.v68.RELEASE.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'DPRO': True}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductionMode': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRe`
- `MemoryMap`: `6480728002000000040000006880728002000000040000000801051102000000080000003002e4110200000008000000f849e4110200000008000000000005110200000008000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000`
- `RawDataDigest`: `2e62b37b6485cc3814fd1cfda528062cac98afd2cb365a23fc5b5a76231ae832f73c74e64b5f17f17195d50d6591a698`
- `Trusted`: `True`

#### `iBoot`
- `Digest`: `28df03c4dfab963ccafdf5a1450157e00e3079f9cf36d5eb4661ec63b91b362fb9ad5543befb828a0ea7f321de8de2c1`
- Info `IsFTAB`: `False`
- Info `IsFirmwarePayload`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/all_flash/iBoot.v68.RELEASE.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `iBootData`
- `Digest`: `09ec9d198c7d9be2a45808f9c668801590df1a4a051bbe7cd79372ba84165cbd321ea81936b8908d7d64ccc52ea56cc9`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/all_flash/iBootData.v68.RELEASE.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `rfta`
- Info `HashMethod`: `sha2-256`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Personalize`: `False`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `rfts`
- Info `HashMethod`: `sha2-256`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Personalize`: `False`
- Info `RestoreRequestRules`: `[{'Actions': {'ESEC': False}, 'Conditions': {'ApRawSecurityMode': False}}, {'Actions': {'ESEC': True}, 'Conditions': {'ApRawSecurityMode': True}}, {'Actions': {'ESEC': False}, 'Conditions': {'ApDemotionPolicyOverride': '', 'ApRawProductionMode': False, 'ApRawSecurityMode': True}}, {'Actions': {'ESEC`
- `Trusted`: `True`

## Customer Upgrade Install (IPSW)

- `ApChipID`: `0x8160`
- `ApBoardID`: `0x0E`
- `ApSecurityDomain`: `0x01`
- `Ap,ProductType`: `iPhone19,4`
- `Ap,Target`: `V68AP`
- `Ap,TargetType`: `v68`
- `Ap,ProductMarketingVersion`: `27.2`
- `Ap,OSLongVersion`: `24.2.102.9.0,0`
- Info `Ap,Timestamp`: `0`
- Info `BuildNumber`: `24B91020`
- Info `BuildTrain`: `RavePopB`
- Info `ContentEncoding`: `aea`
- Info `Cryptex1,AppOSSize`: `16`
- Info `Cryptex1,SystemOSSize`: `5918`
- Info `DeviceClass`: `v68ap`
- Info `FDRSupport`: `True`
- Info `ImageName`: `V68RestoreIPSW`
- Info `MinimumSystemPartition`: `9791`
- Info `MobileDeviceMinVersion`: `1853`
- Info `OSDiskImageSize`: `10364`
- Info `OSVarContentSize`: `818733056`
- Info `RecoveryVariant`: `Recovery Customer Install`
- Info `RequiresNonceSlot`: `True`
- Info `RequiresUIDMode`: `True`
- Info `RestoreAttestationMode`: `8`
- Info `RestoreBehavior`: `Update`
- Info `Variant`: `Customer Upgrade Install (IPSW)`

172 components.

| Component | Path | Digest (SHA-384, first 16 hex) | Flags |
|---|---|---|---|
| `ANE` | `Firmware/ane/h19_ane0_fw_perses_v6x.im4p` | `64b8d6c628bad189` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `ANS` | `Firmware/ansf.t8160.release.im4p` | `14d1f7273d1a1d75` | Trusted, IsFirmwarePayload, RestoreRequestRules |
| `AOP` | `Firmware/AOP/aopfw-v68aop.RELEASE.im4p` | `a8be918779ae2c1d` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `AOP2` | `Firmware/AOP2/aop2fw-v68aop2.RELEASE.im4p` | `abfbc6dc12c26f5c` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `AVE` | `Firmware/ave/AppleAVE2FW_H19.im4p` | `b9030e94822ebb2c` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `Ap,ANE1` | `Firmware/ane/h19_ane1_fw_perses_v6x.im4p` | `051c0dc0bb17eed9` | Trusted, IsFUDFirmware, RestoreRequestRules |
| `Ap,AVD` | `Firmware/avd/AppleAVDFW_H19P.im4p` | `a580555ba355aca0` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `Ap,ApplePMCFirmware` | `Firmware/pmc/t8160pmcfw.im4p` | `887e53baaf9f25ad` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `Ap,AppleVideoEncoder0` | `Firmware/ave/AppleAVE2FW_H19_AVE0.im4p` | `63e41e5d2bfa0328` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `Ap,AppleVideoEncoder1` | `Firmware/ave/AppleAVE2FW_H19_AVE1.im4p` | `049e3519a25033b3` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `Ap,AppleVideoEncoder2` | `Firmware/ave/AppleAVE2FW_H19_AVE2.im4p` | `19c0e781fee7cba7` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `Ap,AppleVideoEncoder3` | `Firmware/ave/AppleAVE2FW_H19_AVE3.im4p` | `5e1206584755555f` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `Ap,AppleVideoEncoder4` | `Firmware/ave/AppleAVE2FW_H19_AVE4.im4p` | `1adac89457306494` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `Ap,AppleVideoEncoder5` | `Firmware/ave/AppleAVE2FW_H19_AVE5.im4p` | `63ff7021a0e26aab` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `Ap,AppleVideoEncoder6` | `Firmware/ave/AppleAVE2FW_H19_AVE6.im4p` | `e62efe0891fc91f5` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `Ap,AppleVideoEncoder7` | `Firmware/ave/AppleAVE2FW_H19_AVE7.im4p` | `223eda99b6bace8b` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `Ap,AppleVideoEncoder8` | `Firmware/ave/AppleAVE2FW_H19_AVE8.im4p` | `05f79bc85c0600aa` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `Ap,AudioBootChime` | `Firmware/embeddedaudioresources/image4/v68-boot-chime.im4p` | `9e584ad82b3787c6` | Trusted, IsiBootNonEssentialFirmware, RestoreRequestRules |
| `Ap,ExclaveOS` | `141-27521-104.dmg.aea` | `e5068d05578a3d9e` | Trusted, RestoreRequestRules |
| `Ap,ExclaveOSIntegrityCatalog` | `Firmware/141-27521-104.dmg.aea.integrity_catalog` | `414d318f25032cf9` | Trusted, IsFUDFirmware, RestoreRequestRules |
| `Ap,ExclaveOSTrustCache` | `Firmware/141-27521-104.dmg.aea.trustcache` | `c11c6fe006449290` | Trusted, IsFUDFirmware, RestoreRequestRules |
| `Ap,ExclaveOSVolume` | `Firmware/141-27521-104.dmg.aea.root_hash` | `e7d273a37772bbb8` | Trusted, IsFUDFirmware, RestoreRequestRules |
| `Ap,GFX1Firmware` | `Firmware/agx/armfw1_g19p.im4p` | `33febef5d5a22898` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `Ap,HapticAssets` | `Firmware/V68_HapticAssets.im4p` | `9a85fd4f0a9f365e` | IsFUDFirmware, RestoreRequestRules |
| `Ap,LowPowerMode` | `Firmware/AppleLPM/AppleLPM.v68.release.im4p` | `d72c01b171d40df1` | IsiBootEANFirmware, RestoreRequestRules |
| `Ap,MSRFirmware` | `Firmware/msr/t8160.msrf.im4p` | `6c2611f3e8b5eaed` | Trusted, IsFUDFirmware, RestoreRequestRules |
| `Ap,MandoFW` | `Firmware/V68_MandoFirmware.im4p` | `44624f1ad5411cbe` | IsFUDFirmware, RestoreRequestRules |
| `Ap,RestoreANE1` | `Firmware/ane/h19_ane1_fw_perses_v6x.im4p` | `d88874b6f35f6d3f` | Trusted, IsLoadedByiBoot, RestoreRequestRules |
| `Ap,RestoreMSRFirmware` | `Firmware/msr/t8160.rmsr.im4p` | `4594142c48d515ef` | Trusted, IsLoadedByiBoot, RestoreRequestRules |
| `Ap,RestoreSecureM3Firmware` | `Firmware/M3/bin/securem3fw-v68.im4p` | `f4a3ee30ac0b966c` | Trusted, IsLoadedByiBoot, RestoreRequestRules |
| `Ap,RestoreSecurePageTableMonitor` | `Firmware/sptm.t8160.release.im4p` | `c9e66676240d53ab` | Trusted, IsLoadedByiBoot, RestoreRequestRules |
| `Ap,RestoreTrustedExecutionMonitor` | `Firmware/txm.iphoneos.release.im4p` | `75371b6d03b94162` | Trusted, IsLoadedByiBoot, RestoreRequestRules |
| `Ap,RestorecL4` | `Firmware/image4/exclavecore_bundle.v68.RELEASE.restore.im4p` | `f7846005a0bfd5a0` | Trusted, IsLoadedByiBoot, RestoreRequestRules |
| `Ap,SecureM3Firmware` | `Firmware/M3/bin/securem3fw-v68.im4p` | `9b9075693ce1ecd8` | Trusted, IsFUDFirmware, RestoreRequestRules |
| `Ap,SecurePageTableMonitor` | `Firmware/sptm.t8160.release.im4p` | `2f69cb8b9dc4932f` | Trusted, IsFUDFirmware, RestoreRequestRules |
| `Ap,SystemVolumeCanonicalMetadata` | `Firmware/141-28898-095.dmg.aea.mtree` | `5d99f6cc85a80b45` | Trusted, IsFUDFirmware, RestoreRequestRules |
| `Ap,TrustedExecutionMonitor` | `Firmware/txm.iphoneos.release.im4p` | `e9f0a0a9f060553d` | Trusted, IsFUDFirmware, RestoreRequestRules |
| `Ap,cL4` | `Firmware/image4/exclavecore_bundle.v68.RELEASE.im4p` | `c52af32219d872a0` | Trusted, IsFUDFirmware, RestoreRequestRules |
| `AppleLogo` | `Firmware/all_flash/applelogo@2d~iphone.im4p` | `72e55666b43d92ae` | Trusted, IsiBootEANFirmware, RestoreRequestRules |
| `BMU,DigestMap` | `Firmware/Volchok/BAT8193/DigestMap.der` | `a217a7c58314ae73` |  |
| `BMU,FirmwareMap` | `Firmware/Volchok/BAT8193/FirmwareMap.plist` | `b87e189151c508da` |  |
| `BMU2,DigestMap` | `Firmware/Volchok/BAT8193/DigestMap.der` | `a217a7c58314ae73` |  |
| `BMU2,FirmwareMap` | `Firmware/Volchok/BAT8193/FirmwareMap.plist` | `b87e189151c508da` |  |
| `Cellular1,CdpAscDl` | `Firmware/c4020iphone/Release/patched/ftab.bin` | `9bb48fff8021c91f` | Trusted, RestoreRequestRules |
| `Cellular1,CdpAscUl` | `Firmware/c4020iphone/Release/patched/ftab.bin` | `c0e59a3e3ffbd3b5` | Trusted, RestoreRequestRules |
| `Cellular1,CdpHost` | `Firmware/c4020iphone/Release/patched/ftab.bin` | `8d30be1ec9e53237` | Trusted, RestoreRequestRules |
| `Cellular1,L1CL1S` | `Firmware/c4020iphone/Release/patched/ftab.bin` | `46e0cdcb8acbca7a` | Trusted, RestoreRequestRules |
| `Cellular1,LLB` | `Firmware/c4020iphone/Release/patched/ftab.bin` | `162f084d64d6ba1e` | Trusted, RestoreRequestRules |
| `Cellular1,PMUFW` | `Firmware/c4020iphone/Release/patched/ftab.bin` | `33e1a57e7ba21e87` | Trusted, RestoreRequestRules |
| `Cellular1,PMUFW2` | `Firmware/c4020iphone/Release/patched/ftab.bin` | `024bbc34f73996a3` | Trusted, RestoreRequestRules |
| `Cellular1,RTKitOS` | `Firmware/c4020iphone/Release/patched/ftab.bin` | `9ccde882d2e36794` | Trusted, RestoreRequestRules |
| `Cellular1,Recipe` | `Firmware/c4020iphone/Release/patched/ftab.bin` | `e7cb1b15c3717f42` | Trusted, RestoreRequestRules |
| `Cellular1,iBootData` | `Firmware/c4020iphone/Release/patched/ftab.bin` | `45b76cdcd9e32532` | Trusted, RestoreRequestRules |
| `Cryptex1,AppOS` | `141-28395-106.dmg` | `87f1114332363108` | RestoreRequestRules |
| `Cryptex1,AppTrustCache` | `Firmware/141-28395-106.dmg.trustcache` | `7072d57c04de1ffd` | RestoreRequestRules |
| `Cryptex1,AppVolume` | `Firmware/141-28395-106.dmg.root_hash` | `e3a31ede1b5fdbb0` | RestoreRequestRules |
| `Cryptex1,SystemOS` | `141-28400-098.dmg.aea` | `597a37020cb5123a` | RestoreRequestRules |
| `Cryptex1,SystemTrustCache` | `Firmware/141-28400-098.dmg.aea.trustcache` | `fa1bbcbdaa387a71` | RestoreRequestRules |
| `Cryptex1,SystemVolume` | `Firmware/141-28400-098.dmg.aea.root_hash` | `9bfa3a33afdde331` | RestoreRequestRules |
| `DCP` | `Firmware/dcp/t8160dcp.im4p` | `aefaf09c5156cd03` | Trusted, IsiBootEANFirmware, RestoreRequestRules |
| `DeviceTree` | `Firmware/all_flash/DeviceTree.v68ap.im4p` | `a3b521b47aa0f054` | Trusted, IsFirmwarePayload, RestoreRequestRules |
| `GFX` | `Firmware/agx/armfw_g19p.im4p` | `40c7cc60cbda6878` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `ISP` | `Firmware/isp_bni/adc-boreas-v68.im4p` | `33b6bdc438ecbe1b` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `KernelCache` | `kernelcache.release.v6x-pandia` | `9f57d7cf359fc767` | Trusted, RestoreRequestRules |
| `LLB` | `Firmware/all_flash/LLB.v68.RELEASE.im4p` | `302b40b9dbf4070b` | Trusted, IsFirmwarePayload, RestoreRequestRules |
| `LeapHaptics` | `Firmware/V68_LeapHapticsFirmware.im4p` | `8afa6138a6d3be9b` | IsFUDFirmware, RestoreRequestRules |
| `Liquid` | `Firmware/all_flash/liquiddetect@2d~iphone.im4p` | `194aaed667db6ada` | Trusted, IsiBootEANFirmware, RestoreRequestRules |
| `MtpFirmware` | `Firmware/V68_MtpFirmware.im4p` | `270a440ad64cb858` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `Multitouch` | `Firmware/V68_Multitouch.im4p` | `7368509e073e8c3b` | IsFUDFirmware, RestoreRequestRules |
| `OS` | `141-28898-095.dmg.aea` | `b1d8bce0e16a7548` | Trusted, RestoreRequestRules |
| `PMP` | `Firmware/pmp/t8160pmp.im4p` | `19008a2bc4a04e1b` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `Rap,RTKitIOConfig` | `Firmware/Rose/r2p1/ftab.bin` | `6b1013023f1c7479` | Trusted, RestoreRequestRules |
| `Rap,RTKitOS` | `Firmware/Rose/r2p1/ftab.bin` | `e46b5fd033a4a736` | Trusted, RestoreRequestRules |
| `Rap,SoftwareBinaryDsp1` | `Firmware/Rose/r2p1/ftab.bin` | `7300dc26d19b540e` | Trusted, RestoreRequestRules |
| `RecoveryMode` | `Firmware/all_flash/recoverymode@2d~iphone.im4p` | `848e2e1ba471a389` | Trusted, IsiBootEANFirmware, RestoreRequestRules |
| `RestoreANS` | `Firmware/rans.t8160.release.im4p` | `c60c3b84b45ea4f0` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `RestoreDCP` | `Firmware/dcp/t8160dcp_restore.im4p` | `39063050c7616fc6` | Trusted, IsLoadedByiBoot, RestoreRequestRules |
| `RestoreDeviceTree` | `Firmware/all_flash/DeviceTree.v68ap.im4p` | `94cbc3d7c32dfcad` | Trusted, RestoreRequestRules |
| `RestoreKernelCache` | `kernelcache.release.v6x-pandia` | `14a743b0cc147a94` | Trusted, RestoreRequestRules |
| `RestoreLogo` | `Firmware/all_flash/applelogo@2d~iphone.im4p` | `0f7534a7d9c2761a` | Trusted, RestoreRequestRules |
| `RestoreRamDisk` | `141-29011-104.dmg` | `5398834502bc9ecc` | Trusted, RestoreRequestRules |
| `RestoreSEP` | `Firmware/all_flash/sep-firmware.v68.RELEASE.im4p` | `6333efcf0bc6eccf` | Trusted, RestoreRequestRules |
| `RestoreTrustCache` | `Firmware/141-29011-104.dmg.trustcache` | `a4cf99fcabdad855` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `SE,RapRTKitOS` | `Firmware/Rose/r2p1/ftab.bin` | `e46b5fd033a4a736` |  |
| `SE,RapSwBinDsp` | `Firmware/Rose/r2p1/ftab.bin` | `7300dc26d19b540e` |  |
| `SE,UpdatePayload` | `Firmware/SE/Stockholm91.RELEASE.sefw` | `` |  |
| `SEP` | `Firmware/all_flash/sep-firmware.v68.RELEASE.im4p` | `a4e4c8fcba2b9a78` | Trusted, RestoreRequestRules |
| `SIO` | `Firmware/SmartIOFirmware_ASCv8.im4p` | `8873ba2b293fc114` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `SepStage1` | `Firmware/all_flash/sep-patches.v68.im4p` | `58a738a8ef5bbc8b` | Trusted, RestoreRequestRules |
| `StaticTrustCache` | `Firmware/141-28898-095.dmg.aea.trustcache` | `f9fd4c9b274ca337` | Trusted, IsFUDFirmware, RestoreRequestRules |
| `SystemVolume` | `Firmware/141-28898-095.dmg.aea.root_hash` | `23684e5cf582fcdd` | Trusted, IsFUDFirmware, RestoreRequestRules |
| `WCHFirmwareUpdater` | `Firmware/WirelessPower/WirelessPower.v68.im4p` | `ee119dfcfbb36a8e` | Trusted, IsLoadedByiBoot, IsiBootEANFirmware, RestoreRequestRules |
| `Wireless1,ACIBT` | `Firmware/t2026phoneG2/Release/ftab.bin` | `51c01d433c414fa2` | Trusted, RestoreRequestRules |
| `Wireless1,ACIBTLPEM` | `Firmware/t2026phoneG2/Release/ftab.bin` | `1f9a194a2e7aaa38` | Trusted, RestoreRequestRules |
| `Wireless1,ACIBTManuf` | `Firmware/t2026phoneG2/Release/ftab.bin` | `51c01d433c414fa2` | Trusted, RestoreRequestRules |
| `Wireless1,ACIWIFI` | `Firmware/t2026phoneG2/Release/ftab.bin` | `902b5adeacd5144f` | Trusted, RestoreRequestRules |
| `Wireless1,ACIWiFiTxManuf` | `Firmware/t2026phoneG2/Release/ftab.bin` | `36423b324369661e` | Trusted, RestoreRequestRules |
| `Wireless1,BTSecondary` | `Firmware/t2026phoneG2/Release/ftab.bin` | `ebd59be4d27b01a4` | Trusted, RestoreRequestRules |
| `Wireless1,BTSecondaryManuf` | `Firmware/t2026phoneG2/Release/ftab.bin` | `ebd59be4d27b01a4` | Trusted, RestoreRequestRules |
| `Wireless1,CCPUApplicationFirmware` | `Firmware/t2026phoneG2/Release/ftab.bin` | `45f576ce687be46e` | Trusted, RestoreRequestRules |
| `Wireless1,CoexRealTimeArbiter` | `Firmware/t2026phoneG2/Release/ftab.bin` | `44749c87da9b89c1` | Trusted, RestoreRequestRules |
| `Wireless1,PhyBlueTooth` | `Firmware/t2026phoneG2/Release/ftab.bin` | `181d64d765b57b4e` | Trusted, RestoreRequestRules |
| `Wireless1,PhyBlueTooth5G` | `Firmware/t2026phoneG2/Release/ftab.bin` | `8c0742a5e9ad20e1` | Trusted, RestoreRequestRules |
| `Wireless1,PhyBlueTooth5GManuf` | `Firmware/t2026phoneG2/Release/ftab.bin` | `8c0742a5e9ad20e1` | Trusted, RestoreRequestRules |
| `Wireless1,PhyBlueToothLPM` | `Firmware/t2026phoneG2/Release/ftab.bin` | `b0b972453c81fc03` | Trusted, RestoreRequestRules |
| `Wireless1,PhyBlueToothManuf` | `Firmware/t2026phoneG2/Release/ftab.bin` | `181d64d765b57b4e` | Trusted, RestoreRequestRules |
| `Wireless1,PhyBluetooth5GTrim` | `Firmware/t2026phoneG2/Release/ftab.bin` | `94c974402ac11c71` | Trusted, RestoreRequestRules |
| `Wireless1,PhyBluetoothTrim` | `Firmware/t2026phoneG2/Release/ftab.bin` | `3820e32dc8f92bf0` | Trusted, RestoreRequestRules |
| `Wireless1,RTKitOS` | `Firmware/t2026phoneG2/Release/ftab.bin` | `8219626cc42aae17` | Trusted, RestoreRequestRules |
| `Wireless1,RTKitOSLPEM` | `Firmware/t2026phoneG2/Release/ftab.bin` | `be6863c3d47047bd` | Trusted, RestoreRequestRules |
| `Wireless1,ScanBTLPEM` | `Firmware/t2026phoneG2/Release/ftab.bin` | `3c449b8c373522b5` | Trusted, RestoreRequestRules |
| `Wireless1,ScanBTManuf` | `Firmware/t2026phoneG2/Release/ftab.bin` | `f890cbeafa0ccbeb` | Trusted, RestoreRequestRules |
| `Wireless1,ScanBluetooth` | `Firmware/t2026phoneG2/Release/ftab.bin` | `f890cbeafa0ccbeb` | Trusted, RestoreRequestRules |
| `Wireless1,ScanWifi` | `Firmware/t2026phoneG2/Release/ftab.bin` | `14f68624a65887fa` | Trusted, RestoreRequestRules |
| `Wireless1,ScanWifiManuf` | `Firmware/t2026phoneG2/Release/ftab.bin` | `611a45ae78230635` | Trusted, RestoreRequestRules |
| `Wireless1,WiFiRx` | `Firmware/t2026phoneG2/Release/ftab.bin` | `00751f9522d1e2e3` | Trusted, RestoreRequestRules |
| `Wireless1,WiFiRxManuf` | `Firmware/t2026phoneG2/Release/ftab.bin` | `43b50d30fed4c6be` | Trusted, RestoreRequestRules |
| `Wireless1,WiFiTx` | `Firmware/t2026phoneG2/Release/ftab.bin` | `b28a762c0e1d7d94` | Trusted, RestoreRequestRules |
| `Wireless1,WiFiTxManuf` | `Firmware/t2026phoneG2/Release/ftab.bin` | `da7ad47bb37867fc` | Trusted, RestoreRequestRules |
| `Wireless1,Wifi2GLMAC` | `Firmware/t2026phoneG2/Release/ftab.bin` | `2d0a90a6fcd00801` | Trusted, RestoreRequestRules |
| `Wireless1,Wifi2GLMACManuf` | `Firmware/t2026phoneG2/Release/ftab.bin` | `3e72c8dbb12e0c77` | Trusted, RestoreRequestRules |
| `Wireless1,Wifi2GLPhy` | `Firmware/t2026phoneG2/Release/ftab.bin` | `847eca454fc4f9f4` | Trusted, RestoreRequestRules |
| `Wireless1,Wifi2GLPhyManuf` | `Firmware/t2026phoneG2/Release/ftab.bin` | `847eca454fc4f9f4` | Trusted, RestoreRequestRules |
| `Wireless1,Wifi2GLPhyTrim` | `Firmware/t2026phoneG2/Release/ftab.bin` | `afc1e501998b0b55` | Trusted, RestoreRequestRules |
| `Wireless1,Wifi5GLMAC` | `Firmware/t2026phoneG2/Release/ftab.bin` | `bedce67d68535076` | Trusted, RestoreRequestRules |
| `Wireless1,Wifi5GLMACManuf` | `Firmware/t2026phoneG2/Release/ftab.bin` | `2372fd4b17cc6eef` | Trusted, RestoreRequestRules |
| `Wireless1,Wifi5GLPhy` | `Firmware/t2026phoneG2/Release/ftab.bin` | `d528706af0b66fe1` | Trusted, RestoreRequestRules |
| `Wireless1,Wifi5GLPhyManuf` | `Firmware/t2026phoneG2/Release/ftab.bin` | `d528706af0b66fe1` | Trusted, RestoreRequestRules |
| `Wireless1,Wifi5GLPhyTrim` | `Firmware/t2026phoneG2/Release/ftab.bin` | `c8dac484934f456d` | Trusted, RestoreRequestRules |
| `Wireless1,WifiRegData` | `Firmware/t2026phoneG2/Release/ftab.bin` | `03adb4c5ce95a3da` | Trusted, RestoreRequestRules |
| `YonkersIR1,SysTopPatch0` | `Firmware/Lakeville/YonkersIR1,SysTopPatch0` | `9c7c82fa00263d52` |  |
| `YonkersIR1,SysTopPatch1` | `Firmware/Lakeville/YonkersIR1,SysTopPatch1` | `052b9ec06213a1db` | EPRO |
| `YonkersIR1,SysTopPatch2` | `Firmware/Lakeville/YonkersIR1,SysTopPatch2` | `9c7c82fa00263d52` |  |
| `YonkersIR1,SysTopPatch3` | `Firmware/Lakeville/YonkersIR1,SysTopPatch3` | `052b9ec06213a1db` | EPRO |
| `YonkersIR1,SysTopPatch4` | `Firmware/Lakeville/YonkersIR1,SysTopPatch4` | `9c7c82fa00263d52` |  |
| `YonkersIR1,SysTopPatch5` | `Firmware/Lakeville/YonkersIR1,SysTopPatch5` | `052b9ec06213a1db` | EPRO |
| `YonkersIR1,SysTopPatch6` | `Firmware/Lakeville/YonkersIR1,SysTopPatch6` | `9c7c82fa00263d52` |  |
| `YonkersIR1,SysTopPatch7` | `Firmware/Lakeville/YonkersIR1,SysTopPatch7` | `052b9ec06213a1db` | EPRO |
| `YonkersIR1,SysTopPatch8` | `Firmware/Lakeville/YonkersIR1,SysTopPatch8` | `bf0b187d19186250` |  |
| `YonkersIR1,SysTopPatch9` | `Firmware/Lakeville/YonkersIR1,SysTopPatch9` | `cbb72635c6f3ab38` | EPRO |
| `YonkersIR1,SysTopPatchA` | `Firmware/Lakeville/YonkersIR1,SysTopPatchA` | `bf0b187d19186250` |  |
| `YonkersIR1,SysTopPatchB` | `Firmware/Lakeville/YonkersIR1,SysTopPatchB` | `cbb72635c6f3ab38` | EPRO |
| `YonkersIR1,SysTopPatchC` | `Firmware/Lakeville/YonkersIR1,SysTopPatchC` | `bf0b187d19186250` |  |
| `YonkersIR1,SysTopPatchD` | `Firmware/Lakeville/YonkersIR1,SysTopPatchD` | `cbb72635c6f3ab38` | EPRO |
| `YonkersIR1,SysTopPatchE` | `Firmware/Lakeville/YonkersIR1,SysTopPatchE` | `bf0b187d19186250` |  |
| `YonkersIR1,SysTopPatchF` | `Firmware/Lakeville/YonkersIR1,SysTopPatchF` | `cbb72635c6f3ab38` | EPRO |
| `YonkersIR2,SysTopPatch0` | `Firmware/Glenbrook/YonkersIR2,SysTopPatch0` | `766c1906a4df7abe` |  |
| `YonkersIR2,SysTopPatch1` | `Firmware/Glenbrook/YonkersIR2,SysTopPatch1` | `dd99f434a5980c4b` | EPRO |
| `YonkersIR2,SysTopPatch2` | `Firmware/Glenbrook/YonkersIR2,SysTopPatch2` | `766c1906a4df7abe` |  |
| `YonkersIR2,SysTopPatch3` | `Firmware/Glenbrook/YonkersIR2,SysTopPatch3` | `dd99f434a5980c4b` | EPRO |
| `YonkersIR2,SysTopPatch4` | `Firmware/Glenbrook/YonkersIR2,SysTopPatch4` | `766c1906a4df7abe` |  |
| `YonkersIR2,SysTopPatch5` | `Firmware/Glenbrook/YonkersIR2,SysTopPatch5` | `dd99f434a5980c4b` | EPRO |
| `YonkersIR2,SysTopPatch6` | `Firmware/Glenbrook/YonkersIR2,SysTopPatch6` | `766c1906a4df7abe` |  |
| `YonkersIR2,SysTopPatch7` | `Firmware/Glenbrook/YonkersIR2,SysTopPatch7` | `dd99f434a5980c4b` | EPRO |
| `YonkersIR2,SysTopPatch8` | `Firmware/Glenbrook/YonkersIR2,SysTopPatch8` | `7f2c2fa99478bc52` |  |
| `YonkersIR2,SysTopPatch9` | `Firmware/Glenbrook/YonkersIR2,SysTopPatch9` | `0305ea5727d84fe4` | EPRO |
| `YonkersIR2,SysTopPatchA` | `Firmware/Glenbrook/YonkersIR2,SysTopPatchA` | `7f2c2fa99478bc52` |  |
| `YonkersIR2,SysTopPatchB` | `Firmware/Glenbrook/YonkersIR2,SysTopPatchB` | `0305ea5727d84fe4` | EPRO |
| `YonkersIR2,SysTopPatchC` | `Firmware/Glenbrook/YonkersIR2,SysTopPatchC` | `7f2c2fa99478bc52` |  |
| `YonkersIR2,SysTopPatchD` | `Firmware/Glenbrook/YonkersIR2,SysTopPatchD` | `0305ea5727d84fe4` | EPRO |
| `YonkersIR2,SysTopPatchE` | `Firmware/Glenbrook/YonkersIR2,SysTopPatchE` | `7f2c2fa99478bc52` |  |
| `YonkersIR2,SysTopPatchF` | `Firmware/Glenbrook/YonkersIR2,SysTopPatchF` | `0305ea5727d84fe4` | EPRO |
| `eUICC,Gold` | `Firmware/vinyl_20.vnlfw` | `a9632326a052c090` |  |
| `eUICC,Main` | `Firmware/vinyl_20.vnlfw` | `ac690767d5368041` |  |
| `ftap` | `` | `` | Trusted, RestoreRequestRules |
| `ftsp` | `` | `` | Trusted, RestoreRequestRules |
| `iBEC` | `Firmware/dfu/iBEC.v68.RELEASE.im4p` | `41fa3c2a7d464186` | Trusted, RestoreRequestRules |
| `iBSS` | `Firmware/dfu/iBSS.v68.RELEASE.im4p` | `198d68bff7940560` | Trusted, RestoreRequestRules |
| `iBoot` | `Firmware/all_flash/iBoot.v68.RELEASE.im4p` | `28df03c4dfab963c` | Trusted, IsFirmwarePayload, RestoreRequestRules |
| `iBootData` | `Firmware/all_flash/iBootData.v68.RELEASE.im4p` | `09ec9d198c7d9be2` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `rfta` | `` | `` | Trusted, RestoreRequestRules |
| `rfts` | `` | `` | Trusted, RestoreRequestRules |

### Component details

#### `ANE`
- `Digest`: `64b8d6c628bad1896a23a2a0475db70ec18674967ded0d3dda576bae22c4a7b0bfa73f3d767d0f529b35f045abad7d85`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/ane/h19_ane0_fw_perses_v6x.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `ANS`
- `Digest`: `14d1f7273d1a1d75710ba2f6619d6842d0e504bf83ccf3375d30036d65420772141b6041fa23b9d7025f8bba1c64beaa`
- Info `IsFTAB`: `False`
- Info `IsFirmwarePayload`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/ansf.t8160.release.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `AOP`
- `Digest`: `a8be918779ae2c1ddb8fbbb6d1d4db0535ab13121086d13e203a7defb7c1e5a16caafdd27a592beead05ac9c116fae74`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/AOP/aopfw-v68aop.RELEASE.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `AOP2`
- `Digest`: `abfbc6dc12c26f5c1587439022847317fa3895b8101e27bfd65913817d5360c8537aae8f5709db99b76dd6f7d25fe7df`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/AOP2/aop2fw-v68aop2.RELEASE.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `AVE`
- `Digest`: `b9030e94822ebb2cbf6f221c75ff0ff8104dd40ce0261813ff9a001f165b9b24e6778b3796ba10db64e05da16b861d61`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/ave/AppleAVE2FW_H19.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,ANE1`
- `Digest`: `051c0dc0bb17eed9933ff020d30d8d8e1d7c1570c6eb091de7164ae582f2ce5b1d0c467b497a867feacfc622cf2f905d`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/ane/h19_ane1_fw_perses_v6x.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,AVD`
- `Digest`: `a580555ba355aca0584aeb5fcde3c494cd965a9ad11abb6a435fd61dee77c8b156c92282247139e17f097c4308f063df`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/avd/AppleAVDFW_H19P.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,ApplePMCFirmware`
- `Digest`: `887e53baaf9f25ad1ef1fd97b1287cd2f195a5ad72b40af70585d943da1e4ba075f02d5cabbbe824774639566caa04cb`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/pmc/t8160pmcfw.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,AppleVideoEncoder0`
- `Digest`: `63e41e5d2bfa0328dfab9db0ffd464622575062c0622fa4732de2cadf58b273c7734f697cc9d1c1e056a7d5cdb107ff7`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/ave/AppleAVE2FW_H19_AVE0.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,AppleVideoEncoder1`
- `Digest`: `049e3519a25033b3033a130df46585b0f2f05555985fd3b0a8654b332f164cd49daf6b2384328906940a7f7a201a1585`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/ave/AppleAVE2FW_H19_AVE1.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,AppleVideoEncoder2`
- `Digest`: `19c0e781fee7cba72045d9ed90dc29c2c7101116685a6168d1dba6f9585a8a8c612d6e8e6bb87f601c12929109898358`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/ave/AppleAVE2FW_H19_AVE2.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,AppleVideoEncoder3`
- `Digest`: `5e1206584755555f9b4c6e3334f4c6c0bca650be8a53f5dd1448a629ff37e60e385bf54335e8b235edc8d3a848ba7e51`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/ave/AppleAVE2FW_H19_AVE3.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,AppleVideoEncoder4`
- `Digest`: `1adac89457306494c8b20c71d04df9ce5251241dd9e34395a8fe4453da82e673024dfd7c5b79cddd2c00af877f98d3be`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/ave/AppleAVE2FW_H19_AVE4.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,AppleVideoEncoder5`
- `Digest`: `63ff7021a0e26aab0bfe4e02ea3fa4925ec892b97dabaa21e8dd549a2aca1a80b7f420e0efbedec143fbbcf3cf6fa2f8`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/ave/AppleAVE2FW_H19_AVE5.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,AppleVideoEncoder6`
- `Digest`: `e62efe0891fc91f53f25b0772008b96d61d83d425dada746baac8b25990eaaf79b92af27a1ab38e2fe8605311d3bd863`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/ave/AppleAVE2FW_H19_AVE6.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,AppleVideoEncoder7`
- `Digest`: `223eda99b6bace8b6acbedbe0bbe4e38700ce20d666597e37fe57d1ad2e30ff5ad169fa5dce78661dc8a3c36d843fc20`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/ave/AppleAVE2FW_H19_AVE7.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,AppleVideoEncoder8`
- `Digest`: `05f79bc85c0600aa2c26f9fc3d8e0496d67d618a71ff4f01d880fd2dfdd3158d10bcbd183f55fb148e0c5b6f72b3242c`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/ave/AppleAVE2FW_H19_AVE8.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,AudioBootChime`
- `Digest`: `9e584ad82b3787c6e8f16678b959c331d48ccb5983f16216999b057bdbc6def30f8ba8bf0a050b4b385264452a3cba1e`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `True`
- Info `Path`: `Firmware/embeddedaudioresources/image4/v68-boot-chime.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,ExclaveOS`
- `Digest`: `e5068d05578a3d9ee1755e0db9618cbf326b558f2a467f1276364611a902f24f97e1519d5c46a30bbb052dfa22a9fda4`
- Info `ExcludeFromiBootSystemContainer`: `True`
- Info `HashMethod`: `sha2-384`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `141-27521-104.dmg.aea`
- Info `Personalize`: `False`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `Ap,ExclaveOSIntegrityCatalog`
- `Digest`: `414d318f25032cf9b4dfd74c45adcd3850dbf56ab847f55a70555d838a5455bd16d25b60f411a32d40838c8395556160`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/141-27521-104.dmg.aea.integrity_catalog`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `Ap,ExclaveOSTrustCache`
- `Digest`: `c11c6fe006449290640ff32a684eec66ec45fa2eba567206fe107e1980b71f4d831ba16df62ed1e734746c0e7b88e9d4`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/141-27521-104.dmg.aea.trustcache`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `Ap,ExclaveOSVolume`
- `Digest`: `e7d273a37772bbb870896c3bc97d83e21f848e762f6a2846254b2309924334ea8e8c029834308e5513e548d075826468`
- Info `ExcludeFromiBootSystemContainer`: `True`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/141-27521-104.dmg.aea.root_hash`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `Ap,GFX1Firmware`
- `Digest`: `33febef5d5a228984d2603f89e1b9ef78dfaae91d0167ae0fdaeb147a20c9ff25b1a79fcbdd1620384b95f1a43bbe0ad`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/agx/armfw1_g19p.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,HapticAssets`
- `Digest`: `9a85fd4f0a9f365ea646340f7ac597c0d39979d9c2a4cbb2ccca79ff81c5cc861a62d9e7ae53a29b71f183af3513ca38`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/V68_HapticAssets.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `False`

#### `Ap,LowPowerMode`
- `Digest`: `d72c01b171d40df1890d463dfb2b5911d53ecd66901f1606a1829767014c90d5cb0ae63c53fffe00bae7c45b2c2a9942`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `True`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/AppleLPM/AppleLPM.v68.release.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `False`

#### `Ap,MSRFirmware`
- `Digest`: `6c2611f3e8b5eaed277fce91ace8673d74e8dab2f938b8c80b72e4cd1ebe091e4c953c06330499553d54ac4b3de4045c`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/msr/t8160.msrf.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,MandoFW`
- `Digest`: `44624f1ad5411cbe0b5805b174c5a05dbf77bbd4d267f8eb2bd318d5364c3e3a0d96c1359f8850dc486141e7789cdaa3`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/V68_MandoFirmware.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `False`

#### `Ap,RestoreANE1`
- `Digest`: `d88874b6f35f6d3ff66e6918060c7ff1724aa8de5126e5665a5e204fe60786c2a565f900e6f36d97731aac4d8d8152e1`
- Info `Img4PayloadType`: `ran1`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/ane/h19_ane1_fw_perses_v6x.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,RestoreMSRFirmware`
- `Digest`: `4594142c48d515ef3d986a85fdf1d8c16ff030de561b578328f58b08850ae8544c0d25b4005c734686b586474034837f`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/msr/t8160.rmsr.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,RestoreSecureM3Firmware`
- `Digest`: `f4a3ee30ac0b966c872be05e9cf85b784a8363473952bff011c4d131ffae982fce7eb3d6ffbc7206c1545baa76f6ad75`
- Info `Img4PayloadType`: `rsm3`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/M3/bin/securem3fw-v68.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `Ap,RestoreSecurePageTableMonitor`
- `Digest`: `c9e66676240d53abb09022bb1d63972ba82a49ae7edce2a118174fae514e58adf4ef8bdf5d1015047dc29c42eb974c1b`
- Info `Img4PayloadType`: `rspt`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/sptm.t8160.release.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `Ap,RestoreTrustedExecutionMonitor`
- `Digest`: `75371b6d03b94162e4e95077067ab36dc4eb92ddbc78574be819b79ebd2399e816ae4416c995e01d597376d729f5a0a1`
- Info `Img4PayloadType`: `rtrx`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/txm.iphoneos.release.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `Ap,RestorecL4`
- `Digest`: `f7846005a0bfd5a07116a05cb9084b8bcd58b56e593e95d5d6a94db71329dbcc9b64adc70b1174d100c7c75bed413baa`
- Info `Img4PayloadType`: `rxcl`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/image4/exclavecore_bundle.v68.RELEASE.restore.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `Ap,SecureM3Firmware`
- `Digest`: `9b9075693ce1ecd88a4952a1529681d9d13412933cb63079d4873bbd510813d422adf8d241617bf139651447372bfbcd`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/M3/bin/securem3fw-v68.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,SecurePageTableMonitor`
- `Digest`: `2f69cb8b9dc4932ffbb28f4bf7ce6712b46e8d3a90367255646779b94aa28895cd6220da5884f6d5dea8715e8b91f737`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/sptm.t8160.release.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,SystemVolumeCanonicalMetadata`
- `Digest`: `5d99f6cc85a80b45ee2e2269ffc9de71339b5cdd1fed01519af43c6baefd2250d44c4f21f1bb99c93002e76fb42ec0af`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/141-28898-095.dmg.aea.mtree`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `Ap,TrustedExecutionMonitor`
- `Digest`: `e9f0a0a9f060553dcba6de84e0cd4b70c381bf3a174168282843fc12cd01509d6071e6286a13022652cfab95189c3c5b`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/txm.iphoneos.release.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `Ap,cL4`
- `Digest`: `c52af32219d872a04f421d10a74e181601a049a4611a906e687807e355102e1085d61892f5e0d0a9750ce56b4ff76863`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/image4/exclavecore_bundle.v68.RELEASE.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `AppleLogo`
- `Digest`: `72e55666b43d92ae01875414c1a25d8809ccde5b720b7d42749d6d3bcda2031bd48561b7a83ebaa4da10299bc2e62634`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `True`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/all_flash/applelogo@2d~iphone.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `BMU,DigestMap`
- `Digest`: `a217a7c58314ae739da9a12c9788affb98ee223a5774f5863d49a071c11cbad6`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Volchok/BAT8193/DigestMap.der`
- Info `Personalize`: `True`

#### `BMU,FirmwareMap`
- `Digest`: `b87e189151c508daaf1029e9dd2a558bb292b9ffa98fc0b1c2a859ba139d3bd5`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Volchok/BAT8193/FirmwareMap.plist`
- Info `Personalize`: `True`

#### `BMU2,DigestMap`
- `Digest`: `a217a7c58314ae739da9a12c9788affb98ee223a5774f5863d49a071c11cbad6`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Volchok/BAT8193/DigestMap.der`
- Info `Personalize`: `True`

#### `BMU2,FirmwareMap`
- `Digest`: `b87e189151c508daaf1029e9dd2a558bb292b9ffa98fc0b1c2a859ba139d3bd5`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Volchok/BAT8193/FirmwareMap.plist`
- Info `Personalize`: `True`

#### `Cellular1,CdpAscDl`
- `Digest`: `9bb48fff8021c91f3f9ce98a38c19ef89399272bcd487c6a6b4bcc777b1dda566e59fb74d2d8089462bb843b1babb0ce`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/c4020iphone/Release/patched/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Cellular1,CdpAscUl`
- `Digest`: `c0e59a3e3ffbd3b5c75428fb36432facabc745944296ff515f737c4fef4efc64586809f7a16f56354a1eaecf2aa8d774`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/c4020iphone/Release/patched/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Cellular1,CdpHost`
- `Digest`: `8d30be1ec9e53237500b942bdabdd2477b6f3337c86a57053e3b2ed5be37baf8cb40b0c8882f5d8a6bc3cc0c38735de9`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/c4020iphone/Release/patched/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Cellular1,L1CL1S`
- `Digest`: `46e0cdcb8acbca7a0ce1ea1672227796130091b7abe75f5fa14d430f370edd93d8b434a7e7df09012657b589b43a7081`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/c4020iphone/Release/patched/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Cellular1,LLB`
- `Digest`: `162f084d64d6ba1ea7d26fd9a94362aa914ac87f0b55b27f5ef35fc6a083666319dd15a3d8748ed32d85ea54787f2d05`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/c4020iphone/Release/patched/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Cellular1,PMUFW`
- `Digest`: `33e1a57e7ba21e87c045b6f85a1fbe1732285f7151962cf6c3cd3f83dbe45745cf2ed60ed5e266851b6d0b1dc733f541`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/c4020iphone/Release/patched/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Cellular1,PMUFW2`
- `Digest`: `024bbc34f73996a33ab5b2e39ce36b158fb336f8d7cd7b7027e2c0ace73bb004c53cb948b03df45f8ef31de51041fe88`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/c4020iphone/Release/patched/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Cellular1,RTKitOS`
- `Digest`: `9ccde882d2e3679418efc6f95b12e7d77d16081ecc9432dd510519cd5f6d773cfbdffee5fc6fe0505cbc6677b1e83e54`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/c4020iphone/Release/patched/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Cellular1,Recipe`
- `Digest`: `e7cb1b15c3717f42a127a35b5506d720f2d58971e781cbe731c87cc96aac422973337922eb80e5ed6695501c35d8168d`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/c4020iphone/Release/patched/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Cellular1,iBootData`
- `Digest`: `45b76cdcd9e32532b492018443e65eb3757a404c02555e76ccb4722eaa69130d76e1d7bba88042f3cf9767e48857df7b`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/c4020iphone/Release/patched/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Cryptex1,AppOS`
- `Digest`: `87f11143323631088cb240ce81efea1106fc9d365f56fb41be851cdf28730b560680cd65b9a3e16e87a99c7604390f22`
- Info `HashMethod`: `sha2-384`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `141-28395-106.dmg`
- Info `Personalize`: `False`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`

#### `Cryptex1,AppTrustCache`
- `Digest`: `7072d57c04de1ffdcddabf6f3e65d8ce2099f2f22245369ccb56c7c3b7432359e5e108f54cd423d4358266db667110b6`
- Info `HashMethod`: `sha2-384`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/141-28395-106.dmg.trustcache`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`

#### `Cryptex1,AppVolume`
- `Digest`: `e3a31ede1b5fdbb0926a736bbf51e45869f925f57ac839fecb3192a8d5ba5c9c8194eee786baa64e8fb74e3945bc11a9`
- Info `HashMethod`: `sha2-384`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/141-28395-106.dmg.root_hash`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`

#### `Cryptex1,SystemOS`
- `Digest`: `597a37020cb5123afbcbf78f749f4b8e1a6fba94e7dc22322495728c9a2ad9070bf4a7307e7fc9a1c30a6073678758a6`
- Info `HashMethod`: `sha2-384`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `141-28400-098.dmg.aea`
- Info `Personalize`: `False`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`

#### `Cryptex1,SystemTrustCache`
- `Digest`: `fa1bbcbdaa387a71ba17cae7d6d3dbe846aa4e8835ca047e3b0cbf2e7e742bdc1bff9bae1a10e879d6eaf8374d3fd181`
- Info `HashMethod`: `sha2-384`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/141-28400-098.dmg.aea.trustcache`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`

#### `Cryptex1,SystemVolume`
- `Digest`: `9bfa3a33afdde3318fbf044538eb669b8f9a2f20b4c5bed0028249cc1b565377b8df1e6d48e027b151ebb5cfd0037d99`
- Info `HashMethod`: `sha2-384`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/141-28400-098.dmg.aea.root_hash`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`

#### `DCP`
- `Digest`: `aefaf09c5156cd037df5a0213fe1eb1e797cf3b68d1fcb7c8c300eae33eddbaf1b387379ee4a76049fe5acf9304253f4`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `True`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/dcp/t8160dcp.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `DeviceTree`
- `Digest`: `a3b521b47aa0f0540ac943eb5afab35b123789358cd16b74e394db195fdbc000bae4adb8b3e2c06b9555034e86269f76`
- Info `IsFTAB`: `False`
- Info `IsFirmwarePayload`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/all_flash/DeviceTree.v68ap.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `GFX`
- `Digest`: `40c7cc60cbda687879663afb4c02f0293531e4a372e5247a2d986276853a7ae2f5f5887e5e0dd0359bb194696c894cf1`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/agx/armfw_g19p.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `ISP`
- `Digest`: `33b6bdc438ecbe1bdfe93f88700d230813ffde3943f1df799a4d69a1ea36b6b2bea61ee51ce971cc578624668eeebc9f`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/isp_bni/adc-boreas-v68.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `KernelCache`
- `Digest`: `9f57d7cf359fc7671d295630bb82f9909ead4c9f41b80b34e8248f3519de737e29c5e1069e48d40d49772b389d176201`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `kernelcache.release.v6x-pandia`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `LLB`
- `BuildString`: `iBoot-15391~1757`
- `Digest`: `302b40b9dbf4070bb0fa4e4215b222b81ad70b1557a03e354f057e3bac40c3136d707e6734924b3456312a8e767631bf`
- Info `IsFTAB`: `False`
- Info `IsFirmwarePayload`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/all_flash/LLB.v68.RELEASE.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'DPRO': True}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductionMode': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresIm`
- `MemoryMap`: `6480728002000000040000006880728002000000040000000801051102000000080000003002e4110200000008000000f849e4110200000008000000000005110200000008000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000`
- `RawDataDigest`: `2e62b37b6485cc3814fd1cfda528062cac98afd2cb365a23fc5b5a76231ae832f73c74e64b5f17f17195d50d6591a698`
- `Trusted`: `True`

#### `LeapHaptics`
- `Digest`: `8afa6138a6d3be9b7fc121d0afefabd41330555a8a3b4915200b9c804531b6238ce070122ba5e1c9632135165738e065`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/V68_LeapHapticsFirmware.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `False`

#### `Liquid`
- `Digest`: `194aaed667db6adaa64d1c9250667a24bf0fb8b94939256a3bbf3958681d7fbd444416e5eda5617964221cc64feda25d`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `True`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/all_flash/liquiddetect@2d~iphone.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `MtpFirmware`
- `Digest`: `270a440ad64cb8582dc2cfef143d513b2a3714afa8c690b2bf2f568fdd31271276ed120cd549dd6997a2020feb3bfe77`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/V68_MtpFirmware.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Multitouch`
- `Digest`: `7368509e073e8c3bbe4f93e101879b48e0f1b3b044038976d643093f87378ccfe88ea58cc6e5afe26933ca94acf4c477`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/V68_Multitouch.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `False`

#### `OS`
- `Digest`: `b1d8bce0e16a7548ac7f3e6a243720965ef8461eda3034e0ea8eaef38b9676d6499b46e6dba99c3f109a8206133480b9`
- Info `HashMethod`: `sha2-384`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `141-28898-095.dmg.aea`
- Info `Personalize`: `False`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `PMP`
- `Digest`: `19008a2bc4a04e1b7ea69fd82e585ea96246e5e3a6ad8718ae0ad9bec05521fbf7770b62c26f1263f1b5a59cf0c4af4b`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/pmp/t8160pmp.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Rap,RTKitIOConfig`
- `Digest`: `6b1013023f1c7479108eef02f6d78f03113b687efbcff90b17d9beca0445f96b0ebac5630f6599b54d3d8e63d164f364`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Rose/r2p1/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Rap,RTKitOS`
- `Digest`: `e46b5fd033a4a73604477ece10221dc011355e265d12086c4a9bdde103094b9c0f89c516bc92f4744660bd66f2f408ef`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Rose/r2p1/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Rap,SoftwareBinaryDsp1`
- `Digest`: `7300dc26d19b540e06204e17e2c34cec3eafc3759cd12b22eac0e14e45d64fd53a38a436a009aece07836f0da32e8446`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Rose/r2p1/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `RecoveryMode`
- `Digest`: `848e2e1ba471a38985b09e96b375b4dc812e101f29b1a109887ae1f46ec41648d11da5a2493434ec091e33c72fbd93df`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `True`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/all_flash/recoverymode@2d~iphone.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `RestoreANS`
- `Digest`: `c60c3b84b45ea4f06c28cbd059377d2ba69f6afce9558d7e578483e45291ddc489b452ff3fcc8a0c98ed5b4306a7bd92`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/rans.t8160.release.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `RestoreDCP`
- `Digest`: `39063050c7616fc6ee7b1dc3b3a1d7ddf8d33f39ca3be62f1fe20638f51f07349463e777a9cdbb944d9afd3d83fbf5fe`
- Info `Img4PayloadType`: `rdcp`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/dcp/t8160dcp_restore.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `RestoreDeviceTree`
- `Digest`: `94cbc3d7c32dfcad8107dca33a68d57d63eed74e57941dde950f8685e5437107e60c664cbdceb25a22a5bbdda95e4ae3`
- Info `Img4PayloadType`: `rdtr`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/all_flash/DeviceTree.v68ap.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `RestoreKernelCache`
- `Digest`: `14a743b0cc147a9480dea7708fc3e5310fa89174656296649188e59c40ca531f44b870ed2b795522fcd6bdc51298b06f`
- Info `Img4PayloadType`: `rkrn`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `kernelcache.release.v6x-pandia`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `RestoreLogo`
- `Digest`: `0f7534a7d9c2761a6401e49ef5d826178a7254f6c052c7cde5d99bdba1cbfda71a304e5d43bea1a7b17812975e9b487e`
- Info `Img4PayloadType`: `rlgo`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/all_flash/applelogo@2d~iphone.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `RestoreRamDisk`
- `Digest`: `5398834502bc9ecc6be905da1f9e4be03c75c85bd1c5c1ac52e08f808aba5c14ecfcb7e7a78a2f349b10b91b7c81a3ac`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `141-29011-104.dmg`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `RestoreSEP`
- `Digest`: `6333efcf0bc6eccfd1b3e879911304bea043d007be0446167aa3cc666598b605e52ef185c48418fa91fa8bcca28939bf`
- Info `Img4PayloadType`: `rsep`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsSecondaryFirmwarePayload`: `True`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/all_flash/sep-firmware.v68.RELEASE.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'ESEC': False}, 'Conditions': {'ApRawSecurityMode': False}}, {'Actions': {'ESEC': True}, 'Conditions': {'ApRawSecurityMode': True}}, {'Actions': {'DSEC': True, 'ESEC': False}, 'Conditions': {'ApDemotionPolicyOverride': '', 'ApRawProductionMode': False, 'ApRawSecurityMode': True}}, {'Ac`
- `MemoryMap`: `000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000`
- `ObjectPayloadPropertyDigest`: `2b8d753529cd508e1a554eed82d7b8dafdcc64736a007453938f23006f0d51139bb0e78ea1f99a0233e4d37b891e9d16`
- `RawDataDigest`: `ce336e482b48402ee816475232d12e9a6dbc7aa138256a1efc2aef36cec5830d8b164d96bd716fb678f0f8be43765611`
- `TBMDigests`: `07acf0061948b097cb65709af43c70f06b51ebc4ac35905ad9bd52f00bb02524a58c0a8cae32e368597b52ec792fc26de436b7988ddffd36523ddb679caa2cc3538088049388d679fa143b955a5e1285afea75c9f0aa0ad9c3dc3f2922d2ad577ea975d9c01166af949d66fb105444985d79af4bb62dc566aaf1e9e7a6928981023268b752cbfb587e97b0bb865c426d95045524af0a75f4e0ee1ddaa192ddb909c91195ae0c269dca390d4d145b2afae46d3c62df4fc9a016a1b04d1ed79e69fc15c98b9e86190f354c80102ed5d06f4c1215853ae50ece2538fd90686ee25a5e7587ac428512b248c64b417306d272`
- `Trusted`: `True`

#### `RestoreTrustCache`
- `Digest`: `a4cf99fcabdad855223954a80750332eb8e4bbf09bc6b005d912c05a70c4ff6bdd8831daf795e16527d7f0d7dd20c8eb`
- Info `Img4PayloadType`: `rtsc`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/141-29011-104.dmg.trustcache`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `SE,RapRTKitOS`
- `Digest`: `e46b5fd033a4a73604477ece10221dc011355e265d12086c4a9bdde103094b9c0f89c516bc92f4744660bd66f2f408ef`
- Info `Img4PayloadType`: `rkos`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Rose/r2p1/ftab.bin`
- Info `Personalize`: `False`

#### `SE,RapSwBinDsp`
- `Digest`: `7300dc26d19b540e06204e17e2c34cec3eafc3759cd12b22eac0e14e45d64fd53a38a436a009aece07836f0da32e8446`
- Info `Img4PayloadType`: `sbd1`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Rose/r2p1/ftab.bin`
- Info `Personalize`: `False`

#### `SE,UpdatePayload`
- `DevelopmentUpdatePayloadHash`: `fdb79271bb26f2f490782b97a01621656e291e612bba82a0d51c070963ee90a1`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/SE/Stockholm91.RELEASE.sefw`
- Info `Personalize`: `True`
- `ProductionUpdatePayloadHash`: `40e6ac72e7665b06e7633ee692ed9d8a838f18ea4af387e15dcde09c62bfd4b5`

#### `SEP`
- `Digest`: `a4e4c8fcba2b9a783553d195a2f3addc07d62cd1dc56896aa8f0d8f82e5c84588e40391f3a356ae595b85cd060e3c248`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsSecondaryFirmwarePayload`: `True`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/all_flash/sep-firmware.v68.RELEASE.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'ESEC': False}, 'Conditions': {'ApRawSecurityMode': False}}, {'Actions': {'ESEC': True}, 'Conditions': {'ApRawSecurityMode': True}}, {'Actions': {'DSEC': True, 'ESEC': False}, 'Conditions': {'ApDemotionPolicyOverride': '', 'ApRawProductionMode': False, 'ApRawSecurityMode': True}}, {'Ac`
- `MemoryMap`: `000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000`
- `ObjectPayloadPropertyDigest`: `2b8d753529cd508e1a554eed82d7b8dafdcc64736a007453938f23006f0d51139bb0e78ea1f99a0233e4d37b891e9d16`
- `RawDataDigest`: `ce336e482b48402ee816475232d12e9a6dbc7aa138256a1efc2aef36cec5830d8b164d96bd716fb678f0f8be43765611`
- `TBMDigests`: `4f9b357da6a251c413dfa30c0f7fb382260b1fdc311e0321c8c78d04512375e8bf46103d787a27cf8695f8843ea068e3fcd750bba68cd7b510f27de03d8636a1a727f00fac5fb9ba7d96306c1a0bdfa11f89ba3375c61b26a1d6c3e07191341558f63c8c1bc13dd68862b47353fadea69364c5b9696e14c65ee250142655fe111685e9fce6f35863eac15db5df9d2101ec14a7658b5760e7358aad4598926a9fe1634914815278410007db1b8fb5d19842c763c6cc2941413fef7c3f5a92ac1c71c3fd355821d378b011d7d0184d64e98292be2737f951ee6d48dfc229481ec53300fb6cac73324f97cf1be7697a2647`
- `Trusted`: `True`

#### `SIO`
- `Digest`: `8873ba2b293fc1144f3fbc9780492ffea17cbac9c3ab5b182ce19ec789d6b75a2b2e3c603dc135bfda6cd21ca3ee7344`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/SmartIOFirmware_ASCv8.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `SepStage1`
- `Digest`: `58a738a8ef5bbc8b36b56d9637cea87db2c6f54634de65755eb9ad4f9d7cb4dcbb80eb0d6e8fb0b15a3ec7b975feb35c`
- Info `Img4PayloadType`: `stg1`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsSecondaryFirmwarePayload`: `True`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/all_flash/sep-patches.v68.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EnableGid0ForNextStage': True}, 'Conditions': {}}, {'Actions': {'ESEC': False}, 'Conditions': {'ApRawSecurityMode': False}}, {'Actions': {'ESEC': True}, 'Conditions': {'ApRawSecurityMode': True}}, {'Actions': {'DSEC': True, 'ESEC': False}, 'Conditions': {'ApDemotionPolicyOverride': ''`
- `MemoryMap`: `000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000`
- `ObjectPayloadPropertyDigest`: `5242f6de7bceb54f81e79d072c7b12bb8d74235561af15029d720cff3fa6a719c96a9e5900b5f279ecaa39c2f16d9034`
- `RawDataDigest`: `5eee7fcf6e3c9c425834179d18c809cd4cc31a863170f350332938ac15bbb8b50e28e92f552cf3b9007bc101f4e35199`
- `Trusted`: `True`

#### `StaticTrustCache`
- `Digest`: `f9fd4c9b274ca337a1c1c0864f6b42bc62e570149d14fcd60d9a8702c1330656974d2fab9554ebf7300aa2d9ef84500f`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/141-28898-095.dmg.aea.trustcache`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `SystemVolume`
- `Digest`: `23684e5cf582fcdde50c305d64f0510f0f608b7128edd7386937636e933f399ecb35e51db91374af4c8aba3c14fe1944`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/141-28898-095.dmg.aea.root_hash`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `WCHFirmwareUpdater`
- `Digest`: `ee119dfcfbb36a8e300f3c169678af57a6dd2328bd5c1368ee4bf285208d20a452246acd87bb4dea7b55b44c4d45287b`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `True`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/WirelessPower/WirelessPower.v68.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,ACIBT`
- `Digest`: `51c01d433c414fa22f7769dad787f55f3fd2de1e308607402da015d423ef5bc0929a525f4d7038d20349509749573d50`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,ACIBTLPEM`
- `Digest`: `1f9a194a2e7aaa3825af77a23dd7f71d6e6b05a94f2aa181d653a885c6c09b3291a3adcc4d6a30ce9a455324dc88f97c`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,ACIBTManuf`
- `Digest`: `51c01d433c414fa22f7769dad787f55f3fd2de1e308607402da015d423ef5bc0929a525f4d7038d20349509749573d50`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,ACIWIFI`
- `Digest`: `902b5adeacd5144fb149f7b3d87c64b0ef7276c13cb92cf7e8e73d4f22ba743dd73f0b920f539e0bfb95ab3f4e3bcbb1`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,ACIWiFiTxManuf`
- `Digest`: `36423b324369661e34da69383f486a7f30838e99a7f7756d74254ecbdf951ca7397ce33d96e05b4dc0d2f590def4c66a`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,BTSecondary`
- `Digest`: `ebd59be4d27b01a4e1a696feb77a6aa10a75087f609efaff2e0f0ce3215113e74b0de656ee29eb9835d6a751b11ae931`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,BTSecondaryManuf`
- `Digest`: `ebd59be4d27b01a4e1a696feb77a6aa10a75087f609efaff2e0f0ce3215113e74b0de656ee29eb9835d6a751b11ae931`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,CCPUApplicationFirmware`
- `Digest`: `45f576ce687be46effa69e4d48584543abe24bb1684e137fe2ac3a307828c0e9024302bf437530d5f1c3c4dc99ab2eea`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,CoexRealTimeArbiter`
- `Digest`: `44749c87da9b89c1e09056d09de81bf1bcc7125480a78db8424e9583d5be8df4f861c9d31813a8c1806398d0c18941ec`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,PhyBlueTooth`
- `Digest`: `181d64d765b57b4e3167ce24151b847f99c713b84bd75abe67708f2abbc66be9a0b1c2ac6b97733ff0132732efa9040e`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,PhyBlueTooth5G`
- `Digest`: `8c0742a5e9ad20e1254c7355de8386dcb335305c0977edbdb3778c149f063353713f8004479930c0b81f44f49b1f3e02`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,PhyBlueTooth5GManuf`
- `Digest`: `8c0742a5e9ad20e1254c7355de8386dcb335305c0977edbdb3778c149f063353713f8004479930c0b81f44f49b1f3e02`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,PhyBlueToothLPM`
- `Digest`: `b0b972453c81fc0327ead8a21c73630cb4d516ee0f7d542181bef7493f68f956da73d4174dd40b41faa2138cda04739d`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,PhyBlueToothManuf`
- `Digest`: `181d64d765b57b4e3167ce24151b847f99c713b84bd75abe67708f2abbc66be9a0b1c2ac6b97733ff0132732efa9040e`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,PhyBluetooth5GTrim`
- `Digest`: `94c974402ac11c7180cb8b14686c18ec353565b2590ce8a709a5cd5d6c26e6b94f24950c03d623e037cecc3d9e582b50`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,PhyBluetoothTrim`
- `Digest`: `3820e32dc8f92bf00be0cc9eeda45317d7f37d600236bd0e1f54a993f1e5d87d6094b4536f56a3ac75179c33fb9505cc`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,RTKitOS`
- `Digest`: `8219626cc42aae1765e87b3c3f8034530f66a23bc1fd3bfdeb69b578c14e78590daec9c28d75c5b9f917f1aacdd68cf6`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,RTKitOSLPEM`
- `Digest`: `be6863c3d47047bde6b35529fa3f3d9eb88b4678531ef6cf7966ffb85b6fc8408b12a745b7ad07f30f8898ccd073cb4a`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,ScanBTLPEM`
- `Digest`: `3c449b8c373522b5025c3161008797cd14cb0907d29e7ccf521ac55a2085553801aebd1545557fba6700a8c7149407ae`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,ScanBTManuf`
- `Digest`: `f890cbeafa0ccbeb427962f17b48f603feff8561172a98d231ed8205e81e30146f04df9e096776d80dafd3d347a53cbd`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,ScanBluetooth`
- `Digest`: `f890cbeafa0ccbeb427962f17b48f603feff8561172a98d231ed8205e81e30146f04df9e096776d80dafd3d347a53cbd`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,ScanWifi`
- `Digest`: `14f68624a65887fa965c6ddf6d01b2b1027db493a891ddcef52454f1a8939ddcfcb7d1d668e857d9353a344de6275289`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,ScanWifiManuf`
- `Digest`: `611a45ae78230635ae909126967e6783cd39e6bda0c3e28d5e87360bc1144756308a86c1b18574652053b727c0b482c1`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,WiFiRx`
- `Digest`: `00751f9522d1e2e3a2b5684278fb36ff6925949b46e878efd797cfde49c32cdb7286856a7ead45383646538e1a487294`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,WiFiRxManuf`
- `Digest`: `43b50d30fed4c6befc3704b461841679cd339fdd85fa06d8a28fe08b83f13ade2a7a8de0c0d1957f8febcff31a0ee3c6`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,WiFiTx`
- `Digest`: `b28a762c0e1d7d947f2f728c3ea45afe5940eb0785f2f10689c17fc23c5fa40cbbec821fab3673637ae1da9f340253b4`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,WiFiTxManuf`
- `Digest`: `da7ad47bb37867fc46f85ebff1f2d02204382ad199efaed984d7f433165cf0377c83afce9477707cd7bb04a584bb238e`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,Wifi2GLMAC`
- `Digest`: `2d0a90a6fcd00801a8381b3111cc4b15ed9e9093de81c6b9dec26025466376bea66f53ebd7112161dfce217b69f01315`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,Wifi2GLMACManuf`
- `Digest`: `3e72c8dbb12e0c77dca7685815aa628373702b63d5b2155e44fd1152f0f560706d38bd019f3ad3b70ffe51a27d3e1566`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,Wifi2GLPhy`
- `Digest`: `847eca454fc4f9f4970ecec9b1fe41dc2649a1ebbfac48747a432a484089f94f300cd1381bce6e186a2802a144d0c28b`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,Wifi2GLPhyManuf`
- `Digest`: `847eca454fc4f9f4970ecec9b1fe41dc2649a1ebbfac48747a432a484089f94f300cd1381bce6e186a2802a144d0c28b`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,Wifi2GLPhyTrim`
- `Digest`: `afc1e501998b0b550ca0f2ea81ac94a37fde226bff043a61eb0f1178575f68da86197e0e667374855cc77a70cd5f78d7`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,Wifi5GLMAC`
- `Digest`: `bedce67d68535076b21cb535a67e61eec4bcfc95637a395f465a2cbafde3b987dea3cc3c9c41ccb56c2020daefd6de66`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,Wifi5GLMACManuf`
- `Digest`: `2372fd4b17cc6eef67f8281125fca7f57a75a36ab005a568763a40defc9cdaa88deb0290a3a7158a5d9e0068e134189f`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,Wifi5GLPhy`
- `Digest`: `d528706af0b66fe115912d7bba9185a176d41b4eddda8e09b107d78d652eecb98a4b38cc0c671d4a068d0ff142ea1d4c`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,Wifi5GLPhyManuf`
- `Digest`: `d528706af0b66fe115912d7bba9185a176d41b4eddda8e09b107d78d652eecb98a4b38cc0c671d4a068d0ff142ea1d4c`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,Wifi5GLPhyTrim`
- `Digest`: `c8dac484934f456d998a8d7438c0d577ea2e660e81330fff47a7497558de462c3a594557c00e652eb30a4e90ba64fa3b`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,WifiRegData`
- `Digest`: `03adb4c5ce95a3dab17572b4c73dfcdbdacef0ab31f6f98372f7356ac38eb839e65f69469fa78b685499cfadf90414f2`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `YonkersIR1,SysTopPatch0`
- `Digest`: `9c7c82fa00263d5265d6210eec68223618fa474ab5f02e2ed635e770d10a5ce3`
- `EPRO`: `False`
- `FabRevision`: `49409`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Lakeville/YonkersIR1,SysTopPatch0`
- Info `Personalize`: `True`

#### `YonkersIR1,SysTopPatch1`
- `Digest`: `052b9ec06213a1db74d7e45917d9bbf1d41b487eb647f3e14032ed1b37a2c1bf`
- `EPRO`: `True`
- `FabRevision`: `49409`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Lakeville/YonkersIR1,SysTopPatch1`
- Info `Personalize`: `True`

#### `YonkersIR1,SysTopPatch2`
- `Digest`: `9c7c82fa00263d5265d6210eec68223618fa474ab5f02e2ed635e770d10a5ce3`
- `EPRO`: `False`
- `FabRevision`: `49473`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Lakeville/YonkersIR1,SysTopPatch2`
- Info `Personalize`: `True`

#### `YonkersIR1,SysTopPatch3`
- `Digest`: `052b9ec06213a1db74d7e45917d9bbf1d41b487eb647f3e14032ed1b37a2c1bf`
- `EPRO`: `True`
- `FabRevision`: `49473`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Lakeville/YonkersIR1,SysTopPatch3`
- Info `Personalize`: `True`

#### `YonkersIR1,SysTopPatch4`
- `Digest`: `9c7c82fa00263d5265d6210eec68223618fa474ab5f02e2ed635e770d10a5ce3`
- `EPRO`: `False`
- `FabRevision`: `49729`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Lakeville/YonkersIR1,SysTopPatch4`
- Info `Personalize`: `True`

#### `YonkersIR1,SysTopPatch5`
- `Digest`: `052b9ec06213a1db74d7e45917d9bbf1d41b487eb647f3e14032ed1b37a2c1bf`
- `EPRO`: `True`
- `FabRevision`: `49729`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Lakeville/YonkersIR1,SysTopPatch5`
- Info `Personalize`: `True`

#### `YonkersIR1,SysTopPatch6`
- `Digest`: `9c7c82fa00263d5265d6210eec68223618fa474ab5f02e2ed635e770d10a5ce3`
- `EPRO`: `False`
- `FabRevision`: `43690`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Lakeville/YonkersIR1,SysTopPatch6`
- Info `Personalize`: `True`

#### `YonkersIR1,SysTopPatch7`
- `Digest`: `052b9ec06213a1db74d7e45917d9bbf1d41b487eb647f3e14032ed1b37a2c1bf`
- `EPRO`: `True`
- `FabRevision`: `43690`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Lakeville/YonkersIR1,SysTopPatch7`
- Info `Personalize`: `True`

#### `YonkersIR1,SysTopPatch8`
- `Digest`: `bf0b187d19186250b12f1bd5a3ce4def94004816a346c3c4f6df914f8c63d2a3`
- `EPRO`: `False`
- `FabRevision`: `49730`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Lakeville/YonkersIR1,SysTopPatch8`
- Info `Personalize`: `True`

#### `YonkersIR1,SysTopPatch9`
- `Digest`: `cbb72635c6f3ab38b4047515ea1471253f3cfa5fc301e7dced9f62b4065af7f7`
- `EPRO`: `True`
- `FabRevision`: `49730`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Lakeville/YonkersIR1,SysTopPatch9`
- Info `Personalize`: `True`

#### `YonkersIR1,SysTopPatchA`
- `Digest`: `bf0b187d19186250b12f1bd5a3ce4def94004816a346c3c4f6df914f8c63d2a3`
- `EPRO`: `False`
- `FabRevision`: `49986`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Lakeville/YonkersIR1,SysTopPatchA`
- Info `Personalize`: `True`

#### `YonkersIR1,SysTopPatchB`
- `Digest`: `cbb72635c6f3ab38b4047515ea1471253f3cfa5fc301e7dced9f62b4065af7f7`
- `EPRO`: `True`
- `FabRevision`: `49986`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Lakeville/YonkersIR1,SysTopPatchB`
- Info `Personalize`: `True`

#### `YonkersIR1,SysTopPatchC`
- `Digest`: `bf0b187d19186250b12f1bd5a3ce4def94004816a346c3c4f6df914f8c63d2a3`
- `EPRO`: `False`
- `FabRevision`: `52428`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Lakeville/YonkersIR1,SysTopPatchC`
- Info `Personalize`: `True`

#### `YonkersIR1,SysTopPatchD`
- `Digest`: `cbb72635c6f3ab38b4047515ea1471253f3cfa5fc301e7dced9f62b4065af7f7`
- `EPRO`: `True`
- `FabRevision`: `52428`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Lakeville/YonkersIR1,SysTopPatchD`
- Info `Personalize`: `True`

#### `YonkersIR1,SysTopPatchE`
- `Digest`: `bf0b187d19186250b12f1bd5a3ce4def94004816a346c3c4f6df914f8c63d2a3`
- `EPRO`: `False`
- `FabRevision`: `56797`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Lakeville/YonkersIR1,SysTopPatchE`
- Info `Personalize`: `True`

#### `YonkersIR1,SysTopPatchF`
- `Digest`: `cbb72635c6f3ab38b4047515ea1471253f3cfa5fc301e7dced9f62b4065af7f7`
- `EPRO`: `True`
- `FabRevision`: `56797`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Lakeville/YonkersIR1,SysTopPatchF`
- Info `Personalize`: `True`

#### `YonkersIR2,SysTopPatch0`
- `Digest`: `766c1906a4df7abea032957e6358e8f0948cd63a17b946de81e900b46e2fe30f`
- `EPRO`: `False`
- `FabRevision`: `49409`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Glenbrook/YonkersIR2,SysTopPatch0`
- Info `Personalize`: `True`

#### `YonkersIR2,SysTopPatch1`
- `Digest`: `dd99f434a5980c4b0779aee077d3d86c97f2739b6299540efabd33e740874230`
- `EPRO`: `True`
- `FabRevision`: `49409`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Glenbrook/YonkersIR2,SysTopPatch1`
- Info `Personalize`: `True`

#### `YonkersIR2,SysTopPatch2`
- `Digest`: `766c1906a4df7abea032957e6358e8f0948cd63a17b946de81e900b46e2fe30f`
- `EPRO`: `False`
- `FabRevision`: `49473`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Glenbrook/YonkersIR2,SysTopPatch2`
- Info `Personalize`: `True`

#### `YonkersIR2,SysTopPatch3`
- `Digest`: `dd99f434a5980c4b0779aee077d3d86c97f2739b6299540efabd33e740874230`
- `EPRO`: `True`
- `FabRevision`: `49473`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Glenbrook/YonkersIR2,SysTopPatch3`
- Info `Personalize`: `True`

#### `YonkersIR2,SysTopPatch4`
- `Digest`: `766c1906a4df7abea032957e6358e8f0948cd63a17b946de81e900b46e2fe30f`
- `EPRO`: `False`
- `FabRevision`: `43690`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Glenbrook/YonkersIR2,SysTopPatch4`
- Info `Personalize`: `True`

#### `YonkersIR2,SysTopPatch5`
- `Digest`: `dd99f434a5980c4b0779aee077d3d86c97f2739b6299540efabd33e740874230`
- `EPRO`: `True`
- `FabRevision`: `43690`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Glenbrook/YonkersIR2,SysTopPatch5`
- Info `Personalize`: `True`

#### `YonkersIR2,SysTopPatch6`
- `Digest`: `766c1906a4df7abea032957e6358e8f0948cd63a17b946de81e900b46e2fe30f`
- `EPRO`: `False`
- `FabRevision`: `48059`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Glenbrook/YonkersIR2,SysTopPatch6`
- Info `Personalize`: `True`

#### `YonkersIR2,SysTopPatch7`
- `Digest`: `dd99f434a5980c4b0779aee077d3d86c97f2739b6299540efabd33e740874230`
- `EPRO`: `True`
- `FabRevision`: `48059`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Glenbrook/YonkersIR2,SysTopPatch7`
- Info `Personalize`: `True`

#### `YonkersIR2,SysTopPatch8`
- `Digest`: `7f2c2fa99478bc52f047cffed36dc3fea3e617113a4788b55b18be2470f97c9c`
- `EPRO`: `False`
- `FabRevision`: `49474`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Glenbrook/YonkersIR2,SysTopPatch8`
- Info `Personalize`: `True`

#### `YonkersIR2,SysTopPatch9`
- `Digest`: `0305ea5727d84fe41c073105ed389517b947e733adcf2aa4fd7d5e1d3082baa7`
- `EPRO`: `True`
- `FabRevision`: `49474`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Glenbrook/YonkersIR2,SysTopPatch9`
- Info `Personalize`: `True`

#### `YonkersIR2,SysTopPatchA`
- `Digest`: `7f2c2fa99478bc52f047cffed36dc3fea3e617113a4788b55b18be2470f97c9c`
- `EPRO`: `False`
- `FabRevision`: `49730`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Glenbrook/YonkersIR2,SysTopPatchA`
- Info `Personalize`: `True`

#### `YonkersIR2,SysTopPatchB`
- `Digest`: `0305ea5727d84fe41c073105ed389517b947e733adcf2aa4fd7d5e1d3082baa7`
- `EPRO`: `True`
- `FabRevision`: `49730`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Glenbrook/YonkersIR2,SysTopPatchB`
- Info `Personalize`: `True`

#### `YonkersIR2,SysTopPatchC`
- `Digest`: `7f2c2fa99478bc52f047cffed36dc3fea3e617113a4788b55b18be2470f97c9c`
- `EPRO`: `False`
- `FabRevision`: `49986`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Glenbrook/YonkersIR2,SysTopPatchC`
- Info `Personalize`: `True`

#### `YonkersIR2,SysTopPatchD`
- `Digest`: `0305ea5727d84fe41c073105ed389517b947e733adcf2aa4fd7d5e1d3082baa7`
- `EPRO`: `True`
- `FabRevision`: `49986`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Glenbrook/YonkersIR2,SysTopPatchD`
- Info `Personalize`: `True`

#### `YonkersIR2,SysTopPatchE`
- `Digest`: `7f2c2fa99478bc52f047cffed36dc3fea3e617113a4788b55b18be2470f97c9c`
- `EPRO`: `False`
- `FabRevision`: `52428`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Glenbrook/YonkersIR2,SysTopPatchE`
- Info `Personalize`: `True`

#### `YonkersIR2,SysTopPatchF`
- `Digest`: `0305ea5727d84fe41c073105ed389517b947e733adcf2aa4fd7d5e1d3082baa7`
- `EPRO`: `True`
- `FabRevision`: `52428`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/Glenbrook/YonkersIR2,SysTopPatchF`
- Info `Personalize`: `True`

#### `eUICC,Gold`
- `Digest`: `a9632326a052c090677482c51c4d07259478c6d941ee1d2ee46ccf0f6f9249aa`
- Info `Path`: `Firmware/vinyl_20.vnlfw`

#### `eUICC,Main`
- `Digest`: `ac690767d53680418ce22855a94fd9f1be619995fc03d66d06fae31b263ae296`
- Info `Path`: `Firmware/vinyl_20.vnlfw`

#### `ftap`
- Info `HashMethod`: `sha2-256`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Personalize`: `False`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `ftsp`
- Info `HashMethod`: `sha2-256`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Personalize`: `False`
- Info `RestoreRequestRules`: `[{'Actions': {'ESEC': False}, 'Conditions': {'ApRawSecurityMode': False}}, {'Actions': {'ESEC': True}, 'Conditions': {'ApRawSecurityMode': True}}, {'Actions': {'ESEC': False}, 'Conditions': {'ApDemotionPolicyOverride': '', 'ApRawProductionMode': False, 'ApRawSecurityMode': True}}, {'Actions': {'ESEC`
- `Trusted`: `True`

#### `iBEC`
- `BuildString`: `iBoot-15391~1757`
- `Digest`: `41fa3c2a7d464186a00f90caec97640c78ffb77af1ffb1db84a00a3b944ed29a3927347c95c939135445fc54baaefc78`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/dfu/iBEC.v68.RELEASE.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `iBSS`
- `BuildString`: `iBoot-15391~1757`
- `Digest`: `198d68bff79405608411f36aa2e2c7036a92f001f474d842c18c52c54634ea77148483530c980bcb7828e3d17f814d90`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/dfu/iBSS.v68.RELEASE.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'DPRO': True}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductionMode': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRe`
- `MemoryMap`: `6480728002000000040000006880728002000000040000000801051102000000080000003002e4110200000008000000f849e4110200000008000000000005110200000008000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000`
- `RawDataDigest`: `2e62b37b6485cc3814fd1cfda528062cac98afd2cb365a23fc5b5a76231ae832f73c74e64b5f17f17195d50d6591a698`
- `Trusted`: `True`

#### `iBoot`
- `Digest`: `28df03c4dfab963ccafdf5a1450157e00e3079f9cf36d5eb4661ec63b91b362fb9ad5543befb828a0ea7f321de8de2c1`
- Info `IsFTAB`: `False`
- Info `IsFirmwarePayload`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/all_flash/iBoot.v68.RELEASE.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `iBootData`
- `Digest`: `09ec9d198c7d9be2a45808f9c668801590df1a4a051bbe7cd79372ba84165cbd321ea81936b8908d7d64ccc52ea56cc9`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/all_flash/iBootData.v68.RELEASE.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `rfta`
- Info `HashMethod`: `sha2-256`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Personalize`: `False`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `rfts`
- Info `HashMethod`: `sha2-256`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Personalize`: `False`
- Info `RestoreRequestRules`: `[{'Actions': {'ESEC': False}, 'Conditions': {'ApRawSecurityMode': False}}, {'Actions': {'ESEC': True}, 'Conditions': {'ApRawSecurityMode': True}}, {'Actions': {'ESEC': False}, 'Conditions': {'ApDemotionPolicyOverride': '', 'ApRawProductionMode': False, 'ApRawSecurityMode': True}}, {'Actions': {'ESEC`
- `Trusted`: `True`

## Recovery Customer Install

- `ApChipID`: `0x8160`
- `ApBoardID`: `0x0E`
- `ApSecurityDomain`: `0x01`
- `Ap,ProductType`: `iPhone19,4`
- `Ap,Target`: `V68AP`
- `Ap,TargetType`: `v68`
- `Ap,ProductMarketingVersion`: `27.2`
- `Ap,OSLongVersion`: `24.2.102.9.0,0`
- Info `Ap,Timestamp`: `0`
- Info `BuildNumber`: `24B91020`
- Info `BuildTrain`: `RavePopB`
- Info `ContentEncoding`: `aea`
- Info `DeviceClass`: `v68ap`
- Info `FDRSupport`: `True`
- Info `ImageName`: `V68RestoreIPSW`
- Info `MinimumSystemPartition`: `511`
- Info `MobileDeviceMinVersion`: `1853`
- Info `OSDiskImageSize`: `248`
- Info `OSVarContentSize`: `8192`
- Info `RequiresNonceSlot`: `True`
- Info `RequiresUIDMode`: `True`
- Info `RestoreAttestationMode`: `8`
- Info `RestoreBehavior`: `Erase`
- Info `Variant`: `Recovery Customer Install`

79 components.

| Component | Path | Digest (SHA-384, first 16 hex) | Flags |
|---|---|---|---|
| `AOP` | `Firmware/AOP/aopfw-v68aop.RELEASE.im4p` | `a8be918779ae2c1d` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `AOP2` | `Firmware/AOP2/aop2fw-v68aop2.RELEASE.im4p` | `abfbc6dc12c26f5c` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `Ap,ApplePMCFirmware` | `Firmware/pmc/t8160pmcfw.im4p` | `887e53baaf9f25ad` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `Ap,GFX1Firmware` | `Firmware/agx/armfw1_g19p.im4p` | `33febef5d5a22898` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `Ap,MSRFirmware` | `Firmware/msr/t8160.msrf.im4p` | `6c2611f3e8b5eaed` | Trusted, IsFUDFirmware, RestoreRequestRules |
| `Ap,RestoreSecureM3Firmware` | `Firmware/M3/bin/securem3fw-v68.im4p` | `f4a3ee30ac0b966c` | Trusted, IsLoadedByiBoot, RestoreRequestRules |
| `Ap,RestoreSecurePageTableMonitor` | `Firmware/sptm.t8160.release.im4p` | `c9e66676240d53ab` | Trusted, IsLoadedByiBoot, RestoreRequestRules |
| `Ap,RestoreTrustedExecutionMonitor` | `Firmware/txm.iphoneos.release.im4p` | `75371b6d03b94162` | Trusted, IsLoadedByiBoot, RestoreRequestRules |
| `Ap,RestorecL4` | `Firmware/image4/exclavecore_bundle.v68.RELEASE.restore.im4p` | `f7846005a0bfd5a0` | Trusted, IsLoadedByiBoot, RestoreRequestRules |
| `Ap,SecureM3Firmware` | `Firmware/M3/bin/securem3fw-v68.im4p` | `9b9075693ce1ecd8` | Trusted, IsFUDFirmware, RestoreRequestRules |
| `Ap,SecurePageTableMonitor` | `Firmware/sptm.t8160.release.im4p` | `2f69cb8b9dc4932f` | Trusted, IsFUDFirmware, RestoreRequestRules |
| `Ap,SystemVolumeCanonicalMetadata` | `Firmware/141-28683-104.dmg.aea.mtree` | `261943c3c31fc377` | Trusted, IsFUDFirmware, RestoreRequestRules |
| `Ap,TrustedExecutionMonitor` | `Firmware/txm.iphoneos.release.im4p` | `e9f0a0a9f060553d` | Trusted, IsFUDFirmware, RestoreRequestRules |
| `AppleLogo` | `Firmware/all_flash/applelogo@2d~iphone.im4p` | `72e55666b43d92ae` | Trusted, IsiBootEANFirmware, RestoreRequestRules |
| `Cellular1,CdpAscDl` | `Firmware/c4020iphone/Release/patched/ftab.bin` | `9bb48fff8021c91f` | Trusted, RestoreRequestRules |
| `Cellular1,CdpAscUl` | `Firmware/c4020iphone/Release/patched/ftab.bin` | `c0e59a3e3ffbd3b5` | Trusted, RestoreRequestRules |
| `Cellular1,CdpHost` | `Firmware/c4020iphone/Release/patched/ftab.bin` | `8d30be1ec9e53237` | Trusted, RestoreRequestRules |
| `Cellular1,L1CL1S` | `Firmware/c4020iphone/Release/patched/ftab.bin` | `46e0cdcb8acbca7a` | Trusted, RestoreRequestRules |
| `Cellular1,LLB` | `Firmware/c4020iphone/Release/patched/ftab.bin` | `162f084d64d6ba1e` | Trusted, RestoreRequestRules |
| `Cellular1,PMUFW` | `Firmware/c4020iphone/Release/patched/ftab.bin` | `33e1a57e7ba21e87` | Trusted, RestoreRequestRules |
| `Cellular1,PMUFW2` | `Firmware/c4020iphone/Release/patched/ftab.bin` | `024bbc34f73996a3` | Trusted, RestoreRequestRules |
| `Cellular1,RTKitOS` | `Firmware/c4020iphone/Release/patched/ftab.bin` | `9ccde882d2e36794` | Trusted, RestoreRequestRules |
| `Cellular1,Recipe` | `Firmware/c4020iphone/Release/patched/ftab.bin` | `e7cb1b15c3717f42` | Trusted, RestoreRequestRules |
| `Cellular1,iBootData` | `Firmware/c4020iphone/Release/patched/ftab.bin` | `45b76cdcd9e32532` | Trusted, RestoreRequestRules |
| `DeviceTree` | `Firmware/all_flash/DeviceTree.v68ap.im4p` | `a3b521b47aa0f054` | Trusted, IsFirmwarePayload, RestoreRequestRules |
| `GFX` | `Firmware/agx/armfw_g19p.im4p` | `40c7cc60cbda6878` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `ISP` | `Firmware/isp_bni/adc-boreas-v68.im4p` | `33b6bdc438ecbe1b` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `KernelCache` | `kernelcache.release.v6x-pandia` | `9f57d7cf359fc767` | Trusted, RestoreRequestRules |
| `OS` | `141-28683-104.dmg.aea` | `9cd2191ab1591154` | Trusted, RestoreRequestRules |
| `PMP` | `Firmware/pmp/t8160pmp.im4p` | `19008a2bc4a04e1b` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `RestoreANS` | `Firmware/rans.t8160.release.im4p` | `c60c3b84b45ea4f0` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `RestoreDCP` | `Firmware/dcp/t8160dcp_restore.im4p` | `39063050c7616fc6` | Trusted, IsLoadedByiBoot, RestoreRequestRules |
| `RestoreKernelCache` | `kernelcache.release.v6x-pandia` | `14a743b0cc147a94` | Trusted, RestoreRequestRules |
| `RestoreRamDisk` | `141-28940-105.dmg` | `2d09674fd3181693` | Trusted, RestoreRequestRules |
| `RestoreTrustCache` | `Firmware/141-28940-105.dmg.trustcache` | `c0b105973b887ac4` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `SIO` | `Firmware/SmartIOFirmware_ASCv8.im4p` | `8873ba2b293fc114` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |
| `StaticTrustCache` | `Firmware/141-28683-104.dmg.aea.trustcache` | `a14bc5c7d88c0428` | Trusted, IsFUDFirmware, RestoreRequestRules |
| `SystemVolume` | `Firmware/141-28683-104.dmg.aea.root_hash` | `fcafa6180157db89` | Trusted, IsFUDFirmware, RestoreRequestRules |
| `Wireless1,ACIBT` | `Firmware/t2026phoneG2/Release/ftab.bin` | `51c01d433c414fa2` | Trusted, RestoreRequestRules |
| `Wireless1,ACIBTLPEM` | `Firmware/t2026phoneG2/Release/ftab.bin` | `1f9a194a2e7aaa38` | Trusted, RestoreRequestRules |
| `Wireless1,ACIBTManuf` | `Firmware/t2026phoneG2/Release/ftab.bin` | `51c01d433c414fa2` | Trusted, RestoreRequestRules |
| `Wireless1,ACIWIFI` | `Firmware/t2026phoneG2/Release/ftab.bin` | `902b5adeacd5144f` | Trusted, RestoreRequestRules |
| `Wireless1,ACIWiFiTxManuf` | `Firmware/t2026phoneG2/Release/ftab.bin` | `36423b324369661e` | Trusted, RestoreRequestRules |
| `Wireless1,BTSecondary` | `Firmware/t2026phoneG2/Release/ftab.bin` | `ebd59be4d27b01a4` | Trusted, RestoreRequestRules |
| `Wireless1,BTSecondaryManuf` | `Firmware/t2026phoneG2/Release/ftab.bin` | `ebd59be4d27b01a4` | Trusted, RestoreRequestRules |
| `Wireless1,CCPUApplicationFirmware` | `Firmware/t2026phoneG2/Release/ftab.bin` | `45f576ce687be46e` | Trusted, RestoreRequestRules |
| `Wireless1,CoexRealTimeArbiter` | `Firmware/t2026phoneG2/Release/ftab.bin` | `44749c87da9b89c1` | Trusted, RestoreRequestRules |
| `Wireless1,PhyBlueTooth` | `Firmware/t2026phoneG2/Release/ftab.bin` | `181d64d765b57b4e` | Trusted, RestoreRequestRules |
| `Wireless1,PhyBlueTooth5G` | `Firmware/t2026phoneG2/Release/ftab.bin` | `8c0742a5e9ad20e1` | Trusted, RestoreRequestRules |
| `Wireless1,PhyBlueTooth5GManuf` | `Firmware/t2026phoneG2/Release/ftab.bin` | `8c0742a5e9ad20e1` | Trusted, RestoreRequestRules |
| `Wireless1,PhyBlueToothLPM` | `Firmware/t2026phoneG2/Release/ftab.bin` | `b0b972453c81fc03` | Trusted, RestoreRequestRules |
| `Wireless1,PhyBlueToothManuf` | `Firmware/t2026phoneG2/Release/ftab.bin` | `181d64d765b57b4e` | Trusted, RestoreRequestRules |
| `Wireless1,PhyBluetooth5GTrim` | `Firmware/t2026phoneG2/Release/ftab.bin` | `94c974402ac11c71` | Trusted, RestoreRequestRules |
| `Wireless1,PhyBluetoothTrim` | `Firmware/t2026phoneG2/Release/ftab.bin` | `3820e32dc8f92bf0` | Trusted, RestoreRequestRules |
| `Wireless1,RTKitOS` | `Firmware/t2026phoneG2/Release/ftab.bin` | `8219626cc42aae17` | Trusted, RestoreRequestRules |
| `Wireless1,RTKitOSLPEM` | `Firmware/t2026phoneG2/Release/ftab.bin` | `be6863c3d47047bd` | Trusted, RestoreRequestRules |
| `Wireless1,ScanBTLPEM` | `Firmware/t2026phoneG2/Release/ftab.bin` | `3c449b8c373522b5` | Trusted, RestoreRequestRules |
| `Wireless1,ScanBTManuf` | `Firmware/t2026phoneG2/Release/ftab.bin` | `f890cbeafa0ccbeb` | Trusted, RestoreRequestRules |
| `Wireless1,ScanBluetooth` | `Firmware/t2026phoneG2/Release/ftab.bin` | `f890cbeafa0ccbeb` | Trusted, RestoreRequestRules |
| `Wireless1,ScanWifi` | `Firmware/t2026phoneG2/Release/ftab.bin` | `14f68624a65887fa` | Trusted, RestoreRequestRules |
| `Wireless1,ScanWifiManuf` | `Firmware/t2026phoneG2/Release/ftab.bin` | `611a45ae78230635` | Trusted, RestoreRequestRules |
| `Wireless1,WiFiRx` | `Firmware/t2026phoneG2/Release/ftab.bin` | `00751f9522d1e2e3` | Trusted, RestoreRequestRules |
| `Wireless1,WiFiRxManuf` | `Firmware/t2026phoneG2/Release/ftab.bin` | `43b50d30fed4c6be` | Trusted, RestoreRequestRules |
| `Wireless1,WiFiTx` | `Firmware/t2026phoneG2/Release/ftab.bin` | `b28a762c0e1d7d94` | Trusted, RestoreRequestRules |
| `Wireless1,WiFiTxManuf` | `Firmware/t2026phoneG2/Release/ftab.bin` | `da7ad47bb37867fc` | Trusted, RestoreRequestRules |
| `Wireless1,Wifi2GLMAC` | `Firmware/t2026phoneG2/Release/ftab.bin` | `2d0a90a6fcd00801` | Trusted, RestoreRequestRules |
| `Wireless1,Wifi2GLMACManuf` | `Firmware/t2026phoneG2/Release/ftab.bin` | `3e72c8dbb12e0c77` | Trusted, RestoreRequestRules |
| `Wireless1,Wifi2GLPhy` | `Firmware/t2026phoneG2/Release/ftab.bin` | `847eca454fc4f9f4` | Trusted, RestoreRequestRules |
| `Wireless1,Wifi2GLPhyManuf` | `Firmware/t2026phoneG2/Release/ftab.bin` | `847eca454fc4f9f4` | Trusted, RestoreRequestRules |
| `Wireless1,Wifi2GLPhyTrim` | `Firmware/t2026phoneG2/Release/ftab.bin` | `afc1e501998b0b55` | Trusted, RestoreRequestRules |
| `Wireless1,Wifi5GLMAC` | `Firmware/t2026phoneG2/Release/ftab.bin` | `bedce67d68535076` | Trusted, RestoreRequestRules |
| `Wireless1,Wifi5GLMACManuf` | `Firmware/t2026phoneG2/Release/ftab.bin` | `2372fd4b17cc6eef` | Trusted, RestoreRequestRules |
| `Wireless1,Wifi5GLPhy` | `Firmware/t2026phoneG2/Release/ftab.bin` | `d528706af0b66fe1` | Trusted, RestoreRequestRules |
| `Wireless1,Wifi5GLPhyManuf` | `Firmware/t2026phoneG2/Release/ftab.bin` | `d528706af0b66fe1` | Trusted, RestoreRequestRules |
| `Wireless1,Wifi5GLPhyTrim` | `Firmware/t2026phoneG2/Release/ftab.bin` | `c8dac484934f456d` | Trusted, RestoreRequestRules |
| `Wireless1,WifiRegData` | `Firmware/t2026phoneG2/Release/ftab.bin` | `03adb4c5ce95a3da` | Trusted, RestoreRequestRules |
| `iBEC` | `Firmware/dfu/iBEC.v68.RELEASE.im4p` | `41fa3c2a7d464186` | Trusted, RestoreRequestRules |
| `iBSS` | `Firmware/dfu/iBSS.v68.RELEASE.im4p` | `198d68bff7940560` | Trusted, RestoreRequestRules |
| `iBootData` | `Firmware/all_flash/iBootData.v68.RELEASE.im4p` | `09ec9d198c7d9be2` | Trusted, IsLoadedByiBoot, IsFUDFirmware, RestoreRequestRules |

### Component details

#### `AOP`
- `Digest`: `a8be918779ae2c1ddb8fbbb6d1d4db0535ab13121086d13e203a7defb7c1e5a16caafdd27a592beead05ac9c116fae74`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/AOP/aopfw-v68aop.RELEASE.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `AOP2`
- `Digest`: `abfbc6dc12c26f5c1587439022847317fa3895b8101e27bfd65913817d5360c8537aae8f5709db99b76dd6f7d25fe7df`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/AOP2/aop2fw-v68aop2.RELEASE.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,ApplePMCFirmware`
- `Digest`: `887e53baaf9f25ad1ef1fd97b1287cd2f195a5ad72b40af70585d943da1e4ba075f02d5cabbbe824774639566caa04cb`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/pmc/t8160pmcfw.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,GFX1Firmware`
- `Digest`: `33febef5d5a228984d2603f89e1b9ef78dfaae91d0167ae0fdaeb147a20c9ff25b1a79fcbdd1620384b95f1a43bbe0ad`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/agx/armfw1_g19p.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,MSRFirmware`
- `Digest`: `6c2611f3e8b5eaed277fce91ace8673d74e8dab2f938b8c80b72e4cd1ebe091e4c953c06330499553d54ac4b3de4045c`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/msr/t8160.msrf.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,RestoreSecureM3Firmware`
- `Digest`: `f4a3ee30ac0b966c872be05e9cf85b784a8363473952bff011c4d131ffae982fce7eb3d6ffbc7206c1545baa76f6ad75`
- Info `Img4PayloadType`: `rsm3`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/M3/bin/securem3fw-v68.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `Ap,RestoreSecurePageTableMonitor`
- `Digest`: `c9e66676240d53abb09022bb1d63972ba82a49ae7edce2a118174fae514e58adf4ef8bdf5d1015047dc29c42eb974c1b`
- Info `Img4PayloadType`: `rspt`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/sptm.t8160.release.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `Ap,RestoreTrustedExecutionMonitor`
- `Digest`: `75371b6d03b94162e4e95077067ab36dc4eb92ddbc78574be819b79ebd2399e816ae4416c995e01d597376d729f5a0a1`
- Info `Img4PayloadType`: `rtrx`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/txm.iphoneos.release.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `Ap,RestorecL4`
- `Digest`: `f7846005a0bfd5a07116a05cb9084b8bcd58b56e593e95d5d6a94db71329dbcc9b64adc70b1174d100c7c75bed413baa`
- Info `Img4PayloadType`: `rxcl`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/image4/exclavecore_bundle.v68.RELEASE.restore.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `Ap,SecureM3Firmware`
- `Digest`: `9b9075693ce1ecd88a4952a1529681d9d13412933cb63079d4873bbd510813d422adf8d241617bf139651447372bfbcd`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/M3/bin/securem3fw-v68.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,SecurePageTableMonitor`
- `Digest`: `2f69cb8b9dc4932ffbb28f4bf7ce6712b46e8d3a90367255646779b94aa28895cd6220da5884f6d5dea8715e8b91f737`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/sptm.t8160.release.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Ap,SystemVolumeCanonicalMetadata`
- `Digest`: `261943c3c31fc3777e4c203d2ca99bebe4413eb1c6beace8286f82d24a80d7da6dab24134b3f89a2bbf5e8e9df615eab`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/141-28683-104.dmg.aea.mtree`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `Ap,TrustedExecutionMonitor`
- `Digest`: `e9f0a0a9f060553dcba6de84e0cd4b70c381bf3a174168282843fc12cd01509d6071e6286a13022652cfab95189c3c5b`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/txm.iphoneos.release.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `AppleLogo`
- `Digest`: `72e55666b43d92ae01875414c1a25d8809ccde5b720b7d42749d6d3bcda2031bd48561b7a83ebaa4da10299bc2e62634`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `True`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/all_flash/applelogo@2d~iphone.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Cellular1,CdpAscDl`
- `Digest`: `9bb48fff8021c91f3f9ce98a38c19ef89399272bcd487c6a6b4bcc777b1dda566e59fb74d2d8089462bb843b1babb0ce`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/c4020iphone/Release/patched/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Cellular1,CdpAscUl`
- `Digest`: `c0e59a3e3ffbd3b5c75428fb36432facabc745944296ff515f737c4fef4efc64586809f7a16f56354a1eaecf2aa8d774`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/c4020iphone/Release/patched/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Cellular1,CdpHost`
- `Digest`: `8d30be1ec9e53237500b942bdabdd2477b6f3337c86a57053e3b2ed5be37baf8cb40b0c8882f5d8a6bc3cc0c38735de9`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/c4020iphone/Release/patched/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Cellular1,L1CL1S`
- `Digest`: `46e0cdcb8acbca7a0ce1ea1672227796130091b7abe75f5fa14d430f370edd93d8b434a7e7df09012657b589b43a7081`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/c4020iphone/Release/patched/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Cellular1,LLB`
- `Digest`: `162f084d64d6ba1ea7d26fd9a94362aa914ac87f0b55b27f5ef35fc6a083666319dd15a3d8748ed32d85ea54787f2d05`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/c4020iphone/Release/patched/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Cellular1,PMUFW`
- `Digest`: `33e1a57e7ba21e87c045b6f85a1fbe1732285f7151962cf6c3cd3f83dbe45745cf2ed60ed5e266851b6d0b1dc733f541`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/c4020iphone/Release/patched/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Cellular1,PMUFW2`
- `Digest`: `024bbc34f73996a33ab5b2e39ce36b158fb336f8d7cd7b7027e2c0ace73bb004c53cb948b03df45f8ef31de51041fe88`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/c4020iphone/Release/patched/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Cellular1,RTKitOS`
- `Digest`: `9ccde882d2e3679418efc6f95b12e7d77d16081ecc9432dd510519cd5f6d773cfbdffee5fc6fe0505cbc6677b1e83e54`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/c4020iphone/Release/patched/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Cellular1,Recipe`
- `Digest`: `e7cb1b15c3717f42a127a35b5506d720f2d58971e781cbe731c87cc96aac422973337922eb80e5ed6695501c35d8168d`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/c4020iphone/Release/patched/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Cellular1,iBootData`
- `Digest`: `45b76cdcd9e32532b492018443e65eb3757a404c02555e76ccb4722eaa69130d76e1d7bba88042f3cf9767e48857df7b`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/c4020iphone/Release/patched/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `DeviceTree`
- `Digest`: `a3b521b47aa0f0540ac943eb5afab35b123789358cd16b74e394db195fdbc000bae4adb8b3e2c06b9555034e86269f76`
- Info `IsFTAB`: `False`
- Info `IsFirmwarePayload`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/all_flash/DeviceTree.v68ap.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `GFX`
- `Digest`: `40c7cc60cbda687879663afb4c02f0293531e4a372e5247a2d986276853a7ae2f5f5887e5e0dd0359bb194696c894cf1`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/agx/armfw_g19p.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `ISP`
- `Digest`: `33b6bdc438ecbe1bdfe93f88700d230813ffde3943f1df799a4d69a1ea36b6b2bea61ee51ce971cc578624668eeebc9f`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/isp_bni/adc-boreas-v68.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `KernelCache`
- `Digest`: `9f57d7cf359fc7671d295630bb82f9909ead4c9f41b80b34e8248f3519de737e29c5e1069e48d40d49772b389d176201`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `kernelcache.release.v6x-pandia`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `OS`
- `Digest`: `9cd2191ab15911546b6481e5d72659b11c8c3b63069150e9d47c5592ae99148d6a18e74de778d570b61c2ca7d36e8abb`
- Info `HashMethod`: `sha2-384`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `141-28683-104.dmg.aea`
- Info `Personalize`: `False`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `PMP`
- `Digest`: `19008a2bc4a04e1b7ea69fd82e585ea96246e5e3a6ad8718ae0ad9bec05521fbf7770b62c26f1263f1b5a59cf0c4af4b`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/pmp/t8160pmp.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `RestoreANS`
- `Digest`: `c60c3b84b45ea4f06c28cbd059377d2ba69f6afce9558d7e578483e45291ddc489b452ff3fcc8a0c98ed5b4306a7bd92`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/rans.t8160.release.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `RestoreDCP`
- `Digest`: `39063050c7616fc6ee7b1dc3b3a1d7ddf8d33f39ca3be62f1fe20638f51f07349463e777a9cdbb944d9afd3d83fbf5fe`
- Info `Img4PayloadType`: `rdcp`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/dcp/t8160dcp_restore.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `RestoreKernelCache`
- `Digest`: `14a743b0cc147a9480dea7708fc3e5310fa89174656296649188e59c40ca531f44b870ed2b795522fcd6bdc51298b06f`
- Info `Img4PayloadType`: `rkrn`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `kernelcache.release.v6x-pandia`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `RestoreRamDisk`
- `Digest`: `2d09674fd3181693644bc53f037b38fd0fd4e683c86d8f8c2cbd5bec2984cf6af5f9a3beedee505d87c50f72f19e79e0`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `141-28940-105.dmg`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `RestoreTrustCache`
- `Digest`: `c0b105973b887ac4806aa2c6eae8f62ad026525842c66d188ccc38e6d34b77d008953e7222db23ad2d3cd820b33081bd`
- Info `Img4PayloadType`: `rtsc`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/141-28940-105.dmg.trustcache`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `SIO`
- `Digest`: `8873ba2b293fc1144f3fbc9780492ffea17cbac9c3ab5b182ce19ec789d6b75a2b2e3c603dc135bfda6cd21ca3ee7344`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/SmartIOFirmware_ASCv8.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `StaticTrustCache`
- `Digest`: `a14bc5c7d88c0428739d33a718eb025ba0d75bbd91ce05c84be0d790fa2a5026de503669fc0c2c4673f33a7b213d0ebc`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/141-28683-104.dmg.aea.trustcache`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `SystemVolume`
- `Digest`: `fcafa6180157db897382654ac5389106d4361e5523a8d59502d9cdbaed82d36ff3a4a23e733b0c203b47bab651999b9d`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/141-28683-104.dmg.aea.root_hash`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `Wireless1,ACIBT`
- `Digest`: `51c01d433c414fa22f7769dad787f55f3fd2de1e308607402da015d423ef5bc0929a525f4d7038d20349509749573d50`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,ACIBTLPEM`
- `Digest`: `1f9a194a2e7aaa3825af77a23dd7f71d6e6b05a94f2aa181d653a885c6c09b3291a3adcc4d6a30ce9a455324dc88f97c`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,ACIBTManuf`
- `Digest`: `51c01d433c414fa22f7769dad787f55f3fd2de1e308607402da015d423ef5bc0929a525f4d7038d20349509749573d50`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,ACIWIFI`
- `Digest`: `902b5adeacd5144fb149f7b3d87c64b0ef7276c13cb92cf7e8e73d4f22ba743dd73f0b920f539e0bfb95ab3f4e3bcbb1`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,ACIWiFiTxManuf`
- `Digest`: `36423b324369661e34da69383f486a7f30838e99a7f7756d74254ecbdf951ca7397ce33d96e05b4dc0d2f590def4c66a`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,BTSecondary`
- `Digest`: `ebd59be4d27b01a4e1a696feb77a6aa10a75087f609efaff2e0f0ce3215113e74b0de656ee29eb9835d6a751b11ae931`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,BTSecondaryManuf`
- `Digest`: `ebd59be4d27b01a4e1a696feb77a6aa10a75087f609efaff2e0f0ce3215113e74b0de656ee29eb9835d6a751b11ae931`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,CCPUApplicationFirmware`
- `Digest`: `45f576ce687be46effa69e4d48584543abe24bb1684e137fe2ac3a307828c0e9024302bf437530d5f1c3c4dc99ab2eea`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,CoexRealTimeArbiter`
- `Digest`: `44749c87da9b89c1e09056d09de81bf1bcc7125480a78db8424e9583d5be8df4f861c9d31813a8c1806398d0c18941ec`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,PhyBlueTooth`
- `Digest`: `181d64d765b57b4e3167ce24151b847f99c713b84bd75abe67708f2abbc66be9a0b1c2ac6b97733ff0132732efa9040e`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,PhyBlueTooth5G`
- `Digest`: `8c0742a5e9ad20e1254c7355de8386dcb335305c0977edbdb3778c149f063353713f8004479930c0b81f44f49b1f3e02`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,PhyBlueTooth5GManuf`
- `Digest`: `8c0742a5e9ad20e1254c7355de8386dcb335305c0977edbdb3778c149f063353713f8004479930c0b81f44f49b1f3e02`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,PhyBlueToothLPM`
- `Digest`: `b0b972453c81fc0327ead8a21c73630cb4d516ee0f7d542181bef7493f68f956da73d4174dd40b41faa2138cda04739d`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,PhyBlueToothManuf`
- `Digest`: `181d64d765b57b4e3167ce24151b847f99c713b84bd75abe67708f2abbc66be9a0b1c2ac6b97733ff0132732efa9040e`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,PhyBluetooth5GTrim`
- `Digest`: `94c974402ac11c7180cb8b14686c18ec353565b2590ce8a709a5cd5d6c26e6b94f24950c03d623e037cecc3d9e582b50`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,PhyBluetoothTrim`
- `Digest`: `3820e32dc8f92bf00be0cc9eeda45317d7f37d600236bd0e1f54a993f1e5d87d6094b4536f56a3ac75179c33fb9505cc`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,RTKitOS`
- `Digest`: `8219626cc42aae1765e87b3c3f8034530f66a23bc1fd3bfdeb69b578c14e78590daec9c28d75c5b9f917f1aacdd68cf6`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,RTKitOSLPEM`
- `Digest`: `be6863c3d47047bde6b35529fa3f3d9eb88b4678531ef6cf7966ffb85b6fc8408b12a745b7ad07f30f8898ccd073cb4a`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,ScanBTLPEM`
- `Digest`: `3c449b8c373522b5025c3161008797cd14cb0907d29e7ccf521ac55a2085553801aebd1545557fba6700a8c7149407ae`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,ScanBTManuf`
- `Digest`: `f890cbeafa0ccbeb427962f17b48f603feff8561172a98d231ed8205e81e30146f04df9e096776d80dafd3d347a53cbd`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,ScanBluetooth`
- `Digest`: `f890cbeafa0ccbeb427962f17b48f603feff8561172a98d231ed8205e81e30146f04df9e096776d80dafd3d347a53cbd`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,ScanWifi`
- `Digest`: `14f68624a65887fa965c6ddf6d01b2b1027db493a891ddcef52454f1a8939ddcfcb7d1d668e857d9353a344de6275289`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,ScanWifiManuf`
- `Digest`: `611a45ae78230635ae909126967e6783cd39e6bda0c3e28d5e87360bc1144756308a86c1b18574652053b727c0b482c1`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,WiFiRx`
- `Digest`: `00751f9522d1e2e3a2b5684278fb36ff6925949b46e878efd797cfde49c32cdb7286856a7ead45383646538e1a487294`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,WiFiRxManuf`
- `Digest`: `43b50d30fed4c6befc3704b461841679cd339fdd85fa06d8a28fe08b83f13ade2a7a8de0c0d1957f8febcff31a0ee3c6`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,WiFiTx`
- `Digest`: `b28a762c0e1d7d947f2f728c3ea45afe5940eb0785f2f10689c17fc23c5fa40cbbec821fab3673637ae1da9f340253b4`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,WiFiTxManuf`
- `Digest`: `da7ad47bb37867fc46f85ebff1f2d02204382ad199efaed984d7f433165cf0377c83afce9477707cd7bb04a584bb238e`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,Wifi2GLMAC`
- `Digest`: `2d0a90a6fcd00801a8381b3111cc4b15ed9e9093de81c6b9dec26025466376bea66f53ebd7112161dfce217b69f01315`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,Wifi2GLMACManuf`
- `Digest`: `3e72c8dbb12e0c77dca7685815aa628373702b63d5b2155e44fd1152f0f560706d38bd019f3ad3b70ffe51a27d3e1566`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,Wifi2GLPhy`
- `Digest`: `847eca454fc4f9f4970ecec9b1fe41dc2649a1ebbfac48747a432a484089f94f300cd1381bce6e186a2802a144d0c28b`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,Wifi2GLPhyManuf`
- `Digest`: `847eca454fc4f9f4970ecec9b1fe41dc2649a1ebbfac48747a432a484089f94f300cd1381bce6e186a2802a144d0c28b`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,Wifi2GLPhyTrim`
- `Digest`: `afc1e501998b0b550ca0f2ea81ac94a37fde226bff043a61eb0f1178575f68da86197e0e667374855cc77a70cd5f78d7`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,Wifi5GLMAC`
- `Digest`: `bedce67d68535076b21cb535a67e61eec4bcfc95637a395f465a2cbafde3b987dea3cc3c9c41ccb56c2020daefd6de66`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,Wifi5GLMACManuf`
- `Digest`: `2372fd4b17cc6eef67f8281125fca7f57a75a36ab005a568763a40defc9cdaa88deb0290a3a7158a5d9e0068e134189f`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,Wifi5GLPhy`
- `Digest`: `d528706af0b66fe115912d7bba9185a176d41b4eddda8e09b107d78d652eecb98a4b38cc0c671d4a068d0ff142ea1d4c`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,Wifi5GLPhyManuf`
- `Digest`: `d528706af0b66fe115912d7bba9185a176d41b4eddda8e09b107d78d652eecb98a4b38cc0c671d4a068d0ff142ea1d4c`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,Wifi5GLPhyTrim`
- `Digest`: `c8dac484934f456d998a8d7438c0d577ea2e660e81330fff47a7497558de462c3a594557c00e652eb30a4e90ba64fa3b`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `Wireless1,WifiRegData`
- `Digest`: `03adb4c5ce95a3dab17572b4c73dfcdbdacef0ab31f6f98372f7356ac38eb839e65f69469fa78b685499cfadf90414f2`
- Info `IsFTAB`: `True`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/t2026phoneG2/Release/ftab.bin`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

#### `iBEC`
- `BuildString`: `iBoot-15391~1757`
- `Digest`: `41fa3c2a7d464186a00f90caec97640c78ffb77af1ffb1db84a00a3b944ed29a3927347c95c939135445fc54baaefc78`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/dfu/iBEC.v68.RELEASE.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': True, 'ApDemotionP`
- `Trusted`: `True`

#### `iBSS`
- `BuildString`: `iBoot-15391~1757`
- `Digest`: `198d68bff79405608411f36aa2e2c7036a92f001f474d842c18c52c54634ea77148483530c980bcb7828e3d17f814d90`
- Info `IsFTAB`: `False`
- Info `IsLoadedByiBoot`: `False`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/dfu/iBSS.v68.RELEASE.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'DPRO': True}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductionMode': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApCurrentProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApCurrentProductionMode': True, 'ApRe`
- `MemoryMap`: `6480728002000000040000006880728002000000040000000801051102000000080000003002e4110200000008000000f849e4110200000008000000000005110200000008000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000006000970200000004000000`
- `RawDataDigest`: `2e62b37b6485cc3814fd1cfda528062cac98afd2cb365a23fc5b5a76231ae832f73c74e64b5f17f17195d50d6591a698`
- `Trusted`: `True`

#### `iBootData`
- `Digest`: `09ec9d198c7d9be2a45808f9c668801590df1a4a051bbe7cd79372ba84165cbd321ea81936b8908d7d64ccc52ea56cc9`
- Info `IsFTAB`: `False`
- Info `IsFUDFirmware`: `True`
- Info `IsLoadedByiBoot`: `True`
- Info `IsLoadedByiBootStage1`: `False`
- Info `IsiBootEANFirmware`: `False`
- Info `IsiBootNonEssentialFirmware`: `False`
- Info `Path`: `Firmware/all_flash/iBootData.v68.RELEASE.im4p`
- Info `Personalize`: `True`
- Info `RestoreRequestRules`: `[{'Actions': {'EPRO': False}, 'Conditions': {'ApRawProductionMode': False, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': True}, 'Conditions': {'ApRawProductionMode': True, 'ApRequiresImage4': True}}, {'Actions': {'EPRO': False}, 'Conditions': {'ApDemotionPolicyOverride': 'Demote', 'ApRawProductio`
- `Trusted`: `True`

