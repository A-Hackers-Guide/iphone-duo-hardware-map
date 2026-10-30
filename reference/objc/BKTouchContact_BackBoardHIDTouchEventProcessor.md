# `BKTouchContact`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`](../userland/System__Library__PrivateFrameworks__BackBoardHIDTouchEventProcessor.framework__BackBoardHIDTouchEventProcessor.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreamable`
- 29 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
q _pathIndex;
I _touchIdentifier;
I _userIdentifier;
I _slotID;
q _presence;
q _previousPresence;
q _hitTestPolicy;
q _hitTestContextCategory;
I _transducerType;
S _eventPhaseBits;
@"BKSHitTestRegion" _hitTestRegion;
q _hitTestRegionLocation;
{CGPoint="x"d"y"d} _normalLocation;
d _positionZ;
{CGPoint="x"d"y"d} _offset;
{BKPathZGradientInfo="previousTimestamp"d"previousQuality"d"zGradient"d} _zGradient;
{BKPointTriple="locationsAreValid"B"hitTestIsShifted"B"preciseLocationCalculated"B"location"{CGPoint="x"d"y"d}"hitTestLocation"{CGPoint="x"d"y"d}"preciseLocation"{CGPoint="x"d"y"d}} _denormalizedLocation;
@"BKSHIDTouchRoutingPolicy" _routingPolicy;
@"BKSHIDEventHitTestLayerInformation" _hitTestInformationAtDown;
@"BKSWindowServerHitTestSecurityAnalysis" _hitTestSecurityAnalysis;
@"NSMutableSet" _destinations;
@"NSArray" _hostingChain;
@"NSArray" _hitTestTargets;
@"NSArray" _hitTestPassthroughTargets;
B _touchDetached;
B _transferred;
B _tapToWake;
B _gestureCancelled;
B _appendAuthMessage;
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
-[BKTouchContact touchIdentifier];
-[BKTouchContact init];
-[BKTouchContact appendDescriptionToFormatter:];
-[BKTouchContact hash];
-[BKTouchContact description];
-[BKTouchContact isEqual:];
-[BKTouchContact pathIndex];
-[BKTouchContact denormalizedLocation];
-[BKTouchContact hitTestPassthroughTargets];
-[BKTouchContact hitTestTargets];
```
