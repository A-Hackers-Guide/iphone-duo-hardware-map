# `BLSXPCBacklightProxyObserverMask`

- Image: [`/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`](../userland/System__Library__PrivateFrameworks__BacklightServices.framework__BacklightServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`, `BSXPCCoding`
- 6 instance variables, 11 properties, 17 instance methods, 3 class methods

## Instance variables

```
B _observingDidCompleteUpdateToState;
B _observingEventsArray;
B _observingDidChangeAlwaysOnEnabled;
B _observingActivatingWithEvent;
B _observingDeactivatingWithEvent;
B _observingPerformingEvent;
```

## Properties

```
@property (TB,R,N,GisObservingDidCompleteUpdateToState,V_observingDidCompleteUpdateToState) observingDidCompleteUpdateToState;
@property (TB,R,N,GisObservingEventsArray,V_observingEventsArray) observingEventsArray;
@property (TB,R,N,GisObservingDidChangeAlwaysOnEnabled,V_observingDidChangeAlwaysOnEnabled) observingDidChangeAlwaysOnEnabled;
@property (TB,R,N,GisObservingActivatingWithEvent,V_observingActivatingWithEvent) observingActivatingWithEvent;
@property (TB,R,N,GisObservingDeactivatingWithEvent,V_observingDeactivatingWithEvent) observingDeactivatingWithEvent;
@property (TB,R,N,GisObservingPerformingEvent,V_observingPerformingEvent) observingPerformingEvent;
@property (TB,R,N,GisObserving) observing;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BLSXPCBacklightProxyObserverMask supportsSecureCoding];
+[BLSXPCBacklightProxyObserverMask maskForObservingDidCompleteUpdateToState:observingEventsArray:didChangeAlwaysOnEnabled:activatingWithEvent:deactivatingWithEvent:performingEvent:];
+[BLSXPCBacklightProxyObserverMask maskForObserver:];
```

## Instance methods

```
-[BLSXPCBacklightProxyObserverMask initWithXPCDictionary:];
-[BLSXPCBacklightProxyObserverMask isObserving];
-[BLSXPCBacklightProxyObserverMask encodeWithXPCDictionary:];
-[BLSXPCBacklightProxyObserverMask encodeWithCoder:];
-[BLSXPCBacklightProxyObserverMask initWithObserver:];
-[BLSXPCBacklightProxyObserverMask hash];
-[BLSXPCBacklightProxyObserverMask description];
-[BLSXPCBacklightProxyObserverMask initWithCoder:];
-[BLSXPCBacklightProxyObserverMask copyWithZone:];
-[BLSXPCBacklightProxyObserverMask isEqual:];
-[BLSXPCBacklightProxyObserverMask isObservingActivatingWithEvent];
-[BLSXPCBacklightProxyObserverMask isObservingDeactivatingWithEvent];
-[BLSXPCBacklightProxyObserverMask isObservingDidChangeAlwaysOnEnabled];
-[BLSXPCBacklightProxyObserverMask isObservingDidCompleteUpdateToState];
-[BLSXPCBacklightProxyObserverMask isObservingEventsArray];
-[BLSXPCBacklightProxyObserverMask isObservingPerformingEvent];
-[BLSXPCBacklightProxyObserverMask initWithObservingDidCompleteUpdateToState:observingEventsArray:didChangeAlwaysOnEnabled:activatingWithEvent:deactivatingWithEvent:performingEvent:];
```
