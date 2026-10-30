# `_IntArray2D`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 3 properties, 12 instance methods, 1 class methods

## Instance variables

```
^q _arrayData;
Q _iSize;
Q _jSize;
B _shouldBoundsCheck;
```

## Properties

```
@property (TQ,R,N,V_iSize) iSize;
@property (TQ,R,N,V_jSize) jSize;
@property (TB,N,V_shouldBoundsCheck) shouldBoundsCheck;
```

## Class methods

```
+[_IntArray2D arrayWithISize:jSize:];
```

## Instance methods

```
-[_IntArray2D dealloc];
-[_IntArray2D description];
-[_IntArray2D ::];
-[_IntArray2D ::outOfBoundsReturnValue:];
-[_IntArray2D ::newValue:];
-[_IntArray2D assertBoundsForIIndex:jIndex:];
-[_IntArray2D iSize];
-[_IntArray2D inBoundsForIIndex:jIndex:];
-[_IntArray2D initWithISize:jSize:];
-[_IntArray2D jSize];
-[_IntArray2D setShouldBoundsCheck:];
-[_IntArray2D shouldBoundsCheck];
```
