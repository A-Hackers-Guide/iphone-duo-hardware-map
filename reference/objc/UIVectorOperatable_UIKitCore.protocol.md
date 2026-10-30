# `UIVectorOperatable` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`, `NSCopying`
- 0 instance variables, 0 properties, 11 instance methods, 2 class methods

## Class methods

```
+[UIVectorOperatable epsilonCompatibleWithVector:];
+[UIVectorOperatable zeroCompatibleWithVector:];
```

## Instance methods

```
-[UIVectorOperatable copy];
-[UIVectorOperatable isUndefined];
-[UIVectorOperatable isCompatibleWith:];
-[UIVectorOperatable addVector:];
-[UIVectorOperatable getValue];
-[UIVectorOperatable integrateWithVelocity:target:intermediateTarget:intermediateTargetVelocity:parameters:state:delta:];
-[UIVectorOperatable interpolateTo:progress:];
-[UIVectorOperatable isApproximatelyEqualTo:withinEpsilon:];
-[UIVectorOperatable multiplyByScalar:];
-[UIVectorOperatable multiplyByVector:];
-[UIVectorOperatable reinitWithVector:];
```
