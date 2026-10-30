# `CAMInterfaceModulationView`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 4 instance variables, 4 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"UIView" _hostingView;
Q _interfaceModulation;
@"CAFilter" __modulationFilter;
Q __inFlightAnimationCount;
```

## Properties

```
@property (T@"CAFilter",&,N,S_setModulationFilter:,V__modulationFilter) _modulationFilter;
@property (TQ,N,S_setInFlightAnimationCount:,V__inFlightAnimationCount) _inFlightAnimationCount;
@property (T@"UIView",R,W,N,V_hostingView) hostingView;
@property (TQ,N,V_interfaceModulation) interfaceModulation;
```

## Instance methods

```
-[CAMInterfaceModulationView didAddSubview:];
-[CAMInterfaceModulationView _setInFlightAnimationCount:];
-[CAMInterfaceModulationView hitTest:withEvent:];
-[CAMInterfaceModulationView hostingView];
-[CAMInterfaceModulationView initWithHostingView:];
-[CAMInterfaceModulationView _updateModulationLayerEnabled];
-[CAMInterfaceModulationView _modulationFilter];
-[CAMInterfaceModulationView interfaceModulation];
-[CAMInterfaceModulationView setInterfaceModulation:animated:];
-[CAMInterfaceModulationView _inFlightAnimationCount];
-[CAMInterfaceModulationView _keyPathForFilterKey:];
-[CAMInterfaceModulationView _setModulationFilter:];
-[CAMInterfaceModulationView setInterfaceModulation:];
-[CAMInterfaceModulationView modulationAnimationDidStop:];
```
