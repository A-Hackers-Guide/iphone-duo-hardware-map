# `DeviceTypeDeviceIdentity`

- Image: [`/System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity`](../userland/System__Library__PrivateFrameworks__DeviceIdentity.framework__DeviceIdentity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 22 instance variables, 22 properties, 30 instance methods, 1 class methods

## Instance variables

```
B _device_supports_dcrt_oob;
B _device_supports_mfi_certificates;
B _device_supports_eda_certificates;
B _is_prodfused_demoted;
B _is_devfused_undemoted;
B _is_dev_board;
B _is_fpga;
B _is_ipod;
B _is_ipad;
B _is_iphone;
B _is_audio_accessory;
B _is_home_accessory;
B _has_baseband;
B _should_hactivate;
B _is_internal_build;
B _is_factory_restored;
B _has_internal_diagnostics;
B _ucrt_enforced;
@"NSString" _product_type;
@"NSString" _device_class;
@"NSString" _hardware_model;
@"NSString" _soc_generation;
```

## Properties

```
@property (T@"NSString",R,C,N,V_product_type) product_type;
@property (T@"NSString",R,C,N,V_device_class) device_class;
@property (T@"NSString",R,C,N,V_hardware_model) hardware_model;
@property (T@"NSString",R,C,N,V_soc_generation) soc_generation;
@property (TB,R,N,V_device_supports_dcrt_oob) device_supports_dcrt_oob;
@property (TB,R,N,V_device_supports_mfi_certificates) device_supports_mfi_certificates;
@property (TB,R,N,V_device_supports_eda_certificates) device_supports_eda_certificates;
@property (TB,R,N,V_is_prodfused_demoted) is_prodfused_demoted;
@property (TB,R,N,V_is_devfused_undemoted) is_devfused_undemoted;
@property (TB,R,N,V_is_dev_board) is_dev_board;
@property (TB,R,N,V_is_fpga) is_fpga;
@property (TB,R,N,V_is_ipod) is_ipod;
@property (TB,R,N,V_is_ipad) is_ipad;
@property (TB,R,N,V_is_iphone) is_iphone;
@property (TB,R,N,V_is_audio_accessory) is_audio_accessory;
@property (TB,R,N,V_is_home_accessory) is_home_accessory;
@property (TB,R,N,V_has_baseband) has_baseband;
@property (TB,R,N,V_should_hactivate) should_hactivate;
@property (TB,R,N,V_is_internal_build) is_internal_build;
@property (TB,R,N,V_is_factory_restored) is_factory_restored;
@property (TB,R,N,V_has_internal_diagnostics) has_internal_diagnostics;
@property (TB,R,N,V_ucrt_enforced) ucrt_enforced;
```

## Class methods

```
+[DeviceTypeDeviceIdentity sharedInstance];
```

## Instance methods

```
-[DeviceTypeDeviceIdentity init];
-[DeviceTypeDeviceIdentity copyBootSessionUUID];
-[DeviceTypeDeviceIdentity copyDeviceTreeInt:key:defaultValue:];
-[DeviceTypeDeviceIdentity copyDeviceTreeProperty:key:];
-[DeviceTypeDeviceIdentity is_fpga];
-[DeviceTypeDeviceIdentity is_ipod];
-[DeviceTypeDeviceIdentity is_ipad];
-[DeviceTypeDeviceIdentity copyBootArgs];
-[DeviceTypeDeviceIdentity copyDeviceTreeInt:key:];
-[DeviceTypeDeviceIdentity copyDeviceTreeString:key:defaultValue:];
-[DeviceTypeDeviceIdentity device_class];
-[DeviceTypeDeviceIdentity device_supports_dcrt_oob];
-[DeviceTypeDeviceIdentity device_supports_eda_certificates];
-[DeviceTypeDeviceIdentity device_supports_mfi_certificates];
-[DeviceTypeDeviceIdentity hardware_model];
-[DeviceTypeDeviceIdentity has_baseband];
-[DeviceTypeDeviceIdentity has_internal_diagnostics];
-[DeviceTypeDeviceIdentity is_audio_accessory];
-[DeviceTypeDeviceIdentity is_dev_board];
-[DeviceTypeDeviceIdentity is_devfused_undemoted];
-[DeviceTypeDeviceIdentity is_factory_restored];
-[DeviceTypeDeviceIdentity is_home_accessory];
-[DeviceTypeDeviceIdentity is_internal_build];
-[DeviceTypeDeviceIdentity is_iphone];
-[DeviceTypeDeviceIdentity is_prodfused_demoted];
-[DeviceTypeDeviceIdentity product_type];
-[DeviceTypeDeviceIdentity runningInRAMDisk];
-[DeviceTypeDeviceIdentity should_hactivate];
-[DeviceTypeDeviceIdentity soc_generation];
-[DeviceTypeDeviceIdentity ucrt_enforced];
```
