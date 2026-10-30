# `_UISTouchAuthenticationRecord`

- Image: [`/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices`](../userland/System__Library__PrivateFrameworks__UIKitServices.framework__UIKitServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreamable`, `NSCopying`
- 10 instance variables, 13 properties, 17 instance methods, 3 class methods

## Instance variables

```
@"BKSWindowServerHitTestSecurityAnalysis" _securityAnalysis;
@"NSString" _hostBundleId;
@"NSString" _hostSDKVersion;
B _hostIsInternal;
@"NSString" _serviceBundleId;
q _serviceInstanceIdentifier;
Q _creationTime;
B _eventLeadToSensitiveDataTransmission;
B _passesSecurityAnalysis;
B _shouldAllowEvents;
```

## Properties

```
@property (T@"BKSWindowServerHitTestSecurityAnalysis",R,N) securityAnalysis;
@property (T@"NSString",R,C,N) hostBundleId;
@property (T@"NSString",R,C,N) hostSDKVersion;
@property (TB,R,N) hostIsInternal;
@property (T@"NSString",R,C,N) serviceBundleId;
@property (Tq,R,N) serviceInstanceIdentifier;
@property (TB,R,N,V_shouldAllowEvents) shouldAllowEvents;
@property (TB,N,V_eventLeadToSensitiveDataTransmission) eventLeadToSensitiveDataTransmission;
@property (TB,R,N) touchIsAuthentic;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UISTouchAuthenticationRecord build:];
+[_UISTouchAuthenticationRecord new];
+[_UISTouchAuthenticationRecord shouldAuthenticateServiceBundleId:];
```

## Instance methods

```
-[_UISTouchAuthenticationRecord init];
-[_UISTouchAuthenticationRecord appendDescriptionToFormatter:];
-[_UISTouchAuthenticationRecord securityAnalysis];
-[_UISTouchAuthenticationRecord hash];
-[_UISTouchAuthenticationRecord description];
-[_UISTouchAuthenticationRecord copyWithZone:];
-[_UISTouchAuthenticationRecord isEqual:];
-[_UISTouchAuthenticationRecord shouldAllowEvents];
-[_UISTouchAuthenticationRecord serviceBundleId];
-[_UISTouchAuthenticationRecord eventLeadToSensitiveDataTransmission];
-[_UISTouchAuthenticationRecord hostBundleId];
-[_UISTouchAuthenticationRecord hostIsInternal];
-[_UISTouchAuthenticationRecord hostSDKVersion];
-[_UISTouchAuthenticationRecord initWithSecurityAnalysis:timestamp:hostBundleId:hostSDKVersion:hostIsInternal:serviceBundleId:];
-[_UISTouchAuthenticationRecord serviceInstanceIdentifier];
-[_UISTouchAuthenticationRecord setEventLeadToSensitiveDataTransmission:];
-[_UISTouchAuthenticationRecord touchIsAuthentic];
```
