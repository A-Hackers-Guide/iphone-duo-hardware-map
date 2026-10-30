# `_UITextFormattingSceneHostingImpl`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UISceneHostingControllerDelegate`, `_UITextFormattingRemoteViewControllerHost`, `_UITextFormattingViewHostingImpl`
- 2 instance variables, 6 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"_UISceneHostingController" _hostingController;
@"UITextFormattingViewController" delegateTextFormattingViewController;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UITextFormattingViewController",W,N,VdelegateTextFormattingViewController) delegateTextFormattingViewController;
@property (T@"<_UIRemoteSheet>",R,N) _remoteSheet;
```

## Instance methods

```
-[_UITextFormattingSceneHostingImpl clientIsReady];
-[_UITextFormattingSceneHostingImpl setupSceneHosting];
-[_UITextFormattingSceneHostingImpl _remoteSheet];
-[_UITextFormattingSceneHostingImpl _presentColorPicker:selectedColor:];
-[_UITextFormattingSceneHostingImpl _presentFontPickerWithConfiguration:selectedFonts:];
-[_UITextFormattingSceneHostingImpl _presentTypographySettingsForFont:];
-[_UITextFormattingSceneHostingImpl _textFormattingDidChangeValue:textAttributesData:];
-[_UITextFormattingSceneHostingImpl _textFormattingDidFinish];
-[_UITextFormattingSceneHostingImpl delegateTextFormattingViewController];
-[_UITextFormattingSceneHostingImpl setDelegateTextFormattingViewController:];
-[_UITextFormattingSceneHostingImpl setRemoteConfiguration:];
-[_UITextFormattingSceneHostingImpl setRemoteFormattingDescriptor:];
-[_UITextFormattingSceneHostingImpl setupRemoteHosting];
```
