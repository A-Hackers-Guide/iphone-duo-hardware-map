# `CAFAccessory`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAFCacheableDescription`, `CAFValueMonitorDelegate`, `CAFEntity`
- 19 instance variables, 28 properties, 48 instance methods, 4 class methods

## Instance variables

```
B _receivedAllValues;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _indexLock;
@"CAFCar" _car;
@"NSString" _version;
@"NSDictionary" _services;
@"NSNumber" _pluginID;
@"NSNumber" _instanceID;
@"NSString" _handlerName;
@"NSString" _categoryType;
@"NSUUID" _uniqueIdentifier;
@"NSString" _typeName;
@"CAFCachedDescription" _cachedDescription;
@"CAFValueMonitor" _valueMonitor;
@"NSArray" _allServices;
@"NSArray" _allCharacteristics;
@"NSArray" _allControls;
@"NSDictionary" _servicesByType;
@"NSDictionary" _servicesIndexBy;
@"CARObserverHashTable" _observers;
```

## Properties

```
@property (T@"NSNumber",R,N,V_pluginID) pluginID;
@property (T@"NSNumber",R,N,V_instanceID) instanceID;
@property (T@"NSString",R,N,V_handlerName) handlerName;
@property (T@"NSString",R,N,V_categoryType) categoryType;
@property (T@"NSUUID",&,N,V_uniqueIdentifier) uniqueIdentifier;
@property (T@"NSString",&,N,V_typeName) typeName;
@property (T@"CAFCachedDescription",&,N,V_cachedDescription) cachedDescription;
@property (T@"CAFValueMonitor",&,N,V_valueMonitor) valueMonitor;
@property (TB,N,V_receivedAllValues) receivedAllValues;
@property (T@"NSArray",R,N,V_allServices) allServices;
@property (T@"NSArray",R,N,V_allCharacteristics) allCharacteristics;
@property (T@"NSArray",R,N,V_allControls) allControls;
@property (T@"NSDictionary",R,N,V_servicesByType) servicesByType;
@property (T@"NSDictionary",R,N,V_servicesIndexBy) servicesIndexBy;
@property (T@"CARObserverHashTable",&,N,V_observers) observers;
@property (T{os_unfair_lock_s=I},N,V_indexLock) indexLock;
@property (T@"CAFCar",R,W,N,V_car) car;
@property (T@"NSString",R,N,V_version) version;
@property (T@"NSDictionary",R,N,V_services) services;
@property (T@"NSArray",R,N) sortedServices;
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
+[CAFAccessory accessoryIdentifier];
+[CAFAccessory _sharedServiceGroupInitQueue];
+[CAFAccessory accessoryWithCar:pluginID:handlerName:config:];
+[CAFAccessory observerProtocol];
```

## Instance methods

```
-[CAFAccessory allServices];
-[CAFAccessory cachedDescription];
-[CAFAccessory categoryType];
-[CAFAccessory typeName];
-[CAFAccessory services];
-[CAFAccessory removeObserver:];
-[CAFAccessory compare:];
-[CAFAccessory setUniqueIdentifier:];
-[CAFAccessory uniqueIdentifier];
-[CAFAccessory version];
-[CAFAccessory addObserver:];
-[CAFAccessory invalidate];
-[CAFAccessory instanceID];
-[CAFAccessory setCachedDescription:];
-[CAFAccessory allControls];
-[CAFAccessory description];
-[CAFAccessory setObservers:];
-[CAFAccessory observers];
-[CAFAccessory registerObserver:];
-[CAFAccessory name];
-[CAFAccessory unregisterObserver:];
-[CAFAccessory state];
-[CAFAccessory setTypeName:];
-[CAFAccessory car];
-[CAFAccessory allCharacteristics];
-[CAFAccessory receivedAllValues];
-[CAFAccessory setReceivedAllValues:];
-[CAFAccessory usable];
-[CAFAccessory servicesIndexBy];
-[CAFAccessory _serviceDidNotify:control:withValue:];
-[CAFAccessory _serviceDidUpdate:characteristic:];
-[CAFAccessory _serviceDidUpdate:control:];
-[CAFAccessory _serviceReceivedAllValues:];
-[CAFAccessory baseCAFClass];
-[CAFAccessory comparisonKeys];
-[CAFAccessory currentDescriptionForCache:];
-[CAFAccessory handlerName];
-[CAFAccessory indexLock];
-[CAFAccessory initWithCar:pluginID:handlerName:config:];
-[CAFAccessory pluginID];
-[CAFAccessory refreshCharacteristics];
-[CAFAccessory servicesByType];
-[CAFAccessory servicesForIndexBy:];
-[CAFAccessory servicesForType:];
-[CAFAccessory setIndexLock:];
-[CAFAccessory setValueMonitor:];
-[CAFAccessory sortedServices];
-[CAFAccessory valueMonitor];
```
