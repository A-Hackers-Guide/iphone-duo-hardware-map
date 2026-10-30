# `CAFSeat`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFAccessory`
- 0 instance variables, 9 properties, 13 instance methods, 2 class methods

## Properties

```
@property (T@"NSArray",R,N) seatBeltServices;
@property (T@"NSArray",R,N) heatingCoolingServices;
@property (T@"NSArray",R,N) fanServices;
@property (T@"NSArray",R,N) seatBelts;
@property (T@"NSDictionary",R,N) seatBeltsIndexed;
@property (T@"NSArray",R,N) heatingCoolings;
@property (T@"NSDictionary",R,N) heatingCoolingsIndexed;
@property (T@"NSArray",R,N) fans;
@property (T@"NSDictionary",R,N) fansIndexed;
```

## Class methods

```
+[CAFSeat accessoryIdentifier];
+[CAFSeat observerProtocol];
```

## Instance methods

```
-[CAFSeat removeObserver:];
-[CAFSeat addObserver:];
-[CAFSeat registerObserver:];
-[CAFSeat unregisterObserver:];
-[CAFSeat heatingCoolings];
-[CAFSeat fanServices];
-[CAFSeat fans];
-[CAFSeat fansIndexed];
-[CAFSeat heatingCoolingServices];
-[CAFSeat heatingCoolingsIndexed];
-[CAFSeat seatBeltServices];
-[CAFSeat seatBelts];
-[CAFSeat seatBeltsIndexed];
```
