# `JFXRemoteCommandServer`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 29 instance methods, 0 class methods

## Instance variables

```
@"<JFXRemoteCommandServerDelegate>" _delegate;
@"NSDistributedNotificationCenter" _distributedNotificationCenter;
```

## Properties

```
@property (T@"<JFXRemoteCommandServerDelegate>",W,N,V_delegate) delegate;
@property (T@"NSDistributedNotificationCenter",&,N,V_distributedNotificationCenter) distributedNotificationCenter;
```

## Instance methods

```
-[JFXRemoteCommandServer initWithDelegate:];
-[JFXRemoteCommandServer distributedNotificationCenter];
-[JFXRemoteCommandServer setDelegate:];
-[JFXRemoteCommandServer delegate];
-[JFXRemoteCommandServer setDistributedNotificationCenter:];
-[JFXRemoteCommandServer onAddAREffectWithIdentifierNotification:];
-[JFXRemoteCommandServer onAddEffectWithIdentifierNotification:];
-[JFXRemoteCommandServer onAddEffectWithNameNotification:];
-[JFXRemoteCommandServer onAddPosterWithIdentifierNotification:];
-[JFXRemoteCommandServer onAddPosterWithNameNotification:];
-[JFXRemoteCommandServer onAddShapeWithIdentifierNotification:];
-[JFXRemoteCommandServer onAddStickerNotification:];
-[JFXRemoteCommandServer onAddStickerWithIdentifierNotification:];
-[JFXRemoteCommandServer onAddTextNotification:];
-[JFXRemoteCommandServer onExportProjectNotification:];
-[JFXRemoteCommandServer onExportProjectResponseNotification:];
-[JFXRemoteCommandServer onGetEffectsRequest:];
-[JFXRemoteCommandServer onGetEffectsResponse:];
-[JFXRemoteCommandServer onNewProjectNotification:];
-[JFXRemoteCommandServer onOpenProjectNotification:];
-[JFXRemoteCommandServer onOpenProjectPickerNotification:];
-[JFXRemoteCommandServer onPlayClipAtIndexNotification:];
-[JFXRemoteCommandServer onPlayNotification:];
-[JFXRemoteCommandServer onRecordNotification:];
-[JFXRemoteCommandServer onRemoveEffectsNotification:];
-[JFXRemoteCommandServer onSetAnimojiNotification:];
-[JFXRemoteCommandServer onSetAspectRatioNotification:];
-[JFXRemoteCommandServer onSetFilterWithIdentifierNotification:];
-[JFXRemoteCommandServer onSetMemojiWithContentsOfFileNotification:];
```
