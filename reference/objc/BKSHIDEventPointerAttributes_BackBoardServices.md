# `BKSHIDEventPointerAttributes`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BKSHIDEventDigitizerAttributes`
- 9 instance variables, 14 properties, 31 instance methods, 2 class methods

## Instance variables

```
C _pointerEdgeMask;
S _teleportState;
q _contextMove;
q _contextType;
@"NSArray" _hitTestContexts;
q _fingerDownCount;
@"BKSWindowServerHitTestSecurityAnalysis" _hitTestSecurityAnalysis;
{CGPoint="x"d"y"d} _unacceleratedRelativePosition;
{CGPoint="x"d"y"d} _acceleratedRelativePosition;
```

## Properties

```
@property (Tq,N,V_contextMove) contextMove;
@property (Tq,N,V_contextType) contextType;
@property (TS,D,N) pointerState;
@property (T@"NSArray",C,N,V_hitTestContexts) hitTestContexts;
@property (T{CGPoint=dd},N,V_unacceleratedRelativePosition) unacceleratedRelativePosition;
@property (T{CGPoint=dd},N,V_acceleratedRelativePosition) acceleratedRelativePosition;
@property (Td,D,N) unacceleratedRelativePositionX;
@property (Td,D,N) unacceleratedRelativePositionY;
@property (Td,D,N) acceleratedRelativePositionX;
@property (Td,D,N) acceleratedRelativePositionY;
@property (Tq,N,V_fingerDownCount) fingerDownCount;
@property (TC,N,V_pointerEdgeMask) pointerEdgeMask;
@property (TS,N,V_teleportState) teleportState;
@property (T@"BKSWindowServerHitTestSecurityAnalysis",&,N,V_hitTestSecurityAnalysis) hitTestSecurityAnalysis;
```

## Class methods

```
+[BKSHIDEventPointerAttributes protobufSchema];
+[BKSHIDEventPointerAttributes _eventAttributeType];
```

## Instance methods

```
-[BKSHIDEventPointerAttributes pointerState];
-[BKSHIDEventPointerAttributes unacceleratedRelativePositionY];
-[BKSHIDEventPointerAttributes contextType];
-[BKSHIDEventPointerAttributes unacceleratedRelativePosition];
-[BKSHIDEventPointerAttributes setUnacceleratedRelativePositionY:];
-[BKSHIDEventPointerAttributes setAcceleratedRelativePositionX:];
-[BKSHIDEventPointerAttributes setUnacceleratedRelativePosition:];
-[BKSHIDEventPointerAttributes setContextType:];
-[BKSHIDEventPointerAttributes appendDescriptionToFormatter:];
-[BKSHIDEventPointerAttributes setContextMove:];
-[BKSHIDEventPointerAttributes acceleratedRelativePosition];
-[BKSHIDEventPointerAttributes pointerEdgeMask];
-[BKSHIDEventPointerAttributes contextMove];
-[BKSHIDEventPointerAttributes setUnacceleratedRelativePositionX:];
-[BKSHIDEventPointerAttributes setHitTestContexts:];
-[BKSHIDEventPointerAttributes hitTestSecurityAnalysis];
-[BKSHIDEventPointerAttributes teleportState];
-[BKSHIDEventPointerAttributes setTeleportState:];
-[BKSHIDEventPointerAttributes hitTestContexts];
-[BKSHIDEventPointerAttributes setAcceleratedRelativePosition:];
-[BKSHIDEventPointerAttributes acceleratedRelativePositionY];
-[BKSHIDEventPointerAttributes acceleratedRelativePositionX];
-[BKSHIDEventPointerAttributes setHitTestSecurityAnalysis:];
-[BKSHIDEventPointerAttributes setAcceleratedRelativePositionY:];
-[BKSHIDEventPointerAttributes copyWithZone:];
-[BKSHIDEventPointerAttributes unacceleratedRelativePositionX];
-[BKSHIDEventPointerAttributes isEqual:];
-[BKSHIDEventPointerAttributes setFingerDownCount:];
-[BKSHIDEventPointerAttributes setPointerState:];
-[BKSHIDEventPointerAttributes setPointerEdgeMask:];
-[BKSHIDEventPointerAttributes fingerDownCount];
```
