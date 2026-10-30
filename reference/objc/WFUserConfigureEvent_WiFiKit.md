# `WFUserConfigureEvent`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WFUIEvent`
- 1 instance variables, 6 properties, 5 instance methods, 1 class methods

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
+[WFUserConfigureEvent configureEventWithType:new:old:];
```

## Instance methods

```
-[WFUserConfigureEvent eventDictionary];
-[WFUserConfigureEvent eventName];
-[WFUserConfigureEvent _configureValueStringForType:];
-[WFUserConfigureEvent _eventTypeStringForType:];
-[WFUserConfigureEvent initWithType:new:old:];
```
