# `EventMO`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSManagedObject`
- 0 instance variables, 21 properties, 2 instance methods, 3 class methods

## Properties

```
@property (Ts,D,N) band;
@property (Ts,D,N) channel;
@property (Ts,D,N) channelWidth;
@property (T@"NSDate",C,D,N) date;
@property (T@"NSObject",&,D,N) historyBcnPer;
@property (T@"NSObject",&,D,N) historyBcnSched;
@property (T@"NSObject",&,D,N) historyCca;
@property (T@"NSObject",&,D,N) historyFwTxFrames;
@property (T@"NSObject",&,D,N) historyFwTxPer;
@property (T@"NSObject",&,D,N) historyRssi;
@property (T@"NSObject",&,D,N) historySnr;
@property (T@"NSObject",&,D,N) historyTxFrames;
@property (T@"NSObject",&,D,N) historyTxPer;
@property (Ts,D,N) motionState;
@property (Ti,D,N) reason;
@property (Ts,D,N) rssi;
@property (Ti,D,N) status;
@property (Ti,D,N) subReason;
@property (T@"BSSMO",&,D,N) bss;
@property (T@"LANMO",&,D,N) lan;
@property (T@"NetworkMO",&,D,N) network;
```

## Class methods

```
+[EventMO fetchRequest];
+[EventMO datedProperty];
+[EventMO unusedSuperEntityProperties];
```

## Instance methods

```
-[EventMO description];
-[EventMO attributeDescription:];
```
