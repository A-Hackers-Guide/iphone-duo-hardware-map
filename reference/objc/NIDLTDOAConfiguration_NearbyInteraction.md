# `NIDLTDOAConfiguration`

- Image: [`/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`](../userland/System__Library__Frameworks__NearbyInteraction.framework__NearbyInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NIConfiguration`
- 4 instance variables, 4 properties, 19 instance methods, 1 class methods

## Instance variables

```
B _cameraAssistanceEnabled;
q _networkIdentifier;
q _discoveryMethod;
@"NSDictionary" _debugParameters;
```

## Properties

```
@property (T@"NSDictionary",C,V_debugParameters) debugParameters;
@property (TB,N,GisCameraAssistanceEnabled,V_cameraAssistanceEnabled) cameraAssistanceEnabled;
@property (Tq,N,V_networkIdentifier) networkIdentifier;
@property (Tq,N,V_discoveryMethod) discoveryMethod;
```

## Class methods

```
+[NIDLTDOAConfiguration supportsSecureCoding];
```

## Instance methods

```
-[NIDLTDOAConfiguration setCameraAssistanceEnabled:];
-[NIDLTDOAConfiguration descriptionInternal];
-[NIDLTDOAConfiguration encodeWithCoder:];
-[NIDLTDOAConfiguration _internalIsCameraAssistanceEnabled];
-[NIDLTDOAConfiguration hash];
-[NIDLTDOAConfiguration isCameraAssistanceEnabled];
-[NIDLTDOAConfiguration description];
-[NIDLTDOAConfiguration initWithCoder:];
-[NIDLTDOAConfiguration copyWithZone:];
-[NIDLTDOAConfiguration isEqual:];
-[NIDLTDOAConfiguration networkIdentifier];
-[NIDLTDOAConfiguration setNetworkIdentifier:];
-[NIDLTDOAConfiguration debugParameters];
-[NIDLTDOAConfiguration discoveryMethod];
-[NIDLTDOAConfiguration initWithConfigParametersOverride:];
-[NIDLTDOAConfiguration initWithNetworkIdentifier:];
-[NIDLTDOAConfiguration initWithNetworkIdentifier:discoveryMethod:];
-[NIDLTDOAConfiguration setDebugParameters:];
-[NIDLTDOAConfiguration setDiscoveryMethod:];
```
