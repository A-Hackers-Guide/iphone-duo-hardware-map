# `UIVideoEditorController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UINavigationController`
- 3 instance variables, 4 properties, 27 instance methods, 1 class methods

## Instance variables

```
i _previousStatusBarStyle;
@"NSMutableDictionary" _properties;
{?="visible"b1"isCleaningUp"b1"didRevertStatusBar"b1} _flags;
```

## Properties

```
@property (T@"<UINavigationControllerDelegate><UIVideoEditorControllerDelegate>",D,N) delegate;
@property (T@"NSString",C,N) videoPath;
@property (Td,N) videoMaximumDuration;
@property (Tq,N) videoQuality;
```

## Class methods

```
+[UIVideoEditorController canEditVideoAtPath:];
```

## Instance methods

```
-[UIVideoEditorController videoQuality];
-[UIVideoEditorController setVideoQuality:];
-[UIVideoEditorController editVideoViewControllerDidCancel:];
-[UIVideoEditorController init];
-[UIVideoEditorController viewWillDisappear:];
-[UIVideoEditorController _setValue:forProperty:];
-[UIVideoEditorController _properties];
-[UIVideoEditorController editVideoViewController:didTrimVideoWithOptions:];
-[UIVideoEditorController viewWillAppear:];
-[UIVideoEditorController viewDidDisappear:];
-[UIVideoEditorController _setProperties:];
-[UIVideoEditorController _autoDismiss];
-[UIVideoEditorController _createInitialController];
-[UIVideoEditorController _didRevertStatusBar];
-[UIVideoEditorController _initializeProperties];
-[UIVideoEditorController _isSupportedInterfaceOrientation:];
-[UIVideoEditorController _removeAllChildren];
-[UIVideoEditorController _setVideoURL:];
-[UIVideoEditorController _setupControllers];
-[UIVideoEditorController _valueForProperty:];
-[UIVideoEditorController _videoURL];
-[UIVideoEditorController editVideoViewController:didFailWithError:];
-[UIVideoEditorController setVideoMaximumDuration:];
-[UIVideoEditorController setVideoPath:];
-[UIVideoEditorController videoMaximumDuration];
-[UIVideoEditorController videoPath];
-[UIVideoEditorController viewWillUnload];
```
