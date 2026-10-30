# `WFHealthUIEvent`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WFUIEvent`
- 1 instance variables, 6 properties, 5 instance methods, 4 class methods

## Instance variables

```
@"NSDictionary" _eventDictionary;
```

## Properties

```
@property (T@"NSString",R,N) eventName;
@property (T@"NSDictionary",R,N,V_eventDictionary) eventDictionary;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[WFHealthUIEvent detailEventWithIssues:ssid:securityType:];
+[WFHealthUIEvent noInternetEventWithTestTimes:didPassTest:failedVelocityTests:ssid:];
+[WFHealthUIEvent subtitleEventWithIssues:ssid:securityType:];
+[WFHealthUIEvent tapLinkEventWithIssues:ssid:securityType:];
```

## Instance methods

```
-[WFHealthUIEvent eventDictionary];
-[WFHealthUIEvent eventName];
-[WFHealthUIEvent _eventTypeStringForType:];
-[WFHealthUIEvent _issuesToJSONString:];
-[WFHealthUIEvent initWithEventType:issues:ssid:securityType:testTimes:didPassTest:failedTests:];
```
