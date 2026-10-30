# `LAPSPasscodeChangeUIPresentationController`

- Image: [`/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI`](../userland/System__Library__Frameworks__LocalAuthenticationEmbeddedUI.framework__LocalAuthenticationEmbeddedUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"UIViewController" _parentVC;
B _parentModalInPresentationOriginalFlag;
@"UIViewController" _rootVC;
@"LACUIContainerViewController" _containerVC;
```

## Instance methods

```
-[LAPSPasscodeChangeUIPresentationController dismissWithCompletion:];
-[LAPSPasscodeChangeUIPresentationController _dismissWithCompletion:];
-[LAPSPasscodeChangeUIPresentationController presentAlertVC:];
-[LAPSPasscodeChangeUIPresentationController _setupParentVCIfNeededAnimated:];
-[LAPSPasscodeChangeUIPresentationController _restoreParentModalInPresentationFlag];
-[LAPSPasscodeChangeUIPresentationController _storeParentModalInPresentationFlag];
-[LAPSPasscodeChangeUIPresentationController initWithParentVC:containerVC:];
-[LAPSPasscodeChangeUIPresentationController presentVC:animated:];
-[LAPSPasscodeChangeUIPresentationController presentVC:transitionStyle:];
```
