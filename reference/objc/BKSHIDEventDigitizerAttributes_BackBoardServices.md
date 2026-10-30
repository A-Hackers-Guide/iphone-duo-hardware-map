# `BKSHIDEventDigitizerAttributes`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BKSHIDEventBaseAttributes`
- 10 instance variables, 12 properties, 27 instance methods, 2 class methods

## Instance variables

```
C _touchStreamIdentifier;
B _systemGesturesPossible;
B _systemGestureStateChange;
f _maximumForce;
d _maximumPositionZ;
@"NSArray" _pathAttributes;
d _initialTouchTimestamp;
q _activeModifiers;
q _sceneTouchBehavior;
{CGSize="width"d"height"d} _digitizerSurfaceSize;
```

## Properties

```
@property (Tf,N,V_maximumForce) maximumForce;
@property (Td,N,V_maximumPositionZ) maximumPositionZ;
@property (T{CGSize=dd},N,V_digitizerSurfaceSize) digitizerSurfaceSize;
@property (Td,D,N) digitizerSurfaceWidth;
@property (Td,D,N) digitizerSurfaceHeight;
@property (T@"NSArray",&,N,V_pathAttributes) pathAttributes;
@property (Td,N,V_initialTouchTimestamp) initialTouchTimestamp;
@property (Tq,N,V_activeModifiers) activeModifiers;
@property (TC,N,V_touchStreamIdentifier) touchStreamIdentifier;
@property (TB,N,V_systemGesturesPossible) systemGesturesPossible;
@property (TB,N,V_systemGestureStateChange) systemGestureStateChange;
@property (Tq,N,V_sceneTouchBehavior) sceneTouchBehavior;
```

## Class methods

```
+[BKSHIDEventDigitizerAttributes protobufSchema];
+[BKSHIDEventDigitizerAttributes _eventAttributeType];
```

## Instance methods

```
-[BKSHIDEventDigitizerAttributes maximumForce];
-[BKSHIDEventDigitizerAttributes sceneTouchBehavior];
-[BKSHIDEventDigitizerAttributes pathAttributes];
-[BKSHIDEventDigitizerAttributes setDigitizerSurfaceWidth:];
-[BKSHIDEventDigitizerAttributes maximumPositionZ];
-[BKSHIDEventDigitizerAttributes appendDescriptionToFormatter:];
-[BKSHIDEventDigitizerAttributes setMaximumForce:];
-[BKSHIDEventDigitizerAttributes digitizerSurfaceSize];
-[BKSHIDEventDigitizerAttributes systemGesturesPossible];
-[BKSHIDEventDigitizerAttributes setSceneTouchBehavior:];
-[BKSHIDEventDigitizerAttributes initialTouchTimestamp];
-[BKSHIDEventDigitizerAttributes setActiveModifiers:];
-[BKSHIDEventDigitizerAttributes touchStreamIdentifier];
-[BKSHIDEventDigitizerAttributes digitizerSurfaceHeight];
-[BKSHIDEventDigitizerAttributes setSystemGestureStateChange:];
-[BKSHIDEventDigitizerAttributes setSystemGesturesPossible:];
-[BKSHIDEventDigitizerAttributes setMaximumPositionZ:];
-[BKSHIDEventDigitizerAttributes setInitialTouchTimestamp:];
-[BKSHIDEventDigitizerAttributes setDigitizerSurfaceSize:];
-[BKSHIDEventDigitizerAttributes setTouchStreamIdentifier:];
-[BKSHIDEventDigitizerAttributes copyWithZone:];
-[BKSHIDEventDigitizerAttributes activeModifiers];
-[BKSHIDEventDigitizerAttributes isEqual:];
-[BKSHIDEventDigitizerAttributes systemGestureStateChange];
-[BKSHIDEventDigitizerAttributes digitizerSurfaceWidth];
-[BKSHIDEventDigitizerAttributes setDigitizerSurfaceHeight:];
-[BKSHIDEventDigitizerAttributes setPathAttributes:];
```
