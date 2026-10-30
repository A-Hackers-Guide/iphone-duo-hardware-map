# `CTSMSSendInfoType`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 4 instance variables, 4 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"NSNumber" _error1;
@"NSNumber" _error2;
q _statusType;
@"NSNumber" _recommendedRetryDelayInSeconds;
```

## Properties

```
@property (T@"NSNumber",&,N,V_error1) error1;
@property (T@"NSNumber",&,N,V_error2) error2;
@property (Tq,N,V_statusType) statusType;
@property (T@"NSNumber",&,N,V_recommendedRetryDelayInSeconds) recommendedRetryDelayInSeconds;
```

## Class methods

```
+[CTSMSSendInfoType supportsSecureCoding];
```

## Instance methods

```
-[CTSMSSendInfoType init];
-[CTSMSSendInfoType encodeWithCoder:];
-[CTSMSSendInfoType initWithCoder:];
-[CTSMSSendInfoType statusType];
-[CTSMSSendInfoType copyWithZone:];
-[CTSMSSendInfoType isEqual:];
-[CTSMSSendInfoType error1];
-[CTSMSSendInfoType error2];
-[CTSMSSendInfoType initWithStatusType:error1:error2:delay:];
-[CTSMSSendInfoType recommendedRetryDelayInSeconds];
-[CTSMSSendInfoType setError1:];
-[CTSMSSendInfoType setError2:];
-[CTSMSSendInfoType setRecommendedRetryDelayInSeconds:];
-[CTSMSSendInfoType setStatusType:];
```
