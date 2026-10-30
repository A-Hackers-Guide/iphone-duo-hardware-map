# `WFInstantHotspotJoinEvent`

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
+[WFInstantHotspotJoinEvent joinEventWithType:latency:channel:error:];
```

## Instance methods

```
-[WFInstantHotspotJoinEvent eventDictionary];
-[WFInstantHotspotJoinEvent eventName];
-[WFInstantHotspotJoinEvent _bandGHzForChannel:];
-[WFInstantHotspotJoinEvent _eventTypeStringForType:];
-[WFInstantHotspotJoinEvent initWithType:latency:channel:error:];
```
