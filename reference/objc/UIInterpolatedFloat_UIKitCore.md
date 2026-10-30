# `UIInterpolatedFloat`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIVectorOperatable`
- 1 instance variables, 5 properties, 13 instance methods, 3 class methods

## Instance variables

```
d _number;
```

## Properties

```
@property (Td,R,N) value;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIInterpolatedFloat valueWithFloat:];
+[UIInterpolatedFloat epsilonCompatibleWithVector:];
+[UIInterpolatedFloat zeroCompatibleWithVector:];
```

## Instance methods

```
-[UIInterpolatedFloat debugDescription];
-[UIInterpolatedFloat value];
-[UIInterpolatedFloat isUndefined];
-[UIInterpolatedFloat copyWithZone:];
-[UIInterpolatedFloat isCompatibleWith:];
-[UIInterpolatedFloat addVector:];
-[UIInterpolatedFloat getValue];
-[UIInterpolatedFloat integrateWithVelocity:target:intermediateTarget:intermediateTargetVelocity:parameters:state:delta:];
-[UIInterpolatedFloat interpolateTo:progress:];
-[UIInterpolatedFloat isApproximatelyEqualTo:withinEpsilon:];
-[UIInterpolatedFloat multiplyByScalar:];
-[UIInterpolatedFloat multiplyByVector:];
-[UIInterpolatedFloat reinitWithVector:];
```
