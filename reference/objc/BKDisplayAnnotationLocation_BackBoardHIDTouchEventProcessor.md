# `BKDisplayAnnotationLocation`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`](../userland/System__Library__PrivateFrameworks__BackBoardHIDTouchEventProcessor.framework__BackBoardHIDTouchEventProcessor.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 5 instance variables, 5 properties, 12 instance methods, 5 class methods

## Instance variables

```
B _inhibitRotation;
B _shouldAutoposition;
B _definedInReferenceSpace;
{CGPoint="x"d"y"d} _superBias;
{CGPoint="x"d"y"d} _point;
```

## Properties

```
@property (TB,N,V_inhibitRotation) inhibitRotation;
@property (TB,N,V_shouldAutoposition) shouldAutoposition;
@property (T{CGPoint=dd},N,V_superBias) superBias;
@property (T{CGPoint=dd},N,V_point) point;
@property (TB,N,V_definedInReferenceSpace) definedInReferenceSpace;
```

## Class methods

```
+[BKDisplayAnnotationLocation centerAtPoint:];
+[BKDisplayAnnotationLocation controlledBySupernode];
+[BKDisplayAnnotationLocation relativeToBottomLeftOfSuper:];
+[BKDisplayAnnotationLocation relativeToBottomMiddleOfSuper:];
+[BKDisplayAnnotationLocation relativeToTopLeftOfSuper:];
```

## Instance methods

```
-[BKDisplayAnnotationLocation point];
-[BKDisplayAnnotationLocation copyWithZone:];
-[BKDisplayAnnotationLocation isEqual:];
-[BKDisplayAnnotationLocation setPoint:];
-[BKDisplayAnnotationLocation inhibitRotation];
-[BKDisplayAnnotationLocation definedInReferenceSpace];
-[BKDisplayAnnotationLocation setDefinedInReferenceSpace:];
-[BKDisplayAnnotationLocation setInhibitRotation:];
-[BKDisplayAnnotationLocation setShouldAutoposition:];
-[BKDisplayAnnotationLocation setSuperBias:];
-[BKDisplayAnnotationLocation shouldAutoposition];
-[BKDisplayAnnotationLocation superBias];
```
