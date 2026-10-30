# `TPSSubscriptionLabel`

- Image: [`/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences`](../userland/System__Library__PrivateFrameworks__TelephonyPreferences.framework__TelephonyPreferences.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"NSString" _localizedBadgeLabel;
@"NSString" _localizedLongLabel;
@"NSString" _unlocalizedLongLabel;
```

## Properties

```
@property (T@"NSString",R,N,V_localizedBadgeLabel) localizedBadgeLabel;
@property (T@"NSString",R,N,V_localizedLongLabel) localizedLongLabel;
@property (T@"NSString",R,N,V_unlocalizedLongLabel) unlocalizedLongLabel;
```

## Class methods

```
+[TPSSubscriptionLabel labelsFromUnlocalizedLabels:localizedLongLabels:localizedBadgeLabels:];
```

## Instance methods

```
-[TPSSubscriptionLabel hash];
-[TPSSubscriptionLabel description];
-[TPSSubscriptionLabel isEqual:];
-[TPSSubscriptionLabel localizedBadgeLabel];
-[TPSSubscriptionLabel initWithUnlocalizedLabel:localizedLongLabel:localizedBadgeLabel:];
-[TPSSubscriptionLabel isEqualToSubscriptionLabel:];
-[TPSSubscriptionLabel localizedLongLabel];
-[TPSSubscriptionLabel unlocalizedLongLabel];
```
