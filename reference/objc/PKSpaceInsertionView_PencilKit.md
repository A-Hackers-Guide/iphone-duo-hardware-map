# `PKSpaceInsertionView`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 6 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
^{CGPath=} _lassoPath;
{CGPoint="x"d"y"d} _handleLocation;
d _scale;
@"PKDrawingAdjustmentKnob" _knobHandle;
B _isDragging;
Q _insertionType;
```

## Properties

```
@property (TQ,N,V_insertionType) insertionType;
@property (TB,N,V_isDragging) isDragging;
```

## Instance methods

```
-[PKSpaceInsertionView setIsDragging:];
-[PKSpaceInsertionView dealloc];
-[PKSpaceInsertionView drawRect:];
-[PKSpaceInsertionView layoutSubviews];
-[PKSpaceInsertionView isDragging];
-[PKSpaceInsertionView pointInside:withEvent:];
-[PKSpaceInsertionView insertionType];
-[PKSpaceInsertionView setInsertionType:];
-[PKSpaceInsertionView initWithFrame:insertionType:path:handleLocation:scale:];
```
