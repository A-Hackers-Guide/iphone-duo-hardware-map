# `CAFService`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAFCacheableDescription`, `CAFValueMonitorDelegate`, `CAFEntity`
- 18 instance variables, 29 properties, 63 instance methods, 5 class methods

## Instance variables

```
B _receivedAllValues;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _characteristicTrackingLock;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _controlTrackingLock;
@"NSDictionary" _characteristics;
@"NSDictionary" _characteristicsByType;
@"NSArray" _characteristicsWithLargePayload;
@"NSDictionary" _controls;
@"NSDictionary" _controlsByType;
@ _observableCache;
@"CAFAccessory" _accessory;
@"NSNumber" _instanceID;
@"NSString" _serviceType;
@"NSUUID" _uniqueIdentifier;
@"NSString" _typeName;
@"CAFCachedDescription" _cachedDescription;
@"CAFValueMonitor" _valueMonitor;
@"CARObserverHashTable" _observers;
@"NSObject<OS_dispatch_queue>" _rawDataRegisterQueue;
```

## Properties

```
@property (T@"NSNumber",R,N,V_instanceID) instanceID;
@property (T@"NSString",R,N,V_serviceType) serviceType;
@property (T@"NSUUID",&,N,V_uniqueIdentifier) uniqueIdentifier;
@property (T@"NSString",&,N,V_typeName) typeName;
@property (T@"CAFCachedDescription",&,N,V_cachedDescription) cachedDescription;
@property (T@"CAFValueMonitor",&,N,V_valueMonitor) valueMonitor;
@property (TB,N,V_receivedAllValues) receivedAllValues;
@property (T@"NSDictionary",R,N,V_characteristicsByType) characteristicsByType;
@property (T@"NSArray",R,N,V_characteristicsWithLargePayload) characteristicsWithLargePayload;
@property (T@"NSDictionary",R,N,V_controlsByType) controlsByType;
@property (T@"CARObserverHashTable",&,N,V_observers) observers;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_rawDataRegisterQueue) rawDataRegisterQueue;
@property (T{os_unfair_lock_s=I},N,V_characteristicTrackingLock) characteristicTrackingLock;
@property (T{os_unfair_lock_s=I},N,V_controlTrackingLock) controlTrackingLock;
@property (T@"CAFCar",R,W,N) car;
@property (T@"CAFAccessory",R,W,N,V_accessory) accessory;
@property (TB,R,N) hasError;
@property (T@"NSDictionary",R,N,V_characteristics) characteristics;
@property (T@"NSArray",R,N) sortedCharacteristics;
@property (T@"NSDictionary",R,N,V_controls) controls;
@property (T@"NSArray",R,N) sortedControls;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,N) name;
@property (TB,R,N) usable;
@property (T#,R,N) baseCAFClass;
@property (T@"NSArray",R,N) comparisonKeys;
```

## Class methods

```
+[CAFService serviceIdentifier];
+[CAFService serviceType];
+[CAFService indexBy];
+[CAFService observerProtocol];
+[CAFService serviceWithAccessory:config:];
```

## Instance methods

```
-[CAFService cachedDescription];
-[CAFService typeName];
-[CAFService removeObserver:];
-[CAFService compare:];
-[CAFService setUniqueIdentifier:];
-[CAFService uniqueIdentifier];
-[CAFService addObserver:];
-[CAFService invalidate];
-[CAFService instanceID];
-[CAFService setCachedDescription:];
-[CAFService description];
-[CAFService setObservers:];
-[CAFService observers];
-[CAFService registerObserver:];
-[CAFService name];
-[CAFService unregisterObserver:];
-[CAFService controls];
-[CAFService accessory];
-[CAFService hasError];
-[CAFService serviceType];
-[CAFService state];
-[CAFService controlForType:];
-[CAFService setTypeName:];
-[CAFService car];
-[CAFService characteristics];
-[CAFService receivedAllValues];
-[CAFService setReceivedAllValues:];
-[CAFService observableCache];
-[CAFService setObservableCache:];
-[CAFService usable];
-[CAFService characteristicsWithLargePayload];
-[CAFService indexBy];
-[CAFService controlForName:];
-[CAFService _characteristicDidUpdate:fromGroupUpdate:];
-[CAFService _characteristicDidUpdateState:];
-[CAFService _controlDidNotify:withValue:];
-[CAFService _controlDidUpdate:];
-[CAFService _didUpdateValuesForGroupedCharacteristics:];
-[CAFService _updateReceivedValuesWithCharacteristic:];
-[CAFService baseCAFClass];
-[CAFService characteristicForName:];
-[CAFService characteristicForType:];
-[CAFService characteristicTrackingLock];
-[CAFService characteristicsByType];
-[CAFService comparisonKeys];
-[CAFService controlTrackingLock];
-[CAFService controlsByType];
-[CAFService currentDescriptionForCache:];
-[CAFService initWithAccessory:config:];
-[CAFService pluginID];
-[CAFService rawDataRegisterQueue];
-[CAFService refreshCharacteristics];
-[CAFService registerAllRawDataIfNeeded];
-[CAFService registerServiceObserver:];
-[CAFService setCharacteristicTrackingLock:];
-[CAFService setControlTrackingLock:];
-[CAFService setRawDataRegisterQueue:];
-[CAFService setValueMonitor:];
-[CAFService sortedCharacteristics];
-[CAFService sortedControls];
-[CAFService unregisterAllRawDataIfNeeded];
-[CAFService unregisterServiceObserver:];
-[CAFService valueMonitor];
```
