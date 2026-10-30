# `PKStrokeDelta`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"_PKStrokeConcrete" _deltaStroke;
@"PKStrokePath" _deltaStrokeData;
@"NSUUID" _strokeUUID;
```

## Properties

```
@property (T@"_PKStrokeConcrete",&,N,V_deltaStroke) deltaStroke;
@property (T@"PKStrokePath",&,N,V_deltaStrokeData) deltaStrokeData;
@property (T@"NSUUID",&,N,V_strokeUUID) _strokeUUID;
```

## Instance methods

```
-[PKStrokeDelta dataRepresentation];
-[PKStrokeDelta initWithData:error:];
-[PKStrokeDelta initWithArchive:error:];
-[PKStrokeDelta saveToArchive:];
-[PKStrokeDelta description];
-[PKStrokeDelta _strokeUUID];
-[PKStrokeDelta deltaStrokeData];
-[PKStrokeDelta setDeltaStroke:];
-[PKStrokeDelta set_strokeUUID:];
-[PKStrokeDelta deltaStroke];
-[PKStrokeDelta setDeltaStrokeData:];
```
