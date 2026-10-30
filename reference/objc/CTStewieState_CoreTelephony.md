# `CTStewieState`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 15 instance variables, 15 properties, 54 instance methods, 1 class methods

## Instance variables

```
B _displaySatelliteIcon;
B _terrestrialNwAssessmentPending;
q _allowedServices;
q _activeServices;
q _status;
q _reason;
q _transportType;
q _subscriptionDeterminedServices;
q _subscribedServices;
q _congestedServices;
q _dataPathAssertedServices;
q _demoAllowedServices;
q _offGridCriteriaSatisfiedServices;
q _configuredForLocationServices;
q _baseReason;
```

## Properties

```
@property (Tq,N,V_allowedServices) allowedServices;
@property (Tq,N,V_activeServices) activeServices;
@property (Tq,N,V_subscriptionDeterminedServices) subscriptionDeterminedServices;
@property (Tq,N,V_subscribedServices) subscribedServices;
@property (Tq,N,V_congestedServices) congestedServices;
@property (Tq,N,V_dataPathAssertedServices) dataPathAssertedServices;
@property (Tq,N,V_demoAllowedServices) demoAllowedServices;
@property (Tq,N,V_offGridCriteriaSatisfiedServices) offGridCriteriaSatisfiedServices;
@property (Tq,N,V_configuredForLocationServices) configuredForLocationServices;
@property (Tq,N,V_status) status;
@property (Tq,N,V_reason) reason;
@property (Tq,N,V_baseReason) baseReason;
@property (Tq,N,V_transportType) transportType;
@property (TB,N,V_displaySatelliteIcon) displaySatelliteIcon;
@property (TB,N,V_terrestrialNwAssessmentPending) terrestrialNwAssessmentPending;
```

## Class methods

```
+[CTStewieState supportsSecureCoding];
```

## Instance methods

```
-[CTStewieState isStewieActive];
-[CTStewieState allowedServices];
-[CTStewieState setTransportType:];
-[CTStewieState isEqualToState:];
-[CTStewieState init];
-[CTStewieState status];
-[CTStewieState transportType];
-[CTStewieState setReason:];
-[CTStewieState activeServices];
-[CTStewieState encodeWithCoder:];
-[CTStewieState description];
-[CTStewieState initWithCoder:];
-[CTStewieState reason];
-[CTStewieState setStatus:];
-[CTStewieState copyWithZone:];
-[CTStewieState isEqual:];
-[CTStewieState isDemoAllowedForService:];
-[CTStewieState isActiveService:];
-[CTStewieState isAllowedService:];
-[CTStewieState searchingForTerrestrialNetworks];
-[CTStewieState baseReason];
-[CTStewieState configuredForLocationServices];
-[CTStewieState congestedServices];
-[CTStewieState dataPathAssertedServices];
-[CTStewieState demoAllowedServices];
-[CTStewieState displayInactiveSOSInStatusBar];
-[CTStewieState displaySatelliteIcon];
-[CTStewieState displayStewieInStatusBar];
-[CTStewieState initWithStewieState:];
-[CTStewieState isCongestedService:];
-[CTStewieState isOffGridCriteriaSatisfied:];
-[CTStewieState isPermittedAtCurrentLocation:];
-[CTStewieState isStewieActiveOverBB];
-[CTStewieState isStewieActiveOverInternet];
-[CTStewieState isSubscribedService:];
-[CTStewieState isSubscriptionRequired:];
-[CTStewieState isSubscriptionStatusNetworkDetermined:];
-[CTStewieState offGridCriteriaSatisfiedServices];
-[CTStewieState setActiveServices:];
-[CTStewieState setAllowedServices:];
-[CTStewieState setBaseReason:];
-[CTStewieState setConfiguredForLocationServices:];
-[CTStewieState setCongestedServices:];
-[CTStewieState setDataPathAssertedServices:];
-[CTStewieState setDemoAllowedServices:];
-[CTStewieState setDisplaySatelliteIcon:];
-[CTStewieState setOffGridCriteriaSatisfiedServices:];
-[CTStewieState setSubscribedServices:];
-[CTStewieState setSubscriptionDeterminedServices:];
-[CTStewieState setTerrestrialNwAssessmentPending:];
-[CTStewieState statusReasonForService:];
-[CTStewieState subscribedServices];
-[CTStewieState subscriptionDeterminedServices];
-[CTStewieState terrestrialNwAssessmentPending];
```
