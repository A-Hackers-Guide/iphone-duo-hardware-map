# `LACDTOFeatureRequirementQuery`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 5 properties, 12 instance methods, 3 class methods

## Instance variables

```
Q mask;
@"NSXPCConnection" connection;
B bypassEntitlements;
```

## Properties

```
@property (TQ,N,Vmask) mask;
@property (T@"NSXPCConnection",N,&,Vconnection) connection;
@property (TB,N,VbypassEntitlements) bypassEntitlements;
@property (T@"NSString",N,R) description;
@property (Tq,N,R) hash;
```

## Class methods

```
+[LACDTOFeatureRequirementQuery requirementsForAutoEnablementCheck];
+[LACDTOFeatureRequirementQuery requirementsForAvailableCheckWithConnection:];
+[LACDTOFeatureRequirementQuery requirementsForSupportedCheckWithConnection:];
```

## Instance methods

```
-[LACDTOFeatureRequirementQuery init];
-[LACDTOFeatureRequirementQuery mask];
-[LACDTOFeatureRequirementQuery setMask:];
-[LACDTOFeatureRequirementQuery connection];
-[LACDTOFeatureRequirementQuery hash];
-[LACDTOFeatureRequirementQuery setConnection:];
-[LACDTOFeatureRequirementQuery description];
-[LACDTOFeatureRequirementQuery isEqual:];
-[LACDTOFeatureRequirementQuery bypassEntitlements];
-[LACDTOFeatureRequirementQuery initWithMask:connection:];
-[LACDTOFeatureRequirementQuery initWithMask:connection:bypassEntitlements:];
-[LACDTOFeatureRequirementQuery setBypassEntitlements:];
```
