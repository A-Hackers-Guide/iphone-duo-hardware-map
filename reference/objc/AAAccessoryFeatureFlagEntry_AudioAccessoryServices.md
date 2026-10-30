# `AAAccessoryFeatureFlagEntry`

- Image: [`/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`](../userland/System__Library__PrivateFrameworks__AudioAccessoryServices.framework__AudioAccessoryServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 4 properties, 10 instance methods, 1 class methods

## Instance variables

```
C _featureID;
C _coreID;
B _state;
@"NSData" _payload;
```

## Properties

```
@property (TC,R,N,V_featureID) featureID;
@property (TC,R,N,V_coreID) coreID;
@property (TB,R,N,V_state) state;
@property (T@"NSData",R,N,V_payload) payload;
```

## Class methods

```
+[AAAccessoryFeatureFlagEntry supportsSecureCoding];
```

## Instance methods

```
-[AAAccessoryFeatureFlagEntry messageSize];
-[AAAccessoryFeatureFlagEntry featureID];
-[AAAccessoryFeatureFlagEntry payload];
-[AAAccessoryFeatureFlagEntry encodeWithCoder:];
-[AAAccessoryFeatureFlagEntry description];
-[AAAccessoryFeatureFlagEntry initWithCoder:];
-[AAAccessoryFeatureFlagEntry state];
-[AAAccessoryFeatureFlagEntry coreID];
-[AAAccessoryFeatureFlagEntry appendMessageToBuffer:];
-[AAAccessoryFeatureFlagEntry initWithFeatureID:coreID:state:payload:];
```
