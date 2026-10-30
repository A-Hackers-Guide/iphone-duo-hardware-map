# `CWFAutoJoinUserActionMetric`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CWFJSONEncodable`, `NSCopying`, `NSSecureCoding`
- 10 instance variables, 21 properties, 34 instance methods, 1 class methods

## Instance variables

```
B _didUserJoinLowRSSINetwork;
B _didUserJoinPartiallyMatchedNetwork;
B _didUserJoinDisallowedNetwork;
B _didUserJoinKnownNetwork;
B _didUserJoinDeferredNetwork;
B _didUserJoinFailedToJoinNetwork;
@"CWFScanResult" _userJoinedNetwork;
@"NSDate" _userJoinedNetworkAt;
@"CWFScanResult" _autoJoinedNetwork;
@"NSDate" _autoJoinEndedAt;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"CWFScanResult",C,N,V_userJoinedNetwork) userJoinedNetwork;
@property (T@"NSDate",C,N,V_userJoinedNetworkAt) userJoinedNetworkAt;
@property (TB,N,V_didUserJoinLowRSSINetwork) didUserJoinLowRSSINetwork;
@property (TB,N,V_didUserJoinPartiallyMatchedNetwork) didUserJoinPartiallyMatchedNetwork;
@property (TB,N,V_didUserJoinDisallowedNetwork) didUserJoinDisallowedNetwork;
@property (TB,N,V_didUserJoinKnownNetwork) didUserJoinKnownNetwork;
@property (TB,N,V_didUserJoinDeferredNetwork) didUserJoinDeferredNetwork;
@property (TB,N,V_didUserJoinFailedToJoinNetwork) didUserJoinFailedToJoinNetwork;
@property (TB,R,D) didUserJoinDisabledNetwork;
@property (TB,R,D) didUserJoin6GHzOnlyNetwork;
@property (TB,R,D) didUserJoinStandalone6GHzNetwork;
@property (TB,R,D) didUserJoinLessPreferredNetwork;
@property (TQ,R,D) userJoinDelay;
@property (T@"CWFScanResult",C,N,V_autoJoinedNetwork) autoJoinedNetwork;
@property (T@"NSDate",C,N,V_autoJoinEndedAt) autoJoinEndedAt;
@property (T@"NSString",R) coreAnalyticsEventName;
@property (T@"NSDictionary",R) coreAnalyticsEventPayload;
```

## Class methods

```
+[CWFAutoJoinUserActionMetric supportsSecureCoding];
```

## Instance methods

```
-[CWFAutoJoinUserActionMetric autoJoinedNetwork];
-[CWFAutoJoinUserActionMetric JSONCompatibleKeyValueMap];
-[CWFAutoJoinUserActionMetric coreAnalyticsEventPayload];
-[CWFAutoJoinUserActionMetric coreAnalyticsEventName];
-[CWFAutoJoinUserActionMetric setAutoJoinedNetwork:];
-[CWFAutoJoinUserActionMetric encodeWithCoder:];
-[CWFAutoJoinUserActionMetric hash];
-[CWFAutoJoinUserActionMetric initWithCoder:];
-[CWFAutoJoinUserActionMetric copyWithZone:];
-[CWFAutoJoinUserActionMetric isEqual:];
-[CWFAutoJoinUserActionMetric autoJoinEndedAt];
-[CWFAutoJoinUserActionMetric didUserJoinLessPreferredNetwork];
-[CWFAutoJoinUserActionMetric didUserJoin6GHzOnlyNetwork];
-[CWFAutoJoinUserActionMetric didUserJoinDeferredNetwork];
-[CWFAutoJoinUserActionMetric didUserJoinDisabledNetwork];
-[CWFAutoJoinUserActionMetric didUserJoinDisallowedNetwork];
-[CWFAutoJoinUserActionMetric didUserJoinFailedToJoinNetwork];
-[CWFAutoJoinUserActionMetric didUserJoinKnownNetwork];
-[CWFAutoJoinUserActionMetric didUserJoinLowRSSINetwork];
-[CWFAutoJoinUserActionMetric didUserJoinPartiallyMatchedNetwork];
-[CWFAutoJoinUserActionMetric didUserJoinStandalone6GHzNetwork];
-[CWFAutoJoinUserActionMetric isEqualToAutoJoinUserActionMetric:];
-[CWFAutoJoinUserActionMetric setAutoJoinEndedAt:];
-[CWFAutoJoinUserActionMetric setDidUserJoinDeferredNetwork:];
-[CWFAutoJoinUserActionMetric setDidUserJoinDisallowedNetwork:];
-[CWFAutoJoinUserActionMetric setDidUserJoinFailedToJoinNetwork:];
-[CWFAutoJoinUserActionMetric setDidUserJoinKnownNetwork:];
-[CWFAutoJoinUserActionMetric setDidUserJoinLowRSSINetwork:];
-[CWFAutoJoinUserActionMetric setDidUserJoinPartiallyMatchedNetwork:];
-[CWFAutoJoinUserActionMetric setUserJoinedNetwork:];
-[CWFAutoJoinUserActionMetric setUserJoinedNetworkAt:];
-[CWFAutoJoinUserActionMetric userJoinDelay];
-[CWFAutoJoinUserActionMetric userJoinedNetwork];
-[CWFAutoJoinUserActionMetric userJoinedNetworkAt];
```
