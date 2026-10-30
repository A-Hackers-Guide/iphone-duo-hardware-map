# `CAFRequestKey`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAFCacheableDescription`, `NSCopying`
- 3 instance variables, 7 properties, 10 instance methods, 2 class methods

## Instance variables

```
@"NSNumber" _priority;
@"NSNumber" _pluginID;
@"CAFCachedDescription" _cachedDescription;
```

## Properties

```
@property (T@"CAFCachedDescription",R,N,V_cachedDescription) cachedDescription;
@property (T@"NSNumber",R,N,V_priority) priority;
@property (T@"NSNumber",R,N,V_pluginID) pluginID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CAFRequestKey requestKeyForCharacteristic:];
+[CAFRequestKey requestKeyForControl:];
```

## Instance methods

```
-[CAFRequestKey priority];
-[CAFRequestKey cachedDescription];
-[CAFRequestKey hash];
-[CAFRequestKey description];
-[CAFRequestKey copyWithZone:];
-[CAFRequestKey isEqual:];
-[CAFRequestKey copyWithPriority:];
-[CAFRequestKey currentDescriptionForCache:];
-[CAFRequestKey initWithPriority:pluginID:];
-[CAFRequestKey pluginID];
```
