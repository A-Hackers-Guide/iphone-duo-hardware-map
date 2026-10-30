# `NIFindingConfiguration`

- Image: [`/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`](../userland/System__Library__Frameworks__NearbyInteraction.framework__NearbyInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NIConfiguration`
- 12 instance variables, 14 properties, 39 instance methods, 1 class methods

## Instance variables

```
B _cameraAssistanceEnabled;
B _cameraAssistanceInClientProcess;
B _isFinder;
B _isObserver;
q _preferredUpdateRate;
q _preferredDiscoveryPriority;
@"NSArray" _monitoredRegions;
q _configType;
@"NIDiscoveryToken" _specifiedToken;
@"NSDictionary" _debugParameters;
q _discoveryTokenVariant;
q _requestedMeasurementQuality;
```

## Properties

```
@property (TB,N,V_isFinder) isFinder;
@property (TB,N,V_isObserver) isObserver;
@property (Tq,N,V_configType) configType;
@property (T@"NIDiscoveryToken",C,N,V_specifiedToken) specifiedToken;
@property (T@"NIDiscoveryToken",R,C,N) findingDiscoveryToken;
@property (T@"NSDictionary",C,N,V_debugParameters) debugParameters;
@property (Tq,N,V_discoveryTokenVariant) discoveryTokenVariant;
@property (Tq,N,V_requestedMeasurementQuality) requestedMeasurementQuality;
@property (T@"NIDiscoveryToken",R,C,N) sessionDiscoveryToken;
@property (Tq,N,V_preferredUpdateRate) preferredUpdateRate;
@property (Tq,N,V_preferredDiscoveryPriority) preferredDiscoveryPriority;
@property (TB,N,GisCameraAssistanceEnabled,V_cameraAssistanceEnabled) cameraAssistanceEnabled;
@property (TB,N,GisCameraAssistanceInClientProcess,V_cameraAssistanceInClientProcess) cameraAssistanceInClientProcess;
@property (T@"NSArray",&,V_monitoredRegions) monitoredRegions;
```

## Class methods

```
+[NIFindingConfiguration supportsSecureCoding];
```

## Instance methods

```
-[NIFindingConfiguration setCameraAssistanceEnabled:];
-[NIFindingConfiguration monitoredRegions];
-[NIFindingConfiguration preferredUpdateRate];
-[NIFindingConfiguration descriptionInternal];
-[NIFindingConfiguration canUpdateToConfiguration:];
-[NIFindingConfiguration setPreferredUpdateRate:];
-[NIFindingConfiguration encodeWithCoder:];
-[NIFindingConfiguration _internalIsCameraAssistanceEnabled];
-[NIFindingConfiguration hash];
-[NIFindingConfiguration setMonitoredRegions:];
-[NIFindingConfiguration isCameraAssistanceEnabled];
-[NIFindingConfiguration description];
-[NIFindingConfiguration initWithCoder:];
-[NIFindingConfiguration copyWithZone:];
-[NIFindingConfiguration isEqual:];
-[NIFindingConfiguration isFinder];
-[NIFindingConfiguration configType];
-[NIFindingConfiguration setConfigType:];
-[NIFindingConfiguration isObserver];
-[NIFindingConfiguration setIsObserver:];
-[NIFindingConfiguration debugParameters];
-[NIFindingConfiguration setRequestedMeasurementQuality:];
-[NIFindingConfiguration _initInternalWithConfigType:isFinder:isObserver:specifiedToken:preferredUpdateRate:requestedMeasurementQuality:];
-[NIFindingConfiguration _internalIsCameraAssistanceInClientProcess];
-[NIFindingConfiguration discoveryTokenVariant];
-[NIFindingConfiguration findingDiscoveryToken];
-[NIFindingConfiguration initWithDiscoveryToken:requestedUpdateRate:requestedMeasaurementQuality:];
-[NIFindingConfiguration initWithRole:discoveryToken:preferredUpdateRate:];
-[NIFindingConfiguration isCameraAssistanceInClientProcess];
-[NIFindingConfiguration preferredDiscoveryPriority];
-[NIFindingConfiguration requestedMeasurementQuality];
-[NIFindingConfiguration sessionDiscoveryToken];
-[NIFindingConfiguration setCameraAssistanceInClientProcess:];
-[NIFindingConfiguration setDebugParameters:];
-[NIFindingConfiguration setDiscoveryTokenVariant:];
-[NIFindingConfiguration setIsFinder:];
-[NIFindingConfiguration setPreferredDiscoveryPriority:];
-[NIFindingConfiguration setSpecifiedToken:];
-[NIFindingConfiguration specifiedToken];
```
