# `AUAudioUnitExtensionHostViewController`

- Image: [`/System/Library/Frameworks/CoreAudioKit.framework/CoreAudioKit`](../userland/System__Library__Frameworks__CoreAudioKit.framework__CoreAudioKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_EXHostViewController`
- Protocols: `_EXHostViewControllerDelegate`, `AUAudioUnitExtensionHostViewControllerInterface`
- 3 instance variables, 6 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"UIViewController" _auViewController;
@"NSXPCConnection" _connection;
@? _didBeginHostingCallback;
```

## Properties

```
@property (T@"NSXPCConnection",&,N,V_connection) connection;
@property (T@?,C,N,V_didBeginHostingCallback) didBeginHostingCallback;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AUAudioUnitExtensionHostViewController _containedRemoteViewController];
-[AUAudioUnitExtensionHostViewController dealloc];
-[AUAudioUnitExtensionHostViewController initWithConfiguration:];
-[AUAudioUnitExtensionHostViewController viewWillAppear:];
-[AUAudioUnitExtensionHostViewController connection];
-[AUAudioUnitExtensionHostViewController setConnection:];
-[AUAudioUnitExtensionHostViewController viewDidDisappear:];
-[AUAudioUnitExtensionHostViewController addChildViewController:];
-[AUAudioUnitExtensionHostViewController hostViewControllerDidActivate:];
-[AUAudioUnitExtensionHostViewController hostViewControllerWillDeactivate:error:];
-[AUAudioUnitExtensionHostViewController determineViewSize:];
-[AUAudioUnitExtensionHostViewController didBeginHostingCallback];
-[AUAudioUnitExtensionHostViewController initWithConfiguration:completion:];
-[AUAudioUnitExtensionHostViewController markViewForRedraw:];
-[AUAudioUnitExtensionHostViewController resizeWindow:size:];
-[AUAudioUnitExtensionHostViewController setAUContainerViewConstraints:childView:auViewSize:];
-[AUAudioUnitExtensionHostViewController setDidBeginHostingCallback:];
```
