# `CAFRouteStatus`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 16 properties, 34 instance methods, 2 class methods

## Properties

```
@property (T@"CAFStringCharacteristic",R,N) userVisibleApplicationNameCharacteristic;
@property (T@"CAFRouteStateCharacteristic",R,N) routeStateCharacteristic;
@property (T@"CAFRerouteReasonCharacteristic",R,N) rerouteReasonCharacteristic;
@property (T@"CAFGeodeticSystemCharacteristic",R,N) geodeticSystemCharacteristic;
@property (T@"CAFPointOfInterestCharacteristic",R,N) originCharacteristic;
@property (T@"CAFPointOfInterestCharacteristic",R,N) destinationCharacteristic;
@property (T@"NSString",C,N) userVisibleApplicationName;
@property (TB,R,N) userVisibleApplicationNameInvalid;
@property (TC,N) routeState;
@property (TC,N) rerouteReason;
@property (TB,R,N) hasRerouteReason;
@property (TC,N) geodeticSystem;
@property (T@"CAFPointOfInterest",&,N) origin;
@property (TB,R,N) originInvalid;
@property (T@"CAFPointOfInterest",&,N) destination;
@property (TB,R,N) destinationInvalid;
```

## Class methods

```
+[CAFRouteStatus serviceIdentifier];
+[CAFRouteStatus observerProtocol];
```

## Instance methods

```
-[CAFRouteStatus destination];
-[CAFRouteStatus origin];
-[CAFRouteStatus removeObserver:];
-[CAFRouteStatus addObserver:];
-[CAFRouteStatus setDestination:];
-[CAFRouteStatus setOrigin:];
-[CAFRouteStatus registerObserver:];
-[CAFRouteStatus name];
-[CAFRouteStatus unregisterObserver:];
-[CAFRouteStatus geodeticSystem];
-[CAFRouteStatus setGeodeticSystem:];
-[CAFRouteStatus setRerouteReason:];
-[CAFRouteStatus setRouteState:];
-[CAFRouteStatus setUserVisibleApplicationName:];
-[CAFRouteStatus hasRerouteReason];
-[CAFRouteStatus registeredForDestination];
-[CAFRouteStatus registeredForGeodeticSystem];
-[CAFRouteStatus registeredForOrigin];
-[CAFRouteStatus registeredForRerouteReason];
-[CAFRouteStatus registeredForRouteState];
-[CAFRouteStatus registeredForUserVisibleApplicationName];
-[CAFRouteStatus rerouteReason];
-[CAFRouteStatus routeState];
-[CAFRouteStatus userVisibleApplicationName];
-[CAFRouteStatus _characteristicDidUpdate:fromGroupUpdate:];
-[CAFRouteStatus destinationCharacteristic];
-[CAFRouteStatus destinationInvalid];
-[CAFRouteStatus geodeticSystemCharacteristic];
-[CAFRouteStatus originCharacteristic];
-[CAFRouteStatus originInvalid];
-[CAFRouteStatus rerouteReasonCharacteristic];
-[CAFRouteStatus routeStateCharacteristic];
-[CAFRouteStatus userVisibleApplicationNameCharacteristic];
-[CAFRouteStatus userVisibleApplicationNameInvalid];
```
