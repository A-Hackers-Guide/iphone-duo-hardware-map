# `PKDrawingPowerSavingController`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 0 properties, 1 instance methods, 0 class methods

## Instance variables

```
{vector<double, std::allocator<double>>="__begin_"^d"__end_"^d""{?="__cap_"^d}} _movementDistanceHistoryBuffer;
{CGPoint="x"d"y"d} _previousDrawingLocation;
d _currentMovement;
d _accumulatedMovement;
d _previousRenderTimestamp;
B _valid;
B _isDrawingWithPencil;
B _isDrawingWithMarkerOrEraser;
```

## Instance methods

```
-[PKDrawingPowerSavingController init];
```
