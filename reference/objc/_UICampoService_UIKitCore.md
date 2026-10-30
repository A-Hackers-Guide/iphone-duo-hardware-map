# `_UICampoService`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIPopoverPresentationControllerDelegate`, `UIAdaptivePresentationControllerDelegate`
- 3 instance variables, 1 properties, 16 instance methods, 4 class methods

## Instance variables

```
$__lazy_storage_$_campoService;
nextIdentifier;
activePopoverSessions;
```

## Properties

```
@property (T@"_TtC13CampoServices14CampoUIService",N,&) campoService;
```

## Class methods

```
+[_UICampoService sharedService];
+[_UICampoService lightweightUICollapsedPillHeight];
+[_UICampoService campoAlwaysUsesPadding];
+[_UICampoService lightweightUIContentHeight];
```

## Instance methods

```
-[_UICampoService adaptivePresentationStyleForPresentationController:traitCollection:];
-[_UICampoService traitCollectionFrom:presentationSourceItem:];
-[_UICampoService presentationControllerWillDismiss:];
-[_UICampoService presentationControllerDidDismiss:];
-[_UICampoService init];
-[_UICampoService viewFrom:];
-[_UICampoService campoService];
-[_UICampoService setCampoService:];
-[_UICampoService resolvedConfigurationFrom:sender:presentationSourceItem:];
-[_UICampoService viewFromPresentationSourceItem:];
-[_UICampoService launchCampoWithConfiguration:sessionDelegate:sender:];
-[_UICampoService sceneFrom:presentationSourceItem:];
-[_UICampoService isLaunchAllowedForSender:];
-[_UICampoService resolvedAssistantType:];
-[_UICampoService launchCampoWithConfiguration:sessionDelegate:sender:presenterConfiguration:presentationSourceItem:];
-[_UICampoService presenterIDFrom:sender:presentationSourceItem:];
```
