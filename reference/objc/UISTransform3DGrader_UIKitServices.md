# `UISTransform3DGrader`

- Image: [`/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices`](../userland/System__Library__PrivateFrameworks__UIKitServices.framework__UIKitServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 0 properties, 13 instance methods, 0 class methods

## Instance variables

```
{vector<double, std::allocator<double>>="__begin_"^d"__end_"^d""{?="__cap_"^d}} _allowedRotations;
{vector<double, std::allocator<double>>="__begin_"^d"__end_"^d""{?="__cap_"^d}} _allowedScales;
d _allowedShear;
d _allowedTranslation;
d _allowedShift;
B _allowHorizontalFlip;
B _allowVerticalFlip;
```

## Instance methods

```
-[UISTransform3DGrader init];
-[UISTransform3DGrader _gradeTransform3D:];
-[UISTransform3DGrader allowHorizontalFlip:];
-[UISTransform3DGrader allowRotations:count:];
-[UISTransform3DGrader allowRotations:count:lowerMultiplier:lowerConstant:upperMultiplier:upperConstant:];
-[UISTransform3DGrader allowScales:count:];
-[UISTransform3DGrader allowScales:count:lowerMultiplier:lowerConstant:upperMultiplier:upperConstant:];
-[UISTransform3DGrader allowShear:];
-[UISTransform3DGrader allowShift:];
-[UISTransform3DGrader allowTranslation:];
-[UISTransform3DGrader allowVerticalFlip:];
-[UISTransform3DGrader gradeStartTransform3D:endTransform3D:];
-[UISTransform3DGrader gradeTransform3D:];
```
