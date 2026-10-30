# `WiFiUsageSessionCAConfig`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 7 instance methods, 0 class methods

## Instance variables

```
Q _ca_sampling;
d _ca_minTimeIntervalBetweenSubmissions;
@"NSDate" _ca_lastSubmission;
```

## Properties

```
@property (TQ,R,N,V_ca_sampling) ca_sampling;
@property (Td,R,N,V_ca_minTimeIntervalBetweenSubmissions) ca_minTimeIntervalBetweenSubmissions;
@property (T@"NSDate",R,N,V_ca_lastSubmission) ca_lastSubmission;
```

## Instance methods

```
-[WiFiUsageSessionCAConfig description];
-[WiFiUsageSessionCAConfig countSubmission];
-[WiFiUsageSessionCAConfig ca_lastSubmission];
-[WiFiUsageSessionCAConfig ca_minTimeIntervalBetweenSubmissions];
-[WiFiUsageSessionCAConfig ca_sampling];
-[WiFiUsageSessionCAConfig canSubmit];
-[WiFiUsageSessionCAConfig initWithSampling:minInterval:];
```
