# `CBALSService`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBHIDService`
- 9 instance variables, 8 properties, 15 instance methods, 0 class methods

## Instance variables

```
B _validData;
d _lux;
B _colorSupport;
d _x;
d _y;
d _CCT;
@"NSString" _desc;
Q _location;
Q _placement;
```

## Properties

```
@property (TB,R,V_validData) validData;
@property (Td,R,V_lux) lux;
@property (TB,R,V_colorSupport) colorSupport;
@property (Td,R,V_x) x;
@property (Td,R,V_y) y;
@property (Td,R,V_CCT) CCT;
@property (TQ,R,V_location) location;
@property (TQ,R,V_placement) placement;
```

## Instance methods

```
-[CBALSService setEvent:];
-[CBALSService placement];
-[CBALSService y];
-[CBALSService location];
-[CBALSService colorSupport];
-[CBALSService dealloc];
-[CBALSService x];
-[CBALSService description];
-[CBALSService lux];
-[CBALSService CCT];
-[CBALSService updateEventData];
-[CBALSService copyDataInDictionary];
-[CBALSService initWithHIDALSServiceClient:];
-[CBALSService resetEventData];
-[CBALSService validData];
```
