# `MTLSAnimatablePathCollection`

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/Frameworks/MTLSpline.framework/MTLSpline`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__Frameworks__MTLSpline.framework__MTLSpline.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 3 properties, 8 instance methods, 0 class methods

## Instance variables

```
{vector<ControlPoint, std::allocator<ControlPoint>>="__begin_"^{ControlPoint}"__end_"^{ControlPoint}""{?="__cap_"^{ControlPoint}}} _controlPointStateVector;
@"NSMutableDictionary" _paths;
@"MTLSPath" _defaultPath;
^{ControlPoint=f} _controlPointState;
```

## Properties

```
@property (T@"NSMutableDictionary",R,V_paths) paths;
@property (T@"MTLSPath",R,V_defaultPath) defaultPath;
@property (T^{ControlPoint=f},N,V_controlPointState) controlPointState;
```

## Instance methods

```
-[MTLSAnimatablePathCollection paths];
-[MTLSAnimatablePathCollection removePath:];
-[MTLSAnimatablePathCollection defaultPath];
-[MTLSAnimatablePathCollection setPath:forKey:];
-[MTLSAnimatablePathCollection initWithDefaultPath:];
-[MTLSAnimatablePathCollection blendPath:withPath:byAmount:];
-[MTLSAnimatablePathCollection controlPointState];
-[MTLSAnimatablePathCollection setControlPointState:];
```
