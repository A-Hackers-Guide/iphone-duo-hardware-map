# `ACCNavigationAccessoryComponent`

- Image: [`/System/Library/PrivateFrameworks/AccessoryNavigation.framework/AccessoryNavigation`](../userland/System__Library__PrivateFrameworks__AccessoryNavigation.framework__AccessoryNavigation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 16 instance variables, 16 properties, 37 instance methods, 1 class methods

## Instance variables

```
B _isEnabled;
B _requestSourceName;
B _requestSourceSupportsRouteGuidance;
B _supportsExitInfo;
B _supportsLaneGuidance;
B _supportsTimeZoneOffset;
B _supportsPreconditioning;
Q _identifier;
@"NSString" _name;
Q _maxLength_CurrentRoadName;
Q _maxLength_DestinationRoadName;
Q _maxLength_PostManeuverRoadName;
Q _maxLength_ManeuverDescription;
Q _maxLength_LaneGuidanceDescription;
Q _maxCapacity_GuidanceManeuver;
Q _maxCapacity_LaneGuidance;
```

## Properties

```
@property (TQ,N,V_identifier) identifier;
@property (T@"NSString",&,V_name) name;
@property (TB,N,V_isEnabled) isEnabled;
@property (TQ,N,V_maxLength_CurrentRoadName) maxLength_CurrentRoadName;
@property (TQ,N,V_maxLength_DestinationRoadName) maxLength_DestinationRoadName;
@property (TQ,N,V_maxLength_PostManeuverRoadName) maxLength_PostManeuverRoadName;
@property (TQ,N,V_maxLength_ManeuverDescription) maxLength_ManeuverDescription;
@property (TQ,N,V_maxLength_LaneGuidanceDescription) maxLength_LaneGuidanceDescription;
@property (TB,N,V_requestSourceName) requestSourceName;
@property (TB,N,V_requestSourceSupportsRouteGuidance) requestSourceSupportsRouteGuidance;
@property (TB,N,V_supportsExitInfo) supportsExitInfo;
@property (TB,N,V_supportsLaneGuidance) supportsLaneGuidance;
@property (TB,N,V_supportsTimeZoneOffset) supportsTimeZoneOffset;
@property (TB,N,V_supportsPreconditioning) supportsPreconditioning;
@property (TQ,N,V_maxCapacity_GuidanceManeuver) maxCapacity_GuidanceManeuver;
@property (TQ,N,V_maxCapacity_LaneGuidance) maxCapacity_LaneGuidance;
```

## Class methods

```
+[ACCNavigationAccessoryComponent supportsSecureCoding];
```

## Instance methods

```
-[ACCNavigationAccessoryComponent identifier];
-[ACCNavigationAccessoryComponent setIsEnabled:];
-[ACCNavigationAccessoryComponent isEnabled];
-[ACCNavigationAccessoryComponent setIdentifier:];
-[ACCNavigationAccessoryComponent encodeWithCoder:];
-[ACCNavigationAccessoryComponent hash];
-[ACCNavigationAccessoryComponent description];
-[ACCNavigationAccessoryComponent setName:];
-[ACCNavigationAccessoryComponent initWithCoder:];
-[ACCNavigationAccessoryComponent isEqual:];
-[ACCNavigationAccessoryComponent name];
-[ACCNavigationAccessoryComponent maxCapacity_GuidanceManeuver];
-[ACCNavigationAccessoryComponent maxCapacity_LaneGuidance];
-[ACCNavigationAccessoryComponent maxLength_CurrentRoadName];
-[ACCNavigationAccessoryComponent maxLength_DestinationRoadName];
-[ACCNavigationAccessoryComponent maxLength_LaneGuidanceDescription];
-[ACCNavigationAccessoryComponent maxLength_ManeuverDescription];
-[ACCNavigationAccessoryComponent maxLength_PostManeuverRoadName];
-[ACCNavigationAccessoryComponent requestSourceName];
-[ACCNavigationAccessoryComponent requestSourceSupportsRouteGuidance];
-[ACCNavigationAccessoryComponent setMaxCapacity_GuidanceManeuver:];
-[ACCNavigationAccessoryComponent setMaxCapacity_LaneGuidance:];
-[ACCNavigationAccessoryComponent setMaxLength_CurrentRoadName:];
-[ACCNavigationAccessoryComponent setMaxLength_DestinationRoadName:];
-[ACCNavigationAccessoryComponent setMaxLength_LaneGuidanceDescription:];
-[ACCNavigationAccessoryComponent setMaxLength_ManeuverDescription:];
-[ACCNavigationAccessoryComponent setMaxLength_PostManeuverRoadName:];
-[ACCNavigationAccessoryComponent setRequestSourceName:];
-[ACCNavigationAccessoryComponent setRequestSourceSupportsRouteGuidance:];
-[ACCNavigationAccessoryComponent setSupportsExitInfo:];
-[ACCNavigationAccessoryComponent setSupportsLaneGuidance:];
-[ACCNavigationAccessoryComponent setSupportsPreconditioning:];
-[ACCNavigationAccessoryComponent setSupportsTimeZoneOffset:];
-[ACCNavigationAccessoryComponent supportsExitInfo];
-[ACCNavigationAccessoryComponent supportsLaneGuidance];
-[ACCNavigationAccessoryComponent supportsPreconditioning];
-[ACCNavigationAccessoryComponent supportsTimeZoneOffset];
```
