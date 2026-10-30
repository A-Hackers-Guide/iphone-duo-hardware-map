# `MLMultiArrayView`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MLMultiArray`
- 1 instance variables, 1 properties, 4 instance methods, 3 class methods

## Instance variables

```
@"MLMultiArray" _parent;
```

## Properties

```
@property (T@"MLMultiArray",R,N,V_parent) parent;
```

## Class methods

```
+[MLMultiArrayView isSqueezableShape:];
+[MLMultiArrayView isSqueezableShape:dimensions:];
+[MLMultiArrayView squeezeShape:strides:resultingShape:resultingStrides:];
```

## Instance methods

```
-[MLMultiArrayView initSqueezingMultiArray:dimensions:error:];
-[MLMultiArrayView parent];
-[MLMultiArrayView initSlicingMultiArray:origin:shape:squeeze:error:];
-[MLMultiArrayView initExpandingDimensionsOfMultiArray:axis:];
```
