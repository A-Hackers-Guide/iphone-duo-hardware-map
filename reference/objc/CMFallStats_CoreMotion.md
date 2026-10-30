# `CMFallStats`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampleExporting`, `SRSampling`, `NSSecureCoding`
- 4 instance variables, 11 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"NSData" _data;
B _isNearFall;
i _fallType;
d _iOStime;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Td,R,N,V_iOStime) iOStime;
@property (Ti,R,N,V_fallType) fallType;
@property (TB,R,N,V_isNearFall) isNearFall;
```

## Class methods

```
+[CMFallStats supportsSecureCoding];
```

## Instance methods

```
-[CMFallStats dealloc];
-[CMFallStats encodeWithCoder:];
-[CMFallStats description];
-[CMFallStats initWithCoder:];
-[CMFallStats initWithData:];
-[CMFallStats iOStime];
-[CMFallStats initWithBufferAndLength:length:];
-[CMFallStats _decodeMeta];
-[CMFallStats binarySampleRepresentation];
-[CMFallStats fallType];
-[CMFallStats initWithBinarySampleRepresentation:metadata:timestamp:];
-[CMFallStats isNearFall];
-[CMFallStats itemsIterator];
-[CMFallStats sr_exportRepresentationEnumerator];
```
