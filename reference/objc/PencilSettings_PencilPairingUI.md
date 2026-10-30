# `PencilSettings`

- Image: [`/System/Library/PrivateFrameworks/PencilPairingUI.framework/PencilPairingUI`](../userland/System__Library__PrivateFrameworks__PencilPairingUI.framework__PencilPairingUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 13 instance methods, 2 class methods

## Instance variables

```
q _preferredTapAction;
q _preferredSqueezeAction;
```

## Properties

```
@property (Tq,N,V_preferredTapAction) preferredTapAction;
@property (Tq,N,V_preferredSqueezeAction) preferredSqueezeAction;
```

## Class methods

```
+[PencilSettings pencilUserDefaults];
+[PencilSettings sharedPencilSettings];
```

## Instance methods

```
-[PencilSettings observeValueForKeyPath:ofObject:change:context:];
-[PencilSettings init];
-[PencilSettings preferredTapAction];
-[PencilSettings preferredSqueezeAction];
-[PencilSettings loadSettings];
-[PencilSettings _dispatchWithErrorHandler:successHandler:];
-[PencilSettings _postPencilSettingsDidChangeRemoteNotification];
-[PencilSettings daemonQueue];
-[PencilSettings setAutoRefineEnabled:];
-[PencilSettings migrateObsoletedAXOpaqueTouchSetting];
-[PencilSettings setPreferredSqueezeAction:];
-[PencilSettings setPreferredTapAction:];
-[PencilSettings syncSettingsToBackboard];
```
