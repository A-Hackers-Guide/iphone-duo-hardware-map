# `BTShareAudioViewController`

- Image: [`/System/Library/PrivateFrameworks/BluetoothServicesUI.framework/BluetoothServicesUI`](../userland/System__Library__PrivateFrameworks__BluetoothServicesUI.framework__BluetoothServicesUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UINavigationController`
- 6 instance variables, 6 properties, 27 instance methods, 1 class methods

## Instance variables

```
I _flags;
@? _completion;
@"BTShareAudioSessionClient" _shareAudioSession;
@"NSBundle" _mainBundle;
@"UIStoryboard" _mainStoryboard;
@"BTShareAudioConnectingViewController" _vcConnecting;
```

## Properties

```
@property (T@"BTShareAudioSessionClient",&,N,V_shareAudioSession) shareAudioSession;
@property (T@"NSBundle",&,N,V_mainBundle) mainBundle;
@property (T@"UIStoryboard",&,N,V_mainStoryboard) mainStoryboard;
@property (T@"BTShareAudioConnectingViewController",&,N,V_vcConnecting) vcConnecting;
@property (T@?,C,N,V_completion) completion;
@property (TI,N,V_flags) flags;
```

## Class methods

```
+[BTShareAudioViewController instantiateViewController];
```

## Instance methods

```
-[BTShareAudioViewController mainBundle];
-[BTShareAudioViewController setCompletion:];
-[BTShareAudioViewController completion];
-[BTShareAudioViewController setFlags:];
-[BTShareAudioViewController flags];
-[BTShareAudioViewController viewWillDisappear:];
-[BTShareAudioViewController viewWillAppear:];
-[BTShareAudioViewController setMainBundle:];
-[BTShareAudioViewController reportError:];
-[BTShareAudioViewController _sessionStart];
-[BTShareAudioViewController _reportCompletion:mediaRouteID:];
-[BTShareAudioViewController _showBringClose];
-[BTShareAudioViewController _sessionProgressEvent:info:];
-[BTShareAudioViewController _showConfirm:];
-[BTShareAudioViewController _showConnecting:];
-[BTShareAudioViewController _showError:];
-[BTShareAudioViewController _showPairInstructions:];
-[BTShareAudioViewController _transitionToViewController:animate:];
-[BTShareAudioViewController mainStoryboard];
-[BTShareAudioViewController reportUserCancelled];
-[BTShareAudioViewController setMainStoryboard:];
-[BTShareAudioViewController setShareAudioSession:];
-[BTShareAudioViewController setVcConnecting:];
-[BTShareAudioViewController shareAudioSession];
-[BTShareAudioViewController vcConnecting];
-[BTShareAudioViewController _imageForPID:colorCode:];
-[BTShareAudioViewController _moviePathForPID:colorCode:];
```
