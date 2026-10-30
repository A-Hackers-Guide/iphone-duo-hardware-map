# `CBColorSample`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 9 properties, 24 instance methods, 0 class methods

## Instance variables

```
d _lux;
d _CCT;
Q _mode;
Q _type;
{?="x"d"y"d} _xy;
{?="X"d"Y"d"Z"d} _XYZ;
```

## Properties

```
@property (Td,R,N,V_lux) lux;
@property (T{?=dd},R,N,V_xy) xy;
@property (T{?=ddd},R,N,V_XYZ) XYZ;
@property (T{?=ddd},R,N) Lab;
@property (Td,R,N,V_CCT) CCT;
@property (Tq,R,N) colorBin;
@property (T{CFXColorSample=[3f]{?=ff}f{?=i[6f]if}},R,N) colorSample;
@property (TQ,N,V_mode) mode;
@property (TQ,N,V_type) type;
```

## Instance methods

```
-[CBColorSample init];
-[CBColorSample setMode:];
-[CBColorSample setType:];
-[CBColorSample type];
-[CBColorSample colorSample];
-[CBColorSample mode];
-[CBColorSample description];
-[CBColorSample lux];
-[CBColorSample initWithHIDEvent:];
-[CBColorSample CCT];
-[CBColorSample CCTDifferenceWith:];
-[CBColorSample Lab];
-[CBColorSample XYZ];
-[CBColorSample LuxDifferenceWith:];
-[CBColorSample setXYZ:];
-[CBColorSample colorBin];
-[CBColorSample colorDeltaEWith:];
-[CBColorSample copyDataInDictionary];
-[CBColorSample fillInChromaticity];
-[CBColorSample fillInTristimulus];
-[CBColorSample initWithChromaticity:illuminance:andTempterature:];
-[CBColorSample initWithTristimulus:illuminance:andTempterature:];
-[CBColorSample setXy:];
-[CBColorSample xy];
```
