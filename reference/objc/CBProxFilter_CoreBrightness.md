# `CBProxFilter`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBFilter`
- Protocols: `CBCoexFilter`
- 6 instance variables, 8 properties, 15 instance methods, 0 class methods

## Instance variables

```
f _proxReleaseTime;
f _proxTriggerDelay;
q _proxState;
@"<CBALSNodeProtocol>" _alsNode;
B _isActive;
@"<CBProxNodeProtocol>" _source;
```

## Properties

```
@property (TB,N,V_isActive) isActive;
@property (Tq) proxState;
@property (T@"<CBProxNodeProtocol>",R,N,V_source) source;
@property (TQ,R,N) coexState;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CBProxFilter setIsActive:];
-[CBProxFilter setProperty:forKey:];
-[CBProxFilter dealloc];
-[CBProxFilter filterEvent:];
-[CBProxFilter handleALSEvent:];
-[CBProxFilter isActive];
-[CBProxFilter source];
-[CBProxFilter coexState];
-[CBProxFilter handleProximityEvent:];
-[CBProxFilter handleSourceEvent:];
-[CBProxFilter initWithALSNode:source:andLogCategory:];
-[CBProxFilter isObstructed];
-[CBProxFilter isObstructedAndActive];
-[CBProxFilter proxState];
-[CBProxFilter setProxState:];
```
