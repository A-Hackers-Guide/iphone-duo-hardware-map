# `BKDirectTouchPerDisplayInfo`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`](../userland/System__Library__PrivateFrameworks__BackBoardHIDTouchEventProcessor.framework__BackBoardHIDTouchEventProcessor.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreamable`
- 6 instance variables, 5 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"BKSHIDEventDisplay" _display;
@"<BKDisplayRenderSpace>" _displayRenderSpace;
@"BKDigitizerTouchStreamAggregate" _touchStreams;
@"NSArray" _hitTestRegions;
@"NSMutableDictionary" _cachedServiceProperties;
@"NSMutableDictionary" _serviceToDigitizer;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V_serviceToDigitizer) serviceToDigitizer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BKDirectTouchPerDisplayInfo appendDescriptionToFormatter:];
-[BKDirectTouchPerDisplayInfo dealloc];
-[BKDirectTouchPerDisplayInfo serviceToDigitizer];
-[BKDirectTouchPerDisplayInfo setServiceToDigitizer:];
```
