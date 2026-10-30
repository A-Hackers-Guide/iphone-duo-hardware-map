# `NISpatialBrowsingConfiguration`

- Image: [`/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`](../userland/System__Library__Frameworks__NearbyInteraction.framework__NearbyInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NIConfiguration`
- 4 instance variables, 4 properties, 16 instance methods, 3 class methods

## Instance variables

```
B _responder;
q _updatesPolicy;
@"NSString" _deviceIdentifier;
d _maxNearbyObjectAge;
```

## Properties

```
@property (Tq,V_updatesPolicy) updatesPolicy;
@property (TB,GisResponder,V_responder) responder;
@property (T@"NSString",C,V_deviceIdentifier) deviceIdentifier;
@property (Td,V_maxNearbyObjectAge) maxNearbyObjectAge;
```

## Class methods

```
+[NISpatialBrowsingConfiguration supportsSecureCoding];
+[NISpatialBrowsingConfiguration new];
+[NISpatialBrowsingConfiguration responderConfigurationWithIdentifier:];
```

## Instance methods

```
-[NISpatialBrowsingConfiguration setDeviceIdentifier:];
-[NISpatialBrowsingConfiguration init];
-[NISpatialBrowsingConfiguration descriptionInternal];
-[NISpatialBrowsingConfiguration setResponder:];
-[NISpatialBrowsingConfiguration deviceIdentifier];
-[NISpatialBrowsingConfiguration encodeWithCoder:];
-[NISpatialBrowsingConfiguration hash];
-[NISpatialBrowsingConfiguration description];
-[NISpatialBrowsingConfiguration initWithCoder:];
-[NISpatialBrowsingConfiguration copyWithZone:];
-[NISpatialBrowsingConfiguration isEqual:];
-[NISpatialBrowsingConfiguration isResponder];
-[NISpatialBrowsingConfiguration maxNearbyObjectAge];
-[NISpatialBrowsingConfiguration setMaxNearbyObjectAge:];
-[NISpatialBrowsingConfiguration setUpdatesPolicy:];
-[NISpatialBrowsingConfiguration updatesPolicy];
```
