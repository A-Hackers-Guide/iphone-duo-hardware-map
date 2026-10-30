# `_UIColorPickerSceneHostingImpl`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UISceneHostingControllerDelegate`, `_UIColorPickerViewProvidingDelegate`, `_UIColorPickerViewHostingImpl`
- 3 instance variables, 6 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"_UISceneHostingController" _hostingController;
@"<BSInvalidatable>" _foregroundAssertion;
@"UIColorPickerViewController" delegateColorPickerViewController;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIColorPickerViewController",W,N,VdelegateColorPickerViewController) delegateColorPickerViewController;
@property (T@"<_UIRemoteSheet>",R,N) _remoteSheet;
```

## Instance methods

```
-[_UIColorPickerSceneHostingImpl clientIsReady];
-[_UIColorPickerSceneHostingImpl dealloc];
-[_UIColorPickerSceneHostingImpl _remoteSheet];
-[_UIColorPickerSceneHostingImpl _pickerDidDismissEyedropper];
-[_UIColorPickerSceneHostingImpl _pickerDidFinish];
-[_UIColorPickerSceneHostingImpl _pickerDidFloatEyedropper];
-[_UIColorPickerSceneHostingImpl _pickerDidSelectColor:colorSpace:isVolatile:];
-[_UIColorPickerSceneHostingImpl _pickerDidShowEyedropper];
-[_UIColorPickerSceneHostingImpl delegateColorPickerViewController];
-[_UIColorPickerSceneHostingImpl dismissEyedropper:];
-[_UIColorPickerSceneHostingImpl setDelegateColorPickerViewController:];
-[_UIColorPickerSceneHostingImpl setRemoteConfiguration:];
-[_UIColorPickerSceneHostingImpl setRemoteSelectedColor:];
-[_UIColorPickerSceneHostingImpl setupRemoteHosting];
```
