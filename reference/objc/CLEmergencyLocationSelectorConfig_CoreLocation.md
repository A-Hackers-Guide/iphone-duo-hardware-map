# `CLEmergencyLocationSelectorConfig`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 16 instance variables, 16 properties, 36 instance methods, 1 class methods

## Instance variables

```
B _firstLocationEarlyReturnEnabled;
B _firstUpdateEnabled;
B _periodicUpdatesEnabled;
d _firstLocationTimeout;
d _locationUpdateTimeout;
d _locationUpdateMinDelay;
q _feature;
d _firstUpdateTimeout;
@"CLEmergencyLocationUsabilityCriteria" _firstLocationUsabilityCriteria;
d _firstLocationMaxEarlyReturnHunc;
d _firstLocationMaxEarlyReturnVunc;
@"CLEmergencyLocationUsabilityCriteria" _locationUpdateUsabilityCriteria;
d _locationUpdateHuncReductionToSendEarly;
d _locationUpdateVuncReductionToSendEarly;
d _locationUpdateDistanceMovedToSendEarly;
d _locationUpdateChangeInAltitudeToSendEarly;
```

## Properties

```
@property (Tq,N,V_feature) feature;
@property (TB,N,V_firstUpdateEnabled) firstUpdateEnabled;
@property (Td,N,V_firstUpdateTimeout) firstUpdateTimeout;
@property (TB,N,V_periodicUpdatesEnabled) periodicUpdatesEnabled;
@property (T@"CLEmergencyLocationUsabilityCriteria",&,N,V_firstLocationUsabilityCriteria) firstLocationUsabilityCriteria;
@property (Td,N,V_firstLocationMaxEarlyReturnHunc) firstLocationMaxEarlyReturnHunc;
@property (Td,N,V_firstLocationMaxEarlyReturnVunc) firstLocationMaxEarlyReturnVunc;
@property (T@"CLEmergencyLocationUsabilityCriteria",&,N,V_locationUpdateUsabilityCriteria) locationUpdateUsabilityCriteria;
@property (Td,N,V_locationUpdateHuncReductionToSendEarly) locationUpdateHuncReductionToSendEarly;
@property (Td,N,V_locationUpdateVuncReductionToSendEarly) locationUpdateVuncReductionToSendEarly;
@property (Td,N,V_locationUpdateDistanceMovedToSendEarly) locationUpdateDistanceMovedToSendEarly;
@property (Td,N,V_locationUpdateChangeInAltitudeToSendEarly) locationUpdateChangeInAltitudeToSendEarly;
@property (TB,N,V_firstLocationEarlyReturnEnabled) firstLocationEarlyReturnEnabled;
@property (Td,N,V_firstLocationTimeout) firstLocationTimeout;
@property (Td,N,V_locationUpdateTimeout) locationUpdateTimeout;
@property (Td,N,V_locationUpdateMinDelay) locationUpdateMinDelay;
```

## Class methods

```
+[CLEmergencyLocationSelectorConfig featureString:];
```

## Instance methods

```
-[CLEmergencyLocationSelectorConfig feature];
-[CLEmergencyLocationSelectorConfig dealloc];
-[CLEmergencyLocationSelectorConfig setFeature:];
-[CLEmergencyLocationSelectorConfig firstLocationMaxEarlyReturnHunc];
-[CLEmergencyLocationSelectorConfig firstLocationEarlyReturnEnabled];
-[CLEmergencyLocationSelectorConfig firstLocationMaxEarlyReturnVunc];
-[CLEmergencyLocationSelectorConfig locationUpdateUsabilityCriteria];
-[CLEmergencyLocationSelectorConfig firstLocationTimeout];
-[CLEmergencyLocationSelectorConfig firstLocationUsabilityCriteria];
-[CLEmergencyLocationSelectorConfig firstUpdateEnabled];
-[CLEmergencyLocationSelectorConfig firstUpdateTimeout];
-[CLEmergencyLocationSelectorConfig initForFeature:withUpdatesEnabled:];
-[CLEmergencyLocationSelectorConfig locationUpdateChangeInAltitudeToSendEarly];
-[CLEmergencyLocationSelectorConfig locationUpdateDistanceMovedToSendEarly];
-[CLEmergencyLocationSelectorConfig locationUpdateHuncReductionToSendEarly];
-[CLEmergencyLocationSelectorConfig locationUpdateMinDelay];
-[CLEmergencyLocationSelectorConfig locationUpdateTimeout];
-[CLEmergencyLocationSelectorConfig locationUpdateVuncReductionToSendEarly];
-[CLEmergencyLocationSelectorConfig periodicUpdatesEnabled];
-[CLEmergencyLocationSelectorConfig printConfiguration];
-[CLEmergencyLocationSelectorConfig setDefaultsForSIP];
-[CLEmergencyLocationSelectorConfig setFirstLocationEarlyReturnEnabled:];
-[CLEmergencyLocationSelectorConfig setFirstLocationMaxEarlyReturnHunc:];
-[CLEmergencyLocationSelectorConfig setFirstLocationMaxEarlyReturnVunc:];
-[CLEmergencyLocationSelectorConfig setFirstLocationTimeout:];
-[CLEmergencyLocationSelectorConfig setFirstLocationUsabilityCriteria:];
-[CLEmergencyLocationSelectorConfig setFirstUpdateEnabled:];
-[CLEmergencyLocationSelectorConfig setFirstUpdateTimeout:];
-[CLEmergencyLocationSelectorConfig setLocationUpdateChangeInAltitudeToSendEarly:];
-[CLEmergencyLocationSelectorConfig setLocationUpdateDistanceMovedToSendEarly:];
-[CLEmergencyLocationSelectorConfig setLocationUpdateHuncReductionToSendEarly:];
-[CLEmergencyLocationSelectorConfig setLocationUpdateMinDelay:];
-[CLEmergencyLocationSelectorConfig setLocationUpdateTimeout:];
-[CLEmergencyLocationSelectorConfig setLocationUpdateUsabilityCriteria:];
-[CLEmergencyLocationSelectorConfig setLocationUpdateVuncReductionToSendEarly:];
-[CLEmergencyLocationSelectorConfig setPeriodicUpdatesEnabled:];
```
