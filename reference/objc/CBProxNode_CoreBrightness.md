# `CBProxNode`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBHIDService`
- Protocols: `CBProxNodeProtocol`
- 1 instance variables, 5 properties, 6 instance methods, 2 class methods

## Instance variables

```
I _placement;
```

## Properties

```
@property (TI,R,N,V_placement) placement;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CBProxNode nodeForService:];
+[CBProxNode matchingCriteria];
```

## Instance methods

```
-[CBProxNode placement];
-[CBProxNode description];
-[CBProxNode canPairWithALS:];
-[CBProxNode initProxProperties];
-[CBProxNode initWithProxServiceClient:];
-[CBProxNode newFiltersForALS:logCategory:];
```
