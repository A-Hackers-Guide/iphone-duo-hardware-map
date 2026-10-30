# `SRAmbientLightSample`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampleDirectExporting`, `NSSecureCoding`, `SRSampling`, `NSCopying`
- 3 instance variables, 9 properties, 18 instance methods, 2 class methods

## Instance variables

```
q _comboTypePlacement;
f _luxValue;
{?="x"f"y"f} _chromaticity;
```

## Properties

```
@property (T@"NSString",R,C) typeString;
@property (T@"NSString",R,C) placementString;
@property (Tq,R) placement;
@property (T{?=ff},R,V_chromaticity) chromaticity;
@property (T@"NSMeasurement",R,C) lux;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SRAmbientLightSample supportsSecureCoding];
+[SRAmbientLightSample initialize];
```

## Instance methods

```
-[SRAmbientLightSample placement];
-[SRAmbientLightSample dealloc];
-[SRAmbientLightSample encodeWithCoder:];
-[SRAmbientLightSample description];
-[SRAmbientLightSample initWithCoder:];
-[SRAmbientLightSample typeString];
-[SRAmbientLightSample lux];
-[SRAmbientLightSample copyWithZone:];
-[SRAmbientLightSample initWithSample:];
-[SRAmbientLightSample binarySampleRepresentation];
-[SRAmbientLightSample initWithBinarySampleRepresentation:metadata:timestamp:];
-[SRAmbientLightSample sr_dictionaryRepresentation];
-[SRAmbientLightSample sr_prefersUTF8StringRepresentation];
-[SRAmbientLightSample sr_writeUTF8RepresentationToOutputStream:];
-[SRAmbientLightSample placementString];
-[SRAmbientLightSample chipType];
-[SRAmbientLightSample chromaticity];
-[SRAmbientLightSample initWithSRALSSampleStruct:];
```
