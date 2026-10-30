# `_SBDisplayConnectionDonationTimer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 8 instance variables, 4 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSTimer" _timer;
@"NSString" _uniqueId;
@"NSString" _deviceName;
@"NSString" _productName;
B _connect;
B _mirroring;
q _counter;
@? _handler;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_SBDisplayConnectionDonationTimer dealloc];
-[_SBDisplayConnectionDonationTimer invalidate];
-[_SBDisplayConnectionDonationTimer stateChanged];
-[_SBDisplayConnectionDonationTimer initWithUniqueId:deviceName:productName:connect:mirroring:handler:];
-[_SBDisplayConnectionDonationTimer resetTimerOnConnect:];
```
