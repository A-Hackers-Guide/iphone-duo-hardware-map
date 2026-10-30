# `NIAcwgConfiguration`

- Image: [`/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`](../userland/System__Library__Frameworks__NearbyInteraction.framework__NearbyInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NIConfiguration`
- 4 instance variables, 4 properties, 16 instance methods, 1 class methods

## Instance variables

```
q _configurationTypeInternal;
S _lockBtConnHandle;
@"NSString" _lockIdentifier;
@"NSDictionary" _debugOptions;
```

## Properties

```
@property (Tq,R) configurationType;
@property (T@"NSString",C,V_lockIdentifier) lockIdentifier;
@property (TS,V_lockBtConnHandle) lockBtConnHandle;
@property (T@"NSDictionary",C,V_debugOptions) debugOptions;
```

## Class methods

```
+[NIAcwgConfiguration supportsSecureCoding];
```

## Instance methods

```
-[NIAcwgConfiguration descriptionInternal];
-[NIAcwgConfiguration debugOptions];
-[NIAcwgConfiguration initWithConfiguration:];
-[NIAcwgConfiguration configurationType];
-[NIAcwgConfiguration setDebugOptions:];
-[NIAcwgConfiguration encodeWithCoder:];
-[NIAcwgConfiguration hash];
-[NIAcwgConfiguration description];
-[NIAcwgConfiguration initWithCoder:];
-[NIAcwgConfiguration copyWithZone:];
-[NIAcwgConfiguration isEqual:];
-[NIAcwgConfiguration initWithLockIdentifier:];
-[NIAcwgConfiguration lockIdentifier];
-[NIAcwgConfiguration lockBtConnHandle];
-[NIAcwgConfiguration setLockBtConnHandle:];
-[NIAcwgConfiguration setLockIdentifier:];
```
