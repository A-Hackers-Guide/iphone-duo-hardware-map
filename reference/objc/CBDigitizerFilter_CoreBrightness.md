# `CBDigitizerFilter`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBFilter`
- Protocols: `CBCoexFilter`
- 8 instance variables, 8 properties, 21 instance methods, 1 class methods

## Instance variables

```
B _firstDigitizerEvent;
{CBDigitizerFilterTouchProperties="digitizerWidth"f"digitizerHeight"f"deviceCenterX"f"deviceCenterY"f"touchHotSpotSquared"f} _props;
q _behavior;
@"CBDigitizerHotspot" _hotspot;
^{__IOHIDServiceClient=} _sourceService;
B _isActive;
i _orientation;
@"<CBDigitizerNodeProtocol>" _source;
```

## Properties

```
@property (Ti,R,N,V_orientation) orientation;
@property (TB,N,V_isActive) isActive;
@property (T@"<CBDigitizerNodeProtocol>",R,N,V_source) source;
@property (TQ,R,N) coexState;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CBDigitizerFilter loadTouchProperties:];
```

## Instance methods

```
-[CBDigitizerFilter setIsActive:];
-[CBDigitizerFilter setProperty:forKey:];
-[CBDigitizerFilter orientation];
-[CBDigitizerFilter dealloc];
-[CBDigitizerFilter filterEvent:];
-[CBDigitizerFilter handleALSEvent:];
-[CBDigitizerFilter description];
-[CBDigitizerFilter isActive];
-[CBDigitizerFilter source];
-[CBDigitizerFilter handleDigitizerEvent:];
-[CBDigitizerFilter coexState];
-[CBDigitizerFilter handleALSEventInternal:];
-[CBDigitizerFilter handleSourceEvent:];
-[CBDigitizerFilter initWithALSNode:source:andLogCategory:];
-[CBDigitizerFilter isObstructed];
-[CBDigitizerFilter isObstructedAndActive];
-[CBDigitizerFilter newHospotForLocationX:andY:];
-[CBDigitizerFilter newHotspot];
-[CBDigitizerFilter newHotspotForOrientation];
-[CBDigitizerFilter overrideHotspotWithCenterX:andCenterY:];
-[CBDigitizerFilter setTriggered:forHotspot:];
```
