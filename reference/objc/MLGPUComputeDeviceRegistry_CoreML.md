# `MLGPUComputeDeviceRegistry`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MLComputeDeviceRegistryProtocol`
- 5 instance variables, 9 properties, 9 instance methods, 2 class methods

## Instance variables

```
{mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}} _mutex;
@"NSMutableDictionary" _availableGPUDevices;
@"NSMutableArray" _pendingChanges;
@"MLMetalDeviceObserver" _metalDeviceObserver;
@"<NSObject>" _observationToken;
```

## Properties

```
@property (T@"NSMutableDictionary",R,C,N,V_availableGPUDevices) availableGPUDevices;
@property (T@"NSMutableArray",R,C,N,V_pendingChanges) pendingChanges;
@property (T@"MLMetalDeviceObserver",R,N,V_metalDeviceObserver) metalDeviceObserver;
@property (T@"<NSObject>",&,N,V_observationToken) observationToken;
@property (T@"NSArray",R,C,N) registeredComputeDevices;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[MLGPUComputeDeviceRegistry sharedRegistry];
+[MLGPUComputeDeviceRegistry registryWithMetalDeviceObserver:];
```

## Instance methods

```
-[MLGPUComputeDeviceRegistry metalDeviceObserver];
-[MLGPUComputeDeviceRegistry availableGPUDevices];
-[MLGPUComputeDeviceRegistry registerGPUDevices];
-[MLGPUComputeDeviceRegistry dealloc];
-[MLGPUComputeDeviceRegistry initWithMetalDeviceObserver:];
-[MLGPUComputeDeviceRegistry observationToken];
-[MLGPUComputeDeviceRegistry setObservationToken:];
-[MLGPUComputeDeviceRegistry pendingChanges];
-[MLGPUComputeDeviceRegistry registeredComputeDevices];
```
