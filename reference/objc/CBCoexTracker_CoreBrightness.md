# `CBCoexTracker`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 0 properties, 17 instance methods, 1 class methods

## Instance variables

```
logCategory;
displayId;
_log;
coexServices;
alses;
```

## Class methods

```
+[CBCoexTracker coexDescription:];
```

## Instance methods

```
-[CBCoexTracker addHIDServiceClient:];
-[CBCoexTracker removeHIDServiceClient:];
-[CBCoexTracker init];
-[CBCoexTracker handleALSEvent:];
-[CBCoexTracker addCoexSource:];
-[CBCoexTracker addEventService:];
-[CBCoexTracker coexStateForALS:];
-[CBCoexTracker handleCoexEvent:];
-[CBCoexTracker hasAnyCoexForALS:type:];
-[CBCoexTracker hasCoexForALS:type:];
-[CBCoexTracker initWithLogCategory:displayId:];
-[CBCoexTracker isProxOccludedForALS:];
-[CBCoexTracker isTouchOccludedForALS:];
-[CBCoexTracker nodeFromService:];
-[CBCoexTracker removeCoexSource:];
-[CBCoexTracker removeEventService:];
-[CBCoexTracker tryMakeFilterFor:with:];
```
