# `ICDocCamRenamePrompt`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UITextFieldDelegate`
- 3 instance variables, 7 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSString" _existingTitle;
@"UIAlertAction" _saveAction;
@"ICDocCamRenamePrompt" _strongSelf;
```

## Properties

```
@property (T@"NSString",C,N,V_existingTitle) existingTitle;
@property (T@"UIAlertAction",&,N,V_saveAction) saveAction;
@property (T@"ICDocCamRenamePrompt",&,N,V_strongSelf) strongSelf;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[ICDocCamRenamePrompt textField:shouldChangeCharactersInRange:replacementString:];
-[ICDocCamRenamePrompt textFieldChanged:];
-[ICDocCamRenamePrompt setStrongSelf:];
-[ICDocCamRenamePrompt strongSelf];
-[ICDocCamRenamePrompt isTitleValid:error:];
-[ICDocCamRenamePrompt initWithExistingTitle:];
-[ICDocCamRenamePrompt showFromViewController:completion:];
-[ICDocCamRenamePrompt enableAction:withString:];
-[ICDocCamRenamePrompt existingTitle];
-[ICDocCamRenamePrompt saveAction];
-[ICDocCamRenamePrompt setExistingTitle:];
-[ICDocCamRenamePrompt setSaveAction:];
-[ICDocCamRenamePrompt showSingleButtonAlertFromViewController:withTitle:message:];
-[ICDocCamRenamePrompt stringByScrubbingStringForCollectionName:];
```
