# `TPSPreferences`

- Image: [`/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences`](../userland/System__Library__PrivateFrameworks__TelephonyPreferences.framework__TelephonyPreferences.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 2 properties, 17 instance methods, 1 class methods

## Instance variables

```
@"NSString" _domain;
```

## Properties

```
@property (T@"NSString",R,C,N,V_domain) domain;
@property (TB,R,N) showSubscriptionList;
```

## Class methods

```
+[TPSPreferences sharedInstance];
```

## Instance methods

```
-[TPSPreferences integerForKey:defaultValue:];
-[TPSPreferences domain];
-[TPSPreferences boolForKey:defaultValue:];
-[TPSPreferences init];
-[TPSPreferences setString:forKey:];
-[TPSPreferences stringForKey:defaultValue:];
-[TPSPreferences setBool:forKey:];
-[TPSPreferences setPreferencesValue:forKey:];
-[TPSPreferences setInteger:forKey:];
-[TPSPreferences setNumber:forKey:];
-[TPSPreferences preferencesValueForKey:];
-[TPSPreferences numberForKey:defaultValue:];
-[TPSPreferences setPreferencesValue:forKey:domain:];
-[TPSPreferences preferencesValueForKey:domain:];
-[TPSPreferences setUnsignedInteger:forKey:];
-[TPSPreferences showSubscriptionList];
-[TPSPreferences unsignedIntegerForKey:defaultValue:];
```
