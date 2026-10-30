# `AVVCPluginRemoteInputHost`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVAudioRemoteInputPluginDelegate`
- 2 instance variables, 1 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray<AVAudioRemoteInputPlugin>" mPlugins;
@"AVVoiceController" _mMotherController;
```

## Properties

```
@property (T@"AVVoiceController",W,N,V_mMotherController) mMotherController;
```

## Instance methods

```
-[AVVCPluginRemoteInputHost init];
-[AVVCPluginRemoteInputHost dealloc];
-[AVVCPluginRemoteInputHost inputPlugin:didUnpublishDevice:];
-[AVVCPluginRemoteInputHost allBundles:];
-[AVVCPluginRemoteInputHost findDeviceWithIdentifier:];
-[AVVCPluginRemoteInputHost findFirstBluetoothDevice];
-[AVVCPluginRemoteInputHost inputPlugin:didPublishDevice:];
-[AVVCPluginRemoteInputHost invalidatePlugins];
-[AVVCPluginRemoteInputHost mMotherController];
-[AVVCPluginRemoteInputHost mockPluginEndpoint];
-[AVVCPluginRemoteInputHost setMMotherController:];
-[AVVCPluginRemoteInputHost setParentVoiceController:];
```
