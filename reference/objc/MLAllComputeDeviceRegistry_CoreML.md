# `MLAllComputeDeviceRegistry`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MLComputeDeviceRegistryProtocol`
- 1 instance variables, 6 properties, 3 instance methods, 2 class methods

## Instance variables

```
@"NSArray" _deviceRegistries;
```

## Properties

```
@property (T@"NSArray",R,C,N,V_deviceRegistries) deviceRegistries;
@property (T@"NSArray",R,C,N) registeredComputeDevices;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[MLAllComputeDeviceRegistry sharedRegistry];
+[MLAllComputeDeviceRegistry registryWithDeviceRegistries:];
```

## Instance methods

```
-[MLAllComputeDeviceRegistry registeredComputeDevices];
-[MLAllComputeDeviceRegistry deviceRegistries];
-[MLAllComputeDeviceRegistry initWithDeviceRegistries:];
```
