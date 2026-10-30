# `BKSHIDEventDeliveryChainObserver`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"BKSEventDeferringChainIdentity" _chainIdentity;
@"BKSHIDEventDisplay" _display;
@"BKSHIDEventDeferringEnvironment" _deferringEnvironment;
```

## Properties

```
@property (T@"BKSEventDeferringChainIdentity",R,N) chainIdentity;
@property (T@"BKSHIDEventDisplay",R,C,N,V_display) display;
@property (T@"BKSHIDEventDeferringEnvironment",R,C,N,V_deferringEnvironment) deferringEnvironment;
```

## Instance methods

```
-[BKSHIDEventDeliveryChainObserver deferringEnvironment];
-[BKSHIDEventDeliveryChainObserver display];
-[BKSHIDEventDeliveryChainObserver init];
-[BKSHIDEventDeliveryChainObserver chainIdentity];
-[BKSHIDEventDeliveryChainObserver addChainObserver:];
-[BKSHIDEventDeliveryChainObserver initWithDisplay:environment:];
```
