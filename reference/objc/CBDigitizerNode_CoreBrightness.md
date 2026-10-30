# `CBDigitizerNode`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBHIDService`
- Protocols: `CBDigitizerNodeProtocol`
- 1 instance variables, 5 properties, 5 instance methods, 2 class methods

## Instance variables

```
Q _locationID;
```

## Properties

```
@property (TQ,R,N,V_locationID) locationID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CBDigitizerNode nodeForService:];
+[CBDigitizerNode matchingCriteria];
```

## Instance methods

```
-[CBDigitizerNode description];
-[CBDigitizerNode locationID];
-[CBDigitizerNode canPairWithALS:];
-[CBDigitizerNode initWithDigitizerServiceClient:];
-[CBDigitizerNode newFiltersForALS:logCategory:];
```
