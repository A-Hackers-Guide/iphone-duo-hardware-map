# `ACCFeaturePluginHIDProvider`

- Image: [`/System/Library/CoreAccessories/PlugIns/Features/HID.feature/HID`](../userland/System__Library__CoreAccessories__PlugIns__Features__HID.feature__HID.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AccessoryHIDClientProtocol`
- 3 instance variables, 7 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"NSMutableArray" _descriptorUUIDs;
@"AccessoryHIDClient" _hidClient;
@"NSObject<OS_dispatch_queue>" _hidProviderLock;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_descriptorUUIDs) descriptorUUIDs;
@property (T@"AccessoryHIDClient",&,V_hidClient) hidClient;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_hidProviderLock) hidProviderLock;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[ACCFeaturePluginHIDProvider sharedHIDProvider];
```

## Instance methods

```
-[ACCFeaturePluginHIDProvider init];
-[ACCFeaturePluginHIDProvider dealloc];
-[ACCFeaturePluginHIDProvider getDescriptor:];
-[ACCFeaturePluginHIDProvider createHIDDescriptor:];
-[ACCFeaturePluginHIDProvider deleteHIDDescriptor:];
-[ACCFeaturePluginHIDProvider processGetReportResponse:reportType:reportID:forUUID:];
-[ACCFeaturePluginHIDProvider processInReport:forUUID:];
-[ACCFeaturePluginHIDProvider descriptorUUIDs];
-[ACCFeaturePluginHIDProvider hidProviderLock];
-[ACCFeaturePluginHIDProvider stopHIDProvider];
-[ACCFeaturePluginHIDProvider hidClient];
-[ACCFeaturePluginHIDProvider setDescriptorUUIDs:];
-[ACCFeaturePluginHIDProvider setHidClient:];
-[ACCFeaturePluginHIDProvider setHidProviderLock:];
-[ACCFeaturePluginHIDProvider startHIDProvider];
```
