# `BKSDisplayArrangementItem`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 4 properties, 11 instance methods, 1 class methods

## Instance variables

```
I _edge;
@"NSString" _displayUUID;
@"NSString" _relativeDisplayUUID;
d _offset;
```

## Properties

```
@property (T@"NSString",R,C,N,V_displayUUID) displayUUID;
@property (T@"NSString",R,C,N,V_relativeDisplayUUID) relativeDisplayUUID;
@property (TI,R,N,V_edge) edge;
@property (Td,R,N,V_offset) offset;
```

## Class methods

```
+[BKSDisplayArrangementItem supportsSecureCoding];
```

## Instance methods

```
-[BKSDisplayArrangementItem edge];
-[BKSDisplayArrangementItem displayUUID];
-[BKSDisplayArrangementItem appendDescriptionToFormatter:];
-[BKSDisplayArrangementItem encodeWithCoder:];
-[BKSDisplayArrangementItem hash];
-[BKSDisplayArrangementItem description];
-[BKSDisplayArrangementItem initWithCoder:];
-[BKSDisplayArrangementItem isEqual:];
-[BKSDisplayArrangementItem offset];
-[BKSDisplayArrangementItem initWithDisplayUUID:relativeToDisplayUUID:alongEdge:atOffset:];
-[BKSDisplayArrangementItem relativeDisplayUUID];
```
