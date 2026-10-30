# `IOUSBMassStorageDriver`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOUSBMassStorageDriver`](../kexts/com.apple.iokit.IOUSBMassStorageDriver.md)
- Object size: `0x1c8` (456 bytes)
- Metaclass: `0xfffffe000ba20c60`; metaclass vtable `0xfffffe00084772f0`; class vtable `0xfffffe0008476c48`
- Registration (init): `0xfffffe000a86dda0`
- Superclasses: [`IOSCSIProtocolServices`](IOSCSIProtocolServices.md) → [`IOSCSIProtocolInterface`](IOSCSIProtocolInterface.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 1 in total)

- [`com_apple_driver_AppleUSBCardReaderUMC`](com_apple_driver_AppleUSBCardReaderUMC.md) — `com.apple.driver.AppleUSBCardReader`

## IOKit personalities that instantiate it (52)

- `IOUSBMassStorageDriver` in [`com.apple.iokit.IOUSBMassStorageDriver`](../kexts/com.apple.iokit.IOUSBMassStorageDriver.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `AppleADSTechnologies_55349` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `AppleAddLogix_25092` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `AppleAlcor21In1Reader_1423_25442` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `AppleBelkin_F5U249` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `AppleBuffalo_USB_HS_1041_149` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `AppleBuffalo_USB_HS_1041_42` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `AppleCasioExlimEx_S500_4099` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `AppleChieftec_USB4500_17664` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `AppleDazzleUSB20MediaReader` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `AppleDazzleUSB20MediaReader2` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `AppleDigitalConcepts_CR_70R` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `AppleDrobo_6585_19728` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `AppleGB_PicoR_4089_4099` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `AppleGenericCFCardReader_25446` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `AppleGenericInitioIHDD_5117_1344` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `AppleHumanwareVictorReaderStream_7281_49153` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `AppleIPadConnectionKit_1` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `AppleIPadConnectionKit_2` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `AppleLacie8In1MediaReader` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `AppleLacieBigDisk` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `AppleLacieBigDisk_1317` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `AppleMacAllyPHR_100AC` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `AppleMagellanMaestro4250_65535` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `AppleMelcoDUB-P20G` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `AppleMelcoUSB2-SCSI-Bridge` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `ApplePQIU510_66` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `ApplePanasonicP2CardReader_1242_10241` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `ApplePanasonicUSBSDCameraDriver` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `ApplePioneer_Inno_GEX_INNO1_315` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `AppleRiData_1539` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `AppleSamsungIts80GB_769` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `AppleSamsungYP_Z5_20545` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `AppleSanDiskCruiser21510` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `AppleSanDiskCruiser21512` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `AppleSanDiskImageMate_6_in_1_Reader_1569` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `AppleSmartDriveHD3_U2` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `AppleSonyGPS_CS1KA_7424` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `AppleStorixAxis` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `AppleTascam2488NEO_1604_32795` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `AppleTascam2488_1604_32779` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `AppleTascam2488mkII_1604_32790` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `AppleTascamDP01_1604_32781` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `AppleTascamDP02_1604_32792` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `AppleTascamDV_RA1000HD_1604_32789` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `AppleTascamDV_RA1000_1604_32780` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `AppleVerbatimPortableUSB30Drive` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `AppleVosonic_VP3320` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `Apple_Procaster_PVR_6300C` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `Kingston_2385_5775` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `Optelec_Alva_BC640` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `StarTech_InfoSafe_9016` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`

## Strings in its kext that name it (16)

- `site.IOUSBMassStorageDriverNubExpansionData`
- `IOUSBMassStorageDriver: %016llX-HLEr> %s\n`
- `IOUSBMassStorageDriver: %016llX-Misc> %s\n`
- `site.IOUSBMassStorageDriverNub`
- `IOUSBMassStorageDriverNub`
- `IOUSBMassStorageDriver: %016llX stop ...\n`
- `site.IOUSBMassStorageDriver`
- `IOUSBMassStorageDriverRequestTimer.cpp`
- `IOUSBMassStorageDriverRequestTimer`
- `IOUSBMassStorageDriver: %016llX usb reset ...\n`
- `site.IOUSBMassStorageDriverRequestTimer`
- `USB device %016llX - fIOUSBMassStorageDriverNub->terminate().\n`
- `site.IOUSBMassStorageDriverExpansionData`
- `IOUSBMassStorageDriver: %016llX-%s %s\n`
- `IOUSBMassStorageDriver.cpp`
- `IOUSBMassStorageDriver`
