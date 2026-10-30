# `CAMSystemMenuController`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 10 properties, 15 instance methods, 0 class methods

## Instance variables

```
? menuControllerDelegate;
```

## Properties

```
@property (T@"<CAMSystemMenuControllerDelegate>",N,W,VmenuControllerDelegate) menuControllerDelegate;
@property (T@"UIMenu",N,R) cameraRollMenu;
@property (T@"UIMenu",N,R) captureMenu;
@property (T@"UIMenu",N,R) captureModeMenu;
@property (T@"UIMenu",N,R) flashModeMenu;
@property (T@"UIMenu",N,R) flipCameraMenu;
@property (T@"UIMenu",N,R) livePhotoModeMenu;
@property (T@"UIMenu",N,R) timerMenu;
@property (T@"UICommand",N,R) cameraSettingsCommand;
@property (T@"NSString",N,R) captureMenuOptionSymbolName;
```

## Instance methods

```
-[CAMSystemMenuController init];
-[CAMSystemMenuController captureModeMenu];
-[CAMSystemMenuController cameraRollMenu];
-[CAMSystemMenuController cameraSettingsCommand];
-[CAMSystemMenuController captureMenu];
-[CAMSystemMenuController captureMenuOptionSymbolName];
-[CAMSystemMenuController flashModeMenu];
-[CAMSystemMenuController flipCameraMenu];
-[CAMSystemMenuController installCameraMenuCommandsWithBuilder:];
-[CAMSystemMenuController livePhotoModeMenu];
-[CAMSystemMenuController menuControllerDelegate];
-[CAMSystemMenuController setMenuControllerDelegate:];
-[CAMSystemMenuController timerMenu];
-[CAMSystemMenuController validateCameraMenuCommand:];
-[CAMSystemMenuController valueForCommand:];
```
