# `ACCNavigationAccessory`

- Image: [`/System/Library/PrivateFrameworks/AccessoryNavigation.framework/AccessoryNavigation`](../userland/System__Library__PrivateFrameworks__AccessoryNavigation.framework__AccessoryNavigation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 5 properties, 27 instance methods, 0 class methods

## Instance variables

```
@"ACCNavigationProvider" _provider;
@"NSString" _accessoryUID;
@"NSMutableDictionary" _componentListInternal;
@"NSMutableDictionary" _objectDetectionComponentListInternal;
```

## Properties

```
@property (T@"NSMutableDictionary",&,V_componentListInternal) componentListInternal;
@property (T@"NSMutableDictionary",&,V_objectDetectionComponentListInternal) objectDetectionComponentListInternal;
@property (T@"ACCNavigationProvider",R,W,N,V_provider) provider;
@property (T@"NSString",&,N,V_accessoryUID) accessoryUID;
@property (T@"NSDictionary",R) componentList;
```

## Instance methods

```
-[ACCNavigationAccessory provider];
-[ACCNavigationAccessory hash];
-[ACCNavigationAccessory description];
-[ACCNavigationAccessory isEqual:];
-[ACCNavigationAccessory accessoryUID];
-[ACCNavigationAccessory setAccessoryUID:];
-[ACCNavigationAccessory supportsExitInfoForAnyComponent];
-[ACCNavigationAccessory componentIdListIsEnabled:];
-[ACCNavigationAccessory componentList];
-[ACCNavigationAccessory componentListForIdList:];
-[ACCNavigationAccessory componentListInternal];
-[ACCNavigationAccessory initWithAccessoryUID:provider:];
-[ACCNavigationAccessory iterateComponentIdList:block:];
-[ACCNavigationAccessory objectDetectionComponentIdListIsEnabled:];
-[ACCNavigationAccessory objectDetectionComponentList];
-[ACCNavigationAccessory objectDetectionComponentListForIdList:];
-[ACCNavigationAccessory objectDetectionComponentListInternal];
-[ACCNavigationAccessory requestedSourceNameForAnyComponent];
-[ACCNavigationAccessory requestedSourceSupportsRouteGuidanceForAnyComponent];
-[ACCNavigationAccessory setComponentListInternal:];
-[ACCNavigationAccessory setObjectDetectionComponentListInternal:];
-[ACCNavigationAccessory supportsLaneGuidanceForAnyComponent];
-[ACCNavigationAccessory supportsPreconditioningForAnyComponent];
-[ACCNavigationAccessory supportsTimeZoneOffsetForAnyComponent];
-[ACCNavigationAccessory updateLaneGuidanceInfo:componentList:];
-[ACCNavigationAccessory updateManeuverInfo:componentList:];
-[ACCNavigationAccessory updateRouteGuidanceInfo:componentList:];
```
