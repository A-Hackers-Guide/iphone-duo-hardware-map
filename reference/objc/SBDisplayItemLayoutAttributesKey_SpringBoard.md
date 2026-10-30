# `SBDisplayItemLayoutAttributesKey`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 3 instance variables, 3 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"SBDisplayItem" _displayItem;
q _displayOrdinal;
q _orientation;
```

## Properties

```
@property (T@"SBDisplayItem",R,N,V_displayItem) displayItem;
@property (Tq,R,N,V_displayOrdinal) displayOrdinal;
@property (Tq,R,N,V_orientation) orientation;
```

## Class methods

```
+[SBDisplayItemLayoutAttributesKey keyFromProtobufRepresentation:];
```

## Instance methods

```
-[SBDisplayItemLayoutAttributesKey displayOrdinal];
-[SBDisplayItemLayoutAttributesKey orientation];
-[SBDisplayItemLayoutAttributesKey protobufRepresentation];
-[SBDisplayItemLayoutAttributesKey displayItem];
-[SBDisplayItemLayoutAttributesKey hash];
-[SBDisplayItemLayoutAttributesKey description];
-[SBDisplayItemLayoutAttributesKey copyWithZone:];
-[SBDisplayItemLayoutAttributesKey isEqual:];
-[SBDisplayItemLayoutAttributesKey initWithDisplayItem:displayOrdinal:orientation:];
-[SBDisplayItemLayoutAttributesKey metadataDescription];
```
