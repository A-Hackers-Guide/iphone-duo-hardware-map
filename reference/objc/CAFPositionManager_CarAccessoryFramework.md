# `CAFPositionManager`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAFCarObserverPrivate`, `CAFServiceObserver`
- 8 instance variables, 13 properties, 31 instance methods, 0 class methods

## Instance variables

```
Q _state;
@"CAFCar" _car;
@"NSObject<OS_dispatch_queue>" _workQueue;
@"CARObserverHashTable" _observers;
@"NSSet" _positionedAccessories;
@"NSArray" _positionedServices;
@"NSDictionary" _servicesForVehicleLayoutKey;
@"NSDictionary" _vehicleLayoutKeysForServiceType;
```

## Properties

```
@property (T@"CAFCar",R,W,N,V_car) car;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_workQueue) workQueue;
@property (T@"CARObserverHashTable",&,N,V_observers) observers;
@property (TQ,N,V_state) state;
@property (T@"NSSet",&,N,V_positionedAccessories) positionedAccessories;
@property (T@"NSArray",&,N,V_positionedServices) positionedServices;
@property (T@"NSDictionary",&,N,V_servicesForVehicleLayoutKey) servicesForVehicleLayoutKey;
@property (T@"NSDictionary",&,N,V_vehicleLayoutKeysForServiceType) vehicleLayoutKeysForServiceType;
@property (T@"NSArray",R,N) vehicleLayoutKeys;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAFPositionManager setState:];
-[CAFPositionManager workQueue];
-[CAFPositionManager setObservers:];
-[CAFPositionManager observers];
-[CAFPositionManager registerObserver:];
-[CAFPositionManager unregisterObserver:];
-[CAFPositionManager state];
-[CAFPositionManager car];
-[CAFPositionManager carDidUpdate:receivedAllValues:];
-[CAFPositionManager carDidUpdate:accessory:service:characteristic:];
-[CAFPositionManager carDidUpdateAccessories:];
-[CAFPositionManager serviceDidUpdate:characteristic:fromGroupUpdate:];
-[CAFPositionManager servicesForVehicleLayoutKey:];
-[CAFPositionManager vehicleLayoutKeys];
-[CAFPositionManager vehicleLayoutKeysFor:];
-[CAFPositionManager _rebuildCacheIfNeededforReason:];
-[CAFPositionManager vehicleLayoutKeysForServiceType];
-[CAFPositionManager setServicesForVehicleLayoutKey:];
-[CAFPositionManager _isVehicleLayoutKeyCharacteristic:];
-[CAFPositionManager _queue_buildTrackingCache];
-[CAFPositionManager _queue_positionedServices];
-[CAFPositionManager _queue_stateForPositionedServices:];
-[CAFPositionManager accessoryIsTracked:];
-[CAFPositionManager carIsConfigured:];
-[CAFPositionManager initWithCar:];
-[CAFPositionManager positionedAccessories];
-[CAFPositionManager positionedServices];
-[CAFPositionManager servicesForVehicleLayoutKey];
-[CAFPositionManager setPositionedAccessories:];
-[CAFPositionManager setPositionedServices:];
-[CAFPositionManager setVehicleLayoutKeysForServiceType:];
```
