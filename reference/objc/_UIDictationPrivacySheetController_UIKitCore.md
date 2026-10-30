# `_UIDictationPrivacySheetController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UINavigationController`
- 4 instance variables, 4 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"<_UIDictationPrivacySheetControllerDelegate>" _privacyDelegate;
@"OBPrivacyPresenter" _privacyPresenter;
q _sheetType;
@"VTUIDictationDataSharingOptInPresenter" _dataSharingOptInPresenter;
```

## Properties

```
@property (T@"<_UIDictationPrivacySheetControllerDelegate>",N,V_privacyDelegate) privacyDelegate;
@property (T@"OBPrivacyPresenter",&,N,V_privacyPresenter) privacyPresenter;
@property (Tq,N,V_sheetType) sheetType;
@property (T@"VTUIDictationDataSharingOptInPresenter",&,N,V_dataSharingOptInPresenter) dataSharingOptInPresenter;
```

## Instance methods

```
-[_UIDictationPrivacySheetController setPresentationDelegate:];
-[_UIDictationPrivacySheetController dismiss];
-[_UIDictationPrivacySheetController initWithType:];
-[_UIDictationPrivacySheetController _canShowWhileLocked];
-[_UIDictationPrivacySheetController privacyDelegate];
-[_UIDictationPrivacySheetController dataSharingOptInPresenter];
-[_UIDictationPrivacySheetController privacyPresenter];
-[_UIDictationPrivacySheetController setDataSharingOptInPresenter:];
-[_UIDictationPrivacySheetController setPrivacyDelegate:];
-[_UIDictationPrivacySheetController setPrivacyPresenter:];
-[_UIDictationPrivacySheetController setSheetType:];
-[_UIDictationPrivacySheetController sheetType];
```
