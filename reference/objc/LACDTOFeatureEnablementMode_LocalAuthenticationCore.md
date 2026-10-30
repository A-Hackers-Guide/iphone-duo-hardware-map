# `LACDTOFeatureEnablementMode`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACDTOFeatureEnablementMode`
- 3 instance variables, 7 properties, 6 instance methods, 5 class methods

## Instance variables

```
B _isEnabled;
B _isGracePeriodEnabled;
C _rawValue;
```

## Properties

```
@property (TB,R,N,V_isEnabled) isEnabled;
@property (TB,R,N,V_isGracePeriodEnabled) isGracePeriodEnabled;
@property (TC,R,N,V_rawValue) rawValue;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[LACDTOFeatureEnablementMode disabled];
+[LACDTOFeatureEnablementMode enabled];
+[LACDTOFeatureEnablementMode enabledWithGracePeriodUnlimited];
+[LACDTOFeatureEnablementMode disabledNotSet];
+[LACDTOFeatureEnablementMode enabledWithGracePeriod];
```

## Instance methods

```
-[LACDTOFeatureEnablementMode rawValue];
-[LACDTOFeatureEnablementMode isEnabled];
-[LACDTOFeatureEnablementMode description];
-[LACDTOFeatureEnablementMode isEqual:];
-[LACDTOFeatureEnablementMode isGracePeriodEnabled];
-[LACDTOFeatureEnablementMode initWithIsEnabled:isGracePeriodEnabled:rawValue:];
```
