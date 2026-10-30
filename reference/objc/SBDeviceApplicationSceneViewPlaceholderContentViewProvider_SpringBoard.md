# `SBDeviceApplicationSceneViewPlaceholderContentViewProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBUserInterfaceStyleForDisplayConfigurationProvider`, `SBScenePlaceholderContentViewProvider`
- 2 instance variables, 5 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"<SBUserInterfaceStyleForDisplayConfigurationProvider>" _userInterfaceStyleForDisplayConfigurationProvider;
@"<SBScenePlaceholderContentViewProviderDelegate>" _delegate;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<SBScenePlaceholderContentViewProviderDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[SBDeviceApplicationSceneViewPlaceholderContentViewProvider initWithApplication:];
-[SBDeviceApplicationSceneViewPlaceholderContentViewProvider dealloc];
-[SBDeviceApplicationSceneViewPlaceholderContentViewProvider setDelegate:];
-[SBDeviceApplicationSceneViewPlaceholderContentViewProvider delegate];
-[SBDeviceApplicationSceneViewPlaceholderContentViewProvider sceneView:requestsPlaceholderContentViewWithContext:];
-[SBDeviceApplicationSceneViewPlaceholderContentViewProvider _loadLiveXIBViewForApplication:];
-[SBDeviceApplicationSceneViewPlaceholderContentViewProvider _checkApplicationRestorationState:useSnapshot:];
-[SBDeviceApplicationSceneViewPlaceholderContentViewProvider _contentTypeToSearchFromSceneHandle:withContext:];
-[SBDeviceApplicationSceneViewPlaceholderContentViewProvider _contentViewFromSceneHandle:displayConfiguration:orientation:snapshot:size:statusBarDescriptor:hasOrientationMismatchForClassicApp:customContainerBounds:compatibilityContentContainer:];
-[SBDeviceApplicationSceneViewPlaceholderContentViewProvider _initWithApplication:userInterfaceStyleForDisplayConfigurationProvider:];
-[SBDeviceApplicationSceneViewPlaceholderContentViewProvider _naturalSizeForOrientation:referenceSize:];
-[SBDeviceApplicationSceneViewPlaceholderContentViewProvider _snapshotsDidChange:];
-[SBDeviceApplicationSceneViewPlaceholderContentViewProvider userInterfaceStyleForDisplayConfiguration:];
```
