# `SBApplicationDropSession`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 12 properties, 22 instance methods, 13 class methods

## Instance variables

```
@"NSObject<OS_dispatch_group>" _activationSettingsGroup;
B _notificationDrag;
B _windowTearOff;
@"SBActivationSettings" _activationSettings;
@"SBApplication" _application;
@"FBSSceneIdentity" _sceneIdentity;
@"<UIDragDropSession>" _uiDragDropSession;
@"UIDraggingSystemSession" _systemSession;
@"SBSAppDragLocalContext" _localContext;
@"NSSet" _launchActions;
@"NSString" _targetContentIdentifier;
```

## Properties

```
@property (T@"FBSSceneIdentity",&,N,V_sceneIdentity) sceneIdentity;
@property (T@"NSString",C,N,V_targetContentIdentifier) targetContentIdentifier;
@property (T@"SBApplication",R,N,V_application) application;
@property (T@"<UIDragDropSession>",R,N,V_uiDragDropSession) uiDragDropSession;
@property (T@"UIDraggingSystemSession",R,N,V_systemSession) systemSession;
@property (Tq,R,N) dropZones;
@property (TB,R,N,GisNotificationDrag,V_notificationDrag) notificationDrag;
@property (TB,R,N,GisWindowTearOff,V_windowTearOff) windowTearOff;
@property (T@"SBSAppDragLocalContext",R,N,V_localContext) localContext;
@property (T@"SBActivationSettings",R,N,V_activationSettings) activationSettings;
@property (T@"NSSet",R,N,V_launchActions) launchActions;
@property (TB,R,N) allowsCommandeering;
```

## Class methods

```
+[SBApplicationDropSession _applicationForHandlingDragItem:URL:error:];
+[SBApplicationDropSession _applicationForIconLeafIdentifier:];
+[SBApplicationDropSession _applicationProxyForIdentifiers:forURL:passingTest:error:];
+[SBApplicationDropSession _dragItemRepresentsAcceptableFileDrag:];
+[SBApplicationDropSession _getFileDropSessionWithUIDragDropSession:dragItem:systemSession:targetApplication:completion:];
+[SBApplicationDropSession _getLocalAppDropSessionWithUIDragDropSession:dragItem:systemSession:completion:];
+[SBApplicationDropSession _getURLDropSessionWithUIDragDropSession:dragItem:systemSession:targetApplication:completion:];
+[SBApplicationDropSession _getUserActivityDropSessionWithUIDragDropSession:dragItem:systemSession:targetApplication:completion:];
+[SBApplicationDropSession _getUserNotificationDropSessionWithUIDragDropSession:systemSession:dragItem:completion:];
+[SBApplicationDropSession _itemProviderRequiresOpenInPlace:];
+[SBApplicationDropSession canHandleUIDragDropSession:];
+[SBApplicationDropSession dropSessionWithWindowUIDragSession:];
+[SBApplicationDropSession getDropSessionWithUIDropSession:sceneProvider:defaultToSourceApplication:completion:];
```

## Instance methods

```
-[SBApplicationDropSession targetContentIdentifier];
-[SBApplicationDropSession setTargetContentIdentifier:];
-[SBApplicationDropSession application];
-[SBApplicationDropSession setSceneIdentity:];
-[SBApplicationDropSession launchActions];
-[SBApplicationDropSession sceneIdentity];
-[SBApplicationDropSession localContext];
-[SBApplicationDropSession _initWithUIDragDropSession:application:targetContentIdentifier:];
-[SBApplicationDropSession isWindowTearOff];
-[SBApplicationDropSession _activityContinuationActionFromActivity:activityData:];
-[SBApplicationDropSession _isApplicationBoundToVisibleIcon];
-[SBApplicationDropSession activationSettings];
-[SBApplicationDropSession allowsCommandeering];
-[SBApplicationDropSession calculateSceneIdentityWithSceneProvider:completion:];
-[SBApplicationDropSession dropZones];
-[SBApplicationDropSession initWithUIDragDropSession:systemSession:application:activity:activityData:];
-[SBApplicationDropSession initWithUIDragDropSession:systemSession:application:targetContentIdentifier:];
-[SBApplicationDropSession initWithUIDragDropSession:systemSession:application:targetContentIdentifier:URL:requiresOpenInPlace:];
-[SBApplicationDropSession initWithUIDragDropSession:systemSession:application:targetContentIdentifier:localContext:activity:activityData:];
-[SBApplicationDropSession isNotificationDrag];
-[SBApplicationDropSession systemSession];
-[SBApplicationDropSession uiDragDropSession];
```
