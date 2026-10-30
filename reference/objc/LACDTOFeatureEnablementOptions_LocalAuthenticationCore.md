# `LACDTOFeatureEnablementOptions`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCoding`
- 5 instance variables, 6 properties, 16 instance methods, 1 class methods

## Instance variables

```
B isGracePeriodEnabled;
B isStrictModeEnabled;
B isExtendedPolicyModeEnabled;
B isAutoEnablement;
q source;
```

## Properties

```
@property (TB,N,VisGracePeriodEnabled) isGracePeriodEnabled;
@property (TB,N,VisStrictModeEnabled) isStrictModeEnabled;
@property (TB,N,VisExtendedPolicyModeEnabled) isExtendedPolicyModeEnabled;
@property (TB,N,VisAutoEnablement) isAutoEnablement;
@property (Tq,N,Vsource) source;
@property (T@"NSString",N,R) description;
```

## Class methods

```
+[LACDTOFeatureEnablementOptions supportsSecureCoding];
```

## Instance methods

```
-[LACDTOFeatureEnablementOptions initWithSource:];
-[LACDTOFeatureEnablementOptions isStrictModeEnabled];
-[LACDTOFeatureEnablementOptions init];
-[LACDTOFeatureEnablementOptions setIsStrictModeEnabled:];
-[LACDTOFeatureEnablementOptions setSource:];
-[LACDTOFeatureEnablementOptions encodeWithCoder:];
-[LACDTOFeatureEnablementOptions description];
-[LACDTOFeatureEnablementOptions initWithCoder:];
-[LACDTOFeatureEnablementOptions isEqual:];
-[LACDTOFeatureEnablementOptions source];
-[LACDTOFeatureEnablementOptions setIsExtendedPolicyModeEnabled:];
-[LACDTOFeatureEnablementOptions isAutoEnablement];
-[LACDTOFeatureEnablementOptions isExtendedPolicyModeEnabled];
-[LACDTOFeatureEnablementOptions isGracePeriodEnabled];
-[LACDTOFeatureEnablementOptions setIsAutoEnablement:];
-[LACDTOFeatureEnablementOptions setIsGracePeriodEnabled:];
```
