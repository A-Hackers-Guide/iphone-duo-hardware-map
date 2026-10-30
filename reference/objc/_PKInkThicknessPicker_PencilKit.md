# `_PKInkThicknessPicker`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIControl`
- 7 instance variables, 1 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _cachedSortedWeights;
d _weight;
@"NSArray" _sortedWeights;
@"UIColor" _buttonTintColorOverride;
@"NSDictionary" _weightsToButtonImages;
@"NSArray" _thicknessButtons;
{CGSize="width"d"height"d} _buttonSize;
```

## Properties

```
@property (T@"NSArray",&,N,V_thicknessButtons) thicknessButtons;
```

## Class methods

```
+[_PKInkThicknessPicker sizeWithButtonCount:buttonSize:];
```

## Instance methods

```
-[_PKInkThicknessPicker layoutSubviews];
-[_PKInkThicknessPicker buttonTapped:];
-[_PKInkThicknessPicker sizeThatFits:];
-[_PKInkThicknessPicker setThicknessButtons:];
-[_PKInkThicknessPicker thicknessButtons];
```
