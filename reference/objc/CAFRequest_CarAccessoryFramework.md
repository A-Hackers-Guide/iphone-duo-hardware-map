# `CAFRequest`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAFCacheableDescription`
- 3 instance variables, 8 properties, 8 instance methods, 2 class methods

## Instance variables

```
@"CAFCharacteristic" _characteristic;
@"CAFControl" _control;
@"CAFCachedDescription" _cachedDescription;
```

## Properties

```
@property (T@"CAFCachedDescription",R,N,V_cachedDescription) cachedDescription;
@property (T@"CAFCharacteristic",R,N,V_characteristic) characteristic;
@property (T@"CAFControl",R,N,V_control) control;
@property (T@"CAFRequestKey",R,N) requestKey;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CAFRequest requestWithCharacteristic:];
+[CAFRequest requestWithControl:];
```

## Instance methods

```
-[CAFRequest cachedDescription];
-[CAFRequest requestKey];
-[CAFRequest description];
-[CAFRequest control];
-[CAFRequest characteristic];
-[CAFRequest initWithCharacteristic:];
-[CAFRequest initWithControl:];
-[CAFRequest currentDescriptionForCache:];
```
