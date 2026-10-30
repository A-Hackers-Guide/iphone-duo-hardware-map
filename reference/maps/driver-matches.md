# Driver match table

978 `IONameMatch` entries (942 distinct strings) in top-level kext personalities. 159 entries (146 distinct strings) match a node on the Duo; 819 match nothing on this board — drivers shipped in the shared kernelcache for hardware the Duo does not have (or that is matched another way). **[KC][DT]**

## Matched on the Duo

| Match string | IOClass | kext | Nodes |
|---|---|---|---|
| `AppleARM` | `AppleARMPE` | [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md) | [`/`](../devicetree/root.md) |
| `SPUApp` | `AppleSPUAppDriver` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) | [`/arm-io/aop/iop-aop-nub/SPUApp`](../devicetree/root__arm-io__aop__iop-aop-nub__SPUApp.md) |
| `aapl,spmi` | `AppleSPMIController` | [`com.apple.driver.AppleSPMI`](../kexts/com.apple.driver.AppleSPMI.md) | [`/arm-io/aop-spmi0`](../devicetree/root__arm-io__aop-spmi0.md), [`/arm-io/aop-spmi1`](../devicetree/root__arm-io__aop-spmi1.md), [`/arm-io/nub-spmi0`](../devicetree/root__arm-io__nub-spmi0.md), [`/arm-io/nub-spmi1`](../devicetree/root__arm-io__nub-spmi1.md), [`/arm-io/nub-spmi2`](../devicetree/root__arm-io__nub-spmi2.md) |
| `admac,v5p0` | `AudioDMAController` | [`com.apple.driver.AudioDMAController-Gen5p0`](../kexts/com.apple.driver.AudioDMAController-Gen5p0.md) | [`/arm-io/admac-dispext0`](../devicetree/root__arm-io__admac-dispext0.md), [`/arm-io/admac-dispint0`](../devicetree/root__arm-io__admac-dispint0.md) |
| `admac-ec-proxy` | `DMAChannelProxy` | [`com.apple.driver.DMAChannelProxy`](../kexts/com.apple.driver.DMAChannelProxy.md) | [`/arm-io/admac-hp-mic-ec-proxy`](../devicetree/root__arm-io__admac-hp-mic-ec-proxy.md), [`/arm-io/admac-receiver-tx-ec-proxy`](../devicetree/root__arm-io__admac-receiver-tx-ec-proxy.md), [`/arm-io/admac-sllb-ec-proxy`](../devicetree/root__arm-io__admac-sllb-ec-proxy.md), [`/arm-io/admac-speaker-tx-ec-proxy`](../devicetree/root__arm-io__admac-speaker-tx-ec-proxy.md) |
| `admac-evolution,v5p0` | `AudioDMAController` | [`com.apple.driver.AudioDMAController-Gen5p0`](../kexts/com.apple.driver.AudioDMAController-Gen5p0.md) | [`/arm-io/admac-base-ns`](../devicetree/root__arm-io__admac-base-ns.md), [`/arm-io/admac-base-s`](../devicetree/root__arm-io__admac-base-s.md), [`/arm-io/admac-leap-ns`](../devicetree/root__arm-io__admac-leap-ns.md), [`/arm-io/admac-leap-s`](../devicetree/root__arm-io__admac-leap-s.md) |
| `admacled,v1p0` | `AudioDMACLLTEscalationDetector` | [`com.apple.driver.AudioDMACLLTEscalationDetector-Gen1p0`](../kexts/com.apple.driver.AudioDMACLLTEscalationDetector-Gen1p0.md) | [`/arm-io/admac-aop-ced-ssw`](../devicetree/root__arm-io__admac-aop-ced-ssw.md), [`/arm-io/admac-dispext0-ced-ssw`](../devicetree/root__arm-io__admac-dispext0-ced-ssw.md), [`/arm-io/admac-dispint0-ced-ssw`](../devicetree/root__arm-io__admac-dispint0-ced-ssw.md) |
| `aes,s8000` | `AppleS8000AESAccelerator` | [`com.apple.driver.AppleS8000AES`](../kexts/com.apple.driver.AppleS8000AES.md) | [`/arm-io/aes`](../devicetree/root__arm-io__aes.md) |
| `aic,3` | `AppleInterruptControllerV3` | [`com.apple.driver.AppleInterruptControllerV3`](../kexts/com.apple.driver.AppleInterruptControllerV3.md) | [`/arm-io/aic`](../devicetree/root__arm-io__aic.md) |
| `ane,ane-exclave-proxy` | `ANEExclaveProxy` | [`com.apple.driver.AppleH16ANEInterface`](../kexts/com.apple.driver.AppleH16ANEInterface.md) | [`/arm-io/ane-exclave-proxy`](../devicetree/root__arm-io__ane-exclave-proxy.md) |
| `ane,ane1-exclave-proxy` | `ANEExclaveProxy` | [`com.apple.driver.AppleH16ANEInterface`](../kexts/com.apple.driver.AppleH16ANEInterface.md) | [`/arm-io/ane1-exclave-proxy`](../devicetree/root__arm-io__ane1-exclave-proxy.md) |
| `aon-ptd` | `AppleSPUAONPTDDriver` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) | [`/arm-io/aon-ptd`](../devicetree/root__arm-io__aon-ptd.md) |
| `aop,h16,vd5b704` | `AppleCameraPhotonDetector` | [`com.apple.driver.AppleCameraPhotonDetector`](../kexts/com.apple.driver.AppleCameraPhotonDetector.md) | [`/arm-io/grimaldi`](../devicetree/root__arm-io__grimaldi.md) |
| `aop-audio` | `AOPAudioService` | [`com.apple.driver.AOPAudio2`](../kexts/com.apple.driver.AOPAudio2.md) | [`/arm-io/aop/iop-aop-nub/aop-audio`](../devicetree/root__arm-io__aop__iop-aop-nub__aop-audio.md) |
| `aop-audio` | `AppleAOPAudioController` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) | [`/arm-io/aop/iop-aop-nub/aop-audio`](../devicetree/root__arm-io__aop__iop-aop-nub__aop-audio.md) |
| `aop-voicetrigger` | `AOPAudioService` | [`com.apple.driver.AOPAudio2`](../kexts/com.apple.driver.AOPAudio2.md) | [`/arm-io/aop/iop-aop-nub/aop-voicetrigger`](../devicetree/root__arm-io__aop__iop-aop-nub__aop-voicetrigger.md) |
| `apcie,t8160` | `AppleT8160PCIe` | [`com.apple.driver.AppleT8160PCIe`](../kexts/com.apple.driver.AppleT8160PCIe.md) | [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) |
| `apcie-bridge` | `APCIECoreRCGen5p1HostBridge` | [`com.apple.driver.AppleT8160PCIe`](../kexts/com.apple.driver.AppleT8160PCIe.md) | [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md), [`/arm-io/apcie/pci-bridge1`](../devicetree/root__arm-io__apcie__pci-bridge1.md) |
| `apple-processor-trace,t8160` | `AppleProcessorTraceT8160` | [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md) | [`/arm-io/apple-processor-trace`](../devicetree/root__arm-io__apple-processor-trace.md) |
| `arm-io,t8160` | `AppleSoCIOPSD` | [`com.apple.driver.AppleT8160`](../kexts/com.apple.driver.AppleT8160.md) | [`/arm-io`](../devicetree/root__arm-io.md) |
| `atc-dpxbar,t602x` | `AppleT602XATCDPXBAR` | [`com.apple.driver.AppleDisplayCrossbar`](../kexts/com.apple.driver.AppleDisplayCrossbar.md) | [`/arm-io/atc0-dpxbar`](../devicetree/root__arm-io__atc0-dpxbar.md) |
| `atc-phy,t8160` | `AppleT8160TypeCPhy` | [`com.apple.driver.AppleT8160TypeCPhy`](../kexts/com.apple.driver.AppleT8160TypeCPhy.md) | [`/arm-io/atc-phy0`](../devicetree/root__arm-io__atc-phy0.md) |
| `audio,embedded-resource-manager` | `AppleEmbeddedAudioResourceManager` | [`com.apple.driver.AppleEmbeddedAudioResourceManager`](../kexts/com.apple.driver.AppleEmbeddedAudioResourceManager.md) | [`/arm-io/audio-resource-manager`](../devicetree/root__arm-io__audio-resource-manager.md) |
| `audio-control,audio-iop-haptic-debug` | `IOPHapticDebug` | [`com.apple.driver.IOPHaptics`](../kexts/com.apple.driver.IOPHaptics.md) | [`/arm-io/iop-audio-controller/audio-hpdbg`](../devicetree/root__arm-io__iop-audio-controller__audio-hpdbg.md) |
| `audio-control,audio-iop-haptics` | `IOPHaptics` | [`com.apple.driver.IOPHaptics`](../kexts/com.apple.driver.IOPHaptics.md) | [`/arm-io/iop-audio-controller/audio-haptic`](../devicetree/root__arm-io__iop-audio-controller__audio-haptic.md) |
| `audio-control,cs42l79` | `AppleCS42L79Audio` | [`com.apple.driver.AppleCS42L79Audio`](../kexts/com.apple.driver.AppleCS42L79Audio.md) | [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) |
| `audio-data,audio-loopback` | `AppleSecondaryAudio` | [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md) | [`/arm-io/iop-audio-controller/audio-mca-loopback/audio-mca-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-mca-loopback__audio-mca-loopback.md) |
| `audio-data,external` | `AppleExternalSecondaryAudio` | [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md) | [`/arm-io/iop-audio-controller/audio-flicker/audio-flicker`](../devicetree/root__arm-io__iop-audio-controller__audio-flicker__audio-flicker.md), [`/arm-io/iop-audio-controller/audio-leap-internal-loopback/audio-leap-internal-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-leap-internal-loopback__audio-leap-internal-loopback.md), [`/arm-io/iop-audio-controller/audio-receiver/audio-receiver`](../devicetree/root__arm-io__iop-audio-controller__audio-receiver__audio-receiver.md), [`/arm-io/iop-audio-controller/audio-s-leap-internal-loopback/audio-s-leap-internal-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-s-leap-internal-loopback__audio-s-leap-internal-loopback.md), [`/arm-io/iop-audio-controller/audio-speaker-tap/audio-speaker-tap`](../devicetree/root__arm-io__iop-audio-controller__audio-speaker-tap__audio-speaker-tap.md), [`/arm-io/iop-audio-controller/lp-mic-injection-device/lp-mic-injection-device`](../devicetree/root__arm-io__iop-audio-controller__lp-mic-injection-device__lp-mic-injection-device.md) |
| `audio-haptic-leap` | `AppleAOPAudioHapticLEAP` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) | [`/arm-io/iop-audio-controller/audio-haptic-leap`](../devicetree/root__arm-io__iop-audio-controller__audio-haptic-leap.md) |
| `audio-hp` | `AppleAOPAudioClientManager` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) | [`/arm-io/iop-audio-controller/audio-hp`](../devicetree/root__arm-io__iop-audio-controller__audio-hp.md) |
| `audio-hw-pcm-audiomgr` | `AppleAOPAudioPCMAssetManagerDevice` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) | [`/arm-io/iop-audio-controller/audio-hw-pcm-audiomgr`](../devicetree/root__arm-io__iop-audio-controller__audio-hw-pcm-audiomgr.md) |
| `audio-iop-speaker` | `IOPAudioSpeaker` | [`com.apple.driver.IOPAudioSpeaker`](../kexts/com.apple.driver.IOPAudioSpeaker.md) | [`/arm-io/iop-audio-controller/audio-speaker`](../devicetree/root__arm-io__iop-audio-controller__audio-speaker.md) |
| `audio-iop-speaker` | `IOPAudioSpeaker` | [`com.apple.driver.IOPAudioSpeaker`](../kexts/com.apple.driver.IOPAudioSpeaker.md) | [`/arm-io/iop-audio-controller/audio-speaker`](../devicetree/root__arm-io__iop-audio-controller__audio-speaker.md) |
| `audio-leap-internal-loopback` | `AppleAOPAudioClientManager` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) | [`/arm-io/iop-audio-controller/audio-leap-internal-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-leap-internal-loopback.md), [`/arm-io/iop-audio-controller/audio-leap-internal-loopback/audio-leap-internal-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-leap-internal-loopback__audio-leap-internal-loopback.md) |
| `audio-shared-dart-proxy` | `SharedDARTMapperProxy` | [`com.apple.driver.AudioSharedDARTMapperProxy`](../kexts/com.apple.driver.AudioSharedDARTMapperProxy.md) | [`/arm-io/audio-shared-dart-proxy`](../devicetree/root__arm-io__audio-shared-dart-proxy.md) |
| `avd,t8103` | `AppleAVD` | [`com.apple.driver.AppleAVD`](../kexts/com.apple.driver.AppleAVD.md) | [`/arm-io/avd`](../devicetree/root__arm-io__avd.md) |
| `ave2` | `AppleAVE2Driver` | [`com.apple.driver.AppleAVE2`](../kexts/com.apple.driver.AppleAVE2.md) | [`/arm-io/ave`](../devicetree/root__arm-io__ave.md) |
| `backlight` | `AppleARMBacklight` | [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md) | [`/backlight`](../devicetree/root__backlight.md) |
| `baseband,heb` | `AppleBasebandSPMIHEB` | [`com.apple.driver.AppleBasebandINT1`](../kexts/com.apple.driver.AppleBasebandINT1.md) | [`/arm-io/aop-spmi0/baseband-heb`](../devicetree/root__arm-io__aop-spmi0__baseband-heb.md) |
| `baseband,heb` | `AppleSARSPMIHEB` | [`com.apple.driver.AppleSARService`](../kexts/com.apple.driver.AppleSARService.md) | [`/arm-io/aop-spmi0/baseband-heb`](../devicetree/root__arm-io__aop-spmi0__baseband-heb.md) |
| `baseband,idc` | `AppleBasebandSPMIHEB` | [`com.apple.driver.AppleBasebandINT1`](../kexts/com.apple.driver.AppleBasebandINT1.md) | [`/arm-io/aop-spmi1/baseband-idc`](../devicetree/root__arm-io__aop-spmi1__baseband-idc.md) |
| `baseband,idc` | `AppleSARSPMIIDC` | [`com.apple.driver.AppleSARService`](../kexts/com.apple.driver.AppleSARService.md) | [`/arm-io/aop-spmi1/baseband-idc`](../devicetree/root__arm-io__aop-spmi1__baseband-idc.md) |
| `baseband,int1` | `AppleBasebandINT1` | [`com.apple.driver.AppleBasebandINT1`](../kexts/com.apple.driver.AppleBasebandINT1.md) | [`/baseband`](../devicetree/root__baseband.md) |
| `baseband,ptd` | `AppleBasebandSARPTD` | [`com.apple.driver.AppleSARService`](../kexts/com.apple.driver.AppleSARService.md) | [`/arm-io/baseband-ptd`](../devicetree/root__arm-io__baseband-ptd.md) |
| `baseband-pcie-leda` | `AppleConvergedPCILedaBB` | [`com.apple.driver.AppleConvergedIPCBBControl`](../kexts/com.apple.driver.AppleConvergedIPCBBControl.md) | [`/arm-io/apcie/pci-bridge1/baseband-pcie-leda`](../devicetree/root__arm-io__apcie__pci-bridge1__baseband-pcie-leda.md) |
| `biosensor,mesa` | `AppleMesa` | [`com.apple.driver.AppleBiometricSensor`](../kexts/com.apple.driver.AppleBiometricSensor.md) | [`/arm-io/spi1/mesa`](../devicetree/root__arm-io__spi1__mesa.md) |
| `biosensor,mesa` | `AppleSandDollar` | [`com.apple.driver.AppleBiometricSensor`](../kexts/com.apple.driver.AppleBiometricSensor.md) | [`/arm-io/spi1/mesa`](../devicetree/root__arm-io__spi1__mesa.md) |
| `btm,phone` | `AppleBTM` | [`com.apple.driver.ApplePhoneBTM`](../kexts/com.apple.driver.ApplePhoneBTM.md) | [`/arm-io/nub-spmi0/btm`](../devicetree/root__arm-io__nub-spmi0__btm.md) |
| `buttons` | `AppleM68Buttons` | [`com.apple.driver.AppleM68Buttons`](../kexts/com.apple.driver.AppleM68Buttons.md) | [`/buttons`](../devicetree/root__buttons.md) |
| `centauri` | `AppleCentauriManagerHelper` | [`com.apple.driver.AppleCentauriManager`](../kexts/com.apple.driver.AppleCentauriManager.md) | [`/centauri`](../devicetree/root__centauri.md) |
| `clpc,t8160` | `AppleCLPC` | [`com.apple.driver.AppleT8160CLPC`](../kexts/com.apple.driver.AppleT8160CLPC.md) | [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) |
| `cpu-debug-interface` | `AppleARMLightEmUp` | [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md) | [`/arm-io/cpu-debug-interface`](../devicetree/root__arm-io__cpu-debug-interface.md) |
| `dart,t8110` | `AppleT8110DART` | [`com.apple.driver.AppleT8110DART`](../kexts/com.apple.driver.AppleT8110DART.md) | [`/arm-io/dart-ane0`](../devicetree/root__arm-io__dart-ane0.md), [`/arm-io/dart-ane1`](../devicetree/root__arm-io__dart-ane1.md), [`/arm-io/dart-apcie0`](../devicetree/root__arm-io__dart-apcie0.md), [`/arm-io/dart-apcie1`](../devicetree/root__arm-io__dart-apcie1.md), [`/arm-io/dart-avd`](../devicetree/root__arm-io__dart-avd.md), [`/arm-io/dart-ave`](../devicetree/root__arm-io__dart-ave.md) … |
| `dcp-control` | `AppleSPUDCPDriver` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) | [`/arm-io/aop/iop-aop-nub/dcp-control`](../devicetree/root__arm-io__aop__iop-aop-nub__dcp-control.md) |
| `dcp-expert-v1` | `AppleDCPExpert` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) | [`/arm-io/dcp0-expert`](../devicetree/root__arm-io__dcp0-expert.md), [`/arm-io/dcpext0-expert`](../devicetree/root__arm-io__dcpext0-expert.md), [`/arm-io/dcpsec-expert`](../devicetree/root__arm-io__dcpsec-expert.md) |
| `dcp-sac-controller` | `DCPAVSACController` | [`com.apple.driver.DCPAVFamilyProxy`](../kexts/com.apple.driver.DCPAVFamilyProxy.md) | [`/arm-io/dcp-sac-controller`](../devicetree/root__arm-io__dcp-sac-controller.md), [`/arm-io/dcpsec-sac-controller`](../devicetree/root__arm-io__dcpsec-sac-controller.md) |
| `defaults` | `AppleImage4` | [`com.apple.security.AppleImage4`](../kexts/com.apple.security.AppleImage4.md) | [`/defaults`](../devicetree/root__defaults.md) |
| `defaults` | `AppleMobileApNonce` | [`com.apple.driver.AppleMobileApNonce`](../kexts/com.apple.driver.AppleMobileApNonce.md) | [`/defaults`](../devicetree/root__defaults.md) |
| `defaults` | `Image4` | [`com.apple.security.Image4`](../kexts/com.apple.security.Image4.md) | [`/defaults`](../devicetree/root__defaults.md) |
| `diagnostic-data,format1` | `AppleDiagnosticDataAccessReadOnly` | [`com.apple.driver.AppleDiagnosticDataAccessReadOnly`](../kexts/com.apple.driver.AppleDiagnosticDataAccessReadOnly.md) | [`/arm-io/i2c3/display-eeprom-2-hi/display-eeprom-data-2-hi`](../devicetree/root__arm-io__i2c3__display-eeprom-2-hi__display-eeprom-data-2-hi.md), [`/arm-io/i2c3/display-eeprom-2/display-eeprom-data-2`](../devicetree/root__arm-io__i2c3__display-eeprom-2__display-eeprom-data-2.md), [`/arm-io/i2c3/display-eeprom-hi/display-eeprom-data-hi`](../devicetree/root__arm-io__i2c3__display-eeprom-hi__display-eeprom-data-hi.md), [`/arm-io/i2c3/display-eeprom/display-eeprom-data`](../devicetree/root__arm-io__i2c3__display-eeprom__display-eeprom-data.md) |
| `disp0,t8160` | `AppleCLCD2` | [`com.apple.driver.AppleMobileDispH19P-DCP`](../kexts/com.apple.driver.AppleMobileDispH19P-DCP.md) | [`/arm-io/disp0`](../devicetree/root__arm-io__disp0.md) |
| `dispext0,t8160` | `AppleCLCD2` | [`com.apple.driver.AppleMobileDispH19P-DCP`](../kexts/com.apple.driver.AppleMobileDispH19P-DCP.md) | [`/arm-io/dispext0`](../devicetree/root__arm-io__dispext0.md) |
| `display-crossbar,t8112` | `AppleT8112DisplayCrossbar` | [`com.apple.driver.AppleDisplayCrossbar`](../kexts/com.apple.driver.AppleDisplayCrossbar.md) | [`/arm-io/display-crossbar0`](../devicetree/root__arm-io__display-crossbar0.md) |
| `display-generic-data,rw` | `AppleEmbeddedTouchEEPROMDriver` | [`com.apple.driver.AppleEmbeddedTouchEEPROM`](../kexts/com.apple.driver.AppleEmbeddedTouchEEPROM.md) | [`/arm-io/i2c3/display-eeprom-2/display-eeprom-generic-data-2`](../devicetree/root__arm-io__i2c3__display-eeprom-2__display-eeprom-generic-data-2.md), [`/arm-io/i2c3/display-eeprom/display-eeprom-generic-data`](../devicetree/root__arm-io__i2c3__display-eeprom__display-eeprom-generic-data.md) |
| `display-health-monitor` | `DisplayHealthMonitorCompanion` | [`com.apple.driver.DisplayHealthMonitorCompanion`](../kexts/com.apple.driver.DisplayHealthMonitorCompanion.md) | [`/display-health-monitor`](../devicetree/root__display-health-monitor.md) |
| `dispsec,t8160` | `AppleCLCD2` | [`com.apple.driver.AppleMobileDispH19P-DCP`](../kexts/com.apple.driver.AppleMobileDispH19P-DCP.md) | [`/arm-io/dispsec`](../devicetree/root__arm-io__dispsec.md) |
| `dock,0pin` | `IOAccessoryDock0PinBuiltin` | [`com.apple.iokit.IOAccessoryManager`](../kexts/com.apple.iokit.IOAccessoryManager.md) | [`/port-magsafe-1`](../devicetree/root__port-magsafe-1.md) |
| `dockchannel-uart` | `AppleSerialShim` | [`com.apple.driver.AppleSerialShim`](../kexts/com.apple.driver.AppleSerialShim.md) | [`/arm-io/dockchannel-uart`](../devicetree/root__arm-io__dockchannel-uart.md) |
| `dp-audio0` | `DCPAVAudioDMADelegate` | [`com.apple.driver.DCPAVFamilyProxy`](../kexts/com.apple.driver.DCPAVFamilyProxy.md) | [`/arm-io/dp-audio0`](../devicetree/root__arm-io__dp-audio0.md) |
| `dp-audio1` | `DCPAVAudioDMADelegate` | [`com.apple.driver.DCPAVFamilyProxy`](../kexts/com.apple.driver.DCPAVFamilyProxy.md) | [`/arm-io/dp-audio1`](../devicetree/root__arm-io__dp-audio1.md) |
| `eeprom,i2c` | `AppleARMI2CEEPROM` | [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md) | [`/arm-io/i2c3/display-eeprom`](../devicetree/root__arm-io__i2c3__display-eeprom.md), [`/arm-io/i2c3/display-eeprom-2`](../devicetree/root__arm-io__i2c3__display-eeprom-2.md), [`/arm-io/i2c3/display-eeprom-2-hi`](../devicetree/root__arm-io__i2c3__display-eeprom-2-hi.md), [`/arm-io/i2c3/display-eeprom-hi`](../devicetree/root__arm-io__i2c3__display-eeprom-hi.md) |
| `error-handler,t8160` | `AppleSoCErrorHandler` | [`com.apple.driver.AppleT8160`](../kexts/com.apple.driver.AppleT8160.md) | [`/arm-io/error-handler`](../devicetree/root__arm-io__error-handler.md) |
| `event-log-handler,t8101` | `AppleEventLogHandler` | [`com.apple.driver.AppleEventLogHandler`](../kexts/com.apple.driver.AppleEventLogHandler.md) | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) |
| `exbright` | `EXBrightKext` | [`com.apple.EXBrightKext`](../kexts/com.apple.EXBrightKext.md) | [`/exbright`](../devicetree/root__exbright.md) |
| `exclaves-test` | `AppleExclaveExampleKext` | [`com.apple.ExclaveKextClient`](../kexts/com.apple.ExclaveKextClient.md) | [`/exclaves-test`](../devicetree/root__exclaves-test.md) |
| `exdisplaypipe,t8160` | `EXDisplayPipe` | [`com.apple.driver.EXDisplayPipeH19P`](../kexts/com.apple.driver.EXDisplayPipeH19P.md) | [`/arm-io/exdisplaypipe`](../devicetree/root__arm-io__exdisplaypipe.md) |
| `exdisplaypipe1,t8160` | `EXDisplayPipe` | [`com.apple.driver.EXDisplayPipeH19P`](../kexts/com.apple.driver.EXDisplayPipeH19P.md) | [`/arm-io/exdisplaypipe1`](../devicetree/root__arm-io__exdisplaypipe1.md) |
| `fpwm,s5l8920x` | `AppleS5L8920XFPWM` | [`com.apple.driver.AppleS5L8920XPWM`](../kexts/com.apple.driver.AppleS5L8920XPWM.md) | [`/arm-io/fpwm`](../devicetree/root__arm-io__fpwm.md) |
| `gnss` | `AppleSPUGNSSDriver` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) | [`/arm-io/aop/iop-aop-nub/gnss`](../devicetree/root__arm-io__aop__iop-aop-nub__gnss.md) |
| `gpio,t8101` | `AppleT8101GPIOIC` | [`com.apple.driver.AppleGPIOICController`](../kexts/com.apple.driver.AppleGPIOICController.md) | [`/arm-io/aop-gpio`](../devicetree/root__arm-io__aop-gpio.md), [`/arm-io/gpio0`](../devicetree/root__arm-io__gpio0.md), [`/arm-io/mtp-gpio`](../devicetree/root__arm-io__mtp-gpio.md), [`/arm-io/nub-gpio`](../devicetree/root__arm-io__nub-gpio.md), [`/arm-io/smc-gpio`](../devicetree/root__arm-io__smc-gpio.md) |
| `gpio-canary,t8101` | `AppleGPIOCanary` | [`com.apple.driver.AppleGPIOCanary`](../kexts/com.apple.driver.AppleGPIOCanary.md) | [`/arm-io/gpio-canary`](../devicetree/root__arm-io__gpio-canary.md) |
| `gpu,t8160` | `AGXAcceleratorG19P` | [`com.apple.AGXG19P`](../kexts/com.apple.AGXG19P.md) | [`/arm-io/sgx`](../devicetree/root__arm-io__sgx.md) |
| `grimaldi-control` | `AppleSPUGrimaldiDriver` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) | [`/arm-io/aop/iop-aop-nub/grimaldi-control`](../devicetree/root__arm-io__aop__iop-aop-nub__grimaldi-control.md) |
| `haptics-support,leap` | `AppleHapticsSupportLEAP` | [`com.apple.driver.AppleHapticsSupportLEAP`](../kexts/com.apple.driver.AppleHapticsSupportLEAP.md) | [`/arm-io/haptics-support-interface`](../devicetree/root__arm-io__haptics-support-interface.md) |
| `i2c,s5l8940x` | `AppleS5L8940XI2CController` | [`com.apple.driver.AppleS5L8940XI2C`](../kexts/com.apple.driver.AppleS5L8940XI2C.md) | [`/arm-io/i2c2`](../devicetree/root__arm-io__i2c2.md), [`/arm-io/i2c3`](../devicetree/root__arm-io__i2c3.md), [`/arm-io/i2c4`](../devicetree/root__arm-io__i2c4.md) |
| `iic,soft` | `AppleARMSoftIICController` | [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md) | [`/arm-io/i2c2`](../devicetree/root__arm-io__i2c2.md), [`/arm-io/i2c3`](../devicetree/root__arm-io__i2c3.md), [`/arm-io/i2c4`](../devicetree/root__arm-io__i2c4.md) |
| `iisaudio,isolated-output-stream-proxy` | `IISAudioIsolatedOutputStreamECProxy` | [`com.apple.driver.IISAudioIsolatedStreamECProxy`](../kexts/com.apple.driver.IISAudioIsolatedStreamECProxy.md) | [`/arm-io/audio-receiver-tx-stream-proxy`](../devicetree/root__arm-io__audio-receiver-tx-stream-proxy.md), [`/arm-io/audio-speaker-tx-stream-proxy`](../devicetree/root__arm-io__audio-speaker-tx-stream-proxy.md) |
| `iisaudio,isolated-stream-proxy` | `IISAudioIsolatedStreamECProxy` | [`com.apple.driver.IISAudioIsolatedStreamECProxy`](../kexts/com.apple.driver.IISAudioIsolatedStreamECProxy.md) | [`/arm-io/audio-hp-proxy`](../devicetree/root__arm-io__audio-hp-proxy.md), [`/arm-io/audio-sllb-proxy`](../devicetree/root__arm-io__audio-sllb-proxy.md) |
| `iommu-mapper` | `IODARTMapper` | [`com.apple.driver.IODARTFamily`](../kexts/com.apple.driver.IODARTFamily.md) | [`/arm-io/dart-ane0/mapper-ane0`](../devicetree/root__arm-io__dart-ane0__mapper-ane0.md), [`/arm-io/dart-ane0/mapper-ane0-iso1`](../devicetree/root__arm-io__dart-ane0__mapper-ane0-iso1.md), [`/arm-io/dart-ane0/mapper-ane0-iso2`](../devicetree/root__arm-io__dart-ane0__mapper-ane0-iso2.md), [`/arm-io/dart-ane0/mapper-ane0-iso3`](../devicetree/root__arm-io__dart-ane0__mapper-ane0-iso3.md), [`/arm-io/dart-ane0/mapper-ane0-iso4`](../devicetree/root__arm-io__dart-ane0__mapper-ane0-iso4.md), [`/arm-io/dart-ane0/mapper-ane0-iso5`](../devicetree/root__arm-io__dart-ane0__mapper-ane0-iso5.md) … |
| `iommu-mapper,gfx` | `AGXArmFirmwareMapper` | [`com.apple.AGXG19P`](../kexts/com.apple.AGXG19P.md) | [`/arm-io/mapper-gfx-asc`](../devicetree/root__arm-io__mapper-gfx-asc.md) |
| `iop,ascwrap-v8` | `AppleASCWrapV8` | [`com.apple.driver.AppleA7IOP-ASCWrap-v8`](../kexts/com.apple.driver.AppleA7IOP-ASCWrap-v8.md) | [`/arm-io/ans`](../devicetree/root__arm-io__ans.md), [`/arm-io/aop`](../devicetree/root__arm-io__aop.md), [`/arm-io/aop2`](../devicetree/root__arm-io__aop2.md), [`/arm-io/dcp`](../devicetree/root__arm-io__dcp.md), [`/arm-io/dcpext0`](../devicetree/root__arm-io__dcpext0.md), [`/arm-io/dcpsec`](../devicetree/root__arm-io__dcpsec.md) … |
| `iop,exclave-sep-manager` | `ExclaveSEPManagerProxy` | [`com.apple.driver.ExclaveSEPManagerProxy`](../kexts/com.apple.driver.ExclaveSEPManagerProxy.md) | [`/arm-io/esm`](../devicetree/root__arm-io__esm.md) |
| `iop,secure-rtbuddy-ioreporting` | `SecureRTBuddyIOReporting` | [`com.apple.driver.SecureRTBuddyProxy`](../kexts/com.apple.driver.SecureRTBuddyProxy.md) | [`/arm-io/aop-exclave-ioreporting`](../devicetree/root__arm-io__aop-exclave-ioreporting.md), [`/arm-io/dcp-exclave-ioreporting`](../devicetree/root__arm-io__dcp-exclave-ioreporting.md), [`/arm-io/dcpsec-exclave-ioreporting`](../devicetree/root__arm-io__dcpsec-exclave-ioreporting.md) |
| `iop,secure-rtbuddy-proxy` | `SecureRTBuddyProxy` | [`com.apple.driver.SecureRTBuddyProxy`](../kexts/com.apple.driver.SecureRTBuddyProxy.md) | [`/arm-io/aop-exclave-mailbox`](../devicetree/root__arm-io__aop-exclave-mailbox.md), [`/arm-io/aop2-exclave-mailbox`](../devicetree/root__arm-io__aop2-exclave-mailbox.md), [`/arm-io/dcp-exclave-mailbox`](../devicetree/root__arm-io__dcp-exclave-mailbox.md), [`/arm-io/dcpsec-exclave-mailbox`](../devicetree/root__arm-io__dcpsec-exclave-mailbox.md) |
| `iop-adma-stream,leap` | `AppleIOPADMAStream` | [`com.apple.driver.AppleIOPADMAStream`](../kexts/com.apple.driver.AppleIOPADMAStream.md) | [`/arm-io/iop-audio-controller/audio-haptic-transport`](../devicetree/root__arm-io__iop-audio-controller__audio-haptic-transport.md), [`/arm-io/iop-audio-controller/audio-hpdbg-transport`](../devicetree/root__arm-io__iop-audio-controller__audio-hpdbg-transport.md), [`/arm-io/iop-audio-controller/audio-leap-internal-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-leap-internal-loopback.md), [`/arm-io/iop-audio-controller/audio-s-leap-internal-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-s-leap-internal-loopback.md) |
| `iop-adma-stream,mca` | `AppleIOPADMAStream` | [`com.apple.driver.AppleIOPADMAStream`](../kexts/com.apple.driver.AppleIOPADMAStream.md) | [`/arm-io/iop-audio-controller/audio-flicker`](../devicetree/root__arm-io__iop-audio-controller__audio-flicker.md), [`/arm-io/iop-audio-controller/audio-hp`](../devicetree/root__arm-io__iop-audio-controller__audio-hp.md), [`/arm-io/iop-audio-controller/audio-mca-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-mca-loopback.md), [`/arm-io/iop-audio-controller/audio-receiver`](../devicetree/root__arm-io__iop-audio-controller__audio-receiver.md), [`/arm-io/iop-audio-controller/audio-speaker-mca`](../devicetree/root__arm-io__iop-audio-controller__audio-speaker-mca.md), [`/arm-io/iop-audio-controller/audio-speaker-tap`](../devicetree/root__arm-io__iop-audio-controller__audio-speaker-tap.md) … |
| `iop-ane,ascwrap-v8` | `AppleASCWrapV8ANE` | [`com.apple.driver.AppleA7IOP-ASCWrap-v8`](../kexts/com.apple.driver.AppleA7IOP-ASCWrap-v8.md) | [`/arm-io/ane0`](../devicetree/root__arm-io__ane0.md), [`/arm-io/ane1`](../devicetree/root__arm-io__ane1.md) |
| `iop-aop-nub` | `AppleLVBOOST` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) | [`/arm-io/aop/iop-aop-nub`](../devicetree/root__arm-io__aop__iop-aop-nub.md) |
| `iop-aop-nub` | `AppleSPUTimesyncV2` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) | [`/arm-io/aop/iop-aop-nub`](../devicetree/root__arm-io__aop__iop-aop-nub.md) |
| `iop-audio,aop-service` | `AOPAudioService` | [`com.apple.driver.AOPAudio2`](../kexts/com.apple.driver.AOPAudio2.md) | [`/arm-io/aop/iop-aop-nub/aop-audio`](../devicetree/root__arm-io__aop__iop-aop-nub__aop-audio.md), [`/arm-io/aop/iop-aop-nub/aop-voicetrigger`](../devicetree/root__arm-io__aop__iop-aop-nub__aop-voicetrigger.md) |
| `iop-audio,client-manager-device` | `IOPAudioClientManagerDevice` | [`com.apple.driver.IOPAudioClientManagerDevice`](../kexts/com.apple.driver.IOPAudioClientManagerDevice.md) | [`/arm-io/iop-audio-controller/siri-listening-device`](../devicetree/root__arm-io__iop-audio-controller__siri-listening-device.md) |
| `iop-audio,controller` | `IOPAudioController` | [`com.apple.iokit.IOPAudioDriverFamily`](../kexts/com.apple.iokit.IOPAudioDriverFamily.md) | [`/arm-io/iop-audio-controller`](../devicetree/root__arm-io__iop-audio-controller.md), [`/arm-io/iop-voicetrigger-controller`](../devicetree/root__arm-io__iop-voicetrigger-controller.md) |
| `iop-audio,haptics-leap-control-device` | `IOPAudioHapticsLEAPControlDevice` | [`com.apple.driver.IOPAudioHapticsLEAPControlDevice`](../kexts/com.apple.driver.IOPAudioHapticsLEAPControlDevice.md) | [`/arm-io/iop-audio-controller/audio-haptic-leap`](../devicetree/root__arm-io__iop-audio-controller__audio-haptic-leap.md) |
| `iop-audio,isolated-io-buffer-device` | `IOPAudioIsolatedIOBufferDevice` | [`com.apple.driver.IOPAudioIsolatedIOBufferDevice`](../kexts/com.apple.driver.IOPAudioIsolatedIOBufferDevice.md) | [`/arm-io/iop-audio-controller/lp-mic-io-buffer-device`](../devicetree/root__arm-io__iop-audio-controller__lp-mic-io-buffer-device.md) |
| `iop-audio,isolated-vt-device` | `IOPAudioIsolatedVoiceTriggerDevice` | [`com.apple.driver.IOPAudioVoiceTriggerDevice`](../kexts/com.apple.driver.IOPAudioVoiceTriggerDevice.md) | [`/arm-io/iop-voicetrigger-controller/audio-vt-device`](../devicetree/root__arm-io__iop-voicetrigger-controller__audio-vt-device.md) |
| `iop-audio,lp-mic-device` | `IOPAudioLPMicDevice` | [`com.apple.driver.IOPAudioLPMicDevice`](../kexts/com.apple.driver.IOPAudioLPMicDevice.md) | [`/arm-io/iop-audio-controller/lp-mic-device`](../devicetree/root__arm-io__iop-audio-controller__lp-mic-device.md) |
| `iop-audio,pcm-asset-manager-device` | `IOPAudioPCMAssetManagerDevice` | [`com.apple.driver.IOPAudioPCMAssetManagerDevice`](../kexts/com.apple.driver.IOPAudioPCMAssetManagerDevice.md) | [`/arm-io/iop-audio-controller/audio-hw-pcm-audiomgr`](../devicetree/root__arm-io__iop-audio-controller__audio-hw-pcm-audiomgr.md) |
| `iop-isp,ascwrap-v8` | `AppleASCWrapV8SISP` | [`com.apple.driver.AppleA7IOP-ASCWrap-v8`](../kexts/com.apple.driver.AppleA7IOP-ASCWrap-v8.md) | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) |
| `iop-nub,rtbuddy-v2` | `RTBuddy` | [`com.apple.driver.RTBuddy`](../kexts/com.apple.driver.RTBuddy.md) | [`/arm-io/ane0/iop-ane0-nub`](../devicetree/root__arm-io__ane0__iop-ane0-nub.md), [`/arm-io/ane1/iop-ane1-nub`](../devicetree/root__arm-io__ane1__iop-ane1-nub.md), [`/arm-io/ans/iop-ans-nub`](../devicetree/root__arm-io__ans__iop-ans-nub.md), [`/arm-io/aop/iop-aop-nub`](../devicetree/root__arm-io__aop__iop-aop-nub.md), [`/arm-io/aop2/iop-aop2-nub`](../devicetree/root__arm-io__aop2__iop-aop2-nub.md), [`/arm-io/dcp/iop-dcp-nub`](../devicetree/root__arm-io__dcp__iop-dcp-nub.md) … |
| `iop-nub,sep` | `AppleSEPManager` | [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md) | [`/arm-io/sep/iop-sep-nub`](../devicetree/root__arm-io__sep__iop-sep-nub.md) |
| `iop-nub,sep` | `AppleSEPManager` | [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md) | [`/arm-io/sep/iop-sep-nub`](../devicetree/root__arm-io__sep__iop-sep-nub.md) |
| `iop-sep,ascwrap-v8` | `AppleASCWrapV8SEP` | [`com.apple.driver.AppleA7IOP-ASCWrap-v8`](../kexts/com.apple.driver.AppleA7IOP-ASCWrap-v8.md) | [`/arm-io/sep`](../devicetree/root__arm-io__sep.md) |
| `isp,isp-exclave-proxy` | `AppleExclaveCameraProxy` | [`com.apple.driver.AppleCamera`](../kexts/com.apple.driver.AppleCamera.md) | [`/arm-io/isp-exclave-proxy`](../devicetree/root__arm-io__isp-exclave-proxy.md) |
| `isp,isp-generic-ex` | `AppleCamera` | [`com.apple.driver.AppleCamera`](../kexts/com.apple.driver.AppleCamera.md) | [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) |
| `jpeg,s5l8920x` | `AppleJPEGDriver` | [`com.apple.driver.AppleJPEGDriver`](../kexts/com.apple.driver.AppleJPEGDriver.md) | [`/arm-io/jpeg`](../devicetree/root__arm-io__jpeg.md) |
| `mcc,t8160` | `AppleT8160MemCacheController` | [`com.apple.driver.AppleT8160MCC`](../kexts/com.apple.driver.AppleT8160MCC.md) | [`/arm-io/mcc`](../devicetree/root__arm-io__mcc.md) |
| `mogul,a1222` | `MogulAuthI2CRelayInterface` | [`com.apple.driver.AppleAuthCP`](../kexts/com.apple.driver.AppleAuthCP.md) | [`/arm-io/i2c3/mogul-display`](../devicetree/root__arm-io__i2c3__mogul-display.md), [`/arm-io/i2c3/mogul-display2`](../devicetree/root__arm-io__i2c3__mogul-display2.md), [`/arm-io/i2c4/mogul-mlb`](../devicetree/root__arm-io__i2c4__mogul-mlb.md) |
| `mogul,a1222` | `MogulAuthSMCRelayInterface` | [`com.apple.driver.AppleAuthCP`](../kexts/com.apple.driver.AppleAuthCP.md) | [`/arm-io/i2c3/mogul-display`](../devicetree/root__arm-io__i2c3__mogul-display.md), [`/arm-io/i2c3/mogul-display2`](../devicetree/root__arm-io__i2c3__mogul-display2.md), [`/arm-io/i2c4/mogul-mlb`](../devicetree/root__arm-io__i2c4__mogul-mlb.md) |
| `msg-mapper` | `AppleMSGKext` | [`com.apple.driver.AppleMSG`](../kexts/com.apple.driver.AppleMSG.md) | [`/arm-io/msg`](../devicetree/root__arm-io__msg.md) |
| `multi-touch` | `AppleSPUControl` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) | [`/arm-io/mtp/iop-mtp-nub/multi-touch`](../devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch.md) |
| `nfc,primary,gpio` | `AppleStockholmControl` | [`com.apple.driver.AppleStockholmControl`](../kexts/com.apple.driver.AppleStockholmControl.md) | [`/arm-io/aop-spmi0/stockholm-spmi/stockholm`](../devicetree/root__arm-io__aop-spmi0__stockholm-spmi__stockholm.md) |
| `nfc,primary,spmi` | `AppleStockholmSPMI` | [`com.apple.driver.AppleStockholmControl`](../kexts/com.apple.driver.AppleStockholmControl.md) | [`/arm-io/aop-spmi0/stockholm-spmi`](../devicetree/root__arm-io__aop-spmi0__stockholm-spmi.md) |
| `nfc,secondary,gpio` | `AppleStockholmControl` | [`com.apple.driver.AppleStockholmControl`](../kexts/com.apple.driver.AppleStockholmControl.md) | [`/arm-io/aop-spmi0/hammerfest-spmi/hammerfest`](../devicetree/root__arm-io__aop-spmi0__hammerfest-spmi__hammerfest.md) |
| `nfc,secondary,spmi` | `AppleStockholmSPMI` | [`com.apple.driver.AppleStockholmControl`](../kexts/com.apple.driver.AppleStockholmControl.md) | [`/arm-io/aop-spmi0/hammerfest-spmi`](../devicetree/root__arm-io__aop-spmi0__hammerfest-spmi.md) |
| `pcie-apiodma,gen3p0` | `ApplePCIePIODMA` | [`com.apple.driver.ApplePCIePIODMAGen3p0`](../kexts/com.apple.driver.ApplePCIePIODMAGen3p0.md) | [`/arm-io/apcie0-piodma`](../devicetree/root__arm-io__apcie0-piodma.md), [`/arm-io/apcie1-piodma`](../devicetree/root__arm-io__apcie1-piodma.md) |
| `plce,t8160` | `APCIECoreRCGen5PLCE` | [`com.apple.driver.AppleT8160PCIe`](../kexts/com.apple.driver.AppleT8160PCIe.md) | [`/arm-io/apcie0-plce`](../devicetree/root__arm-io__apcie0-plce.md), [`/arm-io/apcie1-plce`](../devicetree/root__arm-io__apcie1-plce.md) |
| `pmgr2,arch` | `ApplePMGRv2` | [`com.apple.driver.ApplePMGR`](../kexts/com.apple.driver.ApplePMGR.md) | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) |
| `pmgr2,t8160` | `AppleT8160PMGR` | [`com.apple.driver.AppleT8160PMGR`](../kexts/com.apple.driver.AppleT8160PMGR.md) | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) |
| `pmu,spmi` | `AppleDialogSPMIPMU` | [`com.apple.driver.AppleSPMIPMU`](../kexts/com.apple.driver.AppleSPMIPMU.md) | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md), [`/arm-io/nub-spmi0/pmu-main/sgpio-bridge-pmu-main/pmu-secondary`](../devicetree/root__arm-io__nub-spmi0__pmu-main__sgpio-bridge-pmu-main__pmu-secondary.md) |
| `pmu,spmi` | `ApplePMUFirmwareDriver` | [`com.apple.driver.ApplePMUFirmwareDriver`](../kexts/com.apple.driver.ApplePMUFirmwareDriver.md) | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md), [`/arm-io/nub-spmi0/pmu-main/sgpio-bridge-pmu-main/pmu-secondary`](../devicetree/root__arm-io__nub-spmi0__pmu-main__sgpio-bridge-pmu-main__pmu-secondary.md) |
| `ppm,iphoneacsk` | `ApplePPMCPMSv2` | [`com.apple.driver.AppleiPhoneACSKPPM`](../kexts/com.apple.driver.AppleiPhoneACSKPPM.md) | [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) |
| `ptd,v1` | `ApplePTD` | [`com.apple.driver.ApplePTD`](../kexts/com.apple.driver.ApplePTD.md) | [`/arm-io/aon-ptd`](../devicetree/root__arm-io__aon-ptd.md) |
| `rose` | `AppleSPURoseDriver` | [`com.apple.driver.AppleSPURose`](../kexts/com.apple.driver.AppleSPURose.md) | [`/arm-io/aop/iop-aop-nub/rose`](../devicetree/root__arm-io__aop__iop-aop-nub__rose.md) |
| `rose` | `AppleSPURoseDriverV2` | [`com.apple.driver.AppleSPURose`](../kexts/com.apple.driver.AppleSPURose.md) | [`/arm-io/aop/iop-aop-nub/rose`](../devicetree/root__arm-io__aop__iop-aop-nub__rose.md) |
| `sacm` | `AppleARMSlowAdaptiveClockingManager` | [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md) | [`/sacm-general`](../devicetree/root__sacm-general.md), [`/sacm-jasper`](../devicetree/root__sacm-jasper.md) |
| `sart,coastguard` | `IOCoastGuardSARTMapper` | [`com.apple.driver.AppleSART`](../kexts/com.apple.driver.AppleSART.md) | [`/arm-io/sart-ans`](../devicetree/root__arm-io__sart-ans.md) |
| `scaler,s5l8960x` | `AppleM2ScalerCSCDriver` | [`com.apple.driver.AppleM2ScalerCSCDriver`](../kexts/com.apple.driver.AppleM2ScalerCSCDriver.md) | [`/arm-io/scaler0`](../devicetree/root__arm-io__scaler0.md) |
| `secure-repair,1` | `AppleSecureRepair` | [`com.apple.driver.AppleSecureRepair`](../kexts/com.apple.driver.AppleSecureRepair.md) | [`/arm-io/secure-repair`](../devicetree/root__arm-io__secure-repair.md) |
| `sgpio-bridge` | `AppleSGPIOHostBridgeController` | [`com.apple.driver.AppleSGPIO`](../kexts/com.apple.driver.AppleSGPIO.md) | [`/arm-io/nub-spmi0/pmu-main/sgpio-bridge-pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main__sgpio-bridge-pmu-main.md) |
| `smc-acam` | `AppleSMCACAMDriver` | [`com.apple.driver.AppleSMC`](../kexts/com.apple.driver.AppleSMC.md) | [`/arm-io/smc/iop-smc-nub/smc-acam`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-acam.md) |
| `smc-aop` | `AppleAOPSMC` | [`com.apple.driver.AppleSMC`](../kexts/com.apple.driver.AppleSMC.md) | [`/arm-io/smc/iop-smc-nub/smc-aop`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-aop.md) |
| `smc-charger` | `AppleSMCCharger` | [`com.apple.driver.AppleSMC`](../kexts/com.apple.driver.AppleSMC.md) | [`/arm-io/smc/iop-smc-nub/smc-charger`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-charger.md) |
| `smc-charger-util` | `AppleSMCChargerUtil` | [`com.apple.driver.AppleSMC`](../kexts/com.apple.driver.AppleSMC.md) | [`/arm-io/smc/iop-smc-nub/smc-charger-util`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-charger-util.md) |
| `smc-control` | `AppleAOPSMCDriver` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) | [`/arm-io/aop/iop-aop-nub/smc-control`](../devicetree/root__arm-io__aop__iop-aop-nub__smc-control.md) |
| `smc-ext-charger` | `AppleSMCWirelessCharger` | [`com.apple.driver.AppleSMCWirelessCharger`](../kexts/com.apple.driver.AppleSMCWirelessCharger.md) | [`/arm-io/smc/iop-smc-nub/smc-ext-charger`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-ext-charger.md) |
| `smc-pmu` | `AppleSMCPMU` | [`com.apple.driver.AppleSMC`](../kexts/com.apple.driver.AppleSMC.md) | [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) |
| `smc-power-out` | `AppleSMCPowerOut` | [`com.apple.driver.AppleSMC`](../kexts/com.apple.driver.AppleSMC.md) | [`/arm-io/smc/iop-smc-nub/smc-power-out`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-power-out.md) |
| `smc-tempsensor` | `AppleSMCSensorDispatcher` | [`com.apple.driver.AppleSMC`](../kexts/com.apple.driver.AppleSMC.md) | [`/arm-io/smctempsensor0`](../devicetree/root__arm-io__smctempsensor0.md) |
| `soc-misc,t8160` | `AppleSoCMisc` | [`com.apple.driver.AppleT8160`](../kexts/com.apple.driver.AppleT8160.md) | [`/arm-io/soc-misc`](../devicetree/root__arm-io__soc-misc.md) |
| `soc-reporter,t8160` | `AppleSoCReporter` | [`com.apple.driver.AppleT8160`](../kexts/com.apple.driver.AppleT8160.md) | [`/arm-io/soc-reporter`](../devicetree/root__arm-io__soc-reporter.md) |
| `spi-1,spimc` | `AppleSPIMCController` | [`com.apple.driver.AppleSPIMC`](../kexts/com.apple.driver.AppleSPIMC.md) | [`/arm-io/spi1`](../devicetree/root__arm-io__spi1.md) |
| `timestamp-sync` | `AppleMultitouchTimestampSync` | [`com.apple.driver.AppleMultitouchDriver`](../kexts/com.apple.driver.AppleMultitouchDriver.md) | [`/arm-io/mt-bt-timestamp-sync`](../devicetree/root__arm-io__mt-bt-timestamp-sync.md) |
| `uart-1,samsung` | `AppleSamsungSerial` | [`com.apple.driver.AppleSamsungSerial`](../kexts/com.apple.driver.AppleSamsungSerial.md) | [`/arm-io/uart0`](../devicetree/root__arm-io__uart0.md) |
| `uart0` | `AppleSerialShim` | [`com.apple.driver.AppleSerialShim`](../kexts/com.apple.driver.AppleSerialShim.md) | [`/arm-io/uart0`](../devicetree/root__arm-io__uart0.md) |
| `usb-drd,t8160` | `AppleT8160USBXDCI` | [`com.apple.driver.AppleUSBXDCIARM`](../kexts/com.apple.driver.AppleUSBXDCIARM.md) | [`/arm-io/usb-drd0`](../devicetree/root__arm-io__usb-drd0.md) |
| `usb-drd,t8160` | `AppleT8160USBXHCI` | [`com.apple.driver.usb.AppleSynopsysUSBXHCI`](../kexts/com.apple.driver.usb.AppleSynopsysUSBXHCI.md) | [`/arm-io/usb-drd0`](../devicetree/root__arm-io__usb-drd0.md) |
| `usbc,cbtl1702,spmi` | `AppleHPMARMSPMI` | [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md) | [`/arm-io/nub-spmi2/spmi-hpm0`](../devicetree/root__arm-io__nub-spmi2__spmi-hpm0.md) |
| `wdt,s5l8960x` | `AppleARMWatchdogTimer` | [`com.apple.driver.AppleARMWatchdogTimer`](../kexts/com.apple.driver.AppleARMWatchdogTimer.md) | [`/arm-io/wdt`](../devicetree/root__arm-io__wdt.md) |
| `wlan,idc` | `AppleSARSPMIIDCWLAN` | [`com.apple.driver.AppleSARService`](../kexts/com.apple.driver.AppleSARService.md) | [`/arm-io/aop-spmi1/wlan-idc`](../devicetree/root__arm-io__aop-spmi1__wlan-idc.md) |

## No node on the Duo

| Match string | IOClass | kext |
|---|---|---|
| `AAPL,atc-dpin` | `AppleATCDPINAdapterPort` | [`com.apple.driver.AppleDisplayCrossbar`](../kexts/com.apple.driver.AppleDisplayCrossbar.md) |
| `AAPL,atc-dpin` | `IODPTXVirtualPort` | [`com.apple.iokit.IODisplayPortFamily`](../kexts/com.apple.iokit.IODisplayPortFamily.md) |
| `AAPL,atc-dpout` | `AppleATCDPOUTAdapterPort` | [`com.apple.driver.AppleDisplayCrossbar`](../kexts/com.apple.driver.AppleDisplayCrossbar.md) |
| `AAPL,atc-dpphy` | `AppleATCDPAltModePort` | [`com.apple.driver.AppleDisplayCrossbar`](../kexts/com.apple.driver.AppleDisplayCrossbar.md) |
| `AAPL,atc-dpphy` | `AppleATCDPHDMIPort` | [`com.apple.driver.AppleDisplayCrossbar`](../kexts/com.apple.driver.AppleDisplayCrossbar.md) |
| `AAPL,atc-dpphy` | `IODPTXVirtualPort` | [`com.apple.iokit.IODisplayPortFamily`](../kexts/com.apple.iokit.IODisplayPortFamily.md) |
| `AAPL,display-crossbar` | `AppleDisplayCrossbar` | [`com.apple.driver.AppleDisplayCrossbar`](../kexts/com.apple.driver.AppleDisplayCrossbar.md) |
| `AAPL,dptx-phy` | `IODPTXVirtualPort` | [`com.apple.iokit.IODisplayPortFamily`](../kexts/com.apple.iokit.IODisplayPortFamily.md) |
| `AOP2Endpoint1` | `AFKEPKextV2` | [`com.apple.driver.AppleAOP2`](../kexts/com.apple.driver.AppleAOP2.md) |
| `AOP2Endpoint10` | `AFKEPKextV2` | [`com.apple.driver.AppleAOP2`](../kexts/com.apple.driver.AppleAOP2.md) |
| `AOP2Endpoint11` | `AFKEPKextV2` | [`com.apple.driver.AppleAOP2`](../kexts/com.apple.driver.AppleAOP2.md) |
| `AOP2Endpoint12` | `AFKEPKextV2` | [`com.apple.driver.AppleAOP2`](../kexts/com.apple.driver.AppleAOP2.md) |
| `AOP2Endpoint13` | `AFKEPKextV2` | [`com.apple.driver.AppleAOP2`](../kexts/com.apple.driver.AppleAOP2.md) |
| `AOP2Endpoint14` | `AFKEPKextV2` | [`com.apple.driver.AppleAOP2`](../kexts/com.apple.driver.AppleAOP2.md) |
| `AOP2Endpoint15` | `AFKEPKextV2` | [`com.apple.driver.AppleAOP2`](../kexts/com.apple.driver.AppleAOP2.md) |
| `AOP2Endpoint16` | `AFKEPKextV2` | [`com.apple.driver.AppleAOP2`](../kexts/com.apple.driver.AppleAOP2.md) |
| `AOP2Endpoint17` | `AFKEPKextV2` | [`com.apple.driver.AppleAOP2`](../kexts/com.apple.driver.AppleAOP2.md) |
| `AOP2Endpoint18` | `AFKEPKextV2` | [`com.apple.driver.AppleAOP2`](../kexts/com.apple.driver.AppleAOP2.md) |
| `AOP2Endpoint19` | `AFKEPKextV2` | [`com.apple.driver.AppleAOP2`](../kexts/com.apple.driver.AppleAOP2.md) |
| `AOP2Endpoint2` | `AFKEPKextV2` | [`com.apple.driver.AppleAOP2`](../kexts/com.apple.driver.AppleAOP2.md) |
| `AOP2Endpoint20` | `AFKEPKextV2` | [`com.apple.driver.AppleAOP2`](../kexts/com.apple.driver.AppleAOP2.md) |
| `AOP2Endpoint21` | `AFKEPKextV2` | [`com.apple.driver.AppleAOP2`](../kexts/com.apple.driver.AppleAOP2.md) |
| `AOP2Endpoint22` | `AFKEPKextV2` | [`com.apple.driver.AppleAOP2`](../kexts/com.apple.driver.AppleAOP2.md) |
| `AOP2Endpoint23` | `AFKEPKextV2` | [`com.apple.driver.AppleAOP2`](../kexts/com.apple.driver.AppleAOP2.md) |
| `AOP2Endpoint24` | `AFKEPKextV2` | [`com.apple.driver.AppleAOP2`](../kexts/com.apple.driver.AppleAOP2.md) |
| `AOP2Endpoint3` | `AFKEPKextV2` | [`com.apple.driver.AppleAOP2`](../kexts/com.apple.driver.AppleAOP2.md) |
| `AOP2Endpoint4` | `AFKEPKextV2` | [`com.apple.driver.AppleAOP2`](../kexts/com.apple.driver.AppleAOP2.md) |
| `AOP2Endpoint5` | `AFKEPKextV2` | [`com.apple.driver.AppleAOP2`](../kexts/com.apple.driver.AppleAOP2.md) |
| `AOP2Endpoint6` | `AFKEPKextV2` | [`com.apple.driver.AppleAOP2`](../kexts/com.apple.driver.AppleAOP2.md) |
| `AOP2Endpoint7` | `AFKEPKextV2` | [`com.apple.driver.AppleAOP2`](../kexts/com.apple.driver.AppleAOP2.md) |
| `AOP2Endpoint8` | `AFKEPKextV2` | [`com.apple.driver.AppleAOP2`](../kexts/com.apple.driver.AppleAOP2.md) |
| `AOP2Endpoint9` | `AFKEPKextV2` | [`com.apple.driver.AppleAOP2`](../kexts/com.apple.driver.AppleAOP2.md) |
| `AOPEndpoint1` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `AOPEndpoint10` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `AOPEndpoint11` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `AOPEndpoint12` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `AOPEndpoint13` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `AOPEndpoint14` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `AOPEndpoint15` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `AOPEndpoint16` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `AOPEndpoint17` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `AOPEndpoint18` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `AOPEndpoint19` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `AOPEndpoint2` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `AOPEndpoint20` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `AOPEndpoint21` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `AOPEndpoint22` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `AOPEndpoint23` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `AOPEndpoint24` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `AOPEndpoint25` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `AOPEndpoint26` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `AOPEndpoint27` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `AOPEndpoint28` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `AOPEndpoint29` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `AOPEndpoint3` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `AOPEndpoint30` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `AOPEndpoint31` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `AOPEndpoint32` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `AOPEndpoint4` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `AOPEndpoint5` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `AOPEndpoint6` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `AOPEndpoint7` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `AOPEndpoint8` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `AOPEndpoint9` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `AOP_baseband` | `AppleSPUBasebandDriver` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `AOP_log` | `AppleSPULogFirmwareDriver` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `AOP_profile` | `AppleSPUProfileFirmwareDriver` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `AOP_spherecontrol` | `AppleSPUSphereDriver` | [`com.apple.driver.AppleSPUSphere`](../kexts/com.apple.driver.AppleSPUSphere.md) |
| `DCP0Endpoint1` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCP0Endpoint10` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCP0Endpoint11` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCP0Endpoint12` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCP0Endpoint13` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCP0Endpoint14` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCP0Endpoint15` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCP0Endpoint16` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCP0Endpoint17` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCP0Endpoint18` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCP0Endpoint19` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCP0Endpoint2` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCP0Endpoint20` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCP0Endpoint21` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCP0Endpoint22` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCP0Endpoint23` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCP0Endpoint3` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCP0Endpoint4` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCP0Endpoint5` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCP0Endpoint6` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCP0Endpoint7` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCP0Endpoint8` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCP0Endpoint9` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT0Endpoint1` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT0Endpoint10` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT0Endpoint11` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT0Endpoint12` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT0Endpoint13` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT0Endpoint14` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT0Endpoint15` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT0Endpoint16` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT0Endpoint17` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT0Endpoint18` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT0Endpoint19` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT0Endpoint2` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT0Endpoint20` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT0Endpoint21` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT0Endpoint22` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT0Endpoint23` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT0Endpoint3` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT0Endpoint4` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT0Endpoint5` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT0Endpoint6` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT0Endpoint7` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT0Endpoint8` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT0Endpoint9` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT1Endpoint1` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT1Endpoint10` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT1Endpoint11` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT1Endpoint12` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT1Endpoint13` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT1Endpoint14` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT1Endpoint15` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT1Endpoint16` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT1Endpoint17` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT1Endpoint18` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT1Endpoint19` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT1Endpoint2` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT1Endpoint20` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT1Endpoint21` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT1Endpoint22` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT1Endpoint23` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT1Endpoint3` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT1Endpoint4` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT1Endpoint5` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT1Endpoint6` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT1Endpoint7` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT1Endpoint8` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT1Endpoint9` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT2Endpoint1` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT2Endpoint10` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT2Endpoint11` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT2Endpoint12` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT2Endpoint13` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT2Endpoint14` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT2Endpoint15` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT2Endpoint16` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT2Endpoint17` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT2Endpoint18` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT2Endpoint19` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT2Endpoint2` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT2Endpoint20` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT2Endpoint21` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT2Endpoint22` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT2Endpoint23` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT2Endpoint3` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT2Endpoint4` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT2Endpoint5` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT2Endpoint6` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT2Endpoint7` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT2Endpoint8` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT2Endpoint9` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT3Endpoint1` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT3Endpoint10` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT3Endpoint11` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT3Endpoint12` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT3Endpoint13` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT3Endpoint14` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT3Endpoint15` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT3Endpoint16` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT3Endpoint17` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT3Endpoint18` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT3Endpoint19` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT3Endpoint2` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT3Endpoint20` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT3Endpoint21` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT3Endpoint22` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT3Endpoint23` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT3Endpoint3` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT3Endpoint4` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT3Endpoint5` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT3Endpoint6` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT3Endpoint7` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT3Endpoint8` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT3Endpoint9` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT4Endpoint1` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT4Endpoint10` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT4Endpoint11` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT4Endpoint12` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT4Endpoint13` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT4Endpoint14` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT4Endpoint15` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT4Endpoint16` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT4Endpoint17` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT4Endpoint18` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT4Endpoint19` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT4Endpoint2` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT4Endpoint20` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT4Endpoint21` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT4Endpoint22` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT4Endpoint23` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT4Endpoint3` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT4Endpoint4` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT4Endpoint5` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT4Endpoint6` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT4Endpoint7` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT4Endpoint8` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT4Endpoint9` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT5Endpoint1` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT5Endpoint10` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT5Endpoint11` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT5Endpoint12` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT5Endpoint13` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT5Endpoint14` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT5Endpoint15` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT5Endpoint16` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT5Endpoint17` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT5Endpoint18` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT5Endpoint19` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT5Endpoint2` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT5Endpoint20` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT5Endpoint21` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT5Endpoint22` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT5Endpoint23` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT5Endpoint3` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT5Endpoint4` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT5Endpoint5` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT5Endpoint6` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT5Endpoint7` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT5Endpoint8` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT5Endpoint9` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT6Endpoint1` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT6Endpoint10` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT6Endpoint11` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT6Endpoint12` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT6Endpoint13` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT6Endpoint14` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT6Endpoint15` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT6Endpoint16` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT6Endpoint17` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT6Endpoint18` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT6Endpoint19` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT6Endpoint2` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT6Endpoint20` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT6Endpoint21` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT6Endpoint22` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT6Endpoint23` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT6Endpoint3` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT6Endpoint4` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT6Endpoint5` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT6Endpoint6` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT6Endpoint7` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT6Endpoint8` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT6Endpoint9` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT7Endpoint1` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT7Endpoint10` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT7Endpoint11` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT7Endpoint12` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT7Endpoint13` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT7Endpoint14` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT7Endpoint15` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT7Endpoint16` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT7Endpoint17` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT7Endpoint18` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT7Endpoint19` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT7Endpoint2` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT7Endpoint20` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT7Endpoint21` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT7Endpoint22` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT7Endpoint23` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT7Endpoint3` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT7Endpoint4` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT7Endpoint5` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT7Endpoint6` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT7Endpoint7` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT7Endpoint8` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXT7Endpoint9` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXTEndpoint1` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXTEndpoint10` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXTEndpoint11` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXTEndpoint12` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXTEndpoint13` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXTEndpoint14` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXTEndpoint15` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXTEndpoint16` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXTEndpoint17` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXTEndpoint18` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXTEndpoint19` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXTEndpoint2` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXTEndpoint20` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXTEndpoint21` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXTEndpoint22` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXTEndpoint23` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXTEndpoint24` | `AppleDCPLinkServiceSoC` | [`com.apple.driver.AppleMobileDispH19P-DCP`](../kexts/com.apple.driver.AppleMobileDispH19P-DCP.md) |
| `DCPEXTEndpoint3` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXTEndpoint4` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXTEndpoint5` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXTEndpoint6` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXTEndpoint7` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXTEndpoint8` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEXTEndpoint9` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEndpoint1` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEndpoint10` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEndpoint11` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEndpoint12` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEndpoint13` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEndpoint14` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEndpoint15` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEndpoint16` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEndpoint17` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEndpoint18` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEndpoint19` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEndpoint2` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEndpoint20` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEndpoint21` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEndpoint22` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEndpoint23` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEndpoint24` | `AppleDCPLinkServiceSoC` | [`com.apple.driver.AppleMobileDispH19P-DCP`](../kexts/com.apple.driver.AppleMobileDispH19P-DCP.md) |
| `DCPEndpoint3` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEndpoint4` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEndpoint5` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEndpoint6` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEndpoint7` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEndpoint8` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPEndpoint9` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPSECEndpoint1` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPSECEndpoint10` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPSECEndpoint11` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPSECEndpoint12` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPSECEndpoint13` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPSECEndpoint14` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPSECEndpoint15` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPSECEndpoint16` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPSECEndpoint17` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPSECEndpoint18` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPSECEndpoint19` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPSECEndpoint2` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPSECEndpoint20` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPSECEndpoint21` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPSECEndpoint22` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPSECEndpoint23` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPSECEndpoint24` | `AppleDCPLinkServiceSoC` | [`com.apple.driver.AppleMobileDispH19P-DCP`](../kexts/com.apple.driver.AppleMobileDispH19P-DCP.md) |
| `DCPSECEndpoint3` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPSECEndpoint4` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPSECEndpoint5` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPSECEndpoint6` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPSECEndpoint7` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPSECEndpoint8` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `DCPSECEndpoint9` | `DCPEndpointV2` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `MTPEndpoint1` | `AppleGenericMultitouchDecider` | [`com.apple.driver.AppleGenericMultitouch`](../kexts/com.apple.driver.AppleGenericMultitouch.md) |
| `MTPEndpoint1` | `AppleHIDTransportDeviceMailbox` | [`com.apple.driver.AppleHIDTransportMailbox`](../kexts/com.apple.driver.AppleHIDTransportMailbox.md) |
| `PMP0Endpoint1` | `ApplePMPv2` | [`com.apple.driver.ApplePMP`](../kexts/com.apple.driver.ApplePMP.md) |
| `PMP1Endpoint1` | `ApplePMPv2` | [`com.apple.driver.ApplePMP`](../kexts/com.apple.driver.ApplePMP.md) |
| `PMPEndpoint1` | `ApplePMP` | [`com.apple.driver.ApplePMP`](../kexts/com.apple.driver.ApplePMP.md) |
| `PMPEndpoint1` | `ApplePMPv2` | [`com.apple.driver.ApplePMP`](../kexts/com.apple.driver.ApplePMP.md) |
| `PMPEndpoint2` | `ApplePMPThermal` | [`com.apple.driver.ApplePMP`](../kexts/com.apple.driver.ApplePMP.md) |
| `RTPEndpoint1` | `AppleHIDTransportDeviceMailbox` | [`com.apple.driver.AppleHIDTransportMailbox`](../kexts/com.apple.driver.AppleHIDTransportMailbox.md) |
| `SEPM` | `AppleSEPIntelIOP` | [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md) |
| `SIO1Endpoint1` | `AppleSmartIO` | [`com.apple.driver.AppleSmartIO2`](../kexts/com.apple.driver.AppleSmartIO2.md) |
| `SIOEndpoint1` | `AppleSmartIO` | [`com.apple.driver.AppleSmartIO2`](../kexts/com.apple.driver.AppleSmartIO2.md) |
| `SMCEndpoint1` | `AppleSMCKeysEndpoint` | [`com.apple.driver.AppleSMC`](../kexts/com.apple.driver.AppleSMC.md) |
| `SPU2Endpoint1` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `SPU2Endpoint10` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `SPU2Endpoint11` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `SPU2Endpoint12` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `SPU2Endpoint13` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `SPU2Endpoint14` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `SPU2Endpoint15` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `SPU2Endpoint16` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `SPU2Endpoint2` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `SPU2Endpoint3` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `SPU2Endpoint4` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `SPU2Endpoint5` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `SPU2Endpoint6` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `SPU2Endpoint7` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `SPU2Endpoint8` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `SPU2Endpoint9` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `SPUEndpoint1` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `SPUEndpoint10` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `SPUEndpoint11` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `SPUEndpoint12` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `SPUEndpoint13` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `SPUEndpoint14` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `SPUEndpoint15` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `SPUEndpoint16` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `SPUEndpoint2` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `SPUEndpoint3` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `SPUEndpoint4` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `SPUEndpoint5` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `SPUEndpoint6` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `SPUEndpoint7` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `SPUEndpoint8` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `SPUEndpoint9` | `AppleSPU` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `accbuck,fan53740` | `AppleFAN53740` | [`com.apple.driver.AppleFAN53740`](../kexts/com.apple.driver.AppleFAN53740.md) |
| `acio` | `AppleThunderboltHALType5` | [`com.apple.driver.AppleThunderboltNHI`](../kexts/com.apple.driver.AppleThunderboltNHI.md) |
| `acio,v2` | `AppleThunderboltHALType7` | [`com.apple.driver.AppleThunderboltNHI`](../kexts/com.apple.driver.AppleThunderboltNHI.md) |
| `admac-base-s-proxy` | `DMAChannelProxy` | [`com.apple.driver.DMAChannelProxy`](../kexts/com.apple.driver.DMAChannelProxy.md) |
| `admac-leap-s-proxy` | `DMAChannelProxy` | [`com.apple.driver.DMAChannelProxy`](../kexts/com.apple.driver.DMAChannelProxy.md) |
| `afk-io-service-client` | `AFKIOServiceClient` | [`com.apple.driver.AppleFirmwareKit`](../kexts/com.apple.driver.AppleFirmwareKit.md) |
| `afk-shmem-registry` | `AFKSharedMemoryMapServer` | [`com.apple.driver.AppleFirmwareKit`](../kexts/com.apple.driver.AppleFirmwareKit.md) |
| `afk-shmem-test-registry` | `AFKSharedMemoryMapServer` | [`com.apple.driver.AppleFirmwareKit`](../kexts/com.apple.driver.AppleFirmwareKit.md) |
| `afk-smc-client` | `AFKRemoteSMCClient` | [`com.apple.driver.AppleFirmwareKit`](../kexts/com.apple.driver.AppleFirmwareKit.md) |
| `aht-hibernator` | `AppleHIDTransportHibernator` | [`com.apple.driver.AppleHIDTransportFIFO`](../kexts/com.apple.driver.AppleHIDTransportFIFO.md) |
| `als,ct709` | `AppleTCS3490` | [`com.apple.driver.AppleALSColorSensor`](../kexts/com.apple.driver.AppleALSColorSensor.md) |
| `als,ct711` | `AppleCT711` | [`com.apple.driver.AppleALSColorSensor`](../kexts/com.apple.driver.AppleALSColorSensor.md) |
| `als,ct819` | `AppleCT819` | [`com.apple.driver.AppleEmbeddedLightSensor`](../kexts/com.apple.driver.AppleEmbeddedLightSensor.md) |
| `als,ct821` | `AppleCT821` | [`com.apple.driver.AppleEmbeddedLightSensor`](../kexts/com.apple.driver.AppleEmbeddedLightSensor.md) |
| `als,isl29023` | `AppleISL29023` | [`com.apple.driver.AppleEmbeddedLightSensor`](../kexts/com.apple.driver.AppleEmbeddedLightSensor.md) |
| `als,tcs3490` | `AppleCT711` | [`com.apple.driver.AppleALSColorSensor`](../kexts/com.apple.driver.AppleALSColorSensor.md) |
| `als,tcs3490` | `AppleTCS3490` | [`com.apple.driver.AppleALSColorSensor`](../kexts/com.apple.driver.AppleALSColorSensor.md) |
| `als,tsl2561` | `AppleTSL2561` | [`com.apple.driver.AppleEmbeddedLightSensor`](../kexts/com.apple.driver.AppleEmbeddedLightSensor.md) |
| `als,tsl2581` | `AppleTSL2581` | [`com.apple.driver.AppleEmbeddedLightSensor`](../kexts/com.apple.driver.AppleEmbeddedLightSensor.md) |
| `amctempsensor,s5l8960x` | `AMCTempSensor` | [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md) |
| `ane,t8020` | `H11ANEIn` | [`com.apple.driver.AppleH16ANEInterface`](../kexts/com.apple.driver.AppleH16ANEInterface.md) |
| `ane,t8132exclave` | `H11ANEIn` | [`com.apple.driver.AppleH16ANEInterface`](../kexts/com.apple.driver.AppleH16ANEInterface.md) |
| `aod` | `AppleAstrisGpioProbe` | [`com.apple.driver.AppleAstrisGpioProbe`](../kexts/com.apple.driver.AppleAstrisGpioProbe.md) |
| `aop,vd5b704` | `ApplePhotonDetector` | [`com.apple.driver.ApplePhotonDetector`](../kexts/com.apple.driver.ApplePhotonDetector.md) |
| `aop-haptics-audio` | `AppleSPUHapticsAudioDriver` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `aop-haptics-manager` | `AppleSPUHapticsManagerDriver` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `aop-marconi-bt-control` | `AppleSPUMarconiControl` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `aop2.network.aop2apkernel` | `RTKitNetKernelSharedMemory` | [`com.apple.iokit.RTKitNet`](../kexts/com.apple.iokit.RTKitNet.md) |
| `aop2.system-iopm-aop2.system-iopm.ap.client-rev` | `AppleAOP2IOPMService` | [`com.apple.driver.AppleAOP2`](../kexts/com.apple.driver.AppleAOP2.md) |
| `aop2.system-iopm-aop2.system-iopm.ap.client-rev` | `AppleAOP2KextTightbeamEndpoint` | [`com.apple.driver.AppleAOP2`](../kexts/com.apple.driver.AppleAOP2.md) |
| `ap_echo-test` | `AFKEchoTestEPIC` | [`com.apple.driver.AppleFirmwareKit`](../kexts/com.apple.driver.AppleFirmwareKit.md) |
| `apple-processor-trace,bring-up` | `AppleProcessorTraceBringUp` | [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md) |
| `apple-processor-trace,t6000` | `AppleProcessorTraceT6000` | [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md) |
| `apple-processor-trace,t6020` | `AppleProcessorTraceT6020` | [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md) |
| `apple-processor-trace,t6030` | `AppleProcessorTraceT6030` | [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md) |
| `apple-processor-trace,t6031` | `AppleProcessorTraceT6031` | [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md) |
| `apple-processor-trace,t6040` | `AppleProcessorTraceT6040` | [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md) |
| `apple-processor-trace,t6040` | `AppleProcessorTraceT6040` | [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md) |
| `apple-processor-trace,t6050` | `AppleProcessorTraceT6050` | [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md) |
| `apple-processor-trace,t8101` | `AppleProcessorTraceT8101` | [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md) |
| `apple-processor-trace,t8103` | `AppleProcessorTraceT8103` | [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md) |
| `apple-processor-trace,t8110` | `AppleProcessorTraceT8110` | [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md) |
| `apple-processor-trace,t8112` | `AppleProcessorTraceT8112` | [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md) |
| `apple-processor-trace,t8120` | `AppleProcessorTraceT8120` | [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md) |
| `apple-processor-trace,t8122` | `AppleProcessorTraceT8122` | [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md) |
| `apple-processor-trace,t8130` | `AppleProcessorTraceT8130` | [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md) |
| `apple-processor-trace,t8132` | `AppleProcessorTraceT8132` | [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md) |
| `apple-processor-trace,t8140` | `AppleProcessorTraceT8140` | [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md) |
| `apple-processor-trace,t8142` | `AppleProcessorTraceT8142` | [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md) |
| `apple-processor-trace,t8150` | `AppleProcessorTraceT8150` | [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md) |
| `apple-processor-trace,t8152` | `AppleProcessorTraceT8152` | [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md) |
| `apple-processor-trace,t8310` | `AppleProcessorTraceT8310` | [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md) |
| `apple-processor-trace,t8320` | `AppleProcessorTraceT8320` | [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md) |
| `apr,a0` | `AppleProResHW` | [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md) |
| `apr,a1` | `AppleProResHW` | [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md) |
| `apr,a2` | `AppleProResHW` | [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md) |
| `apr,b0` | `AppleProResHW` | [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md) |
| `apr,c0` | `AppleProResHW` | [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md) |
| `apr,d0` | `AppleProResHW` | [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md) |
| `apr,d1` | `AppleProResHW` | [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md) |
| `apr,d2` | `AppleProResHW` | [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md) |
| `apr,e0` | `AppleProResHW` | [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md) |
| `apr,f0` | `AppleProResHW` | [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md) |
| `apr,g0` | `AppleProResHW` | [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md) |
| `apr,h0` | `AppleProResHW` | [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md) |
| `apr,h1` | `AppleProResHW` | [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md) |
| `apr,h2` | `AppleProResHW` | [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md) |
| `apr,i0` | `AppleProResHW` | [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md) |
| `apr,j0` | `AppleProResHW` | [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md) |
| `apr,j1` | `AppleProResHW` | [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md) |
| `apr,k0` | `AppleProResHW` | [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md) |
| `apr,l0` | `AppleProResHW` | [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md) |
| `apr,m0` | `AppleProResHW` | [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md) |
| `apr,n0` | `AppleProResHW` | [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md) |
| `apr,n1` | `AppleProResHW` | [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md) |
| `apr,n2` | `AppleProResHW` | [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md) |
| `apr,o0` | `AppleProResHW` | [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md) |
| `apr,p0` | `AppleProResHW` | [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md) |
| `apr,q0` | `AppleProResHW` | [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md) |
| `apr,r0` | `AppleProResHW` | [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md) |
| `apr,r1` | `AppleProResHW` | [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md) |
| `apr,r2` | `AppleProResHW` | [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md) |
| `apr,s0` | `AppleProResHW` | [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md) |
| `arc-eeprom-i2c` | `AppleHapticsSupportArcEEPROM` | [`com.apple.driver.AppleHapticsSupportNVM`](../kexts/com.apple.driver.AppleHapticsSupportNVM.md) |
| `area51` | `Area51AuthSMCRelayInterface` | [`com.apple.driver.AppleAuthCP`](../kexts/com.apple.driver.AppleAuthCP.md) |
| `atc-dpxbar,t600x` | `AppleT600XATCDPXBAR` | [`com.apple.driver.AppleDisplayCrossbar`](../kexts/com.apple.driver.AppleDisplayCrossbar.md) |
| `atc-dpxbar,t604x` | `AppleT604XATCDPXBAR` | [`com.apple.driver.AppleDisplayCrossbar`](../kexts/com.apple.driver.AppleDisplayCrossbar.md) |
| `atc-dpxbar,t8103` | `AppleT8103ATCDPXBAR` | [`com.apple.driver.AppleDisplayCrossbar`](../kexts/com.apple.driver.AppleDisplayCrossbar.md) |
| `atc-dpxbar,t8112` | `AppleT8112ATCDPXBAR` | [`com.apple.driver.AppleDisplayCrossbar`](../kexts/com.apple.driver.AppleDisplayCrossbar.md) |
| `atc-dpxbar,t8142` | `AppleT8142ATCDPXBAR` | [`com.apple.driver.AppleDisplayCrossbar`](../kexts/com.apple.driver.AppleDisplayCrossbar.md) |
| `atc-phy,ausbc` | `AppleTypeCPhyAUSBC` | [`com.apple.driver.AppleTypeCPhyAUSBC`](../kexts/com.apple.driver.AppleTypeCPhyAUSBC.md) |
| `atc-phy,t8103` | `AppleT8103TypeCPhy` | [`com.apple.driver.AppleT8103TypeCPhy`](../kexts/com.apple.driver.AppleT8103TypeCPhy.md) |
| `audio-amp` | `AppleAOPAudioAmpManagerDevice` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) |
| `audio-aop-bhap` | `AppleAOPAudioButtonHapticDevice` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) |
| `audio-aop-buttonout` | `AppleAOPAudioButtonOutputDevice` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) |
| `audio-aop-edt-config` | `AppleAOPAudioDevice` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) |
| `audio-aop-hall` | `AppleAOPAudioHallDevice` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) |
| `audio-aop-haptic-leap` | `AppleAOPAudioHapticLEAP` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) |
| `audio-aop-hapticmgr` | `AppleAOPAudioLEAPClientManager` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) |
| `audio-aop-hawking` | `AppleAOPAudioClientManager` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) |
| `audio-aop-ldcm` | `AppleAOPAudioClientManager` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) |
| `audio-aop-leap` | `AppleAOPAudioLEAP` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) |
| `audio-aop-lp-mic-in` | `AppleAOPAudioLPMicInDevice` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) |
| `audio-aop-mca2-pmgr` | `AppleAOPAudioClientManager` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) |
| `audio-aop-mca3-pmgr` | `AppleAOPAudioClientManager` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) |
| `audio-aop-mca4-pmgr` | `AppleAOPAudioClientManager` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) |
| `audio-aop-mca5-pmgr` | `AppleAOPAudioClientManager` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) |
| `audio-aop-pcmaudiomgr` | `AppleAOPAudioPCMAssetManagerDevice` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) |
| `audio-aop-pdm2` | `AppleAOPAudioPDM2Device` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) |
| `audio-aop-speaker-manager` | `AppleAOPAudioClientManager` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) |
| `audio-aop-spkrmgr` | `AppleAOPAudioSpeakerClientManager` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) |
| `audio-aud-mca-baseband` | `AppleAOPAudioClientManager` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) |
| `audio-aud-mca-loopback` | `AppleAOPAudioClientManager` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) |
| `audio-bhap` | `AppleAOPAudioButtonHapticDevice` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) |
| `audio-buttonout` | `AppleAOPAudioButtonOutputDevice` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) |
| `audio-control,iop-embeddedaudio` | `IOPEmbeddedAudio` | [`com.apple.driver.IOPEmbeddedAudio`](../kexts/com.apple.driver.IOPEmbeddedAudio.md) |
| `audio-data,actuator` | `AppleActuatorSecondaryAudio` | [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md) |
| `audio-data,audio-aop-mca-loopback` | `AppleSecondaryAudio` | [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md) |
| `audio-data,audio-tap` | `AppleSecondaryAudio` | [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md) |
| `audio-data,baseband` | `AppleSecondaryAudio` | [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md) |
| `audio-data,baseband-voice` | `AppleSecondaryAudio` | [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md) |
| `audio-data,bluetooth-voice` | `AppleSecondaryAudio` | [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md) |
| `audio-data,cs42l83-input` | `AppleSecondaryAudio` | [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md) |
| `audio-data,cs42l84-input` | `AppleSecondaryAudio` | [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md) |
| `audio-data,dsp-debug1` | `AppleSecondaryAudio` | [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md) |
| `audio-data,dsp-debug2` | `AppleSecondaryAudio` | [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md) |
| `audio-data,ext-haptic-debug` | `AppleSecondaryAudio` | [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md) |
| `audio-data,halogen` | `AppleSecondaryAudio` | [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md) |
| `audio-data,haptic-debug` | `AppleSecondaryAudio` | [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md) |
| `audio-data,haptics-external` | `AppleHapticsExternalSecondaryAudio` | [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md) |
| `audio-data,hawking` | `AppleSecondaryAudio` | [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md) |
| `audio-data,hdmi` | `AppleIISAudioLinkDelegate` | [`com.apple.iokit.IOAVFamily`](../kexts/com.apple.iokit.IOAVFamily.md) |
| `audio-data,maggie-debug` | `AppleSecondaryAudio` | [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md) |
| `audio-data,mck-only` | `AppleMCKAudio` | [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md) |
| `audio-data,mikeybus-secondary` | `AppleSecondaryAudio` | [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md) |
| `audio-data,reference` | `AppleSecondaryAudio` | [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md) |
| `audio-data,secondary` | `AppleSecondaryAudio` | [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md) |
| `audio-data,virtual-secondary` | `AppleSecondaryAudio` | [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md) |
| `audio-data,voice` | `AppleSecondaryAudio` | [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md) |
| `audio-dma-channel,v5p0` | `ADMAChannelInterface` | [`com.apple.driver.AudioDMAController-Gen5p0`](../kexts/com.apple.driver.AudioDMAController-Gen5p0.md) |
| `audio-fwdt-asset-mgr` | `AppleAOPAudioFWdtAssetManagerDevice` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) |
| `audio-hall` | `AppleAOPAudioHallDevice` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) |
| `audio-hapticmgr` | `AppleAOPAudioLEAPClientManager` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) |
| `audio-leap` | `AppleAOPAudioLEAP` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) |
| `audio-leap-mca-loopback` | `AppleAOPAudioClientManager` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) |
| `audio-lp-mic-in` | `AppleAOPAudioLPMicInDevice` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) |
| `audio-mca0` | `AppleAOPAudioMCA2Device` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) |
| `audio-mca1` | `AppleAOPAudioMCA2Device` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) |
| `audio-pcmaudiomgr` | `AppleAOPAudioPCMAssetManagerDevice` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) |
| `audio-pdm2` | `AppleAOPAudioPDM2Device` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) |
| `audio-spkrmgr` | `AppleAOPAudioSpeakerClientManager` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) |
| `authcp,2c` | `AppleAuthCPI2C` | [`com.apple.driver.AppleAuthCP`](../kexts/com.apple.driver.AppleAuthCP.md) |
| `avd,s5l8920x` | `AppleAVD` | [`com.apple.driver.AppleAVD`](../kexts/com.apple.driver.AppleAVD.md) |
| `avd,t8020` | `AppleAVD` | [`com.apple.driver.AppleAVD`](../kexts/com.apple.driver.AppleAVD.md) |
| `avd,t8030` | `AppleAVD` | [`com.apple.driver.AppleAVD`](../kexts/com.apple.driver.AppleAVD.md) |
| `avd,t8101` | `AppleAVD` | [`com.apple.driver.AppleAVD`](../kexts/com.apple.driver.AppleAVD.md) |
| `backlight,pwm` | `AppleARMPWMBacklight` | [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md) |
| `baseband-pcie` | `AppleConvergedPCIICEBB` | [`com.apple.driver.AppleConvergedIPCBBControl`](../kexts/com.apple.driver.AppleConvergedIPCBBControl.md) |
| `baseband-pcie-pandia` | `AppleConvergedPCILedaBB` | [`com.apple.driver.AppleConvergedIPCBBControl`](../kexts/com.apple.driver.AppleConvergedIPCBBControl.md) |
| `batt-adc` | `AppleSPUBattChannelDriver` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `bora-dcplEndpoint1` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcplEndpoint10` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcplEndpoint11` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcplEndpoint12` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcplEndpoint13` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcplEndpoint14` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcplEndpoint15` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcplEndpoint16` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcplEndpoint17` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcplEndpoint18` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcplEndpoint19` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcplEndpoint2` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcplEndpoint20` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcplEndpoint21` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcplEndpoint22` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcplEndpoint23` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcplEndpoint3` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcplEndpoint4` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcplEndpoint5` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcplEndpoint6` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcplEndpoint7` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcplEndpoint8` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcplEndpoint9` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcprEndpoint1` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcprEndpoint10` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcprEndpoint11` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcprEndpoint12` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcprEndpoint13` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcprEndpoint14` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcprEndpoint15` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcprEndpoint16` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcprEndpoint17` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcprEndpoint18` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcprEndpoint19` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcprEndpoint2` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcprEndpoint20` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcprEndpoint21` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcprEndpoint22` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcprEndpoint23` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcprEndpoint3` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcprEndpoint4` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcprEndpoint5` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcprEndpoint6` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcprEndpoint7` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcprEndpoint8` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcprEndpoint9` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcpsEndpoint1` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcpsEndpoint10` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcpsEndpoint11` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcpsEndpoint12` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcpsEndpoint13` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcpsEndpoint14` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcpsEndpoint15` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcpsEndpoint16` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcpsEndpoint17` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcpsEndpoint18` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcpsEndpoint19` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcpsEndpoint2` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcpsEndpoint20` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcpsEndpoint21` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcpsEndpoint22` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcpsEndpoint23` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcpsEndpoint3` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcpsEndpoint4` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcpsEndpoint5` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcpsEndpoint6` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcpsEndpoint7` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcpsEndpoint8` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-dcpsEndpoint9` | `AFKACIPCEndpoint` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `bora-uart` | `AppleSPUBoraUartDriver` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `btm,bpic` | `AppleBPIC` | [`com.apple.driver.ApplePhoneBTM`](../kexts/com.apple.driver.ApplePhoneBTM.md) |
| `btm,pmgr` | `AppleBTM` | [`com.apple.driver.ApplePhoneBTM`](../kexts/com.apple.driver.ApplePhoneBTM.md) |
| `cec-controller` | `DCPAVCECController` | [`com.apple.driver.DCPAVFamilyProxy`](../kexts/com.apple.driver.DCPAVFamilyProxy.md) |
| `charger` | `AppleARMPMUCharger` | [`com.apple.driver.AppleARMPMU`](../kexts/com.apple.driver.AppleARMPMU.md) |
| `charger,passthrough` | `AppleARMPassthroughPowerSource` | [`com.apple.driver.AppleARMPMU`](../kexts/com.apple.driver.AppleARMPMU.md) |
| `com.apple.aop2.afksmplkext-0-com.apple.aop2.afksmplkext-0.ap.client-fwd` | `AFKTightbeamEndpoint` | [`com.apple.driver.AppleT8160PCIe`](../kexts/com.apple.driver.AppleT8160PCIe.md) |
| `com.apple.aop2.afksmplkext-1-com.apple.aop2.afksmplkext-1.ap.client-fwd` | `AFKTightbeamEndpoint` | [`com.apple.driver.AppleT8160PCIe`](../kexts/com.apple.driver.AppleT8160PCIe.md) |
| `com.apple.aop2.ulpn.xnu-com.apple.aop2.ulpn.xnu.ap.client-fwd` | `RTKitNetKernelPacketCapture` | [`com.apple.iokit.RTKitNet`](../kexts/com.apple.iokit.RTKitNet.md) |
| `com.apple.aop2.ulpn.xnu-com.apple.aop2.ulpn.xnu.ap.client-rev` | `RTKitNetKernelPacketCapture` | [`com.apple.iokit.RTKitNet`](../kexts/com.apple.iokit.RTKitNet.md) |
| `cpu` | `AppleARMCPU` | [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md) |
| `cpu-error-handler,everest` | `AppleARM64ErrorHandler` | [`com.apple.driver.AppleEverestErrorHandler`](../kexts/com.apple.driver.AppleEverestErrorHandler.md) |
| `dapf,t8020` | `AppleDAPF` | [`com.apple.driver.AppleDAPF`](../kexts/com.apple.driver.AppleDAPF.md) |
| `dcp-mipi-power-controller` | `AppleDCPMIPIRemotePowerController` | [`com.apple.iokit.IOMIPIFamily`](../kexts/com.apple.iokit.IOMIPIFamily.md) |
| `dcp0-sac-controller` | `DCPAVSACController` | [`com.apple.driver.DCPAVFamilyProxy`](../kexts/com.apple.driver.DCPAVFamilyProxy.md) |
| `dcp1-sac-controller` | `DCPAVSACController` | [`com.apple.driver.DCPAVFamilyProxy`](../kexts/com.apple.driver.DCPAVFamilyProxy.md) |
| `dietempctl,s5l8960x` | `AppleDieTempController` | [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md) |
| `dietempctl,s8000` | `AppleDieTempController` | [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md) |
| `dietempctl,t7000` | `AppleDieTempController` | [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md) |
| `dietempctl,t7001` | `AppleDieTempController` | [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md) |
| `dietempctl,t8004` | `AppleDieTempController` | [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md) |
| `dietempctl,t8006` | `AppleDieTempController` | [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md) |
| `dietempctl,t8010` | `AppleDieTempController` | [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md) |
| `dietempctl,t8012` | `AppleDieTempController` | [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md) |
| `dietempctl,t8015` | `AppleDieTempController` | [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md) |
| `dietempctl,t8020` | `AppleDieTempController` | [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md) |
| `dietempctl,t8027` | `AppleDieTempController` | [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md) |
| `dietempctl,t8030` | `AppleDieTempController` | [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md) |
| `disp-adc` | `AppleSPUDispADCDriver` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `display-crossbar,t600x` | `AppleT600xDisplayCrossbar` | [`com.apple.driver.AppleDisplayCrossbar`](../kexts/com.apple.driver.AppleDisplayCrossbar.md) |
| `display-crossbar,t602x` | `AppleT602XDisplayCrossbar` | [`com.apple.driver.AppleDisplayCrossbar`](../kexts/com.apple.driver.AppleDisplayCrossbar.md) |
| `display-crossbar,t603x` | `AppleT603XDisplayCrossbar` | [`com.apple.driver.AppleDisplayCrossbar`](../kexts/com.apple.driver.AppleDisplayCrossbar.md) |
| `display-crossbar,t6050` | `AppleT6050DisplayCrossbar` | [`com.apple.driver.AppleDisplayCrossbar`](../kexts/com.apple.driver.AppleDisplayCrossbar.md) |
| `display-crossbar,t8132` | `AppleT8132DisplayCrossbar` | [`com.apple.driver.AppleDisplayCrossbar`](../kexts/com.apple.driver.AppleDisplayCrossbar.md) |
| `display-crossbar,t8142` | `AppleT8142DisplayCrossbar` | [`com.apple.driver.AppleDisplayCrossbar`](../kexts/com.apple.driver.AppleDisplayCrossbar.md) |
| `dock,30pin` | `IOAccessoryDock30PinBuiltIn` | [`com.apple.iokit.IOAccessoryManager`](../kexts/com.apple.iokit.IOAccessoryManager.md) |
| `dock,smc-usb-ufp` | `AppleSMCDockUSB_UFP` | [`com.apple.driver.AppleSMC`](../kexts/com.apple.driver.AppleSMC.md) |
| `dock,usb-ufp` | `IOAccessoryDockUSB_UFP` | [`com.apple.iokit.IOAccessoryManager`](../kexts/com.apple.iokit.IOAccessoryManager.md) |
| `dockchannel,t8002` | `AppleDockChannel` | [`com.apple.driver.AppleDockChannel`](../kexts/com.apple.driver.AppleDockChannel.md) |
| `dp-audio` | `DCPAVAudioDMADelegate` | [`com.apple.driver.DCPAVFamilyProxy`](../kexts/com.apple.driver.DCPAVFamilyProxy.md) |
| `dp-audio2` | `DCPAVAudioDMADelegate` | [`com.apple.driver.DCPAVFamilyProxy`](../kexts/com.apple.driver.DCPAVFamilyProxy.md) |
| `dp-audio3` | `DCPAVAudioDMADelegate` | [`com.apple.driver.DCPAVFamilyProxy`](../kexts/com.apple.driver.DCPAVFamilyProxy.md) |
| `dp-audio4` | `DCPAVAudioDMADelegate` | [`com.apple.driver.DCPAVFamilyProxy`](../kexts/com.apple.driver.DCPAVFamilyProxy.md) |
| `dp-audio5` | `DCPAVAudioDMADelegate` | [`com.apple.driver.DCPAVFamilyProxy`](../kexts/com.apple.driver.DCPAVFamilyProxy.md) |
| `dp-audio6` | `DCPAVAudioDMADelegate` | [`com.apple.driver.DCPAVFamilyProxy`](../kexts/com.apple.driver.DCPAVFamilyProxy.md) |
| `dp-audio7` | `DCPAVAudioDMADelegate` | [`com.apple.driver.DCPAVFamilyProxy`](../kexts/com.apple.driver.DCPAVFamilyProxy.md) |
| `dp-audio8` | `DCPAVAudioDMADelegate` | [`com.apple.driver.DCPAVFamilyProxy`](../kexts/com.apple.driver.DCPAVFamilyProxy.md) |
| `dp-audio9` | `DCPAVAudioDMADelegate` | [`com.apple.driver.DCPAVFamilyProxy`](../kexts/com.apple.driver.DCPAVFamilyProxy.md) |
| `dptx-phy,t602x` | `AppleT602XDPTXPort` | [`com.apple.driver.AppleDisplayCrossbar`](../kexts/com.apple.driver.AppleDisplayCrossbar.md) |
| `dptx-phy,t6050` | `AppleT6050DPTXPort` | [`com.apple.driver.AppleDisplayCrossbar`](../kexts/com.apple.driver.AppleDisplayCrossbar.md) |
| `dptx-phy,t8112` | `AppleT8112DPTXPort` | [`com.apple.driver.AppleDisplayCrossbar`](../kexts/com.apple.driver.AppleDisplayCrossbar.md) |
| `dptx-phy,t8122` | `AppleT8122DPTXPort` | [`com.apple.driver.AppleDisplayCrossbar`](../kexts/com.apple.driver.AppleDisplayCrossbar.md) |
| `dptx-phy,t8132` | `AppleT8132DPTXPort` | [`com.apple.driver.AppleDisplayCrossbar`](../kexts/com.apple.driver.AppleDisplayCrossbar.md) |
| `dptx-phy,t8152` | `AppleT8152DPTXPort` | [`com.apple.driver.AppleDisplayCrossbar`](../kexts/com.apple.driver.AppleDisplayCrossbar.md) |
| `dwi,s8000` | `AppleS8000DWI` | [`com.apple.driver.AppleS8000DWI`](../kexts/com.apple.driver.AppleS8000DWI.md) |
| `gen-aft` | `AppleARMFabricTrace` | [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md) |
| `gen-mt-decider` | `AppleGenericMultitouchDecider` | [`com.apple.driver.AppleGenericMultitouch`](../kexts/com.apple.driver.AppleGenericMultitouch.md) |
| `gen-mt-decider` | `AppleGenericMultitouchDecider` | [`com.apple.driver.AppleGenericMultitouch`](../kexts/com.apple.driver.AppleGenericMultitouch.md) |
| `gpio,s5l8960x` | `AppleS5L8960XGPIOIC` | [`com.apple.driver.AppleGPIOICController`](../kexts/com.apple.driver.AppleGPIOICController.md) |
| `gpio,t8006` | `AppleT8006GPIOIC` | [`com.apple.driver.AppleGPIOICController`](../kexts/com.apple.driver.AppleGPIOICController.md) |
| `gps,bcm4750` | `AppleBCM4750` | [`com.apple.driver.AppleEmbeddedGPS`](../kexts/com.apple.driver.AppleEmbeddedGPS.md) |
| `gps,bcm4750` | `AppleEmbeddedGPSControl` | [`com.apple.driver.AppleEmbeddedGPS`](../kexts/com.apple.driver.AppleEmbeddedGPS.md) |
| `gps,bcm4773` | `AppleEmbeddedGPSControl` | [`com.apple.driver.AppleEmbeddedGPS`](../kexts/com.apple.driver.AppleEmbeddedGPS.md) |
| `gpu,t8015` | `AGXAcceleratorG19P` | [`com.apple.AGXG19P`](../kexts/com.apple.AGXG19P.md) |
| `gpu,t8027` | `AGXAcceleratorG19P` | [`com.apple.AGXG19P`](../kexts/com.apple.AGXG19P.md) |
| `gpu,t8030` | `AGXAcceleratorG19P` | [`com.apple.AGXG19P`](../kexts/com.apple.AGXG19P.md) |
| `gpu,t8103` | `AGXAcceleratorG19P` | [`com.apple.AGXG19P`](../kexts/com.apple.AGXG19P.md) |
| `gpu,t8122` | `AGXAcceleratorG19P` | [`com.apple.AGXG19P`](../kexts/com.apple.AGXG19P.md) |
| `hid-transport,dc` | `AppleHIDTransportDeviceFIFO` | [`com.apple.driver.AppleHIDTransportFIFO`](../kexts/com.apple.driver.AppleHIDTransportFIFO.md) |
| `hid-transport,dummy` | `AppleHIDTransportDeviceDummy` | [`com.apple.driver.AppleHIDTransport`](../kexts/com.apple.driver.AppleHIDTransport.md) |
| `hid-transport,k1` | `AppleHIDTransportDeviceSPI` | [`com.apple.driver.AppleHIDTransportSPI`](../kexts/com.apple.driver.AppleHIDTransportSPI.md) |
| `hid-transport,spi` | `AppleHIDTransportDeviceSPI` | [`com.apple.driver.AppleHIDTransportSPI`](../kexts/com.apple.driver.AppleHIDTransportSPI.md) |
| `hpm-aid-controller` | `AppleHPMAIDType1` | [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md) |
| `hpmSingleTransport` | `AppleTCControllerSingleTransport` | [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md) |
| `i2c,vd5b704` | `ApplePhotonDetector` | [`com.apple.driver.ApplePhotonDetector`](../kexts/com.apple.driver.ApplePhotonDetector.md) |
| `iap,uart` | `IOAccessoryPortSerialSync` | [`com.apple.iokit.IOAccessoryManager`](../kexts/com.apple.iokit.IOAccessoryManager.md) |
| `iop-adma-stream,aspen` | `AppleIOPADMAStream` | [`com.apple.driver.AppleIOPADMAStream`](../kexts/com.apple.driver.AppleIOPADMAStream.md) |
| `iop-adma-stream,sense` | `AppleIOPADMAStream` | [`com.apple.driver.AppleIOPADMAStream`](../kexts/com.apple.driver.AppleIOPADMAStream.md) |
| `iop-audio,io-buffer-device` | `IOPAudioIOBufferDevice` | [`com.apple.driver.IOPAudioIOBufferDevice`](../kexts/com.apple.driver.IOPAudioIOBufferDevice.md) |
| `iop-audio,leap-control-device` | `IOPAudioLEAPControlDevice` | [`com.apple.driver.IOPAudioLEAPControlDevice`](../kexts/com.apple.driver.IOPAudioLEAPControlDevice.md) |
| `iop-audio,vt-device` | `IOPAudioVoiceTriggerDevice` | [`com.apple.driver.IOPAudioVoiceTriggerDevice`](../kexts/com.apple.driver.IOPAudioVoiceTriggerDevice.md) |
| `iop-nub,rtbuddy` | `RTBuddy64` | [`com.apple.driver.RTBuddy`](../kexts/com.apple.driver.RTBuddy.md) |
| `iop-nub,rtbuddy-arg` | `RTBuddyARG` | [`com.apple.driver.RTBuddy`](../kexts/com.apple.driver.RTBuddy.md) |
| `iop-nub,rtbuddy-route-only` | `RTBuddyRouteOnly` | [`com.apple.driver.RTBuddy`](../kexts/com.apple.driver.RTBuddy.md) |
| `iop-spu-nub` | `AppleLVBOOST` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `iop-spu-nub` | `AppleSPUTimesyncV1` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `isp,isp-generic-1` | `AppleCamera` | [`com.apple.driver.AppleCamera`](../kexts/com.apple.driver.AppleCamera.md) |
| `juliet` | `AppleSPUGpioUnplugDriver` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `lanai_l` | `AppleSPUGpioUnplugDriver` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `lanai_r` | `AppleSPUGpioUnplugDriver` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `mipi-dsim-1,synopsys` | `AppleSynopsysMIPIDSIController` | [`com.apple.driver.AppleSynopsysMIPIDSI`](../kexts/com.apple.driver.AppleSynopsysMIPIDSI.md) |
| `msg-svc` | `AppleMSGKextEPIC` | [`com.apple.driver.AppleMSG`](../kexts/com.apple.driver.AppleMSG.md) |
| `mtrtempsensor,t8020` | `AppleT8020MTRTempSensor` | [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md) |
| `nco,s5l8960x` | `AppleS5L8960XNCO` | [`com.apple.driver.AppleS5L8960XNCO`](../kexts/com.apple.driver.AppleS5L8960XNCO.md) |
| `nor-flash,cfi` | `AppleARMCFIFlashController` | [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md) |
| `nor-flash,spi` | `AppleARMSPIFlashController` | [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md) |
| `nvram,chrp` | `AppleARMNORNVRAM` | [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md) |
| `nvram,nor` | `AppleARMNORNVRAM` | [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md) |
| `opal` | `AppleSPUControl` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `paniclog` | `AppleARMNORPanicLog` | [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md) |
| `parrot-i2c,a0` | `AppleParrot` | [`com.apple.driver.AppleParrot`](../kexts/com.apple.driver.AppleParrot.md) |
| `pci-bridge` | `IOPCI2PCIBridge` | [`com.apple.iokit.IOPCIFamily`](../kexts/com.apple.iokit.IOPCIFamily.md) |
| `pci106b,1c04` | `AppleConvergedPCILedaBB` | [`com.apple.driver.AppleConvergedIPCBBControl`](../kexts/com.apple.driver.AppleConvergedIPCBBControl.md) |
| `pci8086,7660` | `AppleConvergedPCIICEBB` | [`com.apple.driver.AppleConvergedIPCBBControl`](../kexts/com.apple.driver.AppleConvergedIPCBBControl.md) |
| `pdmclk` | `AppleSPUPDMCLKDriver` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `pmgr-disp-ctrl` | `PMGRDispCtrl` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) |
| `pmgr1,bring-up` | `AppleBringUpPMGR` | [`com.apple.driver.ApplePMGR`](../kexts/com.apple.driver.ApplePMGR.md) |
| `port` | `IOPort` | [`com.apple.iokit.IOAccessoryManager`](../kexts/com.apple.iokit.IOAccessoryManager.md) |
| `portmicro,smc-ccg2` | `AppleSMCHighVoltageCharger` | [`com.apple.driver.AppleSMC`](../kexts/com.apple.driver.AppleSMC.md) |
| `programmer-switch` | `AppleARMNMI` | [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md) |
| `pwm,s5l8920x` | `AppleS5L8920XPWM` | [`com.apple.driver.AppleS5L8920XPWM`](../kexts/com.apple.driver.AppleS5L8920XPWM.md) |
| `remote-ptd,v1` | `ApplePTDRemote` | [`com.apple.driver.ApplePTD`](../kexts/com.apple.driver.ApplePTD.md) |
| `romeo` | `AppleSPUGpioUnplugDriver` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) |
| `roswell` | `RoswellAuthI2CRelayInterface` | [`com.apple.driver.AppleAuthCP`](../kexts/com.apple.driver.AppleAuthCP.md) |
| `sart,t8015` | `IOSARTMapper` | [`com.apple.driver.AppleSART`](../kexts/com.apple.driver.AppleSART.md) |
| `sart-marconi,t8006` | `AppleSARTMarconi` | [`com.apple.driver.AppleSART`](../kexts/com.apple.driver.AppleSART.md) |
| `scctempsensor,s5l8950x` | `AppleSCCTempSensor` | [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md) |
| `sep-endpoint,artr` | `AppleSEPARTRequestsService` | [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md) |
| `sep-endpoint,arts` | `AppleSEPARTStorageService` | [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md) |
| `sep-endpoint,debu` | `AppleSEPDebugService` | [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md) |
| `sep-endpoint,eprl` | `ApplePearlExclaveSEPDriver` | [`com.apple.driver.ApplePearlExclaveSEPDriver`](../kexts/com.apple.driver.ApplePearlExclaveSEPDriver.md) |
| `sep-endpoint,hdcp` | `AppleSEPHDCPManager` | [`com.apple.driver.AppleSEPHDCPManager`](../kexts/com.apple.driver.AppleSEPHDCPManager.md) |
| `sep-endpoint,hilo` | `AppleSEPHiloService` | [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md) |
| `sep-endpoint,log` | `AppleSEPLoggerService` | [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md) |
| `sep-endpoint,pair` | `AppleSEPPairing` | [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md) |
| `sep-endpoint,sbio` | `AppleMesaSEPDriver` | [`com.apple.driver.AppleMesaSEPDriver`](../kexts/com.apple.driver.AppleMesaSEPDriver.md) |
| `sep-endpoint,sprl` | `ApplePearlSEPDriver` | [`com.apple.driver.ApplePearlSEPDriver`](../kexts/com.apple.driver.ApplePearlSEPDriver.md) |
| `sep-endpoint,sse` | `AppleSSE` | [`com.apple.driver.AppleSSE`](../kexts/com.apple.driver.AppleSSE.md) |
| `sep-endpoint,unit` | `AppleSEPTestingService` | [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md) |
| `sep-endpoint,xarm` | `AppleSEPXARTService` | [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md) |
| `sep-endpoint,xars` | `AppleSEPXARTService` | [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md) |
| `smc-orion-charger` | `AppleSMCCharger` | [`com.apple.driver.AppleSMC`](../kexts/com.apple.driver.AppleSMC.md) |
| `soc-tuner,t8030` | `AppleT8030SOCTuner` | [`com.apple.driver.AppleT8030SOCTuner`](../kexts/com.apple.driver.AppleT8030SOCTuner.md) |
| `sochot,s5l8955x` | `AppleSocHot` | [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md) |
| `system-manager` | `AppleAOP2SystemDriver` | [`com.apple.driver.AppleAOP2`](../kexts/com.apple.driver.AppleAOP2.md) |
| `tb-test-client-ep` | `AFKTBTestServer` | [`com.apple.driver.AppleFirmwareKit`](../kexts/com.apple.driver.AppleFirmwareKit.md) |
| `tb-test-server-ep` | `AFKTBTestClient` | [`com.apple.driver.AppleFirmwareKit`](../kexts/com.apple.driver.AppleFirmwareKit.md) |
| `tempsensor,s5l8945x` | `ApplePMGRTempSensor` | [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md) |
| `tempsensor,s8000` | `AppleT700XTempSensor` | [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md) |
| `tempsensor,t7000` | `AppleT700XTempSensor` | [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md) |
| `tempsensor,t7001` | `AppleT700XTempSensor` | [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md) |
| `tempsensor,t8006` | `AppleT700XTempSensor` | [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md) |
| `tempsensor,t8010` | `AppleT700XTempSensor` | [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md) |
| `tempsensor,t8012` | `AppleT700XTempSensor` | [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md) |
| `tempsensor,t8015` | `AppleT8015TempSensor` | [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md) |
| `tempsensor,t8020` | `AppleT8015TempSensor` | [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md) |
| `tempsensor,t8027` | `AppleT8015TempSensor` | [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md) |
| `tempsensor,t8030` | `AppleT8015TempSensor` | [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md) |
| `uart1` | `AppleSerialShim` | [`com.apple.driver.AppleSerialShim`](../kexts/com.apple.driver.AppleSerialShim.md) |
| `uart2` | `AppleSerialShim` | [`com.apple.driver.AppleSerialShim`](../kexts/com.apple.driver.AppleSerialShim.md) |
| `uart3` | `AppleSerialShim` | [`com.apple.driver.AppleSerialShim`](../kexts/com.apple.driver.AppleSerialShim.md) |
| `uart4` | `AppleSerialShim` | [`com.apple.driver.AppleSerialShim`](../kexts/com.apple.driver.AppleSerialShim.md) |
| `uart5` | `AppleSerialShim` | [`com.apple.driver.AppleSerialShim`](../kexts/com.apple.driver.AppleSerialShim.md) |
| `uart6` | `AppleSerialShim` | [`com.apple.driver.AppleSerialShim`](../kexts/com.apple.driver.AppleSerialShim.md) |
| `uart7` | `AppleSerialShim` | [`com.apple.driver.AppleSerialShim`](../kexts/com.apple.driver.AppleSerialShim.md) |
| `uart8` | `AppleSerialShim` | [`com.apple.driver.AppleSerialShim`](../kexts/com.apple.driver.AppleSerialShim.md) |
| `usb-complex,s5l8900x` | `AppleEmbeddedUSBArbitrator` | [`com.apple.driver.AppleEmbeddedUSB`](../kexts/com.apple.driver.AppleEmbeddedUSB.md) |
| `usb-drd,t6000` | `AppleT6000USBXHCI` | [`com.apple.driver.usb.AppleSynopsysUSB40XHCI`](../kexts/com.apple.driver.usb.AppleSynopsysUSB40XHCI.md) |
| `usb-drd,t8027` | `AppleT8027USBXDCI` | [`com.apple.driver.AppleUSBXDCIARM`](../kexts/com.apple.driver.AppleUSBXDCIARM.md) |
| `usb-drd,t8027` | `AppleT8027USBXHCI` | [`com.apple.driver.usb.AppleSynopsysUSBXHCI`](../kexts/com.apple.driver.usb.AppleSynopsysUSBXHCI.md) |
| `usb-drd,t8030` | `AppleT8030USBXDCI` | [`com.apple.driver.AppleUSBXDCIARM`](../kexts/com.apple.driver.AppleUSBXDCIARM.md) |
| `usb-drd,t8030` | `AppleT8030USBXHCI` | [`com.apple.driver.usb.AppleSynopsysUSBXHCI`](../kexts/com.apple.driver.usb.AppleSynopsysUSBXHCI.md) |
| `usb-drd,t8101` | `AppleT8101USBXHCI` | [`com.apple.driver.usb.AppleSynopsysUSBXHCI`](../kexts/com.apple.driver.usb.AppleSynopsysUSBXHCI.md) |
| `usb-drd,t8103` | `AppleT8103USBXDCI` | [`com.apple.driver.AppleUSBXDCIARM`](../kexts/com.apple.driver.AppleUSBXDCIARM.md) |
| `usb-drd,t8103` | `AppleT8103USBXHCI` | [`com.apple.driver.usb.AppleSynopsysUSB40XHCI`](../kexts/com.apple.driver.usb.AppleSynopsysUSB40XHCI.md) |
| `usb-drd,t8112` | `AppleT8112USBXDCI` | [`com.apple.driver.AppleUSBXDCIARM`](../kexts/com.apple.driver.AppleUSBXDCIARM.md) |
| `usb-drd,t8112` | `AppleT8112USBXHCI` | [`com.apple.driver.usb.AppleSynopsysUSB40XHCI`](../kexts/com.apple.driver.usb.AppleSynopsysUSB40XHCI.md) |
| `usb-drd,t8122` | `AppleT8122USBXDCI` | [`com.apple.driver.AppleUSBXDCIARM`](../kexts/com.apple.driver.AppleUSBXDCIARM.md) |
| `usb-drd,t8122` | `AppleT8122USBXHCI` | [`com.apple.driver.usb.AppleSynopsysUSB40XHCI`](../kexts/com.apple.driver.usb.AppleSynopsysUSB40XHCI.md) |
| `usb-drd,t8130` | `AppleT8130USBXDCI` | [`com.apple.driver.AppleUSBXDCIARM`](../kexts/com.apple.driver.AppleUSBXDCIARM.md) |
| `usb-drd,t8130` | `AppleT8130USBXHCI` | [`com.apple.driver.usb.AppleSynopsysUSBXHCI`](../kexts/com.apple.driver.usb.AppleSynopsysUSBXHCI.md) |
| `usb-drd,t8132` | `AppleT8132USBXDCI` | [`com.apple.driver.AppleUSBXDCIARM`](../kexts/com.apple.driver.AppleUSBXDCIARM.md) |
| `usb-drd,t8132` | `AppleT8132USBXHCI` | [`com.apple.driver.usb.AppleSynopsysUSB40XHCI`](../kexts/com.apple.driver.usb.AppleSynopsysUSB40XHCI.md) |
| `usb-drd,t8140` | `AppleT8140USBXDCI` | [`com.apple.driver.AppleUSBXDCIARM`](../kexts/com.apple.driver.AppleUSBXDCIARM.md) |
| `usb-drd,t8140` | `AppleT8140USBXHCI` | [`com.apple.driver.usb.AppleSynopsysUSBXHCI`](../kexts/com.apple.driver.usb.AppleSynopsysUSBXHCI.md) |
| `usb-drd,t8142` | `AppleT8142USBXDCI` | [`com.apple.driver.AppleUSBXDCIARM`](../kexts/com.apple.driver.AppleUSBXDCIARM.md) |
| `usb-drd,t8142` | `AppleT8142USBXHCI` | [`com.apple.driver.usb.AppleSynopsysUSB40XHCI`](../kexts/com.apple.driver.usb.AppleSynopsysUSB40XHCI.md) |
| `usb-drd,t8150` | `AppleT8150USBXDCI` | [`com.apple.driver.AppleUSBXDCIARM`](../kexts/com.apple.driver.AppleUSBXDCIARM.md) |
| `usb-drd,t8150` | `AppleT8150USBXHCI` | [`com.apple.driver.usb.AppleSynopsysUSBXHCI`](../kexts/com.apple.driver.usb.AppleSynopsysUSBXHCI.md) |
| `usb-drd,t8152` | `AppleT8152USBXDCI` | [`com.apple.driver.AppleUSBXDCIARM`](../kexts/com.apple.driver.AppleUSBXDCIARM.md) |
| `usb-drd,t8152` | `AppleT8152USBXHCI` | [`com.apple.driver.usb.AppleSynopsysUSB40XHCI`](../kexts/com.apple.driver.usb.AppleSynopsysUSB40XHCI.md) |
| `usb-hub-i2c` | `AppleUSBHubIICDevice` | [`com.apple.driver.AppleEmbeddedUSBHost`](../kexts/com.apple.driver.AppleEmbeddedUSBHost.md) |
| `usb-repeater-i2c,ticd2e22` | `AppleTICD2E22` | [`com.apple.driver.AppleEmbeddedUSBHost`](../kexts/com.apple.driver.AppleEmbeddedUSBHost.md) |
| `usbc,cd3215` | `AppleHPMARMI2C` | [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md) |
| `usbc,cd3217` | `AppleHPMARMI2C` | [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md) |
| `usbc,cd3217` | `AppleHPMSMCBridge` | [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md) |
| `usbc,manager` | `AppleHPMBusController` | [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md) |
| `usbc,sn201202x,iic` | `AppleHPMARMI2C` | [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md) |
| `usbc,sn201202x,spmi` | `AppleHPMARMSPMI` | [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md) |
| `usbc,spmi` | `AppleHPMARMSPMI` | [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md) |
| `vtempctl,s8000` | `AppleVTempDispatcher` | [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md) |
| `vtempctl,s8001` | `AppleVTempDispatcher` | [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md) |
| `vtempctl,s8003` | `AppleVTempDispatcher` | [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md) |
| `vtempctl,t8006` | `AppleVTempDispatcher` | [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md) |
| `vtempctl,t8010` | `AppleVTempDispatcher` | [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md) |
| `vtempctl,t8015` | `AppleVTempDispatcher` | [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md) |
| `vtempctl,t8020` | `AppleVTempDispatcher` | [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md) |
| `vtempctl,t8027` | `AppleVTempDispatcher` | [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md) |
| `vtempctl,t8030` | `AppleVTempDispatcher` | [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md) |
