# `IOUSBHostDevice`

- Image: [`/System/Library/PrivateFrameworks/IOUSBHost.framework/IOUSBHost`](../userland/System__Library__PrivateFrameworks__IOUSBHost.framework__IOUSBHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOUSBHostObject`
- 1 instance variables, 2 properties, 7 instance methods, 1 class methods

## Instance variables

```
Q _lastKnownConfiguration;
```

## Properties

```
@property (TQ,V_lastKnownConfiguration) lastKnownConfiguration;
@property (Tr^{IOUSBConfigurationDescriptor=CCSCCCCC},R) configurationDescriptor;
```

## Class methods

```
+[IOUSBHostDevice createMatchingDictionaryWithVendorID:productID:bcdDevice:deviceClass:deviceSubclass:deviceProtocol:speed:productIDArray:];
```

## Instance methods

```
-[IOUSBHostDevice resetWithError:];
-[IOUSBHostDevice configurationDescriptor];
-[IOUSBHostDevice allocateDownstreamBusCurrentWithWakeUnits:sleepUnits:error:];
-[IOUSBHostDevice configureWithValue:error:];
-[IOUSBHostDevice configureWithValue:matchInterfaces:error:];
-[IOUSBHostDevice lastKnownConfiguration];
-[IOUSBHostDevice setLastKnownConfiguration:];
```
