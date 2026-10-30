# `PKVectorTimestamp`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `CHStrokeProviderVersion`
- 1 instance variables, 4 properties, 25 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _clock;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PKVectorTimestamp supportsSecureCoding];
```

## Instance methods

```
-[PKVectorTimestamp init];
-[PKVectorTimestamp mergeWithTimestamp:];
-[PKVectorTimestamp shortDescription];
-[PKVectorTimestamp sortedUUIDs];
-[PKVectorTimestamp compareTo:];
-[PKVectorTimestamp initWithArchive:];
-[PKVectorTimestamp isEmpty];
-[PKVectorTimestamp encodeWithCoder:];
-[PKVectorTimestamp serialize];
-[PKVectorTimestamp hash];
-[PKVectorTimestamp saveToArchive:];
-[PKVectorTimestamp description];
-[PKVectorTimestamp initWithCoder:];
-[PKVectorTimestamp initWithData:];
-[PKVectorTimestamp copyWithZone:];
-[PKVectorTimestamp isEqual:];
-[PKVectorTimestamp allUUIDs];
-[PKVectorTimestamp clockElementForUUID:];
-[PKVectorTimestamp clockForUUID:];
-[PKVectorTimestamp incrementClockForUUID:];
-[PKVectorTimestamp setClock:forUUID:];
-[PKVectorTimestamp setClock:subclock:forUUID:];
-[PKVectorTimestamp subclockForUUID:];
-[PKVectorTimestamp compareClock:subclock:forUUID:];
-[PKVectorTimestamp unionClock:subclock:forUUID:];
```
