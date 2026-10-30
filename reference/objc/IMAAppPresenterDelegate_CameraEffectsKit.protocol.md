# `IMAAppPresenterDelegate` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `IMAStickerTarget`
- 0 instance variables, 3 properties, 9 instance methods, 0 class methods

## Properties

```
@property (T@"UIViewController",R,N) dockPresentationViewController;
@property (TB,?,R,N) expandedAppShouldDismissOnDragSuccess;
@property (T{CGSize=dd},?,R,N) expandedAppViewControllerSize;
```

## Instance methods

```
-[IMAAppPresenterDelegate dockPresentationViewController];
-[IMAAppPresenterDelegate didSelectAppWithBundleIdentifier:];
-[IMAAppPresenterDelegate appPresenterCardDidDismiss:];
-[IMAAppPresenterDelegate appPresenterDidDismissFullscreenModal:];
-[IMAAppPresenterDelegate didSelectAppWithBundleIdentifier:type:];
-[IMAAppPresenterDelegate dismissExpandedAppViewController:animated:completion:];
-[IMAAppPresenterDelegate expandedAppShouldDismissOnDragSuccess];
-[IMAAppPresenterDelegate expandedAppViewControllerSize];
-[IMAAppPresenterDelegate presentExpandedAppViewController:animated:completion:];
```
