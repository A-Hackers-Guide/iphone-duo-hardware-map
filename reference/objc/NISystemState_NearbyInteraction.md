# `NISystemState`

- Image: [`/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`](../userland/System__Library__Frameworks__NearbyInteraction.framework__NearbyInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 2 instance variables, 2 properties, 13 instance methods, 1 class methods

## Instance variables

```
Q _uwbPreciseDistanceAvailability;
Q _uwbExtendedDistanceAvailability;
```

## Properties

```
@property (TQ,N,V_uwbPreciseDistanceAvailability) uwbPreciseDistanceAvailability;
@property (TQ,N,V_uwbExtendedDistanceAvailability) uwbExtendedDistanceAvailability;
```

## Class methods

```
+[NISystemState supportsSecureCoding];
```

## Instance methods

```
-[NISystemState init];
-[NISystemState descriptionInternal];
-[NISystemState encodeWithCoder:];
-[NISystemState hash];
-[NISystemState description];
-[NISystemState initWithCoder:];
-[NISystemState copyWithZone:];
-[NISystemState isEqual:];
-[NISystemState uwbExtendedDistanceAvailability];
-[NISystemState initWithUWBPreciseDistanceAvailability:uwbExtendedDistanceAvailability:];
-[NISystemState setUwbExtendedDistanceAvailability:];
-[NISystemState setUwbPreciseDistanceAvailability:];
-[NISystemState uwbPreciseDistanceAvailability];
```
