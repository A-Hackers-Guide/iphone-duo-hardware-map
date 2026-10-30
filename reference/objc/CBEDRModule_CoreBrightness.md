# `CBEDRModule`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBModule`
- Protocols: `CBContainerModuleProtocol`, `CBHIDServiceProtocol`
- 13 instance variables, 4 properties, 16 instance methods, 0 class methods

## Instance variables

```
f _currentLux;
f _currentNits;
f _maxNits;
f _Ycomp;
f _prevLux;
f _prevNits;
f _prevMaxNits;
f _prevYcomp;
@"CADisplay" _cadisplay;
@"CBDisplayModuleHID" _displayModule;
@"<CBContainerModuleProtocol>" _colorModule;
@"NSMutableArray" _filters;
@"NSMutableArray" _alsNodes;
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
-[CBEDRModule copyPropertyForKey:];
-[CBEDRModule setProperty:forKey:];
-[CBEDRModule handleEvent:];
-[CBEDRModule addHIDServiceClient:];
-[CBEDRModule removeHIDServiceClient:];
-[CBEDRModule stop];
-[CBEDRModule dealloc];
-[CBEDRModule start];
-[CBEDRModule handleNotificationForKey:withProperty:];
-[CBEDRModule handleALSEvent:];
-[CBEDRModule copyPropertyForKey:withParameter:];
-[CBEDRModule handleEventInternal:];
-[CBEDRModule handleBrightnessUpdate:];
-[CBEDRModule handleTargetWhitepointUpdate:];
-[CBEDRModule initWithQueue:display:colorModule:andDisplayModule:];
-[CBEDRModule updateEDRState];
```
