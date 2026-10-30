# `IOUSBHostInterface`

- Image: [`/System/Library/PrivateFrameworks/IOUSBHost.framework/IOUSBHost`](../userland/System__Library__PrivateFrameworks__IOUSBHost.framework__IOUSBHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOUSBHostObject`
- 3 instance variables, 5 properties, 12 instance methods, 1 class methods

## Instance variables

```
r^{IOUSBConfigurationDescriptor=CCSCCCCC} _configurationDescriptor;
Q _interfaceNumber;
Q _lastKnownAlternateSetting;
```

## Properties

```
@property (Tr^{IOUSBConfigurationDescriptor=CCSCCCCC},V_configurationDescriptor) configurationDescriptor;
@property (TQ,V_interfaceNumber) interfaceNumber;
@property (TQ,V_lastKnownAlternateSetting) lastKnownAlternateSetting;
@property (Td,R) idleTimeout;
@property (Tr^{IOUSBInterfaceDescriptor=CCCCCCCCC},R) interfaceDescriptor;
```

## Class methods

```
+[IOUSBHostInterface createMatchingDictionaryWithVendorID:productID:bcdDevice:interfaceNumber:configurationValue:interfaceClass:interfaceSubclass:interfaceProtocol:speed:productIDArray:];
```

## Instance methods

```
-[IOUSBHostInterface idleTimeout];
-[IOUSBHostInterface configurationDescriptor];
-[IOUSBHostInterface interfaceNumber];
-[IOUSBHostInterface copyPipeWithAddress:error:];
-[IOUSBHostInterface initWithIOService:options:queue:error:interestHandler:];
-[IOUSBHostInterface interfaceDescriptor];
-[IOUSBHostInterface lastKnownAlternateSetting];
-[IOUSBHostInterface selectAlternateSetting:error:];
-[IOUSBHostInterface setConfigurationDescriptor:];
-[IOUSBHostInterface setIdleTimeout:error:];
-[IOUSBHostInterface setInterfaceNumber:];
-[IOUSBHostInterface setLastKnownAlternateSetting:];
```
