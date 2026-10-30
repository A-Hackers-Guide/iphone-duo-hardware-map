# `WFDiagnosticsEvent`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WFUIEvent`
- 1 instance variables, 6 properties, 4 instance methods, 0 class methods

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

## Instance methods

```
-[WFDiagnosticsEvent eventDictionary];
-[WFDiagnosticsEvent eventName];
-[WFDiagnosticsEvent _testTypeToString:];
-[WFDiagnosticsEvent initWithDiagnosticsEventType:didPassTest:failedTests:];
```
