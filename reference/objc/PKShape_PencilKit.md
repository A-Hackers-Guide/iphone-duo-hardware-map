# `PKShape`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 4 properties, 5 instance methods, 2 class methods

## Instance variables

```
q _type;
@"NSArray" _strokes;
@"PKStroke" _originalStroke;
```

## Properties

```
@property (Tq,R,N,V_type) type;
@property (T@"NSArray",R,N,V_strokes) strokes;
@property (T@"PKStroke",R,N,V_originalStroke) originalStroke;
@property (TB,R,N) fillable;
```

## Class methods

```
+[PKShape isFillableForShapeType:];
+[PKShape snapToShapeActionNameForNumShapes:];
```

## Instance methods

```
-[PKShape type];
-[PKShape strokes];
-[PKShape fillable];
-[PKShape initWithShapeType:strokes:originalStroke:];
-[PKShape originalStroke];
```
