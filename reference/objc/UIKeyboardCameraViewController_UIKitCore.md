# `UIKeyboardCameraViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `UIKeyboardCameraRemoteViewControllerHost`
- 4 instance variables, 8 properties, 18 instance methods, 5 class methods

## Instance variables

```
@"<UIKeyboardCameraViewControllerDelegate>" _delegate;
@"NSString" _textContentType;
@"NSExtension" _extension;
@"UIKeyboardCameraRemoteViewController" _remoteViewController;
```

## Properties

```
@property (T@"NSExtension",&,N,V_extension) extension;
@property (T@"UIKeyboardCameraRemoteViewController",&,N,V_remoteViewController) remoteViewController;
@property (T@"<UIKeyboardCameraViewControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"NSString",N,V_textContentType) textContentType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIKeyboardCameraViewController isEnabled];
+[UIKeyboardCameraViewController isLiveTextEnabled];
+[UIKeyboardCameraViewController isSupportedByDevice];
+[UIKeyboardCameraViewController isCameraRestricted];
+[UIKeyboardCameraViewController _updateIsCameraRestricted];
```

## Instance methods

```
-[UIKeyboardCameraViewController setTextContentType:];
-[UIKeyboardCameraViewController _backgroundColorForModalFormSheet];
-[UIKeyboardCameraViewController init];
-[UIKeyboardCameraViewController remoteViewController];
-[UIKeyboardCameraViewController viewDidLoad];
-[UIKeyboardCameraViewController _canShowWhileLocked];
-[UIKeyboardCameraViewController setDelegate:];
-[UIKeyboardCameraViewController delegate];
-[UIKeyboardCameraViewController setRemoteViewController:];
-[UIKeyboardCameraViewController viewDidDisappear:];
-[UIKeyboardCameraViewController initWithCoder:];
-[UIKeyboardCameraViewController extension];
-[UIKeyboardCameraViewController textContentType];
-[UIKeyboardCameraViewController setExtension:];
-[UIKeyboardCameraViewController keyboardCameraDidAccept];
-[UIKeyboardCameraViewController keyboardCameraDidCancel];
-[UIKeyboardCameraViewController keyboardCameraDidUpdateString:];
-[UIKeyboardCameraViewController prepareWithCompletion:];
```
