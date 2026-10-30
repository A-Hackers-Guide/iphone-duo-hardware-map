# `NIRegionPredicate`

- Image: [`/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`](../userland/System__Library__Frameworks__NearbyInteraction.framework__NearbyInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 7 instance variables, 6 properties, 28 instance methods, 2 class methods

## Instance variables

```
q _devicePresencePreset;
B _requiresUserIntent;
B _coarseEstimation;
f _radius;
@"NSString" _name;
q _regionSizeCategory;
q _preferredUpdateRate;
```

## Properties

```
@property (T@"NSString",R,V_name) name;
@property (Tq,V_regionSizeCategory) regionSizeCategory;
@property (Tf,R,V_radius) radius;
@property (Tq,V_preferredUpdateRate) preferredUpdateRate;
@property (TB,V_requiresUserIntent) requiresUserIntent;
@property (TB,V_coarseEstimation) coarseEstimation;
```

## Class methods

```
+[NIRegionPredicate supportsSecureCoding];
+[NIRegionPredicate _isExecuteRegion:];
```

## Instance methods

```
-[NIRegionPredicate regionSizeCategory];
-[NIRegionPredicate initWithName:radius:];
-[NIRegionPredicate preferredUpdateRate];
-[NIRegionPredicate descriptionInternal];
-[NIRegionPredicate initWithName:devicePresencePreset:];
-[NIRegionPredicate shortDescription];
-[NIRegionPredicate devicePresencePreset];
-[NIRegionPredicate initWithName:radius:preferredUpdateRate:];
-[NIRegionPredicate setCoarseEstimation:];
-[NIRegionPredicate setDevicePresencePreset:];
-[NIRegionPredicate initWithName:regionSizeCategory:radius:preferredUpdateRate:requiresUserIntent:coarseEstimation:devicePresencePreset:];
-[NIRegionPredicate radius];
-[NIRegionPredicate setPreferredUpdateRate:];
-[NIRegionPredicate initWithName:radius:preferredUpdateRate:requiresUserIntent:];
-[NIRegionPredicate encodeWithCoder:];
-[NIRegionPredicate setRegionSizeCategory:];
-[NIRegionPredicate requiresUserIntent];
-[NIRegionPredicate hash];
-[NIRegionPredicate description];
-[NIRegionPredicate initWithCoder:];
-[NIRegionPredicate initWithName:radius:preferredUpdateRate:requiresUserIntent:devicePresencePreset:];
-[NIRegionPredicate initWithName:regionSizeCategory:radius:preferredUpdateRate:requiresUserIntent:];
-[NIRegionPredicate copyWithZone:];
-[NIRegionPredicate coarseEstimation];
-[NIRegionPredicate isEqual:];
-[NIRegionPredicate name];
-[NIRegionPredicate initWithName:regionSizeCategory:radius:preferredUpdateRate:requiresUserIntent:devicePresencePreset:];
-[NIRegionPredicate setRequiresUserIntent:];
```
