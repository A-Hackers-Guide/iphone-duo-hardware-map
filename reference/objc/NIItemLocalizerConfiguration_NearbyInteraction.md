# `NIItemLocalizerConfiguration`

- Image: [`/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`](../userland/System__Library__Frameworks__NearbyInteraction.framework__NearbyInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NIConfiguration`
- 5 instance variables, 5 properties, 20 instance methods, 1 class methods

## Instance variables

```
B _cameraAssistanceEnabled;
@"NSUUID" _itemUUID;
@"NIDiscoveryToken" _discoveryToken;
q _preferredUpdateRate;
@"NSDictionary" _debugParameters;
```

## Properties

```
@property (T@"NSUUID",C,N,V_itemUUID) itemUUID;
@property (T@"NIDiscoveryToken",C,N,V_discoveryToken) discoveryToken;
@property (T@"NSDictionary",C,N,V_debugParameters) debugParameters;
@property (Tq,N,V_preferredUpdateRate) preferredUpdateRate;
@property (TB,N,GisCameraAssistanceEnabled,V_cameraAssistanceEnabled) cameraAssistanceEnabled;
```

## Class methods

```
+[NIItemLocalizerConfiguration supportsSecureCoding];
```

## Instance methods

```
-[NIItemLocalizerConfiguration setCameraAssistanceEnabled:];
-[NIItemLocalizerConfiguration preferredUpdateRate];
-[NIItemLocalizerConfiguration descriptionInternal];
-[NIItemLocalizerConfiguration canUpdateToConfiguration:];
-[NIItemLocalizerConfiguration setPreferredUpdateRate:];
-[NIItemLocalizerConfiguration encodeWithCoder:];
-[NIItemLocalizerConfiguration _internalIsCameraAssistanceEnabled];
-[NIItemLocalizerConfiguration hash];
-[NIItemLocalizerConfiguration isCameraAssistanceEnabled];
-[NIItemLocalizerConfiguration description];
-[NIItemLocalizerConfiguration initWithCoder:];
-[NIItemLocalizerConfiguration copyWithZone:];
-[NIItemLocalizerConfiguration isEqual:];
-[NIItemLocalizerConfiguration itemUUID];
-[NIItemLocalizerConfiguration debugParameters];
-[NIItemLocalizerConfiguration discoveryToken];
-[NIItemLocalizerConfiguration initWithItemUUID:preferredUpdateRate:];
-[NIItemLocalizerConfiguration setDebugParameters:];
-[NIItemLocalizerConfiguration setDiscoveryToken:];
-[NIItemLocalizerConfiguration setItemUUID:];
```
