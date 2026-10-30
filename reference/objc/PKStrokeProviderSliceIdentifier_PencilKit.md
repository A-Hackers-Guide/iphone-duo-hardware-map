# `PKStrokeProviderSliceIdentifier`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CHStrokeIdentifier`
- 3 instance variables, 7 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NSUUID" _strokeUUID;
d _tStart;
d _tEnd;
```

## Properties

```
@property (T@"NSUUID",R,N,V_strokeUUID) strokeUUID;
@property (Td,R,N,V_tStart) tStart;
@property (Td,R,N,V_tEnd) tEnd;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PKStrokeProviderSliceIdentifier supportsSecureCoding];
```

## Instance methods

```
-[PKStrokeProviderSliceIdentifier encodeWithCoder:];
-[PKStrokeProviderSliceIdentifier hash];
-[PKStrokeProviderSliceIdentifier initWithCoder:];
-[PKStrokeProviderSliceIdentifier copyWithZone:];
-[PKStrokeProviderSliceIdentifier isEqual:];
-[PKStrokeProviderSliceIdentifier initWithUUID:tStart:tEnd:];
-[PKStrokeProviderSliceIdentifier strokeUUID];
-[PKStrokeProviderSliceIdentifier tEnd];
-[PKStrokeProviderSliceIdentifier tStart];
```
